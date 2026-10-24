"""Offline preregistration guard for progressive symbolic-law discovery.

This module validates a fair, held-out comparison between one-shot symbolic
regression and a progressive chain of interpretable knowledge units. It does
not implement CoSR, validate a paper's claims, or determine physical truth.
"""
from __future__ import annotations

from dataclasses import dataclass
import re


_REQUIRED_CONSTRAINTS = (
    "dimensional_consistency",
    "symmetry",
    "conservation",
    "causality",
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def _positive_int(value: object, field_name: str) -> None:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{field_name} must be a positive integer")


def _nonempty(value: str, field_name: str) -> None:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{field_name} is required")


@dataclass(frozen=True)
class ResourceBudget:
    """Hard caps that must be identical for both comparison arms."""

    candidate_evaluations: int
    wall_clock_seconds: int
    max_expression_nodes: int
    max_training_rows: int

    def validate(self) -> None:
        for field_name in (
            "candidate_evaluations",
            "wall_clock_seconds",
            "max_expression_nodes",
            "max_training_rows",
        ):
            _positive_int(getattr(self, field_name), field_name)


@dataclass(frozen=True)
class DataSplits:
    """Committed hashes for non-overlapping train, validation and held-out data."""

    train_sha256: str
    validation_sha256: str
    heldout_sha256: str

    def validate(self) -> None:
        values = (self.train_sha256, self.validation_sha256, self.heldout_sha256)
        names = ("train_sha256", "validation_sha256", "heldout_sha256")
        for name, value in zip(names, values):
            if not isinstance(value, str) or not _SHA256.fullmatch(value):
                raise ValueError(f"{name} must be a lowercase SHA-256 digest")
        if len(set(values)) != len(values):
            raise ValueError("train, validation and held-out data hashes must be distinct")


@dataclass(frozen=True)
class DiscoveryStage:
    """One named interpretable unit in a progressive discovery chain."""

    stage_id: str
    knowledge_unit: str
    parent_stage_ids: tuple[str, ...]
    variables_and_units: tuple[str, ...]
    constraint_audit: tuple[str, ...]
    limiting_cases: tuple[str, ...]
    falsifier: str
    discriminating_observable: str
    candidate_evaluations: int
    heldout_used_for_selection: bool = False

    def validate(self) -> None:
        _nonempty(self.stage_id, "stage_id")
        _nonempty(self.knowledge_unit, "knowledge_unit")
        _nonempty(self.falsifier, "falsifier")
        _nonempty(self.discriminating_observable, "discriminating_observable")
        _positive_int(self.candidate_evaluations, "stage candidate_evaluations")
        if not isinstance(self.variables_and_units, tuple) or not self.variables_and_units or any(not isinstance(x, str) or not x.strip() for x in self.variables_and_units):
            raise ValueError("variables_and_units must be a tuple with explicit units")
        if not isinstance(self.limiting_cases, tuple) or not self.limiting_cases or any(not isinstance(x, str) or not x.strip() for x in self.limiting_cases):
            raise ValueError("limiting_cases must be a tuple of explicit limiting cases")
        if not isinstance(self.parent_stage_ids, tuple) or any(not isinstance(x, str) or not x.strip() for x in self.parent_stage_ids) or len(set(self.parent_stage_ids)) != len(self.parent_stage_ids):
            raise ValueError("parent_stage_ids must be a tuple of unique nonempty IDs")
        if not isinstance(self.heldout_used_for_selection, bool) or self.heldout_used_for_selection:
            raise ValueError("held-out data must not be used for selection or repair")
        self._validate_constraint_audit()

    def _validate_constraint_audit(self) -> None:
        if not isinstance(self.constraint_audit, tuple):
            raise ValueError("constraint_audit must be a tuple")
        seen: dict[str, str] = {}
        for entry in self.constraint_audit:
            if not isinstance(entry, str):
                raise ValueError("constraint_audit entries must be strings")
            parts = entry.split(":", 2)
            if len(parts) < 2:
                raise ValueError("constraint audit must use 'constraint: checked' or an explained not_applicable status")
            key, status = parts[0].strip(), parts[1].strip().lower()
            if key not in _REQUIRED_CONSTRAINTS or key in seen:
                raise ValueError("constraint audit must cover each required constraint exactly once")
            if status == "checked":
                if len(parts) != 2:
                    raise ValueError(f"{key} checked audit must not include an extra reason field")
                seen[key] = status
            elif status == "not_applicable":
                if len(parts) != 3 or not parts[2].strip():
                    raise ValueError(f"{key} marked not_applicable requires a reason")
                seen[key] = status
            else:
                raise ValueError(f"unsupported constraint audit status for {key}: {status}")
        if set(seen) != set(_REQUIRED_CONSTRAINTS):
            missing = sorted(set(_REQUIRED_CONSTRAINTS) - set(seen))
            raise ValueError("constraint audit incomplete: " + ", ".join(missing))


@dataclass(frozen=True)
class ProgressiveDiscoveryPlan:
    """Preregistered comparison contract; not an execution result."""

    experiment_id: str
    incumbent_model: str
    one_shot_method: str
    progressive_method: str
    grammar_sha256: str
    evaluator_version: str
    evaluation_metric: str
    optimization_direction: str
    data_splits: DataSplits
    one_shot_budget: ResourceBudget
    progressive_budget: ResourceBudget
    stages: tuple[DiscoveryStage, ...]
    pre_registered: bool = True
    heldout_unblinded_before_freeze: bool = False
    counterexample_search_required: bool = True
    failed_candidates_retained: bool = True
    evidence_class: str = "MODEL_ONLY"
    provider_calls: int = 0
    qpu_jobs: int = 0

    def validate(self) -> None:
        for field_name in (
            "experiment_id",
            "incumbent_model",
            "one_shot_method",
            "progressive_method",
            "evaluator_version",
            "evaluation_metric",
        ):
            _nonempty(getattr(self, field_name), field_name)
        if self.one_shot_method.strip() == self.progressive_method.strip():
            raise ValueError("comparison arms must name distinct search methods")
        if not isinstance(self.grammar_sha256, str) or not _SHA256.fullmatch(self.grammar_sha256):
            raise ValueError("grammar_sha256 must be a lowercase SHA-256 digest")
        if not isinstance(self.optimization_direction, str) or self.optimization_direction not in {"minimize", "maximize"}:
            raise ValueError("optimization_direction must be minimize or maximize")
        if not isinstance(self.data_splits, DataSplits):
            raise ValueError("data_splits must be a DataSplits instance")
        if not isinstance(self.one_shot_budget, ResourceBudget):
            raise ValueError("one_shot_budget must be a ResourceBudget instance")
        if not isinstance(self.progressive_budget, ResourceBudget):
            raise ValueError("progressive_budget must be a ResourceBudget instance")
        self.data_splits.validate()
        self.one_shot_budget.validate()
        self.progressive_budget.validate()
        if self.one_shot_budget != self.progressive_budget:
            raise ValueError("one-shot and progressive arms must have identical resource budgets")
        if not isinstance(self.pre_registered, bool) or not self.pre_registered:
            raise ValueError("the experiment must be preregistered before held-out evaluation")
        if not isinstance(self.heldout_unblinded_before_freeze, bool) or self.heldout_unblinded_before_freeze:
            raise ValueError("heldout_unblinded_before_freeze must be boolean false; held-out data cannot be unblinded before the plan is frozen")
        if not isinstance(self.counterexample_search_required, bool) or not self.counterexample_search_required or not isinstance(self.failed_candidates_retained, bool) or not self.failed_candidates_retained:
            raise ValueError("counterexample search and failed-candidate retention are mandatory")
        if self.evidence_class != "MODEL_ONLY":
            raise ValueError("this offline protocol is MODEL_ONLY and cannot promote a physical-law claim")
        for field_name in ("provider_calls", "qpu_jobs"):
            value = getattr(self, field_name)
            if isinstance(value, bool) or not isinstance(value, int) or value != 0:
                raise ValueError("offline preregistration must make zero provider calls and zero QPU jobs")
        if not isinstance(self.stages, tuple) or len(self.stages) < 2:
            raise ValueError("progressive comparison requires at least two ordered stages")

        seen: set[str] = set()
        total_evaluations = 0
        for index, stage in enumerate(self.stages):
            if not isinstance(stage, DiscoveryStage):
                raise ValueError("each stages entry must be a DiscoveryStage instance")
            stage.validate()
            if stage.stage_id in seen:
                raise ValueError("stage_id values must be unique")
            if index == 0 and stage.parent_stage_ids:
                raise ValueError("the first stage cannot depend on a later or absent stage")
            if index > 0 and not stage.parent_stage_ids:
                raise ValueError("every later stage must name at least one earlier knowledge unit")
            if any(parent not in seen for parent in stage.parent_stage_ids):
                raise ValueError("stage dependencies must point only to earlier stages")
            seen.add(stage.stage_id)
            total_evaluations += stage.candidate_evaluations
        if total_evaluations != self.progressive_budget.candidate_evaluations:
            raise ValueError("sum of stage candidate evaluations must equal the progressive-arm budget")

    @property
    def physical_law_promotion_allowed(self) -> bool:
        """A plan alone can never establish a physical law."""
        return False
