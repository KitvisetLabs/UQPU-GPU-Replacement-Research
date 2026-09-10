from __future__ import annotations

from dataclasses import dataclass
import math


def _probability(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or not 0 < value <= 1:
        raise ValueError(f"{name} must be finite and in (0,1]")
    return value


def _nonnegative(value: float, name: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and non-negative")
    return value


@dataclass(frozen=True)
class TaskShotPricing:
    task_fee: float
    shot_fee: float
    minimum_shots: int = 1

    def __post_init__(self) -> None:
        _nonnegative(self.task_fee, "task_fee")
        _nonnegative(self.shot_fee, "shot_fee")
        if type(self.minimum_shots) is not int or self.minimum_shots < 1:
            raise ValueError("minimum_shots must be a positive integer")

    def submission_cost(self, shots: int) -> float:
        if type(shots) is not int or shots < self.minimum_shots:
            raise ValueError("shots must satisfy minimum_shots")
        return self.task_fee + self.shot_fee * shots


@dataclass(frozen=True)
class TimePricing:
    price_per_second: float
    fixed_submission_fee: float = 0.0

    def __post_init__(self) -> None:
        _nonnegative(self.price_per_second, "price_per_second")
        _nonnegative(self.fixed_submission_fee, "fixed_submission_fee")

    def submission_cost(self, billable_seconds: float) -> float:
        billable_seconds = _nonnegative(billable_seconds, "billable_seconds")
        return self.fixed_submission_fee + self.price_per_second * billable_seconds


@dataclass(frozen=True)
class QualityAdjustedCost:
    shots: int
    success_probability_per_shot: float
    success_probability_per_submission: float
    submission_cost: float
    expected_submissions_to_success: float
    expected_cost_per_accepted_solution: float


def task_shot_quality_adjusted_cost(
    success_probability_per_shot: float,
    shots: int,
    pricing: TaskShotPricing,
) -> QualityAdjustedCost:
    p = _probability(success_probability_per_shot, "success_probability_per_shot")
    if type(shots) is not int or shots < pricing.minimum_shots:
        raise ValueError("shots must satisfy pricing minimum")
    submission_success = 1.0 - (1.0 - p) ** shots
    submission_cost = pricing.submission_cost(shots)
    expected_submissions = 1.0 / submission_success
    return QualityAdjustedCost(
        shots=shots,
        success_probability_per_shot=p,
        success_probability_per_submission=submission_success,
        submission_cost=submission_cost,
        expected_submissions_to_success=expected_submissions,
        expected_cost_per_accepted_solution=submission_cost * expected_submissions,
    )


def best_task_shot_batch(
    success_probability_per_shot: float,
    pricing: TaskShotPricing,
    *,
    maximum_shots: int,
    minimum_submission_success: float | None = None,
) -> QualityAdjustedCost:
    p = _probability(success_probability_per_shot, "success_probability_per_shot")
    if type(maximum_shots) is not int or maximum_shots < pricing.minimum_shots:
        raise ValueError("maximum_shots must be >= minimum_shots")
    if minimum_submission_success is not None:
        minimum_submission_success = _probability(minimum_submission_success, "minimum_submission_success")

    candidates = []
    for shots in range(pricing.minimum_shots, maximum_shots + 1):
        row = task_shot_quality_adjusted_cost(p, shots, pricing)
        if minimum_submission_success is None or row.success_probability_per_submission >= minimum_submission_success:
            candidates.append(row)
    if not candidates:
        raise ValueError("no shot count satisfies the requested submission-success threshold")
    return min(candidates, key=lambda row: (row.expected_cost_per_accepted_solution, row.shots))


def time_priced_quality_adjusted_cost(
    success_probability_per_submission: float,
    billable_seconds: float,
    pricing: TimePricing,
) -> float:
    p = _probability(success_probability_per_submission, "success_probability_per_submission")
    return pricing.submission_cost(billable_seconds) / p
