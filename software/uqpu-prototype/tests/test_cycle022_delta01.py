import tempfile
import unittest
from pathlib import Path
from uqpu.cycle022_delta01 import (
    LANES, alternating_process_cleanup, custody_two_event_rotation,
    descriptor_crc_crossbind, exact_interval_reciprocal,
    four_measurand_ratio_mutation, lineage_v12,
    nested_receipt_rotation, qos_second_pair, run_cycle022_fixture,
    scm_scoped_nonce_then_revocation, second_edge_perturbation,
    seventh_ranking_alternative, seven_component_covariance,
)

class Cycle022Tests(unittest.TestCase):
    def test_a_second_edge_perturbation_changes_witness_set_at_2048_states(self):
        result=second_edge_perturbation()
        self.assertEqual(result["state_counts"],[2048,2048])
        self.assertEqual(result["objectives"],[10,11])
        self.assertNotEqual(result["witness_set_hashes"][0],result["witness_set_hashes"][1])
        self.assertTrue(result["unchanged_edges_invariant"])
        self.assertTrue(result["task_hash_changed"])

    def test_b_nested_receipt_and_key_rotation_controls(self):
        result=nested_receipt_rotation()
        self.assertTrue(result["nested_canonicalization"])
        self.assertTrue(result["duplicate_nested_rejected"])
        self.assertTrue(result["key_revocation_negative"])
        self.assertIsNone(result["provider_claim"])

    def test_c_alternating_targets_keep_complete_old_or_new_bytes(self):
        with tempfile.TemporaryDirectory() as root:
            result=alternating_process_cleanup(root)
        self.assertEqual(result["exit_codes"],[[0,23,23]]*8)
        self.assertEqual(result["complete"],[True]*8)
        self.assertIsNone(result["crash_durability"])

    def test_d_descriptor_crc_binds_before_payload_read(self):
        result=descriptor_crc_crossbind()
        self.assertTrue(result["valid_crossbind"])
        self.assertTrue(result["descriptor_crc_mutation_rejected"])
        self.assertEqual(result["descriptor_forms"],["signed","unsigned"])
        self.assertFalse(result["payload_read"])

    def test_e_two_event_issuer_rotation_and_expiry_order(self):
        result=custody_two_event_rotation()
        self.assertIsNotNone(result["terminal_sha256"])
        self.assertTrue(all(result["negative_controls"].values()))
        self.assertIsNone(result["physical_sample"])

    def test_f_seven_component_covariance_invalid_and_zero_controls(self):
        result=seven_component_covariance()
        self.assertEqual(result["components"],7)
        scenarios=result["model"]["scenarios"]
        for name in ("missing","indefinite","nonfinite"):
            self.assertTrue(all(row["per_output_usd"] is None for row in scenarios[name]["outputs"]))
        self.assertIsNone(scenarios["independent"]["outputs"][-1]["per_output_usd"])
        self.assertIsNone(result["commercial_claim"])

    def test_g_four_measurand_ratio_mutation_rejects_and_binds_order(self):
        result=four_measurand_ratio_mutation()
        self.assertEqual(result["pairwise_products"],16)
        self.assertEqual(len(result["pairwise_unit_products"]),16)
        self.assertTrue(result["order_hash_bound"])
        self.assertTrue(result["symmetric"])
        self.assertTrue(result["psd_by_congruence"])
        self.assertTrue(result["ratio_mutation_rejected"])
        self.assertIsNone(result["calibration"])

    def test_h_seventh_ranking_alternative_enumerates_every_order(self):
        result=seventh_ranking_alternative()
        self.assertEqual(result["scenario_count"],7)
        self.assertEqual(result["orders_each"],24)
        self.assertEqual(sum(result["winner_counts"]),168)
        self.assertLessEqual(result["stability_bounds"][0],result["stability_bounds"][1])
        self.assertIsNone(result["capital"])

    def test_fnd_interval_reciprocal_cancels_exactly_and_binds_source(self):
        result=exact_interval_reciprocal(b"UMRL source fixture")
        self.assertEqual(result["kilometers"],[[1,2000],[1,500]])
        self.assertEqual(result["roundtrip_meters"],[[1,2],[2,1]])
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertTrue(result["incompatible_dimension_rejected"])

    def test_scm_replacement_then_revocation_is_fiction_only(self):
        result=scm_scoped_nonce_then_revocation("2026-09-28")
        self.assertTrue(result["replacement_nonce_revoked_before_use"])
        self.assertTrue(result["old_nonce_replay_rejected"])
        self.assertEqual(result["sort"],"Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v12_parent_and_split_order_mutations_reject(self):
        result=lineage_v12(b"lineage fixture")
        self.assertEqual(result["manifest"]["version"],12)
        self.assertTrue(result["parent_digest_mutation_rejected"])
        self.assertTrue(result["reordered_split_rejected"])
        self.assertIsNone(result["candidate_result"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_second_noncommuting_pair_reconstructs_all_states(self):
        result=qos_second_pair()
        self.assertTrue(result["noncommuting_controls"])
        self.assertEqual(result["basis_states_checked"],64)
        self.assertEqual(result["residual"],0)
        self.assertTrue(result["resource_mutation_rejected"])
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle_fixture_advances_all_twelve_lanes(self):
        root=Path(__file__).resolve().parents[3]
        source=(root/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        with tempfile.TemporaryDirectory() as tmp:
            result=run_cycle022_fixture(source,tmp)
        self.assertEqual(tuple(result),LANES)
        self.assertTrue(all(x["status"]=="BLOCKED_WITH_PROGRESS" for x in result.values()))

if __name__=="__main__": unittest.main()
