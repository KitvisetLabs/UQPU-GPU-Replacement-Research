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

    def test_contract_keeps_equation_baseline_constraints_and_falsifier(self):
        fields = required_discovery_fields()
        for name in (
            "baseline_model",
            "proposed_equation",
            "known_constraints_checked",
            "falsifier",
            "discriminating_observables",
            "independent_validation_plan",
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


    def test_bic_candidate_count_is_invariant_to_common_residual_unit_scaling(self):
        baseline = select_bic_candidate_count(
            residual_sums_squares={1: 100.0, 2: 30.0},
            parameter_counts={1: 2, 2: 4},
            sample_count=100,
        )
        baseline_delta = baseline.scores[1][1] - baseline.scores[0][1]

        # Changing the measurement unit multiplies every RSS by the same
        # positive squared scale. The Gaussian BIC score shifts by a common
        # additive constant, so candidate ranking must not change.
        for rss_scale in (1e-12, 1e12):
            with self.subTest(rss_scale=rss_scale):
                scaled = select_bic_candidate_count(
                    residual_sums_squares={2: 30.0 * rss_scale, 1: 100.0 * rss_scale},
                    parameter_counts={2: 4, 1: 2},
                    sample_count=100,
                )
                scaled_delta = scaled.scores[1][1] - scaled.scores[0][1]
                self.assertEqual(scaled.selected_count, baseline.selected_count)
                self.assertAlmostEqual(scaled_delta, baseline_delta, places=9)


if __name__ == "__main__":
    unittest.main()
