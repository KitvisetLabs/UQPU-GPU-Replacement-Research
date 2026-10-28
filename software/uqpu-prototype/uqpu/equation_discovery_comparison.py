"""Matched-resource comparison contract for equation-discovery methods.

Passing this contract means records are comparable and internally valid; it
does not prove that an equation is a physical law or that a method is superior.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import asdict, dataclass
import math
import re
from typing import Iterable

_SHA256 = re.compile(r"[0-9a-f]{64}")
MIN_PREREGISTERED_SEEDS = 30
_COMMON_HASH_FIELDS = (
    "dataset_sha256",
    "dataset_provenance_sha256",
    "train_split_sha256",
    "validation_split_sha256",
    "test_split_sha256",
    "preprocessing_sha256",
    "grammar_sha256",
    "unit_schema_sha256",
    "acceptance_rule_sha256",
    "split_policy_sha256",
    "heldout_group_manifest_sha256",
)
_ALLOWED_HOLDOUT_UNITS = {
    "LAW_FAMILY",
    "MATERIAL_FAMILY",
    "FLUID_PAIR",
    "SCALE",
    "GEOMETRY",
    "TIME_BLOCK",
    "DEVICE_FAMILY",
    "COMPOSITE_GROUP",
}


def _require_sha256(name: str, value: str) -> None:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{name} must be a lowercase 64-character SHA-256 hex digest")


def _finite_nonnegative(name: str, value: float) -> None:
    if not isinstance(value, (int, float)) or not math.isfinite(float(value)) or value < 0:
        raise ValueError(f"{name} must be finite and >= 0")


def _nonnegative_int(name: str, value: int, *, positive: bool = False) -> None:
    if isinstance(value, bool) or not isinstance(value, int):
        raise ValueError(f"{name} must be an integer")
    if value < 1 if positive else value < 0:
        comparator = ">= 1" if positive else ">= 0"
        raise ValueError(f"{name} must be {comparator}")


@dataclass(frozen=True)
class DiscoveryBudget:
    """Shared hard ceiling for each method/seed run."""

    max_wall_clock_seconds: float
    max_cpu_core_seconds: float
    max_peak_memory_bytes: int
    max_accelerator_seconds: float
    max_candidate_evaluations: int
    max_generated_tokens: int
    max_total_cost_usd: float | None = None

    def validate(self) -> None:
        for name in ("max_wall_clock_seconds", "max_cpu_core_seconds", "max_accelerator_seconds"):
            _finite_nonnegative(name, getattr(self, name))
        if self.max_wall_clock_seconds <= 0:
            raise ValueError("max_wall_clock_seconds must be > 0")
        _nonnegative_int("max_peak_memory_bytes", self.max_peak_memory_bytes, positive=True)
        _nonnegative_int("max_candidate_evaluations", self.max_candidate_evaluations, positive=True)
        _nonnegative_int("max_generated_tokens", self.max_generated_tokens, positive=True)
        if self.max_total_cost_usd is not None:
            _finite_nonnegative("max_total_cost_usd", self.max_total_cost_usd)


@dataclass(frozen=True)
class DiscoveryRun:
    """One method's best candidate from one preregistered seed."""

    method_id: str
    method_revision_sha256: str
    method_config_sha256: str
    runtime_environment_sha256: str
    seed: int
    dataset_sha256: str
    dataset_provenance_sha256: str
    train_split_sha256: str
    validation_split_sha256: str
    test_split_sha256: str
    preprocessing_sha256: str
    grammar_sha256: str
    unit_schema_sha256: str
    acceptance_rule_sha256: str
    split_policy_sha256: str
    heldout_group_manifest_sha256: str
    holdout_unit: str
    heldout_group_count: int
    budget: DiscoveryBudget
    wall_clock_seconds: float
    cpu_core_seconds: float
    peak_memory_bytes: int
    accelerator_seconds: float
    candidate_evaluations: int
    generated_tokens: int
    accepted: bool
    heldout_error: float | None
    constraint_violations: int = 0
    counterexamples: int = 0
    false_discoveries: int = 0
    total_cost_usd: float | None = None
    cost_basis_id: str | None = None

    def validate(self) -> None:
        if not isinstance(self.method_id, str) or not self.method_id.strip():
            raise ValueError("method_id is required")
        _require_sha256("method_revision_sha256", self.method_revision_sha256)
        _require_sha256("method_config_sha256", self.method_config_sha256)
        _require_sha256("runtime_environment_sha256", self.runtime_environment_sha256)
        _nonnegative_int("seed", self.seed)
        for name in _COMMON_HASH_FIELDS:
            _require_sha256(name, getattr(self, name))
        self.budget.validate()
        if self.holdout_unit not in _ALLOWED_HOLDOUT_UNITS:
            raise ValueError(
                "holdout_unit must declare a group-disjoint unit; random-point-only "
                "holdouts are not accepted"
            )
        _nonnegative_int("heldout_group_count", self.heldout_group_count, positive=True)

        for name in ("wall_clock_seconds", "cpu_core_seconds", "accelerator_seconds"):
            _finite_nonnegative(name, getattr(self, name))
        for name in (
            "peak_memory_bytes",
            "candidate_evaluations",
            "generated_tokens",
            "constraint_violations",
            "counterexamples",
            "false_discoveries",
        ):
            _nonnegative_int(name, getattr(self, name))

        if self.heldout_error is not None:
            _finite_nonnegative("heldout_error", self.heldout_error)
        if not isinstance(self.accepted, bool):
            raise ValueError("accepted must be a boolean")
        if self.accepted:
            if self.heldout_error is None:
                raise ValueError("an accepted candidate requires a held-out error")
            if self.constraint_violations or self.counterexamples or self.false_discoveries:
                raise ValueError("an accepted candidate cannot retain constraint violations, counterexamples, or false discoveries")

        ceilings = (
            ("wall_clock_seconds", self.wall_clock_seconds, self.budget.max_wall_clock_seconds),
            ("cpu_core_seconds", self.cpu_core_seconds, self.budget.max_cpu_core_seconds),
            ("peak_memory_bytes", self.peak_memory_bytes, self.budget.max_peak_memory_bytes),
            ("accelerator_seconds", self.accelerator_seconds, self.budget.max_accelerator_seconds),
            ("candidate_evaluations", self.candidate_evaluations, self.budget.max_candidate_evaluations),
            ("generated_tokens", self.generated_tokens, self.budget.max_generated_tokens),
        )
        for name, used, ceiling in ceilings:
            if used > ceiling:
                raise ValueError(f"{name} exceeds the preregistered budget")

        if self.total_cost_usd is None:
            if self.cost_basis_id is not None:
                raise ValueError("cost_basis_id requires total_cost_usd")
            if self.budget.max_total_cost_usd is not None:
                raise ValueError("a cost ceiling requires a measured total_cost_usd")
        else:
            _finite_nonnegative("total_cost_usd", self.total_cost_usd)
            if not isinstance(self.cost_basis_id, str) or not self.cost_basis_id.strip():
                raise ValueError("measured cost requires a nonempty cost_basis_id")
            if self.budget.max_total_cost_usd is not None and self.total_cost_usd > self.budget.max_total_cost_usd:
                raise ValueError("total_cost_usd exceeds the preregistered budget")


