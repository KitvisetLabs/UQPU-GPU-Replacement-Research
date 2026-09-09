from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
import json
from typing import Any


@dataclass(frozen=True)
class BenchmarkArtifact:
    contract_id: str
    implementation: str
    solver_class: str
    objective: float
    accepted: bool
    runtime_seconds: float
    evidence_level: str
    provider_id: str | None = None
    backend_target: str | None = None
    hardware: str | None = None
    peak_memory_bytes: int | None = None
    transfer_bytes: int | None = None
    energy_joules: float | None = None
    cost_per_useful_task: float | None = None
    currency: str | None = None
    notes: str = ""

    def canonical_json(self) -> str:
        return json.dumps(asdict(self), sort_keys=True, separators=(",", ":"))

    @property
    def artifact_id(self) -> str:
        return hashlib.sha256(self.canonical_json().encode()).hexdigest()[:20]

    def validate(self) -> None:
        if not self.contract_id or not self.implementation or not self.solver_class:
            raise ValueError("contract/implementation/solver_class are required")
        if self.runtime_seconds < 0:
            raise ValueError("runtime_seconds must be non-negative")
        for value in (self.peak_memory_bytes, self.transfer_bytes):
            if value is not None and value < 0:
                raise ValueError("byte measurements must be non-negative")
        for value in (self.energy_joules, self.cost_per_useful_task):
            if value is not None and value < 0:
                raise ValueError("energy/cost measurements must be non-negative")
