import tempfile
import unittest
from pathlib import Path
from uqpu.cycle021_delta01 import (
    LANES, custody_validity_start_expiry, covariance_order_mutation, scm_revoked_replay,
    lineage_v11, maxcut_perturbation_ties, noncommuting_qos_pair, rational_reciprocal_conversion,
    receipt_nested_mutations, repeated_exit_cleanup_three, run_cycle021_fixture,
    sixth_ranking_scenario, six_component_covariance, zip_extra_order_duplicate,
)

class Cycle021Tests(unittest.TestCase):
    def test_a_edge_perturbation_changes_tied_objective_and_keeps_unmodified_edges(self):
        result=maxcut_perturbation_ties()
        self.assertEqual(result["states"],[2048,2048])
        self.assertEqual(result["objectives"],[10,11])
        self.assertTrue(result["unchanged_edges_invariant"])
        self.assertTrue(result["task_hash_changed"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_nested_receipt_duplicate_key_and_key_rotation_controls(self):
        result=receipt_nested_mutations()
        self.assertTrue(result["duplicate_nested_rejected"])
        self.assertTrue(result["key_rotation_changes_bytes"])
        self.assertIsNone(result["provider_claim"])
        self.assertIsNone(result["external_authority_job_invoice"])

    def test_c_three_repeated_subprocess_exit_sets_keep_complete_bytes(self):
        with tempfile.TemporaryDirectory() as root:
            result=repeated_exit_cleanup_three(root)
        self.assertEqual(result["exit_codes"],[[0,23,23]]*4)
        self.assertEqual(result["complete"],[True]*4)
        self.assertIsNone(result["crash_durability"])

    def test_d_extra_field_order_passes_duplicate_zip64_rejects(self):
        result=zip_extra_order_duplicate()
        self.assertTrue(result["unrelated_field_order_accepted"])
        self.assertTrue(result["duplicate_zip64_field_rejected"])
        self.assertEqual(result["descriptor_forms"],["signed","unsigned"])
        self.assertFalse(result["payload_read"])

    def test_e_issuer_validity_start_expiry_and_revocation_boundaries(self):
        result=custody_validity_start_expiry()
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNotNone(result["terminal_sha256"])
        self.assertIsNone(result["physical_sample"])

    def test_f_six_component_covariance_invalid_and_zero_cases_null(self):
        result=six_component_covariance()
        self.assertEqual(result["components"],6)
        scenarios=result["model"]["scenarios"]
        for name in ("missing","indefinite","nonfinite"):
            self.assertTrue(all(row["per_output_usd"] is None for row in scenarios[name]["outputs"]))
        self.assertIsNone(scenarios["independent"]["outputs"][-1]["per_output_usd"])

    def test_g_typed_covariance_order_mutation_and_dimensions(self):
        result=covariance_order_mutation()
        self.assertEqual(len(result["order"]),4)
        self.assertTrue(result["order_mutation_rejected"])
        self.assertEqual(result["pairwise_entry_count"],16)
        self.assertTrue(result["positive_semidefinite"])
        self.assertIsNone(result["calibration"])

    def test_h_sixth_ranking_alternative_enumerates_all_orders(self):
        result=sixth_ranking_scenario()
        self.assertEqual(result["scenario_count"],6)
        self.assertEqual(result["orders_each"],24)
        self.assertEqual(sum(result["winner_counts"]),144)
        self.assertEqual(result["stability_bounds"],[5/24,0.375])
        self.assertIsNone(result["capital"])

    def test_fnd_exact_reciprocal_conversion_and_source_binding(self):
        result=rational_reciprocal_conversion(b"umrl source fixture")
        self.assertEqual(result["meters_to_kilometers"],[1,1000])
        self.assertEqual(result["roundtrip_meters"],[1,1])
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertTrue(result["incompatible_dimension_rejected"])

    def test_scm_revoked_consent_and_replay_fail_in_fiction(self):
        result=scm_revoked_replay("2026-09-28")
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertEqual(result["sort"],"Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v11_split_order_and_missing_metric_gates(self):
        result=lineage_v11(b"lineage fixture")
        self.assertEqual(result["manifest"]["version"],11)
        self.assertTrue(result["split_order_mutation_rejected"])
        self.assertIsNone(result["missing_heldout_metric_candidate"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_noncommuting_pair_inverse_reconstructs_64_states(self):
        result=noncommuting_qos_pair()
        self.assertTrue(result["noncommuting_controls"])
        self.assertEqual(result["basis_states_checked"],64)
        self.assertEqual(result["residual"],0)
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle_fixture_advances_exactly_twelve_lanes(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[3]
        source=(root/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            result=run_cycle021_fixture(source,tmp)
        self.assertEqual(tuple(result),LANES)
        self.assertTrue(all(v["status"]=="BLOCKED_WITH_PROGRESS" for v in result.values()))

if __name__=="__main__": unittest.main()
