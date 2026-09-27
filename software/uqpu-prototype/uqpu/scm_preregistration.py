"""SCM Phase-2 preregistration contract.

Validates that an empirical protocol is specified before data collection.
Passing this validator is administrative/methodological readiness only.
"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class SCMPreregistration:
    study_id: str
    protocol_version: str
    primary_hypothesis: str
    null_hypothesis: str
    primary_outcome: str
    sample_size: int
    stopping_rule: str
    randomization_method: str
    blinding_roles: tuple[str, ...]
    exclusion_rules: tuple[str, ...]
    leakage_audit_items: tuple[str, ...]
    calibration_plan: str
    analysis_plan: str
    replication_plan: str
    human_participants: bool = False
    ethics_approval_ref: str = ""
    evidence_class: str = "PREREGISTRATION_ONLY_NO_EMPIRICAL_RESULT"

REQUIRED_LEAKAGE_ITEMS = (
    "target_metadata", "filenames", "trial_timing", "network_traffic",
    "operator_contact", "audio_visual_cues", "rng_custody",
    "ai_retrieval_or_training_contamination", "post_selection",
)

def validate_preregistration(p: SCMPreregistration) -> tuple[str, ...]:
    errors=[]
    required=("study_id","protocol_version","primary_hypothesis","null_hypothesis",
              "primary_outcome","stopping_rule","randomization_method",
              "calibration_plan","analysis_plan","replication_plan")
    for field in required:
        if not getattr(p,field).strip():
            errors.append(f"missing:{field}")
    if p.sample_size <= 0:
        errors.append("invalid:sample_size")
    if len(p.blinding_roles) < 2:
        errors.append("insufficient:blinding_roles")
    if not p.exclusion_rules:
        errors.append("missing:exclusion_rules")
    missing=sorted(set(REQUIRED_LEAKAGE_ITEMS)-set(p.leakage_audit_items))
    errors.extend(f"missing_leakage:{x}" for x in missing)
    if p.human_participants and not p.ethics_approval_ref.strip():
        errors.append("missing:ethics_approval_ref")
    return tuple(errors)

def ready_to_collect(p: SCMPreregistration) -> bool:
    return not validate_preregistration(p)
