import struct
import tempfile
import unittest
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle018_delta01 import (
    _zip18_records,
    ai_lineage_manifest_v8,
    covariance_block_with_expected_order,
    exact_cancel_expression,
    four_measurand_covariance_order_gate,
    make_receipt_v5,
    maxcut_third_perturbation,
    qos_inverse_operator_pair,
    receipt_v5_mutation_matrix,
    run_cycle018_fixture,
    scm_nonce_replacement_scope_transition,
    stale_stage_exit_collision_gate,
    three_adverse_ranking_alternatives,
    three_component_covariance_sweep,
    verify_receipt_v5,
    zip18_crossbind,
)
from uqpu.cycle014_delta01 import ai_lineage_manifest
from uqpu.cycle016_delta01 import ai_lineage_manifest_v6


class Cycle018Tests(unittest.TestCase):
    def test_a_third_weight_perturbation_keeps_exact_state_and_hash_contract(self):
        result = maxcut_third_perturbation()
        self.assertEqual([row["state_count"] for row in result["variants"]], [1024, 1024, 1024])
        self.assertNotEqual(result["variants"][0]["task_sha256"], result["variants"][1]["task_sha256"])
        self.assertTrue(result["unchanged_edges_invariant"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_receipt_v5_scope_key_request_and_null_invoice_mutations(self):
        result = receipt_v5_mutation_matrix()
        self.assertTrue(all(result["cases"].values()))
        self.assertIsNone(result["missing_external_authority_key_job_invoice"])
        keyring = {"k": b"test-key"}
        request = canonical_hash({"q": "fixture"})
        receipt = make_receipt_v5(request, "fixture-only", "k", keyring["k"])["receipt"]
        self.assertTrue(verify_receipt_v5(receipt, request, "fixture-only", keyring))

    def test_c_stale_stage_exit_cleanup_and_active_name_collision_are_scoped(self):
        with tempfile.TemporaryDirectory() as root:
            result = stale_stage_exit_collision_gate(root, "state.bin", [b"a", b"b", b"c"])
            self.assertEqual(result["process_exit_codes"], [0, 23, 23])
            self.assertTrue(result["live_name_survived_stale_cleanup"])
            self.assertTrue(result["stale_stage_removed_after_exit"])
            self.assertTrue(result["visible_payload_complete"])
            before = sorted(p.name for p in Path(root).iterdir())
            with self.assertRaises(ValueError):
                stale_stage_exit_collision_gate(root, "../state.bin", [b"a", b"b", b"c"])
            self.assertEqual(before, sorted(p.name for p in Path(root).iterdir()))
            self.assertIsNone(result["crash_durability"])

    def test_d_zip64_local_central_name_flags_disk_and_descriptor_mutations_reject(self):
        local, central, descriptor, disks, disk, offset = _zip18_records()
        passed = zip18_crossbind(local, central, descriptor, disks, disk, offset)
        self.assertTrue(passed["cross_bound"])
        self.assertFalse(passed["payload_read"])
        bad_flags = bytearray(local)
        struct.pack_into("<H", bad_flags, 6, 0)
        bad_name = local[:30] + b"wrong.bin"
        bad_descriptor = bytearray(descriptor)
        struct.pack_into("<Q", bad_descriptor, 8, 9)
        for args in [
            (bytes(bad_flags), central, descriptor, disks, disk, offset),
            (bad_name, central, descriptor, disks, disk, offset),
            (local, central, descriptor, disks, disk - 1, offset),
            (local, central, bytes(bad_descriptor), disks, disk, offset),
        ]:
            with self.assertRaises(ValueError):
                zip18_crossbind(*args)

    def test_e_custody_terminal_head_and_reordering_reject(self):
        result = run_cycle018_fixture(b"typed source")["E"]
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(len(result["terminal_event_sha256"]), 64)
        self.assertIsNone(result["physical_sample_claim"])

    def test_f_three_component_model_grid_keeps_bad_covariance_and_zero_null(self):
        result = three_component_covariance_sweep()
        self.assertEqual(result["components"], 3)
        self.assertIsNone(result["scenarios"]["invalid"]["total_usd"])
        self.assertIsNone(result["scenarios"]["nonfinite"]["total_usd"])
        self.assertIsNone(result["scenarios"]["correlated"]["outputs"][3]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_four_measurand_covariance_checks_order_units_symmetry_psd(self):
        result = four_measurand_covariance_order_gate()
        self.assertEqual(result["measurand_order"], ["length", "mass", "duration", "current"])
        self.assertTrue(result["positive_semidefinite"])
        self.assertEqual(result["matrix"][0][1], result["matrix"][1][0])
        self.assertIsNone(result["calibration"])
        items = [
            {"id": "length", "unit": "m", "dimension": [1, 0, 0, 0, 0, 0, 0]},
            {"id": "mass", "unit": "kg", "dimension": [0, 1, 0, 0, 0, 0, 0]},
        ]
        with self.assertRaises(ValueError):
            covariance_block_with_expected_order(items, [], ["mass", "length"])

    def test_h_third_adverse_alternative_expands_finite_grid_and_no_capital(self):
        result = three_adverse_ranking_alternatives()
        self.assertEqual(result["declared_alternatives"], 3)
        self.assertEqual(result["declared_order_count"], 12)
        self.assertEqual(len(result["observed_stability_range"]), 2)
        self.assertIsNone(result["capital"])

    def test_fnd_exact_cancellation_and_source_mismatch(self):
        result = exact_cancel_expression(b"UMRL typed source")
        self.assertEqual(result["speed"]["unit"], "m/s")
        self.assertEqual(result["recovered_length"], {"unit": "m", "lower": [1, 1], "upper": [8, 1]})
        self.assertEqual(result["dimensionless"]["unit"], "1")
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertEqual(result["sort"], ["RealModel", "Model"])

    def test_scm_nonce_replacement_and_scope_transition_stay_in_fiction(self):
        result = scm_nonce_replacement_scope_transition("2026-09-28")
        self.assertTrue(all(result["cases"].values()))
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v8_parent_digest_mutation_and_heldout_deletion_null(self):
        splits = {"train": ["t1"], "validation": ["v1"], "test": ["x1"]}
        metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
        config = {"seed": 18}
        p4 = ai_lineage_manifest(b"source4", splits, metrics, config)
        p5body = {"version": 5, "parent_manifest_sha256": p4["manifest_sha256"], "source_sha256": p4["source_sha256"],
                  "split_hashes": p4["split_hashes"], "metrics_sha256": p4["metrics_sha256"], "config_sha256": p4["config_sha256"],
                  "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
        p5 = {**p5body, "manifest_sha256": canonical_hash(p5body)}
        p6 = ai_lineage_manifest_v6(p5, b"source6", splits, metrics, config)["manifest"]
        p7body = {"version": 7, "parent_manifest_sha256": p6["manifest_sha256"], "source_sha256": p6["source_sha256"],
                  "split_hashes": p6["split_hashes"], "metrics_sha256": p6["metrics_sha256"], "config_sha256": p6["config_sha256"],
                  "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
        p7 = {**p7body, "manifest_sha256": canonical_hash(p7body)}
        candidate = ai_lineage_manifest_v8(p7, b"source8", splits, metrics, config)
        self.assertEqual(candidate["manifest"]["version"], 8)
        self.assertIsNone(candidate["candidate_result"])
        with self.assertRaises(ValueError):
            ai_lineage_manifest_v8({**p7, "manifest_sha256": "0" * 64}, b"source8", splits, metrics, config)
        missing = ai_lineage_manifest_v8(p7, b"source8", splits, {"train": metrics["train"], "validation": metrics["validation"]}, config)
        self.assertIsNone(missing["manifest"])
        self.assertEqual(missing["status"], "NULL_INCOMPLETE_LINEAGE")

    def test_qos_inverse_operator_pair_reconstructs_64_states_with_bound_resources(self):
        result = qos_inverse_operator_pair()
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertTrue(result["resource_regression_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle018_fixture_advances_exactly_twelve_lanes(self):
        root = Path(__file__).resolve().parents[3]
        result = run_cycle018_fixture((root / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes())
        self.assertEqual(set(result), {"A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT"})
        self.assertIsNone(result["B"]["provider_claim"])
        self.assertIsNone(result["AI-COST"]["candidate_result"])


if __name__ == "__main__":
    unittest.main()
