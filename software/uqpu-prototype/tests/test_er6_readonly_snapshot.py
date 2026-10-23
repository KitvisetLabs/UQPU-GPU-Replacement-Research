import copy
import unittest

from uqpu.er6_readonly_snapshot import (
    EXPECTED_PROVIDER,
    EXPECTED_SCHEMA,
    EXPECTED_TARGET_ID,
    canonical_snapshot_bytes,
    snapshot_sha256,
    validate_snapshot,
)


def valid_snapshot():
    return {
        "schema": EXPECTED_SCHEMA,
        "provider": EXPECTED_PROVIDER,
        "target_id": EXPECTED_TARGET_ID,
        "captured_at_utc": "2026-10-23T10:00:00Z",
        "client_package_versions": {"qiskit": "2.5.2", "qiskit_ibm_runtime": "0.48.0"},
        "backend_status": {
            "operational": True, "status_message": "operational", "pending_jobs": 0,
            "status_observed_at_utc": "2026-10-23T09:59:00Z",
        },
        "target_structure": {
            "num_qubits": 3,
            "basis_gates": ["sx", "rz", "cx"],
            "instruction_names": ["measure", "cx", "rz", "sx"],
            "coupling_edges": [[1, 0], [0, 1], [1, 2]],
            "measurement_map": [0, 1, 2],
            "dynamic_circuit_capability_if_exposed": False,
            "qubit_indices": [2, 0, 1],
        },
        "timing_constraints": {
            "dt_seconds_if_exposed": None,
            "granularity_if_exposed": None,
            "minimum_length_if_exposed": None,
            "pulse_alignment_if_exposed": None,
            "acquire_alignment_if_exposed": None,
            "null_reasons": {
                "dt_seconds_if_exposed": "not exposed",
                "granularity_if_exposed": "not exposed",
                "minimum_length_if_exposed": "not exposed",
                "pulse_alignment_if_exposed": "not exposed",
                "acquire_alignment_if_exposed": "not exposed",
            },
        },
        "calibration_provenance": {
            "properties_last_update_utc_if_exposed": "2026-10-23T09:50:00Z",
            "target_last_update_utc_if_exposed": "2026-10-23T09:50:00Z",
            "per_instruction_error_and_duration_if_exposed": {"cx": {"error": 0.01, "duration_seconds": 3e-7}},
            "per_qubit_readout_error_and_t1_t2_frequency_if_exposed": None,
            "null_reasons": {"per_qubit_readout_error_and_t1_t2_frequency_if_exposed": "not exposed"},
        },
        "redaction_report": {"scan_completed": True, "forbidden_fields_detected": []},
    }


def validate(payload, route="2026-10-23T10:10:00Z", digest=None):
    return validate_snapshot(payload, route, digest or snapshot_sha256(payload))


class ReadonlyTargetSnapshotTests(unittest.TestCase):
    def test_valid_synthetic_snapshot_passes(self):
        self.assertEqual(validate(valid_snapshot()), [])

    def test_canonicalization_is_order_stable_and_direction_preserving(self):
        left = valid_snapshot()
        right = copy.deepcopy(left)
        right["target_structure"]["basis_gates"].reverse()
        right["target_structure"]["instruction_names"].reverse()
        right["target_structure"]["coupling_edges"].reverse()
        right["target_structure"]["qubit_indices"].reverse()
        self.assertEqual(canonical_snapshot_bytes(left), canonical_snapshot_bytes(right))
        self.assertIn(b"[0,1]", canonical_snapshot_bytes(left))
        self.assertIn(b"[1,0]", canonical_snapshot_bytes(left))

    def test_exact_provider_and_target_are_required(self):
        payload = valid_snapshot()
        payload["target_id"] = "IBM_KINGSTON"
        self.assertIn("target_id_mismatch", validate(payload))
        payload = valid_snapshot()
        payload["provider"] = "another provider"
        self.assertIn("provider_mismatch", validate(payload))

    def test_stale_snapshot_fails(self):
        self.assertIn("snapshot_stale", validate(valid_snapshot(), "2026-10-23T10:16:00Z"))

    def test_future_capture_and_future_calibration_fail(self):
        self.assertIn("capture_after_route_build", validate(valid_snapshot(), "2026-10-23T09:59:00Z"))
        payload = valid_snapshot()
        payload["calibration_provenance"]["target_last_update_utc_if_exposed"] = "2026-10-23T10:01:00Z"
        self.assertIn("calibration_after_capture:target_last_update_utc_if_exposed", validate(payload))

    def test_out_of_range_and_duplicate_directed_edges_fail(self):
        payload = valid_snapshot()
        payload["target_structure"]["coupling_edges"].append([0, 3])
        self.assertTrue(any(x.startswith("coupling_edge_out_of_range") for x in validate(payload)))
        payload = valid_snapshot()
        payload["target_structure"]["coupling_edges"].append([1, 0])
        self.assertIn("duplicate_coupling_edge:1->0", validate(payload))

    def test_digest_mutation_fails(self):
        payload = valid_snapshot()
        digest = snapshot_sha256(payload)
        payload["backend_status"]["status_message"] = "mutated"
        self.assertIn("snapshot_digest_mismatch", validate_snapshot(payload, "2026-10-23T10:10:00Z", digest))

    def test_forbidden_secret_field_and_secret_like_value_fail(self):
        payload = valid_snapshot()
        payload["api_token"] = "REDACTED"
        self.assertTrue(any(x.startswith("forbidden_key") for x in validate(payload)))
        payload = valid_snapshot()
        payload["backend_status"]["status_message"] = "Bearer secret-value"
        self.assertTrue(any(x.startswith("secret_like_value") for x in validate(payload)))

    def test_null_without_reason_fails_but_explained_null_passes(self):
        payload = valid_snapshot()
        payload["timing_constraints"]["null_reasons"].pop("dt_seconds_if_exposed")
        self.assertIn("missing_or_unexplained:timing_constraints.dt_seconds_if_exposed", validate(payload))

    def test_non_finite_number_fails(self):
        payload = valid_snapshot()
        payload["calibration_provenance"]["per_instruction_error_and_duration_if_exposed"]["cx"]["error"] = float("nan")
        self.assertIn("non_finite_number", validate_snapshot(payload, "2026-10-23T10:10:00Z", "0" * 64))

    def test_malformed_coupling_edge_fails(self):
        payload = valid_snapshot()
        payload["target_structure"]["coupling_edges"].append([0, 1, 2])
        self.assertTrue(any(x.startswith("malformed_coupling_edge") for x in validate(payload)))


if __name__ == "__main__":
    unittest.main()
