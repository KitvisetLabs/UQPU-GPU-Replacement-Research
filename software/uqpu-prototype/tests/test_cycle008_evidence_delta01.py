from datetime import date
from decimal import Decimal
import unittest

from uqpu.cycle007_delta01 import measure_fresh_process_durability
from uqpu.cycle008_evidence_delta01 import (
    compare_deterministic_solver_restarts, cost_interval_per_accepted_output,
    plan_archive_integrity, rank_decisive_gates, seal_synthetic_request_receipt,
    validate_ai_cost_candidate, validate_calibration_certificate,
    validate_idempotent_replay, validate_io_claim, validate_material_measurement_record,
    validate_qos_semantic_certificate, validate_request_receipt_link,
)


class Cycle008EvidenceDelta01Tests(unittest.TestCase):
    def test_lane_a_exact_control_and_restart_sensitivity_are_separate(self):
        result = compare_deterministic_solver_restarts()
        self.assertTrue(result["exact_control"]["complete"])
        self.assertEqual(result["exact_control"]["states_evaluated"], 4096)
        self.assertEqual([x["restarts"] for x in result["solver_variants"]], [32, 128])
        self.assertTrue(all(x["gap_to_exact"] >= 0 for x in result["solver_variants"]))

    def test_lane_b_hash_link_and_replay_mutation_fail_closed(self):
        request = {"client_token": "SYNTH-008", "workload_sha256": "a" * 64, "shots": 16}
        envelope = seal_synthetic_request_receipt(request, {"state": "NOT_SUBMITTED", "task_id": None})
        self.assertEqual(validate_request_receipt_link(envelope), [])
        self.assertEqual(validate_idempotent_replay(request, dict(request)), [])
        self.assertIn("request_payload_changed_under_replay", validate_idempotent_replay(request, {**request, "shots": 32}))
        tampered = {**envelope, "provider_bill_id": "must-stay-null"}
        self.assertIn("physical_provider_fields_must_be_null", validate_request_receipt_link(tampered))

    def test_lane_c_fresh_process_is_not_mislabeled_cold_or_durable(self):
        uncontrolled = {"process_scope": "FRESH_PROCESS", "cache_state": "UNCONTROLLED",
                        "cache_control_verified": False, "device_flush_claim": False,
                        "power_loss_claim": False}
        self.assertEqual(validate_io_claim(uncontrolled), [])
        self.assertIn("cache_label_without_control", validate_io_claim({**uncontrolled, "cache_state": "COLD_CONTROLLED"}))
        result = measure_fresh_process_durability({"cycle": "008"}, repetitions=3)
        self.assertTrue(all(row["readback_sha256_matches"] for row in result["rows"]))
        self.assertEqual(result["platform_capabilities"]["cache_state"], "UNCONTROLLED")

    def test_lane_d_full_archive_plan_respects_byte_cap(self):
        result = plan_archive_integrity(expected_bytes=145_469_232, max_download_bytes=100_000_000, download_authorized=True)
        self.assertEqual(result["state"], "BLOCKED_RESOURCE_CAP")
        self.assertFalse(result["download_attempted"])
        self.assertIsNone(result["full_archive_sha256"])

    def test_lane_e_property_record_rejects_uncertainty_unit_mismatch(self):
        record = {"sample_lot_id": "SYN-LOT", "control_id": "SYN-CTRL", "measurand": "conductivity",
                  "unit_code": "S/m", "method_id": "SYN-METHOD", "calibration_certificate_id": "SYN-CAL",
                  "standard_uncertainty": 0.1, "uncertainty_unit_code": "S/m", "evidence_class": "SYNTHETIC"}
        self.assertEqual(validate_material_measurement_record(record), [])
        self.assertIn("uncertainty_unit_mismatch", validate_material_measurement_record({**record, "uncertainty_unit_code": "K"}))

    def test_lane_f_cost_intervals_fail_closed_on_currency_mix(self):
        rows = [{"lower": "1.2", "upper": "1.4", "currency": "USD", "unit_code": "USD"},
                {"lower": "0.5", "upper": "0.7", "currency": "USD", "unit_code": "USD"}]
        good = cost_interval_per_accepted_output(rows, currency="USD", accepted_outputs=2)
        self.assertEqual(good["total_interval"], ["1.7", "2.1"])
        self.assertEqual(good["per_accepted_output_interval"], ["0.85", "1.05"])
        bad = cost_interval_per_accepted_output([rows[0], {**rows[1], "currency": "EUR", "unit_code": "EUR"}], currency="USD", accepted_outputs=2)
        self.assertFalse(bad["complete"])
        self.assertIsNone(bad["total_interval"])

    def test_lane_g_calibration_certificate_expiry_and_uncertainty_are_required(self):
        cert = {"certificate_id": "SYN-CAL", "issuer": "Synthetic Lab", "instrument_id": "SYN-METER",
                "method_scope_id": "SYN-METHOD", "valid_from": "2026-01-01", "valid_until": "2026-12-31",
                "uncertainty_budget": [{"component": "repeatability", "standard_uncertainty": 0.2, "unit_code": "K"}]}
        self.assertEqual(validate_calibration_certificate(cert, as_of=date(2026, 9, 28)), [])
        self.assertIn("certificate_out_of_validity_window", validate_calibration_certificate({**cert, "valid_until": "2026-09-27"}, as_of=date(2026, 9, 28)))

    def test_lane_h_ranking_is_sensitivity_bound_and_not_authorization(self):
        result = rank_decisive_gates([
            {"gate_id": "BILL_RECEIPT", "effort_cost_sensitivity": {"low": 2, "base": 4, "high": 8}, "blocker_reduction_sensitivity": {"low": 6, "base": 8, "high": 10}},
            {"gate_id": "MATERIAL_SAMPLE", "effort_cost_sensitivity": {"low": 5, "base": 10, "high": 20}, "blocker_reduction_sensitivity": {"low": 2, "base": 4, "high": 8}},
        ])
        self.assertEqual(result["ranking"][0]["gate_id"], "BILL_RECEIPT")
        self.assertFalse(result["assumptions_are_measured"])
        self.assertFalse(result["capital_authorized"])
        self.assertIsNone(result["capital_amount"])

    def test_lane_ai_cost_rejects_leakage_and_incomplete_evidence(self):
        complete = {"train_example_ids": ["a", "b"], "held_out_example_ids": ["c"], "quality": 0.9,
                    "runtime_seconds": 3.0, "energy_joules": 10.0, "cost_amount": 0.02,
                    "cost_currency": "USD", "accepted_outputs": 1, "evidence_class": "SYNTHETIC",
                    "independent_verification": False}
        checked = validate_ai_cost_candidate(complete)
        self.assertTrue(checked["structurally_complete"])
        self.assertFalse(checked["candidate_claim_admissible"])
        self.assertIn("train_held_out_leakage", validate_ai_cost_candidate({**complete, "held_out_example_ids": ["b"]})["errors"])
        self.assertIn("energy_joules_missing", validate_ai_cost_candidate({**complete, "energy_joules": None})["errors"])

    def test_lane_qos_semantics_certificate_rejects_map_change(self):
        cert = {"circuit_sha256": "a" * 64, "grammar_subset_id": "ER6-FROZEN", "source_measurement_map": {0: 0, 1: 1},
                "candidate_measurement_map": {0: 0, 1: 1}, "logical_qubits": 6, "logical_depth": 24,
                "t_count": 0, "provider_task_id": None, "hardware_receipt": None}
        self.assertEqual(validate_qos_semantic_certificate(cert), [])
        changed = {**cert, "candidate_measurement_map": {0: 1, 1: 0}}
        self.assertIn("measurement_semantics_mismatch", validate_qos_semantic_certificate(changed))


if __name__ == "__main__":
    unittest.main()
