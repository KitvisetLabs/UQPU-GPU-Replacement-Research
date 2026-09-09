import cmath
from dataclasses import replace
import math
import random
import unittest

from uqpu.adapters.ibm import IBMQuantumAdapter
from uqpu.adapters.aws_braket import AWSBraketAdapter
from uqpu.adapters.azure import AzureQuantumAdapter
from uqpu.cloud import ExecutionRequirements, QuantumParadigm
from uqpu.optimization_baseline import QuboInstance, demo_maxcut_triangle
from uqpu.portable import PortableInstruction as I, PortableProgram
from uqpu.qaoa import qubo_to_ising, qaoa_program
from uqpu.small_statevector import statevector, probabilities, sample_counts


class QaoaTests(unittest.TestCase):
    def test_ising_matches_every_assignment_of_signed_sparse_qubos(self):
        rng = random.Random(37)
        for _ in range(20):
            ids = (2, 5, 9, 12)
            instance = QuboInstance(
                {v: rng.uniform(-3, 3) for v in ids},
                {(a, b): rng.uniform(-2, 2) for a in ids for b in ids},
                constant=rng.uniform(-4, 4),
            )
            obj = qubo_to_ising(instance)
            for k in range(16):
                self.assertAlmostEqual(obj.energy(k), instance.energy(obj.assignment(k)), places=11)

    def test_circuit_matches_independent_dense_qaoa_definition(self):
        # This oracle uses the original QUBO energies and tensor-product mixer,
        # not the compiler's Ising coefficients or its CX/RZ gate decomposition.
        instance = QuboInstance({2: -0.7, 8: 1.2, 11: -0.3}, {(2, 8): 1.1, (8, 11): -0.8}, 2.5)
        gammas, betas = (0.31, -0.57), (0.22, 0.49)
        n = len(instance.variables)
        expected = [complex(1 / math.sqrt(1 << n))] * (1 << n)
        for gamma, beta in zip(gammas, betas):
            phased = [a * cmath.exp(-1j * gamma * instance.energy(
                {v: (k >> q) & 1 for q, v in enumerate(instance.variables)}
            )) for k, a in enumerate(expected)]
            expected = [sum(
                a * math.cos(beta) ** (n - bin(k ^ j).count('1'))
                * (-1j * math.sin(beta)) ** bin(k ^ j).count('1')
                for j, a in enumerate(phased)
            ) for k in range(1 << n)]
        actual = statevector(qaoa_program(instance, gammas, betas))
        phase = cmath.exp(-1j * sum(gammas) * qubo_to_ising(instance).offset)
        for a, e in zip(actual, expected):
            self.assertAlmostEqual(abs(a * phase - e), 0, places=12)

    def test_objective_offset_does_not_change_measurement_distribution(self):
        instance = demo_maxcut_triangle()
        p = probabilities(qaoa_program(instance, [0.7], [0.2]))
        shifted = replace(instance, constant=19)
        self.assertEqual(p, probabilities(qaoa_program(shifted, [0.7], [0.2])))
        self.assertAlmostEqual(qubo_to_ising(shifted).offset - qubo_to_ising(instance).offset, 19)

    def test_zero_cost_angle_gives_uniform_distribution(self):
        p = probabilities(qaoa_program(demo_maxcut_triangle(), [0], [0.3]))
        self.assertAlmostEqual(sum(p), 1)
        for v in p:
            self.assertAlmostEqual(v, 1 / 8)

    def test_noncontiguous_variables_and_basis_order(self):
        obj = qubo_to_ising(QuboInstance({7: 1, 20: 0}, {}))
        self.assertEqual(obj.assignment(1), {7: 1, 20: 0})
        self.assertEqual(obj.assignment(2), {7: 0, 20: 1})
        with self.assertRaises(ValueError):
            obj.assignment(4)

    def test_sampling_is_seeded_and_shot_total_is_preserved(self):
        program = qaoa_program(demo_maxcut_triangle(), [0.6], [0.25], shots=4097)
        counts = sample_counts(program, seed=99)
        self.assertEqual(counts, sample_counts(program, seed=99))
        self.assertEqual(sum(counts.values()), 4097)

    def test_three_provider_inspection_payloads_preserve_circuit(self):
        program = qaoa_program(demo_maxcut_triangle(), [0.6], [0.25], contract_id='test-contract')
        for adapter in (IBMQuantumAdapter(), AWSBraketAdapter(), AzureQuantumAdapter()):
            lowered = adapter.lower(program, ExecutionRequirements(QuantumParadigm.GATE_MODEL))
            dry = adapter.dry_run(lowered)
            self.assertEqual(dry['evidence_level'], 'DRY_RUN_ONLY')
            self.assertFalse(dry['paid_job_submitted'])
            self.assertIn('rx(0.5)', lowered.payload)
            self.assertEqual(lowered.payload.count('cx '), 6)

    def test_large_program_can_compile_but_cannot_allocate_simulation(self):
        program = qaoa_program(QuboInstance({q: 1 for q in range(32)}, {}), [0.3], [0.2])
        self.assertEqual(program.qubits, 32)
        with self.assertRaisesRegex(ValueError, 'at most 12'):
            probabilities(program)

    def test_invalid_parameters_and_nonfinite_coefficients_are_rejected(self):
        for gamma, beta in (([], []), ([1], []), ([float('nan')], [1])):
            with self.assertRaises(ValueError):
                qaoa_program(demo_maxcut_triangle(), gamma, beta)
        for bad in (float('inf'), float('nan')):
            with self.assertRaises(ValueError):
                qubo_to_ising(QuboInstance({0: bad}, {}))
        with self.assertRaises(ValueError):
            qaoa_program(demo_maxcut_triangle(), [1], [1], shots=True)
        with self.assertRaises(ValueError):
            qaoa_program(QuboInstance({0: 1e308}, {}), [10], [1])

    def test_simulator_rejects_malformed_and_dynamic_circuits(self):
        bad = [I('h'), I('cx', targets=(0,), controls=(0,)), I('rz', targets=(0,), params=(float('inf'),))]
        for inst in bad:
            with self.assertRaises(ValueError):
                statevector(PortableProgram('bad', 2, (inst,)))
        with self.assertRaises(ValueError):
            statevector(PortableProgram('dynamic', 2, (I('measure_all'), I('h', targets=(0,)))))


if __name__ == '__main__':
    unittest.main()
