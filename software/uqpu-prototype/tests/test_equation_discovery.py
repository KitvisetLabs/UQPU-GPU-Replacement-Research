import unittest

from uqpu.equation_discovery import EquationHypothesis, required_discovery_fields


class EquationDiscoveryTests(unittest.TestCase):
    def _candidate(self, **overrides):
        data = dict(
            equation_id="EQN-test-001",
            baseline_model="y = a*x",
            proposed_equation="y = a*x + b*x**2",
            variables_and_units=("x [s]", "y [m]", "a [m/s]", "b [m/s^2]"),
            domain_and_assumptions=("x >= 0", "closed test domain"),
            known_constraints_checked=("dimensional consistency", "finite x->0 limit"),
            scaling_or_limiting_cases=("b->0 recovers baseline",),
            falsifier="held-out error is not lower than baseline or predicted curvature is absent",
            discriminating_observables=("held-out y(x)",),
            evidence_level="CONCEPT",
            data_or_proof_provenance=("synthetic unit-test dataset",),
            independent_validation_plan=("blind held-out dataset",),
            heldout_baseline_error=0.2,
            heldout_candidate_error=0.1,
        )
        data.update(overrides)
        return EquationHypothesis(**data)

    def test_complete_candidate_is_testable(self):
        candidate = self._candidate()
        candidate.validate()
        self.assertTrue(candidate.testable)

    def test_ai_generated_concept_cannot_be_promoted_to_physical_candidate(self):
        candidate = self._candidate(independent_validation_count=10)
        self.assertFalse(candidate.ready_for_physical_candidate_claim)

    def test_missing_falsifier_is_rejected(self):
        candidate = self._candidate(falsifier="")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_unknown_evidence_label_is_rejected(self):
        candidate = self._candidate(evidence_level="AI_DISCOVERED_LAW")
        with self.assertRaises(ValueError):
            candidate.validate()

    def test_missing_provenance_is_rejected_even_if_validation_plan_exists(self):
        candidate = self._candidate(data_or_proof_provenance=())
        with self.assertRaises(ValueError):
            candidate.validate()
        self.assertFalse(candidate.testable)

    def test_missing_independent_validation_plan_is_rejected(self):
        candidate = self._candidate(independent_validation_plan=())
        with self.assertRaises(ValueError):
            candidate.validate()
        self.assertFalse(candidate.testable)

    def test_blank_required_tuple_entries_are_rejected(self):
        for field_name in (
            "variables_and_units",
            "domain_and_assumptions",
            "known_constraints_checked",
            "scaling_or_limiting_cases",
            "discriminating_observables",
            "data_or_proof_provenance",
            "independent_validation_plan",
        ):
            with self.subTest(field_name=field_name):
                candidate = self._candidate(**{field_name: ("",)})
                with self.assertRaises(ValueError):
                    candidate.validate()

    def test_nonfinite_heldout_errors_are_rejected(self):
        for field_name in ("heldout_baseline_error", "heldout_candidate_error"):
            for value in (float("nan"), float("inf"), float("-inf")):
                with self.subTest(field_name=field_name, value=value):
                    candidate = self._candidate(**{field_name: value})
                    with self.assertRaises(ValueError):
                        candidate.validate()

    def test_nonnumeric_heldout_errors_are_rejected(self):
        for field_name in ("heldout_baseline_error", "heldout_candidate_error"):
            for value in ("0.1", True):
                with self.subTest(field_name=field_name, value=value):
                    candidate = self._candidate(**{field_name: value})
                    with self.assertRaises(ValueError):
                        candidate.validate()

    def test_negative_heldout_errors_are_rejected(self):
        for field_name in ("heldout_baseline_error", "heldout_candidate_error"):
            with self.subTest(field_name=field_name):
                candidate = self._candidate(**{field_name: -0.01})
                with self.assertRaises(ValueError):
                    candidate.validate()

    def test_validation_count_must_be_nonnegative_integer(self):
        for value in (-1, 1.5, True):
            with self.subTest(value=value):
                candidate = self._candidate(independent_validation_count=value)
                with self.assertRaises(ValueError):
                    candidate.validate()

    def test_physical_candidate_gate_requires_independent_validation_and_heldout_gain(self):
        candidate = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
        )
        self.assertTrue(candidate.ready_for_physical_candidate_claim)
        no_replication = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=0,
        )
        self.assertFalse(no_replication.ready_for_physical_candidate_claim)
        no_gain = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=1,
            heldout_candidate_error=0.3,
        )
        self.assertFalse(no_gain.ready_for_physical_candidate_claim)

    def test_contract_keeps_equation_baseline_constraints_and_falsifier(self):
        fields = required_discovery_fields()
        for name in (
            "baseline_model",
            "proposed_equation",
            "known_constraints_checked",
            "falsifier",
            "discriminating_observables",
            "data_or_proof_provenance",
            "independent_validation_plan",
        ):
            self.assertIn(name, fields)


if __name__ == "__main__":
    unittest.main()
