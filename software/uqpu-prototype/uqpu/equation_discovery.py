"""Evidence-gated contract for AI-assisted scientific equation discovery.

This module does not decide whether a proposed equation is physically true.
It only enforces the minimum metadata required before a candidate may be
considered testable within the UQPU foundational-research program.
"""

from __future__ import annotations

from dataclasses import dataclass, field
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

    def validate(self) -> None:
        if not self.equation_id.strip():
            raise ValueError("equation_id is required")
        if not self.baseline_model.strip():
            raise ValueError("baseline_model is required")
        if not self.proposed_equation.strip():
            raise ValueError("proposed_equation is required")
        if not self.variables_and_units:
            raise ValueError("variables_and_units is required")
        if not self.domain_and_assumptions:
            raise ValueError("domain_and_assumptions is required")
        if not self.known_constraints_checked:
            raise ValueError("known_constraints_checked is required")
        if not self.scaling_or_limiting_cases:
            raise ValueError("scaling_or_limiting_cases is required")
        if not self.falsifier.strip():
            raise ValueError("falsifier is required")
        if not self.discriminating_observables:
            raise ValueError("discriminating_observables is required")
        if self.evidence_level not in _ALLOWED_EVIDENCE:
            raise ValueError(f"unknown evidence level: {self.evidence_level}")
        if self.independent_validation_count < 0:
            raise ValueError("independent_validation_count cannot be negative")
        for value in (self.heldout_baseline_error, self.heldout_candidate_error):
            if value is not None and value < 0:
                raise ValueError("held-out errors cannot be negative")

    @property
    def has_heldout_improvement(self) -> bool:
        if self.heldout_baseline_error is None or self.heldout_candidate_error is None:
            return False
        return self.heldout_candidate_error < self.heldout_baseline_error

    @property
    def testable(self) -> bool:
        try:
            self.validate()
        except ValueError:
            return False
        return bool(self.independent_validation_plan or self.data_or_proof_provenance)

    @property
    def ready_for_physical_candidate_claim(self) -> bool:
        """Conservative promotion guard, not a declaration of physical truth.

        Even True only means the record is sufficiently evidenced to discuss as
        a physically supported *candidate relation*. It never means universal law.
        """
        try:
            self.validate()
        except ValueError:
            return False
        if self.evidence_level not in {"LAB_RESULT", "PUBLISHED_EXPERIMENT", "PROTOTYPE", "PRODUCTION_DATA"}:
            return False
        if self.independent_validation_count < 1:
            return False
        if not self.has_heldout_improvement:
            return False
        return bool(self.data_or_proof_provenance and self.independent_validation_plan)


def required_discovery_fields() -> tuple[str, ...]:
    """Return the permanent minimum contract fields for equation candidates."""
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
    )


def missing_required_text(items: Iterable[str]) -> bool:
    """Small helper used by research ingestion tools."""
    return any(not str(item).strip() for item in items)
