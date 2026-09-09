import unittest
from uqpu.benchmark_tiers import representative_tiers
from uqpu.tier_runner import run_greedy_tier


class Batch008TierRunnerTests(unittest.TestCase):
    def test_small_tier_is_reproducible_contract(self):
        tier=representative_tiers()[0]
        a=run_greedy_tier(tier,restarts=2,seed=77)
        b=run_greedy_tier(tier,restarts=2,seed=77)
        self.assertEqual(a.contract_id,b.contract_id)
        self.assertEqual(a.artifact.objective,b.artifact.objective)
        self.assertEqual(a.artifact.solver_class,"heuristic-classical-cpu")

    def test_all_tiers_have_unique_contracts(self):
        tiers=representative_tiers()
        ids={t.contract().contract_id for t in tiers}
        self.assertEqual(len(ids),len(tiers))


if __name__=="__main__":
    unittest.main()
