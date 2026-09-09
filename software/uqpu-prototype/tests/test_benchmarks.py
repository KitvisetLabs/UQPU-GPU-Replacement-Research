import unittest
from uqpu.benchmarks import cost_tier, run_benchmarks
from uqpu.ir import Operation, OperationKind, ResultContract, Workload, WorkloadDomain


class BenchmarkTests(unittest.TestCase):
    def test_cost_tiers(self):
        self.assertEqual(cost_tier(100), "C1_100X_MINIMUM")
        self.assertEqual(cost_tier(100_000_000), "C7_100M_MOONSHOT")
        self.assertEqual(cost_tier(1), "BELOW_TARGET")

    def test_evidence_is_model_only(self):
        w = Workload("s", WorkloadDomain.DATA, [Operation(OperationKind.SEARCH)], ResultContract.PROBABILISTIC, 1024, 8)
        result = run_benchmarks([w], {"s": 1.0})[0]
        self.assertEqual(result.evidence_level, "MODEL_ONLY")
