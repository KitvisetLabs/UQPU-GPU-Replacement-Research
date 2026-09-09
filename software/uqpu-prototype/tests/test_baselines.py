import unittest
from uqpu.hardware import GPUHardwareProfile
from uqpu.baselines import GPUBaselineCostModel, GPUBenchmarkMeasurement


class BaselineTests(unittest.TestCase):
    def test_cost_increases_with_time(self):
        p = GPUHardwareProfile("g", 20_000, 20_000_000, 0.5, 600, 200)
        m = GPUBaselineCostModel(p)
        a = m.estimate(GPUBenchmarkMeasurement("x", 0.1))
        b = m.estimate(GPUBenchmarkMeasurement("x", 1.0))
        self.assertGreater(b.total_per_task, a.total_per_task)
