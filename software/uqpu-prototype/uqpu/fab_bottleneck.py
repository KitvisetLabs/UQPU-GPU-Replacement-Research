from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

from .fab_flow import ProcessStep


@dataclass(frozen=True)
class StepImpact:
    name: str
    cost_share: float
    yield_loss: float
    time_share: float
    energy_share: float


def rank_step_impacts(steps: Iterable[ProcessStep]) -> list[StepImpact]:
    steps = tuple(steps)
    if not steps:
        raise ValueError("at least one process step is required")
    for s in steps:
        s.validate()

    total_cost = sum(s.cost_per_wafer_usd for s in steps) or 1.0
    total_time = sum(s.cycle_time_seconds for s in steps) or 1.0
    total_energy = sum(s.energy_kwh_per_wafer for s in steps) or 1.0

    impacts = [
        StepImpact(
            name=s.name,
            cost_share=s.cost_per_wafer_usd / total_cost,
            yield_loss=1.0 - s.step_yield,
            time_share=s.cycle_time_seconds / total_time,
            energy_share=s.energy_kwh_per_wafer / total_energy,
        )
        for s in steps
    ]
    return sorted(
        impacts,
        key=lambda x: (x.cost_share + x.yield_loss + x.time_share + x.energy_share),
        reverse=True,
    )