def validate_matched_comparison(runs: Iterable[DiscoveryRun]) -> tuple[str, ...]:
    """Validate a matched comparison and return sorted method identifiers.

    The protocol requires >=30 shared preregistered seeds per method. It rejects
    dataset/split/grammar/unit/acceptance mismatches, mismatched declared group-holdout
    metadata, duplicate method-seed pairs, unequal budgets, resource overruns, and
    mixed cost bases. The hashed holdout manifest is not parsed here; a separate
    partition validator must establish actual record-level disjointness.
    """
    records = tuple(runs)
    if not records:
        raise ValueError("at least two methods and 30 matched seeds are required")
    for record in records:
        record.validate()

    methods = sorted({record.method_id for record in records})
    if len(methods) < 2:
        raise ValueError("at least two distinct methods are required")

    reference = records[0]
    for record in records[1:]:
        for name in _COMMON_HASH_FIELDS:
            if getattr(record, name) != getattr(reference, name):
                raise ValueError(f"comparison mismatch in {name}")
        if record.budget != reference.budget:
            raise ValueError("all methods must use the identical preregistered budget envelope")
        if (
            record.holdout_unit != reference.holdout_unit
            or record.heldout_group_count != reference.heldout_group_count
        ):
            raise ValueError("all methods must use the identical grouped holdout unit and group count")

    by_method: dict[str, dict[int, DiscoveryRun]] = defaultdict(dict)
    for record in records:
        if record.seed in by_method[record.method_id]:
            raise ValueError(f"duplicate method/seed pair: {record.method_id}/{record.seed}")
        by_method[record.method_id][record.seed] = record

    seed_sets = [set(by_method[method]) for method in methods]
    if any(seeds != seed_sets[0] for seeds in seed_sets[1:]):
        raise ValueError("every method must run the same preregistered seed set")
    if len(seed_sets[0]) < MIN_PREREGISTERED_SEEDS:
        raise ValueError(f"at least {MIN_PREREGISTERED_SEEDS} preregistered seeds are required")

    # Prevent a nominally matched method from changing its source, configuration,
    # model/prompt bundle, or runtime between seeds. Hashes are provenance bindings,
    # not proof that the referenced artifacts are authentic or scientifically valid.
    for method in methods:
        method_records = tuple(by_method[method].values())
        for name in ("method_revision_sha256", "method_config_sha256", "runtime_environment_sha256"):
            if len({getattr(record, name) for record in method_records}) != 1:
                raise ValueError(f"{name} must remain constant across all preregistered seeds for method {method}")

    cost_presence = [record.total_cost_usd is not None for record in records]
    if any(cost_presence) and not all(cost_presence):
        raise ValueError("cost must be measured for every run or omitted for every run")
    if all(cost_presence):
        if len({record.cost_basis_id for record in records}) != 1:
            raise ValueError("all costs must use the same declared cost basis")

    return tuple(methods)


