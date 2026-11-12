"""Finite-grid candidate screen for symbolic optimization-law discovery.

This module compares a candidate objective with a reference objective over
explicit context and decision grids. It is a MODEL_ONLY screening utility:
it does not discover equations, prove identifiability, check physical units,
or establish a physical law or engineering advantage.
"""
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from typing import Callable, Sequence

Objective = Callable[[float, float], float]


@dataclass(frozen=True)
class OrderingMetrics:
    pairs_compared: int
    concordant: int
    discordant: int
    matched_ties: int
    tie_disagreements: int

    @property
    def informative_pairs(self) -> int:
        return self.concordant + self.discordant + self.tie_disagreements

    @property
    def agreement(self) -> float | None:
        """Pairwise ordering agreement; None means the split is uninformative."""
        denominator = self.informative_pairs
        if denominator == 0:
            return None
        return self.concordant / denominator


@dataclass(frozen=True)
class SplitMetrics:
    context_count: int
    decision_count: int
    ordering: OrderingMetrics
    optimum_set_match_rate: float


@dataclass(frozen=True)
class BenchmarkResult:
    direction: str
    train: SplitMetrics
    heldout: SplitMetrics
    train_contexts_sha256: str
    heldout_contexts_sha256: str
    decision_grid_sha256: str
    grid_contract_sha256: str


def _sha256_json(value: object) -> str:
    """Hash canonical JSON for numeric-grid reproducibility, not data provenance."""
    encoded = json.dumps(
        value, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")
    return hashlib.sha256(encoded).hexdigest()


def _require_unique(name: str, values: Sequence[float]) -> None:
    if len(set(values)) != len(values):
        raise ValueError(f"{name} must not contain duplicate values")


def _values(
    objective: Objective, context: float, decisions: Sequence[float]
) -> list[float]:
    values: list[float] = []
    for decision in decisions:
        value = float(objective(float(context), float(decision)))
        if not math.isfinite(value):
            raise ValueError("objective values must be finite")
        values.append(value)
    return values


def _optimum_indices(
    values: Sequence[float], direction: str, tolerance: float
) -> tuple[int, ...]:
    target = min(values) if direction == "min" else max(values)
    return tuple(
        index
        for index, value in enumerate(values)
        if abs(value - target) <= tolerance
    )


def _score_split(
    reference: Objective,
    candidate: Objective,
    contexts: Sequence[float],
    decisions: Sequence[float],
    direction: str,
    tolerance: float,
) -> SplitMetrics:
    concordant = discordant = matched_ties = tie_disagreements = pairs = 0
    optimum_matches = 0

    for context in contexts:
        reference_values = _values(reference, context, decisions)
        candidate_values = _values(candidate, context, decisions)
        reference_optima = _optimum_indices(reference_values, direction, tolerance)
        candidate_optima = _optimum_indices(candidate_values, direction, tolerance)
        optimum_matches += reference_optima == candidate_optima

        for left in range(len(decisions)):
            for right in range(left + 1, len(decisions)):
                reference_delta = reference_values[left] - reference_values[right]
                candidate_delta = candidate_values[left] - candidate_values[right]
                reference_tied = abs(reference_delta) <= tolerance
                candidate_tied = abs(candidate_delta) <= tolerance
                pairs += 1

                if reference_tied and candidate_tied:
                    matched_ties += 1
                elif reference_tied or candidate_tied:
                    tie_disagreements += 1
                elif reference_delta * candidate_delta > 0:
                    concordant += 1
                else:
                    discordant += 1

    ordering = OrderingMetrics(
        pairs_compared=pairs,
        concordant=concordant,
        discordant=discordant,
        matched_ties=matched_ties,
        tie_disagreements=tie_disagreements,
    )
    return SplitMetrics(
        context_count=len(contexts),
        decision_count=len(decisions),
        ordering=ordering,
        optimum_set_match_rate=optimum_matches / len(contexts),
    )


def evaluate_objective_candidate(
    reference: Objective,
    candidate: Objective,
    train_contexts: Sequence[float],
    heldout_contexts: Sequence[float],
    decisions: Sequence[float],
    direction: str = "min",
    tolerance: float = 1e-9,
) -> BenchmarkResult:
    """Score objective-order and optimum-set agreement on frozen finite grids.

    Contexts must be split before candidate selection. Duplicate context values,
    train/held-out overlap, and duplicate decisions are rejected so repeated
    entries cannot silently overweight the score. Returned SHA-256 fingerprints
    bind the numeric grids and scoring settings only; they do not bind objective
    callable code, source data, split-generation provenance, or search budgets.
    This utility does not itself freeze the upstream dataset or inspect symbolic
    structure and physical constraints.
    """
    if direction not in {"min", "max"}:
        raise ValueError("direction must be 'min' or 'max'")
    tolerance = float(tolerance)
    if not math.isfinite(tolerance) or tolerance < 0:
        raise ValueError("tolerance must be finite and >= 0")

    train = tuple(float(value) for value in train_contexts)
    heldout = tuple(float(value) for value in heldout_contexts)
    choices = tuple(float(value) for value in decisions)
    if not train or not heldout:
        raise ValueError("train and held-out contexts must be non-empty")
    if len(choices) < 2:
        raise ValueError("at least two decision values are required")
    if not all(math.isfinite(value) for value in (*train, *heldout, *choices)):
        raise ValueError("contexts and decisions must be finite")

    _require_unique("train contexts", train)
    _require_unique("held-out contexts", heldout)
    _require_unique("decision grid", choices)
    if set(train).intersection(heldout):
        raise ValueError("train and held-out contexts must be disjoint")

    train_hash = _sha256_json(train)
    heldout_hash = _sha256_json(heldout)
    decision_hash = _sha256_json(choices)
    grid_contract_hash = _sha256_json(
        {
            "train_contexts": train,
            "heldout_contexts": heldout,
            "decisions": choices,
            "direction": direction,
            "tolerance": tolerance,
        }
    )

    return BenchmarkResult(
        direction=direction,
        train=_score_split(reference, candidate, train, choices, direction, tolerance),
        heldout=_score_split(
            reference, candidate, heldout, choices, direction, tolerance
        ),
        train_contexts_sha256=train_hash,
        heldout_contexts_sha256=heldout_hash,
        decision_grid_sha256=decision_hash,
        grid_contract_sha256=grid_contract_hash,
    )
