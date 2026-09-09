from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class GapStatus(str, Enum):
    ACHIEVABLE_NOW = "ACHIEVABLE_NOW"
    MODEL_ONLY = "MODEL_ONLY"
    SIMULATION_ONLY = "SIMULATION_ONLY"
    NOT_YET_DEMONSTRATED = "NOT_YET_DEMONSTRATED"
    RESOURCE_BLOCKED = "RESOURCE_BLOCKED"
    TOOL_BLOCKED = "TOOL_BLOCKED"
    DATA_BLOCKED = "DATA_BLOCKED"
    CURRENTLY_INFEASIBLE = "CURRENTLY_INFEASIBLE"
    ECONOMICALLY_NONVIABLE_CURRENT_ASSUMPTIONS = "ECONOMICALLY_NONVIABLE_CURRENT_ASSUMPTIONS"
    PHYSICALLY_INCOMPATIBLE_WITH_KNOWN_LAWS = "PHYSICALLY_INCOMPATIBLE_WITH_KNOWN_LAWS"


@dataclass(frozen=True)
class ResearchGap:
    gap_id: str
    objective: str
    status: GapStatus
    evidence: str
    blockers: tuple[str, ...]
    best_alternative: str
    unlock_criteria: tuple[str, ...]
    next_experiments: tuple[str, ...]

    def validate(self) -> None:
        if not self.gap_id.strip(): raise ValueError("gap_id is required")
        if not self.objective.strip(): raise ValueError("objective is required")
        if not self.blockers: raise ValueError("at least one blocker is required")
        if not self.unlock_criteria: raise ValueError("unlock criteria are required")
        if not self.next_experiments: raise ValueError("next experiments are required")
