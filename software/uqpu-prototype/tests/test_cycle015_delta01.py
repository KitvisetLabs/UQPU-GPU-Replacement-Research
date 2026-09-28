import hashlib
import struct
import tempfile
import unittest
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import ai_lineage_manifest, run_cycle014_fixture
from uqpu.cycle015_delta01 import (
    ai_lineage_manifest_v5,
    component_covariance_sweep,
    concurrent_subprocess_replace,
    correlation_ranking_grid,
    make_custody_event,
    matched_maxcut_seed_family,
    provider_receipt_v2,
    qos_er6_reconstruction_v5,
    rational_interval_composition,
    scm_fictional_rejection_suite,
    typed_covariance_block,
    verify_ai_lineage_manifest_v5,
    verify_custody_chain,
    zip64_multidisk_gate,
)


class Cycle015Tests(unittest.TestCase):
    def test_a_seeded_edge_presentations_keep_exact_task_and_output(self):
        graph = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 5), (2, 4, 2), (3, 4, 4)]
        result = matched_maxcut_seed_family(5, graph, [0, 1, 7, 31], 1024)
        self.assertEqual(result["maximum_states_observed"], 32)
        self.assertEqual({row["result"]["best_cut_weight"] for row in result["rows"]}, {18})
        self.assertEqual(len({row["task_sha256"] for row in result["rows"]}), 1)
        self.assertEqual(len({row["result"]["graph_sha256"] for row in result["rows"]}), 1)
        self.assertIsNone(result["scaling_claim"])

    def test_a_rejects_more_than_the_1024_state_bound(self):
        with self.assertRaises(ValueError):
            matched_maxcut_seed_family(11, [(0, 1, 1)], [0], 1024)

    def test_b_unexecuted_receipt_has_null_authorization_and_signature(self):
        digest = canonical_hash({"request": "fixture"})
        receipt = {"schema": "receipt-v2", "request_sha256": digest, "provider_status": "NOT_EXECUTED",
                   "authorization": None, "signature": None, "job_id": None, "invoice": None}
        out = provider_receipt_v2(digest, receipt)
        self.assertIsNone(out["provider_claim"])
        self.assertIsNone(out["authorization"])
        self.assertIsNone(out["signature"])

    def test_b_rejects_success_or_missing_receipt_fields(self):
        digest = canonical_hash({"request": "fixture"})
        base = {"schema": "receipt-v2", "request_sha256": digest, "provider_status": "NOT_EXECUTED",
                "authorization": None, "signature": None, "job_id": None, "invoice": None}
        with self.assertRaises(ValueError):
            provider_receipt_v2(digest, {**base, "provider_status": "SUCCEEDED"})
        with self.assertRaises(ValueError):
            provider_receipt_v2(digest, {k: v for k, v in base.items() if k != "signature"})

    def test_c_concurrent_writers_publish_only_complete_payloads(self):
        payloads = [b"writer-one-whole", b"writer-two-whole", b"writer-three-whole"]
        with tempfile.TemporaryDirectory() as root:
            result = concurrent_subprocess_replace(root, "state.bin", payloads)
            self.assertTrue(result["active_names_survived_stale_cleanup"])
            self.assertTrue(result["visible_complete"])
            self.assertEqual(result["exit_codes"], [0, 23, 23])
            self.assertIn(result["visible_sha256"], {hashlib.sha256(x).hexdigest() for x in payloads + [b"old-complete-payload"]})
            self.assertEqual(result["durability"], "PROCESS_TERMINATION_ONLY")

    def _zip_fixture(self):
        ext = struct.pack("<HI", 0xCAFE, 2) + b"ok"
        zip64 = struct.pack("<4sQHHIIQQQQ", b"PK\x06\x06", 44 + len(ext), 45, 45, 1, 1, 1, 1, 8, 64) + ext
        locator = struct.pack("<4sIQI", b"PK\x06\x07", 1, 128, 2)
        eocd = struct.pack("<4sHHHHIIH", b"PK\x05\x06", 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 2) + b"ok"
        return zip64, locator, eocd

    def test_d_multi_disk_zip64_sentinels_and_extension(self):
        z, l, e = self._zip_fixture()
        result = zip64_multidisk_gate(z, l, e, 128, 128 + len(z), 128 + len(z) + 20, [256, 256])
        self.assertEqual(result["total_disks"], 2)
        self.assertEqual(result["extension_ids"], [0xCAFE])
        self.assertFalse(result["payload_read"])

    def test_d_rejects_truncated_extension_and_bad_offset(self):
        z, l, e = self._zip_fixture()
        broken = z[:-1]
        with self.assertRaises(ValueError):
            zip64_multidisk_gate(broken, l, e, 128, 128 + len(broken), 128 + len(broken) + 20, [256, 256])
        with self.assertRaises(ValueError):
            zip64_multidisk_gate(z, l, e, 128, 128 + len(z), 128 + len(z) + 20, [256, 150])

    def _events(self):
        sample = hashlib.sha256(b"sample-label").hexdigest()
        entries = [("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer")]
        events, prior = [], "0" * 64
        for i, (issuer, scope) in enumerate(entries):
            event = make_custody_event(i, sample, "path-1", issuer, scope, "2026-01-01", "2027-01-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def test_e_multievent_custody_accepts_registered_issuer_scope_changes(self):
        scopes = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-c": {"transfer"}}
        result = verify_custody_chain(self._events(), scopes, "2026-09-28")
        self.assertEqual(result["event_count"], 3)
        self.assertEqual(result["issuer_sequence"], ["issuer-a", "issuer-b", "issuer-c"])
        self.assertIsNone(result["physical_sample_claim"])

    def test_e_expiry_is_exclusive_and_mutated_chain_fails(self):
        scopes = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-c": {"transfer"}}
        with self.assertRaises(ValueError):
            verify_custody_chain(self._events(), scopes, "2027-01-01")
        events = self._events()
        events[1] = {**events[1], "scope": "outside"}
        with self.assertRaises(ValueError):
            verify_custody_chain(events, scopes, "2026-09-28")

    def test_f_covariance_endpoint_and_output_grid_are_finite_with_nulls(self):
        cov = [[0.0, 0.0], [0.0, 0.0]]
        bad = [[1.0, 2.0], [2.0, 1.0]]
        result = component_covariance_sweep([[1, 2], [3, 4]], {"zero": cov, "bad": bad}, [1, 2, 0])
        self.assertEqual(result["scenarios"]["zero"]["total_usd"], [4.0, 6.0])
        self.assertIsNone(result["scenarios"]["zero"]["outputs"][2]["per_output_usd"])
        self.assertIsNone(result["scenarios"]["bad"]["total_usd"])
        self.assertTrue(all(row["per_output_usd"] is None for row in result["scenarios"]["bad"]["outputs"]))
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_covariance_entries_bind_pairwise_product_dimensions(self):
        dims = [1, 0, 0, 0, 0, 0, 0]
        product_dim = [2, 0, 0, 0, 0, 0, 0]
        item = lambda v: {"value": v, "unit": "m*m", "dimension": product_dim}
        result = typed_covariance_block(
            [{"id": "x", "unit": "m", "dimension": dims}, {"id": "y", "unit": "m", "dimension": dims}],
            [[item(1), item(0.2)], [item(0.2), item(1)]],
        )
        self.assertTrue(result["positive_semidefinite"])
        bad = [[item(1), {**item(0.2), "dimension": dims}], [item(0.2), item(1)]]
        with self.assertRaises(ValueError):
            typed_covariance_block(
                [{"id": "x", "unit": "m", "dimension": dims}, {"id": "y", "unit": "m", "dimension": dims}], bad)

    def test_h_correlation_alternatives_return_finite_grid_range(self):
        out = correlation_ranking_grid(["A", "B"], [
            {"name": "independent", "correlation": [[1, 0], [0, 1]], "scenario_orders": [["A", "B"], ["B", "A"]], "assumption": "test"},
            {"name": "positive", "correlation": [[1, 0.5], [0.5, 1]], "scenario_orders": [["A", "B"], ["A", "B"]], "assumption": "sensitivity"},
        ])
        self.assertEqual(out["observed_stability_range"], [0.5, 1.0])
        self.assertIsNone(out["capital"])

    def test_fnd_exact_add_then_registered_multiply_preserves_source_and_sort(self):
        source = b"canonical typed mathematics fixture"
        sha = hashlib.sha256(source).hexdigest()
        base = {"domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": sha}
        x = {**base, "unit": "m", "dimension": [1, 0, 0], "lower": [1, 2], "upper": [3, 2]}
        y = {**base, "unit": "m", "dimension": [1, 0, 0], "lower": [1, 4], "upper": [1, 2]}
        summed = rational_interval_composition(x, y, "add", source)
        self.assertEqual(summed["lower"], [3, 4])
        t = {**base, "unit": "s", "dimension": [0, 0, 1], "lower": [2, 1], "upper": [3, 1]}
        registry = {"m|s": {"unit": "m*s", "dimension": [1, 0, 1]}}
        product = rational_interval_composition(summed, t, "multiply", source, registry)
        self.assertEqual(product["lower"], [3, 2])
        self.assertEqual(product["upper"], [6, 1])
        with self.assertRaises(ValueError):
            rational_interval_composition(x, t, "add", source)
        with self.assertRaises(ValueError):
            rational_interval_composition(x, y, "add", b"different source")

    def test_scm_revoked_expired_replayed_and_out_of_scope_are_rejected(self):
        result = scm_fictional_rejection_suite("2026-09-28")
        self.assertEqual(set(result["negative_controls"].values()), {"REJECTED"})
        self.assertIsNone(result["empirical_coupling"])

    def _ai_inputs(self):
        splits = {"train": ["t1", "t2"], "validation": ["v1"], "test": ["x1"]}
        metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
        config = {"seed": 0, "epochs": 1}
        parent = ai_lineage_manifest(b"v4-source", splits, metrics, config)
        source = b"v5-source"
        manifest = ai_lineage_manifest_v5(parent, source, splits, metrics, config)
        return parent, source, splits, metrics, config, manifest

    def test_ai_v5_manifest_is_parent_linked_and_mutation_sensitive(self):
        parent, source, splits, metrics, config, result = self._ai_inputs()
        manifest = result["manifest"]
        self.assertEqual(manifest["parent_manifest_sha256"], parent["manifest_sha256"])
        self.assertTrue(verify_ai_lineage_manifest_v5(result, parent, source, splits, metrics, config))
        self.assertFalse(verify_ai_lineage_manifest_v5(result, parent, b"changed", splits, metrics, config))
        self.assertFalse(verify_ai_lineage_manifest_v5(result, parent, source, {**splits, "train": ["changed"]}, metrics, config))
        self.assertFalse(verify_ai_lineage_manifest_v5(result, parent, source, splits, {**metrics, "test": {"loss": 9}}, config))
        self.assertFalse(verify_ai_lineage_manifest_v5(result, parent, source, splits, metrics, {"seed": 5}))
        self.assertIsNone(manifest["functional_equivalence"])
        self.assertIsNone(result["candidate_result"])

    def test_ai_missing_lineage_returns_null_candidate(self):
        parent, _, _, _, _, _ = self._ai_inputs()
        result = ai_lineage_manifest_v5(parent, None, None, None, None)
        self.assertEqual(result["status"], "NULL_MISSING_LINEAGE")
        self.assertIsNone(result["manifest"])
        self.assertIsNone(result["candidate_result"])

    def test_qos_reconstruction_is_bound_to_cycle014_v4_certificate(self):
        parent = run_cycle014_fixture()["QOS/QSVT"]
        gates = [{"op": "x", "target": 0}, {"op": "cx", "control": 0, "target": 1},
                 {"op": "cx", "control": 1, "target": 3}, {"op": "x", "target": 5},
                 {"op": "cx", "control": 3, "target": 4}]
        out = qos_er6_reconstruction_v5(parent, gates)
        self.assertEqual(out["parent_certificate_v4_sha256"], parent["certificate_sha256"])
        self.assertEqual(out["basis_states_checked"], 64)
        self.assertEqual(out["maximum_integer_residual"], 0)
        self.assertIsNone(out["hardware"])


if __name__ == "__main__":
    unittest.main()
