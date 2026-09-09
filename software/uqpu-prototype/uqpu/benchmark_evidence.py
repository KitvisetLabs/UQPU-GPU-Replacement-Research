from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class EvidenceKind(str, Enum):
    MODEL_ONLY = "MODEL_ONLY"
    SIMULATION = "SIMULATION"
    DRY_RUN_ONLY = "DRY_RUN_ONLY"
    REAL_QPU = "REAL_QPU"


@dataclass(frozen=True)
class BenchmarkEvidence:
    workload_id: str
    provider_id: str
    classical_cost_per_task_usd: float
    quantum_total_cost_per_task_usd: float
    output_quality_pass: bool
    evidence_kind: EvidenceKind
    classical_runtime_seconds: float | None = None
    quantum_runtime_seconds: float | None = None
    input_prep_cost_usd: float = 0.0
    host_orchestration_cost_usd: float = 0.0
    retry_and_mitigation_cost_usd: float = 0.0
    output_reconstruction_cost_usd: float = 0.0

    def validate(self) -> None:
        vals = (
            self.classical_cost_per_task_usd,
            self.quantum_total_cost_per_task_usd,
            self.input_prep_cost_usd,
            self.host_orchestration_cost_usd,
            self.retry_and_mitigation_cost_usd,
            self.output_reconstruction_cost_usd,
        )
        if any(v < 0 for v in vals):
            raise ValueError("cost values must be non-negative")
        if self.classical_cost_per_task_usd <= 0:
            raise ValueError("classical cost/task must be positive")

    @property
    def advantage_ratio(self) -> float:
        self.validate()
        if self.quantum_total_cost_per_task_usd == 0:
            return float("inf")
        return self.classical_cost_per_task_usd / self.quantum_total_cost_per_task_usd

    @property
    def verified_win(self) -> bool:
        self.validate()
        return (
            self.evidence_kind == EvidenceKind.REAL_QPU
            and self.output_quality_pass
            and self.advantage_ratio > 1.0
        )

    @property
    def verified_100x(self) -> bool:
        return self.verified_win and self.advantage_ratio >= 100.0
