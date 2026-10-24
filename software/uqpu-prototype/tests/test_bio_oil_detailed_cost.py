import unittest
from uqpu.energy_finance import (
    BioOilDetailedCostInputs,
    bio_oil_detailed_cost_breakdown,
)


def sample_inputs(**overrides):
    values = {
        "dry_feedstock_t_per_year": 1000.0,
        "saleable_liters_per_dry_t": 200.0,
        "lower_heating_value_mj_per_liter": 20.0,
        "feedstock_cost_per_dry_t": 50.0,
        "collection_transport_cost_per_dry_t": 5.0,
        "preprocessing_cost_per_dry_t": 10.0,
        "capex": 1_000_000.0,
        "fixed_om_per_year": 20_000.0,
        "conversion_cost_per_saleable_liter": 0.05,
        "upgrading_cost_per_saleable_liter": 0.10,
        "hydrogen_cost_per_saleable_liter": 0.08,
        "catalyst_cost_per_saleable_liter": 0.02,
        "utilities_cost_per_saleable_liter": 0.03,
        "logistics_cost_per_saleable_liter": 0.04,
        "compliance_storage_cost_per_saleable_liter": 0.01,
        "working_capital_carry_cost_per_saleable_liter": 0.02,
        "coproduct_credit_per_dry_t": 3.0,
        "annual_discount_rate": 0.08,
        "plant_life_years": 20.0,
    }
    values.update(overrides)
    return BioOilDetailedCostInputs(**values)


class BioOilDetailedCostTests(unittest.TestCase):
    def test_component_ledger_reconciles_gross_net_and_energy_units(self):
        result = bio_oil_detailed_cost_breakdown(sample_inputs())
        self.assertAlmostEqual(result.annual_saleable_liters, 200_000.0)
        self.assertAlmostEqual(result.feedstock_per_liter, 50.0 / 200.0)
        self.assertAlmostEqual(result.collection_transport_per_liter, 5.0 / 200.0)
        self.assertAlmostEqual(result.preprocessing_per_liter, 10.0 / 200.0)
        self.assertAlmostEqual(result.fixed_om_per_liter, 20_000.0 / 200_000.0)

        components = (
            result.annualized_capex_per_liter,
            result.feedstock_per_liter,
            result.collection_transport_per_liter,
            result.preprocessing_per_liter,
            result.fixed_om_per_liter,
            result.conversion_per_liter,
            result.upgrading_per_liter,
            result.hydrogen_per_liter,
            result.catalyst_per_liter,
            result.utilities_per_liter,
            result.logistics_per_liter,
            result.compliance_storage_per_liter,
            result.working_capital_carry_per_liter,
        )
        self.assertAlmostEqual(result.gross_cost_per_liter, sum(components))
        self.assertAlmostEqual(
            result.coproduct_credit_per_liter, 3.0 / 200.0
        )
        self.assertAlmostEqual(
            result.net_cost_per_liter,
            result.gross_cost_per_liter - result.coproduct_credit_per_liter,
        )
        self.assertAlmostEqual(result.gross_cost_per_gj, result.gross_cost_per_liter * 50.0)
        self.assertAlmostEqual(result.net_cost_per_gj, result.net_cost_per_liter * 50.0)

    def test_higher_accepted_yield_dilutes_per_tonne_and_fixed_costs(self):
        baseline = bio_oil_detailed_cost_breakdown(sample_inputs())
        improved = bio_oil_detailed_cost_breakdown(
            sample_inputs(saleable_liters_per_dry_t=400.0)
        )
        self.assertLess(improved.feedstock_per_liter, baseline.feedstock_per_liter)
        self.assertLess(
            improved.annualized_capex_per_liter,
            baseline.annualized_capex_per_liter,
        )
        self.assertLess(improved.gross_cost_per_liter, baseline.gross_cost_per_liter)

    def test_qualified_coproduct_credit_is_subtracted_once(self):
        no_credit = bio_oil_detailed_cost_breakdown(
            sample_inputs(coproduct_credit_per_dry_t=0.0)
        )
        with_credit = bio_oil_detailed_cost_breakdown(sample_inputs())
        self.assertAlmostEqual(
            no_credit.gross_cost_per_liter, with_credit.gross_cost_per_liter
        )
        self.assertAlmostEqual(
            no_credit.net_cost_per_liter - with_credit.net_cost_per_liter,
            with_credit.coproduct_credit_per_liter,
        )

    def test_large_credit_remains_visible_instead_of_clamping_net_cost(self):
        result = bio_oil_detailed_cost_breakdown(
            sample_inputs(coproduct_credit_per_dry_t=1000.0)
        )
        self.assertGreater(result.gross_cost_per_liter, 0.0)
        self.assertLess(result.net_cost_per_liter, 0.0)
        self.assertGreater(result.gross_cost_per_gj, 0.0)
        self.assertLess(result.net_cost_per_gj, 0.0)

    def test_invalid_yield_costs_and_nonfinite_values_fail_closed(self):
        with self.assertRaises(ValueError):
            bio_oil_detailed_cost_breakdown(
                sample_inputs(saleable_liters_per_dry_t=0.0)
            )
        with self.assertRaises(ValueError):
            bio_oil_detailed_cost_breakdown(
                sample_inputs(hydrogen_cost_per_saleable_liter=float("nan"))
            )
        with self.assertRaises(ValueError):
            bio_oil_detailed_cost_breakdown(
                sample_inputs(coproduct_credit_per_dry_t=-1.0)
            )
        with self.assertRaises(ValueError):
            bio_oil_detailed_cost_breakdown(
                sample_inputs(annual_discount_rate=float("nan"))
            )
        with self.assertRaises(ValueError):
            bio_oil_detailed_cost_breakdown(
                sample_inputs(capex=-1.0)
            )


if __name__ == "__main__":
    unittest.main()
