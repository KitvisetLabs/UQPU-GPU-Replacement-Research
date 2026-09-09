from __future__ import annotations
from dataclasses import dataclass
from enum import Enum


class Strategy(str, Enum):
    FUNCTIONAL_SUBSTITUTION = "functional_substitution"
    MINIMIZATION = "minimization"
    RECOVERY = "recovery"
    HYBRID = "hybrid"


@dataclass(frozen=True)
class MaterialCandidate:
    incumbent: str
    required_function: str
    biomass_feedstock: str
    candidate_material: str
    strategy: Strategy
    incumbent_cost_per_function: float
    candidate_cost_per_function: float
    critical_material_reduction_fraction: float
    evidence_level: str = "MODEL_ONLY"

    def validate(self) -> None:
        if self.incumbent_cost_per_function <= 0:
            raise ValueError("incumbent cost/function must be positive")
        if self.candidate_cost_per_function < 0:
            raise ValueError("candidate cost/function must be non-negative")
        if not 0 <= self.critical_material_reduction_fraction <= 1:
            raise ValueError("critical-material reduction must be in [0,1]")

    @property
    def cost_advantage(self) -> float:
        self.validate()
        if self.candidate_cost_per_function == 0:
            return float("inf")
        return self.incumbent_cost_per_function / self.candidate_cost_per_function

    @property
    def reaches_100x(self) -> bool:
        return self.cost_advantage >= 100


def allowed_strategy_for_elemental_replacement(
    target_element: str,
    *,
    biomass_contains_target_element: bool = False,
) -> tuple[Strategy, ...]:
    """Prevent accidental claims of chemical elemental transmutation."""
    base = (
        Strategy.FUNCTIONAL_SUBSTITUTION,
        Strategy.MINIMIZATION,
        Strategy.RECOVERY,
        Strategy.HYBRID,
    )
    # If the feedstock naturally contains the element, RECOVERY may recover it;
    # otherwise recovery refers to external waste/process streams using
    # biomass-derived recovery media, never creation of the element.
    return base
