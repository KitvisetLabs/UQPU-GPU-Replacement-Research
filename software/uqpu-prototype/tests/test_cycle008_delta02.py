from copy import deepcopy
from datetime import date
import json
from pathlib import Path
import unittest

from uqpu.cycle008_delta02 import (
    DIMENSIONS, build_integrated_checkpoint, canonical_sha256,
    full_download_decision, rank_decisive_gates, validate_ai_candidate,
    validate_calibration_certificate, validate_cost_interval,
    validate_dimension_equation, validate_fictional_state,
    validate_material_measurement, validate_qos_certificate,
    validate_request_receipt, validate_solver_comparison,
    validate_storage_measurement,
)


ROOT = Path(__file__).resolve().parents[3]
ARTIFACT = ROOT / "benchmarks/results/cycle008-delta02-integrated-gates.json"


class Cycle008Delta02Tests(unittest.TestCase):
    def test_lane_a_rejects_missing_completion_and_hardware_extrapolation(self):
        row = {"fixture_id": "f", "solver_id": "s", "completion": "COMPLETE", "objective": 1, "runtime_ns": 1, "states_examined": 2}
        self.assertEqual(validate_solver_comparison([row]), [])
        broken = dict(row, completion=None, gpu_extrapolation=True)
        errors = validate_solver_comparison([broken])
        self.assertIn("row[0]:completion_missing", errors)
        self.assertIn("row[0]:hardware_extrapolation_forbidden", errors)

    def test_lane_b_hash_chain_and_idempotency_fail_closed(self):
        request = {"idempotency_key": "key", "submission_authorized": False}
        body = {"request_sha256": canonical_sha256(request), "idempotency_key": "key", "status": "SYNTHETIC"}
        receipt = dict(body, receipt_sha256=canonical_sha256(body))
        self.assertEqual(validate_request_receipt(request, receipt), [])
        receipt["idempotency_key"] = "other"
        self.assertIn("idempotency_replay_mismatch", validate_request_receipt(request, receipt))

    def test_lane_c_does_not_invent_cold_cache(self):
        record = {"platform": "linux", "filesystem": "ext4", "process_mode": "FRESH_PROCESS", "cache_control_attempted": False, "device_flush_attested": False, "power_loss_tested": False}
        self.assertEqual(validate_storage_measurement(record), [])
        self.assertIn("cache_label_requires_control", validate_storage_measurement(dict(record, cache_label="COLD")))

    def test_lane_d_full_download_and_checksum_are_separate_gates(self):
        blocked = full_download_decision(bytes_total=100, byte_limit=10, publisher_checksum="sha256:a", computed_checksum=None)
        self.assertEqual(blocked["state"], "BLOCKED")
        allowed = full_download_decision(bytes_total=10, byte_limit=10, publisher_checksum="sha256:a", computed_checksum=None)
        self.assertEqual(allowed["state"], "ALLOWED_NOT_VERIFIED")
        verified = full_download_decision(bytes_total=10, byte_limit=10, publisher_checksum="sha256:a", computed_checksum="sha256:a")
        self.assertEqual(verified["state"], "VERIFIED")

    def test_lane_e_requires_distinct_control_and_uncertainty(self):
        record = {"function_id": "conductivity", "sample_lot_id": "s", "control_lot_id": "c", "value": 1, "unit_code": "S/m", "calibration_id": "cal", "uncertainty": 0.1, "method_id": "m"}
        self.assertEqual(validate_material_measurement(record), [])
        errors = validate_material_measurement(dict(record, control_lot_id="s", uncertainty=-1))
        self.assertIn("sample_control_collision", errors)
        self.assertIn("uncertainty_invalid", errors)

    def test_lane_f_rejects_currency_and_denominator_faults(self):
        record = {"currency": "USD", "amount_unit": "USD", "lower": 1, "upper": 2, "accepted_output_count": 1, "accepted_output_provenance": "artifact://accepted"}
        self.assertEqual(validate_cost_interval(record), [])
        errors = validate_cost_interval(dict(record, amount_unit="THB", lower=3, upper=2, accepted_output_count=0))
        self.assertIn("currency_unit_mismatch", errors)
        self.assertIn("interval_inverted", errors)
        self.assertIn("accepted_output_count_invalid", errors)

    def test_lane_g_rejects_expiry_scope_and_nonindependence(self):
        certificate = {"certificate_id": "c", "scope_id": "scope", "valid_until": "2027-01-01", "uncertainty_budget": {"b": 1}, "issuer": "i", "reviewer": "r"}
        self.assertEqual(validate_calibration_certificate(certificate, as_of=date(2026, 10, 15), required_scope="scope"), [])
        broken = dict(certificate, scope_id="other", valid_until="2026-01-01", reviewer="i")
        errors = validate_calibration_certificate(broken, as_of=date(2026, 10, 15), required_scope="scope")
        self.assertIn("scope_mismatch", errors)
        self.assertIn("certificate_expired", errors)
        self.assertIn("issuer_reviewer_collision", errors)
        self.assertIn("valid_until_invalid", validate_calibration_certificate(
            {}, as_of=date(2026, 10, 15), required_scope="scope"
        ))

    def test_lane_h_ranking_is_deterministic_and_capital_not_inferred(self):
        ranked = rank_decisive_gates([
            {"gate_id": "b", "sensitivity_abs": 1, "evidence_gap": "x", "falsifier": "y"},
            {"gate_id": "a", "sensitivity_abs": 2, "evidence_gap": "x", "falsifier": "y"},
        ])
        self.assertEqual([row["gate_id"] for row in ranked], ["a", "b"])
        checkpoint = build_integrated_checkpoint()
        self.assertIsNone(checkpoint["capital_amount"])
        self.assertFalse(checkpoint["owner_authorization"])

    def test_fnd_eqn_requires_explicit_exact_dimensions(self):
        zero = {axis: "0" for axis in DIMENSIONS}
        term = {"quantity_kind": "count", "unit_code": "1", "dimension_vector": zero}
        self.assertEqual(validate_dimension_equation([term, deepcopy(term)]), [])
        broken = deepcopy(term)
        broken["dimension_vector"]["time"] = "1"
        self.assertIn("equation_dimension_mismatch", validate_dimension_equation([term, broken]))

    def test_scm_is_fictional_conserved_and_nonhuman(self):
        record = {"domain": "FICTIONAL_PROTOCOL", "real_world_coupling": None, "human_study_authorized": False, "consent_state": "NOT_APPLICABLE_FICTIONAL", "quantities": {"inputs": [1], "outputs": [1]}}
        self.assertEqual(validate_fictional_state(record), [])
        broken = dict(record, real_world_coupling="claimed", human_study_authorized=True, quantities={"inputs": [1], "outputs": [2]})
        errors = validate_fictional_state(broken)
        self.assertIn("real_world_coupling_must_be_null", errors)
        self.assertIn("human_study_must_be_disabled", errors)
        self.assertIn("fictional_conservation_failed", errors)

    def test_ai_cost_rejects_leakage_and_incomplete_economics(self):
        candidate = {"candidate_id": "c", "train_hash": "a", "heldout_hash": "b", "quality": 1, "runtime_ns": 1, "energy_j": 1, "cost": 1}
        self.assertEqual(validate_ai_candidate(candidate), [])
        broken = dict(candidate, heldout_hash="a", energy_j=None)
        errors = validate_ai_candidate(broken)
        self.assertIn("train_heldout_leakage", errors)
        self.assertIn("energy_j_missing", errors)

    def test_qos_rejects_semantic_and_provider_evidence_mixing(self):
        certificate = {"contract_id": "ER6", "source_semantics_sha256": "a", "lowered_semantics_sha256": "a", "logical_qubits": 1, "two_qubit_gates": 1, "measurements": 1, "provider_execution_id": None, "provider_cost": None}
        self.assertEqual(validate_qos_certificate(certificate), [])
        errors = validate_qos_certificate(dict(certificate, lowered_semantics_sha256="b", provider_cost=1))
        self.assertIn("semantic_equivalence_failed", errors)
        self.assertIn("provider_fields_must_be_null", errors)

    def test_committed_artifact_equals_builder(self):
        artifact = json.loads(ARTIFACT.read_text(encoding="utf-8"))
        self.assertEqual(artifact, build_integrated_checkpoint())
        self.assertEqual(set(artifact["lanes"]), {"A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT"})
        self.assertTrue(artifact["all_synthetic_gates_pass"])
        self.assertFalse(artifact["provider_submission_authorized"])


if __name__ == "__main__":
    unittest.main()
