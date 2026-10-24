"""Offline preregistration guard for progressive symbolic-law discovery.

This module validates a fair, held-out comparison between one-shot symbolic
regression and a progressive chain of interpretable knowledge units. It does
not implement CoSR, validate a paper's claims, or determine physical truth.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
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


_SPLIT_SCHEMA_VERSION = "uqpu-split-membership-v1"
_SPLIT_CANONICALIZATION_VERSION = "sorted-json-utf8-v1"


def _json_sha256(payload: object) -> str:
    canonical = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def _validated_sample_ids(values: object, split_name: str) -> set[str]:
    if not isinstance(values, tuple) or not values:
        raise ValueError(f"{split_name}_ids must be a nonempty tuple")
    if any(
        not isinstance(value, str)
        or not value
        or value != value.strip()
        or any(character in value for character in ("\n", "\r", "\0"))
        for value in values
    ):
        raise ValueError(f"{split_name}_ids must contain normalized, nonempty string identifiers")
    if len(set(values)) != len(values):
        raise ValueError(f"{split_name}_ids must not contain duplicate identifiers")
    return set(values)


def _split_manifest_digest(
    source_dataset_sha256: str,
    sample_id_namespace: str,
    split_name: str,
    sample_ids: tuple[str, ...],
    schema_version: str,
    canonicalization_version: str,
) -> str:
    return _json_sha256(
        {
            "canonicalization_version": canonicalization_version,
            "sample_id_namespace": sample_id_namespace,
            "sample_ids": sorted(sample_ids),
            "schema_version": schema_version,
            "source_dataset_sha256": source_dataset_sha256,
            "split_name": split_name,
        }
    )


@dataclass(frozen=True)
class DataSplits:
    """Versioned record-membership certificate bound to a frozen dataset digest.

    This validates identifier-level disjointness and deterministic manifest
    hashes. The data loader must still independently hash the raw dataset bytes
    and derive these stable IDs from that exact dataset before accepting a run.
    """

    source_dataset_sha256: str
    sample_id_namespace: str
    train_ids: tuple[str, ...]
    validation_ids: tuple[str, ...]
    heldout_ids: tuple[str, ...]
    train_manifest_sha256: str
    validation_manifest_sha256: str
    heldout_manifest_sha256: str
    schema_version: str = _SPLIT_SCHEMA_VERSION
    canonicalization_version: str = _SPLIT_CANONICALIZATION_VERSION

    @classmethod
    def from_ids(
        cls,
        *,
        source_dataset_sha256: str,
        sample_id_namespace: str,
        train_ids: tuple[str, ...],
        validation_ids: tuple[str, ...],
        heldout_ids: tuple[str, ...],
    ) -> "DataSplits":
        _nonempty(sample_id_namespace, "sample_id_namespace")
        if not isinstance(source_dataset_sha256, str) or not _SHA256.fullmatch(source_dataset_sha256):
            raise ValueError("source_dataset_sha256 must be a lowercase SHA-256 digest")
        for name, values in (
            ("train", train_ids),
            ("validation", validation_ids),
            ("heldout", heldout_ids),
        ):
            _validated_sample_ids(values, name)
        train_set, validation_set, heldout_set = map(
            set, (train_ids, validation_ids, heldout_ids)
        )
        if (
            train_set & validation_set
            or train_set & heldout_set
            or validation_set & heldout_set
        ):
            raise ValueError("train, validation and held-out sample IDs must be pairwise disjoint")
        schema_version = _SPLIT_SCHEMA_VERSION
        canonicalization_version = _SPLIT_CANONICALIZATION_VERSION
        candidate = cls(
            source_dataset_sha256=source_dataset_sha256,
            sample_id_namespace=sample_id_namespace,
            train_ids=train_ids,
            validation_ids=validation_ids,
            heldout_ids=heldout_ids,
            train_manifest_sha256=_split_manifest_digest(
                source_dataset_sha256, sample_id_namespace, "train", train_ids,
                schema_version, canonicalization_version
            ),
            validation_manifest_sha256=_split_manifest_digest(
                source_dataset_sha256, sample_id_namespace, "validation", validation_ids,
                schema_version, canonicalization_version
            ),
            heldout_manifest_sha256=_split_manifest_digest(
                source_dataset_sha256, sample_id_namespace, "heldout", heldout_ids,
                schema_version, canonicalization_version
            ),
            schema_version=schema_version,
            canonicalization_version=canonicalization_version,
        )
        candidate.validate()
        return candidate

    def validate(self) -> None:
        if not isinstance(self.source_dataset_sha256, str) or not _SHA256.fullmatch(self.source_dataset_sha256):
            raise ValueError("source_dataset_sha256 must be a lowercase SHA-256 digest")
        _nonempty(self.sample_id_namespace, "sample_id_namespace")
        if self.schema_version != _SPLIT_SCHEMA_VERSION:
            raise ValueError("unsupported split manifest schema_version")
        if self.canonicalization_version != _SPLIT_CANONICALIZATION_VERSION:
            raise ValueError("unsupported split manifest canonicalization_version")

        train_set = _validated_sample_ids(self.train_ids, "train")
        validation_set = _validated_sample_ids(self.validation_ids, "validation")
        heldout_set = _validated_sample_ids(self.heldout_ids, "heldout")
        if (
            train_set & validation_set
            or train_set & heldout_set
            or validation_set & heldout_set
        ):
            raise ValueError("train, validation and held-out sample IDs must be pairwise disjoint")

        for name, declared, ids in (
            ("train", self.train_manifest_sha256, self.train_ids),
            ("validation", self.validation_manifest_sha256, self.validation_ids),
            ("heldout", self.heldout_manifest_sha256, self.heldout_ids),
        ):
            if not isinstance(declared, str) or not _SHA256.fullmatch(declared):
                raise ValueError(f"{name}_manifest_sha256 must be a lowercase SHA-256 digest")
            expected = _split_manifest_digest(
                self.source_dataset_sha256,
                self.sample_id_namespace,
                name,
                ids,
                self.schema_version,
                self.canonicalization_version,
            )
            if declared != expected:
                raise ValueError(f"{name} manifest/data digest mismatch")

    def to_manifest(self) -> dict[str, object]:
        self.validate()
        return {
            "schema_version": self.schema_version,
            "canonicalization_version": self.canonicalization_version,
            "source_dataset_sha256": self.source_dataset_sha256,
            "sample_id_namespace": self.sample_id_namespace,
            "splits": {
                "train": {
                    "sample_ids": sorted(self.train_ids),
                    "manifest_sha256": self.train_manifest_sha256,
                },
                "validation": {
                    "sample_ids": sorted(self.validation_ids),
                    "manifest_sha256": self.validation_manifest_sha256,
                },
                "heldout": {
                    "sample_ids": sorted(self.heldout_ids),
                    "manifest_sha256": self.heldout_manifest_sha256,
                },
            },
        }

    @property
    def manifest_sha256(self) -> str:
        """Stable digest of the full split certificate."""
        return _json_sha256(self.to_manifest())


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
