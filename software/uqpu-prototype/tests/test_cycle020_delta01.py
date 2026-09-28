import tempfile
import unittest
from pathlib import Path
from uqpu.cycle020_delta01 import (
    LANES, all_measurand_rescaling, custody_expiry_revocation, fifth_ranking_scenario,
    fiction_revocation_before_use, five_component_covariance, lineage_v10,
    maxcut_11_boundary, nested_receipt_gate, rational_conversion_path,
    repeated_process_cleanup, run_cycle020_fixture, second_qos_permutation,
    zip64_extended_crossbind,
)

class Cycle020Tests(unittest.TestCase):
    def test_a_11_node_boundary_enumerates_exactly_2048_states(self):
        result=maxcut_11_boundary()
        self.assertEqual(result["state_count"],2048)
        self.assertEqual(result["objective"],10)
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_nested_receipt_keys_and_rotation_mutations(self):
        result=nested_receipt_gate()
        self.assertTrue(result["nested_duplicate_rejected"])
        self.assertTrue(result["key_rotation_changes_bytes"])
        self.assertIsNone(result["external_authority_job_invoice"])
        self.assertIsNone(result["provider_claim"])

    def test_c_repeated_process_failure_boundaries_keep_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result=repeated_process_cleanup(root)
        self.assertEqual(result["exit_codes"],[[0,23,23],[0,23,23]])
        self.assertEqual(result["complete"],[True,True])
        self.assertIsNone(result["crash_durability"])

    def test_d_local_central_offset_mutation_rejects_with_both_descriptor_forms(self):
        result=zip64_extended_crossbind()
        self.assertTrue(result["cross_bound"])
        self.assertEqual(result["descriptor_forms"],["signed","unsigned"])
        self.assertTrue(result["offset_mutation_rejected"])
        self.assertFalse(result["payload_read"])

    def test_e_expiry_boundary_and_revocation_fail_closed(self):
        result=custody_expiry_revocation()
        self.assertTrue(result["expiry_boundary_rejected"])
        self.assertTrue(result["revocation_rejected"])
        self.assertIsNotNone(result["valid_terminal"])
        self.assertIsNone(result["physical_sample"])

    def test_f_five_component_covariance_failures_and_zero_denominator_null(self):
        result=five_component_covariance()
        self.assertEqual(result["components"],5)
        scenarios=result["model"]["scenarios"]
        self.assertEqual(len(scenarios["independent"]["outputs"]),4)
        for name in ("missing","indefinite","nonfinite"):
            self.assertTrue(all(row["per_output_usd"] is None for row in scenarios[name]["outputs"]))
        self.assertIsNone(scenarios["independent"]["outputs"][-1]["per_output_usd"])

    def test_g_all_measurands_rescale_pairwise_covariance_and_preserve_psd(self):
        result=all_measurand_rescaling()
        self.assertEqual(len(result["order"]),4)
        self.assertEqual(len(result["pairwise_product_units"]),10)
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_fifth_adverse_scenario_enumerates_all_candidate_orders(self):
        result=fifth_ranking_scenario()
        self.assertEqual(result["scenario_count"],5)
        self.assertEqual(result["orders_each"],24)
        self.assertEqual(sum(result["winner_counts"]),120)
        self.assertEqual(result["stability_bounds"],[0.15,0.45])
        self.assertIsNone(result["capital"])

    def test_fnd_rational_conversion_keeps_exact_source_and_rejects_bad_types(self):
        result=rational_conversion_path(b"UMRL fixture")
        self.assertEqual(result["meters_to_centimeters"],[100,1])
        self.assertEqual(result["roundtrip_meters"],[1,1])
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertTrue(result["incompatible_dimension_rejected"])

    def test_scm_revocation_before_use_stays_fictional(self):
        result=fiction_revocation_before_use("2026-09-28")
        self.assertTrue(result["revoked_before_use_rejected"])
        self.assertEqual(result["sort"],"Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v10_detects_parent_corruption_and_split_leak(self):
        result=lineage_v10(b"lineage fixture")
        self.assertEqual(result["manifest"]["version"],10)
        self.assertTrue(result["parent_corruption_rejected"])
        self.assertTrue(result["heldout_leakage_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_second_nonidentity_pair_reconstructs_64_states(self):
        result=second_qos_permutation()
        self.assertEqual(result["basis_states_checked"],64)
        self.assertEqual(result["residual"],0)
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle_fixture_advances_exactly_twelve_lanes(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[3]
        source=(root/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            result=run_cycle020_fixture(source,tmp)
        self.assertEqual(tuple(result),LANES)
        self.assertTrue(all(v["status"]=="BLOCKED_WITH_PROGRESS" for v in result.values()))

if __name__=="__main__":
    unittest.main()
