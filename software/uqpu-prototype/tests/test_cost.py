import unittest
from uqpu.cost import CostModel
from uqpu.resources import ResourceEstimate


class CostTests(unittest.TestCase):
    def test_cost_positive(self):
        r = ResourceEstimate(execution_seconds=1.0, energy_joules=3600)
        c = CostModel().estimate(r, io_bytes=1024)
        self.assertGreater(c.total, 0)

    def test_advantage(self):
        self.assertEqual(CostModel.advantage(100.0, 1.0), 100.0)
