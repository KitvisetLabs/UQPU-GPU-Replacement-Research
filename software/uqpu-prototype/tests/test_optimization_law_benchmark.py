import math
import unittest

from uqpu.optimization_law_benchmark import evaluate_objective_candidate


class OptimizationLawBenchmarkTests(unittest.TestCase):
    def setUp(self):
        self.decisions = (-2, -1, 0, 1, 2, 3, 4)
        self.reference = lambda context, decision: (decision - context) ** 2

    def test_positive_rescaling_preserves_order_and_optima(self):
        candidate = lambda c, x: 5 * (x - c) ** 2 + c ** 2 + 3
        result = evaluate_objective_candidate(
            self.reference, candidate, [0, 1], [2, 3], self.decisions
        )
        self.assertEqual(result.train.optimum_set_match_rate, 1.0)
        self.assertEqual(result.heldout.optimum_set_match_rate, 1.0)
        self.assertEqual(result.heldout.ordering.agreement, 1.0)

    def test_training_only_fit_fails_on_heldout_contexts(self):
        candidate = lambda c, x: (x - c) ** 2 + c ** 2 * x
        result = evaluate_objective_candidate(
            self.reference, candidate, [0], [1, 2], self.decisions
        )
        self.assertEqual(result.train.optimum_set_match_rate, 1.0)
        self.assertEqual(result.heldout.optimum_set_match_rate, 0.0)
        self.assertGreater(
            result.heldout.ordering.discordant
            + result.heldout.ordering.tie_disagreements,
            0,
        )

    def test_constant_candidate_is_not_equivalent(self):
        result = evaluate_objective_candidate(
            self.reference, lambda c, x: 0.0, [0], [1], self.decisions
        )
        self.assertEqual(result.heldout.optimum_set_match_rate, 0.0)
        self.assertEqual(result.heldout.ordering.agreement, 0.0)

    def test_invalid_direction_and_empty_split_are_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_objective_candidate(
                self.reference, self.reference, [0], [1], self.decisions,
                direction="sideways",
            )
        with self.assertRaises(ValueError):
            evaluate_objective_candidate(
                self.reference, self.reference, [], [1], self.decisions
            )

    def test_nonfinite_objective_output_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_objective_candidate(
                self.reference, lambda c, x: math.nan, [0], [1], self.decisions
            )

    def test_maximization_direction_is_supported(self):
        reference = lambda c, x: -(x - c) ** 2
        candidate = lambda c, x: 4 * (-(x - c) ** 2) + c
        result = evaluate_objective_candidate(
            reference, candidate, [0], [2], self.decisions, direction="max"
        )
        self.assertEqual(result.heldout.optimum_set_match_rate, 1.0)
        self.assertEqual(result.heldout.ordering.agreement, 1.0)

    def test_grid_fingerprints_are_stable_and_sensitive_to_contract(self):
        first = evaluate_objective_candidate(
            self.reference, self.reference, [0, 1], [2, 3], self.decisions
        )
        repeat = evaluate_objective_candidate(
            self.reference, self.reference, [0, 1], [2, 3], self.decisions
        )
        changed = evaluate_objective_candidate(
            self.reference, self.reference, [0, 1], [2, 3], self.decisions,
            tolerance=1e-8,
        )
        self.assertEqual(first.grid_contract_sha256, repeat.grid_contract_sha256)
        self.assertNotEqual(first.grid_contract_sha256, changed.grid_contract_sha256)
        for fingerprint in (
            first.train_contexts_sha256,
            first.heldout_contexts_sha256,
            first.decision_grid_sha256,
            first.grid_contract_sha256,
        ):
            self.assertEqual(len(fingerprint), 64)
        self.assertNotEqual(
            first.train_contexts_sha256, first.heldout_contexts_sha256
        )

    def test_overlapping_or_duplicate_contexts_and_decisions_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "disjoint"):
            evaluate_objective_candidate(
                self.reference, self.reference, [0, 1], [1, 2], self.decisions
            )
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate_objective_candidate(
                self.reference, self.reference, [0, 0], [1], self.decisions
            )
        with self.assertRaisesRegex(ValueError, "duplicate"):
            evaluate_objective_candidate(
                self.reference, self.reference, [0], [1], (-2, -2, 0)
            )


if __name__ == "__main__":
    unittest.main()
