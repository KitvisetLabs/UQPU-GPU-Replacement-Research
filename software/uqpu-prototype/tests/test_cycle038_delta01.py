import math
import tempfile
import unittest

from uqpu.cycle038_delta01 import (
    LANES,
    eighteen_issuer_watermark_gate,
    eighteenth_graph_conjugacy_orbits,
    eleven_observer_three_transitions,
    fifteen_unit_affine_tree_conditions,
    lineage_manifest_v28_multiproof,
    nine_signed_transform_trace_invariants,
    run_cycle038_fixture,
    schema_v2_to_v3_default_gate,
    sixteen_inverse_pairs_level_schedule,
    twelve_reader_cleanup_gate,
    twenty_two_component_four_parenthesizations,
    twenty_two_scenario_deletion_intervals,
    zip64_unicode_path_parity_gate,
)


class Cycle038Tests(unittest.TestCase):
    def test_a_conjugacy_fixed_vector_and_orbit_encodings_agree(self):
        result = eighteenth_graph_conjugacy_orbits()
        self.assertEqual(result["states"], 16384)
        self.assertEqual(result["objective"], 14)
        self.assertEqual(result["witness_count"], 2)
        self.assertEqual(result["action_count"], 56)
        self.assertEqual(result["conjugacy_class_count"], 20)
        self.assertEqual(sum(row["size"] for row in result["conjugacy_class_fixed_vector"]), 56)
        self.assertTrue(result["fixed_counts_constant_within_classes"])
        self.assertEqual(result["burnside_numerator"], 56)
        self.assertEqual(result["burnside_orbit_count"], 1)
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["two_orbit_encodings_match"])
        self.assertTrue(result["representative_reconstruction_matches"])
        self.assertEqual(result["canonical_orbit_representatives"], [5461])
        self.assertIsNone(result["scaling_claim"])

    def test_b_v2_to_v3_default_insertion_fails_closed(self):
        result = schema_v2_to_v3_default_gate()
        self.assertTrue(result["upgrade_matches_v3"])
        self.assertEqual(result["inserted_default"], {"mode": "strict", "retry": 0})
        self.assertEqual(len(result["negative_controls"]), 14)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"], {
            "depth": 11, "tokens": 72,
            "minimum_exponent": -40, "maximum_exponent": 40,
            "max_exact_integer": 9007199254740991,
        })
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_twelve_readers_reject_rename_and_cleanup_failures(self):
        with tempfile.TemporaryDirectory() as root:
            result = twelve_reader_cleanup_gate(root)
        self.assertEqual(result["reader_count"], 12)
        self.assertEqual(result["replacement_stages"], 8)
        self.assertEqual(len(result["runs"]), 2)
        self.assertEqual(result["file_fsync_call_count"], 16)
        self.assertEqual(result["directory_fsync_call_count"], 16)
        self.assertTrue(result["all_fsync_orders_valid"])
        self.assertTrue(result["all_reader_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        self.assertTrue(result["all_temporary_cleanup_complete"])
        controls = result["failure_controls"]
        self.assertEqual(set(controls), {"partial_write", "file_fsync", "rename",
                                         "directory_fsync", "temporary_cleanup"})
        self.assertTrue(controls["rename"]["injected_failure_observed"])
        self.assertTrue(all(item["rejected_as_durable"] for item in controls.values()))
        self.assertTrue(all(not item["evidence_promoted"] for item in controls.values()))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_unicode_zip64_local_central_parity_rejects_mutations(self):
        result = zip64_unicode_path_parity_gate()
        self.assertTrue(result["valid_metadata"])
        self.assertEqual(result["extra_field_count"], 2)
        self.assertEqual(result["canonical_extra_identifiers"], [0x0001, 0x7075])
        self.assertEqual(result["unicode_path"], "café.txt")
        self.assertTrue(result["local_central_parity"])
        self.assertEqual(len(result["negative_controls"]), 16)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_nonce_watermark_and_replay_cache_fail_closed(self):
        result = eighteen_issuer_watermark_gate()
        self.assertEqual(result["event_count"], 18)
        self.assertEqual(result["policy_versions"], [36, 37, 38])
        self.assertEqual(result["revocation_epochs"], [9, 10, 11])
        self.assertEqual(result["nonce_window"], [2000, 2011])
        self.assertEqual(result["initial_watermark"], 2007)
        self.assertEqual(result["new_watermark"], 2010)
        self.assertEqual(result["replay_cache_size"], 5)
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertEqual(len(result["boundary_rejections"]), 16)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertIsNone(result["physical_sample"])

    def test_f_four_parenthesizations_recover_twenty_two_components(self):
        result = twenty_two_component_four_parenthesizations(b"cycle038 covariance source")
        self.assertEqual(result["components"], 22)
        self.assertEqual(result["sparse_nonzero_count"], 58)
        self.assertEqual(result["parenthesization_count"], 4)
        self.assertEqual(sorted(result["composed_permutation"]), list(range(22)))
        self.assertTrue(result["all_parenthesizations_equal"])
        self.assertTrue(result["composition_matches_sequential_intervals"])
        self.assertTrue(result["composition_matches_sequential_matrices"])
        self.assertTrue(result["inverse_map_valid"])
        self.assertTrue(result["four_permutation_recovers_intervals"])
        self.assertTrue(result["four_permutation_recovers_matrices"])
        self.assertTrue(result["permutation_equivalence"])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        for sweep in result["sweeps"].values():
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in sweep["scenarios"][name]["outputs"]))
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_nine_transforms_bind_trace_powers_and_cayley_hamilton(self):
        result = nine_signed_transform_trace_invariants()
        self.assertEqual(result["transform_count"], 9)
        self.assertEqual(result["matrix_product_count"], 144)
        self.assertEqual(len(result["cayley_rows"]), 9)
        self.assertEqual(len(result["characteristic_coefficients"]), 5)
        self.assertEqual(len(result["trace_powers"]), 4)
        self.assertTrue(result["all_cayley_rows_valid"])
        self.assertTrue(result["closure_is_signed_permutation"])
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["characteristic_polynomial_invariant"])
        self.assertTrue(result["trace_power_invariant"])
        self.assertTrue(result["cayley_hamilton_zero"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["all_principal_minors_positive"])
        self.assertTrue(result["symmetric"])
        self.assertIsNone(result["calibration"])

    def test_h_dynamic_program_exhausts_fourteen_deletion_depths(self):
        result = twenty_two_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 22)
        self.assertEqual(result["full_grid_size"], 528)
        self.assertEqual(sum(result["winner_counts"]), 528)
        self.assertEqual(result["deletion_grid_counts"],
                         {str(count): math.comb(22, count) for count in range(1, 15)})
        self.assertTrue(result["counts_match_binomial"])
        self.assertEqual(len(result["dynamic_program_state_counts"]), 14)
        self.assertTrue(all(result["dynamic_program_state_counts"].values()))
        self.assertEqual(result["all_grid_interval"], [[0, 1], [13, 16]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_fifteen_unit_maps_match_tree_parenthesizations(self):
        sources = tuple(f"source-{index}".encode() for index in range(15))
        result = fifteen_unit_affine_tree_conditions(*sources)
        self.assertEqual(len(set(result["source_sha256"])), 15)
        self.assertEqual(result["map_count"], 15)
        self.assertEqual(len(result["unit_chain"]), 16)
        self.assertEqual(result["terminal_unit"], "u15")
        self.assertEqual(result["tree_parenthesizations"], ["left_fold", "right_fold", "balanced"])
        self.assertTrue(result["all_tree_parenthesizations_match"])
        self.assertEqual(len(result["split_composition_rows"]), 5)
        self.assertTrue(result["all_split_compositions_match"])
        self.assertTrue(all(row["condition_product"] == [1, 1]
                            for row in result["split_composition_rows"]))
        self.assertEqual(result["lipschitz_product"], [1, 1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_eleven_observers_bind_three_transitions(self):
        result = eleven_observer_three_transitions()
        self.assertEqual(result["observer_count"], 11)
        self.assertEqual(result["quorum"], 9)
        self.assertEqual(result["certificate_intersection_size"], 7)
        self.assertEqual(result["minimum_quorum_intersection"], 7)
        self.assertEqual(result["membership_epoch"], 22)
        self.assertEqual(result["transition_count"], 3)
        self.assertEqual(len(result["control_table"]), 11)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v28_compresses_minimal_multiproof(self):
        result = lineage_manifest_v28_multiproof(b"cycle038 synthetic lineage")
        self.assertEqual(result["real_leaf_count"], 15)
        self.assertEqual(result["padded_leaf_count"], 16)
        self.assertEqual(result["padding_leaf_count"], 1)
        self.assertEqual(result["padding_exclusion_count"], 1)
        self.assertEqual(result["selected_leaf_count"], 5)
        self.assertEqual(result["multiproof_target_count"], 6)
        self.assertEqual(result["compressed_multiproof_node_count"], 7)
        self.assertEqual(result["individual_proof_node_count"], 24)
        self.assertTrue(result["multiproof_is_smaller"])
        self.assertTrue(result["valid_manifest"])
        self.assertEqual(len(result["mutation_rejections"]), 13)
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_sixteen_pairs_bind_level_and_work_certificates(self):
        result = sixteen_inverse_pairs_level_schedule()
        self.assertEqual(len(result["inverse_pair_names"]), 16)
        self.assertEqual(result["proof_count"], 16)
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
        self.assertTrue(result["level_schedule_valid"])
        self.assertTrue(result["level_schedule_mutation_rejected"])
        self.assertTrue(result["work_conservation"])
        self.assertTrue(result["work_mutation_rejected"])
        self.assertEqual(result["resource_bound"], {
            "gates": 300, "serial_depth": 96, "dag_critical_depth": 50,
            "antichain_width": 4, "level_count": 7, "level_width": 4,
            "unconstrained_parallel_lower_bound": 10, "max_qubits": 6,
        })
        self.assertTrue(result["parallel_bounds_are_model_only"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle038_fixture(b"cycle038 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
