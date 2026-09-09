import unittest
from uqpu.sensitivity import sweep


class SensitivityTests(unittest.TestCase):
    def test_sweep(self):
        pts = sweep("x", [1, 2, 4], lambda x: (1 / x, 1.0))
        self.assertEqual(len(pts), 3)
        self.assertLess(pts[0].cost_advantage, pts[-1].cost_advantage)
