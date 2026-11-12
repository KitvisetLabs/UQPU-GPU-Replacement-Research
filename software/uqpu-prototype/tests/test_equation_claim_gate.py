import unittest

from uqpu.equation_claim_gate import EquationClaimGate, required_equation_claim_fields


def valid_claim(**overrides):
    fields = dict(
        claim_id="EQN-TEST-001",
        incumbent_assumption="The constitutive closure is local in time.",
        incumbent_model="y(t) = a*x(t)",
        alternative_equation="y(t) = a*x(t) + b*integral(exp(-(t-s)/tau)*x(s), ds)",
        variables_and_units=("x: m", "y: N", "t: s", "a: N/m", "b: N/(m*s)"),
        domain_and_assumptions=("t >= 0", "linear response regime"),
        dimensional_analysis="Every additive term has units of force.",
        symmetry_checks=("Check time-translation symmetry in the stationary limit.",),
        conservation_checks=("Check the stated energy balance for the coupled system.",),
        causality_checks=("Kernel vanishes for s > t.",),
        limiting_cases=("b -> 0 recovers the incumbent model.", "tau -> 0 has a finite stated limit."),
        falsifier="Held-out residuals fail to improve at the preregistered threshold.",
        discriminating_observable="Phase lag after a frozen step input.",
        heldout_prediction="Predict phase lag for a withheld forcing waveform.",
        counterexample_search_plan="Sweep boundary values and search sign/scale counterexamples.",
        proof_or_simulation_plan="Check symbolic dimensions and simulate a frozen synthetic system.",
        experiment_plan="Measure a preregistered step response if the model-only gate passes.",
        independent_validation_plan="A second implementation scores sealed held-out data.",
        device_or_system_consequence="Could change the controller state-memory requirement if validated.",
        economic_consequence="Any cost effect is evaluated only after measured system validation.",
        source_provenance="Frozen source hash and dataset hash in the run manifest.",
        failure_recording_plan="Retain all rejected candidates, counterexamples, and failed runs.",
        evidence_level="MODEL_ONLY",
    )
    fields.update(overrides)
    return EquationClaimGate(**fields)


class EquationClaimGateTests(unittest.TestCase):
    def test_complete_hypothesis_passes_metadata_gate_only(self):
        claim = valid_claim()
        claim.validate()
        self.assertTrue(claim.test_contract_complete)
        self.assertEqual(claim.evidence_boundary, "HYPOTHESIS_ONLY_PENDING_INDEPENDENT_EVIDENCE")

    def test_explicit_incumbent_assumption_and_alternative_are_required(self):
        for field in ("incumbent_assumption", "incumbent_model", "alternative_equation"):
            with self.subTest(field=field):
                claim = valid_claim(**{field: "   "})
                self.assertFalse(claim.test_contract_complete)
                with self.assertRaisesRegex(ValueError, field):
                    claim.validate()

    def test_each_physics_constraint_family_is_explicit(self):
        for field in ("dimensional_analysis", "symmetry_checks", "conservation_checks", "causality_checks", "limiting_cases"):
            with self.subTest(field=field):
                claim = valid_claim(**{field: () if field.endswith("checks") or field == "limiting_cases" else ""})
                self.assertIn(field, claim.missing_required_fields())

    def test_falsifier_observable_heldout_proof_experiment_and_replication_are_required(self):
        fields = ("falsifier", "discriminating_observable", "heldout_prediction", "counterexample_search_plan", "proof_or_simulation_plan", "experiment_plan", "independent_validation_plan")
        for field in fields:
            with self.subTest(field=field):
                claim = valid_claim(**{field: ""})
                self.assertIn(field, claim.missing_required_fields())

    def test_system_economic_and_failure_paths_are_required(self):
        for field in ("device_or_system_consequence", "economic_consequence", "failure_recording_plan", "source_provenance"):
            with self.subTest(field=field):
                claim = valid_claim(**{field: ""})
                self.assertIn(field, claim.missing_required_fields())

    def test_sequence_fields_fail_closed_on_lists_and_blank_entries(self):
        self.assertIn("variables_and_units", valid_claim(variables_and_units=["x: m"]).missing_required_fields())
        self.assertIn("symmetry_checks", valid_claim(symmetry_checks=("   ",)).missing_required_fields())

    def test_unknown_evidence_level_is_rejected(self):
        claim = valid_claim(evidence_level="NEW_PHYSICS_CONFIRMED")
        self.assertIn("evidence_level", claim.missing_required_fields())
        with self.assertRaisesRegex(ValueError, "evidence_level"):
            claim.validate()
        malformed = valid_claim(evidence_level=["MODEL_ONLY"])
        self.assertIn("evidence_level", malformed.missing_required_fields())

    def test_model_only_does_not_promote_to_law(self):
        claim = valid_claim(evidence_level="MODEL_ONLY")
        claim.validate()
        self.assertEqual(claim.evidence_boundary, "HYPOTHESIS_ONLY_PENDING_INDEPENDENT_EVIDENCE")

    def test_required_fields_are_stable_and_include_user_mandated_gates(self):
        fields = required_equation_claim_fields()
        for name in ("incumbent_assumption", "dimensional_analysis", "symmetry_checks", "conservation_checks", "causality_checks", "limiting_cases", "falsifier", "discriminating_observable", "heldout_prediction", "counterexample_search_plan", "experiment_plan", "independent_validation_plan", "device_or_system_consequence", "economic_consequence", "failure_recording_plan"):
            self.assertIn(name, fields)


if __name__ == "__main__":
    unittest.main()
