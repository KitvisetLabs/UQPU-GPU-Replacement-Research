from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MissionImpact:
    functional_coverage_gain: float = 0.0
    cost_reduction_leverage: float = 0.0
    uncertainty_reduction: float = 0.0
    cross_lane_enablement: float = 0.0
    evidence_maturity_gain: float = 0.0
    estimated_effort: float = 1.0

    def validate(self) -> None:
        values = (
            self.functional_coverage_gain,
            self.cost_reduction_leverage,
            self.uncertainty_reduction,
            self.cross_lane_enablement,
            self.evidence_maturity_gain,
        )
        if any(v < 0 for v in values):
            raise ValueError("mission-impact values must be non-negative")
        if self.estimated_effort <= 0:
            raise ValueError("estimated_effort must be positive")

    @property
    def score(self) -> float:
        self.validate()
        benefit = (
            self.functional_coverage_gain
            + self.cost_reduction_leverage
            + self.uncertainty_reduction
            + self.cross_lane_enablement
            + self.evidence_maturity_gain
        )
        return benefit / self.estimated_effort


@dataclass(frozen=True)
class MissionGateResult:
    advances_original_mission: bool
    reasons: tuple[str, ...]


def mission_gate(
    *,
    improves_function: bool = False,
    improves_cost: bool = False,
    improves_evidence: bool = False,
    improves_portability: bool = False,
    reduces_data_movement: bool = False,
    improves_manufacturability: bool = False,
    removes_blocker: bool = False,
) -> MissionGateResult:
    reasons = []
    if improves_function: reasons.append("functional_coverage")
    if improves_cost: reasons.append("cost_per_useful_task")
    if improves_evidence: reasons.append("evidence_maturity")
    if improves_portability: reasons.append("provider_portability")
    if reduces_data_movement: reasons.append("data_movement")
    if improves_manufacturability: reasons.append("manufacturability")
    if removes_blocker: reasons.append("blocker_reduction")
    return MissionGateResult(bool(reasons), tuple(reasons))
