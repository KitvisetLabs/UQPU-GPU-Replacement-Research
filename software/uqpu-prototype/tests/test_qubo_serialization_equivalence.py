import itertools
import unittest

from uqpu.optimization_baseline import QuboInstance
from uqpu.qubo_serialization import to_dwave_qubo, to_portable_qubo


class QuboSerializationEquivalenceTests(unittest.TestCase):
    def _instance(self):
        # Includes reversed pair orientation, a diagonal quadratic term and an offset.
        return QuboInstance(
            linear={0: -1.5, 1: 0.25},
            quadratic={(0, 1): 2.0, (1, 0): -0.5, (1, 1): 0.75, (0, 2): -1.25},
            constant=3.0,
        )

    def test_portable_lowering_preserves_every_binary_assignment(self):
        instance = self._instance()
        payload = to_portable_qubo(instance).payload
        restored = QuboInstance(
            linear={int(key): value for key, value in payload["linear"].items()},
            quadratic={(i, j): value for i, j, value in payload["quadratic"]},
            constant=payload["constant"],
        )
        for values in itertools.product((0, 1), repeat=len(instance.variables)):
            bits = dict(zip(instance.variables, values))
            self.assertAlmostEqual(instance.energy(bits), restored.energy(bits), places=12)

    def test_dwave_lowering_preserves_every_binary_assignment_including_offset(self):
        instance = self._instance()
        payload = to_dwave_qubo(instance).payload
        q = payload["Q"]
        for values in itertools.product((0, 1), repeat=len(instance.variables)):
            bits = dict(zip(instance.variables, values))
            lowered_energy = payload["offset"] + sum(
                weight * bits[i] * bits[j] for (i, j), weight in q.items()
            )
            self.assertAlmostEqual(instance.energy(bits), lowered_energy, places=12)

    def test_reversed_pair_terms_are_summed_in_dwave_upper_triangle(self):
        payload = to_dwave_qubo(self._instance()).payload
        self.assertAlmostEqual(payload["Q"][(0, 1)], 1.5)
        self.assertNotIn((1, 0), payload["Q"])

    def test_diagonal_quadratic_term_is_combined_with_linear_term(self):
        payload = to_dwave_qubo(self._instance()).payload
        self.assertAlmostEqual(payload["Q"][(1, 1)], 1.0)

    def test_nonfinite_constant_is_rejected_by_both_serializers(self):
        instance = QuboInstance(linear={0: 1.0}, quadratic={}, constant=float("nan"))
        for serializer in (to_dwave_qubo, to_portable_qubo):
            with self.subTest(serializer=serializer.__name__):
                with self.assertRaises(ValueError):
                    serializer(instance)

    def test_infinite_linear_coefficient_is_rejected(self):
        instance = QuboInstance(linear={0: float("inf")}, quadratic={})
        with self.assertRaises(ValueError):
            to_portable_qubo(instance)

    def test_nan_quadratic_coefficient_is_rejected(self):
        instance = QuboInstance(linear={}, quadratic={(0, 1): float("nan")})
        with self.assertRaises(ValueError):
            to_dwave_qubo(instance)

    def test_non_numeric_coefficient_is_rejected(self):
        instance = QuboInstance(linear={0: "not-a-number"}, quadratic={})
        with self.assertRaises(ValueError):
            to_portable_qubo(instance)


if __name__ == "__main__":
    unittest.main()
