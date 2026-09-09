import unittest

from uqpu.fab_flow import DieGeometry, estimate_fab_flow, reference_generic_flow
from uqpu.fabrication_budget import (
    ManufacturingDeployment,
    assess_fabrication_against_inverse_budget,
)
from uqpu.inverse_system import allocate_inverse_budget


class FabricationBudgetTests(unittest.TestCase):
    def setUp(self):
        self.fab = estimate_fab_flow(
            reference_generic_flow(),
            DieGeometry(300, 100),
            defect_density_per_cm2=0.05,
        )
        self.budgets = allocate_inverse_budget(1.0)

    def test_more_lifetime_tasks_relaxes_die_cost_limit(self):
        budget = self.budgets[0]
        a = assess_fabrication_against_inverse_budget(
            budget,
            self.fab,
            ManufacturingDeployment(1, 1_000_000, 5),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        b = assess_fabrication_against_inverse_budget(
            budget,
            self.fab,
            ManufacturingDeployment(1, 10_000_000, 5),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        self.assertGreater(
            b.max_fab_cost_per_good_die_usd,
            a.max_fab_cost_per_good_die_usd,
        )

    def test_more_devices_tightens_per_device_budget(self):
        budget = self.budgets[0]
        one = assess_fabrication_against_inverse_budget(
            budget,
            self.fab,
            ManufacturingDeployment(1, 1_000_000, 0),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        four = assess_fabrication_against_inverse_budget(
            budget,
            self.fab,
            ManufacturingDeployment(4, 1_000_000, 0),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        self.assertLess(
            four.max_manufacturing_cost_per_device_usd,
            one.max_manufacturing_cost_per_device_usd,
        )

    def test_harder_advantage_target_tightens_fab_budget(self):
        easy = assess_fabrication_against_inverse_budget(
            self.budgets[0],
            self.fab,
            ManufacturingDeployment(1, 1_000_000_000, 0),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        hard = assess_fabrication_against_inverse_budget(
            self.budgets[-1],
            self.fab,
            ManufacturingDeployment(1, 1_000_000_000, 0),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        self.assertLess(
            hard.max_fab_cost_per_good_die_usd,
            easy.max_fab_cost_per_good_die_usd,
        )

    def test_package_cost_can_consume_entire_device_budget(self):
        result = assess_fabrication_against_inverse_budget(
            self.budgets[-1],
            self.fab,
            ManufacturingDeployment(1, 1, 1),
            manufacturing_fraction_of_compute_budget=0.25,
        )
        self.assertEqual(result.max_fab_cost_per_good_die_usd, 0)
        self.assertFalse(result.passes_budget)

    def test_invalid_fraction_rejected(self):
        with self.assertRaises(ValueError):
            assess_fabrication_against_inverse_budget(
                self.budgets[0],
                self.fab,
                ManufacturingDeployment(1, 1000),
                manufacturing_fraction_of_compute_budget=0,
            )


if __name__ == "__main__":
    unittest.main()
