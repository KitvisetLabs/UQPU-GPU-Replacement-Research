import tempfile
import unittest

from uqpu.cycle033_delta01 import (
    LANES,
    eleven_inverse_pairs_aggregate_resources,
    four_signed_block_transforms,
    lineage_manifest_v23,
    run_cycle033_fixture,
    seven_reader_three_stage_atomicity,
    seventeen_component_sparse_covariance,
    seventeen_scenario_deletion_intervals,
    six_observer_intersecting_certificates,
    ten_source_affine_derivatives,
    thirteen_issuer_rotating_fresh_receipts,
    thirteenth_graph_nontrivial_burnside,
    typed_decimal_unicode_receipt_gate,
    zip64_classic_sentinel_single_disk_bind,
)


class Cycle033Tests(unittest.TestCase):
    def test_a_nontrivial_stabilizer_burnside_matches_direct(self):
        result = thirteenth_graph_nontrivial_burnside()
        self.assertEqual(result["states"], 2048)
        self.assertEqual(result["objective"], 35)
        self.assertEqual(result["witness_count"], 4)
        self.assertTrue(result["declared_reflection_symmetric"])
        self.assertEqual(result["stabilizer"], [[1, 0], [-1, 0]])
        self.assertEqual(result["stabilizer_size"], 2)
        self.assertEqual(result["action_count"], 4)
        self.assertEqual(result["fixed_point_counts"], [4, 0, 0, 0])
        self.assertEqual(result["burnside_orbit_count"], len(result["direct_quotient"]))
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_decimal_tuples_and_typed_scalars_do_not_collide(self):
        result = typed_decimal_unicode_receipt_gate()
        self.assertTrue(result["canonical_decimal_tuple_equivalence"])
        self.assertTrue(result["typed_scalar_collision_free"])
        self.assertEqual(len(set(result["typed_scalar_hashes"].values())), 4)
        self.assertTrue(all(result["typed_tag_controls"].values()))
        self.assertTrue(result["prior_recursive_equivalence"])
        self.assertTrue(all(result["prior_negative_controls"].values()))
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_seven_readers_three_stages_keep_complete_bytes(self):
        with tempfile.TemporaryDirectory() as root:
            result = seven_reader_three_stage_atomicity(root)
        self.assertEqual(result["reader_count"], 7)
        self.assertEqual(result["replacement_stages"], 3)
        self.assertEqual(len(result["runs"]), 2)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        self.assertTrue(all(row["exit_codes"] == [[0, 23, 23]] * 3 for row in result["runs"]))
        self.assertEqual(result["directory_fsync_protocol_model"],
                         ["write-temp", "fsync-temp", "replace", "fsync-directory"])
        self.assertFalse(result["directory_fsync_observed"])
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_classic_sentinels_and_single_disk_policy_bind(self):
        result = zip64_classic_sentinel_single_disk_bind()
        self.assertTrue(result["classic_eocd_valid"])
        self.assertEqual(result["classic_eocd_size"], 22)
        self.assertTrue(result["single_disk_policy"])
        self.assertTrue(all(result["sentinel_controls"].values()))
        self.assertEqual(result["prior_zip64_valid"], [True, True])
        self.assertTrue(all(result["prior_zip64_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_rotated_and_stale_receipts_fail_closed(self):
        result = thirteen_issuer_rotating_fresh_receipts()
        self.assertEqual(result["event_count"], 13)
        self.assertEqual(result["receipt_authority_count"], 4)
        self.assertEqual(result["active_signer_count"], 3)
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertIsNone(result["physical_sample"])

    def test_f_seventeen_component_sparse_grid_keeps_nulls(self):
        result = seventeen_component_sparse_covariance(b"cycle033 covariance source")
        self.assertEqual(result["components"], 17)
        self.assertEqual(len(result["component_order"]), 17)
        self.assertEqual(result["sparse_nonzero_count"], 43)
        self.assertEqual(sorted(result["permutation"]), list(range(17)))
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_four_signed_transforms_close_associate_and_invert(self):
        result = four_signed_block_transforms()
        self.assertEqual(result["transform_count"], 4)
        self.assertEqual(result["matrix_product_count"], 64)
        self.assertTrue(result["closure_is_signed_permutation"])
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_absolute_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_signed_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_nine_deletion_depths_are_exhaustive(self):
        result = seventeen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 17)
        self.assertEqual(result["full_grid_size"], 408)
        self.assertEqual(sum(result["winner_counts"]), 408)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 17, "2": 136, "3": 680, "4": 2380, "5": 6188,
            "6": 12376, "7": 19448, "8": 24310, "9": 24310,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [21, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_ten_affine_maps_bind_derivatives_and_roundtrip(self):
        result = ten_source_affine_derivatives(
            b"one", b"two", b"three", b"four", b"five",
            b"six", b"seven", b"eight", b"nine", b"ten",
        )
        self.assertEqual(len(set(result["source_sha256"])), 10)
        self.assertEqual(result["map_count"], 10)
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["derivative_positive"])
        self.assertEqual(result["derivative_interval"][0], result["derivative_interval"][1])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["new_law_claim"])

    def test_scm_six_observer_quorums_intersect_in_two(self):
        result = six_observer_intersecting_certificates()
        self.assertEqual(result["observer_count"], 6)
        self.assertEqual(result["quorum"], 4)
        self.assertEqual(result["certificate_intersection_size"], 2)
        self.assertEqual(result["minimum_quorum_intersection"], 2)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 8)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v23_compresses_and_binds_minimal_proof(self):
        result = lineage_manifest_v23(b"cycle033 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertEqual(result["selected_leaf_count"], 4)
        self.assertEqual(result["compressed_proof_node_count"], 3)
        self.assertEqual(result["individual_proof_node_count"], 12)
        self.assertEqual(result["nonmembership_count"], 3)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_eleven_pairs_bind_aggregate_resource_proofs(self):
        result = eleven_inverse_pairs_aggregate_resources()
        self.assertEqual(len(result["inverse_pair_names"]), 11)
        self.assertEqual(result["proof_count"], 11)
        self.assertTrue(result["all_inclusion_proofs_valid"])
        self.assertTrue(result["proof_aggregate_mutation_rejected"])
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {"gates": 200, "depth": 35, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle033_fixture(b"cycle033 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
