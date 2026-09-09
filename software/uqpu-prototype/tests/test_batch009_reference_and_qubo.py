import unittest
from uqpu.benchmark_tiers import representative_tiers
from uqpu.qubo_serialization import to_dwave_qubo,to_portable_qubo
from uqpu.reference_certificate import ObjectiveReference,ReferenceKind,assess_minimization_quality
from uqpu.tier_runner import run_greedy_tier

class Batch009Tests(unittest.TestCase):
    def test_no_reference_means_not_accepted(self):
        tier=representative_tiers()[0]
        run=run_greedy_tier(tier,restarts=2,seed=7)
        self.assertFalse(run.artifact.accepted)

    def test_exact_reference_can_verify_quality(self):
        ref=ObjectiveReference("abc",ReferenceKind.EXACT_OPTIMUM,-100.0,"exact","MEASURED","artifact://x")
        q=assess_minimization_quality(-100.0,ref,0.0)
        self.assertTrue(q.accepted); self.assertTrue(q.verified_quality)

    def test_best_known_is_not_verified_quality(self):
        ref=ObjectiveReference("abc",ReferenceKind.BEST_KNOWN_FEASIBLE,-100.0,"solver","MEASURED","artifact://x")
        q=assess_minimization_quality(-100.0,ref,0.0)
        self.assertTrue(q.accepted); self.assertFalse(q.verified_quality)

    def test_dwave_serialization_preserves_term_count(self):
        instance=representative_tiers()[0].instance()
        p=to_dwave_qubo(instance)
        self.assertEqual(len(p.payload["Q"]),len(instance.linear)+len(instance.quadratic))

    def test_portable_qubo_is_json_friendly(self):
        p=to_portable_qubo(representative_tiers()[0].instance())
        self.assertEqual(p.format,"uqpu-qubo-v1")
        self.assertTrue(all(isinstance(k,str) for k in p.payload["linear"]))

if __name__=="__main__":
    unittest.main()
