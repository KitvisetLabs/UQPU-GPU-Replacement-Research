import unittest

from uqpu.equation_discovery_benchmark import (
    compare_matched_heldout_errors,
    validate_grouped_splits,
)


class EquationDiscoveryBenchmarkTests(unittest.TestCase):
    def _statuses(self, case_ids, default="CHECKED_EQUIVALENCE"):
        return {case_id: default for case_id in case_ids}

    def _certificates(self, case_ids):
        return {case_id: (format(index + 1, "x") * 64)[:64] for index, case_id in enumerate(case_ids)}

    def _compare(self, baseline, candidate, statuses=None, certificates=None, **kwargs):
        case_ids = tuple(baseline)
        return compare_matched_heldout_errors(
            baseline,
            candidate,
            statuses if statuses is not None else self._statuses(case_ids),
            certificates if certificates is not None else self._certificates(case_ids),
            **kwargs,
        )

    def test_grouped_splits_are_sorted_and_disjoint(self):
        result = validate_grouped_splits(
            ["eqn-b", "eqn-a"], ["eqn-c"], ["eqn-d", "eqn-e"]
        )
        self.assertEqual(result["train"], ("eqn-a", "eqn-b"))
        self.assertEqual(result["validation"], ("eqn-c",))
        self.assertEqual(result["test"], ("eqn-d", "eqn-e"))

    def test_grouped_splits_reject_overlap(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            validate_grouped_splits(["system-1"], ["system-2"], ["system-1"])

    def test_grouped_splits_reject_duplicate_or_empty_ids(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            validate_grouped_splits(["a", "a"], ["b"], ["c"])
        with self.assertRaises(ValueError):
            validate_grouped_splits(["a"], [" "], ["c"])

    def test_matched_improvement_passes_metric_gate_only(self):
        result = self._compare(
            {"case-a": 1.0, "case-b": 2.0, "case-c": 4.0},
            {"case-a": 0.8, "case-b": 1.8, "case-c": 3.6},
        )
        self.assertTrue(result["metric_gate_passed"])
        self.assertAlmostEqual(result["mean_candidate_to_baseline_ratio"], 0.8666666667)
        self.assertEqual(result["evidence_class"], "MODEL_ONLY_METRIC_SUMMARY")
        self.assertIn("not proof", result["claim_boundary"])

    def test_large_per_case_regression_blocks_gate_even_if_mean_improves(self):
        result = self._compare(
            {"a": 1.0, "b": 1.0, "c": 100.0},
            {"a": 0.1, "b": 0.1, "c": 106.0},
        )
        self.assertFalse(result["metric_conditions_passed"])
        self.assertFalse(result["metric_gate_passed"])
        self.assertAlmostEqual(result["worst_relative_regression"], 0.06)

    def test_unverified_equivalence_blocks_gate(self):
        result = self._compare(
            {"a": 1.0, "b": 2.0, "c": 4.0},
            {"a": 0.5, "b": 1.0, "c": 2.0},
            statuses={"a": "CHECKED_EQUIVALENCE", "b": "UNVERIFIED", "c": "CHECKED_EQUIVALENCE"},
        )
        self.assertTrue(result["metric_conditions_passed"])
        self.assertFalse(result["equivalence_conditions_passed"])
        self.assertFalse(result["metric_gate_passed"])

    def test_no_mean_improvement_blocks_gate(self):
        result = self._compare(
            {"a": 1.0, "b": 2.0, "c": 4.0},
            {"a": 1.0, "b": 2.0, "c": 4.0},
        )
        self.assertFalse(result["metric_gate_passed"])

    def test_mismatched_cases_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "identical case IDs"):
            self._compare(
                {"a": 1.0, "b": 2.0, "c": 3.0},
                {"a": 0.5, "b": 1.0, "other": 1.5},
            )

    def test_bad_certificate_digest_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            self._compare(
                {"a": 1.0, "b": 2.0, "c": 3.0},
                {"a": 0.5, "b": 1.0, "c": 1.5},
                certificates={"a": "bad", "b": "b" * 64, "c": "c" * 64},
            )

    def test_invalid_error_values_and_zero_baseline_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "finite and >= 0"):
            self._compare(
                {"a": 1.0, "b": 2.0, "c": 3.0},
                {"a": float("nan"), "b": 1.0, "c": 1.5},
            )
        with self.assertRaisesRegex(ValueError, "must be > 0"):
            self._compare(
                {"a": 0.0, "b": 2.0, "c": 3.0},
                {"a": 0.0, "b": 1.0, "c": 1.5},
            )

    def test_invalid_threshold_and_too_few_cases_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "finite and >= 0"):
            self._compare(
                {"a": 1.0, "b": 2.0, "c": 3.0},
                {"a": 0.5, "b": 1.0, "c": 1.5},
                max_relative_regression=float("nan"),
            )
        with self.assertRaisesRegex(ValueError, "at least"):
            compare_matched_heldout_errors(
                {"a": 1.0, "b": 2.0},
                {"a": 0.5, "b": 1.0},
                {"a": "CHECKED_EQUIVALENCE", "b": "CHECKED_EQUIVALENCE"},
                {"a": "a" * 64, "b": "b" * 64},
            )


if __name__ == "__main__":
    unittest.main()
