import tempfile
import unittest

from uqpu.cycle024_delta01 import (
    LANES,
    canonical_receipt_adversaries,
    composed_noncommuting_inverse_pairs,
    consent_null_control_table,
    covariance_uncertainty_sweep,
    four_issuer_custody_rotation,
    fourth_graph_perturbation,
    independent_rational_interval,
    leave_one_scenario_out_ranking,
    lineage_manifest_v14,
    process_termination_boundaries,
    run_cycle024_fixture,
    typed_covariance_roundtrip,
    zip64_signature_prefix_gate,
)


class Cycle024Tests(unittest.TestCase):
    def test_a_fourth_graph_perturbation_is_exact_and_deterministic(self):
        result = fourth_graph_perturbation()
        self.assertEqual(result["states"], 2048)
        self.assertEqual(result["objectives"], [10, 11])
        self.assertTrue(result["changed_edge_forced_cut"])
        self.assertTrue(result["unchanged_edge_7_weight_invariant"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_receipt_reordering_is_invariant_and_adversaries_reject(self):
        result = canonical_receipt_adversaries()
        self.assertTrue(result["nested_reordering_invariant"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIn("NFC", result["collision_policy"])
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_process_termination_recovers_only_complete_targets(self):
        with tempfile.TemporaryDirectory() as root:
            result = process_termination_boundaries(root)
        self.assertEqual(len(result["runs"]), 2)
        self.assertTrue(result["all_recovered_complete"])
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23] for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_descriptors_bind_sizes_without_reading_payload(self):
        result = zip64_signature_prefix_gate()
        self.assertEqual(result["descriptor_forms"], ["signed", "unsigned"])
        self.assertTrue(result["size_mutation_rejected"])
        self.assertTrue(result["central_size_mutation_rejected"])
        self.assertFalse(result["signature_like_payload_read"])
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_four_issuer_custody_rotation_fails_closed_at_boundaries(self):
        result = four_issuer_custody_rotation()
        self.assertEqual(result["event_count"], 4)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_covariance_uncertainty_sweep_retains_null_controls(self):
        result = covariance_uncertainty_sweep()
        self.assertEqual(result["components"], 8)
        self.assertEqual(result["sigma_values"], [0.5, 1.0, 2.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            self.assertIsNone(scenarios["correlated"]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_typed_covariance_rescaling_has_exact_inverse(self):
        result = typed_covariance_roundtrip()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["exact_inverse_roundtrip"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_positive_diagonal_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_leave_one_out_grid_is_finite_and_exhaustive(self):
        result = leave_one_scenario_out_ranking()
        self.assertEqual(result["scenario_count"], 8)
        self.assertEqual(result["grid_size"], 192)
        self.assertEqual(sum(result["winner_counts"]), 192)
        self.assertEqual(len(result["leave_one_out_winner_counts"]), 8)
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_rational_interval_roundtrip_is_exact_and_typed(self):
        result = independent_rational_interval(b"cycle024 typed source")
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(result["source_mutation_rejected"])
        self.assertTrue(result["dimension_mutation_rejected"])
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_consent_null_table_stays_fiction_only(self):
        result = consent_null_control_table("2026-09-29")
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 5)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v14_requires_complete_heldout_lineage(self):
        result = lineage_manifest_v14(b"cycle024 synthetic lineage")
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["missing_heldout_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertTrue(result["split_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_composed_pairs_reconstruct_all_64_states(self):
        result = composed_noncommuting_inverse_pairs()
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertTrue(result["noncommuting_order_detected"])
        self.assertEqual(result["resource_bound"], {"gates": 22, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle024_fixture(b"cycle024 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
