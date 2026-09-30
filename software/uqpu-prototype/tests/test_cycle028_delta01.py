import tempfile
import unittest

from uqpu.cycle028_delta01 import (
    LANES,
    descriptor_extra_cross_bind,
    determinant_correlation_transform,
    dual_reader_atomicity,
    eight_issuer_time_controls,
    eighth_graph_dihedral_bindings,
    five_source_affine_maps,
    lineage_manifest_v18,
    magnitude_token_receipt_gate,
    run_cycle028_fixture,
    sequence_epoch_consent_controls,
    six_inverse_pairs_prefix_gate,
    twelve_component_covariance_envelope,
    twelve_scenario_deletion_intervals,
)


class Cycle028Tests(unittest.TestCase):
    def test_a_eighth_graph_binds_all_dihedral_transforms(self):
        result = eighth_graph_dihedral_bindings()
        self.assertEqual(result["states_each"], [2048, 2048])
        self.assertEqual(result["objectives"], [20, 25])
        self.assertEqual(result["witness_counts"], [14, 12])
        self.assertEqual(result["changed_edge_indices"], [10])
        self.assertTrue(result["unchanged_edges_identical"])
        self.assertEqual(result["dihedral_transform_count"], 22)
        self.assertTrue(result["all_dihedral_transforms_match"])
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_magnitude_and_token_caps_reject_every_control(self):
        result = magnitude_token_receipt_gate()
        self.assertTrue(result["negative_zero_and_exponent_equivalence"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["caps"], {
            "bytes": 256, "depth": 5, "tokens": 24, "magnitude": 10 ** 12,
        })
        self.assertIsNone(result["external_authority"])
        self.assertIsNone(result["provider_job_invoice"])

    def test_c_two_readers_observe_only_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result = dual_reader_atomicity(root)
        self.assertEqual(len(result["runs"]), 4)
        self.assertEqual(result["reader_count"], 2)
        self.assertTrue(result["all_reader_parent_observations_complete"])
        self.assertTrue(all(all(count > 0 for count in row["reader_counts"])
                            for row in result["runs"]))
        self.assertTrue(all(row["exit_codes"] == [0, 23, 23]
                            for row in result["runs"]))
        self.assertIsNone(result["crash_durability"])
        self.assertIsNone(result["power_loss_durability"])

    def test_d_descriptor_and_extra_records_cross_bind(self):
        result = descriptor_extra_cross_bind()
        self.assertEqual(result["descriptor_forms_valid"], [True, True])
        self.assertTrue(result["local_central_equal"])
        self.assertTrue(result["unknown_extra_preserved"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertFalse(result["signature_like_payload_read"])
        self.assertFalse(result["payload_read"])
        self.assertIsNone(result["real_producer_corpus"])

    def test_e_eight_issuer_time_controls_fail_closed(self):
        result = eight_issuer_time_controls()
        self.assertEqual(result["event_count"], 8)
        self.assertTrue(all(result["boundary_rejections"].values()))
        self.assertEqual(len(result["terminal_sha256"]), 64)
        self.assertIsNone(result["physical_sample"])

    def test_f_twelve_component_sweep_keeps_null_controls(self):
        result = twelve_component_covariance_envelope()
        self.assertEqual(result["components"], 12)
        self.assertEqual(result["sigma_values"], [0.0, 1.0, 2.0, 4.0, 6.0])
        for sweep in result["sweeps"].values():
            scenarios = sweep["scenarios"]
            for name in ("missing", "indefinite", "nonfinite"):
                self.assertTrue(all(row["per_output_usd"] is None
                                    for row in scenarios[name]["outputs"]))
            for name in ("positive", "zero", "negative"):
                self.assertIsNone(scenarios[name]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_interpretation"])

    def test_g_determinant_and_correlation_survive_transform(self):
        result = determinant_correlation_transform()
        self.assertEqual(result["matrix_product_count"], 16)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(result["determinant_scaling_invariant"])
        self.assertTrue(result["correlation_invariant"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_positive_congruence_and_permutation"])
        self.assertIsNone(result["calibration"])

    def test_h_four_deletion_depths_are_exhaustive(self):
        result = twelve_scenario_deletion_intervals()
        self.assertEqual(result["scenario_count"], 12)
        self.assertEqual(result["full_grid_size"], 288)
        self.assertEqual(sum(result["winner_counts"]), 288)
        self.assertEqual(result["deletion_grid_counts"], {
            "1": 12, "2": 66, "3": 220, "4": 495,
        })
        self.assertEqual(result["all_grid_interval"], [[1, 32], [13, 32]])
        self.assertIsNone(result["probability_claim"])
        self.assertIsNone(result["capital"])

    def test_fnd_five_affine_maps_roundtrip_and_reject_mutations(self):
        result = five_source_affine_maps(b"one", b"two", b"three", b"four", b"five")
        self.assertEqual(len(set(result["source_sha256"])), 5)
        self.assertEqual(len(result["maps"]), 5)
        self.assertTrue(result["exact_roundtrip"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"], ["RealModel", "Model"])
        self.assertIsNone(result["new_law_claim"])

    def test_scm_sequence_and_epoch_controls_stay_fiction_only(self):
        result = sequence_epoch_consent_controls("2026-09-30")
        self.assertTrue(result["all_controls_match"])
        self.assertEqual(len(result["control_table"]), 5)
        by_case = {row["case"]: row for row in result["control_table"]}
        self.assertFalse(by_case["sequence_replay"]["accepted"])
        self.assertFalse(by_case["sequence_skip"]["accepted"])
        self.assertFalse(by_case["epoch_downgrade"]["accepted"])
        self.assertEqual(result["sort"], "Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v18_binds_merkle_root_parent_and_schema(self):
        result = lineage_manifest_v18(b"cycle028 synthetic lineage")
        self.assertEqual(result["leaf_count"], 8)
        self.assertTrue(result["valid_manifest"])
        self.assertTrue(result["merkle_root_mutation_rejected"])
        self.assertTrue(result["schema_version_mutation_rejected"])
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_six_pairs_bind_prefixes_and_reconstruct(self):
        result = six_inverse_pairs_prefix_gate()
        self.assertEqual(len(result["inverse_pair_names"]), 6)
        self.assertEqual(len(result["prefix_program_sha256"]), 6)
        self.assertEqual(result["basis_states_checked"], 64)
        self.assertEqual(result["distinct_outputs"], 64)
        self.assertEqual(result["residual"], 0)
        self.assertGreater(result["order_mutation_witness_count"], 0)
        self.assertEqual(result["resource_bound"], {"gates": 88, "max_qubits": 6})
        self.assertTrue(result["resource_accounting_valid"])
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        with tempfile.TemporaryDirectory() as root:
            result = run_cycle028_fixture(b"cycle028 integrated source", root)
        self.assertEqual(tuple(result), LANES)
        self.assertTrue(all(item["status"] == "BLOCKED_WITH_PROGRESS"
                            for item in result.values()))


if __name__ == "__main__":
    unittest.main()
