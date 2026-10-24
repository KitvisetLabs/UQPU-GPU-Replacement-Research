import unittest

from uqpu.thermodynamic_gap import (
    ThermodynamicGapObservation,
    evaluate_thermodynamic_gap,
)


class ThermodynamicGapTests(unittest.TestCase):
    def observation(self, **changes):
        data = {
            "workload_contract_id": "UQPU-QUBO-ACCEPTED-OUTPUT-v1",
            "attempt_count": 5,
            "accepted_count": 2,
            "total_wall_plug_joules": 10.0,
            "energy_scope": "FULL_SYSTEM_WALL_PLUG",
            "temperature_kelvin": 300.0,
            "temperature_basis": "measured erasure-bath temperature",
            "evidence_level": "LAB_RESULT",
            "energy_provenance": "calibrated wall-plug meter record sha256:abc",
            "accepted_output_provenance": "frozen quality gate and output log sha256:def",
            "measurement_window": "2026-10-24T10:00:00Z/2026-10-24T10:10:00Z",
            "irreversible_erased_bits_per_accepted_task": 8.0,
            "erasure_accounting_basis": "reversible-circuit audit plus measured reset count",
            "erasure_provenance": "reset ledger sha256:ghi",
        }
        data.update(changes)
        return ThermodynamicGapObservation(**data)

    def test_ratio_uses_energy_per_accepted_task_including_failed_attempts(self):
        report = evaluate_thermodynamic_gap(self.observation())
        self.assertEqual(report["attempt_count"], 5)
        self.assertEqual(report["accepted_count"], 2)
        self.assertEqual(report["wall_plug_joules_per_accepted_task"], 5.0)
        self.assertGreater(report["wall_plug_to_landauer_floor_ratio"], 0.0)
        self.assertEqual(report["status"], "DIAGNOSTIC_ONLY")
        self.assertFalse(report["project_advantage_claim_allowed"])

    def test_missing_erasure_accounting_fails_closed(self):
        report = evaluate_thermodynamic_gap(
            self.observation(
                irreversible_erased_bits_per_accepted_task=None,
                erasure_accounting_basis="",
                erasure_provenance="",
            )
        )
        self.assertEqual(report["status"], "BLOCKED_ERASURE_ACCOUNTING")
        self.assertIsNone(report["landauer_floor_joules_per_accepted_task"])
        self.assertIsNone(report["wall_plug_to_landauer_floor_ratio"])
        self.assertFalse(report["eligible_for_fnd001_gap_analysis"])

    def test_no_accepted_outputs_has_no_per_task_ratio(self):
        report = evaluate_thermodynamic_gap(self.observation(accepted_count=0))
        self.assertEqual(report["status"], "NO_ACCEPTED_OUTPUTS")
        self.assertIsNone(report["wall_plug_joules_per_accepted_task"])
        self.assertIsNone(report["wall_plug_to_landauer_floor_ratio"])

    def test_zero_erasure_floor_has_undefined_ratio(self):
        report = evaluate_thermodynamic_gap(
            self.observation(
                irreversible_erased_bits_per_accepted_task=0.0,
                erasure_accounting_basis="explicit zero-erasure proof",
                erasure_provenance="proof sha256:zero",
            )
        )
        self.assertEqual(report["status"], "ZERO_ERASURE_FLOOR_RATIO_UNDEFINED")
        self.assertIsNone(report["wall_plug_to_landauer_floor_ratio"])

    def test_below_floor_requests_boundary_audit_not_physics_claim(self):
        report = evaluate_thermodynamic_gap(self.observation(total_wall_plug_joules=1e-30))
        self.assertEqual(report["status"], "BOUNDARY_AUDIT_REQUIRED")
        self.assertFalse(report["project_advantage_claim_allowed"])

    def test_measured_full_system_with_complete_provenance_is_eligible_only_for_analysis(self):
        report = evaluate_thermodynamic_gap(self.observation())
        self.assertTrue(report["eligible_for_fnd001_gap_analysis"])
        self.assertFalse(report["project_advantage_claim_allowed"])

    def test_model_only_cannot_become_measured_evidence(self):
        report = evaluate_thermodynamic_gap(
            self.observation(
                evidence_level="MODEL_ONLY",
                energy_provenance="scenario inputs",
                accepted_output_provenance="synthetic output fixture",
                measurement_window="not a measurement window",
            )
        )
        self.assertFalse(report["eligible_for_fnd001_gap_analysis"])
        self.assertEqual(report["evidence_level"], "MODEL_ONLY")

    def test_subsystem_energy_is_not_full_system_eligible(self):
        report = evaluate_thermodynamic_gap(self.observation(energy_scope="QPU_SUBSYSTEM"))
        self.assertFalse(report["eligible_for_fnd001_gap_analysis"])

    def test_measured_level_requires_provenance(self):
        with self.assertRaisesRegex(ValueError, "energy_provenance"):
            evaluate_thermodynamic_gap(self.observation(energy_provenance=""))

    def test_erasure_count_requires_basis_and_provenance(self):
        with self.assertRaisesRegex(ValueError, "erasure_accounting_basis"):
            evaluate_thermodynamic_gap(self.observation(erasure_accounting_basis=""))
        with self.assertRaisesRegex(ValueError, "erasure_provenance"):
            evaluate_thermodynamic_gap(self.observation(erasure_provenance=""))

    def test_nonfinite_or_negative_energy_is_rejected(self):
        for value in (float("nan"), float("inf"), -1.0):
            with self.subTest(value=value), self.assertRaises(ValueError):
                evaluate_thermodynamic_gap(self.observation(total_wall_plug_joules=value))

    def test_invalid_temperature_and_erasure_bits_are_rejected(self):
        for value in (0.0, -1.0, float("nan"), float("inf")):
            with self.subTest(temperature=value), self.assertRaises(ValueError):
                evaluate_thermodynamic_gap(self.observation(temperature_kelvin=value))
        with self.assertRaises(ValueError):
            evaluate_thermodynamic_gap(
                self.observation(irreversible_erased_bits_per_accepted_task=-1.0)
            )

    def test_invalid_counts_and_evidence_label_are_rejected(self):
        with self.assertRaises(ValueError):
            evaluate_thermodynamic_gap(self.observation(accepted_count=6))
        with self.assertRaises(ValueError):
            evaluate_thermodynamic_gap(self.observation(attempt_count=True))
        with self.assertRaises(ValueError):
            evaluate_thermodynamic_gap(self.observation(evidence_level="NEW_PHYSICS"))

    def test_output_bits_are_not_an_input_to_erasure_inference(self):
        report = evaluate_thermodynamic_gap(
            self.observation(
                irreversible_erased_bits_per_accepted_task=None,
                erasure_accounting_basis="",
                erasure_provenance="",
            )
        )
        self.assertIsNone(report["irreversible_erased_bits_per_accepted_task"])
        self.assertIn(
            "erased bits are not inferred from output bits, qubit count, or Hilbert-space dimension",
            report["nonclaims"],
        )

    def test_non_string_metadata_is_rejected_as_value_error(self):
        for changes in (
            {"workload_contract_id": None},
            {"temperature_basis": None},
            {"energy_scope": []},
            {"evidence_level": []},
            {"energy_provenance": None},
        ):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                evaluate_thermodynamic_gap(self.observation(**changes))


if __name__ == "__main__":
    unittest.main()
