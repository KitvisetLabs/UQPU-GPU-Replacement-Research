import unittest

from uqpu.ai_training_vqc_reproduction import (
    REFERENCE_CALIBRATION,
    REFERENCE_INITIAL_PARAMETERS,
    REFERENCE_Z0_FINAL_PARAMETERS,
    REFERENCE_ZZ_FINAL_PARAMETERS,
    VQCReproductionConfig,
    expectation_and_gradient,
    parameter_shift_deployment_ledger,
    run_reproduction,
    structurally_inactive_parameter_indices,
)


class AITrainingVQCReproductionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.result = run_reproduction(VQCReproductionConfig())

    def test_public_route_reproduces_negative_result(self):
        route = self.result["paper_architecture_route"]
        self.assertEqual(route["test_metrics"]["accuracy"], 0.95703125)
        self.assertAlmostEqual(
            route["test_metrics"]["binary_cross_entropy"],
            0.37888043300038676,
            places=12,
        )
        self.assertFalse(self.result["accepted_capability_contract"]["paper_architecture_route_passes"])
        for actual, expected in zip(route["final_parameters"], REFERENCE_Z0_FINAL_PARAMETERS):
            self.assertAlmostEqual(actual, expected, places=11)

    def test_uqpu_readout_repair_passes_frozen_contract(self):
        repair = self.result["uqpu_readout_repair"]
        quantum = repair["quantum_route_before_calibration"]
        for actual, expected in zip(quantum["final_parameters"], REFERENCE_ZZ_FINAL_PARAMETERS):
            self.assertAlmostEqual(actual, expected, places=11)
        self.assertEqual(quantum["test_metrics"]["accuracy"], 0.9921875)
        self.assertAlmostEqual(
            quantum["test_metrics"]["binary_cross_entropy"],
            0.3774990388898494,
            places=12,
        )
        self.assertAlmostEqual(repair["calibration"]["scale"], REFERENCE_CALIBRATION[0], places=10)
        self.assertAlmostEqual(repair["calibration"]["bias"], REFERENCE_CALIBRATION[1], places=10)
        self.assertEqual(repair["calibrated_test_metrics"]["accuracy"], 0.984375)
        self.assertAlmostEqual(
            repair["calibrated_test_metrics"]["binary_cross_entropy"],
            0.12508869380594245,
            places=11,
        )
        self.assertTrue(self.result["accepted_capability_contract"]["uqpu_readout_repair_passes"])

    def test_z0_readout_has_four_exactly_inactive_last_layer_parameters(self):
        _, gradient = expectation_and_gradient(
            0.31,
            -0.47,
            REFERENCE_INITIAL_PARAMETERS,
            depth=2,
            observable="Z0",
        )
        inactive = structurally_inactive_parameter_indices(2, "Z0")
        self.assertEqual(inactive, (8, 9, 10, 11))
        for index in inactive:
            self.assertAlmostEqual(gradient[index], 0.0, places=13)

    def test_parity_readout_reduces_structurally_inactive_tail(self):
        _, gradient = expectation_and_gradient(
            0.31,
            -0.47,
            REFERENCE_INITIAL_PARAMETERS,
            depth=2,
            observable="ZZ",
        )
        inactive = structurally_inactive_parameter_indices(2, "ZZ")
        self.assertEqual(inactive, (8, 11))
        for index in inactive:
            self.assertAlmostEqual(gradient[index], 0.0, places=13)
        self.assertGreater(abs(gradient[9]) + abs(gradient[10]), 1e-8)

    def test_parameter_shift_resource_pressure_is_explicit(self):
        ledger = parameter_shift_deployment_ledger(VQCReproductionConfig())
        self.assertEqual(ledger["training_samples_processed"], 64000)
        self.assertEqual(ledger["circuits_per_training_sample"], 25)
        self.assertEqual(ledger["training_circuit_evaluations"], 1_600_000)
        self.assertEqual(ledger["training_single_qubit_rotation_applications"], 22_400_000)
        self.assertEqual(ledger["training_cnot_applications"], 3_200_000)
        self.assertEqual(ledger["shots_if_128_per_circuit"], 204_800_000)
        self.assertEqual(ledger["shots_if_1024_per_circuit"], 1_638_400_000)
        self.assertEqual(ledger["status"], "PARAMETER_SHIFT_CIRCUIT_EQUIVALENT_NOT_EXECUTED")


if __name__ == "__main__":
    unittest.main()
