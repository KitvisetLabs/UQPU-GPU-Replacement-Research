import tempfile
import unittest

from uqpu.cycle025_delta01 import (
    LANES,
    alternating_process_termination,
    composed_source_bound_interval_maps,
    extended_consent_null_table,
    fifth_graph_perturbation,
    five_issuer_revocation_boundary,
    lineage_manifest_v15,
    nine_component_covariance_sweep,
    nine_scenario_leave_one_out,
    permuted_typed_covariance_roundtrip,
    run_cycle025_fixture,
    three_noncommuting_inverse_pairs,
    typed_receipt_scalar_gate,
    zip64_extra_field_cross_bind,
)


class Cycle025Tests(unittest.TestCase):
    def test_a_fifth_graph_perturbation_binds_complete_witness_change(self):
        result = fifth_graph_perturbation()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [11, 13])
        self.assertEqual(result["changed_edge_indices"], [8])
        self.assertTrue(result["complete_witness_sets_differ"])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_receipt_scalars_are_bound_and_adversaries_reject(self):
        result = typed_receipt_scalar_gate()
        self.assertTrue(result["reordering_invariant"])
        self.assertTrue(result["scalar_types_bound"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["byte_cap"], 256)
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_alternating_targets_recover_only_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result = alternating_process_termination(root)
        self.assertEqual(len(result["runs"]), 4)
        self.assertEqual(result["targets"], ["target-0.bin", "target-1.bin"])
        self.assertTrue(result["all_recovered_complete"])
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23]
                            for row in result["runs"]))
        self.assertTrue(all(len(item) == 64 for item in result["classified_digests"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_zip64_cross_bind_rejects_all_metadata_mutations(self):
        result = zip64_extra_field_cross_bind()
        self.assertEqual(result["descriptor_forms"], ["signed", "unsigned"])
        self.assertTrue(all(result["mutations_rejected_before_payload"].values()))
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_fifth_issuer_fails_closed_at_revocation_boundary(self):
        result = five_issuer_revocation_boundary()
        self.assertEqual(result["event_count"], 5)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_nine_component_sweep_retains_null_controls(self):
        result = nine_component_covariance_sweep()
        self.assertEqual(result["components"], 9)
        self.assertEqual(result["sigma_values"], [0.5, 1.0, 2.0, 3.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            self.assertIsNone(scenarios["correlated"]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_permuted_covariance_rescaling_has_exact_inverse(self):
        result = permuted_typed_covariance_roundtrip()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertEqual(result["permutation"], [2, 0, 3, 1])
        self.assertTrue(result["exact_inverse_roundtrip"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_congruence_and_permutation"])
        self.assertIsNone(result["calibration"])

    def test_h_nine_scenario_grid_and_leave_one_out_are_exhaustive(self):
        result = nine_scenario_leave_one_out()
        self.assertEqual(result["scenario_count"], 9)
        self.assertEqual(result["grid_size"], 216)
        self.assertEqual(sum(result["winner_counts"]), 216)
        self.assertEqual(len(result["leave_one_out_winner_counts"]), 9)
        self.assertTrue(all(sum(row) == 192
                            for row in result["leave_one_out_winner_counts"]))
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_two_source_bound_maps_roundtrip_exactly(self):
        result = composed_source_bound_interval_maps(b"map-one", b"map-two")
        self.assertEqual(len(result["source_sha256"]), 2)
        self.assertNotEqual(*result["source_sha256"])
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_extended_null_table_stays_fiction_only(self):
        result = extended_consent_null_table("2026-09-29")
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 7)
        by_case = {row["case"]: row for row in result["control_table"]}
        self.assertFalse(by_case["challenge_mismatch"]["accepted"])
        self.assertFalse(by_case["post_expiry_nonce_replacement"]["accepted"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v15_binds_membership_and_metric_schema(self):
        result = lineage_manifest_v15(b"cycle025 synthetic lineage")
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["heldout_membership_mutation_rejected"])
        self.assertTrue(result["metric_schema_mutation_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_three_pairs_reconstruct_all_states_and_do_not_commute(self):
        result = three_noncommuting_inverse_pairs()
        self.assertEqual(len(result["inverse_pair_names"]), 3)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertTrue(all(result["pairwise_noncommuting"].values()))
        self.assertEqual(result["resource_bound"], {"gates": 28, "max_qubits": 6})
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle025_fixture(b"cycle025 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
