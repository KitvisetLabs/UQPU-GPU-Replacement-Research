import tempfile
import unittest

from uqpu.cycle036_delta01 import (
    LANES,
    fourteen_inverse_pairs_branched_dag,
    lineage_manifest_v26,
    nine_observer_membership_transition,
    run_cycle036_fixture,
    schema_path_numeric_gate,
    seven_signed_transform_principal_minors,
    sixteenth_graph_orbit_representatives,
    sixteen_issuer_revocation_chain,
    ten_reader_injected_fsync_gate,
    thirteen_unit_affine_bilipschitz,
    twenty_component_composed_permutations,
    twenty_scenario_deletion_intervals,
    zip64_adjacency_sentinel_gate,
)


class Cycle036Tests(unittest.TestCase):
    def test_a_canonical_representative_matches_two_partition_digests(self):
        result = sixteenth_graph_orbit_representatives()
        self.assertEqual(result["states"], 4096)
        self.assertEqual(result["objective"], 30)
        self.assertEqual(result["witness_count"], 2)
        self.assertEqual(result["stabilizer_size"], 12)
        self.assertEqual(result["action_count"], 24)
        self.assertEqual(result["canonical_orbit_representatives"], [1365])
        self.assertEqual(result["burnside_numerator"], 24)
        self.assertEqual(result["burnside_orbit_count"], 1)
        self.assertTrue(result["partition_digest_matches"])
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_schema_paths_and_normalized_keys_fail_closed(self):
        result = schema_path_numeric_gate()
        self.assertTrue(result["schema_path_equivalence"])
        self.assertEqual(len(result["negative_controls"]), 10)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"], {
            "depth": 9, "tokens": 60,
            "minimum_exponent": -30, "maximum_exponent": 30,
            "max_exact_integer": 9007199254740991,
        })
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_ten_readers_and_injected_fsync_failures_bind(self):
        with tempfile.TemporaryDirectory() as root:
            result = ten_reader_injected_fsync_gate(root)
        self.assertEqual(result["reader_count"], 10)
        self.assertEqual(result["replacement_stages"], 6)
        self.assertEqual(len(result["runs"]), 2)
        self.assertEqual(result["file_fsync_call_count"], 12)
        self.assertEqual(result["directory_fsync_call_count"], 12)
        self.assertTrue(result["all_fsync_orders_valid"])
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        controls = result["injected_failure_controls"]
        self.assertTrue(all(item["rejected_as_durable"] for item in controls.values()))
        self.assertTrue(all(not item["evidence_promoted"] for item in controls.values()))
        self.assertFalse(controls["file_fsync"]["replace_occurred"])
        self.assertTrue(controls["directory_fsync"]["replace_occurred"])
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_adjacency_and_sentinels_bind(self):
        result = zip64_adjacency_sentinel_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["zip64_eocd_position"], 4096)
        self.assertEqual(result["locator_position"], 4152)
        self.assertEqual(result["classic_eocd_position"], 4172)
        self.assertEqual(result["adjacency_bytes"], [56, 20])
        self.assertEqual(len(result["negative_controls"]), 9)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_revocation_epochs_and_receipt_replay_fail_closed(self):
        result = sixteen_issuer_revocation_chain()
        self.assertEqual(result["event_count"], 16)
        self.assertEqual(result["policy_versions"], [34, 35, 36])
        self.assertEqual(result["revocation_epochs"], [7, 8, 9])
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertEqual(len(result["boundary_rejections"]), 12)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertIsNone(result["physical_sample"])

    def test_f_two_permutations_compose_and_recover_twenty_components(self):
        result = twenty_component_composed_permutations(b"cycle036 covariance source")
        self.assertEqual(result["components"], 20)
        self.assertEqual(result["sparse_nonzero_count"], 52)
        self.assertEqual(sorted(result["composed_permutation"]), list(range(20)))
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
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

    def test_g_seven_transforms_bind_exact_principal_minors(self):
        result = seven_signed_transform_principal_minors()
        self.assertEqual(result["transform_count"], 7)
        self.assertEqual(result["matrix_product_count"], 112)
        self.assertEqual(len(result["cayley_rows"]), 7)
        self.assertTrue(result["all_cayley_rows_valid"])
        self.assertTrue(result["closure_is_signed_permutation"])
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_absolute_invariant"])
        self.assertTrue(result["all_principal_minors_positive"])
        self.assertEqual(len(result["original_principal_minors"]), 4)
        self.assertEqual(len(result["transformed_principal_minors"]), 4)
        self.assertTrue(result["symmetric"])
        self.assertIsNone(result["calibration"])

    def test_h_twelve_deletion_depths_are_exhaustive(self):
        result = twenty_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 20)
        self.assertEqual(result["full_grid_size"], 480)
        self.assertEqual(sum(result["winner_counts"]), 480)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 20, "2": 190, "3": 1140, "4": 4845, "5": 15504,
            "6": 38760, "7": 77520, "8": 125970, "9": 167960,
            "10": 184756, "11": 167960, "12": 125970,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [13, 16]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_thirteen_unit_maps_bind_bilipschitz_roundtrip(self):
        result = thirteen_unit_affine_bilipschitz(
            b"one", b"two", b"three", b"four", b"five", b"six", b"seven",
            b"eight", b"nine", b"ten", b"eleven", b"twelve", b"thirteen",
        )
        self.assertEqual(len(set(result["source_sha256"])), 13)
        self.assertEqual(result["map_count"], 13)
        self.assertEqual(len(result["unit_chain"]), 14)
        self.assertEqual(result["terminal_unit"], "u13")
        self.assertTrue(result["associative_composition"])
        self.assertEqual(result["lipschitz_product"], [1, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_nine_observers_bind_membership_transition(self):
        result = nine_observer_membership_transition()
        self.assertEqual(result["observer_count"], 9)
        self.assertEqual(result["quorum"], 7)
        self.assertEqual(result["certificate_intersection_size"], 5)
        self.assertEqual(result["minimum_quorum_intersection"], 5)
        self.assertEqual(result["membership_epoch"], 17)
        self.assertEqual(len(result["control_table"]), 11)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v26_binds_inclusion_and_padding_exclusion(self):
        result = lineage_manifest_v26(b"cycle036 synthetic lineage")
        self.assertEqual(result["real_leaf_count"], 13)
        self.assertEqual(result["padded_leaf_count"], 16)
        self.assertEqual(result["padding_leaf_count"], 3)
        self.assertEqual(result["padding_exclusion_count"], 3)
        self.assertEqual(result["selected_leaf_count"], 4)
        self.assertEqual(result["simultaneous_proof_count"], 7)
        self.assertEqual(result["compressed_proof_node_count"], 18)
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 14)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_fourteen_pairs_bind_branched_dag_depth(self):
        result = fourteen_inverse_pairs_branched_dag()
        self.assertEqual(len(result["inverse_pair_names"]), 14)
        self.assertEqual(result["proof_count"], 14)
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
            "gates": 236, "serial_depth": 77, "dag_critical_depth": 38,
            "unconstrained_parallel_lower_bound": 9, "max_qubits": 6,
        })
        self.assertTrue(result["parallel_bounds_are_model_only"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle036_fixture(b"cycle036 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
