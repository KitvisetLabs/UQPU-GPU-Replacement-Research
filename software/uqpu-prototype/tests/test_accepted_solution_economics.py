import unittest

from uqpu.accepted_solution_economics import (
    AcceptedSolutionCost,
    expected_independent_shots_to_success,
    shots_for_success_confidence,
)


class AcceptedSolutionEconomicsTests(unittest.TestCase):
    def test_expected_shots(self):
        self.assertEqual(expected_independent_shots_to_success(1.0), 1.0)
        self.assertAlmostEqual(expected_independent_shots_to_success(0.25), 4.0)

    def test_confidence_budget(self):
        self.assertEqual(shots_for_success_confidence(1.0, 0.999), 1)
        self.assertEqual(shots_for_success_confidence(0.5, 0.75), 2)
        self.assertGreaterEqual(shots_for_success_confidence(0.1, 0.999), 1)

    def test_cost_includes_fixed_submission_overhead(self):
        c = AcceptedSolutionCost(
            success_probability_per_shot=0.5,
            variable_cost_per_shot=2.0,
            fixed_cost_per_submission=10.0,
            shots_per_submission=2,
        )
        self.assertAlmostEqual(c.submission_success_probability, 0.75)
        self.assertAlmostEqual(c.submission_cost, 14.0)
        self.assertAlmostEqual(c.expected_cost_per_accepted_solution, 14.0 / 0.75)

    def test_invalid_probabilities_rejected(self):
        for p in (0, -0.1, 1.1, float("nan")):
            with self.assertRaises(ValueError):
                expected_independent_shots_to_success(p)


if __name__ == "__main__":
    unittest.main()
