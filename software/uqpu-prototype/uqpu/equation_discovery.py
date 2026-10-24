"""Evidence-gated contract for AI-assisted scientific equation discovery.

This module does not decide whether a proposed equation is physically true.
It records the evidence stages required to make a candidate testable and
prevents formal proof metadata from being mistaken for empirical validation.
"""
from __future__ import annotations

from dataclasses import dataclass, field
import re
from typing import Iterable


_ALLOWED_EVIDENCE = {
    "CONCEPT",
    "THEORY",
    "MODEL_ONLY",
    "SIMULATION",
    "DEVICE_MODEL",
    "FABRICATION_PROPOSAL",
    "LAB_RESULT",
    "PUBLISHED_EXPERIMENT",
    "PROTOTYPE",
    "PRODUCTION_DATA",
    "ROADMAP",
    "DRY_RUN_ONLY",
    "RESOURCE_BLOCKED",
    "TOOL_BLOCKED",
    "DATA_BLOCKED",
    "CURRENTLY_INFEASIBLE",
}
_FORMAL_STATUSES = {"NOT_ATTEMPTED", "PROVED", "DISPROVED", "UNRESOLVED", "NOT_APPLICABLE"}
_COUNTEREXAMPLE_STATUSES = {
    "NOT_ATTEMPTED",
    "SEARCHED_NONE_FOUND",
    "COUNTEREXAMPLE_FOUND",
    "INCONCLUSIVE",
}
_REPLICATION_STATUSES = {"NOT_ATTEMPTED", "REPLICATED", "FAILED", "INCONCLUSIVE"}
_SHA256_RE = re.compile(r"sha256:[0-9a-f]{64}")


def _is_sha256(value: str) -> bool:
    return bool(_SHA256_RE.fullmatch(value))


