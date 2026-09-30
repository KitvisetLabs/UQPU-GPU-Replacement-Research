import tempfile
import unittest

from uqpu.cycle030_delta01 import (
    LANES,
    eight_inverse_pairs_program_tree,
    four_reader_directory_atomicity,
    fourteen_component_covariance_grid,
    fourteen_scenario_deletion_intervals,
    integer_escaped_key_receipt_gate,
    lineage_manifest_v20,
    run_cycle030_fixture,
    seven_source_affine_maps,
    signed_block_covariance_transform,
    ten_issuer_two_level_revocation,
    tenth_graph_double_orbits,
    transcript_fork_stale_controls,
    zip64_local_central_full_bind,
)


class Cycle030Tests(unittest.TestCase):
    def test_a_tenth_graph_binds_complement_stabilizer_double_orbits(self):
        result = tenth_graph_double_orbits()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [31, 38])
        self.assertEqual(result["witness_counts"], [10, 8])
        self.assertEqual(result["changed_edge_indices"], [0])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertEqual(result["dihedral_transform_count"], 22)
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertEqual(sum(map(len, result["complement_stabilizer_double_orbits"])), 8)
        self.assertTrue(all(len(orbit) == 2 for orbit in result["complement_stabilizer_double_orbits"]))
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_integer_and_escaped_key_controls_reject(self):
        result = integer_escaped_key_receipt_gate()
        self.assertTrue(result["escaped_key_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"]["max_exact_integer"], 2 ** 53 - 1)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_four_readers_and_directory_snapshots_are_complete(self):
        with tempfile.TemporaryDirectory() as root:
            result = four_reader_directory_atomicity(root)
        self.assertEqual(result["reader_count"], 4)
        self.assertEqual(len(result["runs"]), 4)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(result["all_targets_declared"])
        self.assertTrue(all(all(count > 0 for count in row["reader_counts"])
                            for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23] for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_local_central_fields_and_extras_bind(self):
        result = zip64_local_central_full_bind()
        self.assertEqual(result["signed_unsigned_valid"], [True, True])
        self.assertTrue(result["unknown_extra_preserved"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_ten_issuer_two_level_revocation_fails_closed(self):
        result = ten_issuer_two_level_revocation()
        self.assertEqual(result["event_count"], 10)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_fourteen_component_source_bound_grid_keeps_nulls(self):
        result = fourteen_component_covariance_grid(b"cycle030 covariance source")
        self.assertEqual(result["components"], 14)
        self.assertEqual(result["sigma_values"], [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0])
        self.assertEqual(len(result["covariance_grid_sha256"]), 64)
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_signed_block_transform_preserves_declared_invariants(self):
        result = signed_block_covariance_transform()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["signed_correlation_index_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_signed_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_six_deletion_depths_are_exhaustive(self):
        result = fourteen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 14)
        self.assertEqual(result["full_grid_size"], 336)
        self.assertEqual(sum(result["winner_counts"]), 336)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 14, "2": 91, "3": 364, "4": 1001, "5": 2002, "6": 3003,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [17, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_seven_affine_maps_roundtrip_and_reject_mutations(self):
        result = seven_source_affine_maps(
            b"one", b"two", b"three", b"four", b"five", b"six", b"seven"
        )
        self.assertEqual(len(set(result["source_sha256"])), 7)
        self.assertEqual(result["map_count"], 7)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_fork_and_stale_head_controls_stay_fiction_only(self):
        result = transcript_fork_stale_controls()
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 8)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v20_binds_membership_and_nonmembership(self):
        result = lineage_manifest_v20(b"cycle030 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertEqual(result["heldout_path_count"], 3)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(all(result["mutation_rejections"].values()))
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_eight_pairs_bind_program_tree_and_reconstruct(self):
        result = eight_inverse_pairs_program_tree()
        self.assertEqual(len(result["inverse_pair_names"]), 8)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {"gates": 164, "max_qubits": 6})
        self.assertEqual(result["tree_resource_sum"], 164)
        self.assertTrue(result["tree_mutation_rejected"])
        self.assertTrue(result["resource_accounting_valid"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle030_fixture(b"cycle030 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
