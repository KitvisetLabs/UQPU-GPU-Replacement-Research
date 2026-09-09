import unittest
from unittest.mock import patch

from uqpu.benchmark_tiers import representative_tiers
from uqpu.optimized_solver import OptimizedSolverResult
from uqpu.reference_certificate import ReferenceKind
from uqpu.reference_generation import generate_ortools_reference
from uqpu.reference_manifest import reference_record


class Batch010Tests(unittest.TestCase):
    def test_optimal_solver_status_generates_exact_certificate(self):
        tier=representative_tiers()[0]
        fake=OptimizedSolverResult({},-10.0,0.25,"ortools-cp-sat","OPTIMAL",True)
        with patch("uqpu.reference_generation.ortools_available",return_value=True), patch(
            "uqpu.reference_generation.solve_qubo_ortools",return_value=fake
        ):
            result=generate_ortools_reference(tier)
        self.assertEqual(result.reference.kind,ReferenceKind.EXACT_OPTIMUM)
        self.assertEqual(result.reference.contract_id,tier.contract().contract_id)

    def test_feasible_only_generates_best_known_not_proof(self):
        tier=representative_tiers()[1]
        fake=OptimizedSolverResult({},-9.0,1.0,"ortools-cp-sat","FEASIBLE",False)
        with patch("uqpu.reference_generation.ortools_available",return_value=True), patch(
            "uqpu.reference_generation.solve_qubo_ortools",return_value=fake
        ):
            result=generate_ortools_reference(tier)
        self.assertEqual(result.reference.kind,ReferenceKind.BEST_KNOWN_FEASIBLE)
        self.assertFalse(result.proven_optimal)
        self.assertEqual(reference_record(result)["proven_optimal"],False)


if __name__=="__main__":
    unittest.main()
