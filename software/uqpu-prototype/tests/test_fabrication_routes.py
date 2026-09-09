import unittest

from uqpu.fabrication_routes import (
    DeviceProcessRequirement,
    LithographyKind,
    assess_route,
    choose_route,
    reference_routes,
)


class FabricationRouteTests(unittest.TestCase):
    def test_mature_requirement_prefers_lower_cost_route(self):
        req = DeviceProcessRequirement(
            max_feature_nm=90,
            max_overlay_nm=10,
            min_yield=0.90,
            min_wafers_per_hour=100,
        )
        selected = choose_route(reference_routes(), req)
        self.assertEqual(selected.route.kind, LithographyKind.DUV_DRY)

    def test_advanced_requirement_rejects_dry_duv(self):
        dry = reference_routes()[0]
        req = DeviceProcessRequirement(
            max_feature_nm=15,
            max_overlay_nm=2,
            min_yield=0.85,
        )
        result = assess_route(dry, req)
        self.assertFalse(result.feasible)
        self.assertIn("feature_size", result.blockers)

    def test_high_na_only_when_requirement_demands_it(self):
        req = DeviceProcessRequirement(
            max_feature_nm=8,
            max_overlay_nm=1,
            min_yield=0.89,
        )
        selected = choose_route(reference_routes(), req)
        self.assertEqual(selected.route.kind, LithographyKind.EUV_HIGH_NA)

    def test_maskless_requirement_selects_direct_write(self):
        req = DeviceProcessRequirement(
            max_feature_nm=20,
            max_overlay_nm=6,
            min_yield=0.70,
            require_maskless=True,
        )
        selected = choose_route(reference_routes(), req)
        self.assertEqual(selected.route.kind, LithographyKind.DIRECT_WRITE)

    def test_no_route_is_explicit_failure(self):
        req = DeviceProcessRequirement(
            max_feature_nm=2,
            max_overlay_nm=0.2,
            min_yield=0.99,
            min_wafers_per_hour=500,
        )
        with self.assertRaises(RuntimeError):
            choose_route(reference_routes(), req)


if __name__ == "__main__":
    unittest.main()
