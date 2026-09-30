import tempfile
import unittest

from uqpu.cycle026_delta01 import (
    LANES,
    bounded_numeric_receipt_gate,
    context_bound_consent_controls,
    four_inverse_pairs_order_gate,
    lineage_manifest_v16,
    order_independent_zip64_extras,
    parent_directory_observation,
    run_cycle026_fixture,
    six_issuer_delegation_boundaries,
    sixth_graph_perturbation,
    ten_component_covariance_sweep,
    ten_scenario_deletion_intervals,
    three_source_bound_interval_maps,
    translation_invariant_covariance_transform,
)


class Cycle026Tests(unittest.TestCase):
    def test_a_sixth_graph_perturbation_binds_complement_pairs(self):
        result = sixth_graph_perturbation()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [13, 16])
        self.assertEqual(result["changed_edge_indices"], [5])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertTrue(result["all_witnesses_complement_paired"])
        self.assertEqual(result["complement_pair_count"] * 2, result["witness_counts"][1])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_bounded_numeric_receipts_reject_every_control(self):
        result = bounded_numeric_receipt_gate()
        self.assertTrue(result["exponent_sign_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["byte_cap"], 256)
        self.assertEqual(result["depth_cap"], 4)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_parent_directory_observations_are_complete(self):
        with tempfile.TemporaryDirectory() as root:
            result = parent_directory_observation(root)
        self.assertEqual(len(result["observation_rows"]), 4)
        self.assertEqual(result["targets"], ["observed-0.bin", "observed-1.bin"])
        self.assertTrue(result["all_observations_complete"])
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23]
                            for row in result["observation_rows"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_permutations_agree_and_mutations_reject(self):
        result = order_independent_zip64_extras()
        self.assertTrue(result["valid_permutations_agree"])
        self.assertEqual(result["descriptor_forms_valid"], [True, True])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_six_issuer_delegation_boundaries_fail_closed(self):
        result = six_issuer_delegation_boundaries()
        self.assertEqual(result["event_count"], 6)
        self.assertEqual(result["delegated_scope"], "archive:delegated")
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_ten_component_sweep_retains_all_null_controls(self):
        result = ten_component_covariance_sweep()
        self.assertEqual(result["components"], 10)
        self.assertEqual(result["sigma_values"], [0.0, 0.5, 1.0, 2.0, 3.0, 4.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            self.assertIsNone(scenarios["correlated"]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_translation_does_not_change_typed_covariance(self):
        result = translation_invariant_covariance_transform()
        self.assertTrue(result["translation_invariant"])
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["rescale_permutation_inverse_roundtrip"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_centered_gram_construction"])
        self.assertIsNone(result["calibration"])

    def test_h_full_and_deletion_grids_are_exhaustive(self):
        result = ten_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 10)
        self.assertEqual(result["full_grid_size"], 240)
        self.assertEqual(sum(result["winner_counts"]), 240)
        self.assertEqual(result["leave_one_out_grids"], 10)
        self.assertEqual(result["leave_two_out_grids"], 45)
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_three_source_maps_roundtrip_and_bind_order(self):
        result = three_source_bound_interval_maps(b"one", b"two", b"three")
        self.assertEqual(len(set(result["source_sha256"])), 3)
        self.assertEqual(len(result["factors"]), 3)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_context_and_revocation_controls_stay_fiction_only(self):
        result = context_bound_consent_controls("2026-09-29")
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 5)
        by_case = {row["case"]: row for row in result["control_table"]}
        self.assertFalse(by_case["context_mismatch"]["accepted"])
        self.assertFalse(by_case["revoked_after_challenge"]["accepted"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v16_rejects_overlap_and_bad_direction(self):
        result = lineage_manifest_v16(b"cycle026 synthetic lineage")
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["cross_split_overlap_rejected"])
        self.assertTrue(result["metric_direction_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_four_pairs_detect_order_mutation_and_reconstruct(self):
        result = four_inverse_pairs_order_gate()
        self.assertEqual(len(result["inverse_pair_names"]), 4)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertGreater(result["order_mutation_witness_count"], 0)
        self.assertEqual(result["resource_bound"], {"gates": 40, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle026_fixture(b"cycle026 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
