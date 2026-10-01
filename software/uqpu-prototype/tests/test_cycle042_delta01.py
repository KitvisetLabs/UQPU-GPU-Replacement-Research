import math
import tempfile
import unittest

from uqpu.cycle042_delta01 import (
    LANES, fifteen_observer_seven_transitions, lineage_manifest_v32_two_leaf_update,
    nineteen_unit_affine_seven_trees, run_cycle042_fixture,
    schema_v6_to_v7_compacted_checkpoint_gate, sixteen_reader_dual_recovery_gate,
    thirteen_transform_woodbury_gate, twenty_inverse_pairs_resource_gate,
    twenty_second_weighted_stabilizer_cosets, twenty_six_component_eight_parenthesizations,
    twenty_six_scenario_deletion_intervals, twenty_two_issuer_four_batch_handoffs,
    zip64_split_disk_comment_length_gate,
)


class Cycle042Tests(unittest.TestCase):
    def test_a_stabilizer_cosets_and_four_labels(self):
        result = twenty_second_weighted_stabilizer_cosets()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (262144, 27, 8))
        self.assertEqual((result["graph_stabilizer_size"], result["action_count"],
                          result["rotation_subgroup_size"], result["coset_count"]), (6, 12, 3, 4))
        self.assertEqual((result["orbit_count"], result["orbit_sizes"]), (2, [2, 6]))
        self.assertTrue(result["cosets_partition_actions"])
        self.assertTrue(result["orbit_stabilizer_valid"] and result["burnside_matches_direct"])
        self.assertTrue(result["four_canonical_algorithms_agree"])
        self.assertTrue(result["canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v7_checkpoint_compaction_and_replay_controls(self):
        result = schema_v6_to_v7_compacted_checkpoint_gate()
        self.assertTrue(result["migration_matches_v7"])
        self.assertEqual((result["compacted_record_count"], result["tail_record_count"]), (3, 1))
        self.assertEqual(len(result["negative_controls"]), 14)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_sixteen_readers_ordered_dual_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            result = sixteen_reader_dual_recovery_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (16, 12))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertEqual((result["replacement_file_fsync_call_count"],
                          result["replacement_directory_fsync_call_count"]), (12, 12))
        self.assertEqual((result["pending_recovery_count"], result["recovery_generations"]), (2, [13, 14]))
        self.assertTrue(result["ordered_dual_recovery"] and result["reordered_recovery_rejected"])
        self.assertTrue(result["cleanup_journal_empty"])
        self.assertTrue(all(row["rejected_as_durable"] for row in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_split_disk_comment_length_and_end_record_parity(self):
        result = zip64_split_disk_comment_length_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual((result["corpus_size"], result["disk_starts"]), (2, [2, 5]))
        self.assertEqual(result["unicode_comment_lengths"], [8, 12])
        self.assertTrue(result["local_central_end_record_parity"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])

    def test_e_four_batches_and_three_handoffs(self):
        result = twenty_two_issuer_four_batch_handoffs()
        self.assertEqual(result["event_count"], 22)
        self.assertEqual(result["batch_watermarks"], [6002, 6005, 6008, 6011])
        self.assertEqual(result["cache_epochs"], [18, 19, 20, 21])
        self.assertEqual((len(result["batch_commit_sha256"]), len(result["handoff_sha256"])), (4, 3))
        self.assertTrue(result["cache_epochs_pairwise_disjoint"] and result["commit_chain_bound"])
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_eight_parenthesizations_recover_twenty_six_components(self):
        result = twenty_six_component_eight_parenthesizations(b"cycle042 covariance")
        self.assertEqual((result["components"], result["permutation_count"],
                          result["parenthesization_count"]), (26, 8, 8))
        self.assertEqual(result["sparse_nonzero_count"], 76)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"] and result["recovers_intervals"]
                        and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_rank_two_woodbury_and_determinant_identity(self):
        result = thirteen_transform_woodbury_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"],
                          result["woodbury_rank"]), (13, 208, 2))
        self.assertTrue(result["left_inverse_valid_v13"] and result["right_inverse_valid_v13"])
        self.assertTrue(result["determinant_identity_valid_v13"])
        self.assertEqual(result["updated_determinant_v13"], [35, 1])
        self.assertTrue(result["inverse_mutation_rejected_v13"])
        self.assertTrue(result["determinant_mutation_rejected_v13"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_eighteen(self):
        result = twenty_six_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (26, 624))
        self.assertEqual(sum(result["winner_counts"]), 624)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(26, k) for k in range(1, 19)})
        self.assertTrue(result["counts_match_binomial"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [1, 2]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_nineteen_maps_match_seven_trees_and_derivative(self):
        sources = tuple(f"source-{index}".encode() for index in range(19))
        result = nineteen_unit_affine_seven_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (19, 7))
        self.assertEqual((len(result["unit_chain"]), result["terminal_unit"]), (20, "u19"))
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["independent_derivative_product_valid"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_fifteen_observers_bind_seven_transitions(self):
        result = fifteen_observer_seven_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (15, 13))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (11, 11))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (47, 7))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v32_two_leaf_update_multiproof(self):
        result = lineage_manifest_v32_two_leaf_update(b"cycle042 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual((result["updated_leaf_count"], result["frontier_node_count"]), (2, 6))
        self.assertTrue(result["old_root_reconstruction_valid"])
        self.assertTrue(result["new_root_reconstruction_valid"])
        self.assertTrue(result["independent_old_root_valid"] and result["independent_new_root_valid"])
        self.assertTrue(result["root_changed"] and result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_twenty_pairs_bind_resource_certificates(self):
        result = twenty_inverse_pairs_resource_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (20, 20))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"] and result["critical_path_recomputed"]
                        and result["width_recomputed"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (100, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 452, "serial_depth": 146,
                         "dag_critical_depth": 100, "antichain_width": 4,
                         "level_count": 11, "level_width": 4,
                         "unconstrained_parallel_lower_bound": 14, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle042_fixture(b"cycle042 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
