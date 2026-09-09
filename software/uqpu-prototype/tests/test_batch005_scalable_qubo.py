import unittest
from uqpu.scalable_qubo import WeightedEdge,maxcut_qubo,seeded_erdos_renyi_maxcut,greedy_bitflip
from uqpu.optimization_baseline import exact_qubo_baseline
from uqpu.benchmark_contract import OptimizationBenchmarkContract


class Batch005Tests(unittest.TestCase):
    def test_maxcut_triangle_matches_fixture(self):
        q=maxcut_qubo(3,[WeightedEdge(0,1),WeightedEdge(0,2),WeightedEdge(1,2)])
        self.assertEqual(exact_qubo_baseline(q).objective,-2.0)

    def test_seeded_generator_reproducible(self):
        a=seeded_erdos_renyi_maxcut(12,0.3,42)
        b=seeded_erdos_renyi_maxcut(12,0.3,42)
        self.assertEqual(a.linear,b.linear); self.assertEqual(a.quadratic,b.quadratic)

    def test_greedy_never_worse_than_zero_assignment(self):
        q=seeded_erdos_renyi_maxcut(30,0.2,7)
        bits,value=greedy_bitflip(q,restarts=4,seed=9)
        self.assertLessEqual(value,q.energy({i:0 for i in q.variables}))

    def test_contract_id_stable(self):
        c=OptimizationBenchmarkContract("opt-maxcut","erdos-renyi",42,30,required_relative_gap=0.05)
        self.assertEqual(c.contract_id,c.contract_id)
        self.assertTrue(c.accepts(-95,-100))


if __name__=="__main__":
    unittest.main()
