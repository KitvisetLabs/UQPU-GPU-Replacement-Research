from __future__ import annotations
from dataclasses import dataclass

from .benchmark_evidence import BenchmarkEvidence
from .output_accounting import (
    OutputAccountingAudit,
    OutputMeasurement,
    audit_output_accounting,
)
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
    output_measurement: OutputMeasurement | None = None

    def validate(self) -> None:
        self.contract.validate()
        if not self.provider_id or not self.backend_target:
            raise ValueError("provider and backend target are required")
        if self.shots <= 0:
            raise ValueError("shots must be positive")
        self.classical_state.validate()
        self.uqpu_state.validate()

        output_contract = self.contract.output_information
        if output_contract is None:
            if self.output_measurement is not None:
                raise ValueError(
                    "output_measurement requires a declared output_information contract"
                )
            return
        if self.output_measurement is None:
            raise ValueError(
                "output_measurement is required when output_information is declared"
            )
        audit = audit_output_accounting(output_contract, self.output_measurement)
        if audit.fixed_width_label_status == "BELOW_FLOOR_REQUIRES_REVIEW":
            raise ValueError(
                "measured output payload is below the declared fixed-width label floor"
            )
        if audit.error_budget_status == "FAIL":
            raise ValueError("measured output error exceeds the declared contract budget")


@dataclass(frozen=True)
class BenchmarkGate:
    contract_valid: bool
    output_quality_pass: bool
    real_qpu: bool
    economic_win: bool
    verified_100x: bool
    output_accounting: OutputAccountingAudit | None = None


def evaluate_gate(plan: BenchmarkRunPlan, evidence: BenchmarkEvidence) -> BenchmarkGate:
    plan.validate()
    audit = None
    if plan.contract.output_information is not None and plan.output_measurement is not None:
        audit = audit_output_accounting(plan.contract.output_information, plan.output_measurement)
    return BenchmarkGate(
        contract_valid=True,
        output_quality_pass=evidence.output_quality_pass,
        real_qpu=evidence.evidence_kind.value == "REAL_QPU",
        economic_win=evidence.verified_win,
        verified_100x=evidence.verified_100x,
        output_accounting=audit,
    )
