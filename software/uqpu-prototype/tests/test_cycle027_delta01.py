import tempfile
import unittest

from uqpu.cycle027_delta01 import (
    LANES,
    correlation_rescale_invariance,
    delayed_reader_atomicity,
    eleven_component_correlation_extrema,
    eleven_scenario_deletion_intervals,
    five_inverse_pairs_program_gate,
    four_source_monotone_maps,
    lineage_manifest_v17,
    local_central_zip64_cross_bind,
    run_cycle027_fixture,
    seven_issuer_substitution_controls,
    seventh_graph_rotation_orbits,
    token_bounded_receipt_gate,
    version_audience_consent_controls,
)


class Cycle027Tests(unittest.TestCase):
    def test_a_seventh_graph_binds_simultaneous_rotation_orbits(self):
        result = seventh_graph_rotation_orbits()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [16, 20])
        self.assertEqual(result["changed_edge_indices"], [1])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertTrue(result["all_simultaneous_rotations_match"])
        self.assertEqual(result["complement_pair_count"] * 2, result["witness_counts"][1])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_token_bounded_arrays_reject_every_control(self):
        result = token_bounded_receipt_gate()
        self.assertTrue(result["array_numeric_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["byte_cap"], 256)
        self.assertEqual(result["depth_cap"], 5)
        self.assertEqual(result["token_cap"], 24)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_delayed_reader_observes_only_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result = delayed_reader_atomicity(root)
        self.assertEqual(len(result["runs"]), 4)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(all(row["reader_observation_count"] > 0 for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23] for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_local_central_zip64_cross_bind_rejects_mutations(self):
        result = local_central_zip64_cross_bind()
        self.assertTrue(result["local_central_sizes_equal"])
        self.assertTrue(result["unknown_extra_preserved"])
        self.assertTrue(result["order_independent"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_seven_issuer_substitutions_fail_closed(self):
        result = seven_issuer_substitution_controls()
        self.assertEqual(result["event_count"], 7)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_eleven_component_extrema_keep_null_controls(self):
        result = eleven_component_correlation_extrema()
        self.assertEqual(result["components"], 11)
        self.assertTrue(result["asymmetric_component_intervals"])
        self.assertEqual(result["sigma_values"], [1.0, 3.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in result["correlation_extrema"]:
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_correlation_is_invariant_under_positive_rescaling(self):
        result = correlation_rescale_invariance()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["exact_covariance_roundtrip"])
        self.assertTrue(result["correlation_coefficient_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_positive_diagonal_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_three_deletion_depths_are_exhaustive(self):
        result = eleven_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 11)
        self.assertEqual(result["full_grid_size"], 264)
        self.assertEqual(sum(result["winner_counts"]), 264)
        self.assertEqual(result["leave_one_out_grids"], 11)
        self.assertEqual(result["leave_two_out_grids"], 55)
        self.assertEqual(result["leave_three_out_grids"], 165)
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_four_monotone_maps_roundtrip_and_reject_mutations(self):
        result = four_source_monotone_maps(b"one", b"two", b"three", b"four")
        self.assertEqual(len(set(result["source_sha256"])), 4)
        self.assertEqual(len(result["factors"]), 4)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(result["strictly_monotone"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_version_audience_and_epoch_stay_fiction_only(self):
        result = version_audience_consent_controls("2026-09-30")
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 6)
        by_case = {row["case"]: row for row in result["control_table"]}
        self.assertFalse(by_case["version_mismatch"]["accepted"])
        self.assertFalse(by_case["audience_mismatch"]["accepted"])
        self.assertFalse(by_case["revoked_epoch"]["accepted"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v17_binds_root_counts_and_metric_type(self):
        result = lineage_manifest_v17(b"cycle027 synthetic lineage")
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["dataset_root_mutation_rejected"])
        self.assertTrue(result["membership_count_mutation_rejected"])
        self.assertTrue(result["metric_type_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_five_pairs_bind_program_and_reconstruct(self):
        result = five_inverse_pairs_program_gate()
        self.assertEqual(len(result["inverse_pair_names"]), 5)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertGreater(result["order_mutation_witness_count"], 0)
        self.assertEqual(result["resource_bound"], {"gates": 58, "max_qubits": 6})
        self.assertEqual(len(result["program_sha256"]), 64)
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle027_fixture(b"cycle027 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
