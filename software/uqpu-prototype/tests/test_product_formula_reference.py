import math
import unittest

from uqpu.product_formula_reference import (
    evolve_xz_lie_trotter,
    frobenius_distance_2x2,
)
from uqpu.small_hamiltonian_reference import (
    evolve_2x2_hermitian,
    max_unitarity_residual,
)


class ProductFormulaReferenceTests(unittest.TestCase):
    def test_first_order_trotter_converges_to_exact_reference(self):
        alpha, beta, time = 0.7, 0.4, 0.8
        exact = evolve_2x2_hermitian(alpha, -alpha, beta, time)
        errors = [
            frobenius_distance_2x2(
                evolve_xz_lie_trotter(alpha, beta, time, steps), exact
            )
            for steps in (1, 2, 4, 8, 16, 32)
        ]
        self.assertTrue(all(left > right for left, right in zip(errors, errors[1:])))
        self.assertLess(errors[-1], 0.01)
        self.assertLess(
            max_unitarity_residual(evolve_xz_lie_trotter(alpha, beta, time, 32)),
            2e-14,
        )

    def test_commuting_single_term_cases_match_exact_solution(self):
        for alpha, beta, time, steps in (
            (0.0, 0.4, 1.3, 7),
            (0.7, 0.0, -0.8, 5),
            (0.0, 0.0, 2.0, 1),
        ):
            exact = evolve_2x2_hermitian(alpha, -alpha, beta, time)
            approximate = evolve_xz_lie_trotter(alpha, beta, time, steps)
            self.assertLess(frobenius_distance_2x2(approximate, exact), 2e-14)

    def test_invalid_steps_and_nonfinite_values_fail_closed(self):
        for steps in (0, -1, True, 1.5, "4"):
            with self.subTest(steps=steps):
                with self.assertRaises(ValueError):
                    evolve_xz_lie_trotter(0.7, 0.4, 0.8, steps)
        for args in (
            (float("inf"), 0.4, 0.8, 2),
            (0.7, float("nan"), 0.8, 2),
            (0.7, 0.4, float("inf"), 2),
            (1e308, 0.4, 1e308, 1),
        ):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    evolve_xz_lie_trotter(*args)

    def test_frobenius_distance_validates_matrix_shape_and_entries(self):
        identity = ((1 + 0j, 0j), (0j, 1 + 0j))
        self.assertEqual(frobenius_distance_2x2(identity, identity), 0.0)
        with self.assertRaises(ValueError):
            frobenius_distance_2x2(((1, 0), (0, 1, 2)), identity)
        with self.assertRaises(ValueError):
            frobenius_distance_2x2(((1, 0), (0, float("inf"))), identity)


if __name__ == "__main__":
    unittest.main()
