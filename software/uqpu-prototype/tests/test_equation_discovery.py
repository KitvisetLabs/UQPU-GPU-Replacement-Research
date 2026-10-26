import unittest

from uqpu.equation_discovery import (
    EquationHypothesis,
    required_discovery_fields,
    select_bic_candidate_count,
)


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
            incumbent_assumption="linear baseline assumes no quadratic curvature",
            dimensional_symmetry_conservation_causality_checks=(
                "units agree for every term",
                "declared symmetry is preserved",
                "conservation constraints are unchanged",
                "causal domain excludes future-to-past dependence",
            ),
            counterexample_search_plan="probe domain boundaries, singular limits, symmetry transforms and adversarial points",
            counterexample_search_status="NO_COUNTEREXAMPLE_FOUND",
            counterexample_notes=(),
            heldout_prediction="positive curvature persists on the preregistered blind domain",
            proof_or_discriminating_experiment_plan=(
                "verify the b->0 limiting case algebraically",
                "measure y(x) on a blind held-out dataset",
            ),
            formal_proof_status="NOT_RUN",
            formal_proof_notes=(),
            false_discovery_status="NO_FALSE_DISCOVERY_FOUND",
            false_discovery_notes=(),
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

    def test_explicit_incumbent_and_physics_gates_are_required(self):
        with self.assertRaises(ValueError):
            self._candidate(incumbent_assumption="").validate()
        with self.assertRaises(ValueError):
            self._candidate(dimensional_symmetry_conservation_causality_checks=()).validate()
        with self.assertRaises(ValueError):
            self._candidate(counterexample_search_plan="").validate()
        with self.assertRaises(ValueError):
            self._candidate(heldout_prediction="").validate()
        with self.assertRaises(ValueError):
            self._candidate(proof_or_discriminating_experiment_plan=()).validate()

    def test_formal_proof_status_is_explicit_and_auditable(self):
        with self.assertRaises(ValueError):
            self._candidate(formal_proof_status="KERNEL_CHECKED").validate()
        with self.assertRaises(ValueError):
            self._candidate(formal_proof_status="CHECKED", formal_proof_notes=()).validate()
        checked = self._candidate(
            formal_proof_status="CHECKED",
            formal_proof_notes=("synthetic unit-test theorem; pinned checker and statement hash recorded",),
        )
        checked.validate()

    def test_counterexamples_and_false_discoveries_block_candidate_promotion(self):
        unsearched = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT", independent_validation_count=1,
            counterexample_search_status="NOT_RUN",
        )
        self.assertFalse(unsearched.ready_for_physical_candidate_claim)
        counterexample = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT", independent_validation_count=1,
            counterexample_search_status="COUNTEREXAMPLE_FOUND",
            counterexample_notes=("candidate fails at x=0.9",),
        )
        self.assertFalse(counterexample.ready_for_physical_candidate_claim)
        false_discovery = self._candidate(
            evidence_level="PUBLISHED_EXPERIMENT", independent_validation_count=1,
            false_discovery_status="FALSE_DISCOVERY_FOUND",
            false_discovery_notes=("apparent gain disappears under a unit-consistent holdout",),
        )
        self.assertFalse(false_discovery.ready_for_physical_candidate_claim)

    def test_contract_keeps_equation_baseline_constraints_and_falsifier(self):
        fields = required_discovery_fields()
        for name in (
            "baseline_model",
            "proposed_equation",
            "known_constraints_checked",
            "falsifier",
            "discriminating_observables",
            "independent_validation_plan",
            "incumbent_assumption",
            "dimensional_symmetry_conservation_causality_checks",
            "counterexample_search_plan",
            "counterexample_search_status",
            "heldout_prediction",
            "proof_or_discriminating_experiment_plan",
            "formal_proof_status",
            "formal_proof_notes",
            "false_discovery_status",
            "false_discovery_notes",
        ):
            self.assertIn(name, fields)


    def test_bic_prefers_one_candidate_when_extra_fit_is_too_small(self):
        result = select_bic_candidate_count(
            residual_sums_squares={1: 100.0, 2: 95.0},
            parameter_counts={1: 2, 2: 4},
            sample_count=100,
        )
        self.assertEqual(result.selected_count, 1)
        self.assertLess(result.scores[0][1], result.scores[1][1])

    def test_bic_selects_two_candidate_models_for_large_fit_improvement(self):
        result = select_bic_candidate_count(
            residual_sums_squares={1: 100.0, 2: 30.0},
            parameter_counts={1: 2, 2: 4},
            sample_count=100,
        )
        self.assertEqual(result.selected_count, 2)
        self.assertEqual(tuple(count for count, _ in result.scores), (1, 2))

    def test_bic_rejects_mismatched_counts_and_nonpositive_rss(self):
        with self.assertRaises(ValueError):
            select_bic_candidate_count({1: 10.0}, {2: 1}, sample_count=20)
        with self.assertRaises(ValueError):
            select_bic_candidate_count({1: 0.0}, {1: 1}, sample_count=20)
        with self.assertRaises(ValueError):
            select_bic_candidate_count({1: float("nan")}, {1: 1}, sample_count=20)

    def test_bic_rejects_invalid_sample_and_parameter_contracts(self):
        for sample_count in (True, 1, 10.0):
            with self.subTest(sample_count=sample_count):
                with self.assertRaises(ValueError):
                    select_bic_candidate_count({1: 10.0}, {1: 1}, sample_count=sample_count)
        with self.assertRaises(ValueError):
            select_bic_candidate_count({1: 10.0}, {1: 10}, sample_count=10)


if __name__ == "__main__":
    unittest.main()
