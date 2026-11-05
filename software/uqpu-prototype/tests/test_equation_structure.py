import unittest

from uqpu.equation_structure import (
    canonical_expression_tree,
    canonical_structure_distance,
    normalized_structure_distance,
)


class EquationStructureTests(unittest.TestCase):
    def test_commutative_addition_has_zero_distance(self):
        self.assertEqual(canonical_structure_distance("x + y", "y + x"), 0)

    def test_associative_addition_is_flattened(self):
        self.assertEqual(
            canonical_structure_distance("x + (y + z)", "(x + y) + z"), 0
        )

    def test_commutative_multiplication_is_canonicalized(self):
        self.assertEqual(
            canonical_structure_distance("a * (b * c)", "c * a * b"), 0
        )

    def test_constants_are_abstracted_by_default(self):
        self.assertEqual(
            canonical_structure_distance("2*x + 3", "5*x + 7"), 0
        )

    def test_constant_values_can_be_preserved(self):
        self.assertGreater(
            canonical_structure_distance(
                "x**2", "x**3", abstract_numeric_constants=False
            ),
            0,
        )

    def test_different_operator_structure_has_positive_distance(self):
        self.assertGreater(canonical_structure_distance("x * y", "x + y"), 0)
        self.assertGreater(
            canonical_structure_distance("x**2", "x**2 + 0.001*x**3"), 0
        )

    def test_supported_math_function_and_unsafe_syntax_policy(self):
        self.assertEqual(canonical_structure_distance("sin(x)", "sin(x)"), 0)
        for expression in ("unknown(x)", "x.__class__", "x[0]", "lambda x: x"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    canonical_expression_tree(expression)

    def test_invalid_constants_and_empty_expressions_fail_closed(self):
        for expression in ("", "True", "1e309", "1j", "x // 2"):
            with self.subTest(expression=expression):
                with self.assertRaises(ValueError):
                    canonical_expression_tree(expression)

    def test_normalized_distance_is_bounded_and_identical_trees_are_zero(self):
        self.assertEqual(normalized_structure_distance("x**2", "x**2"), 0.0)
        distance = normalized_structure_distance("x**2", "x**2 + 0.001*x**3")
        self.assertGreater(distance, 0.0)
        self.assertLessEqual(distance, 1.0)


if __name__ == "__main__":
    unittest.main()
