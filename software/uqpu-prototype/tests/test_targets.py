import unittest
from uqpu.targets import solve_cost_target, target_ladder


class TargetTests(unittest.TestCase):
    def test_100x(self):
        t = solve_cost_target(1.0, 100)
        self.assertAlmostEqual(t.maximum_uqpu_cost_per_task, 0.01)

    def test_moonshot(self):
        t = solve_cost_target(10.0, 100_000_000)
        self.assertAlmostEqual(t.maximum_uqpu_cost_per_task, 1e-7)

    def test_ladder(self):
        ladder = target_ladder(1.0)
        self.assertEqual(len(ladder), 7)
        self.assertGreater(
            ladder[0].maximum_uqpu_cost_per_task,
            ladder[-1].maximum_uqpu_cost_per_task,
        )
