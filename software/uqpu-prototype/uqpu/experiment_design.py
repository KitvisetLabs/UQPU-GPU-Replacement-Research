"""Fail-closed offline experiment-plan contracts for equation discovery.

This module validates plan metadata and matched resource envelopes only. It does
not execute an experiment, select a physically true equation, or authorize any
instrument/provider access.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import re
from numbers import Real
from typing import Iterable

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_INTEGER_FIELDS = (
    "generation_calls", "simulator_calls", "transfer_bytes", "retries", "provider_jobs"
)
_FLOAT_FIELDS = (
    "wall_time_seconds", "cpu_seconds", "gpu_seconds", "reconstruction_seconds",
    "replication_seconds", "provider_cost_usd", "instrument_minutes"
)


def _nonempty(value: str, name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} is required")


def _finite_nonnegative(value: object, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a real finite nonnegative number")
    number = float(value)
    if not math.isfinite(number) or number < 0:
        raise ValueError(f"{name} must be finite and nonnegative")
    return number


def _finite_parameter(value: object, name: str) -> float:
    """Finite numeric distribution parameter; some parameters may be negative."""
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{name} must be a real finite number")
    number = float(value)
    if not math.isfinite(number):
        raise ValueError(f"{name} must be finite")
    return number


@dataclass(frozen=True)
class PredictionSummary:
    """Typed, compact predictive distribution summary for one observable."""

    distribution_family: str
    parameters: tuple[float, ...]
    uncertainty: float
    unit: str

    def validate(self, expected_unit: str, field_name: str) -> None:
        _nonempty(self.distribution_family, f"{field_name}.distribution_family")
        _nonempty(self.unit, f"{field_name}.unit")
        if self.unit != expected_unit:
            raise ValueError(f"{field_name}.unit must match observable_unit")
        if not self.parameters:
            raise ValueError(f"{field_name}.parameters is required")
        for index, value in enumerate(self.parameters):
            _finite_parameter(value, f"{field_name}.parameters[{index}]")
        _finite_nonnegative(self.uncertainty, f"{field_name}.uncertainty")


@dataclass(frozen=True)
class ResourceBudget:
    """One declared budget or measured-use vector; None energy means unmeasured."""

    generation_calls: int
    simulator_calls: int
    wall_time_seconds: float
    cpu_seconds: float
    gpu_seconds: float
    transfer_bytes: int
    retries: int
    reconstruction_seconds: float
    replication_seconds: float
    energy_joules: float | None = None
    provider_jobs: int = 0
    provider_cost_usd: float = 0.0
    instrument_minutes: float = 0.0

    def validate(self, label: str) -> None:
        for name in _INTEGER_FIELDS:
            value = getattr(self, name)
            if isinstance(value, bool) or not isinstance(value, int) or value < 0:
                raise ValueError(f"{label}.{name} must be a nonnegative integer")
        for name in _FLOAT_FIELDS:
            _finite_nonnegative(getattr(self, name), f"{label}.{name}")
        if self.energy_joules is not None:
            _finite_nonnegative(self.energy_joules, f"{label}.energy_joules")

    def require_offline(self, label: str) -> None:
        if self.provider_jobs != 0 or self.provider_cost_usd != 0 or self.instrument_minutes != 0:
            raise ValueError(f"{label} must have zero provider jobs/cost and zero instrument time")

    def ensure_within(self, cap: "ResourceBudget", label: str) -> None:
        self.validate(f"{label}.used")
        cap.validate(f"{label}.cap")
        for name in _INTEGER_FIELDS + _FLOAT_FIELDS:
            if getattr(self, name) > getattr(cap, name):
                raise ValueError(f"{label}.{name} exceeds the matched budget cap")
        if (self.energy_joules is None) != (cap.energy_joules is None):
            raise ValueError(
                f"{label}.energy_joules must be measured for both use and cap, or unknown for both"
            )
        if self.energy_joules is not None and self.energy_joules > cap.energy_joules:
            raise ValueError(f"{label}.energy_joules exceeds the matched budget cap")


@dataclass(frozen=True)
class ExperimentPlan:
    """Candidate experiment plan; acceptance is schema/feasibility, not truth."""

    plan_id: str
    planner_id: str
    experiment_action: str
    incumbent_model: str
    incumbent_assumptions: tuple[str, ...]
    alternative_model: str
    changed_assumption: str
    observable_name: str
    observable_unit: str
    incumbent_prediction: PredictionSummary
    alternative_prediction: PredictionSummary
    uncertainty_model: str
    acceptance_predicate: str
    falsifier: str
    heldout_prediction: str
    capability_constraints: tuple[str, ...]
    hard_constraints: tuple[str, ...]
    violated_hard_constraints: tuple[str, ...]
    training_sha256: str
    validation_sha256: str
    heldout_sha256: str
    simulator_version: str
    model_version: str
    independent_validation_method: str
    budget_cap: ResourceBudget
    budget_used: ResourceBudget
    evidence_class: str = "MODEL_ONLY"
    execution_mode: str = "OFFLINE_SIMULATION"

    def validate(self) -> None:
        for name in (
            "plan_id", "planner_id", "experiment_action", "incumbent_model",
            "alternative_model", "changed_assumption", "observable_name", "observable_unit",
            "uncertainty_model", "acceptance_predicate", "falsifier", "heldout_prediction",
            "simulator_version", "model_version", "independent_validation_method",
        ):
            _nonempty(getattr(self, name), name)
        for name in ("incumbent_assumptions", "capability_constraints", "hard_constraints"):
            values = getattr(self, name)
            if not values or any(not isinstance(v, str) or not v.strip() for v in values):
                raise ValueError(f"{name} must contain nonempty text entries")
        if self.violated_hard_constraints:
            raise ValueError("plan violates one or more hard feasibility constraints")
        if self.evidence_class != "MODEL_ONLY":
            raise ValueError("offline plan evidence_class must remain MODEL_ONLY")
        if self.execution_mode != "OFFLINE_SIMULATION":
            raise ValueError("EXP-DESIGN-002 only permits OFFLINE_SIMULATION")
        hashes = (self.training_sha256, self.validation_sha256, self.heldout_sha256)
        if any(not isinstance(value, str) or not _SHA256_RE.fullmatch(value) for value in hashes):
            raise ValueError("training/validation/heldout identifiers must be lowercase SHA-256 hashes")
        if len(set(hashes)) != 3:
            raise ValueError("training, validation and held-out hashes must be distinct")
        self.incumbent_prediction.validate(self.observable_unit, "incumbent_prediction")
        self.alternative_prediction.validate(self.observable_unit, "alternative_prediction")
        self.budget_cap.validate("budget_cap")
        self.budget_used.validate("budget_used")
        self.budget_cap.require_offline("budget_cap")
        self.budget_used.require_offline("budget_used")
        self.budget_used.ensure_within(self.budget_cap, self.plan_id)


def validate_matched_plans(plans: Iterable[ExperimentPlan]) -> tuple[str, ...]:
    """Validate three distinct planner roles against the exact same budget cap."""
    candidates = tuple(plans)
    if len(candidates) < 3:
        raise ValueError("matched comparison requires human, information-gain and AI planner candidates")
    required_planners = {"human", "information_gain", "ai_proposed"}
    if not required_planners.issubset({p.planner_id for p in candidates}):
        raise ValueError("matched comparison must include human, information_gain and ai_proposed planners")
    for plan in candidates:
        plan.validate()
    if len({p.plan_id for p in candidates}) != len(candidates):
        raise ValueError("plan_id values must be unique")
    if len({p.planner_id for p in candidates}) != len(candidates):
        raise ValueError("planner_id values must be unique")
    reference_cap = candidates[0].budget_cap
    if any(plan.budget_cap != reference_cap for plan in candidates[1:]):
        raise ValueError("all planners must share the identical declared budget cap")
    return tuple(p.plan_id for p in candidates)
