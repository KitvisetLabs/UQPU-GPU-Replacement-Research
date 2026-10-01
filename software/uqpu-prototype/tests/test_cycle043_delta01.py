import math
import tempfile
import unittest

from uqpu.cycle043_delta01 import (
    LANES,
    fourteen_transform_schur_gate,
    lineage_manifest_v33_three_leaf_update,
    run_cycle043_fixture,
    schema_v7_to_v8_checkpoint_tail_merge_gate,
    seventeen_reader_triple_recovery_gate,
    sixteen_observer_eight_transitions,
    twenty_one_inverse_pairs_resource_gate,
    twenty_seven_component_nine_parenthesizations,
    twenty_seven_scenario_deletion_intervals,
    twenty_three_issuer_five_batch_handoffs,
    twenty_third_weighted_double_cosets,
    twenty_unit_affine_eight_trees,
    zip64_extra_alignment_sequence_gate,
)


class Cycle043Tests(unittest.TestCase):
    def test_a_double_cosets_and_five_labels(self):
        result = twenty_third_weighted_double_cosets()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (262144, 27, 8))
        self.assertEqual((result["double_coset_count"], result["double_coset_sizes"]),
                         (4, [3, 3, 3, 3]))
        self.assertTrue(result["double_cosets_partition_actions"])
        self.assertTrue(result["orbit_stabilizer_valid"] and result["burnside_matches_direct"])
        self.assertTrue(result["five_canonical_algorithms_agree"])
        self.assertTrue(result["fifth_canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v8_checkpoint_tail_merge_and_fork_controls(self):
        result = schema_v7_to_v8_checkpoint_tail_merge_gate()
        self.assertTrue(result["migration_matches_v8"])
        self.assertEqual((result["merged_record_count"], result["tail_record_count"]), (4, 0))
        self.assertEqual(len(result["negative_controls"]), 14)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_seventeen_readers_ordered_triple_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            result = seventeen_reader_triple_recovery_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (17, 13))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertEqual((result["replacement_file_fsync_call_count"],
                          result["replacement_directory_fsync_call_count"]), (13, 13))
        self.assertEqual((result["pending_recovery_count"], result["recovery_generations"]),
                         (3, [14, 15, 16]))
        self.assertTrue(result["ordered_triple_recovery"] and result["generation_gap_rejected"])
        self.assertTrue(result["reordered_recovery_rejected"] and result["cleanup_journal_empty"])
        self.assertTrue(all(row["rejected_as_durable"] for row in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_zip64_extra_alignment_sequence_and_end_record_parity(self):
        result = zip64_extra_alignment_sequence_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual((result["corpus_size"], result["extra_field_header_id"]), (3, 0x0001))
        self.assertEqual(result["extra_field_lengths"], [24, 24, 24])
        self.assertEqual(result["split_disk_sequence"], [0, 1, 2])
        self.assertTrue(result["all_extra_fields_aligned"])
        self.assertTrue(result["local_central_end_record_parity"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])

    def test_e_five_batches_and_four_handoffs(self):
        result = twenty_three_issuer_five_batch_handoffs()
        self.assertEqual(result["event_count"], 23)
        self.assertEqual(result["batch_watermarks"], [7002, 7005, 7008, 7011, 7014])
        self.assertEqual(result["cache_epochs"], [22, 23, 24, 25, 26])
        self.assertEqual((len(result["batch_commit_sha256"]), len(result["handoff_sha256"])), (5, 4))
        self.assertTrue(result["cache_epochs_pairwise_disjoint"] and result["commit_chain_bound"])
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_nine_parenthesizations_recover_twenty_seven_components(self):
        result = twenty_seven_component_nine_parenthesizations(b"cycle043 covariance")
        self.assertEqual((result["components"], result["permutation_count"],
                          result["parenthesization_count"]), (27, 9, 9))
        self.assertEqual(result["sparse_nonzero_count"], 79)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"] and result["recovers_intervals"]
                        and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_schur_inverse_and_determinant_identity(self):
        result = fourteen_transform_schur_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"],
                          result["schur_dimension"]), (14, 224, 1))
        self.assertEqual(result["schur_complement"], [119, 20])
        self.assertTrue(result["left_inverse_valid_v14"] and result["right_inverse_valid_v14"])
        self.assertTrue(result["determinant_identity_valid_v14"])
        self.assertEqual(result["updated_determinant_v14"], [119, 1])
        self.assertTrue(result["inverse_mutation_rejected_v14"])
        self.assertTrue(result["determinant_mutation_rejected_v14"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_nineteen(self):
        result = twenty_seven_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (27, 648))
        self.assertEqual(sum(result["winner_counts"]), 648)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(27, k) for k in range(1, 20)})
        self.assertTrue(result["counts_match_binomial"] and result["prior_leave_eighteen_valid"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [1, 2]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_twenty_maps_match_eight_trees_and_two_derivatives(self):
        sources = tuple(f"source-{index}".encode() for index in range(20))
        result = twenty_unit_affine_eight_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (20, 8))
        self.assertEqual((len(result["unit_chain"]), result["terminal_unit"]), (21, "u20"))
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["independent_first_derivative_valid"])
        self.assertTrue(result["independent_second_derivative_valid"])
        self.assertEqual(result["exact_second_derivative"], [0, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_sixteen_observers_bind_eight_transitions(self):
        result = sixteen_observer_eight_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (16, 14))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (12, 12))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (56, 8))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v33_three_leaf_update_multiproof(self):
        result = lineage_manifest_v33_three_leaf_update(b"cycle043 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual((result["updated_leaf_count"], result["frontier_node_count"]), (3, 7))
        self.assertTrue(result["old_root_reconstruction_valid"])
        self.assertTrue(result["new_root_reconstruction_valid"])
        self.assertTrue(result["independent_old_root_valid"] and result["independent_new_root_valid"])
        self.assertTrue(result["root_changed"] and result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_twenty_one_pairs_bind_resource_certificates(self):
        result = twenty_one_inverse_pairs_resource_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (21, 21))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"] and result["critical_path_recomputed"]
                        and result["width_recomputed"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (115, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 495, "serial_depth": 161,
                         "dag_critical_depth": 115, "antichain_width": 4,
                         "level_count": 12, "level_width": 4,
                         "unconstrained_parallel_lower_bound": 15, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle043_fixture(b"cycle043 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
