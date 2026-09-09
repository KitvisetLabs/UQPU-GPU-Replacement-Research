from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class StateStrategy(str, Enum):
    MATERIALIZE_CLASSICAL = "MATERIALIZE_CLASSICAL"
    RECOMPUTE = "RECOMPUTE"
    COMPRESS = "COMPRESS"
    CHECKPOINT = "CHECKPOINT"
    PROVIDER_STATE_REUSE = "PROVIDER_STATE_REUSE"
    HYBRID_CACHE = "HYBRID_CACHE"


@dataclass(frozen=True)
class StatePlan:
    strategy: StateStrategy
    bytes_materialized: int
    recompute_seconds: float
    persistence: bool
    notes: str = ""

    def validate(self) -> None:
        if self.bytes_materialized < 0:
            raise ValueError("bytes_materialized must be non-negative")
        if self.recompute_seconds < 0:
            raise ValueError("recompute_seconds must be non-negative")


def choose_lower_materialization(plans: tuple[StatePlan, ...]) -> StatePlan:
    if not plans:
        raise ValueError("at least one plan is required")
    for p in plans:
        p.validate()
    return min(plans, key=lambda p: (p.bytes_materialized, p.recompute_seconds))
