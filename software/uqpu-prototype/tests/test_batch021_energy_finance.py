import math
import unittest

from uqpu.energy_finance import (
    BioOilCostInputs,
    FusionElectricityCostInputs,
    amortizing_loan_total_interest,
    bio_oil_levelized_cost_per_liter,
    capital_recovery_factor,
    fusion_lcoe_per_mwh,
    interest_savings_from_lower_principal,
    liquid_cost_per_gj,
)


class Batch021EnergyFinanceTests(unittest.TestCase):
    def test_zero_rate_capital_recovery(self):
        self.assertAlmostEqual(capital_recovery_factor(0.0, 20), 0.05)

    def test_bio_oil_cost_falls_when_saleable_yield_rises(self):
        baseline = BioOilCostInputs(
            dry_feedstock_t_per_year=100_000,
            feedstock_cost_per_dry_t=50,
            saleable_liters_per_dry_t=250,
            capex=100_000_000,
            fixed_om_per_year=5_000_000,
            variable_process_cost_per_liter=0.20,
        )
        improved = BioOilCostInputs(
            **{**baseline.__dict__, "saleable_liters_per_dry_t": 300}
        )
        self.assertLess(
            bio_oil_levelized_cost_per_liter(improved),
            bio_oil_levelized_cost_per_liter(baseline),
        )

    def test_bio_oil_energy_normalization(self):
        self.assertAlmostEqual(liquid_cost_per_gj(0.60, 20.0), 30.0)

    def test_fusion_lcoe_falls_with_lower_capex_at_same_output(self):
        high_capex = FusionElectricityCostInputs(
            net_capacity_mw=1000,
            capacity_factor=0.80,
            capex=10_000_000_000,
            fixed_om_per_year=200_000_000,
            variable_om_per_mwh=5,
            fuel_cycle_per_mwh=2,
            replacement_reserve_per_mwh=5,
            annual_discount_rate=0.08,
            plant_life_years=30,
        )
        low_capex = FusionElectricityCostInputs(
            **{**high_capex.__dict__, "capex": 5_000_000_000}
        )
        self.assertLess(fusion_lcoe_per_mwh(low_capex), fusion_lcoe_per_mwh(high_capex))

    def test_fusion_lcoe_falls_with_lower_financing_rate(self):
        high_rate = FusionElectricityCostInputs(
            net_capacity_mw=1000,
            capacity_factor=0.80,
            capex=8_000_000_000,
            fixed_om_per_year=150_000_000,
            variable_om_per_mwh=4,
            annual_discount_rate=0.10,
            plant_life_years=30,
        )
        low_rate = FusionElectricityCostInputs(
            **{**high_rate.__dict__, "annual_discount_rate": 0.04}
        )
        self.assertLess(fusion_lcoe_per_mwh(low_rate), fusion_lcoe_per_mwh(high_rate))

    def test_lower_principal_directly_lowers_absolute_interest(self):
        before = amortizing_loan_total_interest(100_000_000, 0.08, 10)
        after = amortizing_loan_total_interest(60_000_000, 0.08, 10)
        saving = interest_savings_from_lower_principal(100_000_000, 60_000_000, 0.08, 10)
        self.assertGreater(before, after)
        self.assertAlmostEqual(saving, before - after)
        self.assertAlmostEqual(after / before, 0.60, places=10)

    def test_model_rejects_impossible_capacity_factor(self):
        bad = FusionElectricityCostInputs(
            net_capacity_mw=100,
            capacity_factor=1.01,
            capex=1,
            fixed_om_per_year=0,
            variable_om_per_mwh=0,
        )
        with self.assertRaises(ValueError):
            fusion_lcoe_per_mwh(bad)

    def test_outputs_are_finite_for_valid_inputs(self):
        x = capital_recovery_factor(0.08, 30)
        self.assertTrue(math.isfinite(x))
        self.assertGreater(x, 0)


if __name__ == "__main__":
    unittest.main()
