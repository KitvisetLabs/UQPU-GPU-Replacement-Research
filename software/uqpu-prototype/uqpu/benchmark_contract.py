from __future__ import annotations
from dataclasses import dataclass, asdict
import hashlib
import json
from typing import Any


@dataclass(frozen=True)
class OptimizationBenchmarkContract:
    workload_id: str
    instance_family: str
    instance_seed: int
    variable_count: int
    objective_sense: str = "minimize"
    quality_metric: str = "objective_value"
    required_relative_gap: float = 0.0

    def canonical_json(self) -> str:
        return json.dumps(asdict(self),sort_keys=True,separators=(",",":"))

    @property
    def contract_id(self) -> str:
        return hashlib.sha256(self.canonical_json().encode()).hexdigest()[:16]

    def accepts(self, candidate: float, reference: float) -> bool:
        if self.objective_sense != "minimize":
            raise NotImplementedError("only minimize is implemented")
        scale=max(abs(reference),1.0)
        return candidate <= reference + self.required_relative_gap*scale
