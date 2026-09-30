import tempfile
import unittest

from uqpu.cycle032_delta01 import (
    LANES,
    five_observer_branch_certificate,
    lineage_manifest_v22,
    nine_source_affine_associativity,
    recursive_unicode_numeric_receipt_gate,
    run_cycle032_fixture,
    six_reader_chained_atomicity,
    sixteen_component_block_covariance,
    sixteen_scenario_deletion_intervals,
    ten_inverse_pairs_merkle_proofs,
    three_signed_block_transforms,
    twelve_issuer_threshold_receipts,
    twelfth_graph_burnside_quotient,
    zip64_eocd_locator_bind,
)


class Cycle032Tests(unittest.TestCase):
    def test_a_twelfth_graph_burnside_count_matches_direct_quotient(self):
        result = twelfth_graph_burnside_quotient()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [46, 56])
        self.assertEqual(result["witness_counts"], [6, 4])
        self.assertEqual(result["changed_edge_indices"], [4])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertEqual(result["dihedral_transform_count"], 22)
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertEqual(result["stabilizer"], [[1, 0]])
        self.assertEqual(result["action_count"], 2)
        self.assertEqual(result["fixed_point_counts"], [4, 0])
        self.assertEqual(result["burnside_orbit_count"], len(result["direct_quotient"]))
        self.assertTrue(result["burnside_matches_direct"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_recursive_unicode_numeric_equivalence_and_caps(self):
        result = recursive_unicode_numeric_receipt_gate()
        self.assertTrue(result["recursive_numeric_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"]["max_exact_integer"], 2 ** 53 - 1)
        self.assertEqual(result["caps"]["depth"], 6)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_six_readers_two_replacements_and_retained_descriptors(self):
        with tempfile.TemporaryDirectory() as root:
            result = six_reader_chained_atomicity(root)
        self.assertEqual(result["reader_count"], 6)
        self.assertEqual(result["replacement_stages"], 2)
        self.assertEqual(len(result["runs"]), 3)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(result["all_retained_descriptors_complete"])
        self.assertTrue(all(all(count > 0 for count in row["reader_counts"])
                            for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [[0, 23, 23], [0, 23, 23]]
                            for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_eocd_locator_and_metadata_bind(self):
        result = zip64_eocd_locator_bind()
        self.assertEqual(result["signed_unsigned_valid"], [True, True])
        self.assertEqual(result["filename_utf8"], "cycle032-Ω.bin")
        self.assertEqual(result["eocd_record_size"], 56)
        self.assertEqual(result["locator_size"], 20)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_twelve_issuer_threshold_receipts_fail_closed(self):
        result = twelve_issuer_threshold_receipts()
        self.assertEqual(result["event_count"], 12)
        self.assertEqual(result["receipt_authority_count"], 3)
        self.assertEqual(result["receipt_threshold"], 2)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(result["signature_kind"],
                         "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE")
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_sixteen_component_block_grid_keeps_nulls(self):
        result = sixteen_component_block_covariance(b"cycle032 covariance source")
        self.assertEqual(result["components"], 16)
        self.assertEqual(len(result["component_order"]), 16)
        self.assertEqual(len(result["block_layout"]), 16)
        self.assertEqual(result["sigma_values"], [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0])
        self.assertTrue(all(result["binding_mutation_rejections"].values()))
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_three_signed_transforms_are_associative_and_invertible(self):
        result = three_signed_block_transforms()
        self.assertEqual(result["transform_count"], 3)
        self.assertEqual(result["matrix_product_count"], 48)
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_reverse_order_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_signed_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_eight_deletion_depths_are_exhaustive(self):
        result = sixteen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 16)
        self.assertEqual(result["full_grid_size"], 384)
        self.assertEqual(sum(result["winner_counts"]), 384)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 16, "2": 120, "3": 560, "4": 1820,
            "5": 4368, "6": 8008, "7": 11440, "8": 12870,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [19, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_nine_affine_maps_associate_roundtrip_and_reject(self):
        result = nine_source_affine_associativity(
            b"one", b"two", b"three", b"four", b"five",
            b"six", b"seven", b"eight", b"nine",
        )
        self.assertEqual(len(set(result["source_sha256"])), 9)
        self.assertEqual(result["map_count"], 9)
        self.assertTrue(result["associative_composition"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_five_observer_quorum_controls_stay_fiction_only(self):
        result = five_observer_branch_certificate()
        self.assertEqual(result["observer_count"], 5)
        self.assertEqual(result["quorum"], 4)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 8)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v22_binds_multiproof_order_and_boundaries(self):
        result = lineage_manifest_v22(b"cycle032 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertEqual(result["multiproof_leaf_count"], 4)
        self.assertEqual(result["boundary_nonmembership_count"], 2)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_ten_inverse_pairs_bind_merkle_inclusion_proofs(self):
        result = ten_inverse_pairs_merkle_proofs()
        self.assertEqual(len(result["inverse_pair_names"]), 10)
        self.assertEqual(result["proof_count"], 10)
        self.assertTrue(result["all_inclusion_proofs_valid"])
        self.assertTrue(result["proof_direction_mutation_rejected"])
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {"gates": 182, "max_qubits": 6})
        self.assertEqual(result["tree_resource_sum"], 182)
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle032_fixture(b"cycle032 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
