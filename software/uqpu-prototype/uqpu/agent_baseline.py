"""Fail-closed matched contracts for goal-only and specialized GPU-kernel agents.

Synthetic tests validate comparison logic only; this module does not benchmark hardware.
"""
from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass
import math
from statistics import median


def _text(name: str, value: object) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a non-empty string")
    return value.strip()


def _positive(name: str, value: object) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric and not boolean")
    try:
        number = float(value)
    except (TypeError, ValueError, OverflowError) as exc:
        raise ValueError(f"{name} must convert to a finite float") from exc
    if not math.isfinite(number) or number <= 0:
        raise ValueError(f"{name} must be finite and strictly positive")
    return number


def _boolean(name: str, value: object) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be boolean")
    return value


def _shapes(values: Iterable[object]) -> tuple[str, ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError("workload_shapes must be a non-string iterable")
    try:
        raw = tuple(values)
    except TypeError as exc:
        raise ValueError("workload_shapes must be iterable") from exc
    if not raw:
        raise ValueError("workload_shapes must not be empty")
    result = tuple(_text("workload shape", item) for item in raw)
    if len(set(result)) != len(result):
        raise ValueError("workload_shapes must not contain duplicates")
    return tuple(sorted(result))


def _samples_by_shape(values: Iterable[object]) -> tuple[tuple[str, tuple[float, ...]], ...]:
    if isinstance(values, (str, bytes)):
        raise ValueError("latency_samples_by_shape must be a non-string iterable")
    try:
        raw = tuple(values)
    except TypeError as exc:
        raise ValueError("latency_samples_by_shape must be iterable") from exc
    if not raw:
        raise ValueError("latency_samples_by_shape must not be empty")
    result = []
    seen = set()
    for entry in raw:
        if not isinstance(entry, (tuple, list)) or len(entry) != 2:
            raise ValueError("each latency entry must be a (shape_id, samples) pair")
        shape = _text("latency shape", entry[0])
        if shape in seen:
            raise ValueError("latency_samples_by_shape must not contain duplicate shapes")
        seen.add(shape)
        raw_samples = entry[1]
        if isinstance(raw_samples, (str, bytes)):
            raise ValueError("latency samples must be a non-string iterable")
        try:
            samples = tuple(_positive("latency sample", x) for x in raw_samples)
        except TypeError as exc:
            raise ValueError("latency samples must be iterable") from exc
        if len(samples) < 3:
            raise ValueError("at least three latency samples are required per shape")
        result.append((shape, samples))
    return tuple(sorted(result))


@dataclass(frozen=True)
class KernelRunContract:
    model_id: str
    model_version: str
    reasoning_effort: str
    target_id: str
    driver_version: str
    runtime_version: str
    operator_id: str
    scope_id: str
    workload_shapes: tuple[str, ...]
    budget_seconds: float
    precision: str
    correctness_protocol_id: str
    timing_protocol_id: str
    reference_code_access: bool = False
    kernel_specific_knowledge: bool = False
    kernel_specific_evaluator: bool = False
    predefined_search_workflow: bool = False

    def __post_init__(self) -> None:
        for name in (
            "model_id", "model_version", "reasoning_effort", "target_id",
            "driver_version", "runtime_version", "operator_id", "scope_id",
            "precision", "correctness_protocol_id", "timing_protocol_id",
        ):
            object.__setattr__(self, name, _text(name, getattr(self, name)))
        object.__setattr__(self, "workload_shapes", _shapes(self.workload_shapes))
        object.__setattr__(self, "budget_seconds", _positive("budget_seconds", self.budget_seconds))
        for name in (
            "reference_code_access", "kernel_specific_knowledge",
            "kernel_specific_evaluator", "predefined_search_workflow",
        ):
            object.__setattr__(self, name, _boolean(name, getattr(self, name)))


@dataclass(frozen=True)
class KernelRunMeasurement:
    latency_samples_by_shape: tuple[tuple[str, tuple[float, ...]], ...]
    correctness_passed: bool
    independent_verifier_passed: bool
    sanitizer_passed: bool

    def __post_init__(self) -> None:
        object.__setattr__(self, "latency_samples_by_shape", _samples_by_shape(self.latency_samples_by_shape))
        for name in ("correctness_passed", "independent_verifier_passed", "sanitizer_passed"):
            object.__setattr__(self, name, _boolean(name, getattr(self, name)))


@dataclass(frozen=True)
class KernelComparisonAudit:
    accepted: bool
    rejection_reasons: tuple[str, ...]
    goal_only_medians_by_shape: tuple[tuple[str, float], ...] | None
    specialized_medians_by_shape: tuple[tuple[str, float], ...] | None
    specialized_speedups_by_shape: tuple[tuple[str, float], ...] | None
    specialized_geomean_speedup_over_goal_only: float | None
    matched_scope_id: str | None


def compare_goal_only_and_specialized(
    goal_only: KernelRunContract,
    specialized: KernelRunContract,
    goal_only_measurement: KernelRunMeasurement,
    specialized_measurement: KernelRunMeasurement,
) -> KernelComparisonAudit:
    """Return a speedup only for a fully matched, independently verified comparison."""
    if not isinstance(goal_only, KernelRunContract) or not isinstance(specialized, KernelRunContract):
        raise ValueError("both contracts must be KernelRunContract instances")
    if not isinstance(goal_only_measurement, KernelRunMeasurement) or not isinstance(specialized_measurement, KernelRunMeasurement):
        raise ValueError("both measurements must be KernelRunMeasurement instances")

    fields = (
        "model_id", "model_version", "reasoning_effort", "target_id",
        "driver_version", "runtime_version", "operator_id", "scope_id",
        "workload_shapes", "budget_seconds", "precision",
        "correctness_protocol_id", "timing_protocol_id", "reference_code_access",
    )
    reasons = [f"mismatch:{field}" for field in fields
               if getattr(goal_only, field) != getattr(specialized, field)]
    expected = set(goal_only.workload_shapes)
    for arm, measurement in (("goal_only", goal_only_measurement), ("specialized", specialized_measurement)):
        if {shape for shape, _ in measurement.latency_samples_by_shape} != expected:
            reasons.append(f"{arm}_shape_coverage_mismatch")
        if not measurement.correctness_passed:
            reasons.append(f"{arm}_correctness_failed")
        if not measurement.independent_verifier_passed:
            reasons.append(f"{arm}_independent_verifier_failed")
        if not measurement.sanitizer_passed:
            reasons.append(f"{arm}_sanitizer_failed")

    if goal_only.reference_code_access:
        reasons.append("goal_only_reference_code_access_not_allowed")
    if goal_only.kernel_specific_knowledge:
        reasons.append("goal_only_kernel_specific_knowledge_not_allowed")
    if goal_only.kernel_specific_evaluator:
        reasons.append("goal_only_kernel_specific_evaluator_not_allowed")
    if goal_only.predefined_search_workflow:
        reasons.append("goal_only_predefined_search_workflow_not_allowed")
    if reasons:
        return KernelComparisonAudit(False, tuple(reasons), None, None, None, None, None)

    goal = tuple((shape, median(samples)) for shape, samples in goal_only_measurement.latency_samples_by_shape)
    spec = tuple((shape, median(samples)) for shape, samples in specialized_measurement.latency_samples_by_shape)
    gmap, smap = dict(goal), dict(spec)
    speedups = tuple((shape, gmap[shape] / smap[shape]) for shape in goal_only.workload_shapes)
    if any(not math.isfinite(v) or v <= 0 for _, v in speedups):
        return KernelComparisonAudit(False, ("invalid_speedup",), None, None, None, None, None)
    geomean = math.exp(math.fsum(math.log(v) for _, v in speedups) / len(speedups))
    if not math.isfinite(geomean) or geomean <= 0:
        return KernelComparisonAudit(False, ("invalid_geomean_speedup",), None, None, None, None, None)
    return KernelComparisonAudit(True, (), goal, spec, speedups, geomean, goal_only.scope_id)
