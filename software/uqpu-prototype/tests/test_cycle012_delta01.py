import hashlib
import unittest

from uqpu.cycle012_delta01 import (
    atomic_publish_model, canonical_hash, consent_transition, cost_per_output,
    covariance_block, custody_chain, exact_keys, lineage_manifest,
    migrate_er6, migrate_v3_to_v4, priority_sensitivity, run_cycle012_fixture,
    typed_interval, weighted_maxcut, zip64_directory_gate,
)


class Cycle012Tests(unittest.TestCase):
    def test_a_weighted_exact_case_is_complete_and_seed_independent(self):
        x=weighted_maxcut(4,[(0,1,2),(1,2,3),(2,3,1),(0,3,4)])
        self.assertEqual(x["states"],16); self.assertEqual(x["best"],10)
        with self.assertRaises(ValueError): weighted_maxcut(10,[(0,1,1)],cap=512)

    def test_b_v3_optional_migration_is_bound_and_unknown_fields_reject(self):
        x=migrate_v3_to_v4({"schema":"v3","payload":{"x":1},"token":"n"},"commit")
        self.assertEqual(len(x["binding"]),64)
        with self.assertRaises(ValueError): migrate_v3_to_v4({"schema":"v3","payload":{},"token":"n","surprise":1},"commit")

    def test_c_atomic_publish_failure_preserves_old_and_cleans_temp(self):
        x=atomic_publish_model(b"old",b"new","before_replace")
        self.assertEqual(x["visible_sha256"],hashlib.sha256(b"old").hexdigest())
        self.assertTrue(x["temp_removed"])

    def test_d_zip_entry_count_and_end_boundaries(self):
        self.assertEqual(zip64_directory_gate([(10,20),(20,30)],2,10,30,32,40)["entries"],2)
        with self.assertRaises(ValueError): zip64_directory_gate([(10,20)],2,10,20,22,30)

    def test_e_custody_chain_detects_change(self):
        ev={"sample":"s","from":"a","to":"b","method":"m","unit":"u","expiry":"2030","previous":"0"*64}
        self.assertEqual(len(custody_chain([ev])),1)
        ev["previous"]="1"*64
        with self.assertRaises(ValueError): custody_chain([ev])

    def test_f_cost_interval_keeps_zero_output_null_and_checks_covariance(self):
        cs=[{"low":1,"high":2,"unit":"USD"} for _ in range(4)]
        self.assertIsNone(cost_per_output(cs,0))
        self.assertEqual(cost_per_output(cs,2)["per_output_usd"],[2,4])
        self.assertIsNone(cost_per_output(cs,2,[[1,2,0,0],[2,1,0,0],[0,0,1,0],[0,0,0,1]]))

    def test_g_three_measurand_covariance_requires_psd_and_scope(self):
        self.assertEqual(covariance_block(["x","y","z"],["u"]*3,[[1,0,0],[0,1,0],[0,0,1]],"scope","m","2030")["measurands"],3)
        with self.assertRaises(ValueError): covariance_block(["x","y","z"],["u"]*3,[[1,2,0],[2,1,0],[0,0,1]],"scope","m","2030")

    def test_h_held_out_priority_scenarios_report_capital_null(self):
        x=priority_sensitivity(["a","b"],[{"a":2,"b":1},{"a":1,"b":2}],[{"a":1,"b":2}])
        self.assertEqual(x["orderings"],2); self.assertIsNone(x["capital"])

    def test_fnd_eqn_requires_registered_dimension_and_source(self):
        self.assertEqual(typed_interval([1,2],[0]*10,"a"*64)["evidence"],"DECLARATION_ONLY")
        with self.assertRaises(ValueError): typed_interval([1,2],[0]*9,"a"*64)

    def test_scm_revocation_blocks_replay_and_later_transition(self):
        s={"active":set(),"seen":set()}; s=consent_transition(s,{"action":"grant","nonce":"e1","consent_id":"c1"})
        s=consent_transition(s,{"action":"revoke","nonce":"e2","consent_id":"c1"})
        with self.assertRaises(ValueError): consent_transition(s,{"action":"transition","nonce":"e3","consent_id":"c1"})
        with self.assertRaises(ValueError): consent_transition(s,{"action":"revoke","nonce":"e4","consent_id":"c1"})
        with self.assertRaises(ValueError): consent_transition(s,{"action":"grant","nonce":"e1","consent_id":"c2"})

    def test_ai_cost_split_order_stable_and_disjoint(self):
        a=lineage_manifest(b"v2",{"train":["a"],"validation":["b"],"test":["c"]},{k:{"loss":1} for k in ("train","validation","test")})
        b=lineage_manifest(b"v2",{"test":["c"],"train":["a"],"validation":["b"]},{k:{"loss":1} for k in ("train","validation","test")})
        self.assertEqual(a,b)
        with self.assertRaises(ValueError): lineage_manifest(b"v2",{"train":["a"],"validation":["a"],"test":["c"]},{k:{"loss":1} for k in ("train","validation","test")})

    def test_qos_certificate_resource_decrease_is_versioned(self):
        old={"version":1,"qubits":6,"bits":6,"depth":20,"gates":40,"source_sha256":"a"*64}
        new={"version":2,"qubits":6,"bits":6,"depth":18,"gates":38,"source_sha256":"b"*64}
        self.assertEqual(migrate_er6(old,new)["resource_delta"],{"depth":-2,"gates":-2})
        new["gates"]=41
        with self.assertRaises(ValueError): migrate_er6(old,new)

    def test_fixture_has_all_twelve_lanes(self):
        self.assertEqual(set(run_cycle012_fixture()),{"A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT"})


if __name__ == "__main__":
    unittest.main()
