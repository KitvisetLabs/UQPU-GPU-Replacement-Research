import unittest
from dataclasses import replace

from uqpu.cycle001_delta07 import PangolaCouponResult, compare_coupon_curves
from uqpu.scm_preregistration import (
    REQUIRED_LEAKAGE_ITEMS,
    SCMPreregistration,
    validate_preregistration,
)


def complete_preregistration(**changes):
    values = dict(
        study_id="SCM-SYNTHETIC-CAL-001",
        protocol_version="1.0",
        primary_hypothesis="known synthetic interference is detected",
        null_hypothesis="the sealed synthetic label has no association with the registered output",
        primary_outcome="exact-match rate on synthetic packets",
        sample_size=10,
        stopping_rule="stop after the registered ten synthetic trials",
        randomization_method="seeded cryptographic pseudorandom assignment",
        blinding_roles=("packet custodian", "scorer"),
        exclusion_rules=("predeclared file-integrity failure only",),
        leakage_audit_items=REQUIRED_LEAKAGE_ITEMS,
        calibration_plan="inject known synthetic interference",
        analysis_plan="compute the preregistered exact-match rate",
        replication_plan="independent code review on held-out synthetic packets",
    )
    values.update(changes)
    return SCMPreregistration(**values)


class Cycle002Delta01SafeguardTests(unittest.TestCase):
    def test_coupon_comparison_uses_explicit_preregistered_geometry_tolerance(self):
        candidate = PangolaCouponResult(
            "DMF-BIOCARBON-EMI-001", "unmeasured-lot", "pangola", "recipe-1", "ASTM-D4935-18R26",
            30e6, 1.5e9, 1.50, 2.085, shielding_curve_db=((30e6, 10.0), (1.5e9, 12.0)),
        )
        incumbent = replace(
            candidate, incumbent_id="Parker-A230-HTHF", thickness_mm=1.52,
            areal_density_kg_m2=2.12, shielding_curve_db=((30e6, 11.0), (1.5e9, 15.0)),
        )
        result = compare_coupon_curves(candidate, incumbent, geometry_rel_tolerance=0.02)
        self.assertEqual(result, ((30e6, -1.0), (1.5e9, -3.0)))
        with self.assertRaisesRegex(ValueError, "areal-density mismatch"):
            compare_coupon_curves(candidate, replace(incumbent, areal_density_kg_m2=2.13), geometry_rel_tolerance=0.02)
        with self.assertRaisesRegex(ValueError, "geometry_rel_tolerance"):
            compare_coupon_curves(candidate, incumbent, geometry_rel_tolerance=-0.01)

    def test_human_participant_readiness_requires_consent_scope_and_reference(self):
        incomplete = complete_preregistration(human_participants=True)
        errors = validate_preregistration(incomplete)
        self.assertIn("missing:ethics_approval_ref", errors)
        self.assertIn("invalid:consent_status", errors)
        self.assertIn("missing:consent_scope", errors)
        self.assertIn("missing:consent_reference", errors)
        documented = replace(
            incomplete,
            ethics_approval_ref="ethics-approval-reference",
            consent_status="DOCUMENTED",
            consent_scope="participation in the preregistered protocol",
            consent_reference="approved-consent-record-reference",
        )
        self.assertEqual(validate_preregistration(documented), ())

    def test_ethics_approved_waiver_is_explicit_and_nonhuman_studies_default_cleanly(self):
        waiver = complete_preregistration(
            human_participants=True,
            ethics_approval_ref="approved-waiver-reference",
            consent_status="WAIVED_WITH_ETHICS_APPROVAL",
            consent_scope="approved waiver applies to this protocol",
            consent_reference="waiver-record-reference",
        )
        self.assertEqual(validate_preregistration(waiver), ())
        synthetic = complete_preregistration()
        self.assertEqual(synthetic.consent_status, "NOT_APPLICABLE")
        self.assertEqual(validate_preregistration(synthetic), ())
        inconsistent = replace(synthetic, consent_status="DOCUMENTED")
        self.assertIn("unexpected:consent_fields_without_human_participants", validate_preregistration(inconsistent))


if __name__ == "__main__":
    unittest.main()
