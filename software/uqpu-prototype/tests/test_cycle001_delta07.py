import unittest
from dataclasses import replace

from uqpu.cycle001_delta07 import (
    BosonicMemoryResourceLedger,
    PangolaCouponResult,
    ProviderAICostLink,
    ReplicationPackage,
    bosonic_memory_template,
    bosonic_missing_resources,
    canonical_provider_ai_cost_links,
    capital_gate_records,
    compare_coupon_curves,
    coupon_missing_preregistration_and_measurements,
    cycle001_delta07_artifact,
    evaluate_provider_ai_cost_link,
    evaluate_replication_pair,
    ising_missing_resources,
    ising_pair_template,
    validate_bosonic_memory,
    validate_capital_gate_record,
    validate_coupon_result,
    validate_ising_comparison,
)
from uqpu.scm_replication_contract import REQUIRED_ENVIRONMENT_FIELDS, ReplicationManifest, sha256_bytes


class Delta07Tests(unittest.TestCase):
    def test_ising_ledgers_cannot_compare_different_output_or_instance(self):
        classical, quantum = ising_pair_template()
        self.assertIn("missing:instance_sha256", validate_ising_comparison(classical, quantum))
        quantum = replace(quantum, output_contract_id="different contract")
        self.assertIn("mismatch:output_contract_id", validate_ising_comparison(classical, quantum))
        self.assertTrue(ising_missing_resources(classical, quantum))

    def test_bosonic_template_exposes_the_unmeasured_overhead(self):
        x = bosonic_memory_template()
        self.assertEqual(x.evidence_class, "LITERATURE_ANCHORED_RESOURCE_TEMPLATE")
        self.assertEqual(validate_bosonic_memory(x), ())
        missing = bosonic_missing_resources(x)
        self.assertIn("state_prep_seconds", missing)
        self.assertIn("decoder_seconds", missing)
        self.assertIn("cost_usd", missing)
        self.assertGreater(len(missing), 5)

    def test_coupon_requires_matched_measured_curves_before_comparison(self):
        blank = PangolaCouponResult("DMF-BIOCARBON-EMI-001", "", "", "", "", 1e6, 1e9)
        self.assertIn("TEMPLATE_NO_MEASUREMENTS", blank.evidence_class)
        self.assertEqual(blank.shielding_curve_db, ())
        self.assertEqual(validate_coupon_result(blank), ())
        self.assertIn("shielding_curve_db", coupon_missing_preregistration_and_measurements(blank))
        with self.assertRaisesRegex(ValueError, "both measured shielding curves"):
            compare_coupon_curves(blank, blank)

    def test_coupon_comparison_rejects_different_thickness_and_frequency_grid(self):
        candidate = PangolaCouponResult("DMF-BIOCARBON-EMI-001", "lot-1", "inc-1", "r1", "method", 1e6, 1e9, 1.0, 2.0, shielding_curve_db=((1e6, 20.0),))
        incumbent = replace(candidate, incumbent_id="inc-1", shielding_curve_db=((1e6, 18.0),))
        self.assertEqual(compare_coupon_curves(candidate, incumbent), ((1e6, 2.0),))
        with self.assertRaisesRegex(ValueError, "thickness mismatch"):
            compare_coupon_curves(candidate, replace(incumbent, thickness_mm=1.1))
        with self.assertRaisesRegex(ValueError, "areal-density mismatch"):
            compare_coupon_curves(candidate, replace(incumbent, areal_density_kg_m2=2.2))
        with self.assertRaisesRegex(ValueError, "frequency grids differ"):
            compare_coupon_curves(candidate, replace(incumbent, shielding_curve_db=((2e6, 18.0),)))

    def test_replication_evaluator_checks_data_integrity_independence_and_drift(self):
        def package(data, team, site, *, score="exact-match-v1", independent=False):
            manifest = ReplicationManifest(
                "SCM-GATE-003", "1.0", "commit-a", sha256_bytes(data), "schema-v1",
                "CSPRNG-after-isolation", score, ("hardware-failure-only",),
                REQUIRED_ENVIRONMENT_FIELDS,
            )
            return ReplicationPackage(manifest, data, team, site, independent)

        from uqpu.cycle001_delta07 import ReplicationPackage
        primary = package(b"primary", "team-a", "site-a")
        second = package(b"replica", "team-b", "site-b", independent=True)
        result = evaluate_replication_pair(primary, second)
        self.assertEqual(result.status, "CONSISTENT_REPLICATION_PACKAGES")
        self.assertFalse(result.source_claim_supported)
        self.assertEqual(result.evidence_class, "REPLICATION_INFRASTRUCTURE_ONLY")

        drifted = package(b"replica", "team-b", "site-b", score="post-hoc-score", independent=True)
        self.assertEqual(evaluate_replication_pair(primary, drifted).status, "BLOCKED")
        bad_hash = replace(second, raw_data=b"tampered")
        self.assertIn("replication:dataset_integrity_failure", evaluate_replication_pair(primary, bad_hash).errors)

    def test_capital_gate_records_keep_amount_unbudgeted_and_unauthorized(self):
        records = capital_gate_records()
        self.assertEqual({x.gate_id for x in records}, {"CAP-DMF-EMI-001", "CAP-BOSONIC-001"})
        for record in records:
            self.assertIsNone(record.proposed_capital_at_risk_thb)
            self.assertEqual(record.authorization_status, "NOT_AUTHORIZED")
            self.assertEqual(validate_capital_gate_record(record), ())

    def test_provider_cost_unknown_blocks_numeric_claim_but_enables_sensitivity(self):
        low, high = canonical_provider_ai_cost_links()
        self.assertEqual(evaluate_provider_ai_cost_link(low).status, "PRICE_EVIDENCE_REQUIRED")
        target_usd = low.target_thb / low.thb_per_usd
        result = evaluate_provider_ai_cost_link(replace(low, provider_component_cost_usd=target_usd * 0.25, other_fixed_cost_usd=target_usd * 0.25))
        self.assertAlmostEqual(result.maximum_residual_fraction, (target_usd * 0.5) / low.baseline_usd)
        blocked = evaluate_provider_ai_cost_link(replace(high, provider_component_cost_usd=target_usd + 1.0, other_fixed_cost_usd=0.0))
        self.assertEqual(blocked.status, "FIXED_COSTS_EXCEED_TOTAL_TARGET")
        self.assertEqual(blocked.maximum_residual_fraction, 0.0)
        with self.assertRaises(ValueError):
            evaluate_provider_ai_cost_link(replace(low, provider_component_cost_usd=-1.0))

    def test_machine_readable_cycle_record_keeps_all_current_measurements_unknown(self):
        record = cycle001_delta07_artifact()
        self.assertEqual(record["status"], "ALL_LANE_CONTRACTS_AND_TEMPLATES_NO_NEW_EMPIRICAL_CLAIM")
        self.assertIsNone(record["ising"]["classical"]["wall_seconds"])
        self.assertEqual(record["pangola_coupon"]["shielding_curve_db"], ())
        self.assertEqual(record["scm_replication"]["status"], "AWAITING_PRIMARY_AND_INDEPENDENT_REPLICATION_PACKAGES")
        self.assertTrue(all(x["status"] == "PRICE_EVIDENCE_REQUIRED" for x in record["provider_ai_cost_links"]))


if __name__ == "__main__":
    unittest.main()
