"""Fair-budget audit contract for equation-discovery method comparisons.

This module evaluates experiment metadata and preserves failures. It does not
infer physical truth, validate a physical law, or promote a candidate beyond
MODEL_ONLY. It is intentionally dependency-free so the contract can run in CI.
"""
from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
import math
import re
from statistics import fmean
from typing import Iterable

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_METHODS = frozenset({
    "symbolic_search",
    "transformer_generator",
    "llm_guided_search",
    "physics_constrained_hybrid",
    "deterministic_baseline",
})
_CONSTRAINTS = (
    "dimensional_consistency",
    "symmetry",
    "conservation",
    "causality",
)


def _is_nonnegative_int(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


def _require_sha256(name: str, value: str) -> None:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{name} must be a lowercase 64-character SHA-256 hex digest")


@dataclass(frozen=True)
class FormulaDiscoveryRun:
    """One seeded run against frozen train, interpolation and extrapolation splits."""

    method: str
    seed: int
    dataset_sha256: str
    train_split_sha256: str
    heldout_split_sha256: str
    extrapolation_split_sha256: str
    split_disjointness_certificate_sha256: str
    candidate_sha256: str
    train_error: float
    heldout_error: float
    extrapolation_error: float
    budget_seconds: float
    wall_clock_seconds: float
    host_cpu_seconds: float
    peak_memory_bytes: int
    candidate_complexity: int
    candidate_count: int
    dimensional_consistency_passed: bool
    symmetry_passed: bool
    conservation_passed: bool
    causality_passed: bool
    energy_joules: float | None = None
    token_count: int | None = None
    model_sha256: str | None = None
    training_gpu_hours: float | None = None
    training_energy_joules: float | None = None
    model_parameters: int | None = None
    counterexample_count: int = 0
    failed_search_count: int = 0
    false_discovery: bool = False
    provenance: str = ""

    def validate(self) -> None:
        if self.method not in _METHODS:
            raise ValueError(f"unsupported discovery method: {self.method!r}")
        if not _is_nonnegative_int(self.seed):
            raise ValueError("seed must be a nonnegative integer")
        for name in (
            "dataset_sha256",
            "train_split_sha256",
            "heldout_split_sha256",
            "extrapolation_split_sha256",
            "split_disjointness_certificate_sha256",
            "candidate_sha256",
        ):
            _require_sha256(name, getattr(self, name))
        if len({
            self.train_split_sha256,
            self.heldout_split_sha256,
            self.extrapolation_split_sha256,
        }) != 3:
            raise ValueError("train, held-out and extrapolation split hashes must be distinct")
        numeric = (
            ("train_error", self.train_error),
            ("heldout_error", self.heldout_error),
            ("extrapolation_error", self.extrapolation_error),
            ("budget_seconds", self.budget_seconds),
            ("wall_clock_seconds", self.wall_clock_seconds),
            ("host_cpu_seconds", self.host_cpu_seconds),
        )
        for name, value in numeric:
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{name} must be numeric")
            if not math.isfinite(float(value)) or value < 0:
                raise ValueError(f"{name} must be finite and nonnegative")
        if self.budget_seconds <= 0:
            raise ValueError("budget_seconds must be positive")
        if self.wall_clock_seconds > self.budget_seconds * (1.0 + 1e-12):
            raise ValueError("wall_clock_seconds exceeds the declared run budget")
        for name in ("peak_memory_bytes", "candidate_complexity", "candidate_count"):
            value = getattr(self, name)
            if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
                raise ValueError(f"{name} must be a positive integer")
        for name in ("counterexample_count", "failed_search_count"):
            if not _is_nonnegative_int(getattr(self, name)):
                raise ValueError(f"{name} must be a nonnegative integer")
        for name in (
            "dimensional_consistency_passed",
            "symmetry_passed",
            "conservation_passed",
            "causality_passed",
            "false_discovery",
        ):
            if not isinstance(getattr(self, name), bool):
                raise ValueError(f"{name} must be a boolean")
        if self.energy_joules is not None:
            if (
                isinstance(self.energy_joules, bool)
                or not isinstance(self.energy_joules, (int, float))
                or not math.isfinite(float(self.energy_joules))
                or self.energy_joules < 0
            ):
                raise ValueError("energy_joules must be finite and nonnegative when supplied")
        if self.token_count is not None and not _is_nonnegative_int(self.token_count):
            raise ValueError("token_count must be a nonnegative integer when supplied")
        training_fields = (
            self.training_gpu_hours,
            self.training_energy_joules,
            self.model_parameters,
        )
        if any(value is not None for value in training_fields) and self.model_sha256 is None:
            raise ValueError("model_sha256 is required when model training resources are supplied")
        if self.model_sha256 is not None:
            _require_sha256("model_sha256", self.model_sha256)
        for name in ("training_gpu_hours", "training_energy_joules"):
            value = getattr(self, name)
            if value is not None and (
                isinstance(value, bool)
                or not isinstance(value, (int, float))
                or not math.isfinite(float(value))
                or value < 0
            ):
                raise ValueError(f"{name} must be finite and nonnegative when supplied")
        if self.model_parameters is not None and (
            not isinstance(self.model_parameters, int)
            or isinstance(self.model_parameters, bool)
            or self.model_parameters <= 0
        ):
            raise ValueError("model_parameters must be a positive integer when supplied")
        if not isinstance(self.provenance, str) or not self.provenance.strip():
            raise ValueError("provenance is required")


@dataclass(frozen=True)
class FormulaDiscoveryAudit:
    """Comparison summary; the evidence class is deliberately fixed at MODEL_ONLY."""

    evidence_class: str
    methods: tuple[str, ...]
    run_count: int
    runs_per_method: tuple[tuple[str, int], ...]
    mean_heldout_error: tuple[tuple[str, float], ...]
    mean_extrapolation_error: tuple[tuple[str, float], ...]
    false_discovery_runs: int
    failed_search_count: int
    counterexample_count: int
    constraint_failure_counts: tuple[tuple[str, int], ...]
    max_budget_spread_fraction: float
    token_instrumented_runs: int
    energy_instrumented_runs: int
    training_models_instrumented: int
    training_gpu_hours_by_method: tuple[tuple[str, float | None], ...]
    training_energy_joules_by_method: tuple[tuple[str, float | None], ...]
    physical_law_claim_allowed: bool = False
    promotion_blocker: str = (
        "MODEL_ONLY benchmark metadata; require held-out replication, "
        "counterexample review and a discriminating physical experiment."
    )


def audit_formula_discovery_comparison(
    runs: Iterable[FormulaDiscoveryRun],
    *,
    min_seeds_per_method: int = 3,
    relative_budget_tolerance: float = 0.05,
) -> FormulaDiscoveryAudit:
    """Validate a matched-budget comparison and summarize failures without dropping them."""
    rows = tuple(runs)
    if not rows:
        raise ValueError("at least one run is required")
    if not _is_nonnegative_int(min_seeds_per_method) or min_seeds_per_method < 1:
        raise ValueError("min_seeds_per_method must be a positive integer")
    if (
        isinstance(relative_budget_tolerance, bool)
        or not isinstance(relative_budget_tolerance, (int, float))
        or not math.isfinite(float(relative_budget_tolerance))
        or not 0 <= relative_budget_tolerance < 1
    ):
        raise ValueError("relative_budget_tolerance must be finite and in [0, 1)")

    for row in rows:
        row.validate()
    methods = tuple(sorted({row.method for row in rows}))
    if len(methods) < 2:
        raise ValueError("at least two distinct methods are required")

    def invariant(field: str) -> None:
        if len({getattr(row, field) for row in rows}) != 1:
            raise ValueError(f"all methods must share the same {field}")

    for field in (
        "dataset_sha256",
        "train_split_sha256",
        "heldout_split_sha256",
        "extrapolation_split_sha256",
        "split_disjointness_certificate_sha256",
    ):
        invariant(field)

    by_method: dict[str, list[FormulaDiscoveryRun]] = defaultdict(list)
    for row in rows:
        by_method[row.method].append(row)
    for method, group in by_method.items():
        seeds = [row.seed for row in group]
        if len(seeds) != len(set(seeds)):
            raise ValueError(f"{method} has duplicate seeds")
        if len(seeds) < min_seeds_per_method:
            raise ValueError(f"{method} has fewer than {min_seeds_per_method} seeds")

    budgets = [float(row.budget_seconds) for row in rows]
    max_budget = max(budgets)
    spread = (max_budget - min(budgets)) / max_budget
    if spread > relative_budget_tolerance:
        raise ValueError("method budgets are not matched within the declared tolerance")

    constraint_failure_counts = []
    for field, label in (
        ("dimensional_consistency_passed", "dimensional_consistency"),
        ("symmetry_passed", "symmetry"),
        ("conservation_passed", "conservation"),
        ("causality_passed", "causality"),
    ):
        constraint_failure_counts.append((label, sum(not getattr(row, field) for row in rows)))

    training_gpu_hours_by_method = []
    training_energy_joules_by_method = []
    training_models_instrumented = 0
    for method in methods:
        models: dict[str, tuple[float | None, float | None, int | None]] = {}
        for row in by_method[method]:
            if row.model_sha256 is None:
                continue
            signature = (
                row.training_gpu_hours,
                row.training_energy_joules,
                row.model_parameters,
            )
            prior = models.get(row.model_sha256)
            if prior is not None and prior != signature:
                raise ValueError("training resource metadata differs for the same model_sha256")
            models[row.model_sha256] = signature
        training_models_instrumented += len(models)
        gpu_values = [v[0] for v in models.values()]
        energy_values = [v[1] for v in models.values()]
        gpu_total = None if not models or any(v is None for v in gpu_values) else sum(float(v) for v in gpu_values)
        energy_total = None if not models or any(v is None for v in energy_values) else sum(float(v) for v in energy_values)
        training_gpu_hours_by_method.append((method, gpu_total))
        training_energy_joules_by_method.append((method, energy_total))

    return FormulaDiscoveryAudit(
        evidence_class="MODEL_ONLY",
        methods=methods,
        run_count=len(rows),
        runs_per_method=tuple((m, len(by_method[m])) for m in methods),
        mean_heldout_error=tuple((m, fmean(r.heldout_error for r in by_method[m])) for m in methods),
        mean_extrapolation_error=tuple((m, fmean(r.extrapolation_error for r in by_method[m])) for m in methods),
        false_discovery_runs=sum(row.false_discovery for row in rows),
        failed_search_count=sum(row.failed_search_count for row in rows),
        counterexample_count=sum(row.counterexample_count for row in rows),
        constraint_failure_counts=tuple(constraint_failure_counts),
        max_budget_spread_fraction=spread,
        token_instrumented_runs=sum(row.token_count is not None for row in rows),
        energy_instrumented_runs=sum(row.energy_joules is not None for row in rows),
        training_models_instrumented=training_models_instrumented,
        training_gpu_hours_by_method=tuple(training_gpu_hours_by_method),
        training_energy_joules_by_method=tuple(training_energy_joules_by_method),
        physical_law_claim_allowed=False,
    )
