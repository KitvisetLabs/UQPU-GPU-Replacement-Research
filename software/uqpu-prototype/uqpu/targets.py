from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CostTarget:
    gpu_cost_per_task: float
    target_advantage: float
    maximum_uqpu_cost_per_task: float


def solve_cost_target(gpu_cost_per_task: float, target_advantage: float) -> CostTarget:
    if gpu_cost_per_task <= 0:
        raise ValueError("gpu_cost_per_task must be positive")
    if target_advantage <= 0:
        raise ValueError("target_advantage must be positive")
    return CostTarget(
        gpu_cost_per_task=gpu_cost_per_task,
        target_advantage=target_advantage,
        maximum_uqpu_cost_per_task=gpu_cost_per_task / target_advantage,
    )


def target_ladder(gpu_cost_per_task: float) -> list[CostTarget]:
    return [
        solve_cost_target(gpu_cost_per_task, x)
        for x in (100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000)
    ]
