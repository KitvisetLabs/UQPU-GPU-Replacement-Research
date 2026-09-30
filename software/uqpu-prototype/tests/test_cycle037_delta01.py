import tempfile
import unittest

from uqpu.cycle037_delta01 import (
    LANES,
    eight_signed_transform_characteristic_invariants,
    eleven_reader_partial_write_gate,
    fifteen_inverse_pairs_antichain_dag,
    fourteen_unit_affine_split_conditions,
    lineage_manifest_v27,
    run_cycle037_fixture,
    schema_version_transition_gate,
    seventeenth_graph_orbit_histogram,
    seventeen_issuer_nonce_window,
    ten_observer_two_transitions,
    twenty_one_component_three_permutations,
    twenty_one_scenario_deletion_intervals,
    zip64_extra_field_gate,
)


class Cycle037Tests(unittest.TestCase):
    def test_a_orbit_histogram_reconstructs_all_witnesses(self):
        result = seventeenth_graph_orbit_histogram()
        self.assertEqual(result["states"], 8192)
        self.assertEqual(result["objective"], 12)
        self.assertEqual(result["witness_count"], 26)
        self.assertEqual(result["stabilizer_size"], 26)
        self.assertEqual(result["action_count"], 52)
        self.assertEqual(result["canonical_orbit_representatives"], [1365])
        self.assertEqual(result["orbit_size_histogram"], {"26": 1})
        self.assertEqual(result["burnside_numerator"], 52)
        self.assertEqual(result["burnside_orbit_count"], 1)
        self.assertTrue(result["representative_reconstruction_matches"])
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_schema_upgrade_and_item_paths_fail_closed(self):
        result = schema_version_transition_gate()
        self.assertTrue(result["upgrade_matches_v2"])
        self.assertEqual(len(result["negative_controls"]), 12)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"], {
            "depth": 10, "tokens": 68,
            "minimum_exponent": -36, "maximum_exponent": 36,
            "max_exact_integer": 9007199254740991,
        })
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_eleven_readers_reject_partial_and_fsync_failures(self):
        with tempfile.TemporaryDirectory() as root:
            result = eleven_reader_partial_write_gate(root)
        self.assertEqual(result["reader_count"], 11)
        self.assertEqual(result["replacement_stages"], 7)
        self.assertEqual(len(result["runs"]), 2)
        self.assertEqual(result["file_fsync_call_count"], 14)
        self.assertEqual(result["directory_fsync_call_count"], 14)
        self.assertTrue(result["all_fsync_orders_valid"])
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        controls = result["failure_controls"]
        self.assertEqual(set(controls), {"partial_write", "file_fsync", "directory_fsync"})
        self.assertTrue(all(item["rejected_as_durable"] for item in controls.values()))
        self.assertTrue(all(not item["evidence_promoted"] for item in controls.values()))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_extra_field_parser_rejects_twelve_mutations(self):
        result = zip64_extra_field_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["extra_field_count"], 2)
        self.assertEqual(result["zip64_eocd_position"], 8192)
        self.assertEqual(result["locator_position"], 8248)
        self.assertEqual(result["classic_eocd_position"], 8268)
        self.assertEqual(len(result["negative_controls"]), 12)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_nonce_window_and_transition_replay_fail_closed(self):
        result = seventeen_issuer_nonce_window()
        self.assertEqual(result["event_count"], 17)
        self.assertEqual(result["policy_versions"], [35, 36, 37])
        self.assertEqual(result["revocation_epochs"], [8, 9, 10])
        self.assertEqual(result["nonce_window"], [1000, 1009])
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertEqual(len(result["boundary_rejections"]), 14)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertIsNone(result["physical_sample"])

    def test_f_three_permutations_associate_and_recover_twenty_one_components(self):
        result = twenty_one_component_three_permutations(b"cycle037 covariance source")
        self.assertEqual(result["components"], 21)
        self.assertEqual(result["sparse_nonzero_count"], 55)
        self.assertEqual(sorted(result["composed_permutation"]), list(range(21)))
        self.assertTrue(result["composition_associative"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["triple_permutation_recovers_intervals"])
        self.assertTrue(result["triple_permutation_recovers_matrices"])
        self.assertTrue(result["permutation_equivalence"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        for sweep in result["sweeps"].values():
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in sweep["scenarios"][name]["outputs"]))
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_eight_transforms_preserve_characteristic_polynomial(self):
        result = eight_signed_transform_characteristic_invariants()
        self.assertEqual(result["transform_count"], 8)
        self.assertEqual(result["matrix_product_count"], 128)
        self.assertEqual(len(result["cayley_rows"]), 8)
        self.assertEqual(len(result["characteristic_coefficients"]), 5)
        self.assertTrue(result["all_cayley_rows_valid"])
        self.assertTrue(result["closure_is_signed_permutation"])
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["characteristic_polynomial_invariant"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["all_principal_minors_positive"])
        self.assertTrue(result["symmetric"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_exhausts_thirteen_deletion_depths(self):
        result = twenty_one_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 21)
        self.assertEqual(result["full_grid_size"], 504)
        self.assertEqual(sum(result["winner_counts"]), 504)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 21, "2": 210, "3": 1330, "4": 5985, "5": 20349,
            "6": 54264, "7": 116280, "8": 203490, "9": 293930,
            "10": 352716, "11": 352716, "12": 293930, "13": 203490,
        })
        self.assertTrue(result["counts_match_binomial"])
        self.assertTrue(all(result["dynamic_program_state_counts"].values()))
        self.assertEqual(result["all_grid_interval"], [[0, 1], [13, 16]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_fourteen_unit_maps_match_five_split_points(self):
        result = fourteen_unit_affine_split_conditions(
            b"one", b"two", b"three", b"four", b"five", b"six", b"seven",
            b"eight", b"nine", b"ten", b"eleven", b"twelve", b"thirteen", b"fourteen",
        )
        self.assertEqual(len(set(result["source_sha256"])), 14)
        self.assertEqual(result["map_count"], 14)
        self.assertEqual(len(result["unit_chain"]), 15)
        self.assertEqual(result["terminal_unit"], "u14")
        self.assertEqual(len(result["split_composition_rows"]), 5)
        self.assertTrue(result["all_split_compositions_match"])
        self.assertTrue(all(row["condition_product"] == [1, 1]
                            for row in result["split_composition_rows"]))
        self.assertEqual(result["lipschitz_product"], [1, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_ten_observers_bind_two_transitions(self):
        result = ten_observer_two_transitions()
        self.assertEqual(result["observer_count"], 10)
        self.assertEqual(result["quorum"], 8)
        self.assertEqual(result["certificate_intersection_size"], 6)
        self.assertEqual(result["minimum_quorum_intersection"], 6)
        self.assertEqual(result["membership_epoch"], 19)
        self.assertEqual(result["transition_count"], 2)
        self.assertEqual(len(result["control_table"]), 11)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v27_binds_batch_proof_minimality(self):
        result = lineage_manifest_v27(b"cycle037 synthetic lineage")
        self.assertEqual(result["real_leaf_count"], 14)
        self.assertEqual(result["padded_leaf_count"], 16)
        self.assertEqual(result["padding_leaf_count"], 2)
        self.assertEqual(result["padding_exclusion_count"], 2)
        self.assertEqual(result["selected_leaf_count"], 5)
        self.assertEqual(result["batch_proof_count"], 7)
        self.assertEqual(result["compressed_proof_node_count"], 19)
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 13)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_fifteen_pairs_bind_exact_antichain_width(self):
        result = fifteen_inverse_pairs_antichain_dag()
        self.assertEqual(len(result["inverse_pair_names"]), 15)
        self.assertEqual(result["proof_count"], 15)
        self.assertTrue(result["dependency_dag_valid"])
        self.assertTrue(result["dependency_dag_mutation_rejected"])
        self.assertTrue(result["all_inclusion_proofs_valid"])
        self.assertTrue(result["proof_resource_mutation_rejected"])
        self.assertTrue(result["leaf_resource_mutation_rejected"])
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["maximum_antichain"], [2, 3, 4, 5])
        self.assertEqual(result["antichain_width"], 4)
        self.assertTrue(result["antichain_valid"])
        self.assertTrue(result["antichain_mutation_rejected"])
        self.assertEqual(result["resource_bound"], {
            "gates": 267, "serial_depth": 86, "dag_critical_depth": 40,
            "antichain_width": 4, "unconstrained_parallel_lower_bound": 9,
            "max_qubits": 6,
        })
        self.assertTrue(result["parallel_bounds_are_model_only"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle037_fixture(b"cycle037 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
