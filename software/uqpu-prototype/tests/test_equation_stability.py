import math
import unittest
from uqpu.equation_stability import normalized_perturbation_amplification


class EquationStabilityTests(unittest.TestCase):
    def test_dimensionless_normalized_amplification(self):
        result = normalized_perturbation_amplification(
            (1.0, 2.0), (1.1, 2.0), (2.0, 4.0), (2.2, 4.0),
            (1.0, 2.0), (2.0, 4.0))
        self.assertAlmostEqual(result, 1.0)

    def test_unchanged_input_and_output_returns_zero(self):
        self.assertEqual(normalized_perturbation_amplification(
            (1.0,), (1.0,), (3.0,), (3.0,), (1.0,), (1.0,)), 0.0)

    def test_same_input_with_different_output_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "zero input perturbation"):
            normalized_perturbation_amplification(
                (1.0,), (1.0,), (3.0,), (3.1,), (1.0,), (1.0,))

    def test_non_finite_values_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "finite"):
            normalized_perturbation_amplification(
                (1.0,), (math.inf,), (3.0,), (3.1,), (1.0,), (1.0,))
        with self.assertRaisesRegex(ValueError, "finite"):
            normalized_perturbation_amplification(
                (1.0,), (1.1,), (3.0,), (math.nan,), (1.0,), (1.0,))

    def test_boolean_and_non_numeric_values_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "not boolean"):
            normalized_perturbation_amplification(
                (True,), (1.1,), (3.0,), (3.1,), (1.0,), (1.0,))
        with self.assertRaisesRegex(ValueError, "numeric"):
            normalized_perturbation_amplification(
                ("one",), (1.1,), (3.0,), (3.1,), (1.0,), (1.0,))

    def test_shape_and_non_positive_scales_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "equal lengths"):
            normalized_perturbation_amplification(
                (1.0, 2.0), (1.1,), (3.0,), (3.1,), (1.0, 1.0), (1.0,))
        with self.assertRaisesRegex(ValueError, "strictly positive"):
            normalized_perturbation_amplification(
                (1.0,), (1.1,), (3.0,), (3.1,), (0.0,), (1.0,))


if __name__ == "__main__":
    unittest.main()
