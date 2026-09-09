from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, List


@dataclass(frozen=True)
class SensitivityPoint:
    parameter: str
    value: float
    uqpu_cost_per_task: float
    gpu_cost_per_task: float
    cost_advantage: float


def sweep(
    parameter: str,
    values: Iterable[float],
    evaluator: Callable[[float], tuple[float, float]],
) -> List[SensitivityPoint]:
    points: List[SensitivityPoint] = []
    for value in values:
        uqpu_cost, gpu_cost = evaluator(float(value))
        if uqpu_cost <= 0 or gpu_cost < 0:
            raise ValueError("cost evaluator returned invalid costs")
        points.append(
            SensitivityPoint(
                parameter=parameter,
                value=float(value),
                uqpu_cost_per_task=uqpu_cost,
                gpu_cost_per_task=gpu_cost,
                cost_advantage=gpu_cost / uqpu_cost,
            )
        )
    return points
