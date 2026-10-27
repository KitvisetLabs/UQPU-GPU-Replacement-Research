import dataclasses
import math
import unittest

from uqpu.energy_finance import (
    BioOilBatchCostInputs,
    bio_oil_batch_cost,
    simple_interest_for_capital_lockup,
)


def sample_inputs(**overrides):
    values = dict(
        batch_id="BIO001-BATCH-TEST-01",
        provenance_ids=("source:published-study",),
        source_evidence_class="MODEL_ONLY",
        wet_feedstock_kg=1000.0,
        moisture_fraction=0.20,
        feedstock_cost_usd_per_wet_tonne=100.0,
        preprocessing_cost_usd_per_wet_tonne=50.0,
        logistics_cost_usd=25.0,
        raw_bio_oil_kg=300.0,
        accepted_liquid_kg=180.0,
        accepted_liquid_lhv_mj_per_kg=35.0,
        acceptance_passed=True,
        acceptance_spec_sha256="a" * 64,
        hydrogen_kg=20.0,
        hydrogen_cost_usd_per_kg=5.0,
        catalyst_cost_usd=40.0,
        utility_cost_usd=30.0,
        other_opex_usd=20.0,
        plant_capex_usd=1_000_000.0,
        annual_nameplate_feedstock_kg=1_000_000.0,
        capacity_factor=0.80,
        plant_life_years=20.0,
        annual_capital_charge_rate=0.08,
        product_density_kg_per_litre=0.75,
        feedstock_lhv_mj_per_dry_kg=18.0,
        utility_electricity_kwh=12.0,
        utility_process_heat_mj=10.0,
    )
    values.update(overrides)
    return BioOilBatchCostInputs(**values)


