import tempfile
import unittest

from uqpu.cycle029_delta01 import (
    LANES,
    block_basis_covariance_transform,
    duplicate_lexical_receipt_gate,
    lineage_manifest_v19,
    nine_issuer_revocation_controls,
    ninth_graph_stabilizer_partition,
    run_cycle029_fixture,
    seven_inverse_pairs_segment_gate,
    six_source_affine_maps,
    thirteen_component_covariance_grid,
    thirteen_scenario_deletion_intervals,
    transcript_hash_chain_controls,
    triple_reader_inode_atomicity,
    zip64_header_descriptor_bind,
)


class Cycle029Tests(unittest.TestCase):
    def test_a_ninth_graph_binds_stabilizer_partition(self):
        result = ninth_graph_stabilizer_partition()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [25, 31])
        self.assertEqual(result["witness_counts"], [12, 10])
        self.assertEqual(result["changed_edge_indices"], [7])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertEqual(result["dihedral_transform_count"], 22)
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertEqual(sum(map(len, result["stabilizer_orbit_partition"])), 10)
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_duplicate_and_lexical_controls_reject(self):
        result = duplicate_lexical_receipt_gate()
        self.assertTrue(result["accepted_lexical_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"]["exponent_abs"], 12)
        self.assertEqual(result["caps"]["fraction_digits"], 6)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_three_readers_observe_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result = triple_reader_inode_atomicity(root)
        self.assertEqual(result["reader_count"], 3)
        self.assertEqual(len(result["runs"]), 4)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(all(all(count > 0 for count in row["reader_counts"])
                            for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23] for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_header_and_descriptor_controls_reject(self):
        result = zip64_header_descriptor_bind()
        self.assertEqual(result["descriptor_forms_valid"], [True, True])
        self.assertTrue(result["reordered_extra_maps_equal"])
        self.assertTrue(result["unknown_extra_preserved"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_nine_issuer_revocation_and_ancestry_fail_closed(self):
        result = nine_issuer_revocation_controls()
        self.assertEqual(result["event_count"], 9)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_thirteen_component_grid_keeps_null_controls(self):
        result = thirteen_component_covariance_grid()
        self.assertEqual(result["components"], 13)
        self.assertEqual(result["sigma_values"], [0.0, 1.0, 2.0, 3.0, 5.0, 8.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_block_basis_preserves_typed_invariants(self):
        result = block_basis_covariance_transform()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(result["trace_invariant"])
        self.assertTrue(result["determinant_invariant"])
        self.assertTrue(result["correlation_permutation_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_permutation_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_five_deletion_depths_are_exhaustive(self):
        result = thirteen_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 13)
        self.assertEqual(result["full_grid_size"], 312)
        self.assertEqual(sum(result["winner_counts"]), 312)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 13, "2": 78, "3": 286, "4": 715, "5": 1287,
        })
        self.assertEqual(result["all_grid_interval"], [[0, 1], [17, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_six_affine_maps_roundtrip_and_reject_mutations(self):
        result = six_source_affine_maps(b"one", b"two", b"three", b"four", b"five", b"six")
        self.assertEqual(len(set(result["source_sha256"])), 6)
        self.assertEqual(result["map_count"], 6)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_hash_chain_controls_stay_fiction_only(self):
        result = transcript_hash_chain_controls()
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 6)
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v19_binds_heldout_inclusion_paths(self):
        result = lineage_manifest_v19(b"cycle029 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertEqual(result["heldout_path_count"], 3)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["path_mutation_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertTrue(result["schema_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_seven_pairs_bind_segments_and_reconstruct(self):
        result = seven_inverse_pairs_segment_gate()
        self.assertEqual(len(result["inverse_pair_names"]), 7)
        self.assertEqual(len(result["prefix_program_sha256"]), 7)
        self.assertEqual(len(result["suffix_program_sha256"]), 7)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertEqual(result["order_mutation_witness_count"], 64)
        self.assertEqual(result["resource_bound"], {"gates": 123, "max_qubits": 6})
        self.assertTrue(result["resource_accounting_valid"])
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle029_fixture(b"cycle029 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
