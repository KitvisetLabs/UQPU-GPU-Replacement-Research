"""Evidence-gated contract for foundational physics/mathematics hypotheses."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

ALLOWED_EVIDENCE_LEVELS = {
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

REQUIRED_FIELDS = (
    "mathematical_formulation",
    "causal_mechanism",
    "target_bottleneck",
    "known_constraints",
    "scaling_law",
    "falsifier",
    "observable",
    "baseline",
    "resource_accounting",
)


@dataclass(frozen=True)
class FrontierHypothesis:
    name: str
    layer: str
    evidence_level: str
    mathematical_formulation: str
    causal_mechanism: str
    target_bottleneck: str
    known_constraints: tuple[str, ...]
    scaling_law: str
    falsifier: str
    observable: str
    baseline: str
    resource_accounting: tuple[str, ...]

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("name is required")
        if not self.layer.strip():
            raise ValueError("layer is required")
        if self.evidence_level not in ALLOWED_EVIDENCE_LEVELS:
            raise ValueError("evidence_level is not in the governed project taxonomy")
        missing = self.missing_required_fields()
        if missing:
            raise ValueError("missing frontier fields: " + ", ".join(missing))

    def missing_required_fields(self) -> tuple[str, ...]:
        missing: list[str] = []
        scalar_names = (
            "mathematical_formulation",
            "causal_mechanism",
            "target_bottleneck",
            "scaling_law",
            "falsifier",
            "observable",
            "baseline",
        )
        for field_name in scalar_names:
            if not str(getattr(self, field_name)).strip():
                missing.append(field_name)
        if not _nonempty_strings(self.known_constraints):
            missing.append("known_constraints")
        if not _nonempty_strings(self.resource_accounting):
            missing.append("resource_accounting")
        return tuple(missing)

    @property
    def testable(self) -> bool:
        """True when the proposal is precise enough to attempt falsification.

        This does not mean the proposal is correct or experimentally supported.
        """
        return not self.missing_required_fields()


def _nonempty_strings(values: Iterable[str]) -> bool:
    vals = tuple(values)
    return bool(vals) and all(isinstance(v, str) and v.strip() for v in vals)
