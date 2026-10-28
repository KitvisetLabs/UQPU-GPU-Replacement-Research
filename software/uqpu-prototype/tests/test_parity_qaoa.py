import cmath
import math
import unittest

from uqpu.parity_encoding import build_parity_encoding
from uqpu.parity_qaoa import parity_qaoa_objective, parity_qaoa_program
from uqpu.small_statevector import statevector


class ParityQAOATests(unittest.TestCase):
    def setUp(self):
        self.encoding = build_parity_encoding(3, [(0, 1), (1, 2), (0, 2)])
        self.objective = parity_qaoa_objective(
            self.encoding, (-1.0, -1.0, -1.0), penalty_weight=7.0
        )

    def test_exact_certificate_matches_logical_maxcut_optimum(self):
        cert = self.objective.exact_certificate()
        self.assertEqual(cert.physical_qubits, 3)
        self.assertEqual(cert.states_evaluated, 8)
        self.assertTrue(cert.all_ground_states_feasible)
        self.assertAlmostEqual(cert.optimum_energy, -2.0)
        self.assertAlmostEqual(cert.feasible_optimum_energy, -2.0)
        self.assertEqual(cert.optimal_assignments, cert.feasible_optimal_assignments)
        for physical in cert.optimal_assignments:
            logical = self.objective.decode(physical)
            encoded = self.encoding.encode_logical(logical)
            self.assertEqual(encoded, physical)
            self.assertEqual(sum(bit for bit in encoded), 2)

    def test_higher_order_cycle_phase_gadget_matches_independent_dense_qaoa(self):
        objective = parity_qaoa_objective(
            self.encoding, (-1.0, -0.7, -1.3), penalty_weight=7.5
        )
        gammas, betas = (0.31, -0.57), (0.22, 0.49)
        program = parity_qaoa_program(objective, gammas, betas, shots=4097)
        n = objective.physical_qubits
        expected = [complex(1 / math.sqrt(1 << n))] * (1 << n)
        for gamma, beta in zip(gammas, betas):
            phased = [
                amplitude * cmath.exp(-1j * gamma * objective.energy(
                    tuple((basis >> q) & 1 for q in range(n))
                ))
                for basis, amplitude in enumerate(expected)
            ]
            expected = [
                sum(
                    amplitude
                    * math.cos(beta) ** (n - bin(basis ^ other).count("1"))
                    * (-1j * math.sin(beta)) ** bin(basis ^ other).count("1")
                    for other, amplitude in enumerate(phased)
                )
                for basis in range(1 << n)
            ]
        actual = statevector(program)
        global_phase = cmath.exp(-1j * sum(gammas) * objective.offset)
        for got, want in zip(actual, expected):
            self.assertAlmostEqual(abs(got * global_phase - want), 0.0, places=11)
        self.assertEqual(program.metadata["evidence_level"], "PROTOTYPE")
        self.assertTrue(program.metadata["acceptance_requires_cycle_parity_and_decode"])
        self.assertFalse(program.metadata["feasibility_preserving_mixer"])
        self.assertEqual(sum(inst.op == "cx" for inst in program.instructions), 8)

    def test_overlapping_four_and_five_cycle_gadgets_match_direct_reference(self):
        encoding = build_parity_encoding(
            5, [(0, 1), (0, 3), (1, 2), (2, 3), (2, 4), (3, 4)]
        )
        self.assertEqual(sorted(len(cycle) for cycle in encoding.cycle_constraints), [4, 5])
        objective = parity_qaoa_objective(
            encoding, (-1.0, 0.6, -0.7, 0.9, -1.2, 0.4), penalty_weight=12.0
        )
        certificate = objective.exact_certificate()
        self.assertEqual(certificate.states_evaluated, 1 << 6)
        self.assertTrue(certificate.all_ground_states_feasible)
        self.assertAlmostEqual(certificate.optimum_energy, certificate.feasible_optimum_energy)

        gammas, betas = (0.17, -0.43), (0.29, 0.51)
        program = parity_qaoa_program(objective, gammas, betas, shots=2048)
        n = objective.physical_qubits
        expected = [complex(1 / math.sqrt(1 << n))] * (1 << n)
        for gamma, beta in zip(gammas, betas):
            phased = [
                amplitude * cmath.exp(-1j * gamma * objective.energy(
                    tuple((basis >> q) & 1 for q in range(n))
                ))
                for basis, amplitude in enumerate(expected)
            ]
            expected = [
                sum(
                    amplitude
                    * math.cos(beta) ** (n - bin(basis ^ other).count("1"))
                    * (-1j * math.sin(beta)) ** bin(basis ^ other).count("1")
                    for other, amplitude in enumerate(phased)
                )
                for basis in range(1 << n)
            ]
        actual = statevector(program)
        global_phase = cmath.exp(-1j * sum(gammas) * objective.offset)
        for got, want in zip(actual, expected):
            self.assertAlmostEqual(abs(got * global_phase - want), 0.0, places=11)
        self.assertEqual(sum(inst.op == "cx" for inst in program.instructions), 28)

    def test_invalid_penalty_and_malformed_inputs_fail_closed(self):
        with self.assertRaisesRegex(ValueError, "penalty_weight"):
            parity_qaoa_objective(self.encoding, (-1.0, -1.0, -1.0), penalty_weight=6.0)
        with self.assertRaises(ValueError):
            parity_qaoa_objective(self.encoding, (-1.0, -1.0), penalty_weight=7.0)
        with self.assertRaises(ValueError):
            parity_qaoa_program(self.objective, [0.1], [])
        with self.assertRaises(ValueError):
            parity_qaoa_program(self.objective, [float("nan")], [0.2])
        with self.assertRaises(ValueError):
            self.objective.exact_certificate(max_qubits=2)

    def test_cycle_penalty_is_zero_only_for_even_parity(self):
        for bits in ((0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)):
            self.assertEqual(self.objective.violated_cycle_count(bits), 0)
        for bits in ((1, 0, 0), (0, 1, 0), (0, 0, 1), (1, 1, 1)):
            self.assertEqual(self.objective.violated_cycle_count(bits), 1)
            self.assertFalse(self.objective.is_feasible(bits))


if __name__ == "__main__":
    unittest.main()
