import unittest
from uqpu.compiler import SemanticCompiler
from uqpu.ir import Operation, OperationKind, ResultContract, Workload, WorkloadDomain


class CompilerTests(unittest.TestCase):
    def test_exact_general_uses_reversible(self):
        w = Workload(
            name="exact",
            domain=WorkloadDomain.GENERAL,
            operations=[Operation(OperationKind.GENERAL_KERNEL)],
            contract=ResultContract.EXACT,
            input_bytes=1024,
            output_bytes=1024,
        )
        plan = SemanticCompiler().compile(w)
        self.assertEqual(plan.selected.assessment.backend, "reversible-fallback")

    def test_probabilistic_search_has_candidate(self):
        w = Workload(
            name="search",
            domain=WorkloadDomain.DATA,
            operations=[Operation(OperationKind.SEARCH)],
            contract=ResultContract.PROBABILISTIC,
            input_bytes=1024*1024,
            output_bytes=8,
        )
        plan = SemanticCompiler().compile(w)
        self.assertGreaterEqual(len(plan.candidates), 1)
