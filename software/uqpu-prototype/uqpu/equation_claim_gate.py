"""Fail-closed metadata gate for alternative physical-equation hypotheses.

This gate checks whether a claim is specified well enough to test. It does not
prove a theorem, validate a physical model, or promote an equation to a law.
"""
from __future__ import annotations

from dataclasses import dataclass
from .frontier_hypothesis import ALLOWED_EVIDENCE_LEVELS

_TEXT_FIELDS = (
    "claim_id",
    "incumbent_assumption",
    "incumbent_model",
    "alternative_equation",
    "dimensional_analysis",
    "falsifier",
    "discriminating_observable",
    "heldout_prediction",
    "counterexample_search_plan",
    "proof_or_simulation_plan",
    "experiment_plan",
    "independent_validation_plan",
    "device_or_system_consequence",
    "economic_consequence",
    "source_provenance",
    "failure_recording_plan",
)
_SEQUENCE_FIELDS = (
    "variables_and_units",
    "domain_and_assumptions",
    "symmetry_checks",
    "conservation_checks",
    "causality_checks",
    "limiting_cases",
)


@dataclass(frozen=True)
class EquationClaimGate:
    """Structured preflight for INV-034/INV-035 alternative-equation work.

    A successful validate means only that required falsification metadata
    is present. All entries are plans/claims supplied by the researcher and
    still require independent checking and, where applicable, experiments.
    """

    claim_id: str
    incumbent_assumption: str
    incumbent_model: str
    alternative_equation: str
    variables_and_units: tuple[str, ...]
    domain_and_assumptions: tuple[str, ...]
    dimensional_analysis: str
    symmetry_checks: tuple[str, ...]
    conservation_checks: tuple[str, ...]
    causality_checks: tuple[str, ...]
    limiting_cases: tuple[str, ...]
    falsifier: str
    discriminating_observable: str
    heldout_prediction: str
    counterexample_search_plan: str
    proof_or_simulation_plan: str
    experiment_plan: str
    independent_validation_plan: str
    device_or_system_consequence: str
    economic_consequence: str
    source_provenance: str
    failure_recording_plan: str
    evidence_level: str = "CONCEPT"

    def missing_required_fields(self) -> tuple[str, ...]:
        """Return missing or malformed fields without treating them as truth."""
        missing: list[str] = []
        for name in _TEXT_FIELDS:
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                missing.append(name)
        for name in _SEQUENCE_FIELDS:
            values = getattr(self, name)
            if (
                not isinstance(values, tuple)
                or not values
                or any(not isinstance(item, str) or not item.strip() for item in values)
            ):
                missing.append(name)
        if not isinstance(self.evidence_level, str) or self.evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            missing.append("evidence_level")
        return tuple(missing)

    def validate(self) -> None:
        """Raise ValueError unless the hypothesis has the full test contract."""
        missing = self.missing_required_fields()
        if missing:
            raise ValueError("incomplete equation-claim gate: " + ", ".join(missing))

    @property
    def test_contract_complete(self) -> bool:
        """True means metadata is complete, not that the hypothesis is true."""
        return not self.missing_required_fields()

    @property
    def evidence_boundary(self) -> str:
        """This metadata gate never promotes a hypothesis to a physical law."""
        return "HYPOTHESIS_ONLY_PENDING_INDEPENDENT_EVIDENCE"


def required_equation_claim_fields() -> tuple[str, ...]:
    """Return the stable required-field names for manifests and tests."""
    return _TEXT_FIELDS + _SEQUENCE_FIELDS + ("evidence_level",)
