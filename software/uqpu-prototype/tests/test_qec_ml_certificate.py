import unittest

from uqpu.qec_ml_certificate import (
    AggregateCertificate,
    CostInterval,
    classify_cost_intervals,
    exhaustive_class_minima,
    validate_certificate_against_exact,
)


class QECMLCertificateTests(unittest.TestCase):
    def test_exhaustive_oracle_and_certified_success(self):
        exact_true, exact_competing = exhaustive_class_minima(
            [
                ("TRUE", 1),
                ("TRUE", 4),
                ("COMPETING", 3),
                ("COMPETING", 5),
            ]
        )
        self.assertEqual((exact_true, exact_competing), (1.0, 3.0))
        self.assertEqual(
            validate_certificate_against_exact(
                CostInterval(1, 2), CostInterval(3, 4),
                exact_true, exact_competing
            ),
            "SUCCESS",
        )

    def test_failure_and_tie_remain_distinct(self):
        self.assertEqual(
            classify_cost_intervals(CostInterval(4, 5), CostInterval(1, 2)),
            "FAILURE",
        )
        self.assertEqual(
            classify_cost_intervals(CostInterval(2, 2), CostInterval(2, 2)),
            "UNDECIDED",
        )

    def test_loose_valid_bounds_remain_undecided(self):
        self.assertEqual(
            validate_certificate_against_exact(
                CostInterval(1, 4), CostInterval(2, 5), 2, 3
            ),
            "UNDECIDED",
        )

    def test_interval_must_contain_exact_minimum(self):
        with self.assertRaises(ValueError):
            validate_certificate_against_exact(
                CostInterval(1, 1), CostInterval(2, 3), 2, 2
            )

    def test_malformed_candidates_fail_closed(self):
        cases = (
            [],
            [("TRUE", 1)],
            [("TRUE", -1), ("COMPETING", 2)],
            [("OTHER", 1), ("COMPETING", 2)],
            [("TRUE", True), ("COMPETING", 2)],
        )
        for candidates in cases:
            with self.subTest(candidates=candidates):
                with self.assertRaises(ValueError):
                    exhaustive_class_minima(candidates)

    def test_aggregate_interval_width_equals_undecided_fraction(self):
        aggregate = AggregateCertificate(success=5, failure=2, undecided=3)
        low, high = aggregate.logical_error_interval
        self.assertEqual((low, high), (0.2, 0.5))
        self.assertAlmostEqual(high - low, 3 / 10)

    def test_aggregate_counts_are_validated(self):
        with self.assertRaises(ValueError):
            AggregateCertificate(0, 0, 0).logical_error_interval
        with self.assertRaises(ValueError):
            AggregateCertificate(True, 0, 1).logical_error_interval


if __name__ == "__main__":
    unittest.main()
