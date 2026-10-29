import unittest

from uqpu.qubo_reference import exact_qubo_reference


class ExactQuboReferenceTests(unittest.TestCase):
    def test_unique_minimum_and_full_enumeration(self):
        result = exact_qubo_reference(
            2, [(0, 0, -2), (1, 1, -2), (0, 1, 1)]
        )
        self.assertEqual(result["optimum_energy"], "-3")
        self.assertEqual(result["optimal_bitstrings"], ["11"])
        self.assertEqual(result["evaluated_assignments"], 4)
        self.assertEqual(result["reference_kind"], "EXHAUSTIVE_BINARY_ENUMERATION")

    def test_ties_are_preserved_in_stable_order(self):
        result = exact_qubo_reference(
            2, [(0, 0, -1), (1, 1, -1), (0, 1, 3)]
        )
        self.assertEqual(result["optimum_energy"], "-1")
        self.assertEqual(result["optimal_bitstrings"], ["01", "10"])

    def test_decimal_inputs_are_summed_as_declared(self):
        result = exact_qubo_reference(
            2, [(0, 0, "-0.1"), (1, 1, "-0.2"), (0, 1, "-0.3")]
        )
        self.assertEqual(result["optimum_energy"], "-0.6")

    def test_term_order_does_not_change_problem_or_certificate_hash(self):
        left = exact_qubo_reference(2, [(0, 0, -1), (1, 1, -1)])
        right = exact_qubo_reference(2, [(1, 1, -1), (0, 0, -1)])
        self.assertEqual(left["problem_sha256"], right["problem_sha256"])
        self.assertEqual(left["certificate_sha256"], right["certificate_sha256"])

    def test_coefficient_change_changes_problem_hash(self):
        left = exact_qubo_reference(2, [(0, 0, -1)])
        right = exact_qubo_reference(2, [(0, 0, "-1.01")])
        self.assertNotEqual(left["problem_sha256"], right["problem_sha256"])

    def test_empty_objective_enumerates_all_assignments_as_optima(self):
        result = exact_qubo_reference(3, [])
        self.assertEqual(result["optimum_energy"], "0")
        self.assertEqual(result["optimal_bitstrings"], [
            "000", "001", "010", "011", "100", "101", "110", "111"
        ])

    def test_rejects_duplicate_and_noncanonical_terms(self):
        with self.assertRaisesRegex(ValueError, "duplicate"):
            exact_qubo_reference(2, [(0, 0, 1), (0, 0, 2)])
        with self.assertRaisesRegex(ValueError, "upper-triangle"):
            exact_qubo_reference(2, [(1, 0, 1)])

    def test_rejects_invalid_coefficients_and_indices(self):
        for coefficient in ("NaN", "Infinity", True):
            with self.subTest(coefficient=coefficient):
                with self.assertRaises(ValueError):
                    exact_qubo_reference(2, [(0, 0, coefficient)])
        with self.assertRaisesRegex(ValueError, "out of range"):
            exact_qubo_reference(2, [(2, 2, 1)])

    def test_hard_limit_prevents_accidental_exponential_blowup(self):
        with self.assertRaisesRegex(ValueError, "limited to 20"):
            exact_qubo_reference(21, [])


if __name__ == "__main__":
    unittest.main()
