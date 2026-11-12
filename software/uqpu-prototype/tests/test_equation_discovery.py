import unittest

from uqpu.equation_discovery import (
    EquationHypothesis,
    required_discovery_fields,
    select_bic_candidate_count,
    evaluate_bic_selection_stability,
)
from uqpu.formal_proof_evidence import build_formal_proof_evidence


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

    def _formal_proof_evidence(self, status="KERNEL_CHECKED", **overrides):
        values = dict(
            claim_id="EQN-test-001",
            claim_kind="PHYSICAL_EQUATION_HYPOTHESIS",
            statement="y = a*x + b*x**2",
            assumptions=("x >= 0", "declared unit contract"),
            status=status,
            source_revision="a" * 40,
            proof_artifact=b"theorem proof bytes\\n",
            checker_name="Lean",
            checker_version="4.19.0",
            checker_command="lake env lean Candidate.lean",
            environment_bytes=b"pinned toolchain manifest\\n",
            run_log=b"exit_code=1\\n" if status == "FAILED" else b"exit_code=0\\n",
            checker_exit_code=1 if status == "FAILED" else 0,
            independent_reproduction_count=1 if status == "INDEPENDENTLY_REPRODUCED" else 0,
            notes=("checker rejected candidate",) if status == "FAILED" else (("independent reproduction inconclusive",) if status == "INCONCLUSIVE" else ()),
        )
        values.update(overrides)
        return build_formal_proof_evidence(**values)

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

    def test_formal_proof_status_requires_exact_bound_evidence(self):
        notes = ("synthetic unit-test theorem; pinned checker and statement hash recorded",)
        with self.assertRaisesRegex(ValueError, "formal_proof_evidence is required"):
            self._candidate(formal_proof_status="CHECKED", formal_proof_notes=notes).validate()

        checked = self._candidate(
            formal_proof_status="CHECKED",
            formal_proof_notes=notes,
            formal_proof_evidence=self._formal_proof_evidence(),
        )
        checked.validate()

        with self.assertRaisesRegex(ValueError, "claim_id must match equation_id"):
            self._candidate(
                formal_proof_status="CHECKED",
                formal_proof_notes=notes,
                formal_proof_evidence=self._formal_proof_evidence(claim_id="EQN-other-001"),
            ).validate()

        with self.assertRaisesRegex(ValueError, "status does not match formal_proof_status"):
            self._candidate(
                formal_proof_status="FAILED",
                formal_proof_notes=("failed attempt retained",),
                formal_proof_evidence=self._formal_proof_evidence(),
            ).validate()

    def test_formal_statement_and_failure_states_remain_distinct(self):
        statement_only = self._candidate(
            formal_proof_status="FORMAL_STATEMENT",
            formal_proof_evidence=self._formal_proof_evidence("FORMAL_STATEMENT"),
        )
        statement_only.validate()
        self.assertFalse(statement_only.ready_for_physical_candidate_claim)

        failed = self._candidate(
            formal_proof_status="FAILED",
            formal_proof_notes=("checker rejected candidate",),
            formal_proof_evidence=self._formal_proof_evidence("FAILED"),
        )
        failed.validate()
        self.assertFalse(failed.ready_for_physical_candidate_claim)

    def test_proof_reproduction_does_not_replace_physical_replication(self):
        candidate = self._candidate(
            formal_proof_status="INDEPENDENTLY_REPRODUCED",
            formal_proof_notes=("formal proof independently rebuilt",),
            formal_proof_evidence=self._formal_proof_evidence("INDEPENDENTLY_REPRODUCED"),
            evidence_level="PUBLISHED_EXPERIMENT",
            independent_validation_count=0,
        )
        candidate.validate()
        self.assertFalse(candidate.ready_for_physical_candidate_claim)

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

    def test_heldout_errors_must_be_finite_numeric_and_non_boolean(self):
        invalid_values = (
            float("nan"),
            float("inf"),
            float("-inf"),
            True,
            False,
            "0.1",
        )
        for field_name in ("heldout_baseline_error", "heldout_candidate_error"):
            for invalid_value in invalid_values:
                with self.subTest(field=field_name, value=invalid_value):
                    with self.assertRaisesRegex(ValueError, "finite numeric value"):
                        self._candidate(**{field_name: invalid_value}).validate()

        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            self._candidate(heldout_candidate_error=-0.1).validate()

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
            "formal_proof_evidence",
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


    def test_bic_stability_reports_unique_selection_at_preregistered_threshold(self):
        weak_gain = {1: 100.0, 2: 95.0}
        strong_gain = {1: 100.0, 2: 30.0}
        rss = {
            "seed-01": weak_gain,
            "seed-02": weak_gain,
            "seed-03": weak_gain,
            "seed-04": weak_gain,
            "seed-05": strong_gain,
        }
        result = evaluate_bic_selection_stability(
            replicate_residual_sums_squares=rss,
            parameter_counts={1: 2, 2: 4},
            sample_counts={seed: 100 for seed in rss},
            minimum_selection_fraction=0.8,
        )
        self.assertTrue(result.stable)
        self.assertEqual(result.stable_selection, 1)
        self.assertEqual(result.replicate_count, 5)
        self.assertEqual(result.selection_frequencies, ((1, 4, 0.8), (2, 1, 0.2)))
        self.assertEqual(tuple(seed for seed, _ in result.selections), tuple(sorted(rss)))

    def test_bic_stability_tie_is_unstable_even_at_half_threshold(self):
        result = evaluate_bic_selection_stability(
            replicate_residual_sums_squares={
                "weak-fit-gain": {1: 100.0, 2: 95.0},
                "large-fit-gain": {1: 100.0, 2: 30.0},
            },
            parameter_counts={1: 2, 2: 4},
            sample_counts={"weak-fit-gain": 100, "large-fit-gain": 100},
            minimum_selection_fraction=0.5,
        )
        self.assertFalse(result.stable)
        self.assertIsNone(result.stable_selection)

    def test_bic_stability_fails_closed_on_missing_or_mismatched_replicates(self):
        with self.assertRaises(ValueError):
            evaluate_bic_selection_stability(
                {"only-one": {1: 10.0}},
                {1: 1},
                {"only-one": 20},
            )
        with self.assertRaises(ValueError):
            evaluate_bic_selection_stability(
                {"a": {1: 10.0}, "b": {1: 11.0}},
                {1: 1},
                {"a": 20},
            )
        with self.assertRaises(ValueError):
            evaluate_bic_selection_stability(
                {"a": {1: 10.0}, "b": {1: 11.0, 2: 9.0}},
                {1: 1, 2: 2},
                {"a": 20, "b": 20},
            )

    def test_bic_stability_rejects_invalid_thresholds(self):
        for threshold in (True, 0.0, 1.1, float("nan"), float("inf")):
            with self.subTest(threshold=threshold):
                with self.assertRaises(ValueError):
                    evaluate_bic_selection_stability(
                        {"a": {1: 10.0}, "b": {1: 11.0}},
                        {1: 1},
                        {"a": 20, "b": 20},
                        minimum_selection_fraction=threshold,
                    )


if __name__ == "__main__":
    unittest.main()
