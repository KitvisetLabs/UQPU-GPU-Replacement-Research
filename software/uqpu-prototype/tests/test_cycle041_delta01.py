import math
import tempfile
import unittest

from uqpu.cycle041_delta01 import (
    LANES,
    eighteen_unit_affine_six_trees,
    fifteen_reader_generation_recovery_gate,
    fourteen_observer_six_transitions,
    lineage_manifest_v31_incremental_update,
    nineteen_inverse_pairs_width_slack_gate,
    run_cycle041_fixture,
    schema_v5_to_v6_migration_journal_gate,
    twelve_transform_sherman_morrison_gate,
    twenty_five_component_seven_parenthesizations,
    twenty_five_scenario_deletion_intervals,
    twenty_first_weighted_orbit_stabilizer,
    twenty_one_issuer_three_batch_handoffs,
    zip64_unicode_comment_locator_gate,
)


class Cycle041Tests(unittest.TestCase):
    def test_a_orbit_stabilizer_and_three_canonical_algorithms(self):
        result = twenty_first_weighted_orbit_stabilizer()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (131072, 27, 16))
        self.assertEqual((result["graph_stabilizer_size"], result["action_count"]), (2, 4))
        self.assertEqual((result["orbit_count"], result["orbit_sizes"]), (4, [4, 4, 4, 4]))
        self.assertEqual(result["orbit_stabilizer_products"], [4, 4, 4, 4])
        self.assertTrue(result["orbit_stabilizer_double_count_valid"])
        self.assertTrue(result["burnside_matches_direct"])
        self.assertEqual(result["burnside_orbit_count"], 4)
        self.assertTrue(result["three_canonical_algorithms_agree"])
        self.assertTrue(result["canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v6_hash_linked_journal_and_rollback_denial(self):
        result = schema_v5_to_v6_migration_journal_gate()
        self.assertTrue(result["migration_matches_v6"])
        self.assertEqual(result["journal_record_count"], 3)
        self.assertEqual(len(result["negative_controls"]), 14)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_fifteen_readers_generations_and_stale_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            result = fifteen_reader_generation_recovery_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (15, 11))
        self.assertEqual(result["generation_sequence"], list(range(1, 12)))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["generation_sequence_valid"])
        self.assertEqual((result["replacement_file_fsync_call_count"],
                          result["replacement_directory_fsync_call_count"]), (11, 11))
        self.assertEqual(result["recovery_generation"], 12)
        self.assertTrue(result["recovery_checksum_valid"])
        self.assertTrue(result["stale_recovery_rejected"])
        self.assertTrue(result["interrupted_recovery_completed"])
        self.assertTrue(result["cleanup_journal_empty"])
        self.assertTrue(all(row["rejected_as_durable"] for row in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_unicode_comment_crc_and_zip64_locator_parity(self):
        result = zip64_unicode_comment_locator_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["corpus_size"], 2)
        self.assertEqual((result["locator_signature"], result["eocd64_signature"]),
                         (0x07064B50, 0x06064B50))
        self.assertEqual(len(result["unicode_comment_crc32"]), 2)
        self.assertTrue(result["local_central_end_record_parity"])
        self.assertGreaterEqual(len(result["negative_controls"]), 31)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])

    def test_e_three_batches_and_two_epoch_handoffs(self):
        result = twenty_one_issuer_three_batch_handoffs()
        self.assertEqual(result["event_count"], 21)
        self.assertEqual(result["batch_watermarks"], [5002, 5005, 5008])
        self.assertEqual(result["cache_epochs"], [15, 16, 17])
        self.assertEqual(result["cache_sizes"], [2, 2, 2])
        self.assertEqual((len(result["batch_commit_sha256"]), len(result["handoff_sha256"])), (3, 2))
        self.assertTrue(result["cache_epochs_pairwise_disjoint"])
        self.assertTrue(result["commit_chain_bound"])
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_seven_parenthesizations_recover_twenty_five_components(self):
        result = twenty_five_component_seven_parenthesizations(b"cycle041 covariance")
        self.assertEqual((result["components"], result["permutation_count"],
                          result["parenthesization_count"]), (25, 7, 7))
        self.assertEqual(result["sparse_nonzero_count"], 73)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["recovers_intervals"] and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_sherman_morrison_inverse_and_determinant(self):
        result = twelve_transform_sherman_morrison_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"]), (12, 192))
        self.assertTrue(result["left_inverse_valid"] and result["right_inverse_valid"])
        self.assertTrue(result["determinant_consistency"])
        self.assertEqual((result["updated_determinant"], result["denominator"]), ([17, 1], [17, 10]))
        self.assertTrue(result["inverse_mutation_rejected"])
        self.assertTrue(result["determinant_mutation_rejected_v12"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_seventeen(self):
        result = twenty_five_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (25, 600))
        self.assertEqual(sum(result["winner_counts"]), 600)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(25, k) for k in range(1, 18)})
        self.assertTrue(result["counts_match_binomial"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [1, 1]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_eighteen_maps_match_six_trees(self):
        sources = tuple(f"source-{index}".encode() for index in range(18))
        result = eighteen_unit_affine_six_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (18, 6))
        self.assertEqual(len(result["unit_chain"]), 19)
        self.assertEqual(result["terminal_unit"], "u18")
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["endpoint_certificate_valid"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_fourteen_observers_bind_six_transitions(self):
        result = fourteen_observer_six_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (14, 12))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (10, 10))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (39, 6))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v31_incremental_update_recomputes_both_roots(self):
        result = lineage_manifest_v31_incremental_update(b"cycle041 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual(result["update_path_node_count"], 4)
        self.assertTrue(result["old_root_reconstruction_valid"])
        self.assertTrue(result["new_root_reconstruction_valid"])
        self.assertTrue(result["independent_new_root_valid"])
        self.assertTrue(result["root_changed"])
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 8)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_nineteen_pairs_bind_width_path_and_slack(self):
        result = nineteen_inverse_pairs_width_slack_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (19, 19))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"])
        self.assertTrue(result["critical_path_recomputed"] and result["width_recomputed"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (86, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 411, "serial_depth": 132,
                         "dag_critical_depth": 86, "antichain_width": 4,
                         "level_count": 10, "level_width": 4,
                         "unconstrained_parallel_lower_bound": 13, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle041_fixture(b"cycle041 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
