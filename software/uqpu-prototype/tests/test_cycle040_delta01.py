import math
import tempfile
import unittest

from uqpu.cycle040_delta01 import (
    LANES,
    eighteen_inverse_pairs_critical_path_gate,
    eleven_transform_determinant_recurrence_gate,
    fourteen_reader_journal_recovery_gate,
    lineage_manifest_v30_reconstruction,
    run_cycle040_fixture,
    schema_v4_to_v5_provenance_chain_gate,
    seventeen_unit_affine_five_trees,
    thirteen_observer_five_transitions,
    twenty_four_component_six_parenthesizations,
    twenty_four_scenario_deletion_intervals,
    twenty_issuer_two_batch_handoff_gate,
    twentieth_weighted_orbit_incidence,
    zip64_unicode_crc_signature_corpus_gate,
)


class Cycle040Tests(unittest.TestCase):
    def test_a_orbit_incidence_and_two_canonical_algorithms(self):
        result = twentieth_weighted_orbit_incidence()
        self.assertEqual((result["states"], result["objective"], result["witness_count"]),
                         (65536, 24, 16))
        self.assertEqual((result["stabilizer_size"], result["action_count"]), (4, 8))
        self.assertEqual((result["orbit_count"], result["orbit_sizes"]), (4, [2, 8, 4, 2]))
        self.assertTrue(result["incidence_rows_bind_actions"])
        self.assertEqual(result["incidence_row_sums"], [8, 8, 8, 8])
        self.assertTrue(result["burnside_matches_direct"])
        self.assertEqual(result["burnside_orbit_count"], 4)
        self.assertTrue(result["canonical_algorithms_agree"])
        self.assertTrue(result["canonical_label_reconstruction"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v5_provenance_chain_and_downgrade_controls(self):
        result = schema_v4_to_v5_provenance_chain_gate()
        self.assertTrue(result["upgrade_matches_v5"])
        self.assertEqual([(row["from"], row["to"]) for row in result["provenance_chain"]],
                         [(3, 4), (4, 5)])
        self.assertEqual(len(result["negative_controls"]), 14)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c_fourteen_readers_checksum_and_recovery(self):
        with tempfile.TemporaryDirectory() as root:
            result = fourteen_reader_journal_recovery_gate(root)
        self.assertEqual((result["reader_count"], result["replacement_stages"]), (14, 10))
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_stage_orders_valid"])
        self.assertTrue(result["journal_checksums_unique"])
        self.assertEqual((result["replacement_file_fsync_call_count"],
                          result["replacement_directory_fsync_call_count"]), (10, 10))
        self.assertTrue(result["recovery_checksum_valid"])
        self.assertTrue(result["interrupted_cleanup_recovered"])
        self.assertTrue(result["cleanup_journal_empty"])
        self.assertTrue(all(row["rejected_as_durable"]
                            for row in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d_unicode_path_crc_signature_and_parity(self):
        result = zip64_unicode_crc_signature_corpus_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual((result["corpus_size"], result["descriptor_signature"]), (2, 0x08074B50))
        self.assertEqual(len(result["unicode_path_crc32"]), 2)
        self.assertTrue(result["local_central_normalization_parity"])
        self.assertGreaterEqual(len(result["negative_controls"]), 26)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_two_batch_commits_and_cache_epoch_handoff(self):
        result = twenty_issuer_two_batch_handoff_gate()
        self.assertEqual(result["event_count"], 20)
        self.assertEqual((result["initial_watermark"], result["first_watermark"],
                          result["second_watermark"]), (4000, 4002, 4005))
        self.assertEqual(result["cache_epochs"], [13, 14])
        self.assertEqual(result["cache_sizes"], [2, 2])
        self.assertTrue(result["cache_epochs_disjoint"])
        self.assertTrue(result["commit_chain_bound"])
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_six_parenthesizations_recover_twenty_four_components(self):
        result = twenty_four_component_six_parenthesizations(b"cycle040 covariance")
        self.assertEqual((result["components"], result["permutation_count"],
                          result["parenthesization_count"]), (24, 6, 6))
        self.assertEqual(result["sparse_nonzero_count"], 70)
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["recovers_intervals"] and result["recovers_matrices"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        self.assertTrue(result["invalid_outputs_null"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_determinant_lemma_and_power_sum_recurrence(self):
        result = eleven_transform_determinant_recurrence_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"]), (11, 176))
        self.assertTrue(result["adjugate_identity_left"] and result["adjugate_identity_right"])
        self.assertEqual(result["determinant_lemma_left"], result["determinant_lemma_right"])
        self.assertTrue(result["determinant_lemma_valid"])
        self.assertTrue(result["power_sum_recurrence_valid"])
        self.assertTrue(result["determinant_mutation_rejected"])
        self.assertTrue(result["power_sum_mutation_rejected"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_through_leave_sixteen(self):
        result = twenty_four_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"]), (24, 576))
        self.assertEqual(sum(result["winner_counts"]), 576)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(k): math.comb(24, k) for k in range(1, 17)})
        self.assertTrue(result["counts_match_binomial"])
        self.assertEqual(result["all_grid_interval"], [[0, 1], [1, 1]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_seventeen_maps_match_five_trees(self):
        sources = tuple(f"source-{index}".encode() for index in range(17))
        result = seventeen_unit_affine_five_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"]), (17, 5))
        self.assertEqual(len(result["unit_chain"]), 18)
        self.assertEqual(result["terminal_unit"], "u17")
        self.assertTrue(result["all_tree_shapes_match"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_thirteen_observers_bind_five_transitions(self):
        result = thirteen_observer_five_transitions()
        self.assertEqual((result["observer_count"], result["quorum"]), (13, 11))
        self.assertEqual((result["certificate_intersection_size"],
                          result["minimum_quorum_intersection"]), (9, 9))
        self.assertEqual((result["membership_epoch"], result["transition_count"]), (32, 5))
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_v30_frontier_reconstructs_independent_root(self):
        result = lineage_manifest_v30_reconstruction(b"cycle040 lineage")
        self.assertEqual((result["real_leaf_count"], result["padding_leaf_count"]), (16, 0))
        self.assertEqual(result["selected_leaf_count"], 5)
        self.assertTrue(result["frontier_is_smaller"])
        self.assertTrue(result["frontier_reconstruction_valid"])
        self.assertTrue(result["independent_root_valid"])
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(result["frontier_reconstructed_root"], result["independently_recomputed_root"])
        self.assertEqual(len(result["mutation_rejections"]), 8)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_eighteen_pairs_bind_critical_path_and_slack(self):
        result = eighteen_inverse_pairs_critical_path_gate()
        self.assertEqual((len(result["inverse_pair_names"]), result["proof_count"]), (18, 18))
        self.assertTrue(result["extension_proof_valid"])
        self.assertEqual((result["basis_states_checked"], result["distinct_outputs"], result["residual"]),
                         (64, 64, 0))
        self.assertTrue(result["dependency_dag_valid"] and result["all_inclusion_proofs_valid"])
        self.assertTrue(result["work_conservation"])
        self.assertTrue(result["critical_path_recomputed"])
        self.assertEqual((result["scheduled_depth"], result["schedule_slack"]), (73, 0))
        self.assertTrue(result["slack_certificate_valid"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 372, "serial_depth": 119,
                         "dag_critical_depth": 73, "antichain_width": 4,
                         "level_count": 9, "level_width": 4,
                         "unconstrained_parallel_lower_bound": 12, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle040_fixture(b"cycle040 integrated", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS" for item in result.values()))


if __name__ == "__main__":
    unittest.main()
