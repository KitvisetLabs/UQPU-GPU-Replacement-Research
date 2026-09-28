import hashlib
import tempfile
import unittest

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle017_delta01 import (
    LANES, adverse_ranking_grid, ai_lineage_v7, custody_truncation_duplicate_suite,
    maxcut_weight_perturbation_family, receipt_v4_fixture, run_cycle017_fixture,
    safe_same_device_replace, second_qos_operator, shared_covariance_grid,
    three_measurand_covariance, verify_receipt_v4_fixture,
)


class Cycle017Tests(unittest.TestCase):
    def _graphs(self):
        base=[[0,1,4],[0,3,7],[0,6,2],[1,2,5],[1,5,3],[2,3,6],[2,7,4],[3,4,8],[4,5,2],[4,8,5],[5,6,7],[6,7,3],[7,8,6],[8,9,4],[2,9,1]]
        changed=[row[:] for row in base];changed[0][2]+=1;changed[4][2]+=2
        return base,changed

    def test_a_weight_perturbations_keep_exact_1024_state_contract(self):
        base,changed=self._graphs();out=maxcut_weight_perturbation_family([base,changed])
        self.assertEqual([x["state_count"] for x in out["rows"]],[1024,1024])
        self.assertNotEqual(out["rows"][0]["task_sha256"],out["rows"][1]["task_sha256"])
        self.assertIsNone(out["scaling_claim"])

    def test_b_receipt_v4_rotation_and_revocation_are_fixture_only(self):
        request=canonical_hash({"r":17});key=b"test-key"
        receipt=receipt_v4_fixture(request,"key-a",key)
        self.assertTrue(verify_receipt_v4_fixture(receipt,request,"key-a",key))
        self.assertFalse(verify_receipt_v4_fixture(receipt,request,"key-a",key,["key-a"]))
        self.assertFalse(verify_receipt_v4_fixture(receipt,request,"key-b",key))
        self.assertIsNone(receipt["provider_claim"])
        self.assertIsNone(receipt_v4_fixture(request,None,None)["receipt"])

    def test_c_target_collision_rejects_and_safe_name_passes(self):
        with tempfile.TemporaryDirectory() as d:
            for unsafe in ("../state.bin",".",".."):
                with self.assertRaises(ValueError): safe_same_device_replace(d,unsafe,[b"a",b"b",b"c"])
            self.assertTrue(safe_same_device_replace(d,"state.bin",[b"a",b"b",b"c"])["device_id_match"])

    def test_d_evidence_fixture_crossbinds_local_central_descriptor(self):
        result=run_cycle017_fixture(b"source") ["D"]
        self.assertTrue(result["local_central_match"])
        self.assertTrue(result["data_descriptor_flag"])
        self.assertFalse(result["payload_read"])

    def test_e_custody_truncation_and_duplicate_sequence_reject(self):
        out=custody_truncation_duplicate_suite("2026-09-28")
        self.assertEqual(out["valid_events"],3)
        self.assertTrue(out["truncated_chain_rejected"])
        self.assertTrue(out["duplicate_sequence_rejected"])
        self.assertIsNone(out["physical_sample_claim"])

    def test_f_shared_covariance_changes_model_interval_and_keeps_nulls(self):
        out=shared_covariance_grid()["scenarios"]
        self.assertNotEqual(out["shared"]["total_usd"],out["independent"]["total_usd"])
        self.assertIsNone(out["invalid"]["total_usd"])
        self.assertIsNone(out["shared"]["outputs"][3]["per_output_usd"])

    def test_g_three_unit_products_preserve_order_symmetry_and_dimensions(self):
        out=three_measurand_covariance()
        self.assertEqual(out["measurand_order"],["length","duration","mass"])
        self.assertTrue(out["positive_semidefinite"])
        self.assertIsNone(out["calibration"])

    def test_h_adverse_rank_grid_has_explicit_range_and_null_capital(self):
        out=adverse_ranking_grid()
        self.assertEqual(out["observed_stability_range"],[0.0,1/3])
        self.assertIsNone(out["capital"])

    def test_fnd_division_then_multiplication_is_exact_and_source_typed(self):
        import hashlib
        source=b"source-bound cycle017 fixture";out=run_cycle017_fixture(source)["FND/EQN"]
        length=out["composed_length"]
        self.assertEqual(length["unit"],"m")
        self.assertEqual(length["lower"],[1,1])
        self.assertEqual(length["upper"],[6,1])
        self.assertEqual(length["source_sha256"],hashlib.sha256(source).hexdigest())

    def test_scm_replay_expiry_and_scope_cases_stay_fiction_only(self):
        out=run_cycle017_fixture(b"src")["SCM"]
        self.assertEqual(out["cases"]["valid_fiction"],"ACCEPTED_FICTION_ONLY")
        self.assertTrue(all(v=="REJECTED" for k,v in out["cases"].items() if k!="valid_fiction"))
        self.assertIsNone(out["empirical_coupling"])

    def test_ai_v7_parent_chain_and_candidate_null(self):
        out=ai_lineage_v7(b"umrl")
        self.assertEqual(out["manifest"]["version"],7)
        self.assertEqual(len(out["manifest"]["parent_manifest_sha256"]),64)
        self.assertIsNone(out["candidate_result"])
        self.assertIsNone(out["equivalence"])

    def test_qos_second_operator_has_exact_residual_and_null_hardware(self):
        out=second_qos_operator()
        self.assertEqual(out["basis_states_checked"],64)
        self.assertEqual(out["maximum_integer_residual"],0)
        self.assertIsNone(out["hardware"])

    def test_integrated_fixture_advances_all_twelve_lanes(self):
        from pathlib import Path
        source=(Path(__file__).resolve().parents[3]/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md").read_bytes()
        out=run_cycle017_fixture(source)
        self.assertEqual(set(out),set(LANES))
        self.assertEqual(out["A"]["rows"][0]["state_count"],1024)


if __name__=="__main__":
    unittest.main()
