import unittest

from uqpu.predictive_interval_metrics import score_prediction_intervals


class PredictiveIntervalMetricsTests(unittest.TestCase):
    def test_known_function_positive_control(self):
        xs = range(5)
        observations = [2 * x + 1 for x in xs]
        lower = [value - 0.5 for value in observations]
        upper = [value + 0.5 for value in observations]

        result = score_prediction_intervals(observations, lower, upper, 0.95)

        self.assertEqual(result.sample_count, 5)
        self.assertEqual(result.empirical_coverage, 1.0)
        self.assertAlmostEqual(result.coverage_error, 0.05)
        self.assertAlmostEqual(result.mean_width, 1.0)
        self.assertAlmostEqual(result.mean_interval_score, 1.0)

    def test_null_no_signal_fixture_scores_coverage_and_outlier_penalty(self):
        observations = [0.1, -0.2, 0.3, -0.4, 2.0]
        lower = [-1.0] * len(observations)
        upper = [1.0] * len(observations)

        result = score_prediction_intervals(observations, lower, upper, 0.8)

        self.assertEqual(result.empirical_coverage, 0.8)
        self.assertAlmostEqual(result.coverage_error, 0.0)
        self.assertAlmostEqual(result.mean_width, 2.0)
        self.assertAlmostEqual(result.mean_interval_score, 4.0)

    def test_uninformatively_wide_intervals_are_penalized(self):
        observations = [0.0, 1.0]
        narrow = score_prediction_intervals(
            observations, [-0.5, 0.5], [0.5, 1.5], 0.9
        )
        wide = score_prediction_intervals(
            observations, [-10.0, -9.0], [10.0, 11.0], 0.9
        )

        self.assertEqual(narrow.empirical_coverage, wide.empirical_coverage)
        self.assertAlmostEqual(narrow.mean_interval_score, 1.0)
        self.assertAlmostEqual(wide.mean_interval_score, 20.0)
        self.assertGreater(wide.mean_interval_score, narrow.mean_interval_score)

    def test_outside_interval_penalty_uses_nominal_miscoverage(self):
        result = score_prediction_intervals([2.0], [-1.0], [1.0], 0.8)
        self.assertAlmostEqual(result.mean_interval_score, 12.0)

    def test_invalid_shapes_and_empty_sequences_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "nonempty"):
            score_prediction_intervals([], [], [], 0.95)
        with self.assertRaisesRegex(ValueError, "equal lengths"):
            score_prediction_intervals([1.0, 2.0], [0.0], [2.0, 3.0], 0.95)

    def test_invalid_coverage_level_fails_closed(self):
        for level in (0.0, 1.0, float("nan"), float("inf"), True, "0.95"):
            with self.subTest(level=level), self.assertRaises(ValueError):
                score_prediction_intervals([0.0], [-1.0], [1.0], level)

    def test_nonfinite_values_and_inverted_bounds_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "finite number"):
            score_prediction_intervals([float("nan")], [-1.0], [1.0], 0.95)
        with self.assertRaisesRegex(ValueError, "<="):
            score_prediction_intervals([0.0], [1.0], [-1.0], 0.95)
        with self.assertRaisesRegex(ValueError, "finite"):
            score_prediction_intervals([0.0], [-1e308], [1e308], 0.95)


if __name__ == "__main__":
    unittest.main()
