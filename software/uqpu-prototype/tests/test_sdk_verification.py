import importlib.util
import unittest

from uqpu.sdk_verification import classical_probabilities, terminal_measurement_map


@unittest.skipUnless(importlib.util.find_spec('qiskit'), 'optional Qiskit verification dependency')
class SdkVerificationTests(unittest.TestCase):
    def test_permuted_readout_is_decoded_in_classical_bit_order(self):
        from qiskit import QuantumCircuit
        circuit = QuantumCircuit(2, 2)
        circuit.x(0)
        circuit.measure(0, 1)
        circuit.measure(1, 0)
        self.assertEqual(terminal_measurement_map(circuit), {0: 1, 1: 0})
        self.assertEqual(classical_probabilities(circuit), (0, 0, 1, 0))

    def test_partial_and_dynamic_measurements_are_rejected(self):
        from qiskit import QuantumCircuit
        circuit = QuantumCircuit(2, 2)
        circuit.measure(0, 0)
        with self.assertRaises(ValueError):
            terminal_measurement_map(circuit)
        circuit.x(1)
        circuit.measure(1, 1)
        with self.assertRaises(ValueError):
            terminal_measurement_map(circuit)

    def test_large_state_allocation_is_rejected(self):
        from qiskit import QuantumCircuit
        with self.assertRaises(ValueError):
            classical_probabilities(QuantumCircuit(32, 32))
