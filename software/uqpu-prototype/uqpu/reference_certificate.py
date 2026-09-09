from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import hashlib
import json


class ReferenceKind(str, Enum):
    EXACT_OPTIMUM = "EXACT_OPTIMUM"
    PROVEN_LOWER_BOUND = "PROVEN_LOWER_BOUND"
    BEST_KNOWN_FEASIBLE = "BEST_KNOWN_FEASIBLE"


@dataclass(frozen=True)
class ObjectiveReference:
    contract_id: str
    kind: ReferenceKind
    objective: float
    method: str
    evidence_level: str
    source: str
    notes: str = ""

    def validate(self) -> None:
        if not self.contract_id or not self.method or not self.evidence_level or not self.source:
            raise ValueError("reference provenance fields are required")

    @property
    def certificate_id(self) -> str:
        self.validate()
        payload={
            "contract_id":self.contract_id,
            "kind":self.kind.value,
            "objective":self.objective,
            "method":self.method,
            "evidence_level":self.evidence_level,
            "source":self.source,
            "notes":self.notes,
        }
        return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()[:20]


@dataclass(frozen=True)
class QualityAssessment:
    accepted: bool
    verified_quality: bool
    relative_gap: float
    reference_kind: ReferenceKind
    certificate_id: str


def assess_minimization_quality(
    candidate_objective: float,
    reference: ObjectiveReference,
    allowed_relative_gap: float,
) -> QualityAssessment:
    reference.validate()
    if allowed_relative_gap < 0:
        raise ValueError("allowed_relative_gap must be non-negative")
    scale=max(abs(reference.objective),1.0)
    gap=max(0.0,(candidate_objective-reference.objective)/scale)
    accepted=gap <= allowed_relative_gap
    verified=accepted and reference.kind in {
        ReferenceKind.EXACT_OPTIMUM,
        ReferenceKind.PROVEN_LOWER_BOUND,
    }
    return QualityAssessment(
        accepted=accepted,
        verified_quality=verified,
        relative_gap=gap,
        reference_kind=reference.kind,
        certificate_id=reference.certificate_id,
    )
