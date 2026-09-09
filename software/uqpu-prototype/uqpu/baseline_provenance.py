from __future__ import annotations
from dataclasses import dataclass, asdict
import json
import platform
import sys
from typing import Any

from .optimization_baseline import ClassicalBaselineResult


@dataclass(frozen=True)
class BaselineProvenance:
    workload_id: str
    implementation: str
    python_version: str
    platform: str
    processor: str
    runtime_seconds: float
    states_evaluated: int
    objective: float
    cost_per_task_usd: float | None
    cost_method: str
    notes: str = ""

    def to_json(self) -> str:
        return json.dumps(asdict(self),indent=2,sort_keys=True)


def capture_baseline(
    workload_id: str,
    result: ClassicalBaselineResult,
    *,
    cost_per_task_usd: float | None = None,
    cost_method: str = "UNPRICED_LOCAL_RUNTIME",
    notes: str = "",
) -> BaselineProvenance:
    return BaselineProvenance(
        workload_id=workload_id,
        implementation=result.method,
        python_version=sys.version.split()[0],
        platform=platform.platform(),
        processor=platform.processor(),
        runtime_seconds=result.runtime_seconds,
        states_evaluated=result.states_evaluated,
        objective=result.objective,
        cost_per_task_usd=cost_per_task_usd,
        cost_method=cost_method,
        notes=notes,
    )
