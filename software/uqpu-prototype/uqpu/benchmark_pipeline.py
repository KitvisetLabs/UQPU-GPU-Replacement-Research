from __future__ import annotations
from dataclasses import dataclass

from .benchmark_evidence import BenchmarkEvidence
from .state_accounting import StateAccounting
from .workload_contracts import WorkloadContract


@dataclass(frozen=True)
class BenchmarkRunPlan:
    contract: WorkloadContract
    provider_id: str
    backend_target: str
    shots: int
    classical_state: StateAccounting
    uqpu_state: StateAccounting
    evidence_target: str = "SIMULATION"

    def validate(self) -> None:
        self.contract.validate()
        if not self.provider_id or not self.backend_target:
            raise ValueError("provider and backend target are required")
        if self.shots<=0:
            raise ValueError("shots must be positive")
        self.classical_state.validate()
        self.uqpu_state.validate()


@dataclass(frozen=True)
class BenchmarkGate:
    contract_valid: bool
    output_quality_pass: bool
    real_qpu: bool
    economic_win: bool
    verified_100x: bool


def evaluate_gate(plan: BenchmarkRunPlan, evidence: BenchmarkEvidence) -> BenchmarkGate:
    plan.validate()
    return BenchmarkGate(
        contract_valid=True,
        output_quality_pass=evidence.output_quality_pass,
        real_qpu=evidence.evidence_kind.value=="REAL_QPU",
        economic_win=evidence.verified_win,
        verified_100x=evidence.verified_100x,
    )
