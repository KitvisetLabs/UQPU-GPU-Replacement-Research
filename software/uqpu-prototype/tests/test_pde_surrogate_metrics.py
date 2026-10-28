import unittest

from uqpu.pde_surrogate_metrics import score_conservative_bounded_trajectory


class PdeSurrogateMetricsTests(unittest.TestCase):
    def test_exact_conservation_and_bounds_pass(self):
        result = score_conservative_bounded_trajectory(
            [0.2, 0.3, 0.5],
            [[0.2, 0.5, 0.3], [0.4, 0.4, 0.2]],
            lower_bound=0.0,
            upper_bound=1.0,
            normalized_conservation_tolerance=1e-12,
        )
        self.assertEqual(result.time_step_count, 2)
        self.assertEqual(result.cell_count, 3)
        self.assertAlmostEqual(result.initial_conserved_total, 1.0)
        self.assertEqual(result.predicted_conserved_totals, (1.0, 1.0))
        self.assertTrue(result.conservation_pass)
        self.assertTrue(result.bounds_pass)
        self.assertEqual(result.bound_violation_count, 0)

    def test_conservation_drift_is_reported_and_can_fail(self):
        result = score_conservative_bounded_trajectory(
            [0.2, 0.3, 0.5], [[0.2, 0.3, 0.6]],
            conservation_scale=1.0,
            normalized_conservation_tolerance=0.01,
        )
        self.assertAlmostEqual(result.max_absolute_conservation_drift, 0.1)
        self.assertAlmostEqual(result.max_normalized_conservation_drift, 0.1)
        self.assertFalse(result.conservation_pass)
        self.assertIsNone(result.bounds_pass)

    def test_cell_weights_change_the_discrete_integral(self):
        result = score_conservative_bounded_trajectory(
            [1.0, 2.0], [[2.0, 1.0]], cell_weights=[0.5, 0.5],
            normalized_conservation_tolerance=1e-12,
        )
        self.assertAlmostEqual(result.initial_conserved_total, 1.5)
        self.assertTrue(result.conservation_pass)

    def test_lower_and_upper_bound_violations_are_counted(self):
        result = score_conservative_bounded_trajectory(
            [0.5, 0.5], [[-0.1, 1.2]], lower_bound=0.0, upper_bound=1.0,
            conservation_scale=1.0,
        )
        self.assertEqual(result.bound_violation_count, 2)
        self.assertEqual(result.bound_violation_rate, 1.0)
        self.assertAlmostEqual(result.max_bound_violation, 0.2)
        self.assertFalse(result.bounds_pass)

    def test_bound_tolerance_is_applied_in_field_units(self):
        result = score_conservative_bounded_trajectory(
            [0.5, 0.5], [[-0.01, 1.01]], lower_bound=0.0, upper_bound=1.0,
            conservation_scale=1.0, bound_tolerance=0.02,
        )
        self.assertEqual(result.bound_violation_count, 0)
        self.assertTrue(result.bounds_pass)
        self.assertAlmostEqual(result.max_bound_violation, 0.01)

    def test_zero_initial_field_requires_explicit_scale(self):
        with self.assertRaisesRegex(ValueError, "zero-magnitude"):
            score_conservative_bounded_trajectory([0.0, 0.0], [[0.0, 0.0]])
        result = score_conservative_bounded_trajectory(
            [0.0, 0.0], [[0.0, 0.0]], conservation_scale=1.0
        )
        self.assertTrue(result.conservation_pass)

    def test_bad_shapes_and_empty_trajectory_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "nonempty"):
            score_conservative_bounded_trajectory([], [[1.0]])
        with self.assertRaisesRegex(ValueError, "nonempty"):
            score_conservative_bounded_trajectory([1.0], [])
        with self.assertRaisesRegex(ValueError, "match initial_field"):
            score_conservative_bounded_trajectory([1.0, 2.0], [[1.0]])
        with self.assertRaisesRegex(ValueError, "cell_weights"):
            score_conservative_bounded_trajectory([1.0, 2.0], [[1.0, 2.0]], cell_weights=[1.0])

    def test_nonfinite_boolean_and_invalid_weights_fail_closed(self):
        bad_calls = [
            lambda: score_conservative_bounded_trajectory([True], [[1.0]], conservation_scale=1.0),
            lambda: score_conservative_bounded_trajectory([1.0], [[float("nan")]]),
            lambda: score_conservative_bounded_trajectory([1.0], [[1.0]], cell_weights=[0.0]),
            lambda: score_conservative_bounded_trajectory([1.0], [[1.0]], lower_bound=2.0, upper_bound=1.0),
            lambda: score_conservative_bounded_trajectory([1.0], [[1.0]], normalized_conservation_tolerance=float("inf")),
            lambda: score_conservative_bounded_trajectory([1.0], [[1.0]], conservation_scale=0.0),
            lambda: score_conservative_bounded_trajectory([0.0], [[-1e308]], lower_bound=1e308, conservation_scale=1.0),
        ]
        for call in bad_calls:
            with self.subTest(call=call), self.assertRaises(ValueError):
                call()

    def test_bound_flags_are_not_claimed_when_no_bounds_are_supplied(self):
        result = score_conservative_bounded_trajectory([1.0], [[1.0]])
        self.assertFalse(result.bounds_applicable)
        self.assertIsNone(result.bounds_pass)


if __name__ == "__main__":
    unittest.main()
