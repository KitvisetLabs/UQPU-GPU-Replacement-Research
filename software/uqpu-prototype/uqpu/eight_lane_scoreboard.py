from __future__ import annotations
from dataclasses import dataclass


LANES = ("A","B","C","D","E","F","G","H")


@dataclass(frozen=True)
class LaneProgress:
    lane: str
    artifact_count: int
    blocked_count: int
    evidence_points: float
    mission_impact_points: float

    def validate(self) -> None:
        if self.lane not in LANES:
            raise ValueError("unknown lane")
        if self.artifact_count < 0 or self.blocked_count < 0:
            raise ValueError("counts must be non-negative")
        if self.evidence_points < 0 or self.mission_impact_points < 0:
            raise ValueError("scores must be non-negative")


def validate_complete_cycle(rows: tuple[LaneProgress, ...]) -> None:
    seen={r.lane for r in rows}
    for r in rows:
        r.validate()
    if seen != set(LANES):
        missing=set(LANES)-seen
        extra=seen-set(LANES)
        raise ValueError(f"cycle must cover A-H; missing={sorted(missing)} extra={sorted(extra)}")
