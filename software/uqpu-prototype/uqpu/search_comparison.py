"""Fail-closed audit contract for matched scientific equation-search runs.

This module validates comparison metadata only. It does not decide whether an
equation is true, whether a fitted model is causal, or whether a new physical
law has been discovered. Resource caps must be identical across compared runs;
actual resource use is recorded separately. Direct cost should include model
serving/fine-tuning, evaluator compute, storage, retries and independent replay.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from numbers import Real
from typing import Sequence


def _finite_nonnegative(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a real number or None")
    numeric = float(value)
    if not math.isfinite(numeric) or numeric < 0:
        raise ValueError(f"{name} must be finite and >= 0")
    return numeric


def _nonnegative_int(name: str, value: object) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


@dataclass(frozen=True)
class SearchBudget:
    """Declared comparison caps; None means the quantity is not bounded/measured."""
    max_wall_seconds: float
    max_evaluator_calls: int
    max_generated_tokens: int
    max_energy_joules: float | None = None
    max_direct_cost_usd: float | None = None

    def validate(self) -> None:
        if _finite_nonnegative("max_wall_seconds", self.max_wall_seconds) <= 0:
            raise ValueError("max_wall_seconds must be > 0")
        if _nonnegative_int("max_evaluator_calls", self.max_evaluator_calls) <= 0:
            raise ValueError("max_evaluator_calls must be > 0")
        if _nonnegative_int("max_generated_tokens", self.max_generated_tokens) <= 0:
            raise ValueError("max_generated_tokens must be > 0")
        for name in ("max_energy_joules", "max_direct_cost_usd"):
            value = getattr(self, name)
            if value is not None:
                _finite_nonnegative(name, value)

    def comparison_key(self) -> tuple[float, int, int, float | None, float | None]:
        self.validate()
        return (
            float(self.max_wall_seconds),
            self.max_evaluator_calls,
            self.max_generated_tokens,
            None if self.max_energy_joules is None else float(self.max_energy_joules),
            None if self.max_direct_cost_usd is None else float(self.max_direct_cost_usd),
        )


@dataclass(frozen=True)
class SearchRun:
    method_id: str
    benchmark_id: str
    dataset_digest: str
    train_digest: str
    validation_digest: str
    heldout_digest: str
    budget: SearchBudget
    actual_wall_seconds: float
    actual_evaluator_calls: int
    actual_generated_tokens: int
    energy_joules: float | None
    direct_cost_usd: float | None
    candidate_count: int
    accepted_useful_model_count: int
    best_heldout_error: float | None
    constraint_violating_candidate_count: int
    accepted_model_constraint_violations: int
    false_discovery_count: int | None
    independent_replay_count: int

    def validate(self) -> None:
        for name in (
            "method_id", "benchmark_id", "dataset_digest",
            "train_digest", "validation_digest", "heldout_digest",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} is required")
        splits = (self.train_digest, self.validation_digest, self.heldout_digest)
        if len(set(splits)) != 3:
            raise ValueError("train, validation and held-out digests must be distinct")
        self.budget.validate()
        wall = _finite_nonnegative("actual_wall_seconds", self.actual_wall_seconds)
        calls = _nonnegative_int("actual_evaluator_calls", self.actual_evaluator_calls)
        tokens = _nonnegative_int("actual_generated_tokens", self.actual_generated_tokens)
        candidates = _nonnegative_int("candidate_count", self.candidate_count)
        accepted = _nonnegative_int(
            "accepted_useful_model_count", self.accepted_useful_model_count
        )
        violating_candidates = _nonnegative_int(
            "constraint_violating_candidate_count", self.constraint_violating_candidate_count
        )
        accepted_violations = _nonnegative_int(
            "accepted_model_constraint_violations", self.accepted_model_constraint_violations
        )
        if self.false_discovery_count is None:
            false_discoveries = None
        else:
            false_discoveries = _nonnegative_int(
                "false_discovery_count", self.false_discovery_count
            )
        replays = _nonnegative_int("independent_replay_count", self.independent_replay_count)
        if wall > self.budget.max_wall_seconds:
            raise ValueError("actual wall time exceeds the declared cap")
        if calls > self.budget.max_evaluator_calls:
            raise ValueError("actual evaluator calls exceed the declared cap")
        if tokens > self.budget.max_generated_tokens:
            raise ValueError("actual generated tokens exceed the declared cap")
        for name in ("energy_joules", "direct_cost_usd"):
            value = getattr(self, name)
            if value is not None:
                _finite_nonnegative(name, value)
        if self.budget.max_energy_joules is not None:
            if self.energy_joules is None:
                raise ValueError("energy cap declared but energy use is unknown")
            if self.energy_joules > self.budget.max_energy_joules:
                raise ValueError("actual energy exceeds the declared cap")
        if self.budget.max_direct_cost_usd is not None:
            if self.direct_cost_usd is None:
                raise ValueError("direct-cost cap declared but direct cost is unknown")
            if self.direct_cost_usd > self.budget.max_direct_cost_usd:
                raise ValueError("actual direct cost exceeds the declared cap")
        if violating_candidates > candidates:
            raise ValueError("constraint-violating candidates cannot exceed candidates")
        if accepted > candidates:
            raise ValueError("accepted useful models cannot exceed candidates")
        if false_discoveries is not None:
            if false_discoveries > candidates:
                raise ValueError("false discoveries cannot exceed candidates")
            if accepted + false_discoveries > candidates:
                raise ValueError("accepted models and false discoveries cannot overlap")
        if self.best_heldout_error is not None:
            _finite_nonnegative("best_heldout_error", self.best_heldout_error)
        if accepted > 0:
            if self.best_heldout_error is None:
                raise ValueError("accepted models require a recorded held-out error")
            if accepted_violations != 0:
                raise ValueError("accepted models require zero recorded constraint violations")
            if replays < accepted:
                raise ValueError("each accepted model requires an independent replay")


def validate_matched_search_runs(runs: Sequence[SearchRun]) -> None:
    """Fail closed unless runs share a benchmark, splits and declared resource caps."""
    if len(runs) < 2:
        raise ValueError("at least two methods are required for comparison")
    for run in runs:
        run.validate()
    if len({run.method_id for run in runs}) != len(runs):
        raise ValueError("method_id values must be unique")
    first = runs[0]
    identity = (
        first.benchmark_id, first.dataset_digest, first.train_digest,
        first.validation_digest, first.heldout_digest,
    )
    budget = first.budget.comparison_key()
    for run in runs[1:]:
        if (
            run.benchmark_id, run.dataset_digest, run.train_digest,
            run.validation_digest, run.heldout_digest,
        ) != identity:
            raise ValueError("all methods must use identical benchmark and split digests")
        if run.budget.comparison_key() != budget:
            raise ValueError("all methods must use identical declared resource caps")


def cost_per_accepted_useful_model(run: SearchRun) -> float | None:
    """Return measured direct cost per accepted model, or None when undefined."""
    run.validate()
    if run.direct_cost_usd is None or run.accepted_useful_model_count == 0:
        return None
    return run.direct_cost_usd / run.accepted_useful_model_count


def energy_comparison_available(runs: Sequence[SearchRun]) -> bool:
    """Energy comparisons are available only when every run has measured energy."""
    validate_matched_search_runs(runs)
    return all(run.energy_joules is not None for run in runs)
