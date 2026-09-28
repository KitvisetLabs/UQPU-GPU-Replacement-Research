import hashlib
import tempfile
import unittest
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import ai_lineage_manifest
from uqpu.cycle016_delta01 import (
    ai_lineage_manifest_v6,
    correlation_stress_fixture,
    cross_unit_covariance_fixture,
    custody_revocation_fork_suite,
    exact_maxcut_10_node,
    rational_interval_divide,
    run_cycle016_fixture,
    same_filesystem_concurrent_replace,
    scm_nonce_scope_matrix,
    synthetic_receipt_v3,
    verify_synthetic_receipt_v3,
    zip64_central_entry_gate,
    qos_mutation_gate,
)


class Cycle016Tests(unittest.TestCase):
    def test_a_exact_1024_state_graph_matches_independent_comparator(self):
        graph = [[0, 1, 4], [0, 3, 7], [0, 6, 2], [1, 2, 5], [1, 5, 3], [2, 3, 6],
                 [2, 7, 4], [3, 4, 8], [4, 5, 2], [4, 8, 5], [5, 6, 7], [6, 7, 3], [7, 8, 6], [8, 9, 4], [2, 9, 1]]
        result = exact_maxcut_10_node(graph)
        self.assertEqual(result["state_count"], 1024)
        self.assertEqual(len(result["task_sha256"]), 64)
        self.assertIsNone(result["scaling_claim"])

    def test_b_synthetic_receipt_binds_scope_key_request_and_null_invoice(self):
        key = b"fixture-only-key"
        request = canonical_hash({"request": "fixture"})
        receipt = synthetic_receipt_v3(request, "fixture-only", "test-key", key)
        self.assertTrue(verify_synthetic_receipt_v3(receipt, request, "fixture-only", "test-key", key))
        self.assertIsNone(receipt["invoice"])
        self.assertIsNone(receipt["job_id"])
        self.assertIsNone(receipt["provider_claim"])
        mutations = [
            {**receipt, "request_sha256": "0" * 64},
            {**receipt, "authorization_scope": "external-provider"},
            {**receipt, "key_id": "other-key"},
            {**receipt, "invoice": {"id": "invented"}},
        ]
        self.assertTrue(all(not verify_synthetic_receipt_v3(x, request, "fixture-only", "test-key", key) for x in mutations))

    def test_b_missing_external_signing_key_keeps_result_null(self):
        result = synthetic_receipt_v3("0" * 64, None, None, None)
        self.assertIsNone(result["receipt"])
        self.assertIsNone(result["provider_claim"])
        self.assertEqual(result["status"], "NULL_MISSING_EXTERNAL_AUTHENTICATION")

    def test_c_same_device_and_concurrent_writers_keep_complete_bytes(self):
        with tempfile.TemporaryDirectory() as temp:
            result = same_filesystem_concurrent_replace(temp, "state.bin", [b"a-whole", b"b-whole", b"c-whole"])
            self.assertTrue(result["device_id_match"])
            self.assertTrue(result["replacement"]["visible_complete"])
            self.assertIsNone(result["crash_durability"])

    def _zip_fixture(self):
        name = b"sample.bin"
        extra_payload = (8).to_bytes(8, "little") + (8).to_bytes(8, "little") + (64).to_bytes(8, "little") + (1).to_bytes(4, "little")
        extra = (1).to_bytes(2, "little") + len(extra_payload).to_bytes(2, "little") + extra_payload
        import struct
        record = struct.pack(
            "<4sHHHHHHIIIHHHHHII", b"PK\x01\x02",
            45, 45, 0, 0, 0, 0,
            0x12345678, 0xFFFFFFFF, 0xFFFFFFFF,
            len(name), len(extra), 0, 0xFFFF, 0,
            0, 0xFFFFFFFF,
        ) + name + extra
        desc = struct.pack("<4sIQQ", b"PK\x07\x08", 0x12345678, 8, 8)
        return record, desc

    def test_d_zip64_directory_entry_and_descriptor_offsets(self):
        record, desc = self._zip_fixture()
        out = zip64_central_entry_gate(record, desc, [128, 256])
        self.assertEqual(out["disk"], 1)
        self.assertEqual(out["local_header_offset"], 64)
        self.assertFalse(out["payload_read"])

    def test_d_rejects_bad_disk_offset_and_descriptor_binding(self):
        record, desc = self._zip_fixture()
        with self.assertRaises(ValueError):
            zip64_central_entry_gate(record, desc, [32, 32])
        with self.assertRaises(ValueError):
            zip64_central_entry_gate(record, desc[:-1] + b"x", [128, 256])

    def test_e_valid_chain_then_revocation_and_fork_reject(self):
        result = custody_revocation_fork_suite("2026-09-28")
        self.assertEqual(result["valid_chain_events"], 3)
        self.assertTrue(result["revoked_issuer_rejected"])
        self.assertTrue(result["fork_rejected"])
        self.assertIsNone(result["physical_sample_claim"])

    def test_f_covariance_stress_keeps_invalid_and_zero_denominators_null(self):
        result = run_cycle016_fixture(b"typed-source") ["F"]
        self.assertEqual(result["scenarios"]["independent"]["outputs"][3]["per_output_usd"], None)
        self.assertIsNone(result["scenarios"]["invalid"]["total_usd"])
        self.assertIsNone(result["scenarios"]["nonfinite"]["total_usd"])
        self.assertEqual(result["evidence_class"], "MODEL_ONLY")

    def test_g_cross_unit_covariance_uses_pairwise_product_dimensions(self):
        result = cross_unit_covariance_fixture()
        self.assertEqual(result["measurand_order"], ["distance", "duration"])
        self.assertEqual(result["matrix"][0][1], result["matrix"][1][0])
        self.assertIsNone(result["calibration"])

    def test_h_correlation_grid_reports_spread_and_null_capital(self):
        result = correlation_stress_fixture()
        self.assertEqual(result["observed_stability_range"], [0.0, 0.5])
        self.assertIsNone(result["capital"])

    def test_fnd_division_preserves_exact_unit_source_sort_and_zero_null(self):
        source = b"UMRL fixture"
        digest = hashlib.sha256(source).hexdigest()
        base = {"domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": digest}
        m = {**base, "unit": "m", "dimension": [1, 0, 0], "lower": [2, 1], "upper": [4, 1]}
        s = {**base, "unit": "s", "dimension": [0, 0, 1], "lower": [2, 1], "upper": [4, 1]}
        registry = {"m|s": {"unit": "m/s", "dimension": [1, 0, -1]}}
        result = rational_interval_divide(m, s, source, registry)
        self.assertEqual(result["result"]["lower"], [1, 2])
        self.assertEqual(result["result"]["upper"], [2, 1])
        zero = rational_interval_divide(m, {**s, "lower": [-1, 1], "upper": [1, 1]}, source, registry)
        self.assertEqual(zero["status"], "NULL_ZERO_CROSSING_DENOMINATOR")
        self.assertIsNone(zero["result"])

    def test_scm_scope_nonce_and_response_mutations_are_fiction_only(self):
        result = scm_nonce_scope_matrix("2026-09-28")
        self.assertEqual(result["cases"]["valid_fiction"], "ACCEPTED_FICTION_ONLY")
        self.assertTrue(all(v == "REJECTED" for k, v in result["cases"].items() if k != "valid_fiction"))
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v6_links_parent_and_returns_null_without_equivalence(self):
        splits = {"train": ["t"], "validation": ["v"], "test": ["x"]}
        metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
        config = {"seed": 1}
        parent4 = ai_lineage_manifest(b"p4", splits, metrics, config)
        parent5 = {"version": 5, "parent_manifest_sha256": parent4["manifest_sha256"], "source_sha256": parent4["source_sha256"],
                   "split_hashes": parent4["split_hashes"], "metrics_sha256": parent4["metrics_sha256"],
                   "config_sha256": parent4["config_sha256"], "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
        parent5["manifest_sha256"] = canonical_hash(parent5)
        candidate = ai_lineage_manifest_v6(parent5, b"source6", splits, metrics, config)
        self.assertEqual(candidate["manifest"]["version"], 6)
        self.assertIsNone(candidate["manifest"]["functional_equivalence"])
        self.assertIsNone(candidate["candidate_result"])
        self.assertNotEqual(candidate, ai_lineage_manifest_v6(parent5, b"changed", splits, metrics, config))
        self.assertNotEqual(candidate, ai_lineage_manifest_v6(parent5, b"source6", {**splits, "train": ["changed"]}, metrics, config))
        self.assertNotEqual(candidate, ai_lineage_manifest_v6(parent5, b"source6", splits, metrics, {"seed": 8}))
        self.assertNotEqual(candidate, ai_lineage_manifest_v6(parent5, b"source6", splits, {**metrics, "test": {"loss": 8.0}}, config))
        self.assertIsNone(ai_lineage_manifest_v6(parent5, None, splits, metrics, config)["manifest"])

    def test_qos_parent_hash_and_resource_regression_mutations_reject(self):
        result = qos_mutation_gate()
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertTrue(result["source_mutation_rejected"])
        self.assertTrue(result["semantic_map_mutation_rejected"])
        self.assertTrue(result["resource_regression_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle016_fixture_advances_all_lanes(self):
        root = Path(__file__).resolve().parents[3]
        fixture = run_cycle016_fixture((root / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes())
        self.assertEqual(set(fixture), {"A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT"})
        self.assertIsNone(fixture["B"]["provider_claim"])


if __name__ == "__main__":
    unittest.main()
