"""Integrated signed-Max-Cut -> portable QAOA -> exact local simulator gate.

This is a finite classical/reference and ideal statevector contract only. It
does not execute a provider target, establish noisy-device quality, or claim
quantum/economic advantage.
"""
import cmath
import math
import unittest

from uqpu.adapters.aws_braket import AWSBraketAdapter
from uqpu.adapters.azure import AzureQuantumAdapter
from uqpu.adapters.ibm import IBMQuantumAdapter
from uqpu.cloud import ExecutionRequirements, QuantumParadigm
from uqpu.optimization_baseline import QuboInstance
from uqpu.qaoa import qaoa_program, qubo_to_ising
from uqpu.sdk_signed_maxcut import tiny_signed_maxcut_fixtures
from uqpu.signed_maxcut_objective import compile_signed_maxcut
from uqpu.small_statevector import probabilities, statevector


def _minimize_negative_cut(lowering):
    return QuboInstance(
        {v: -lowering.qubo_linear[v] for v in range(lowering.vertex_count)},
        {(u, v): -coefficient for u, v, coefficient in lowering.qubo_quadratic},
        constant=0.0,
    )


def _independent_reference_statevector(lowering, gammas, betas):
    """Dense reference uses direct signed-cut scores, not compiler Ising terms."""
    n = lowering.vertex_count
    amplitudes = [complex(1 / math.sqrt(1 << n))] * (1 << n)
    for gamma, beta in zip(gammas, betas):
        phased = []
        for basis_index, amplitude in enumerate(amplitudes):
            bits = tuple((basis_index >> q) & 1 for q in range(n))
            energy = -lowering.direct_score(bits)
            phased.append(amplitude * cmath.exp(-1j * gamma * energy))
        mixed = []
        for output_index in range(1 << n):
            total = 0j
            for input_index, amplitude in enumerate(phased):
                flips = (output_index ^ input_index).bit_count()
                total += (
                    amplitude
                    * math.cos(beta) ** (n - flips)
                    * (-1j * math.sin(beta)) ** flips
                )
            mixed.append(total)
        amplitudes = mixed
    return tuple(amplitudes)


class SignedMaxCutPortableQAOATests(unittest.TestCase):
    def test_frozen_signed_graphs_preserve_objective_and_portable_qaoa_state(self):
        gammas = (0.23, -0.41)
        betas = (0.17, 0.29)
        for name, vertex_count, edges in tiny_signed_maxcut_fixtures():
            with self.subTest(fixture=name):
                lowering = compile_signed_maxcut(vertex_count, edges)
                instance = _minimize_negative_cut(lowering)
                ising = qubo_to_ising(instance)
                for basis_index in range(1 << vertex_count):
                    bits = tuple((basis_index >> q) & 1 for q in range(vertex_count))
                    expected_energy = -lowering.direct_score(bits)
                    assignment = {q: bits[q] for q in range(vertex_count)}
                    self.assertAlmostEqual(instance.energy(assignment), expected_energy, places=11)
                    self.assertAlmostEqual(ising.energy(basis_index), expected_energy, places=11)

                contract_id = f"INT-20261028-SIGNED-MAXCUT-{name}"
                program = qaoa_program(
                    instance, gammas, betas, shots=257, contract_id=contract_id
                )
                self.assertEqual(program.metadata["contract_id"], contract_id)
                self.assertEqual(program.metadata["objective_sense"], "minimize")
                self.assertEqual(program.metadata["bit_order"], "qubit_0_is_integer_lsb")
                self.assertEqual(program.shots, 257)
                actual = statevector(program)
                reference = _independent_reference_statevector(lowering, gammas, betas)
                omitted_offset_phase = cmath.exp(-1j * sum(gammas) * ising.offset)
                for observed, expected in zip(actual, reference):
                    self.assertAlmostEqual(
                        abs(observed * omitted_offset_phase - expected), 0.0, places=10
                    )
                self.assertAlmostEqual(sum(probabilities(program)), 1.0, places=11)

    def test_provider_adapters_are_dry_run_only_for_the_same_signed_workload(self):
        name, vertex_count, edges = tiny_signed_maxcut_fixtures()[1]
        lowering = compile_signed_maxcut(vertex_count, edges)
        program = qaoa_program(
            _minimize_negative_cut(lowering), [0.6], [0.25],
            shots=257, contract_id=f"INT-20261028-SIGNED-MAXCUT-{name}",
        )
        requirements = ExecutionRequirements(QuantumParadigm.GATE_MODEL)
        for adapter in (IBMQuantumAdapter(), AWSBraketAdapter(), AzureQuantumAdapter()):
            lowered = adapter.lower(program, requirements)
            dry = adapter.dry_run(lowered)
            self.assertEqual(dry["evidence_level"], "DRY_RUN_ONLY")
            self.assertFalse(dry["paid_job_submitted"])


if __name__ == "__main__":
    unittest.main()
