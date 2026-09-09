import unittest

from uqpu.fab_bottleneck import rank_step_impacts
from uqpu.fab_flow import (
    DieGeometry,
    ProcessKind,
    ProcessStep,
    estimate_fab_flow,
    reference_generic_flow,
)


class FabFlowTests(unittest.TestCase):
    def test_cost_per_good_die_is_positive(self):
        r = estimate_fab_flow(
            reference_generic_flow(),
            DieGeometry(300, 100),
            defect_density_per_cm2=0.1,
        )
        self.assertGreater(r.cost_per_good_die_usd, 0)
        self.assertGreater(r.expected_good_dies_per_wafer, 0)

    def test_lower_step_yield_increases_cost_per_good_die(self):
        base = list(reference_generic_flow())
        worse = list(base)
        s = worse[1]
        worse[1] = ProcessStep(
            s.name, s.kind, s.cost_per_wafer_usd, 0.95,
            s.cycle_time_seconds, s.energy_kwh_per_wafer,
        )
        a = estimate_fab_flow(base, DieGeometry(300, 100))
        b = estimate_fab_flow(worse, DieGeometry(300, 100))
        self.assertGreater(b.cost_per_good_die_usd, a.cost_per_good_die_usd)

    def test_larger_die_reduces_good_dies_per_wafer(self):
        steps = reference_generic_flow()
        small = estimate_fab_flow(steps, DieGeometry(300, 50))
        large = estimate_fab_flow(steps, DieGeometry(300, 200))
        self.assertLess(large.expected_good_dies_per_wafer, small.expected_good_dies_per_wafer)

    def test_bottleneck_ranking_returns_all_steps(self):
        steps = reference_generic_flow()
        impacts = rank_step_impacts(steps)
        self.assertEqual(len(impacts), len(steps))

    def test_invalid_yield_rejected(self):
        with self.assertRaises(ValueError):
            ProcessStep("bad", ProcessKind.ETCH, 1, 0, 1).validate()


if __name__ == "__main__":
    unittest.main()
