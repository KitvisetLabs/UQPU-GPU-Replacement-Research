import unittest

from uqpu.equation_recovery_stress import (
    CandidateExpression,
    fit_candidate,
    run_noise_trial,
    run_stress_suite,
)


class EquationRecoveryStressTests(unittest.TestCase):
    def test_unit_consistent_distractors_do_not_need_dimension_filter(self):
        z = (0.5, 1.0, 1.5, 2.0, 2.5, 3.0)
        y = tuple(2.0 * value**2 for value in z)
        fit = fit_candidate(
            z,
            y,
            CandidateExpression((2,)),
            train_indices=(0, 2, 4),
            holdout_indices=(1,),
            extrapolation_indices=(3, 5),
        )
        self.assertAlmostEqual(fit.holdout_rmse, 0.0, places=12)
        self.assertAlmostEqual(fit.extrapolation_rmse, 0.0, places=12)

    def test_splits_must_be_disjoint(self):
        with self.assertRaises(ValueError):
            fit_candidate(
                (0.5, 1.0, 1.5, 2.0),
                (0.25, 1.0, 2.25, 4.0),
                CandidateExpression((2,)),
                train_indices=(0, 1),
                holdout_indices=(1, 2),
                extrapolation_indices=(3,),
            )

    def test_trial_is_reproducible(self):
        first = run_noise_trial(17, 0.05)
        second = run_noise_trial(17, 0.05)
        self.assertEqual(
            first["error_only"].candidate.powers,
            second["error_only"].candidate.powers,
        )
        self.assertAlmostEqual(
            first["parsimony_regularized"].holdout_rmse,
            second["parsimony_regularized"].holdout_rmse,
            places=15,
        )

    def test_regularization_reduces_false_discovery_on_low_noise_fixture(self):
        result = run_stress_suite(seed_count=64, noise_levels=(0.01, 0.05))
        for row in result["noise_levels"]:
            plain = row["error_only"]
            regularized = row["parsimony_regularized"]
            self.assertGreater(
                regularized["exact_structure_recovery_rate"],
                plain["exact_structure_recovery_rate"],
            )
            self.assertLess(
                regularized["false_discovery_rate"],
                plain["false_discovery_rate"],
            )
            self.assertAlmostEqual(
                regularized["exact_structure_recovery_rate"]
                + regularized["false_discovery_rate"],
                1.0,
                places=12,
            )

    def test_result_remains_model_only(self):
        result = run_stress_suite(seed_count=8, noise_levels=(0.01,))
        self.assertEqual(result["evidence_level"], "MODEL_ONLY_SYNTHETIC")
        self.assertFalse(result["new_physical_law_claim"])
        self.assertIn("dimensionless", result["dimension_contract"])


if __name__ == "__main__":
    unittest.main()
