import math
import tempfile
import unittest

from uqpu.cycle039_delta01 import (
    LANES, lineage_manifest_v29_frontier, nineteen_issuer_batch_rotation_gate,
    nineteenth_weighted_graph_characters, run_cycle039_fixture,
    schema_v3_to_v4_provenance_gate, seventeen_inverse_pairs_slack_gate,
    sixteen_unit_affine_four_trees, ten_transform_adjugate_gate,
    thirteen_reader_exdev_journal_gate, twelve_observer_four_transitions,
    twenty_three_component_five_parenthesizations,
    twenty_three_scenario_deletion_intervals, zip64_normalization_descriptor_gate,
)


class Cycle039Tests(unittest.TestCase):
    def test_a_weighted_character_burnside_reconstruction(self):
        result = nineteenth_weighted_graph_characters()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (32768, 19, 20))
        self.assertEqual((result["stabilizer_size"], result["action_count"]), (10, 20))
        self.assertEqual(result["conjugacy_class_count"], 8)
        self.assertTrue(result["class_characters_constant"])
        self.assertTrue(result["burnside_matches_direct"])
        self.assertEqual(result["burnside_orbit_count"], 1)
        self.assertTrue(result["canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v4_provenance_rejects_elision(self):
        result = schema_v3_to_v4_provenance_gate()
        self.assertTrue(result["upgrade_matches_v4"])
        self.assertEqual(result["provenance"], {"source_schema": 3, "migration": "v3-to-v4",
                                                "default_origin": "schema-v3"})
        self.assertEqual(len(result["negative_controls"]), 12)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_exdev_and_cleanup_journal_fail_closed(self):
        with tempfile.TemporaryDirectory() as root:
            result = thirteen_reader_exdev_journal_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (13, 9))
        self.assertEqual((result["file_fsync_call_count"], result["directory_fsync_call_count"]), (9, 9))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_stage_orders_valid"])
        self.assertTrue(result["exdev_failure_observed"])
        self.assertTrue(result["cleanup_journal_empty"])
        self.assertTrue(all(item["rejected_as_durable"] for item in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_normalization_collision_and_descriptor_parity(self):
        result = zip64_normalization_descriptor_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["normalized_name"], "é.txt")
        self.assertTrue(result["normalization_collision_rejected"])
        self.assertTrue(result["local_central_descriptor_parity"])
        self.assertEqual(len(result["negative_controls"]), 20)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])

    def test_e_batch_watermark_and_cache_rotation(self):
        result = nineteen_issuer_batch_rotation_gate()
        self.assertEqual(result["event_count"], 19)
        self.assertEqual(result["policy_versions"], [37, 38, 39])
        self.assertEqual(result["revocation_epochs"], [10, 11, 12])
        self.assertEqual((result["initial_watermark"], result["new_watermark"]), (3007, 3011))
        self.assertEqual((result["cache_epoch"], result["rotated_cache_size"]), (12, 3))
        self.assertEqual(len(result["boundary_rejections"]), 22)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_five_parenthesizations_recover_twenty_three_components(self):
        result = twenty_three_component_five_parenthesizations(b"cycle039 covariance")
        self.assertEqual((result["components"], result["parenthesization_count"]), (23, 5))
        self.assertEqual(result["sparse_nonzero_count"], 67)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["recovers_intervals"] and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_tenth_transform_binds_adjugate_identity(self):
        result = ten_transform_adjugate_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"]), (10, 160))
        self.assertTrue(result["trace_power_invariant"])
        self.assertTrue(result["cayley_hamilton_zero"])
        self.assertTrue(result["adjugate_identity_left"])
        self.assertTrue(result["adjugate_identity_right"])
        self.assertTrue(result["adjugate_mutation_rejected"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_fifteen(self):
        result = twenty_three_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (23, 552))
        self.assertEqual(sum(result["winner_counts"]), 552)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(23, k) for k in range(1, 16)})
        self.assertTrue(result["counts_match_binomial"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [7, 8]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_sixteen_maps_match_four_trees(self):
        sources = tuple(f"source-{index}".encode() for index in range(16))
        result = sixteen_unit_affine_four_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (16, 4))
        self.assertEqual(len(result["unit_chain"]), 17)
        self.assertEqual(result["terminal_unit"], "u16")
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_twelve_observers_bind_four_transitions(self):
        result = twelve_observer_four_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (12, 10))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (8, 8))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (26, 4))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v29_frontier_is_smaller_than_individual_proofs(self):
        result = lineage_manifest_v29_frontier(b"cycle039 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual(result["selected_leaf_count"], 6)
        self.assertLess(result["frontier_node_count"], result["individual_proof_node_count"])
        self.assertTrue(result["frontier_is_smaller"])
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 8)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_seventeen_pairs_bind_schedule_slack(self):
        result = seventeen_inverse_pairs_slack_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (17, 17))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (61, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 335, "serial_depth": 107,
                         "dag_critical_depth": 61, "antichain_width": 4, "level_count": 8,
                         "level_width": 4, "unconstrained_parallel_lower_bound": 11, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle039_fixture(b"cycle039 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
