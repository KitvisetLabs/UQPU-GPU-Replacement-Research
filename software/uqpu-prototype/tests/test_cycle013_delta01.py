import copy
import hashlib
import math
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

from uqpu.cycle013_delta01 import (
    LANES, MAX_U64, bind_v4_request, canonical_hash, certify_er6_v3,
    consent_event_13, consent_state_13, cost_interval_13, correlated_priority_sensitivity,
    covariance_certificate_13, custody_chain_13, lineage_v3, publish_atomic_file,
    registered_interval_13, run_cycle013_fixture, verify_v4_request,
    weighted_maxcut_13, zip64_layout_gate,
)


def covariance_fixture():
    names = ["algorithm", "state-prep", "provider", "readout", "retry"]
    entries = [{"left": name, "right": name, "value": 1.0} for name in names]
    entries.append({"left": "state-prep", "right": "provider", "value": 0.1})
    all_pairs = [(names[i], names[j]) for i in range(len(names)) for j in range(i, len(names))]
    zeros = [list(pair) for pair in all_pairs if pair[0] != pair[1] and pair != ("state-prep", "provider")]
    return {"labels": names, "entries": entries, "structural_zero_pairs": zeros}


def unit_registry_fixture():
    return {
        "m": [1, 0, 0, 0, 0, 0, 0],
        "s": [0, 0, 1, 0, 0, 0, 0],
        "m/s": [1, 0, -1, 0, 0, 0, 0],
        "J": [2, 1, -2, 0, 0, 0, 0],
    }


def valid_v4():
    return {
        "schema": "v4", "payload": {"operation": "fixture", "version": 3},
        "token": "token-1", "options": {"priority": "normal"},
        "source_commit": "707750fb4bec7d701d2c6c35f155c3e381c72b00",
    }


def valid_zip64():
    return zip64_layout_gate(
        [(100, 120), (120, 140), (140, 160)], 3, 100, 160,
        160, 216, 216, 236, 258,
    )


def valid_interval(source_bytes):
    return {
        "id": "FND-EQN-013-SYN-01", "lower": [1, 1], "upper": [2, 1],
        "kind": "bounded_interval", "unit": "1", "dimension": [0] * 10,
        "domain_sort": "RealModel",
        "source_locator": "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md:397-412#UMRL-031",
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "evidence": "DECLARATION_ONLY", "provenance": "UMRL-031",
    }


