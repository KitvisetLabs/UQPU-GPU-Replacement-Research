import unittest
from hardware_cost import HardwareLayerCost, SystemEconomics


class HardwareCostTests(unittest.TestCase):
    def test_total_capex(self):
        c = HardwareLayerCost(fabrication_usd=10, photonics_usd=20, memory_usd=30)
        self.assertEqual(c.total_capex, 60)

    def test_cost_increases_with_runtime(self):
        e = SystemEconomics(
            HardwareLayerCost(fabrication_usd=1_000_000),
            lifetime_seconds=10_000_000,
            utilization=0.5,
            operating_power_watts=1000,
        )
        self.assertGreater(e.cost_per_task(10), e.cost_per_task(1))


if __name__ == "__main__":
    unittest.main()
