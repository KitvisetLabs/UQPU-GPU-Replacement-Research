import unittest

from uqpu.circuit_fab_bridge import assess_circuit_fab_bridge


def complete_payload():
    return {
        "workload_contract_id": "WORK-001",
        "quality_contract_id": "QUALITY-001",
        "candidate_circuit_sha256": "a" * 64,
        "reference_circuit_sha256": "b" * 64,
        "evidence_class": "SIMULATION",
        "equivalence_status": "PASS_INDEPENDENT",
        "output_equivalence_certificate_id": "CERT-001",
        "logical_qubits": 12,
        "native_gate_counts": {"1q": 100, "2q": 40},
        "routed_depth": 88,
        "shots_per_accepted_task": 4096,
        "target_id": "QPU-TARGET-001",
        "target_snapshot_sha256": "c" * 64,
        "calibration_snapshot_id": "CAL-001",
        "native_gate_set_id": "GATESET-001",
        "routing_profile_id": "ROUTE-001",
        "qec_profile_id": "QEC-001",
        "physical_qubits": 48,
        "readout_profile_id": "READOUT-001",
        "control_power_w": 12.5,
        "cryogenic_load_w": 20.0,
        "latency_s": 1.2,
        "device_architecture_id": "DEVICE-001",
        "process_window_id": "PROCESS-001",
        "yield_fraction": 0.8,
        "fab_cost_per_good_die_usd": 12000.0,
        "package_test_cost_per_device_usd": 900.0,
        "lifetime_tasks_per_device": 1_000_000,
        "uqpu_cost_target_id": "QPU-TARGET-001",
        "baseline_stack_id": "CPU-GPU-BASELINE-001",
        "baseline_workload_contract_id": "WORK-001",
        "baseline_quality_contract_id": "QUALITY-001",
        "measurement_window_id": "WINDOW-001",
        "baseline_measurement_window_id": "WINDOW-001",
        "provider_cost_per_task_usd": 0.01,
        "host_cost_per_task_usd": 0.001,
        "energy_kwh_per_task": 0.0002,
        "maintenance_cost_per_task_usd": 0.0001,
        "reconstruction_cost_per_task_usd": 0.0002,
        "baseline_cost_per_task_usd": 0.02,
        "uqpu_cost_per_task_usd": 0.015,
        "accepted_output_count": 100,
        "uncertainty_manifest_id": "UNCERTAINTY-001",
    }


class CircuitFabBridgeTests(unittest.TestCase):
    def test_complete_contract_is_only_ready_for_review(self):
        result = assess_circuit_fab_bridge(complete_payload())
        self.assertEqual(result.status, "READY_FOR_INTEGRATION_REVIEW")
        self.assertIn("no physical advantage", result.claim_boundary)

    def test_literature_resource_counts_do_not_replace_circuit_certificate(self):
        literature_only = {
            "evidence_class": "LITERATURE_ONLY",
            "reported_toffoli_count": 440_000,
            "reported_peak_qubits": 1_837,
        }
        result = assess_circuit_fab_bridge(literature_only)
        self.assertEqual(result.status, "BLOCKED_CIRCUIT_CERTIFICATE")
        self.assertIn("workload_contract_id", result.missing_fields)
        self.assertEqual(result.evidence_class, "LITERATURE_ONLY")

    def test_same_implementation_equivalence_is_not_independent_acceptance(self):
        payload = complete_payload()
        payload["equivalence_status"] = "PASS_SAME_IMPLEMENTATION"
        result = assess_circuit_fab_bridge(payload)
        self.assertEqual(result.status, "BLOCKED_EQUIVALENCE")

    def test_missing_target_snapshot_blocks_device_mapping(self):
        payload = complete_payload()
        for key in (
            "target_id", "target_snapshot_sha256", "calibration_snapshot_id",
            "native_gate_set_id", "routing_profile_id", "qec_profile_id",
            "physical_qubits", "readout_profile_id", "control_power_w",
            "cryogenic_load_w", "latency_s",
        ):
            payload.pop(key)
        result = assess_circuit_fab_bridge(payload)
        self.assertEqual(result.status, "BLOCKED_TARGET_MAPPING")

    def test_missing_process_window_blocks_manufacturing_claim(self):
        payload = complete_payload()
        payload.pop("process_window_id")
        result = assess_circuit_fab_bridge(payload)
        self.assertEqual(result.status, "BLOCKED_DEVICE_PROCESS")

    def test_cross_target_cost_is_rejected(self):
        payload = complete_payload()
        payload["uqpu_cost_target_id"] = "OTHER-TARGET"
        result = assess_circuit_fab_bridge(payload)
        self.assertEqual(result.status, "REJECTED_CONTEXT_MISMATCH")
        self.assertIn("uqpu_cost_target_id!=target_id", result.context_mismatches)

    def test_baseline_must_share_workload_quality_and_measurement_window(self):
        payload = complete_payload()
        payload["baseline_workload_contract_id"] = "OTHER-WORK"
        result = assess_circuit_fab_bridge(payload)
        self.assertEqual(result.status, "REJECTED_CONTEXT_MISMATCH")
        self.assertIn(
            "baseline_workload_contract_id!=workload_contract_id",
            result.context_mismatches,
        )

    def test_invalid_hash_and_yield_are_rejected(self):
        payload = complete_payload()
        payload["candidate_circuit_sha256"] = "not-a-hash"
        with self.assertRaises(ValueError):
            assess_circuit_fab_bridge(payload)
        payload = complete_payload()
        payload["yield_fraction"] = 1.2
        with self.assertRaises(ValueError):
            assess_circuit_fab_bridge(payload)

    def test_costs_must_be_finite_and_nonnegative(self):
        payload = complete_payload()
        payload["uqpu_cost_per_task_usd"] = float("nan")
        with self.assertRaises(ValueError):
            assess_circuit_fab_bridge(payload)
        payload = complete_payload()
        payload["provider_cost_per_task_usd"] = -1
        with self.assertRaises(ValueError):
            assess_circuit_fab_bridge(payload)

    def test_invalid_gate_counts_are_rejected(self):
        payload = complete_payload()
        payload["native_gate_counts"] = {"CX": -1}
        with self.assertRaises(ValueError):
            assess_circuit_fab_bridge(payload)


if __name__ == "__main__":
    unittest.main()
