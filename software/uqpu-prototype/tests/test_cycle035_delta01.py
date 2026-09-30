import tempfile
import unittest

from uqpu.cycle035_delta01 import (
    LANES,
    eight_observer_membership_epochs,
    fifteen_issuer_policy_chain,
    fifteenth_graph_conjugacy_checksum,
    heterogeneous_array_unicode_gate,
    lineage_manifest_v25,
    nineteen_component_permutation_roundtrip,
    nineteen_scenario_deletion_intervals,
    nine_reader_fsync_order_gate,
    run_cycle035_fixture,
    six_signed_transform_cayley_rows,
    thirteen_inverse_pairs_dependency_dag,
    twelve_source_affine_lipschitz,
    zip64_locator_trailing_comment_gate,
)


class Cycle035Tests(unittest.TestCase):
    def test_a_conjugacy_classes_match_direct_orbit_checksum(self):
        result = fifteenth_graph_conjugacy_checksum()
        self.assertEqual(result["states"], 2048)
        self.assertEqual(result["objective"], 67)
        self.assertEqual(result["witness_count"], 4)
        self.assertEqual(result["stabilizer_size"], 2)
        self.assertEqual(result["action_count"], 4)
        self.assertEqual(result["burnside_numerator"], 4)
        self.assertEqual(result["burnside_orbit_count"], 1)
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["checksum_matches_witnesses"])
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertEqual(result["independent_orbit_checksum"]["count"], 4)
        self.assertIsNone(result["scaling_claim"])

    def test_b_heterogeneous_arrays_and_unicode_fail_closed(self):
        result = heterogeneous_array_unicode_gate()
        self.assertTrue(result["heterogeneous_array_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(len(result["negative_controls"]), 10)
        self.assertEqual(result["caps"], {
            "depth": 8, "tokens": 52,
            "minimum_exponent": -24, "maximum_exponent": 24,
            "max_exact_integer": 9007199254740991,
        })
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_nine_readers_bind_file_then_directory_fsync_order(self):
        with tempfile.TemporaryDirectory() as root:
            result = nine_reader_fsync_order_gate(root)
        self.assertEqual(result["reader_count"], 9)
        self.assertEqual(result["replacement_stages"], 5)
        self.assertEqual(len(result["runs"]), 2)
        self.assertEqual(result["file_fsync_call_count"], 10)
        self.assertEqual(result["directory_fsync_call_count"], 10)
        self.assertTrue(result["all_fsync_orders_valid"])
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        self.assertTrue(all(result["fsync_order_negative_controls"].values()))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_locator_comment_and_trailing_policy_bind(self):
        result = zip64_locator_trailing_comment_gate()
        self.assertTrue(result["small_comment_valid"])
        self.assertTrue(result["maximum_comment_valid"])
        self.assertEqual(result["maximum_comment_length"], 65535)
        self.assertEqual(result["locator_target_offset"], 4096)
        self.assertEqual(result["locator_position"], 8192)
        self.assertEqual(set(result["negative_controls"]), {
            "trailing", "comment_bytes", "crc", "count", "disk",
            "locator_offset", "locator_position", "size", "comment_overflow",
        })
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_policy_chain_and_fifteen_events_fail_closed(self):
        result = fifteen_issuer_policy_chain()
        self.assertEqual(result["event_count"], 15)
        self.assertEqual(result["policy_versions"], [33, 34, 35])
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertEqual(len(result["boundary_rejections"]), 10)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertIsNone(result["physical_sample"])

    def test_f_nineteen_component_double_permutation_recovers(self):
        result = nineteen_component_permutation_roundtrip(b"cycle035 covariance source")
        self.assertEqual(result["components"], 19)
        self.assertEqual(result["sparse_nonzero_count"], 49)
        self.assertEqual(sorted(result["permutation"]), list(range(19)))
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["double_permutation_recovers_intervals"])
        self.assertTrue(result["double_permutation_recovers_matrices"])
        self.assertTrue(result["permutation_equivalence"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        for sweep in result["sweeps"].values():
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in sweep["scenarios"][name]["outputs"]))
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_six_transforms_bind_selected_cayley_rows(self):
        result = six_signed_transform_cayley_rows()
        self.assertEqual(result["transform_count"], 6)
        self.assertEqual(result["matrix_product_count"], 96)
        self.assertEqual(len(result["cayley_rows"]), 6)
        self.assertTrue(result["all_cayley_rows_valid"])
        self.assertTrue(result["closure_is_signed_permutation"])
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_absolute_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_signed_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_eleven_deletion_depths_are_exhaustive(self):
        result = nineteen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 19)
        self.assertEqual(result["full_grid_size"], 456)
        self.assertEqual(sum(result["winner_counts"]), 456)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 19, "2": 171, "3": 969, "4": 3876, "5": 11628,
            "6": 27132, "7": 50388, "8": 75582, "9": 92378,
            "10": 92378, "11": 75582,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [23, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_twelve_maps_bind_lipschitz_and_inverse(self):
        result = twelve_source_affine_lipschitz(
            b"one", b"two", b"three", b"four", b"five", b"six",
            b"seven", b"eight", b"nine", b"ten", b"eleven", b"twelve",
        )
        self.assertEqual(len(set(result["source_sha256"])), 12)
        self.assertEqual(result["map_count"], 12)
        self.assertTrue(result["associative_composition"])
        self.assertEqual(result["lipschitz_product"], [1, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_eight_observer_quorums_intersect_in_four(self):
        result = eight_observer_membership_epochs()
        self.assertEqual(result["observer_count"], 8)
        self.assertEqual(result["quorum"], 6)
        self.assertEqual(result["certificate_intersection_size"], 4)
        self.assertEqual(result["minimum_quorum_intersection"], 4)
        self.assertEqual(result["membership_epoch"], 16)
        self.assertEqual(len(result["control_table"]), 10)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v25_excludes_four_padding_leaves(self):
        result = lineage_manifest_v25(b"cycle035 synthetic lineage")
        self.assertEqual(result["real_leaf_count"], 12)
        self.assertEqual(result["padded_leaf_count"], 16)
        self.assertEqual(result["padding_leaf_count"], 4)
        self.assertEqual(result["padding_exclusion_count"], 4)
        self.assertEqual(result["selected_leaf_count"], 4)
        self.assertEqual(result["compressed_proof_node_count"], 7)
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 12)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_thirteen_pairs_bind_dependency_dag_and_resources(self):
        result = thirteen_inverse_pairs_dependency_dag()
        self.assertEqual(len(result["inverse_pair_names"]), 13)
        self.assertEqual(result["proof_count"], 13)
        self.assertTrue(result["dependency_dag_valid"])
        self.assertTrue(result["dependency_dag_mutation_rejected"])
        self.assertTrue(result["all_inclusion_proofs_valid"])
        self.assertTrue(result["proof_resource_mutation_rejected"])
        self.assertTrue(result["leaf_resource_mutation_rejected"])
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {
            "gates": 269, "sequential_depth": 47,
            "dag_critical_depth": 47,
            "unconstrained_parallel_lower_bound": 8, "max_qubits": 6,
        })
        self.assertTrue(result["parallel_bound_is_model_only"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle035_fixture(b"cycle035 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
