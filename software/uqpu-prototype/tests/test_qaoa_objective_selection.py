import math
import unittest

from uqpu.qaoa_objective_selection import (
    compare_p1_grid_objectives,
    cvar_minimization,
    expected_energy,
)
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut


class QaoaObjectiveSelectionTests(unittest.TestCase):
    def test_cvar_lower_tail(self):
        probabilities = (0.25, 0.75)
        energies = (-2.0, 2.0)
        self.assertEqual(cvar_minimization(probabilities, energies, 0.25), -2.0)
        self.assertEqual(cvar_minimization(probabilities, energies, 0.5), 0.0)

    def test_alpha_one_equals_mean(self):
        probabilities = (0.2, 0.3, 0.5)
        energies = (-3.0, 1.0, 4.0)
        self.assertAlmostEqual(
            cvar_minimization(probabilities, energies, 1.0),
            expected_energy(probabilities, energies),
            places=12,
        )

    def test_shared_budget_and_reproducibility(self):
        instance = seeded_erdos_renyi_maxcut(6, 0.5, 42)
        a = compare_p1_grid_objectives(instance, gamma_steps=8, beta_steps=8)
        b = compare_p1_grid_objectives(instance, gamma_steps=8, beta_steps=8)
        self.assertEqual(a, b)
        self.assertEqual(a.evaluations, 64)
        self.assertEqual(len(a.selections), 4)
        self.assertTrue(all(math.isfinite(x.score) for x in a.selections))
        self.assertTrue(all(0.0 <= x.optimum_probability <= 1.0 for x in a.selections))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            cvar_minimization((0.4, 0.4), (0.0, 1.0), 0.5)
        with self.assertRaises(ValueError):
            cvar_minimization((0.5, 0.5), (0.0, 1.0), 0.0)
        with self.assertRaises(ValueError):
            compare_p1_grid_objectives(
                seeded_erdos_renyi_maxcut(4, 0.5, 1), alphas=(0.5, 0.5)
            )


if __name__ == "__main__":
    unittest.main()
