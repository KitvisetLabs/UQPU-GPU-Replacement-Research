import unittest

from uqpu.qos_d23_phase_reconstruction_v040 import FROZEN_PHASES_V040
from uqpu.qos_d23_qsvt_matrix_fixture import (
    fixture_block_encoding,
    fixture_matrix,
    resource_ledger,
    verify_matrix_fixture,
)


class QOSD23QSVTMatrixFixtureTests(unittest.TestCase):
    def test_block_encoding_contains_fixture_matrix(self):
        matrix = fixture_matrix()
        block = fixture_block_encoding()
        for row in range(2):
            for column in range(2):
                self.assertAlmostEqual(block[row][column], matrix[row][column], delta=1e-15)

    def test_matrix_transform_and_unitarity_pass(self):
        certificate = verify_matrix_fixture()
        self.assertTrue(certificate.passed)
        self.assertLessEqual(certificate.transformed_real_block_residual, 2e-12)
        self.assertLessEqual(certificate.transformed_unitarity_residual, 2e-13)

    def test_phase_perturbation_is_detected(self):
        perturbed = list(FROZEN_PHASES_V040)
        perturbed[17] += 0.01
        certificate = verify_matrix_fixture(tuple(perturbed))
        self.assertFalse(certificate.passed)
        self.assertGreater(certificate.transformed_real_block_residual, 2e-12)

    def test_resource_ledger_is_explicit_and_non_hardware(self):
        ledger = resource_ledger()
        self.assertEqual(ledger["signal_or_block_encoding_queries"], 81)
        self.assertEqual(ledger["phase_rotations"], 82)
        self.assertEqual(ledger["provider_jobs"], 0)
        self.assertEqual(ledger["gate_decomposition_status"], "NOT_PERFORMED")
        self.assertEqual(ledger["energy_and_cost_status"], "NOT_MEASURED")


if __name__ == "__main__":
    unittest.main()
