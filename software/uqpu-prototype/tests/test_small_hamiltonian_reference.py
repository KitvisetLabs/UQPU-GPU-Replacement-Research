import cmath
import math
import unittest

from uqpu.small_hamiltonian_reference import (
    evolve_2x2_hermitian,
    hamiltonian_2x2_contract,
    max_unitarity_residual,
)


def _multiply_2x2(left, right):
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


class SmallHamiltonianReferenceTests(unittest.TestCase):
    def test_pauli_x_closed_form_matches_analytic_reference(self):
        time = 0.7
        unitary = evolve_2x2_hermitian(0.0, 0.0, 1.0, time)
        expected = (
            (complex(math.cos(time), 0.0), -1j * math.sin(time)),
            (-1j * math.sin(time), complex(math.cos(time), 0.0)),
        )
        for i in range(2):
            for j in range(2):
                self.assertLess(abs(unitary[i][j] - expected[i][j]), 1e-14)
        self.assertLess(max_unitarity_residual(unitary), 1e-14)

    def test_diagonal_degenerate_limit_and_zero_time(self):
        unitary = evolve_2x2_hermitian(2.0, 2.0, 0.0, 0.4)
        phase = cmath.exp(-2j * 0.4)
        self.assertLess(abs(unitary[0][0] - phase), 1e-14)
        self.assertLess(abs(unitary[1][1] - phase), 1e-14)
        self.assertEqual(unitary[0][1], 0j)
        self.assertEqual(unitary[1][0], 0j)
        identity = evolve_2x2_hermitian(2.0, -3.0, 0.5j, 0.0)
        self.assertEqual(identity, ((1 + 0j, 0j), (0j, 1 + 0j)))

    def test_unitarity_and_semigroup_property(self):
        hamiltonian = (0.7, -1.2, 0.4 + 0.3j)
        u03 = evolve_2x2_hermitian(*hamiltonian, 0.3)
        u04 = evolve_2x2_hermitian(*hamiltonian, 0.4)
        u07 = evolve_2x2_hermitian(*hamiltonian, 0.7)
        self.assertLess(max_unitarity_residual(u03), 2e-14)
        self.assertLess(max_unitarity_residual(u07), 2e-14)
        composed = _multiply_2x2(u03, u04)
        for i in range(2):
            for j in range(2):
                self.assertLess(abs(composed[i][j] - u07[i][j]), 2e-14)

    def test_sparse_contract_reports_row_and_column_norms(self):
        contract = hamiltonian_2x2_contract(0.0, 0.0, 1.0)
        self.assertEqual(contract["dimension"], 2)
        self.assertEqual(contract["max_row_sparsity"], 1)
        self.assertEqual(contract["row_euclidean_norms"], (1.0, 1.0))
        self.assertEqual(contract["column_euclidean_norms"], (1.0, 1.0))
        self.assertEqual(contract["eta"], 1.0)
        self.assertEqual(contract["evidence_level"], "MODEL_ONLY")
        full = hamiltonian_2x2_contract(2.0, -3.0, 0.5j)
        self.assertEqual(full["max_row_sparsity"], 2)
        self.assertAlmostEqual(full["eta"], math.sqrt(9.25))

    def test_invalid_inputs_fail_closed(self):
        for args in (
            (True, 0.0, 0.0),
            (0.0, float("nan"), 0.0),
            (0.0, 0.0, complex(float("inf"), 0.0)),
        ):
            with self.subTest(args=args):
                with self.assertRaises(ValueError):
                    hamiltonian_2x2_contract(*args)
        with self.assertRaises(ValueError):
            evolve_2x2_hermitian(0.0, 0.0, 1.0, float("nan"))
        with self.assertRaises(ValueError):
            max_unitarity_residual(((1.0, 0.0), (0.0, float("inf"))))
        with self.assertRaises(ValueError):
            max_unitarity_residual(((1.0, 0.0, 0.0), (0.0, 1.0, 0.0)))


if __name__ == "__main__":
    unittest.main()
