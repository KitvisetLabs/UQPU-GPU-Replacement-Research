import dataclasses
import unittest

from uqpu.qaoa_comparison_contract import (
    QAOAEvidenceClass,
    QAOARunRecord,
    compare_matched_qaoa_runs,
)


def digest(ch="a"):
    return ch * 64


def record(method="direct", *, evidence=QAOAEvidenceClass.SIMULATION_ONLY, **overrides):
    values = dict(
        method_id=method,
        workload_contract_sha256=digest("a"),
        test_manifest_sha256=digest("b"),
        acceptance_contract_sha256=digest("c"),
        reference_certificate_sha256=digest("d"),
        provider_id="ibm",
        target_id="heron-test-target",
        target_config_sha256=digest("e"),
        evidence_class=evidence,
        total_shots=8192,
        optimizer_evaluations=120,
        repetitions=4,
        accepted_tasks=1200,
        quality_pass=True,
        qubits=21,
        two_qubit_gates=800,
        circuit_depth=120,
        host_compute_seconds=18.5,
        input_bytes=1024,
        output_bytes=512,
        peak_memory_bytes=1024 * 1024,
        reconstruction_seconds=0.4,
    )
    if evidence == QAOAEvidenceClass.SAVED_CALIBRATION_SIMULATION:
        values["calibration_snapshot_sha256"] = digest("f")
    if evidence == QAOAEvidenceClass.REAL_QPU:
        values.update(
            calibration_epoch_id="ibm-heron-cal-2026-10-27T01",
            pricing_snapshot_sha256=digest("9"),
            job_id="job-123",
            run_log_sha256=digest("8"),
            provider_cost_usd=2.0,
            host_compute_cost_usd=0.5,
            input_preparation_cost_usd=0.1,
            data_movement_cost_usd=0.1,
            mitigation_retry_cost_usd=0.2,
            reconstruction_cost_usd=0.1,
            energy_cost_usd=0.1,
            capital_allocation_cost_usd=0.1,
        )
    values.update(overrides)
    return QAOARunRecord(**values)


class QAOAComparisonContractTests(unittest.TestCase):
    def test_matched_simulation_is_comparable_but_not_economic_evidence(self):
        result = compare_matched_qaoa_runs(record(), record("higher_order_parity", qubits=32))
        self.assertTrue(result.matched)
        self.assertFalse(result.economic_claim_eligible)
        self.assertIsNone(result.baseline_to_candidate_cost_ratio)
        self.assertEqual(result.baseline_acceptance_probability, 1200 / 8192)

    def test_provider_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "provider_id"):
            compare_matched_qaoa_runs(record(), record("parity", provider_id="other"))

    def test_target_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "target_id"):
            compare_matched_qaoa_runs(record(), record("parity", target_id="other-target"))

    def test_pricing_snapshot_mismatch_is_rejected_on_real_qpu(self):
        a = record(evidence=QAOAEvidenceClass.REAL_QPU)
        b = record("parity", evidence=QAOAEvidenceClass.REAL_QPU, pricing_snapshot_sha256=digest("7"))
        with self.assertRaisesRegex(ValueError, "pricing_snapshot_sha256"):
            compare_matched_qaoa_runs(a, b)

    def test_real_qpu_cost_per_accepted_task_uses_all_components(self):
        a = record(evidence=QAOAEvidenceClass.REAL_QPU, accepted_tasks=4)
        b = record("parity", evidence=QAOAEvidenceClass.REAL_QPU, accepted_tasks=8,
                   provider_cost_usd=1.0, host_compute_cost_usd=0.25,
                   input_preparation_cost_usd=0.05, data_movement_cost_usd=0.05,
                   mitigation_retry_cost_usd=0.1, reconstruction_cost_usd=0.05,
                   energy_cost_usd=0.05, capital_allocation_cost_usd=0.05)
        result = compare_matched_qaoa_runs(a, b)
        self.assertTrue(result.economic_claim_eligible)
        self.assertAlmostEqual(result.baseline_cost_per_accepted_task_usd, 3.2 / 4)
        self.assertAlmostEqual(result.candidate_cost_per_accepted_task_usd, 1.6 / 8)
        self.assertAlmostEqual(result.baseline_to_candidate_cost_ratio, 4.0)

    def test_incomplete_cost_boundary_blocks_economic_claim(self):
        a = record(evidence=QAOAEvidenceClass.REAL_QPU)
        b = record("parity", evidence=QAOAEvidenceClass.REAL_QPU, energy_cost_usd=None)
        result = compare_matched_qaoa_runs(a, b)
        self.assertFalse(result.economic_claim_eligible)
        self.assertIsNone(result.candidate_cost_per_accepted_task_usd)

    def test_test_optimum_leakage_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "test optimum"):
            compare_matched_qaoa_runs(record(selection_used_test_optimum=True), record("parity"))

    def test_unequal_shot_budget_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "total_shots"):
            compare_matched_qaoa_runs(record(), record("parity", total_shots=4096))

    def test_saved_calibration_snapshot_must_match(self):
        a = record(evidence=QAOAEvidenceClass.SAVED_CALIBRATION_SIMULATION)
        b = record("parity", evidence=QAOAEvidenceClass.SAVED_CALIBRATION_SIMULATION,
                   calibration_snapshot_sha256=digest("7"))
        with self.assertRaisesRegex(ValueError, "calibration snapshot"):
            compare_matched_qaoa_runs(a, b)

    def test_real_qpu_requires_job_and_run_provenance(self):
        with self.assertRaisesRegex(ValueError, "run_log_sha256"):
            record(evidence=QAOAEvidenceClass.REAL_QPU, run_log_sha256=None).validate()

    def test_accepted_tasks_cannot_exceed_shots(self):
        with self.assertRaisesRegex(ValueError, "cannot exceed"):
            record(accepted_tasks=8193).validate()

    def test_unpriced_component_blocks_total_cost(self):
        a = record(evidence=QAOAEvidenceClass.REAL_QPU, unpriced_cost_components=("energy",))
        self.assertIsNone(a.all_in_cost_usd)

    def test_energy_requires_measurement_method(self):
        with self.assertRaisesRegex(ValueError, "measurement method"):
            record(energy_joules=4.2).validate()

    def test_record_validation_runs_for_property_access(self):
        with self.assertRaisesRegex(ValueError, "SHA-256"):
            dataclasses.replace(record(), workload_contract_sha256="bad").validate()

    def test_required_identity_fields_cannot_be_empty(self):
        with self.assertRaisesRegex(ValueError, "provider_id"):
            dataclasses.replace(record(), provider_id=" ").validate()


if __name__ == "__main__":
    unittest.main()
