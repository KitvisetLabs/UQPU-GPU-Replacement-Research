import unittest

from uqpu.gate_speed_limit_contract import GateSpeedLimitRecord

SHA = "a" * 64
SCOPE = (
    "bounded_hamiltonian_spectral_width",
    "target_unitary_identity",
    "initial_final_operator_definition",
    "control_resource_boundary",
    "noise_environment_scope",
    "calibration_validity",
)


def record(**overrides):
    values = dict(
        record_id="FND003-GATE-QSL-TEST-001",
        theorem_reference="APS accepted paper DOI:10.1103/28zn-ch8y",
        theorem_source_sha256=SHA,
        bound_derivation_sha256="b" * 64,
        gate_name="test-unitary",
        target_id="synthetic-target-v1",
        target_kind="SIMULATOR",
        unitary_sha256="c" * 64,
        hamiltonian_model_sha256="d" * 64,
        calibration_sha256="e" * 64,
        observed_duration_seconds=2.0,
        duration_uncertainty_seconds=0.1,
        lower_bound_seconds=1.5,
        bound_uncertainty_seconds=0.1,
        repeat_count=10,
        scope_checks=SCOPE,
        observation_method="deterministic synthetic fixture; no hardware execution",
        evidence_level="SIMULATION",
    )
    values.update(overrides)
    return GateSpeedLimitRecord(**values)


class GateSpeedLimitContractTests(unittest.TestCase):
    def test_valid_simulation_record_is_consistent_with_bound_interval(self):
        self.assertEqual(record().consistency_classification(), "CONSISTENT_WITH_BOUND_INTERVAL")

    def test_interval_below_bound_requests_audit_not_new_physics(self):
        result = record(
            observed_duration_seconds=0.5, duration_uncertainty_seconds=0.01,
            lower_bound_seconds=1.5, bound_uncertainty_seconds=0.01,
        ).consistency_classification()
        self.assertEqual(result, "BELOW_BOUND_REQUIRES_THEOREM_AND_METROLOGY_AUDIT")
        self.assertNotIn("VIOLATION", result)

    def test_overlapping_intervals_are_not_forced_to_pass_or_fail(self):
        result = record(
            observed_duration_seconds=1.5, duration_uncertainty_seconds=0.2,
            lower_bound_seconds=1.5, bound_uncertainty_seconds=0.2,
        ).consistency_classification()
        self.assertEqual(result, "OVERLAPPING_UNCERTAINTY_INTERVALS")

    def test_missing_scope_check_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "missing scope checks"):
            record(scope_checks=("bounded_hamiltonian_spectral_width",)).validate()

    def test_invalid_hash_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            record(unitary_sha256="not-a-hash").validate()

    def test_nonfinite_boolean_or_negative_duration_inputs_fail(self):
        invalid = (
            {"observed_duration_seconds": True},
            {"observed_duration_seconds": float("nan")},
            {"lower_bound_seconds": float("inf")},
            {"duration_uncertainty_seconds": -0.1},
            {"bound_uncertainty_seconds": float("nan")},
            {"observed_duration_seconds": 0.0},
        )
        for changes in invalid:
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                record(**changes).validate()

    def test_hardware_record_requires_provider_job_and_physical_evidence_label(self):
        with self.assertRaisesRegex(ValueError, "provider_job_id"):
            record(target_kind="HARDWARE_TARGET", evidence_level="LAB_RESULT").validate()
        with self.assertRaisesRegex(ValueError, "physical target records"):
            record(
                target_kind="HARDWARE_TARGET", evidence_level="SIMULATION",
                provider_job_id="synthetic-placeholder-only",
            ).validate()

    def test_simulator_cannot_be_promoted_to_lab_evidence(self):
        with self.assertRaisesRegex(ValueError, "simulator records"):
            record(evidence_level="LAB_RESULT").validate()

    def test_repeat_count_must_be_positive_non_boolean_integer(self):
        for value in (0, -1, True, 2.5):
            with self.subTest(value=value), self.assertRaisesRegex(ValueError, "repeat_count"):
                record(repeat_count=value).validate()

    def test_classification_is_deterministic_for_frozen_record(self):
        candidate = record()
        self.assertEqual(candidate.consistency_classification(), candidate.consistency_classification())


if __name__ == "__main__":
    unittest.main()
