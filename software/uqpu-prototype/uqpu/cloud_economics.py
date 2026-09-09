from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class CloudPricingKind(str, Enum):
    PER_SECOND = "PER_SECOND"
    PER_TASK_SHOT = "PER_TASK_SHOT"
    PER_GATE_SHOT = "PER_GATE_SHOT"
    PER_QPU_HOUR = "PER_QPU_HOUR"
    PER_TIME_INCREMENT = "PER_TIME_INCREMENT"


@dataclass(frozen=True)
class CloudPricingProfile:
    provider_id: str
    plan_name: str
    kind: CloudPricingKind
    currency: str = "USD"
    per_second: float = 0.0
    per_task: float = 0.0
    per_shot: float = 0.0
    per_one_qubit_gate_shot: float = 0.0
    per_two_qubit_gate_shot: float = 0.0
    minimum_program_price: float = 0.0
    per_qpu_hour: float = 0.0
    time_increment_seconds: float = 0.0
    per_time_increment: float = 0.0
    evidence_level: str = "OFFICIAL_PRICING_SNAPSHOT"
    source_url: str = ""
    snapshot_date: str = "2026-09"

    def validate(self) -> None:
        numeric = [
            self.per_second, self.per_task, self.per_shot,
            self.per_one_qubit_gate_shot, self.per_two_qubit_gate_shot,
            self.minimum_program_price, self.per_qpu_hour,
            self.time_increment_seconds, self.per_time_increment,
        ]
        if any(x < 0 for x in numeric):
            raise ValueError("pricing values must be non-negative")


@dataclass(frozen=True)
class CloudWorkloadUsage:
    useful_tasks: int = 1
    executions: int = 1
    shots_per_execution: int = 0
    runtime_seconds: float = 0.0
    one_qubit_gates: int = 0
    two_qubit_gates: int = 0

    def validate(self) -> None:
        if self.useful_tasks <= 0 or self.executions <= 0:
            raise ValueError("useful_tasks and executions must be positive")
        if self.shots_per_execution < 0 or self.runtime_seconds < 0:
            raise ValueError("shots/runtime must be non-negative")
        if self.one_qubit_gates < 0 or self.two_qubit_gates < 0:
            raise ValueError("gate counts must be non-negative")


def estimate_cloud_cost(profile: CloudPricingProfile, usage: CloudWorkloadUsage) -> float:
    profile.validate()
    usage.validate()

    if profile.kind == CloudPricingKind.PER_SECOND:
        return profile.per_second * usage.runtime_seconds

    if profile.kind == CloudPricingKind.PER_TASK_SHOT:
        return usage.executions * (
            profile.per_task + profile.per_shot * usage.shots_per_execution
        )

    if profile.kind == CloudPricingKind.PER_GATE_SHOT:
        raw = usage.executions * usage.shots_per_execution * (
            profile.per_one_qubit_gate_shot * usage.one_qubit_gates
            + profile.per_two_qubit_gate_shot * usage.two_qubit_gates
        )
        return max(profile.minimum_program_price * usage.executions, raw)

    if profile.kind == CloudPricingKind.PER_QPU_HOUR:
        return profile.per_qpu_hour * usage.runtime_seconds / 3600.0

    if profile.kind == CloudPricingKind.PER_TIME_INCREMENT:
        if profile.time_increment_seconds <= 0:
            raise ValueError("time_increment_seconds must be positive")
        import math
        increments = math.ceil(usage.runtime_seconds / profile.time_increment_seconds)
        return profile.per_time_increment * increments

    raise ValueError("unsupported pricing kind")


def cloud_cost_per_useful_task(profile: CloudPricingProfile, usage: CloudWorkloadUsage) -> float:
    return estimate_cloud_cost(profile, usage) / usage.useful_tasks
