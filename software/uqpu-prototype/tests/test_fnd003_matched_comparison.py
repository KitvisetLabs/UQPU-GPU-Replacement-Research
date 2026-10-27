import unittest

from uqpu.fnd003_matched_comparison import (
    build_fnd003_matched_comparison_contract,
    canonical_sha256,
    validate_fnd003_matched_comparison_contract,
)


class FND003MatchedComparisonTests(unittest.TestCase):
    def setUp(self):
        self.task = {
            "workload_id": "FND003-TEST-WORKLOAD",
            "input_sha256": "1" * 64,
            "output_contract_sha256": "2" * 64,
            "acceptance_metric": "normalized_output_quality",
            "quality_direction": "MINIMUM",
            "quality_threshold": 0.95,
            "time_boundary_id": "start-to-accepted-output-v1",
            "held_out_case_id": "held-out-case-01",
        }
        self.task_sha = canonical_sha256(self.task)
        self.evolution = {
            "initial_state_sha256": "3" * 64,
            "final_state_sha256": "4" * 64,
            "hamiltonian_sha256": "5" * 64,
            "dynamics_model_sha256": "6" * 64,
            "state_distance_definition": "trace distance, frozen convention v1",
            "coarse_graining_definition": "declared subsystem partition v1",
            "entropy_production_definition": "source-defined entropy production v1",
        }
        self.evolution_sha = canonical_sha256(self.evolution)
        self.control = {
            "run_id": "control-run-01",
            "task_contract_sha256": self.task_sha,
            "elapsed_seconds": 2.0,
            "elapsed_uncertainty_seconds": 0.05,
            "quality_value": 0.98,
            "measurement_class": "LAB_MEASURED",
            "measurement_artifact_sha256": "7" * 64,
            "wall_plug_energy": {
                "joules": 5.0,
                "uncertainty_j": 0.2,
                "boundary_id": "whole-system-wall-plug-v1",
                "meter_source": "calibrated-meter-A",
            },
        }
        self.quantum = {
            "run_id": "quantum-run-01",
            "task_contract_sha256": self.task_sha,
            "elapsed_seconds": 1.0,
            "elapsed_uncertainty_seconds": 0.04,
            "quality_value": 0.97,
            "measurement_class": "LAB_MEASURED",
            "measurement_artifact_sha256": "8" * 64,
            "evolution_contract_sha256": self.evolution_sha,
            "wall_plug_energy": {
                "joules": 2.0,
                "uncertainty_j": 0.1,
                "boundary_id": "whole-system-wall-plug-v1",
                "meter_source": "calibrated-meter-B",
            },
        }
        self.speed_limit = {
            "theorem_id": "FND003-THERMODYNAMIC-SPEED-LIMIT-TEST",
            "source_url": "https://arxiv.org/abs/2609.12520",
            "source_version": "pinned-test-version",
            "theorem_scope": "finite-time unitary driving under declared coarse-graining",
            "task_contract_sha256": self.task_sha,
            "quantum_run_id": self.quantum["run_id"],
            "evolution_contract": self.evolution,
            "evolution_contract_sha256": self.evolution_sha,
            "assumptions_verified": True,
            "assumption_audit_sha256": "9" * 64,
            "bound_derivation_sha256": "a" * 64,
            "bound_seconds": 0.25,
        }

    def build(self, **changes):
        speed = dict(self.speed_limit)
        speed.update(changes)
        return build_fnd003_matched_comparison_contract(
            self.task, self.control, self.quantum, speed
        )

    def test_matched_accepted_measurements_emit_descriptive_ratios_only(self):
        record = self.build()
        self.assertEqual(record["comparison"]["status"], "MATCHED_ACCEPTED_OUTPUTS_MEASURED")
        self.assertEqual(
            record["comparison"]["control_over_quantum_elapsed_time_ratio"], 2.0
        )
        self.assertEqual(
            record["comparison"]["quantum_elapsed_over_applicable_bound_ratio"], 4.0
        )
        self.assertEqual(
            record["comparison"]["control_over_quantum_wall_plug_energy_ratio"], 2.5
        )
        self.assertFalse(record["measured_advantage_established"])
        self.assertFalse(record["physical_law_established"])
        self.assertEqual(validate_fnd003_matched_comparison_contract(record), [])

    def test_simulation_cannot_emit_measured_ratios(self):
        control = dict(self.control, measurement_class="SIMULATION_ONLY",
                       measurement_artifact_sha256=None)
        quantum = dict(self.quantum, measurement_class="SIMULATION_ONLY",
                       measurement_artifact_sha256=None)
        record = build_fnd003_matched_comparison_contract(
            self.task, control, quantum, self.speed_limit
        )
        self.assertIsNone(record["comparison"]["control_over_quantum_elapsed_time_ratio"])
        self.assertIsNone(record["comparison"]["quantum_elapsed_over_applicable_bound_ratio"])
        self.assertEqual(
            record["comparison"]["status"],
            "ACCEPTED_OUTPUTS_BUT_LAB_MEASUREMENTS_REQUIRED",
        )

    def test_unverified_assumptions_cannot_carry_a_bound(self):
        with self.assertRaisesRegex(ValueError, "must not carry bound_seconds"):
            self.build(assumptions_verified=False)

    def test_verified_assumptions_require_derivation_and_audit_digests(self):
        with self.assertRaisesRegex(ValueError, "bound_derivation_sha256"):
            self.build(bound_derivation_sha256=None)

    def test_control_run_must_match_shared_task_contract(self):
        control = dict(self.control, task_contract_sha256="b" * 64)
        with self.assertRaisesRegex(ValueError, "not bound to the shared task"):
            build_fnd003_matched_comparison_contract(
                self.task, control, self.quantum, self.speed_limit
            )

    def test_quantum_run_must_match_exact_evolution_contract(self):
        quantum = dict(self.quantum, evolution_contract_sha256="c" * 64)
        with self.assertRaisesRegex(ValueError, "not bound to the speed-limit evolution"):
            build_fnd003_matched_comparison_contract(
                self.task, self.control, quantum, self.speed_limit
            )

    def test_failed_quality_gate_suppresses_comparison_ratios(self):
        quantum = dict(self.quantum, quality_value=0.80)
        record = build_fnd003_matched_comparison_contract(
            self.task, self.control, quantum, self.speed_limit
        )
        self.assertEqual(record["comparison"]["status"], "OUTPUT_QUALITY_GATE_FAILED")
        self.assertIsNone(record["comparison"]["control_over_quantum_elapsed_time_ratio"])
        self.assertIsNone(record["comparison"]["quantum_elapsed_over_applicable_bound_ratio"])

    def test_energy_ratio_is_suppressed_when_boundaries_differ(self):
        quantum = dict(self.quantum)
        quantum["wall_plug_energy"] = dict(
            quantum["wall_plug_energy"], boundary_id="quantum-only-meter-boundary"
        )
        record = build_fnd003_matched_comparison_contract(
            self.task, self.control, quantum, self.speed_limit
        )
        self.assertEqual(
            record["comparison"]["wall_plug_energy_boundary_status"],
            "ENERGY_BOUNDARIES_DO_NOT_MATCH",
        )
        self.assertIsNone(record["comparison"]["control_over_quantum_wall_plug_energy_ratio"])

    def test_duplicate_run_ids_are_rejected(self):
        quantum = dict(self.quantum, run_id=self.control["run_id"])
        with self.assertRaisesRegex(ValueError, "run_id values must differ"):
            build_fnd003_matched_comparison_contract(
                self.task, self.control, quantum, self.speed_limit
            )

    def test_nonfinite_or_nonpositive_elapsed_time_is_rejected(self):
        for value in (0, -1, float("nan"), float("inf")):
            control = dict(self.control, elapsed_seconds=value)
            with self.subTest(value=value), self.assertRaises(ValueError):
                build_fnd003_matched_comparison_contract(
                    self.task, control, self.quantum, self.speed_limit
                )

    def test_quality_direction_maximum_is_supported(self):
        task = dict(self.task, quality_direction="MAXIMUM", quality_threshold=0.1)
        task_sha = canonical_sha256(task)
        control = dict(self.control, task_contract_sha256=task_sha, quality_value=0.05)
        quantum = dict(self.quantum, task_contract_sha256=task_sha, quality_value=0.08)
        speed = dict(
            self.speed_limit,
            task_contract_sha256=task_sha,
        )
        record = build_fnd003_matched_comparison_contract(task, control, quantum, speed)
        self.assertTrue(record["comparison"]["control_quality_accepted"])
        self.assertTrue(record["comparison"]["quantum_quality_accepted"])

    def test_tampering_with_derived_metrics_fails_validation(self):
        record = self.build()
        altered = dict(record)
        altered["comparison"] = dict(record["comparison"], measured_advantage_established=True)
        self.assertEqual(
            validate_fnd003_matched_comparison_contract(altered), ["contract_mismatch"]
        )

    def test_invalid_energy_uncertainty_is_rejected(self):
        control = dict(self.control)
        control["wall_plug_energy"] = dict(
            control["wall_plug_energy"], uncertainty_j=-0.1
        )
        with self.assertRaisesRegex(ValueError, "cannot be negative"):
            build_fnd003_matched_comparison_contract(
                self.task, control, self.quantum, self.speed_limit
            )


if __name__ == "__main__":
    unittest.main()
