import unittest

from uqpu.benchmark_artifact import BenchmarkArtifact
from uqpu.optimization_baseline import demo_maxcut_triangle
from uqpu.optimized_solver import ortools_available, solve_qubo_ortools


class Batch007Tests(unittest.TestCase):
    def test_artifact_id_is_stable(self):
        a=BenchmarkArtifact("c","impl","solver",-2.0,True,0.1,"MEASURED_LOCAL")
        self.assertEqual(a.artifact_id,a.artifact_id)

    def test_negative_runtime_rejected(self):
        a=BenchmarkArtifact("c","impl","solver",-2.0,True,-1.0,"MEASURED_LOCAL")
        with self.assertRaises(ValueError):
            a.validate()

    def test_ortools_adapter_absence_is_explicit(self):
        if not ortools_available():
            with self.assertRaises(RuntimeError):
                solve_qubo_ortools(demo_maxcut_triangle())

    @unittest.skipUnless(ortools_available(),"OR-Tools optional dependency not installed")
    def test_ortools_triangle_optimum(self):
        r=solve_qubo_ortools(demo_maxcut_triangle(),time_limit_seconds=5)
        self.assertEqual(r.objective,-2.0)
        self.assertTrue(r.proven_optimal)


if __name__=="__main__":
    unittest.main()
