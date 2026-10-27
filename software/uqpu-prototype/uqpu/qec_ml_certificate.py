"""Conservative interval checks for tiny finite decoder-reference fixtures.

This module validates generic class-minimum intervals and a finite-candidate
oracle. It is not a QLDPC decoder, a branch-and-bound implementation, or a
reproduction of Banfi et al. (arXiv:2610.28008).
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Literal, Sequence

Outcome = Literal["SUCCESS", "FAILURE", "UNDECIDED"]
TRUE_CLASS = "TRUE"
COMPETING_CLASS = "COMPETING"


@dataclass(frozen=True)
class CostInterval:
    lower: float
    upper: float

    def validate(self) -> None:
        if isinstance(self.lower, bool) or isinstance(self.upper, bool):
            raise ValueError("interval bounds must be numeric, not booleans")
        try:
            lower = float(self.lower)
            upper = float(self.upper)
        except (TypeError, ValueError) as exc:
            raise ValueError("interval bounds must be numeric") from exc
        if not isfinite(lower) or not isfinite(upper):
            raise ValueError("interval bounds must be finite")
        if lower < 0 or upper < lower:
            raise ValueError("interval requires 0 <= lower <= upper")


@dataclass(frozen=True)
class AggregateCertificate:
    success: int
    failure: int
    undecided: int

    def validate(self) -> None:
        counts = (self.success, self.failure, self.undecided)
        if any(
            not isinstance(n, int) or isinstance(n, bool) or n < 0
            for n in counts
        ):
            raise ValueError("outcome counts must be non-negative integers")
        if sum(counts) <= 0:
            raise ValueError("at least one shot is required")

    @property
    def total(self) -> int:
        self.validate()
        return self.success + self.failure + self.undecided

    @property
    def logical_error_interval(self) -> tuple[float, float]:
        """Return [certified failures/N, (failures + undecided)/N]."""
        n = self.total
        return self.failure / n, (self.failure + self.undecided) / n


def classify_cost_intervals(
    true_class: CostInterval, competing_class: CostInterval
) -> Outcome:
    """Classify only when strict interval separation certifies the result.

    A tie or overlapping intervals remains UNDECIDED; it is never silently
    converted to success or failure.
    """
    true_class.validate()
    competing_class.validate()
    if true_class.upper < competing_class.lower:
        return "SUCCESS"
    if competing_class.upper < true_class.lower:
        return "FAILURE"
    return "UNDECIDED"


def exhaustive_class_minima(
    candidates: Sequence[tuple[str, float]],
) -> tuple[float, float]:
    """Exact tiny-instance oracle over a finite candidate list.

    Each candidate is labeled TRUE or COMPETING and has a non-negative cost.
    This is a generic finite oracle, not a syndrome/Pauli enumerator or a QLDPC
    decoder implementation.
    """
    if not candidates:
        raise ValueError("candidates must not be empty")
    true_costs: list[float] = []
    competing_costs: list[float] = []
    for logical_class, raw_cost in candidates:
        if logical_class not in (TRUE_CLASS, COMPETING_CLASS):
            raise ValueError("logical_class must be TRUE or COMPETING")
        if isinstance(raw_cost, bool):
            raise ValueError("candidate costs must be numeric, not booleans")
        try:
            cost = float(raw_cost)
        except (TypeError, ValueError) as exc:
            raise ValueError("candidate costs must be numeric") from exc
        if not isfinite(cost) or cost < 0:
            raise ValueError("candidate costs must be finite and non-negative")
        (true_costs if logical_class == TRUE_CLASS else competing_costs).append(
            cost
        )
    if not true_costs or not competing_costs:
        raise ValueError("both TRUE and COMPETING candidates are required")
    return min(true_costs), min(competing_costs)


def validate_certificate_against_exact(
    true_interval: CostInterval,
    competing_interval: CostInterval,
    exact_true_minimum: float,
    exact_competing_minimum: float,
) -> Outcome:
    """Check interval containment and return the conservative outcome.

    SUCCESS/FAILURE requires strict interval separation. This validates a
    generic interval contract, not the source paper's search algorithm.
    """
    true_interval.validate()
    competing_interval.validate()
    if isinstance(exact_true_minimum, bool) or isinstance(
        exact_competing_minimum, bool
    ):
        raise ValueError("exact minima must be numeric, not booleans")
    try:
        exact_true = float(exact_true_minimum)
        exact_competing = float(exact_competing_minimum)
    except (TypeError, ValueError) as exc:
        raise ValueError("exact minima must be numeric") from exc
    if (
        not isfinite(exact_true)
        or not isfinite(exact_competing)
        or exact_true < 0
        or exact_competing < 0
    ):
        raise ValueError("exact minima must be finite and non-negative")
    if not float(true_interval.lower) <= exact_true <= float(true_interval.upper):
        raise ValueError("true-class interval excludes the exact minimum")
    if not float(competing_interval.lower) <= exact_competing <= float(
        competing_interval.upper
    ):
        raise ValueError("competing-class interval excludes the exact minimum")
    return classify_cost_intervals(true_interval, competing_interval)