class Cycle013Tests(unittest.TestCase):
    def test_a_positive_graph_and_exact_1024_state_boundary(self):
        graph = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 5), (2, 4, 2), (3, 4, 4)]
        result = weighted_maxcut_13(5, graph)
        self.assertEqual(result["states"], 32)
        self.assertEqual(result["best_cut_weight"], 18)
        self.assertEqual(result["optimal_state_set_sha256"], "9e2fc64b6bf2097f840c11932e2294bc97e4efd47074518004911605c6898e9e")
        self.assertEqual(result["graph_sha256"], "9213eddd3a10d78f584a6f49b23cef3cb66ceac72cec3d3742ddab7585848c4b")
        reordered = [(v, u, w) for u, v, w in reversed(graph)]
        self.assertEqual(result["graph_sha256"], weighted_maxcut_13(5, reordered)["graph_sha256"])
        boundary = weighted_maxcut_13(10, [(0, 1, 1)])
        self.assertEqual(boundary["states"], 1024)
        self.assertEqual(len(boundary["restart_sha256"]), 64)
        with self.assertRaises(ValueError):
            weighted_maxcut_13(11, [(0, 1, 1)])
        with self.assertRaises(ValueError):
            weighted_maxcut_13(2, [(0, 1, 0)])
        with self.assertRaises(ValueError):
            weighted_maxcut_13(10**100, [(0, 1, 1)])
        with self.assertRaises(ValueError):
            weighted_maxcut_13(2, [(0, 1, 1)], cap=True)

    def test_b_canonical_v4_binding_rejects_semantic_or_token_mutation(self):
        body_a = valid_v4()
        body_b = dict(reversed(list(valid_v4().items())))
        bound_a = bind_v4_request(body_a)
        bound_b = bind_v4_request(body_b)
        self.assertEqual(bound_a["binding"], bound_b["binding"])
        self.assertTrue(verify_v4_request(bound_a))
        for field, value in (("payload", {"operation": "changed", "version": 3}), ("token", "token-2")):
            changed = copy.deepcopy(bound_a)
            changed[field] = value
            with self.assertRaises(ValueError):
                verify_v4_request(changed)
        with self.assertRaises(ValueError):
            bind_v4_request({**body_a, "unknown": True})
        with self.assertRaises(ValueError):
            bind_v4_request({**body_a, "payload": {1: "x"}})
        with self.assertRaises(ValueError):
            bind_v4_request({**body_a, "payload": {"value": float("nan")}})
        with self.assertRaises(ValueError):
            bind_v4_request({**body_a, "options": {"value": float("inf")}})

    def test_c_stale_temp_cleanup_and_two_atomic_failure_points(self):
        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            target = root / "payload.bin"
            target.write_bytes(b"old-complete")
            stale = root / ".payload.bin.tmp.stale.old"
            stale.write_bytes(b"partial-old")
            before = publish_atomic_file(root, "payload.bin", b"new-complete", "after_stage_before_replace")
            self.assertEqual(before["visible_bytes"], b"old-complete")
            self.assertEqual(before["stale_temps_removed"], 1)
            self.assertTrue(before["temp_removed"])
            self.assertEqual(before["cache_state"], "UNCONTROLLED")
            after = publish_atomic_file(root, "payload.bin", b"next-complete", "after_replace_before_report")
            self.assertEqual(after["visible_bytes"], b"next-complete")
            self.assertTrue(after["temp_removed"])
            self.assertEqual(after["durability"], "PROCESS_LOCAL_ONLY")

        with tempfile.TemporaryDirectory() as tempdir:
            root = Path(tempdir)
            payloads = [f"complete-{i}".encode() for i in range(24)]
            with ThreadPoolExecutor(max_workers=8) as pool:
                list(pool.map(lambda payload: publish_atomic_file(root, "shared.bin", payload), payloads))
            self.assertIn((root / "shared.bin").read_bytes(), payloads)
            self.assertFalse(any(".tmp.active." in path.name for path in root.iterdir()))

    def test_d_zip64_count_overflow_and_locator_overlap_reject(self):
        self.assertEqual(valid_zip64()["entries"], 3)
        with self.assertRaises(ValueError):
            zip64_layout_gate([], MAX_U64 + 1, 100, 100, 100, 156, 156, 176, 198)
        with self.assertRaises(ValueError):
            zip64_layout_gate(
                [(100, 120), (120, 140), (140, 160)], 3, 100, 160,
                160, 216, 210, 230, 252,
            )
        bad_layouts = [
            ([(100, 120), (121, 140), (140, 160)], 3, 100, 160, 160, 216, 216, 236, 258),
            ([(100, 120), (120, 140), (140, 160)], 3, 100, 160, 160, 161, 161, 181, 203),
            ([(100, 120), (120, 140), (140, 160)], 3, 100, 160, 160, 216, 217, 237, 259),
            ([(False, 120), (120, 140), (140, 160)], 3, 100, 160, 160, 216, 216, 236, 258),
        ]
        for args in bad_layouts:
            with self.subTest(layout=args), self.assertRaises(ValueError):
                zip64_layout_gate(*args)

    def test_e_custody_hashes_bind_authorized_issuer_and_scope(self):
        event = {
            "sample": "synthetic", "from": "vault", "to": "lab", "method": "fixture",
            "unit": "fixture-unit", "expiry": "2030-01-01", "issuer": "issuer-a",
            "scope": "scope-a", "previous": "0" * 64,
        }
        chain = custody_chain_13([event], {"issuer-a": ["scope-a"]}, "2026-09-28")
        self.assertEqual(len(chain[0]), 64)
        for field, value in (("issuer", "issuer-b"), ("scope", "scope-b")):
            changed = dict(event)
            changed[field] = value
            with self.assertRaises(ValueError):
                custody_chain_13([changed], {"issuer-a": ["scope-a"]}, "2026-09-28")
        second = dict(event, **{"from": "lab", "to": "archive", "previous": chain[0]})
        with self.assertRaises(ValueError):
            custody_chain_13([second, event], {"issuer-a": ["scope-a"]}, "2026-09-28")
        wrong_sample = dict(second, sample="sample-B", **{"from": "lab"})
        wrong_sample["previous"] = canonical_hash(event)
        with self.assertRaises(ValueError):
            custody_chain_13([event, wrong_sample], {"issuer-a": ["scope-a"]}, "2026-09-28")
        wrong_path = dict(second, **{"from": "elsewhere"})
        wrong_path["previous"] = canonical_hash(event)
        with self.assertRaises(ValueError):
            custody_chain_13([event, wrong_path], {"issuer-a": ["scope-a"]}, "2026-09-28")
        for expiry in ("yesterday", "2020-01-01"):
            bad_event = dict(event, expiry=expiry)
            with self.assertRaises(ValueError):
                custody_chain_13([bad_event], {"issuer-a": ["scope-a"]}, "2026-09-28")

    def test_f_five_cost_components_need_complete_sparse_covariance(self):
        components = [
            {"name": name, "low": low, "high": high, "unit": "USD"}
            for name, low, high in (
                ("algorithm", 1, 2), ("state-prep", 2, 3), ("provider", 3, 4),
                ("readout", 1, 2), ("retry", 0, 1),
            )
        ]
        covariance = covariance_fixture()
        result = cost_interval_13(components, 2, covariance)
        self.assertEqual(result["component_count"], 5)
        self.assertEqual(result["per_accepted_output_usd"], [3.5, 6.0])
        self.assertEqual(result["evidence_class"], "MODEL_ONLY")
        incomplete = copy.deepcopy(covariance)
        incomplete["structural_zero_pairs"].pop()
        self.assertIsNone(cost_interval_13(components, 2, incomplete))
        self.assertIsNone(cost_interval_13(components, 2, {"labels": list("abcde"), "entries": []}))
        self.assertIsNone(cost_interval_13(components, 0, covariance))
        extreme = copy.deepcopy(covariance)
        extreme["entries"][0]["value"] = 1e308
        extreme["entries"][1]["value"] = 1e308
        pair = ["algorithm", "state-prep"]
        extreme["structural_zero_pairs"].remove(pair)
        extreme["entries"].append({"left": pair[0], "right": pair[1], "value": 1.1e308})
        self.assertIsNone(cost_interval_13(components, 2, extreme))
        overflow_variance = copy.deepcopy(covariance)
        for entry in overflow_variance["entries"]:
            if entry["left"] == entry["right"]:
                entry["value"] = 1e308
        self.assertIsNone(cost_interval_13(components, 2, overflow_variance))

    def test_g_four_measurand_certificate_checks_units_dimensions_order_and_psd(self):
        registry = unit_registry_fixture()
        names = ["distance", "duration", "velocity", "energy"]
        units = ["m", "s", "m/s", "J"]
        dimensions = [registry[u] for u in units]
        matrix = [[1.0 if i == j else 0.0 for j in range(4)] for i in range(4)]
        cert = covariance_certificate_13(
            names, names, units, dimensions, matrix, registry,
            "synthetic-scope", "synthetic-method", "2030-01-01", "2026-09-28",
        )
        self.assertEqual(len(cert["names"]), 4)
        bad_dimensions = copy.deepcopy(dimensions)
        bad_dimensions[2] = registry["s"]
        with self.assertRaises(ValueError):
            covariance_certificate_13(names, names, units, bad_dimensions, matrix, registry, "s", "m", "2030-01-01", "2026-09-28")
        with self.assertRaises(ValueError):
            covariance_certificate_13(names, list(reversed(names)), units, dimensions, matrix, registry, "s", "m", "2030-01-01", "2026-09-28")
        bad_matrix = copy.deepcopy(matrix)
        bad_matrix[0][1] = bad_matrix[1][0] = 2.0
        with self.assertRaises(ValueError):
            covariance_certificate_13(names, names, units, dimensions, bad_matrix, registry, "s", "m", "2030-01-01", "2026-09-28")
        extreme_indefinite = [[1e308, 1.1e308, 0.0, 0.0], [1.1e308, 1e308, 0.0, 0.0],
                              [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0]]
        with self.assertRaises(ValueError):
            covariance_certificate_13(names, names, units, dimensions, extreme_indefinite,
                                      registry, "s", "m", "2030-01-01", "2026-09-28")
        for expires in ("yesterday", "2020-01-01"):
            with self.assertRaises(ValueError):
                covariance_certificate_13(names, names, units, dimensions, matrix,
                                          registry, "s", "m", expires, "2026-09-28")

    def test_h_correlated_held_out_priority_keeps_capital_null(self):
        result = correlated_priority_sensitivity(
            ["provider", "state-prep", "readout"],
            {"provider": 3.0, "state-prep": 2.5, "readout": 1.8},
            [[1.0, 0.6, 0.0], [0.6, 1.0, 0.1], [0.0, 0.1, 1.0]],
            [[0.2, -0.2, 0.1], [-1.0, 1.2, 0.1]],
        )
        self.assertEqual(len(result["heldout_orders"]), 2)
        self.assertGreaterEqual(result["conditional_order_stability"], 0.0)
        self.assertLessEqual(result["conditional_order_stability"], 1.0)
        self.assertIsNone(result["capital"])
        with self.assertRaises(ValueError):
            correlated_priority_sensitivity(
                ["a", "b"], {"a": 1.0, "b": 2.0}, [[1.0, 2.0], [2.0, 1.0]], [[0, 0]],
            )
        with self.assertRaises(ValueError):
            correlated_priority_sensitivity(
                ["z", "a"], {"z": 1e308, "a": 9e307}, [[1.0, 0.0], [0.0, 1.0]],
                [[1e308, 1e308]],
            )

    def test_fnd_eqn_interval_is_rational_and_source_located(self):
        source_bytes = (Path(__file__).resolve().parents[3] / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        entry = valid_interval(source_bytes)
        self.assertEqual(registered_interval_13(entry, source_bytes)["evidence"], "DECLARATION_ONLY")
        bad = dict(entry, source_locator="unlocated")
        with self.assertRaises(ValueError):
            registered_interval_13(bad, source_bytes)
        bad = dict(entry, lower=[3, 1])
        with self.assertRaises(ValueError):
            registered_interval_13(bad, source_bytes)
        for changes in (
            {"id": "made-up"}, {"dimension": [0] * 9 + [1]}, {"unit": "m"},
            {"source_sha256": "a" * 64}, {"domain_sort": "Fiction"},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                registered_interval_13({**entry, **changes}, source_bytes)
        with self.assertRaises(ValueError):
            registered_interval_13(entry, source_bytes + b"changed")

    def test_scm_expiry_replay_revocation_and_new_grant_stay_fictional(self):
        state = consent_state_13()
        state = consent_event_13(state, {
            "action": "grant", "nonce": "grant-1", "consent_id": "old",
            "issued_at": 10, "expires_at": 20,
        }, 10)
        state = consent_event_13(state, {
            "action": "revoke", "nonce": "revoke-1", "consent_id": "old",
            "issued_at": 11, "expires_at": 20,
        }, 11)
        state = consent_event_13(state, {
            "action": "grant", "nonce": "grant-2", "consent_id": "new",
            "issued_at": 12, "expires_at": 30,
        }, 12)
        self.assertEqual(state["active"], {"new": 30})
        self.assertTrue(state["fiction_only"])
        self.assertIsNone(state["empirical_coupling"])
        with self.assertRaises(ValueError):
            consent_event_13(state, {
                "action": "transition", "nonce": "old-transition", "consent_id": "old",
                "issued_at": 13, "expires_at": 20,
            }, 13)
        with self.assertRaises(ValueError):
            consent_event_13(state, {
                "action": "transition", "nonce": "expired", "consent_id": "new",
                "issued_at": 30, "expires_at": 30,
            }, 30)
        with self.assertRaises(ValueError):
            consent_event_13(state, {
                "action": "grant", "nonce": "grant-2", "consent_id": "other",
                "issued_at": 13, "expires_at": 40,
            }, 13)
        with self.assertRaises(ValueError):
            consent_event_13(state, {
                "action": "grant", "nonce": ["unhashable"], "consent_id": "bad",
                "issued_at": 13, "expires_at": 40,
            }, 13)
        with self.assertRaises(ValueError):
            consent_event_13(state, {
                "action": "grant", "nonce": "bool-time", "consent_id": "bad",
                "issued_at": True, "expires_at": 40,
            }, 13)

    def test_ai_cost_third_lineage_version_keeps_disjoint_heldout_splits(self):
        previous = {
            "version": 2, "source_sha256": hashlib.sha256(b"source-v2").hexdigest(),
            "split_hashes": {"train": "a" * 64, "validation": "b" * 64, "test": "c" * 64},
        }
        split_rows = {"train": ["r1", "r2"], "validation": ["r3"], "test": ["r4"]}
        metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
        result = lineage_v3(previous, b"source-v3", split_rows, metrics)
        self.assertEqual(result["version"], 3)
        self.assertEqual(result["parent_source_sha256"], previous["source_sha256"])
        with self.assertRaises(ValueError):
            lineage_v3(previous, b"source-v3", {"train": ["r1"], "validation": ["r2"], "test": ["r2"]}, metrics)
        with self.assertRaises(ValueError):
            lineage_v3(previous, b"source-v3", split_rows, {"train": {"loss": 1}, "validation": {"loss": 1}, "test": {}})
        for bad_previous in (
            {**previous, "source_sha256": "not-a-digest"},
            {**previous, "split_hashes": {**previous["split_hashes"], "train": "bad"}},
            {**previous, "version": True},
        ):
            with self.subTest(previous=bad_previous), self.assertRaises(ValueError):
                lineage_v3(bad_previous, b"source-v3", split_rows, metrics)
        for bad_metrics in (
            {**metrics, "test": {"loss": float("nan")}},
            {**metrics, "test": {"loss": float("inf")}},
            {**metrics, "test": {"loss": -1.0}},
            {**metrics, "test": {"loss": 1.0, "accuracy": 1.0}},
        ):
            with self.subTest(metrics=bad_metrics), self.assertRaises(ValueError):
                lineage_v3(previous, b"source-v3", split_rows, bad_metrics)

    def test_qos_third_certificate_binds_map_parent_and_resource_bounds(self):
        previous = {
            "version": 2, "qubits": 6, "bits": 6, "depth": 18, "gates": 38,
            "source_sha256": hashlib.sha256(b"er6-source-v2-synthetic").hexdigest(),
            "map_sha256": canonical_hash({"map": "v2"}),
        }
        mapping = {"map": "v3", "bounded_subset": "ER6"}
        certificate = {
            "version": 3, "qubits": 6, "bits": 6, "depth": 16, "gates": 34,
            "source_sha256": hashlib.sha256(b"er6-source-v3-synthetic").hexdigest(),
            "map_sha256": canonical_hash(mapping),
            "parent_certificate_sha256": canonical_hash(previous),
        }
        result = certify_er6_v3(previous, certificate, mapping)
        self.assertEqual(result["resource_delta"], {"depth": -2, "gates": -4})
        self.assertEqual(result["resources"], {"qubits": 6, "bits": 6, "depth": 16, "gates": 34})
        self.assertEqual(result["certificate_sha256"], canonical_hash(certificate))
        self.assertEqual(result["parent_certificate_sha256"], certificate["parent_certificate_sha256"])
        self.assertIsNone(result["hardware"])
        with self.assertRaises(ValueError):
            certify_er6_v3(previous, certificate, {**mapping, "map": "mutated"})
        with self.assertRaises(ValueError):
            certify_er6_v3(previous, {**certificate, "depth": 19}, mapping)
        for bad_previous, bad_certificate in (
            ({**previous, "qubits": True}, certificate),
            (previous, {**certificate, "gates": False}),
            (previous, {**certificate, "version": True}),
        ):
            with self.subTest(resources=(bad_previous, bad_certificate)), self.assertRaises(ValueError):
                certify_er6_v3(bad_previous, bad_certificate, mapping)

    def test_cycle_fixture_advances_all_twelve_lanes(self):
        source_bytes = (Path(__file__).resolve().parents[3] / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        result = run_cycle013_fixture(hashlib.sha256(source_bytes).hexdigest(), source_bytes)
        self.assertEqual(set(result), set(LANES))
        self.assertTrue(all(result[lane] is not None for lane in LANES))
        self.assertEqual(result["A"]["cap_boundary"]["states"], 1024)
        self.assertIsNone(result["QOS/QSVT"]["hardware"])


if __name__ == "__main__":
    unittest.main()