@dataclass(frozen=True)
class EquationHypothesis:
    equation_id: str
    baseline_model: str
    proposed_equation: str
    variables_and_units: tuple[str, ...]
    domain_and_assumptions: tuple[str, ...]
    known_constraints_checked: tuple[str, ...]
    scaling_or_limiting_cases: tuple[str, ...]
    falsifier: str
    discriminating_observables: tuple[str, ...]
    evidence_level: str = "CONCEPT"
    data_or_proof_provenance: tuple[str, ...] = field(default_factory=tuple)
    independent_validation_plan: tuple[str, ...] = field(default_factory=tuple)
    claimed_mechanism: str = ""
    heldout_baseline_error: float | None = None
    heldout_candidate_error: float | None = None
    independent_validation_count: int = 0

    # Proof-carrying metadata. A proof is relative to the declared formal
    # system and assumptions; it is never a substitute for empirical evidence.
    formal_verification_status: str = "NOT_ATTEMPTED"
    formal_system: str = ""
    formal_statement_hash: str = ""
    formal_assumptions: tuple[str, ...] = field(default_factory=tuple)
    formal_proof_provenance: tuple[str, ...] = field(default_factory=tuple)

    # Generalization, counterexample and experiment gates.
    heldout_split_hash: str = ""
    counterexample_search_status: str = "NOT_ATTEMPTED"
    counterexample_search_provenance: tuple[str, ...] = field(default_factory=tuple)
    discriminating_experiment_protocol: str = ""

    # Independent replication is tracked separately from an author-supplied
    # proof artifact or a held-out score.
    independent_replication_status: str = "NOT_ATTEMPTED"
    independent_replication_provenance: tuple[str, ...] = field(default_factory=tuple)

    def validate(self) -> None:
        for name in ("equation_id", "baseline_model", "proposed_equation", "falsifier",
                     "discriminating_experiment_protocol"):
            if not getattr(self, name).strip():
                raise ValueError(f"{name} is required")
        for name in (
            "variables_and_units",
            "domain_and_assumptions",
            "known_constraints_checked",
            "scaling_or_limiting_cases",
            "discriminating_observables",
            "formal_assumptions",
        ):
            value = getattr(self, name)
            if name == "formal_assumptions" and self.formal_verification_status in {
                "NOT_ATTEMPTED", "NOT_APPLICABLE", "UNRESOLVED"
            }:
                continue
            if not value or any(not isinstance(item, str) or not item.strip() for item in value):
                raise ValueError(f"{name} is required and must contain non-empty strings")
        if not _is_sha256(self.heldout_split_hash):
            raise ValueError("heldout_split_hash must be a pinned sha256:<64 lowercase hex> value")
        if self.evidence_level not in _ALLOWED_EVIDENCE:
            raise ValueError(f"unknown evidence level: {self.evidence_level}")
        if self.formal_verification_status not in _FORMAL_STATUSES:
            raise ValueError(f"unknown formal_verification_status: {self.formal_verification_status}")
        if self.counterexample_search_status not in _COUNTEREXAMPLE_STATUSES:
            raise ValueError(f"unknown counterexample_search_status: {self.counterexample_search_status}")
        if self.independent_replication_status not in _REPLICATION_STATUSES:
            raise ValueError(f"unknown independent_replication_status: {self.independent_replication_status}")
        if self.independent_validation_count < 0:
            raise ValueError("independent_validation_count cannot be negative")
        for value in (self.heldout_baseline_error, self.heldout_candidate_error):
            if value is not None and (value < 0 or not float(value) < float("inf")):
                raise ValueError("held-out errors must be finite and >= 0")
        if self.formal_verification_status in {"PROVED", "DISPROVED"}:
            if not self.formal_system.strip():
                raise ValueError("formal_system is required for a completed formal check")
            if not _is_sha256(self.formal_statement_hash):
                raise ValueError("formal_statement_hash must be a pinned sha256:<64 lowercase hex> value")
            if not self.formal_assumptions or any(not item.strip() for item in self.formal_assumptions):
                raise ValueError("formal_assumptions are required for a completed formal check")
            if not self.formal_proof_provenance or any(not item.strip() for item in self.formal_proof_provenance):
                raise ValueError("formal_proof_provenance is required for a completed formal check")
        if self.counterexample_search_status in {"SEARCHED_NONE_FOUND", "COUNTEREXAMPLE_FOUND"}:
            if not self.counterexample_search_provenance or any(
                not item.strip() for item in self.counterexample_search_provenance
            ):
                raise ValueError("counterexample_search_provenance is required for a completed search")
        if self.independent_replication_status in {"REPLICATED", "FAILED", "INCONCLUSIVE"}:
            if not self.independent_replication_provenance or any(
                not item.strip() for item in self.independent_replication_provenance
            ):
                raise ValueError("independent_replication_provenance is required for a completed replication attempt")

    @property
    def has_heldout_improvement(self) -> bool:
        if self.heldout_baseline_error is None or self.heldout_candidate_error is None:
            return False
        return self.heldout_candidate_error < self.heldout_baseline_error

    @property
    def testable(self) -> bool:
        try:
            self.validate()
        except (ValueError, TypeError, AttributeError):
            return False
        return bool(self.independent_validation_plan or self.data_or_proof_provenance)

    @property
    def ready_for_physical_candidate_claim(self) -> bool:
        """Conservative empirical gate, never a declaration of a physical law.

        Formal proof alone cannot satisfy this gate. The candidate must also
        have empirical evidence, held-out improvement, a completed
        counterexample search, a discriminating experiment protocol, and an
        independently replicated result. Even True means only that the record
        may be discussed as a supported candidate relation in its stated domain.
        """
        try:
            self.validate()
        except (ValueError, TypeError, AttributeError):
            return False
        if self.evidence_level not in {
            "LAB_RESULT", "PUBLISHED_EXPERIMENT", "PROTOTYPE", "PRODUCTION_DATA"
        }:
            return False
        if self.formal_verification_status == "DISPROVED":
            return False
        if self.independent_validation_count < 1 or not self.has_heldout_improvement:
            return False
        if self.counterexample_search_status != "SEARCHED_NONE_FOUND":
            return False
        if self.independent_replication_status != "REPLICATED":
            return False
        return bool(
            self.data_or_proof_provenance
            and self.independent_validation_plan
            and self.independent_replication_provenance
        )


def required_discovery_fields() -> tuple[str, ...]:
    """Return the governed minimum fields for equation candidates."""
    return (
        "equation_id",
        "baseline_model",
        "proposed_equation",
        "variables_and_units",
        "domain_and_assumptions",
        "known_constraints_checked",
        "scaling_or_limiting_cases",
        "falsifier",
        "discriminating_observables",
        "evidence_level",
        "data_or_proof_provenance",
        "independent_validation_plan",
        "heldout_split_hash",
        "formal_verification_status",
        "formal_system",
        "formal_statement_hash",
        "formal_assumptions",
        "formal_proof_provenance",
        "counterexample_search_status",
        "counterexample_search_provenance",
        "discriminating_experiment_protocol",
        "independent_replication_status",
        "independent_replication_provenance",
    )


def missing_required_text(items: Iterable[str]) -> bool:
    """Small helper used by research ingestion tools."""
    return any(not str(item).strip() for item in items)
