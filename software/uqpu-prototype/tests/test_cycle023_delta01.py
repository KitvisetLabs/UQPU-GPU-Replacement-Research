import tempfile
import unittest
from pathlib import Path
from uqpu.cycle023_delta01 import (
    LANES, descriptor_size_mutations, eight_component_covariance, eighth_ranking_alternative,
    lineage_v13, malformed_receipt_gate, qos_third_noncommuting_pair,
    repeat_temp_name_cleanup, run_cycle023_fixture,
    second_rescaling_order_hash, second_unit_family, scoped_revoke_replay,
    third_custody_issuer, third_edge_perturbation,
)

class Cycle023Tests(unittest.TestCase):
    def test_a_third_edge_perturbation_is_exact_and_hash_bound(self):
        result=third_edge_perturbation()
        self.assertEqual(result["state_counts"],[2048,2048])
        self.assertEqual(result["objectives"],[10,12])
        self.assertTrue(result["witness_hash_changed"])
        self.assertTrue(result["unchanged_edges_invariant"])

    def test_b_duplicate_and_malformed_utf8_receipts_reject(self):
        result=malformed_receipt_gate()
        self.assertTrue(result["duplicate_key_rejected"])
        self.assertTrue(result["malformed_utf8_rejected"])
        self.assertIsNone(result["provider_claim"])

    def test_c_repeated_stale_cleanup_preserves_complete_payloads(self):
        with tempfile.TemporaryDirectory() as root:
            result=repeat_temp_name_cleanup(root)
        self.assertEqual(len(result["exit_codes"]),8)
        self.assertTrue(all(x==[0,23,23] for x in result["exit_codes"]))
        self.assertEqual(result["complete"],[True]*8)
        self.assertIsNone(result["crash_durability"])

    def test_d_descriptor_size_mutations_reject_before_payload(self):
        result=descriptor_size_mutations()
        self.assertTrue(result["valid"])
        self.assertTrue(result["descriptor_size_mutations_rejected"])
        self.assertEqual(result["descriptor_forms"],["signed","unsigned"])
        self.assertFalse(result["payload_read"])

    def test_e_third_custody_issuer_and_validity_controls(self):
        result=third_custody_issuer()
        self.assertEqual(result["issuer_count"],3)
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNotNone(result["terminal_sha256"])
        self.assertIsNone(result["physical_sample"])

    def test_f_eight_component_covariance_invalid_zero_controls(self):
        result=eight_component_covariance()
        self.assertEqual(result["components"],8)
        scenarios=result["model"]["scenarios"]
        for key in ("missing","indefinite","nonfinite"):
            self.assertTrue(all(row["per_output_usd"] is None for row in scenarios[key]["outputs"]))
        self.assertIsNone(scenarios["independent"]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_claim"])

    def test_g_second_rescaling_binds_order_and_psd(self):
        result=second_rescaling_order_hash()
        self.assertEqual(len(result["pairwise_products"]),16)
        self.assertTrue(result["order_mutation_rejected"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_congruence"])
        self.assertIsNone(result["calibration"])

    def test_h_eighth_ranking_scenario_enumerates_all_orders(self):
        result=eighth_ranking_alternative()
        self.assertEqual(result["scenario_count"],8)
        self.assertEqual(result["orders_each"],24)
        self.assertEqual(sum(result["winner_counts"]),192)
        self.assertLessEqual(result["stability_bounds"][0],result["stability_bounds"][1])
        self.assertIsNone(result["capital"])

    def test_fnd_two_unit_families_cancel_exactly(self):
        result=second_unit_family(b"umrl fixture")
        self.assertEqual(result["meter_interval_km"],[[1,2000],[1,500]])
        self.assertEqual(result["roundtrip_meters"],[[1,2],[2,1]])
        self.assertEqual(result["seconds_to_milliseconds"],[1500,1])
        self.assertEqual(result["milliseconds_roundtrip"],[3,2])
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertTrue(result["incompatible_dimension_rejected"])

    def test_scm_revoked_scope_bound_replay_rejects_in_fiction(self):
        result=scoped_revoke_replay("2026-09-28")
        self.assertTrue(result["scope_bound"])
        self.assertTrue(result["replay"])
        self.assertTrue(result["revoked"])
        self.assertEqual(result["sort"],"Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v13_parent_and_split_overlap_controls(self):
        result=lineage_v13(b"lineage fixture")
        self.assertEqual(result["manifest"]["version"],13)
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertTrue(result["split_overlap_rejected"])
        self.assertIsNone(result["missing_heldout_candidate"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_third_noncommuting_inverse_reconstructs_64_states(self):
        result=qos_third_noncommuting_pair()
        self.assertTrue(result["noncommuting"])
        self.assertEqual(result["basis_states_checked"],64)
        self.assertEqual(result["residual"],0)
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_fixture_advances_exactly_twelve_lanes(self):
        root=Path(__file__).resolve().parents[3]
        source=(root/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            result=run_cycle023_fixture(source,tmp)
        self.assertEqual(tuple(result),LANES)
        self.assertTrue(all(x["status"]=="BLOCKED_WITH_PROGRESS" for x in result.values()))

if __name__=="__main__": unittest.main()
