import tempfile
import unittest

from uqpu.cycle031_delta01 import (
    LANES,
    composed_signed_block_transforms,
    eight_source_affine_maps,
    eleventh_graph_witness_quotient,
    eleven_issuer_revocation_quorum,
    fifteen_component_ordered_covariance,
    fifteen_scenario_deletion_intervals,
    five_reader_descriptor_atomicity,
    lineage_manifest_v21,
    nine_inverse_pairs_resource_merkle,
    run_cycle031_fixture,
    transcript_equivocation_quorum_controls,
    unicode_value_receipt_gate,
    zip64_name_version_bind,
)


class Cycle031Tests(unittest.TestCase):
    def test_a_eleventh_graph_binds_complement_stabilizer_quotient(self):
        result = eleventh_graph_witness_quotient()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [38, 46])
        self.assertEqual(result["witness_counts"], [8, 6])
        self.assertEqual(result["changed_edge_indices"], [2])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertEqual(result["dihedral_transform_count"], 22)
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertEqual(result["stabilizer"], [[1, 0]])
        self.assertEqual(sum(len(row["members"]) for row in result["witness_quotient"]), 6)
        self.assertTrue(all(len(row["members"]) == 2 for row in result["witness_quotient"]))
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_unicode_values_and_normalized_key_collisions_bind(self):
        result = unicode_value_receipt_gate()
        self.assertTrue(result["normalized_value_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"]["max_exact_integer"], 2 ** 53 - 1)
        self.assertEqual(result["caps"]["normalized_string_length"], 16)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_five_readers_and_held_descriptors_are_complete(self):
        with tempfile.TemporaryDirectory() as root:
            result = five_reader_descriptor_atomicity(root)
        self.assertEqual(result["reader_count"], 5)
        self.assertEqual(len(result["runs"]), 4)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(result["all_held_descriptors_complete"])
        self.assertTrue(all(all(count > 0 for count in row["reader_counts"])
                            for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23] for row in result["runs"]))
        self.assertTrue(all(row["held_descriptor_old_complete"] for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_names_versions_and_descriptors_bind(self):
        result = zip64_name_version_bind()
        self.assertEqual(result["signed_unsigned_valid"], [True, True])
        self.assertEqual(result["filename_utf8"], "cycle031-Δ.bin")
        self.assertTrue(result["unknown_extra_preserved"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_eleven_issuer_revocation_quorum_fails_closed(self):
        result = eleven_issuer_revocation_quorum()
        self.assertEqual(result["event_count"], 11)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_fifteen_component_ordered_grid_keeps_nulls(self):
        result = fifteen_component_ordered_covariance(b"cycle031 covariance source")
        self.assertEqual(result["components"], 15)
        self.assertEqual(len(result["component_order"]), 15)
        self.assertEqual(result["sigma_values"], [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0])
        self.assertTrue(result["order_mutation_rejected"])
        self.assertEqual(len(result["covariance_grid_sha256"]), 64)
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_two_signed_block_transforms_preserve_invariants(self):
        result = composed_signed_block_transforms()
        self.assertEqual(result["transform_count"], 2)
        self.assertEqual(result["matrix_product_count"], 32)
        self.assertTrue(result["exact_composition_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_signed_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_seven_deletion_depths_are_exhaustive(self):
        result = fifteen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 15)
        self.assertEqual(result["full_grid_size"], 360)
        self.assertEqual(sum(result["winner_counts"]), 360)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 15, "2": 105, "3": 455, "4": 1365,
            "5": 3003, "6": 5005, "7": 6435,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [19, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_eight_affine_maps_roundtrip_and_reject_mutations(self):
        result = eight_source_affine_maps(
            b"one", b"two", b"three", b"four",
            b"five", b"six", b"seven", b"eight",
        )
        self.assertEqual(len(set(result["source_sha256"])), 8)
        self.assertEqual(result["map_count"], 8)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_equivocation_quorum_controls_stay_fiction_only(self):
        result = transcript_equivocation_quorum_controls()
        self.assertEqual(result["observer_count"], 4)
        self.assertEqual(result["quorum"], 3)
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 8)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v21_binds_indices_directions_and_nonmembership(self):
        result = lineage_manifest_v21(b"cycle031 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertEqual(result["nonmembership_count"], 2)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_nine_inverse_pairs_bind_resources_and_reconstruct(self):
        result = nine_inverse_pairs_resource_merkle()
        self.assertEqual(len(result["inverse_pair_names"]), 9)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {"gates": 176, "max_qubits": 6})
        self.assertEqual(result["tree_resource_sum"], 176)
        self.assertTrue(result["tree_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle031_fixture(b"cycle031 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
