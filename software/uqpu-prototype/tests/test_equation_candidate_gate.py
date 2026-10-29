import unittest

from uqpu.equation_candidate_gate import evaluate_candidate_acceptance


class EquationCandidateGateTests(unittest.TestCase):
    def evaluate(self, candidate, amplification=0.0, violations=0, failures=0):
        return evaluate_candidate_acceptance(
            reference_outputs=(1.0, 2.0),
            candidate_outputs=candidate,
            output_scales=(1.0, 2.0),
            measured_perturbation_amplification=amplification,
            max_normalized_rms_error=0.01,
            max_perturbation_amplification=5.0,
            constraint_violations=violations,
            numerical_failures=failures,
        )

    def test_accurate_stable_candidate_passes_synthetic_gate_only(self):
        result = self.evaluate((1.0, 2.0))
        self.assertTrue(result["accepted_for_synthetic_benchmark"])
        self.assertEqual(result["evidence_class"], "MODEL_ONLY_SYNTHETIC_EQUATION_EVALUATION")
        self.assertIn("does not prove", result["claim_boundary"])

    def test_zero_sensitivity_does_not_rescue_inaccurate_constant_candidate(self):
        result = self.evaluate((0.0, 0.0), amplification=0.0)
        self.assertFalse(result["accepted_for_synthetic_benchmark"])
        self.assertAlmostEqual(result["metrics"]["normalized_rms_error"], 1.0)
        self.assertIn("HELDOUT_ACCURACY_THRESHOLD_FAILED", result["rejection_reasons"])

    def test_good_fit_does_not_rescue_unstable_candidate(self):
        result = self.evaluate((1.0, 2.0), amplification=6.0)
        self.assertFalse(result["accepted_for_synthetic_benchmark"])
        self.assertIn("PERTURBATION_STABILITY_THRESHOLD_FAILED", result["rejection_reasons"])

    def test_constraint_violations_and_numerical_failures_are_hard_stops(self):
        self.assertFalse(self.evaluate((1.0, 2.0), violations=1)["accepted_for_synthetic_benchmark"])
        self.assertFalse(self.evaluate((1.0, 2.0), failures=1)["accepted_for_synthetic_benchmark"])

    def test_nonfinite_candidate_is_rejected_before_scoring(self):
        with self.assertRaises(ValueError):
            self.evaluate((1.0, float("nan")))

    def test_thresholds_must_be_nonnegative_and_finite(self):
        with self.assertRaises(ValueError):
            evaluate_candidate_acceptance(
                (1.0,), (1.0,), (1.0,), 0.0, float("inf"), 1.0
            )


if __name__ == "__main__":
    unittest.main()
