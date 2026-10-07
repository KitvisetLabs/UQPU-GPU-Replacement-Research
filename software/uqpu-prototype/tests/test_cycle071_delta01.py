import math
import tempfile
import unittest

from uqpu.cycle071_delta01 import *


class Cycle071Tests(unittest.TestCase):
    def test_a(self):
        result = fifty_first_weighted_length_twenty_six_walks()
        self.assertEqual(
            (result["fixture_ordinal"], len(result["length_twenty_six_walk_multiplicities"]), result["length_twenty_six_walk_total"]),
            (51, 6, 255870340469520072704),
        )
        self.assertTrue(
            result["length_twenty_six_walks_match_matrix_power"]
            and result["thirty_third_canonical_label_reconstruction"]
            and result["thirty_three_canonical_algorithms_agree"]
        )
        self.assertIsNone(result["scaling_claim"])

    def test_b(self):
        result = schema_v35_to_v36_twenty_five_checkpoint_gate()
        self.assertTrue(result["migration_matches_v36"])
        self.assertEqual(result["checkpoint_count"], 25)
        self.assertGreaterEqual(len(result["negative_controls"]), 163)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["external_authority"])

    def test_c(self):
        with tempfile.TemporaryDirectory() as directory:
            result = forty_five_reader_thirty_one_recovery_gate(directory)
        self.assertEqual(
            (result["reader_count"], result["replacement_stages"], result["pending_recovery_count"], result["complete_marker_fsync_count"]),
            (45, 41, 31, 72),
        )
        self.assertTrue(
            result["all_reader_observations_complete"]
            and result["ordered_thirty_one_recovery"]
            and result["complete_marker_barrier_preserved"]
            and result["cleanup_journal_empty"]
        )
        self.assertTrue(all(value["rejected_as_durable"] and not value["evidence_promoted"] for value in result["failure_controls"].values()))
        self.assertIsNone(result["crash_durability"])

    def test_d(self):
        result = zip64_twenty_six_volume_eighteen_envelope_gate()
        self.assertEqual(
            (result["corpus_size"], result["central_directory_segment_count"], result["central_directory_total_length"], result["envelope_count"]),
            (26, 25, 819200, 18),
        )
        self.assertTrue(result["valid_metadata"] and all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e(self):
        result = fifty_first_issuer_thirty_three_batch_handoffs()
        self.assertEqual((result["event_count"], len(result["batch_commit_sha256"]), len(result["handoff_sha256"])), (51, 33, 32))
        self.assertTrue(result["cache_epochs_pairwise_disjoint"] and result["commit_chain_bound"] and all(result["boundary_rejections"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f(self):
        result = fifty_five_component_thirty_seven_parenthesizations(b"cycle071")
        self.assertEqual((result["components"], result["permutation_count"], result["parenthesization_count"], result["sparse_nonzero_count"]), (55, 37, 37, 165))
        self.assertTrue(
            result["all_parenthesizations_equal"]
            and result["composition_matches_sequential_intervals"]
            and result["composition_matches_sequential_matrices"]
            and result["inverse_map_valid"]
            and all(result["binding_mutation_rejections"].values())
        )
        self.assertIsNone(result["commercial_interpretation"])

    def test_g(self):
        result = forty_two_transform_fourteen_stage_update_gate()
        self.assertEqual((result["transform_count"], result["matrix_product_count"], result["fourteen_stage_determinant_left"]), (42, 980, [-1466921138940036679, 1871844320586240]))
        self.assertTrue(
            result["fourteen_stage_direct_matrix_equal"]
            and result["fourteen_stage_determinant_valid"]
            and result["fourteen_stage_matches_prior_certificate"]
            and result["fourteen_stage_solve_valid"]
            and result["stage_order_mutation_rejected"]
        )
        self.assertEqual(result["fourteen_stage_residual"], [[0, 1]] * 3)
        self.assertIsNone(result["calibration"])

    def test_h(self):
        result = fifty_five_scenario_deletion_intervals()
        self.assertEqual((result["scenario_count"], result["full_grid_size"], len(result["deletion_grid_counts"])), (55, 1760, 47))
        self.assertTrue(result["counts_match_binomial"] and result["prior_leave_forty_six_valid"])
        self.assertEqual(result["deletion_grid_counts"]["47"], math.comb(55, 47))
        self.assertIsNone(result["probability_claim"])

    def test_fnd(self):
        sources = [b"s", *[f"s:{index}".encode() for index in range(1, 48)]]
        result = forty_eight_unit_affine_thirty_six_trees(*sources)
        self.assertEqual((result["map_count"], result["tree_shape_count"], result["terminal_unit"]), (48, 36, "u48"))
        self.assertTrue(
            result["all_tree_shapes_match"]
            and result["independent_first_derivative_valid"]
            and result["independent_second_derivative_valid"]
            and all(result["negative_controls"].values())
        )
        self.assertIsNone(result["new_law_claim"])

    def test_scm(self):
        result = forty_four_observer_thirty_six_transitions()
        self.assertEqual(
            (result["observer_count"], result["quorum"], result["certificate_intersection_size"], result["membership_epoch"], result["transition_count"]),
            (44, 42, 40, 714, 36),
        )
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost(self):
        result = lineage_manifest_v61_thirty_one_leaf_update(b"cycle071")
        self.assertEqual((result["manifest"]["version"], result["real_leaf_count"], result["updated_leaf_count"], result["frontier_node_count"]), (61, 32, 31, 1))
        self.assertTrue(
            result["valid_manifest"]
            and result["old_root_reconstruction_valid"]
            and result["new_root_reconstruction_valid"]
            and result["independent_old_root_valid"]
            and result["independent_new_root_valid"]
            and result["prior_update_valid"]
            and all(result["mutation_rejections"].values())
        )
        self.assertIsNone(result["functional_equivalence"])

    def test_qos(self):
        result = forty_nine_inverse_pairs_resource_gate()
        self.assertEqual(
            (result["proof_count"], result["basis_states_checked"], result["resource_bound"]["gates"], result["resource_bound"]["dag_critical_depth"], result["resource_bound"]["serial_depth"], result["antichain_width"], result["schedule_slack"]),
            (49, 64, 3179, 1046, 1465, 4, 0),
        )
        self.assertTrue(
            result["extension_proof_valid"]
            and result["dependency_dag_valid"]
            and result["all_inclusion_proofs_valid"]
            and result["work_conservation"]
            and result["critical_path_recomputed"]
            and result["width_recomputed"]
            and result["slack_certificate_valid"]
            and all(result["mutation_rejections"].values())
        )
        self.assertIsNone(result["hardware"])

    def test_integrated_contract(self):
        with tempfile.TemporaryDirectory() as directory:
            result = run_cycle071_fixture(b"cycle071-integrated", directory)
        self.assertEqual(set(result), set(LANES))
        self.assertTrue(all(value["status"] == "BLOCKED_WITH_PROGRESS" for value in result.values()))
        self.assertNotIn("NO_UPDATE", {value["status"] for value in result.values()})


if __name__ == "__main__":
    unittest.main()
