import unittest

from uqpu.cloud_economics import CloudPricingKind, CloudPricingProfile, CloudWorkloadUsage
from uqpu.cloud_vs_owned import OwnedHardwareEconomics, OwnedWorkloadUsage
from uqpu.economic_sensitivity import (
    CostEnvelope,
    FxConversion,
    convert_cloud_profile,
    find_route_transition,
    robust_route_assessment,
    sweep_owned_capex,
    sweep_owned_utilization,
)


class EconomicSensitivityTests(unittest.TestCase):
    def setUp(self):
        self.cloud = CloudPricingProfile(
            "test", "test", CloudPricingKind.PER_SECOND, per_second=1.0
        )
        self.cloud_usage = CloudWorkloadUsage(runtime_seconds=100, useful_tasks=100)
        self.owned = OwnedHardwareEconomics(
            capex_usd=100_000,
            lifetime_seconds=10_000_000,
            utilization=0.5,
            operating_power_watts=1000,
        )
        self.owned_usage = OwnedWorkloadUsage(100, 100)

    def test_higher_utilization_reduces_owned_cost(self):
        points = sweep_owned_utilization(
            self.cloud, self.cloud_usage, self.owned, self.owned_usage,
            [0.1, 0.5, 0.9],
        )
        self.assertGreater(points[0].owned_cost_per_task, points[-1].owned_cost_per_task)

    def test_capex_sweep_can_change_route(self):
        points = sweep_owned_capex(
            self.cloud, self.cloud_usage, self.owned, self.owned_usage,
            [1_000, 1_000_000, 100_000_000],
        )
        self.assertIsNotNone(find_route_transition(points))

    def test_fx_conversion_has_provenance(self):
        eur = CloudPricingProfile(
            "p", "p", CloudPricingKind.PER_QPU_HOUR,
            currency="EUR", per_qpu_hour=3000,
        )
        usd = convert_cloud_profile(
            eur, FxConversion("EUR", "USD", 1.10, "2026-09-09", "test-source")
        )
        self.assertEqual(usd.currency, "USD")
        self.assertAlmostEqual(usd.per_qpu_hour, 3300)

    def test_fx_mismatch_rejected(self):
        eur = CloudPricingProfile(
            "p", "p", CloudPricingKind.PER_QPU_HOUR,
            currency="EUR", per_qpu_hour=3000,
        )
        with self.assertRaises(ValueError):
            convert_cloud_profile(
                eur, FxConversion("GBP", "USD", 1.3, "2026-09-09", "test-source")
            )

    def test_robust_cloud(self):
        r = robust_route_assessment(
            CostEnvelope(1, 1.5, 2),
            CostEnvelope(3, 4, 5),
        )
        self.assertEqual(r.classification, "ROBUST_CLOUD")

    def test_overlap_is_uncertain(self):
        r = robust_route_assessment(
            CostEnvelope(1, 3, 5),
            CostEnvelope(4, 6, 8),
        )
        self.assertEqual(r.classification, "UNCERTAIN_OVERLAP")


if __name__ == "__main__":
    unittest.main()
