import unittest

from uqpu.open_quantum_invariant_toy import evaluate_pure_dephasing_candidate


I = (1, 0, 0, 0)
X = (0, 1, 0, 0)
Y = (0, 0, 1, 0)
Z = (0, 0, 0, 1)


class OpenQuantumInvariantToyTests(unittest.TestCase):
    def test_invariant_and_algebra_closed_candidate_passes_toy_checks(self):
        result = evaluate_pure_dephasing_candidate((I, Z))
        self.assertTrue(result["invariant_under_declared_generator"])
        self.assertTrue(result["closed_under_operator_product"])
        self.assertTrue(result["passes_exact_toy_checks"])
        self.assertEqual(result["evidence_class"], "MODEL_ONLY")
        self.assertIn("not an experimental result", result["claim_boundary"])

    def test_invariant_subspace_that_is_not_an_algebra_is_rejected(self):
        result = evaluate_pure_dephasing_candidate((I, X, Y))
        self.assertTrue(result["invariant_under_declared_generator"])
        self.assertFalse(result["closed_under_operator_product"])
        self.assertFalse(result["passes_exact_toy_checks"])

    def test_noninvariant_candidate_is_rejected_even_when_closed(self):
        result = evaluate_pure_dephasing_candidate((I, (0, 1, 0, 1)))
        self.assertFalse(result["invariant_under_declared_generator"])
        self.assertTrue(result["closed_under_operator_product"])
        self.assertFalse(result["passes_exact_toy_checks"])

    def test_zero_dephasing_rate_preserves_full_operator_algebra(self):
        result = evaluate_pure_dephasing_candidate((I, X, Y, Z), gamma=0)
        self.assertTrue(result["invariant_under_declared_generator"])
        self.assertTrue(result["closed_under_operator_product"])

    def test_dependent_basis_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_pure_dephasing_candidate((I, I))

    def test_nonfinite_coefficient_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_pure_dephasing_candidate(((1, float("nan"), 0, 0),))

    def test_invalid_gamma_is_rejected(self):
        for gamma in (-1, float("inf"), True):
            with self.subTest(gamma=gamma), self.assertRaises(ValueError):
                evaluate_pure_dephasing_candidate((I, Z), gamma=gamma)

    def test_invalid_tolerance_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_pure_dephasing_candidate((I, Z), tolerance=0)

    def test_wrong_vector_dimension_is_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_pure_dephasing_candidate(((1, 0, 0),))


if __name__ == "__main__":
    unittest.main()
