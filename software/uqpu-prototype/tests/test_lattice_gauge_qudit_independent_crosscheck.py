"""Tests for FND-007B2 independent lattice-QED operator cross-check.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: independent implementation cross-check tests and numerical audit.
"""

import math
import unittest

from uqpu.lattice_gauge_qudit_independent_crosscheck import (
    PROJECTED_PLAQUETTE_OPERATOR,
    ZERO_MAGNETIZATION_FULL_INDICES,
    classification,
    eigenpair_residual,
    independent_ground_state,
    operator_expectation,
    projected_hamiltonian,
    symmetric_jacobi_eigendecomposition,
)
from uqpu.lattice_gauge_qudit_reproduction import (
    ground_state,
    plaquette_expectation,
    single_plaquette_hamiltonian,
)


COUPLINGS = (0.01, 0.1, 1.0, 10.0, 100.0)


def _max_abs_matrix_difference(left, right):
    return max(
        abs(left[row][column] - right[row][column])
        for row in range(len(left))
        for column in range(len(left[row]))
    )


class LatticeGaugeQuditIndependentCrosscheckTests(unittest.TestCase):
    def test_full_space_projection_has_expected_dimension(self):
        self.assertEqual(len(ZERO_MAGNETIZATION_FULL_INDICES), 18)
        self.assertEqual(len(set(ZERO_MAGNETIZATION_FULL_INDICES)), 18)

    def test_independent_tensor_product_builder_matches_batch042_state_builder(self):
        for inverse_g_squared in COUPLINGS:
            with self.subTest(inverse_g_squared=inverse_g_squared):
                independent = projected_hamiltonian(inverse_g_squared)
                batch042 = single_plaquette_hamiltonian(inverse_g_squared)
                self.assertLess(_max_abs_matrix_difference(independent, batch042), 1e-12)

    def test_independent_jacobi_ground_states_have_small_residuals(self):
        for inverse_g_squared in COUPLINGS:
            with self.subTest(inverse_g_squared=inverse_g_squared):
                result = independent_ground_state(inverse_g_squared)
                self.assertLess(result.residual_norm, 2e-12)
                self.assertLess(result.jacobi_rotations, 1_000)

    def test_batch042_power_iteration_energy_and_observable_are_crosschecked(self):
        maximum_energy_difference = 0.0
        maximum_plaquette_difference = 0.0
        maximum_batch042_residual = 0.0

        for inverse_g_squared in COUPLINGS:
            hamiltonian = single_plaquette_hamiltonian(inverse_g_squared)
            batch042_energy, batch042_state, _ = ground_state(hamiltonian)
            independent = independent_ground_state(inverse_g_squared)

            energy_difference = abs(batch042_energy - independent.energy)
            plaquette_difference = abs(
                plaquette_expectation(batch042_state)
                - independent.plaquette_expectation
            )
            batch042_residual = eigenpair_residual(
                hamiltonian,
                batch042_energy,
                batch042_state,
            )

            maximum_energy_difference = max(maximum_energy_difference, energy_difference)
            maximum_plaquette_difference = max(
                maximum_plaquette_difference,
                plaquette_difference,
            )
            maximum_batch042_residual = max(maximum_batch042_residual, batch042_residual)

        self.assertLess(maximum_energy_difference, 1e-12)
        self.assertLess(maximum_plaquette_difference, 1e-7)
        # Energy-only convergence in Batch 042 can stop before the vector residual
        # reaches the Jacobi tolerance; preserve that numerical distinction.
        self.assertGreater(maximum_batch042_residual, 1e-6)
        self.assertLess(maximum_batch042_residual, 1e-5)

    def test_independent_full_spectrum_is_sorted_and_ground_observable_is_consistent(self):
        hamiltonian = projected_hamiltonian(1.0)
        eigenvalues, eigenvectors, _ = symmetric_jacobi_eigendecomposition(hamiltonian)
        self.assertEqual(len(eigenvalues), 18)
        self.assertEqual(eigenvalues, sorted(eigenvalues))

        ground = eigenvectors[0]
        self.assertTrue(
            math.isclose(sum(value * value for value in ground), 1.0, abs_tol=1e-12)
        )
        self.assertLess(eigenpair_residual(hamiltonian, eigenvalues[0], ground), 2e-12)
        self.assertTrue(
            math.isclose(
                operator_expectation(PROJECTED_PLAQUETTE_OPERATOR, ground),
                independent_ground_state(1.0).plaquette_expectation,
                rel_tol=0.0,
                abs_tol=1e-12,
            )
        )

    def test_evidence_classification_keeps_independence_boundary_and_nonclaims(self):
        evidence = classification()
        self.assertEqual(
            evidence["classification"],
            "LATTICE_QED_INDEPENDENT_OPERATOR_CROSSCHECK",
        )
        self.assertEqual(
            evidence["evidence_level"],
            "INTERNAL_INDEPENDENT_IMPLEMENTATION_CROSSCHECK",
        )
        self.assertEqual(evidence["full_hilbert_dimension"], 48)
        self.assertEqual(evidence["projected_sector_dimension"], 18)
        self.assertIn("not an independent external team", evidence["independence_boundary"])
        self.assertTrue(all(value is False for value in evidence["non_claims"].values()))


if __name__ == "__main__":
    unittest.main()
