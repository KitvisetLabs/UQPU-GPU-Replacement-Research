"""Fail-closed evidence contract for matched QAOA encoding comparisons.

This module audits comparisons; it does not implement parity encoding or run a QPU.
A successful audit means records are comparable, not that the candidate is better.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math
import re


_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_COST_FIELDS = (
    "provider_cost_usd",
    "host_compute_cost_usd",
    "input_preparation_cost_usd",
    "data_movement_cost_usd",
    "mitigation_retry_cost_usd",
    "reconstruction_cost_usd",
    "energy_cost_usd",
    "capital_allocation_cost_usd",
)


class QAOAEvidenceClass(str, Enum):
    MODEL_ONLY = "MODEL_ONLY"
    SIMULATION_ONLY = "SIMULATION_ONLY"
    SAVED_CALIBRATION_SIMULATION = "SAVED_CALIBRATION_SIMULATION"
    REAL_QPU = "REAL_QPU"


@dataclass(frozen=True)
class QAOARunRecord:
    """One method's result on a frozen workload/test manifest and target.

    Cost components use USD for the same accounting boundary. Use 0.0 only when
    a component is explicitly inapplicable; use None or unpriced_cost_components
    when it is unknown. accepted_tasks counts outputs meeting the same frozen
    acceptance contract, not merely jobs that executed successfully.
    """

    method_id: str
    workload_contract_sha256: str
    test_manifest_sha256: str
    acceptance_contract_sha256: str
    reference_certificate_sha256: str
    provider_id: str
    target_id: str
    target_config_sha256: str
    evidence_class: QAOAEvidenceClass
    total_shots: int
    optimizer_evaluations: int
    repetitions: int
    accepted_tasks: int
    quality_pass: bool
    qubits: int
    two_qubit_gates: int
    circuit_depth: int
    host_compute_seconds: float
    input_bytes: int
    output_bytes: int
    peak_memory_bytes: int
    reconstruction_seconds: float
    retries: int = 0
    selection_used_test_optimum: bool = False
    calibration_snapshot_sha256: str | None = None
    calibration_epoch_id: str | None = None
    pricing_snapshot_sha256: str | None = None
    job_id: str | None = None
    run_log_sha256: str | None = None
    energy_joules: float | None = None
    energy_measurement_method: str | None = None
    unpriced_cost_components: tuple[str, ...] = ()
    provider_cost_usd: float | None = None
    host_compute_cost_usd: float | None = None
    input_preparation_cost_usd: float | None = None
    data_movement_cost_usd: float | None = None
    mitigation_retry_cost_usd: float | None = None
    reconstruction_cost_usd: float | None = None
    energy_cost_usd: float | None = None
    capital_allocation_cost_usd: float | None = None

    def validate(self) -> None:
        for name in ("method_id", "provider_id", "target_id"):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} must be a non-empty string")
        for name in ("calibration_epoch_id", "job_id"):
            value = getattr(self, name)
            if value is not None and (not isinstance(value, str) or not value.strip()):
                raise ValueError(f"{name} must be a non-empty string when supplied")
        for name in (
            "workload_contract_sha256", "test_manifest_sha256",
            "acceptance_contract_sha256", "reference_certificate_sha256",
            "target_config_sha256",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not _SHA256.fullmatch(value):
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")
        for name in ("calibration_snapshot_sha256", "pricing_snapshot_sha256", "run_log_sha256"):
            value = getattr(self, name)
            if value is not None and (not isinstance(value, str) or not _SHA256.fullmatch(value)):
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest when supplied")
        if not isinstance(self.evidence_class, QAOAEvidenceClass):
            raise ValueError("evidence_class must be a QAOAEvidenceClass")
        for name in ("total_shots", "optimizer_evaluations", "repetitions", "qubits"):
            value = getattr(self, name)
            if type(value) is not int or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        for name in ("accepted_tasks", "two_qubit_gates", "circuit_depth", "input_bytes", "output_bytes", "peak_memory_bytes", "retries"):
            value = getattr(self, name)
            if type(value) is not int or value < 0:
                raise ValueError(f"{name} must be a non-negative integer")
        if self.accepted_tasks > self.total_shots:
            raise ValueError("accepted_tasks cannot exceed total_shots")
        for name in ("quality_pass", "selection_used_test_optimum"):
            if type(getattr(self, name)) is not bool:
                raise ValueError(f"{name} must be boolean")
        for name in ("host_compute_seconds", "reconstruction_seconds"):
            value = float(getattr(self, name))
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and non-negative")
        if self.energy_joules is not None:
            if not math.isfinite(float(self.energy_joules)) or self.energy_joules < 0:
                raise ValueError("energy_joules must be finite and non-negative")
            if not isinstance(self.energy_measurement_method, str) or not self.energy_measurement_method.strip():
                raise ValueError("energy measurement method is required when energy_joules is supplied")
        for name in _COST_FIELDS:
            value = getattr(self, name)
            if value is not None and (not math.isfinite(float(value)) or value < 0):
                raise ValueError(f"{name} must be finite and non-negative when supplied")
        if any(not isinstance(x, str) or not x.strip() for x in self.unpriced_cost_components):
            raise ValueError("unpriced_cost_components must contain non-empty strings")
        if self.evidence_class == QAOAEvidenceClass.SAVED_CALIBRATION_SIMULATION and not self.calibration_snapshot_sha256:
            raise ValueError("saved-calibration simulation requires calibration_snapshot_sha256")
        if self.evidence_class == QAOAEvidenceClass.REAL_QPU:
            required = ("pricing_snapshot_sha256", "calibration_epoch_id", "job_id", "run_log_sha256")
            missing = [name for name in required if not getattr(self, name)]
            if missing:
                raise ValueError("REAL_QPU records require: " + ", ".join(missing))

    @property
    def accepted_task_probability(self) -> float:
        self.validate()
        return self.accepted_tasks / self.total_shots

    @property
    def all_in_cost_usd(self) -> float | None:
        self.validate()
        if self.unpriced_cost_components:
            return None
        values = [getattr(self, name) for name in _COST_FIELDS]
        if any(value is None for value in values):
            return None
        return sum(float(value) for value in values)

    @property
    def cost_per_accepted_task_usd(self) -> float | None:
        total = self.all_in_cost_usd
        if total is None or not self.quality_pass or self.accepted_tasks == 0:
            return None
        return total / self.accepted_tasks


@dataclass(frozen=True)
class QAOAComparisonAudit:
    baseline_method_id: str
    candidate_method_id: str
    matched: bool
    evidence_class: QAOAEvidenceClass
    baseline_acceptance_probability: float
    candidate_acceptance_probability: float
    economic_claim_eligible: bool
    baseline_cost_per_accepted_task_usd: float | None
    candidate_cost_per_accepted_task_usd: float | None
    baseline_to_candidate_cost_ratio: float | None


def compare_matched_qaoa_runs(
    baseline: QAOARunRecord, candidate: QAOARunRecord
) -> QAOAComparisonAudit:
    """Require paired inputs, output contract, resource budget and target identity.

    This rejects test-optimum leakage and cross-provider/target price-probability
    mixing. It never upgrades simulation or model records into real-QPU evidence.
    """
    baseline.validate()
    candidate.validate()
    if baseline.method_id == candidate.method_id:
        raise ValueError("baseline and candidate method_id must differ")
    paired_fields = (
        "workload_contract_sha256", "test_manifest_sha256",
        "acceptance_contract_sha256", "reference_certificate_sha256",
        "provider_id", "target_id", "target_config_sha256", "evidence_class",
        "total_shots", "optimizer_evaluations", "repetitions",
    )
    mismatches = [name for name in paired_fields if getattr(baseline, name) != getattr(candidate, name)]
    if mismatches:
        raise ValueError("unmatched QAOA comparison fields: " + ", ".join(mismatches))
    if baseline.selection_used_test_optimum or candidate.selection_used_test_optimum:
        raise ValueError("test optimum/reference may be used for evaluation, not parameter selection")
    if baseline.evidence_class == QAOAEvidenceClass.SAVED_CALIBRATION_SIMULATION:
        if baseline.calibration_snapshot_sha256 != candidate.calibration_snapshot_sha256:
            raise ValueError("saved-calibration comparisons require the same calibration snapshot")
    if baseline.evidence_class == QAOAEvidenceClass.REAL_QPU:
        for name in ("pricing_snapshot_sha256", "calibration_epoch_id"):
            if getattr(baseline, name) != getattr(candidate, name):
                raise ValueError(f"REAL_QPU comparisons require matching {name}")
    baseline_cost = baseline.cost_per_accepted_task_usd
    candidate_cost = candidate.cost_per_accepted_task_usd
    eligible = (
        baseline.evidence_class == QAOAEvidenceClass.REAL_QPU
        and baseline.quality_pass and candidate.quality_pass
        and baseline_cost is not None and candidate_cost is not None
    )
    ratio = None
    if eligible and candidate_cost is not None and candidate_cost > 0:
        ratio = baseline_cost / candidate_cost  # type: ignore[operator]
    return QAOAComparisonAudit(
        baseline_method_id=baseline.method_id,
        candidate_method_id=candidate.method_id,
        matched=True,
        evidence_class=baseline.evidence_class,
        baseline_acceptance_probability=baseline.accepted_task_probability,
        candidate_acceptance_probability=candidate.accepted_task_probability,
        economic_claim_eligible=eligible,
        baseline_cost_per_accepted_task_usd=baseline_cost,
        candidate_cost_per_accepted_task_usd=candidate_cost,
        baseline_to_candidate_cost_ratio=ratio,
    )
