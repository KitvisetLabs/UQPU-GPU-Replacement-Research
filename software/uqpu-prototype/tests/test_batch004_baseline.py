import unittest
from uqpu.optimization_baseline import QuboInstance, demo_maxcut_triangle, exact_qubo_baseline
from uqpu.baseline_provenance import capture_baseline


class Batch004BaselineTests(unittest.TestCase):
    def test_triangle_optimum(self):
        r=exact_qubo_baseline(demo_maxcut_triangle())
        self.assertEqual(r.states_evaluated,8)
        self.assertEqual(r.objective,-2.0)

    def test_cap_prevents_accidental_exponential_run(self):
        q=QuboInstance({i:1.0 for i in range(25)}, {})
        with self.assertRaises(ValueError):
            exact_qubo_baseline(q)

    def test_provenance_is_explicitly_unpriced(self):
        r=exact_qubo_baseline(demo_maxcut_triangle())
        p=capture_baseline("combinatorial_optimization",r)
        self.assertIsNone(p.cost_per_task_usd)
        self.assertEqual(p.cost_method,"UNPRICED_LOCAL_RUNTIME")


if __name__=="__main__":
    unittest.main()
