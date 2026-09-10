import math
import unittest

from uqpu.control_limit_gap import summarize_ml_duration_requirements
from uqpu.fundamental_limits import (
    PLANCK_CONSTANT_J_S,
    margolus_levitin_equivalent_frequency_hz,
    margolus_levitin_min_seconds,
    margolus_levitin_observed_to_bound_ratio,
    margolus_levitin_required_mean_energy_joule,
)


class InverseMargolusLevitinTests(unittest.TestCase):
    def test_inverse_duration_round_trip(self):
        duration = 32e-9
        energy = margolus_levitin_required_mean_energy_joule(duration)
        self.assertAlmostEqual(energy, PLANCK_CONSTANT_J_S / (4.0 * duration))
        self.assertAlmostEqual(margolus_levitin_min_seconds(energy), duration)
        self.assertAlmostEqual(
            margolus_levitin_equivalent_frequency_hz(duration), 7_812_500.0
        )
        self.assertAlmostEqual(
            margolus_levitin_observed_to_bound_ratio(duration, energy), 1.0
        )

    def test_invalid_inverse_inputs(self):
        for bad in (0.0, -1.0, float("nan"), float("inf")):
            with self.assertRaises(ValueError):
                margolus_levitin_required_mean_energy_joule(bad)
            with self.assertRaises(ValueError):
                margolus_levitin_equivalent_frequency_hz(bad)


class ControlDurationDiagnosticTests(unittest.TestCase):
    def fixture(self):
        return {
            "used_instruction_instances": [
                {"operation": "sx", "physical_qubits": [1], "duration_seconds": 32e-9},
                {"operation": "cz", "physical_qubits": [1, 2], "duration_seconds": 68e-9},
                {"operation": "rz", "physical_qubits": [1], "duration_seconds": 0.0},
                {"operation": "measure", "physical_qubits": [1], "duration_seconds": 2.28e-6},
            ]
        }

    def test_summary_excludes_measurement_and_virtual_rz(self):
        result = summarize_ml_duration_requirements(self.fixture())
        self.assertEqual(result["included_instruction_count"], 2)
        self.assertEqual(set(result["summary_by_operation"]), {"sx", "cz"})
        self.assertEqual(result["excluded_instruction_counts"]["operation:rz"], 1)
        self.assertEqual(result["excluded_instruction_counts"]["operation:measure"], 1)
        self.assertFalse(result["true_observed_to_ml_bound_ratio_available"])
        self.assertFalse(result["summed_duration_is_wall_clock_latency"])
        self.assertAlmostEqual(
            result["summed_included_instruction_duration_seconds"], 100e-9
        )

    def test_inverse_energy_order_tracks_duration(self):
        result = summarize_ml_duration_requirements(self.fixture())
        sx = result["summary_by_operation"]["sx"]
        cz = result["summary_by_operation"]["cz"]
        self.assertGreater(
            sx["ml_required_mean_energy_joule_for_equal_bound"]["mean"],
            cz["ml_required_mean_energy_joule_for_equal_bound"]["mean"],
        )

    def test_missing_rows_rejected(self):
        with self.assertRaises(ValueError):
            summarize_ml_duration_requirements({})


if __name__ == "__main__":
    unittest.main()