def _wilson_interval(successes: int, trials: int) -> tuple[float, float]:
    """Return a marginal 95% Wilson interval for a Bernoulli acceptance rate."""
    if trials <= 0:
        raise ValueError("trials must be > 0")
    z = 1.959963984540054
    rate = successes / trials
    z_squared = z * z
    denominator = 1.0 + z_squared / trials
    center = (rate + z_squared / (2.0 * trials)) / denominator
    half_width = (
        z
        * math.sqrt(
            rate * (1.0 - rate) / trials
            + z_squared / (4.0 * trials * trials)
        )
        / denominator
    )
    return max(0.0, center - half_width), min(1.0, center + half_width)


def compare_methods(runs: Iterable[DiscoveryRun]) -> dict[str, object]:
    """Return descriptive summaries only; do not infer a winner or physical law."""
    records = tuple(runs)
    methods = validate_matched_comparison(records)
    by_method: dict[str, list[DiscoveryRun]] = defaultdict(list)
    for record in records:
        by_method[record.method_id].append(record)

    summaries: dict[str, dict[str, object]] = {}
    for method in methods:
        group = by_method[method]
        accepted = [record for record in group if record.accepted]
        costs_measured = all(record.total_cost_usd is not None for record in group)
        total_cost = (
            math.fsum(record.total_cost_usd for record in group if record.total_cost_usd is not None)
            if costs_measured else None
        )
        accepted_errors = [record.heldout_error for record in accepted if record.heldout_error is not None]
        acceptance_rate = len(accepted) / len(group)
        acceptance_interval = _wilson_interval(len(accepted), len(group))
        summaries[method] = {
            "runs": len(group),
            "provenance": {
                "method_revision_sha256": group[0].method_revision_sha256,
                "method_config_sha256": group[0].method_config_sha256,
                "runtime_environment_sha256": group[0].runtime_environment_sha256,
            },
            "accepted_candidates": len(accepted),
            "acceptance_rate": acceptance_rate,
            "acceptance_rate_95pct_wilson_ci": [acceptance_interval[0], acceptance_interval[1]],
            "mean_heldout_error_of_accepted": (
                math.fsum(accepted_errors) / len(accepted_errors) if accepted_errors else None
            ),
            "total_wall_clock_seconds": math.fsum(record.wall_clock_seconds for record in group),
            "total_cost_usd": total_cost,
            "cost_per_accepted_candidate_usd": (
                total_cost / len(accepted) if total_cost is not None and accepted else None
            ),
        }

    by_method_seed = {
        method: {record.seed: record for record in by_method[method]}
        for method in methods
    }
    pairwise_acceptance: dict[str, dict[str, object]] = {}
    for index, left in enumerate(methods):
        for right in methods[index + 1:]:
            seeds = sorted(by_method_seed[left])
            left_only = sum(
                by_method_seed[left][seed].accepted and not by_method_seed[right][seed].accepted
                for seed in seeds
            )
            right_only = sum(
                by_method_seed[right][seed].accepted and not by_method_seed[left][seed].accepted
                for seed in seeds
            )
            both = sum(
                by_method_seed[left][seed].accepted and by_method_seed[right][seed].accepted
                for seed in seeds
            )
            neither = len(seeds) - left_only - right_only - both
            pairwise_acceptance[f"{left}__vs__{right}"] = {
                "left_method": left,
                "right_method": right,
                "shared_seed_count": len(seeds),
                "both_accepted": both,
                "left_only_accepted": left_only,
                "right_only_accepted": right_only,
                "neither_accepted": neither,
                "acceptance_rate_difference_left_minus_right": (
                    float(summaries[left]["acceptance_rate"])
                    - float(summaries[right]["acceptance_rate"])
                ),
                "interpretation": "Descriptive paired counts only; no significance test or winner is inferred.",
            }

    return {
        "schema": "uqpu-equation-discovery-matched-comparison-v4",
        "shared_dataset": {
            "dataset_sha256": records[0].dataset_sha256,
            "dataset_provenance_sha256": records[0].dataset_provenance_sha256,
        },
        "method_ids": list(methods),
        "preregistered_seed_count": len({record.seed for record in records}),
        "shared_budget": asdict(records[0].budget),
        "shared_holdout": {
            "unit": records[0].holdout_unit,
            "group_count": records[0].heldout_group_count,
            "split_policy_sha256": records[0].split_policy_sha256,
            "heldout_group_manifest_sha256": records[0].heldout_group_manifest_sha256,
            "manifest_content_verified_by_this_module": False,
        },
        "methods": summaries,
        "pairwise_acceptance": pairwise_acceptance,
        "interpretation": (
            "Descriptive benchmark summary only. Marginal 95% Wilson intervals treat seed runs as "
            "an exchangeable Bernoulli sample for this fixed benchmark and do not account for tuning "
            "or multiple comparisons. Pairwise seed counts are descriptive; no p-values or winner are "
            "produced. All methods share a declared group-holdout policy and manifest digest, but "
            "the manifest contents and actual record-level disjointness require a separate validator. "
            "Per-method source, configuration/model/prompt bundle and runtime-environment digests must remain "
            "constant across all preregistered seeds; hashes alone do not authenticate the referenced artifacts. "
            "Acceptance is defined by the frozen benchmark rule and does not establish a physical law, "
            "independent replication, device benefit, or economic advantage outside the measured "
            "resource boundary."
        ),
    }
