from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class ClassicalRole(str, Enum):
    CPU = "CPU"
    GPU = "GPU"
    RAM = "RAM"
    VRAM = "VRAM"
    STORAGE = "STORAGE"


@dataclass(frozen=True)
class WorkloadContract:
    workload_id: str
    roles: tuple[ClassicalRole, ...]
    input_semantics: str
    output_semantics: str
    quality_metric: str
    latency_budget_seconds: float | None = None
    persistence_required: bool = False
    exactness_required: bool = False

    def validate(self) -> None:
        if not self.workload_id:
            raise ValueError("workload_id is required")
        if not self.roles:
            raise ValueError("at least one classical role is required")
        if not self.input_semantics or not self.output_semantics or not self.quality_metric:
            raise ValueError("contract semantics and quality metric are required")


def first_verified_win_candidates() -> tuple[WorkloadContract, ...]:
    return (
        WorkloadContract(
            "combinatorial_optimization",
            (ClassicalRole.CPU, ClassicalRole.GPU),
            "weighted discrete optimization instance",
            "feasible solution plus objective value",
            "objective_gap_to_best_known",
        ),
        WorkloadContract(
            "monte_carlo_like_estimation",
            (ClassicalRole.CPU, ClassicalRole.GPU),
            "distribution/model plus estimator query",
            "estimate plus uncertainty",
            "absolute_or_relative_error",
        ),
        WorkloadContract(
            "linear_algebra_subroutine",
            (ClassicalRole.GPU, ClassicalRole.VRAM),
            "structured matrix/vector problem",
            "task-specific scalar/vector observable",
            "task_specific_error",
        ),
        WorkloadContract(
            "stateful_checkpoint_workflow",
            (ClassicalRole.RAM, ClassicalRole.VRAM, ClassicalRole.STORAGE),
            "state transition sequence",
            "recoverable task state and final result",
            "recovery_correctness",
            persistence_required=True,
        ),
    )
