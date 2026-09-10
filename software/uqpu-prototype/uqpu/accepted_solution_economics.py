from __future__ import annotations

from dataclasses import dataclass
import math


def expected_independent_shots_to_success(success_probability: float) -> float:
    """Expected Bernoulli trials until one accepted result."""
    p = float(success_probability)
    if not math.isfinite(p) or not 0 < p <= 1:
        raise ValueError("success_probability must be finite and in (0,1]")
    return 1.0 / p


def shots_for_success_confidence(success_probability: float, confidence: float) -> int:
    """Minimum independent shots needed for >= confidence of >=1 success."""
    p = float(success_probability)
    c = float(confidence)
    if not math.isfinite(p) or not 0 < p <= 1:
        raise ValueError("success_probability must be finite and in (0,1]")
    if not math.isfinite(c) or not 0 < c < 1:
        raise ValueError("confidence must be finite and in (0,1)")
    if p == 1.0:
        return 1
    return max(1, math.ceil(math.log1p(-c) / math.log1p(-p)))


@dataclass(frozen=True)
class AcceptedSolutionCost:
    success_probability_per_shot: float
    variable_cost_per_shot: float
    fixed_cost_per_submission: float = 0.0
    shots_per_submission: int = 1

    def __post_init__(self) -> None:
        p = float(self.success_probability_per_shot)
        if not math.isfinite(p) or not 0 < p <= 1:
            raise ValueError("success_probability_per_shot must be in (0,1]")
        for name, value in (
            ("variable_cost_per_shot", self.variable_cost_per_shot),
            ("fixed_cost_per_submission", self.fixed_cost_per_submission),
        ):
            if not math.isfinite(value) or value < 0:
                raise ValueError(f"{name} must be finite and non-negative")
        if type(self.shots_per_submission) is not int or self.shots_per_submission < 1:
            raise ValueError("shots_per_submission must be a positive integer")

    @property
    def submission_success_probability(self) -> float:
        return 1.0 - (1.0 - self.success_probability_per_shot) ** self.shots_per_submission

    @property
    def submission_cost(self) -> float:
        return self.fixed_cost_per_submission + self.variable_cost_per_shot * self.shots_per_submission

    @property
    def expected_cost_per_accepted_solution(self) -> float:
        """Geometric-repeat expectation for independent identical submissions."""
        return self.submission_cost / self.submission_success_probability
