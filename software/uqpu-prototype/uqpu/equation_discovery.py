"""Evidence-gated contract for AI-assisted scientific equation discovery.

This module does not decide whether a proposed equation is physically true.
It only enforces the minimum metadata required before a candidate may be
considered testable within the UQPU foundational-research program.
"""

from __future__ import annotations

import math
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

        for field_name, values in (
            ("variables_and_units", self.variables_and_units),
            ("domain_and_assumptions", self.domain_and_assumptions),
            ("known_constraints_checked", self.known_constraints_checked),
            ("scaling_or_limiting_cases", self.scaling_or_limiting_cases),
            ("discriminating_observables", self.discriminating_observables),
            ("data_or_proof_provenance", self.data_or_proof_provenance),
            ("independent_validation_plan", self.independent_validation_plan),
        ):
            _require_nonempty_strings(field_name, values)

        if not self.falsifier.strip():
            raise ValueError("falsifier is required")
        if self.evidence_level not in _ALLOWED_EVIDENCE:
            raise ValueError(f"unknown evidence level: {self.evidence_level}")
        if (
            isinstance(self.independent_validation_count, bool)
            or not isinstance(self.independent_validation_count, int)
            or self.independent_validation_count < 0
        ):
            raise ValueError("independent_validation_count must be an integer >= 0")

        for name, value in (
            ("heldout_baseline_error", self.heldout_baseline_error),
            ("heldout_candidate_error", self.heldout_candidate_error),
        ):
            if value is None:
                continue
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValueError(f"{name} must be a finite numeric value >= 0")
            if not math.isfinite(float(value)) or value < 0:
                raise ValueError(f"{name} must be a finite numeric value >= 0")

    @property
    def has_heldout_improvement(self) -> bool:
        if self.heldout_baseline_error is None or self.heldout_candidate_error is None:
            return False
        return self.heldout_candidate_error < self.heldout_baseline_error

    @property
    def testable(self) -> bool:
        """True only when all required provenance and validation fields exist.

        This is a testability contract, not evidence that a candidate is correct.
        """
        try:
            self.validate()
        except ValueError:
            return False
        return True

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


def _require_nonempty_strings(field_name: str, values: Iterable[str]) -> None:
    """Reject absent, blank, or non-text entries in a required tuple field."""
    items = tuple(values)
    if not items or any(not isinstance(item, str) or not item.strip() for item in items):
        raise ValueError(f"{field_name} must contain non-empty strings")