class BioOilBatchCostContractTests(unittest.TestCase):
    def test_cost_is_normalized_to_accepted_final_liquid_not_raw_oil(self):
        result = bio_oil_batch_cost(sample_inputs())
        self.assertAlmostEqual(result.dry_feedstock_kg, 800.0)
        self.assertAlmostEqual(result.raw_liquid_mass_yield_kg_per_dry_kg, 300 / 800)
        self.assertAlmostEqual(result.accepted_liquid_mass_yield_kg_per_dry_kg, 180 / 800)
        self.assertAlmostEqual(result.feedstock_cost_usd, 100.0)
        self.assertAlmostEqual(result.preprocessing_cost_usd, 50.0)
        self.assertAlmostEqual(result.hydrogen_cost_usd, 100.0)
        self.assertAlmostEqual(result.accepted_fuel_energy_mj, 6300.0)
        self.assertAlmostEqual(
            result.cost_usd_per_accepted_mj,
            result.net_batch_cost_usd / result.accepted_fuel_energy_mj,
        )
        self.assertEqual(result.result_evidence_class, "MODEL_ONLY")

    def test_litre_and_energy_outputs_use_final_accepted_product(self):
        result = bio_oil_batch_cost(sample_inputs())
        self.assertAlmostEqual(result.accepted_liters, 240.0)
        self.assertAlmostEqual(
            result.cost_usd_per_accepted_liter,
            result.net_batch_cost_usd / 240.0,
        )
        self.assertAlmostEqual(result.feedstock_energy_mj, 14_400.0)
        self.assertAlmostEqual(result.utility_energy_mj, 53.2)

    def test_no_accepted_output_has_no_cost_per_accepted_function(self):
        result = bio_oil_batch_cost(
            sample_inputs(acceptance_passed=False, accepted_liquid_kg=0.0)
        )
        self.assertEqual(result.accepted_fuel_energy_mj, 0.0)
        self.assertIsNone(result.accepted_liquid_mass_yield_kg_per_dry_kg)
        self.assertIsNone(result.cost_usd_per_accepted_mj)
        self.assertIsNone(result.cost_usd_per_accepted_liter)

    def test_rejected_batch_cannot_claim_accepted_mass(self):
        with self.assertRaisesRegex(ValueError, "rejected batches"):
            bio_oil_batch_cost(sample_inputs(acceptance_passed=False))

    def test_coproduct_credit_requires_disjoint_stream_and_net_costs(self):
        with self.assertRaisesRegex(ValueError, "coproduct credits require"):
            bio_oil_batch_cost(sample_inputs(coproduct_net_credit_usd=10.0))
        result = bio_oil_batch_cost(
            sample_inputs(
                coproduct_net_credit_usd=10.0,
                coproduct_stream_ids=("char-stream-1",),
                coproduct_credits_net_of_incremental_costs=True,
            )
        )
        self.assertEqual(result.coproduct_net_credit_usd, 10.0)
        self.assertAlmostEqual(
            result.net_batch_cost_usd, result.precredit_batch_cost_usd - 10.0
        )

    def test_coproduct_ids_cannot_overlap_or_duplicate(self):
        with self.assertRaisesRegex(ValueError, "cannot also be credited"):
            bio_oil_batch_cost(
                sample_inputs(
                    coproduct_net_credit_usd=1.0,
                    coproduct_stream_ids=("accepted-liquid",),
                    coproduct_credits_net_of_incremental_costs=True,
                )
            )
        with self.assertRaisesRegex(ValueError, "unique nonempty"):
            bio_oil_batch_cost(
                sample_inputs(coproduct_stream_ids=("char", "char"))
            )

    def test_invalid_provenance_or_acceptance_hash_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "provenance_ids"):
            bio_oil_batch_cost(sample_inputs(provenance_ids=()))
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            bio_oil_batch_cost(sample_inputs(acceptance_spec_sha256="not-a-hash"))

    def test_capital_lockup_interest_is_explicit_and_separate(self):
        self.assertAlmostEqual(simple_interest_for_capital_lockup(1000, 0.08, 365), 80.0)
        result = bio_oil_batch_cost(
            sample_inputs(
                rnd_financed_principal_usd=10_000.0,
                rnd_annual_interest_rate=0.08,
                rnd_lockup_days=90,
                rnd_interest_allocation_fraction=0.5,
                rnd_principal_excluded_from_plant_capex=True,
            )
        )
        self.assertAlmostEqual(result.rnd_interest_total_usd, 10_000 * 0.08 * 90 / 365)
        self.assertAlmostEqual(result.allocated_rnd_interest_usd, result.rnd_interest_total_usd * 0.5)

    def test_rnd_principal_in_plant_capex_is_rejected_as_double_count_risk(self):
        with self.assertRaisesRegex(ValueError, "excluded from plant CAPEX"):
            bio_oil_batch_cost(
                sample_inputs(
                    rnd_financed_principal_usd=10_000.0,
                    rnd_principal_excluded_from_plant_capex=False,
                )
            )

    def test_higher_accepted_yield_lowers_cost_per_accepted_energy(self):
        baseline = bio_oil_batch_cost(sample_inputs())
        improved = bio_oil_batch_cost(sample_inputs(accepted_liquid_kg=210.0))
        self.assertLess(
            improved.cost_usd_per_accepted_mj,
            baseline.cost_usd_per_accepted_mj,
        )

    def test_invalid_moisture_and_capacity_factor_fail(self):
        with self.assertRaises(ValueError):
            bio_oil_batch_cost(sample_inputs(moisture_fraction=1.0))
        with self.assertRaisesRegex(ValueError, "capacity_factor"):
            bio_oil_batch_cost(sample_inputs(capacity_factor=1.01))

    def test_unknown_energy_fields_do_not_create_partial_energy_total(self):
        result = bio_oil_batch_cost(
            sample_inputs(utility_electricity_kwh=12.0, utility_process_heat_mj=None)
        )
        self.assertIsNone(result.utility_energy_mj)

    def test_input_evidence_does_not_promote_calculated_result(self):
        result = bio_oil_batch_cost(
            sample_inputs(source_evidence_class="PUBLISHED_EXPERIMENT")
        )
        self.assertEqual(result.input_evidence_class, "PUBLISHED_EXPERIMENT")
        self.assertEqual(result.result_evidence_class, "MODEL_ONLY")

    def test_outputs_are_finite_for_valid_record(self):
        result = bio_oil_batch_cost(sample_inputs())
        self.assertTrue(math.isfinite(result.net_batch_cost_usd))
        self.assertTrue(math.isfinite(result.cost_usd_per_accepted_mj))


if __name__ == "__main__":
    unittest.main()
