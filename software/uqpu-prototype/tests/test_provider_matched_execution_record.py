import unittest

from uqpu.provider_matched_execution_record import (
    SCHEMA,
    billable_cost_per_accepted_output,
    validate_execution_record,
)


def valid_record():
    ident = {
        "provider": "ExampleProvider",
        "target_id": "example-qpu-v1",
        "region": "region-1",
        "execution_route_id": "route-a",
        "workload_contract_id": "ER6-TEST-v1",
        "circuit_sha256": "a" * 64,
        "target_snapshot_sha256": "b" * 64,
        "target_snapshot_timestamp_utc": "2026-10-26T00:00:00Z",
    }
    return {
        "schema": SCHEMA,
        "evidence_class": "SYNTHETIC_TEST_FIXTURE",
        "execution": {
            **ident,
            "calibration_snapshot_sha256": "c" * 64,
            "calibration_timestamp_utc": "2026-10-26T00:00:00Z",
            "shots_requested": 100,
            "shots_completed": 100,
            "job_ids": ["synthetic-job-1"],
            "queue_latency_seconds": 1.0,
            "execution_latency_seconds": 2.0,
            "end_to_end_latency_seconds": 4.0,
            "host_preprocess_seconds": 0.2,
            "host_postprocess_seconds": 0.3,
            "host_peak_memory_bytes": 4096,
            "payload_bytes_sent": 128,
            "result_bytes_received": 256,
            "retry_count": 0,
            "energy_measurement_status": "NOT_MEASURED",
            "energy_joules": None,
        },
        "quality": {
            **ident,
            "calibration_snapshot_sha256": "c" * 64,
            "calibration_timestamp_utc": "2026-10-26T00:00:00Z",
            "success_probability": 0.8,
            "accepted_output_count": 2,
            "quality_metric_name": "accepted_quality_score",
            "quality_metric_value": 0.9,
            "quality_threshold": 0.8,
            "quality_direction": "MAX",
            "quality_gate_passed": True,
        },
        "billing": {
            **ident,
            "job_ids": ["synthetic-job-1"],
            "pricing_source_url": "https://provider.example/pricing",
            "pricing_observed_at_utc": "2026-10-26T00:00:00Z",
            "pricing_record_sha256": "d" * 64,
            "currency": "USD",
            "actual_billable_cost": 0.6,
        },
        "cost_per_accepted_useful_output": 0.3,
    }


class ProviderMatchedExecutionRecordTests(unittest.TestCase):
    def test_matching_record_passes_and_cost_is_derived(self):
        record = valid_record()
        self.assertEqual(validate_execution_record(record), [])
        self.assertAlmostEqual(billable_cost_per_accepted_output(record), 0.3)

    def test_cross_provider_or_target_price_join_fails(self):
        record = valid_record()
        record["billing"]["target_id"] = "other-target"
        errors = validate_execution_record(record)
        self.assertIn("identity_mismatch:target_id:billing", errors)

    def test_provider_identity_must_match(self):
        record = valid_record()
        record["billing"]["provider"] = "OtherProvider"
        errors = validate_execution_record(record)
        self.assertIn("identity_mismatch:provider:billing", errors)

    def test_target_snapshot_identity_must_match(self):
        record = valid_record()
        record["quality"]["target_snapshot_sha256"] = "e" * 64
        errors = validate_execution_record(record)
        self.assertIn("identity_mismatch:target_snapshot_sha256:quality", errors)

    def test_workload_and_circuit_must_match_probability_and_billing(self):
        record = valid_record()
        record["quality"]["circuit_sha256"] = "e" * 64
        errors = validate_execution_record(record)
        self.assertIn("identity_mismatch:circuit_sha256:quality", errors)

    def test_calibration_snapshot_must_match(self):
        record = valid_record()
        record["quality"]["calibration_snapshot_sha256"] = "f" * 64
        errors = validate_execution_record(record)
        self.assertIn("calibration_mismatch:calibration_snapshot_sha256", errors)

    def test_job_ids_must_match_billing_to_execution(self):
        record = valid_record()
        record["billing"]["job_ids"] = ["different-job"]
        errors = validate_execution_record(record)
        self.assertIn("job_ids_mismatch", errors)

    def test_invalid_probability_and_shot_counts_fail(self):
        record = valid_record()
        record["quality"]["success_probability"] = float("nan")
        record["execution"]["shots_completed"] = 101
        errors = validate_execution_record(record)
        self.assertIn("success_probability", errors)
        self.assertIn("shots_completed_exceeds_requested", errors)

    def test_non_https_pricing_source_and_negative_cost_fail(self):
        record = valid_record()
        record["billing"]["pricing_source_url"] = "http://provider.example/pricing"
        record["billing"]["actual_billable_cost"] = -1
        errors = validate_execution_record(record)
        self.assertIn("pricing_source_url", errors)
        self.assertIn("actual_billable_cost", errors)

    def test_zero_accepted_outputs_has_undefined_cost_not_zero_cost(self):
        record = valid_record()
        record["quality"]["accepted_output_count"] = 0
        record["quality"]["quality_metric_value"] = 0.2
        record["quality"]["quality_gate_passed"] = False
        record["cost_per_accepted_useful_output"] = None
        self.assertEqual(validate_execution_record(record), [])
        self.assertIsNone(billable_cost_per_accepted_output(record))

    def test_zero_accepted_outputs_rejects_numeric_cost_per_accepted_output(self):
        record = valid_record()
        record["quality"]["accepted_output_count"] = 0
        record["quality"]["quality_metric_value"] = 0.2
        record["quality"]["quality_gate_passed"] = False
        record["cost_per_accepted_useful_output"] = 0.0
        self.assertIn("undefined_cost_must_be_null", validate_execution_record(record))

    def test_quality_flag_must_follow_preregistered_threshold(self):
        record = valid_record()
        record["quality"]["quality_metric_value"] = 0.4
        record["quality"]["quality_gate_passed"] = True
        self.assertIn("quality_gate_inconsistent", validate_execution_record(record))

    def test_reported_cost_must_match_actual_billable_cost(self):
        record = valid_record()
        record["cost_per_accepted_useful_output"] = 0.4
        self.assertIn("cost_per_accepted_output_mismatch", validate_execution_record(record))

    def test_missing_fields_fail_closed(self):
        record = valid_record()
        del record["billing"]["pricing_record_sha256"]
        errors = validate_execution_record(record)
        self.assertIn("missing:billing.pricing_record_sha256", errors)


if __name__ == "__main__":
    unittest.main()
