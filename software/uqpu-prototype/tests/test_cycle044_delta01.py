import math
import tempfile
import unittest

from uqpu.cycle044_delta01 import (
    LANES,
    eighteen_reader_four_recovery_gate,
    fifteen_transform_block_ldu_gate,
    lineage_manifest_v34_four_leaf_update,
    run_cycle044_fixture,
    schema_v8_to_v9_checkpoint_lineage_gate,
    seventeen_observer_nine_transitions,
    twenty_eight_component_ten_parenthesizations,
    twenty_eight_scenario_deletion_intervals,
    twenty_four_issuer_six_batch_handoffs,
    twenty_fourth_weighted_double_coset_representatives,
    twenty_one_unit_affine_nine_trees,
    twenty_two_inverse_pairs_resource_gate,
    zip64_extensible_sector_gate,
)


class Cycle044Tests(unittest.TestCase):
    def test_a_double_coset_representatives_and_six_labels(self):
        result = twenty_fourth_weighted_double_coset_representatives()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (262144, 27, 8))
        self.assertEqual((result["double_coset_count"], result["representative_count"]), (4, 4))
        self.assertEqual(result["double_coset_sizes"], [3, 3, 3, 3])
        self.assertTrue(result["representatives_reconstruct_group"])
        self.assertTrue(result["orbit_stabilizer_valid"] and result["burnside_matches_direct"])
        self.assertTrue(result["six_canonical_algorithms_agree"])
        self.assertTrue(result["sixth_canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v9_checkpoint_lineage_and_fork_ancestry_controls(self):
        result = schema_v8_to_v9_checkpoint_lineage_gate()
        self.assertTrue(result["migration_matches_v9"])
        self.assertEqual((result["lineage_record_count"], result["parent_count"]), (4, 1))
        self.assertEqual(len(result["negative_controls"]), 15)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_eighteen_readers_ordered_four_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            result = eighteen_reader_four_recovery_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (18, 14))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertEqual((result["replacement_file_fsync_call_count"],
                          result["replacement_directory_fsync_call_count"]), (14, 14))
        self.assertEqual((result["pending_recovery_count"], result["recovery_generations"]),
                         (4, [15, 16, 17, 18]))
        self.assertTrue(result["ordered_four_recovery"] and result["duplicate_generation_rejected"])
        self.assertTrue(result["generation_gap_rejected"] and result["reordered_recovery_rejected"])
        self.assertTrue(result["cleanup_journal_empty"])
        self.assertTrue(all(row["rejected_as_durable"] for row in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_zip64_extensible_sector_and_end_record_parity(self):
        result = zip64_extensible_sector_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["corpus_size"], 4)
        self.assertEqual(result["extensible_sector_lengths"], [8, 16, 24, 32])
        self.assertEqual(result["zip64_record_sizes"], [52, 60, 68, 76])
        self.assertEqual(result["split_disk_sequence"], [0, 1, 2, 3])
        self.assertTrue(result["local_central_end_record_parity"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])

    def test_e_six_batches_and_five_handoffs(self):
        result = twenty_four_issuer_six_batch_handoffs()
        self.assertEqual(result["event_count"], 24)
        self.assertEqual(result["batch_watermarks"], [8002, 8005, 8008, 8011, 8014, 8017])
        self.assertEqual(result["cache_epochs"], [27, 28, 29, 30, 31, 32])
        self.assertEqual((len(result["batch_commit_sha256"]), len(result["handoff_sha256"])), (6, 5))
        self.assertTrue(result["cache_epochs_pairwise_disjoint"] and result["commit_chain_bound"])
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_ten_parenthesizations_recover_twenty_eight_components(self):
        result = twenty_eight_component_ten_parenthesizations(b"cycle044 covariance")
        self.assertEqual((result["components"], result["permutation_count"],
                          result["parenthesization_count"]), (28, 10, 10))
        self.assertEqual(result["sparse_nonzero_count"], 82)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"] and result["recovers_intervals"]
                        and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_block_ldu_inverse_and_determinant_identity(self):
        result = fifteen_transform_block_ldu_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"]), (15, 240))
        self.assertTrue(result["block_ldu_factorization_valid"])
        self.assertTrue(result["block_ldu_left_inverse_valid"] and result["block_ldu_right_inverse_valid"])
        self.assertTrue(result["block_ldu_determinant_identity_valid"])
        self.assertEqual(result["updated_determinant_v15"], [119, 1])
        self.assertTrue(result["factor_mutation_rejected_v15"])
        self.assertTrue(result["inverse_mutation_rejected_v15"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_twenty(self):
        result = twenty_eight_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (28, 672))
        self.assertEqual(sum(result["winner_counts"]), 672)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(28, k) for k in range(1, 21)})
        self.assertTrue(result["counts_match_binomial"] and result["prior_leave_nineteen_valid"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [1, 2]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_twenty_one_maps_match_nine_trees_and_two_derivatives(self):
        sources = tuple(f"source-{index}".encode() for index in range(21))
        result = twenty_one_unit_affine_nine_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (21, 9))
        self.assertEqual((len(result["unit_chain"]), result["terminal_unit"]), (22, "u21"))
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["independent_first_derivative_valid"])
        self.assertTrue(result["independent_second_derivative_valid"])
        self.assertEqual(result["exact_second_derivative"], [0, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_seventeen_observers_bind_nine_transitions(self):
        result = seventeen_observer_nine_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (17, 15))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (13, 13))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (66, 9))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v34_four_leaf_update_multiproof(self):
        result = lineage_manifest_v34_four_leaf_update(b"cycle044 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual((result["updated_leaf_count"], result["frontier_node_count"]), (4, 8))
        self.assertTrue(result["old_root_reconstruction_valid"])
        self.assertTrue(result["new_root_reconstruction_valid"])
        self.assertTrue(result["independent_old_root_valid"] and result["independent_new_root_valid"])
        self.assertTrue(result["root_changed"] and result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_twenty_two_pairs_bind_resource_certificates(self):
        result = twenty_two_inverse_pairs_resource_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (22, 22))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"] and result["critical_path_recomputed"]
                        and result["width_recomputed"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (131, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 540, "serial_depth": 177,
                         "dag_critical_depth": 131, "antichain_width": 4,
                         "level_count": 13, "level_width": 4,
                         "unconstrained_parallel_lower_bound": 16, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle044_fixture(b"cycle044 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
