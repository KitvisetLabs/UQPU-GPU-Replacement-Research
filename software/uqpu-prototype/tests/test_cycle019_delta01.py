import tempfile
import unittest
from uqpu.cycle019_delta01 import (
    LANES, canonical_receipt_bytes, custody_rotation_order, fourth_ranking_alternative,
    four_component_covariance, fiction_scoped_nonce, lineage_v9, nonidentity_qos_inverse,
    process_exit_boundary_gate, receipt_ambiguity_gate, run_cycle019_fixture,
    source_bound_composition, tie_boundary_maxcut, unit_rescale_covariance, zip64_descriptor_forms,
)


class Cycle019Tests(unittest.TestCase):
    def test_a_tie_boundary_is_deterministic_and_exact(self):
        result=tie_boundary_maxcut()
        self.assertEqual(result["state_count"],1024)
        self.assertEqual(result["objective"],10)
        self.assertTrue(result["deterministic"])
        self.assertIsNone(result["scaling_claim"])

    def test_b_unicode_canonicalization_duplicate_and_revoked_key_controls(self):
        result=receipt_ambiguity_gate()
        self.assertTrue(result["canonical_unicode_equal"])
        self.assertTrue(result["duplicate_normalized_key_rejected"])
        self.assertTrue(result["revoked_key_rejected"])
        with self.assertRaises(ValueError):
            canonical_receipt_bytes(b'{"a":1,"a":2}')

    def test_c_process_exit_boundaries_show_complete_old_or_new_payload(self):
        with tempfile.TemporaryDirectory() as root:
            result=process_exit_boundary_gate(root)
        self.assertEqual(result["exit_codes"],[0,23,23])
        self.assertTrue(result["visible_complete"])
        self.assertTrue(result["old_or_new"])
        self.assertIsNone(result["crash_durability"])

    def test_d_signed_and_unsigned_zip64_descriptor_forms(self):
        result=zip64_descriptor_forms()
        self.assertEqual(result["forms"],["signed","unsigned"])
        self.assertTrue(result["mismatch_rejected_before_payload"])
        self.assertFalse(result["payload_read"])

    def test_e_rotated_issuer_and_revoked_old_chain(self):
        result=custody_rotation_order()
        self.assertTrue(result["rotation_valid"])
        self.assertTrue(result["revoked_old_chain_rejected"])
        self.assertIsNone(result["physical_sample"])

    def test_f_four_component_covariance_invalid_and_zero_output_controls(self):
        result=four_component_covariance()
        self.assertEqual(result["components"],4)
        self.assertEqual(len(result["result"]["scenarios"]["independent"]["outputs"]),4)
        self.assertIsNone(result["result"]["scenarios"]["independent"]["outputs"][-1]["per_output_usd"])
        for scenario in ("indefinite", "nonfinite"):
            self.assertTrue(all(row["per_output_usd"] is None for row in result["result"]["scenarios"][scenario]["outputs"]))
        self.assertIsNone(result["commercial_claim"])

    def test_g_unit_rescaling_preserves_psd_and_scales_cross_covariance(self):
        result=unit_rescale_covariance()
        self.assertTrue(result["cross_covariance_scaled"])
        self.assertTrue(result["psd_before_after"])
        self.assertIsNone(result["calibration"])

    def test_h_fourth_ranking_alternative_stays_finite_and_noncommercial(self):
        result=fourth_ranking_alternative()
        self.assertEqual(len(result["alternatives"]),4)
        self.assertEqual(result["orders_each"],24)
        self.assertEqual(result["stability_bounds"],[0.0,0.5])
        self.assertIsNone(result["capital"])

    def test_fnd_exact_source_bound_composition(self):
        result=source_bound_composition(b"fixture-source")
        self.assertTrue(result["source_mismatch_rejected"])
        self.assertEqual(result["sort"],["RealModel","Model"])
        self.assertTrue(result["exact_paths_agree"])
        self.assertEqual(result["associative_paths"],[[1,1],[1,1]])

    def test_scm_nonce_scope_and_expiry_are_fiction_only(self):
        result=fiction_scoped_nonce("2026-09-28")
        self.assertTrue(result["fresh"])
        self.assertTrue(all(result["rejections"].values()))
        self.assertEqual(result["sort"],"Fiction")
        self.assertIsNone(result["empirical_coupling"])

    def test_ai_cost_v9_parent_digest_and_missing_heldout_are_null(self):
        result=lineage_v9(b"fixture-source")
        self.assertEqual(result["manifest"]["version"],9)
        self.assertTrue(result["parent_mutation_rejected"])
        self.assertIsNone(result["missing_heldout_candidate"])
        self.assertIsNone(result["functional_equivalence"])

    def test_qos_nonidentity_inverse_reconstructs_64_states(self):
        result=nonidentity_qos_inverse()
        self.assertEqual(result["basis_states_checked"],64)
        self.assertEqual(result["residual"],0)
        self.assertIsNone(result["hardware"])

    def test_integrated_cycle_fixture_advances_exactly_twelve_lanes(self):
        from pathlib import Path
        root=Path(__file__).resolve().parents[3]
        source=(root/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        result=run_cycle019_fixture(source)
        self.assertEqual(tuple(result),LANES)
        self.assertTrue(all(v["status"]=="BLOCKED_WITH_PROGRESS" for v in result.values()))


if __name__=="__main__":
    unittest.main()
