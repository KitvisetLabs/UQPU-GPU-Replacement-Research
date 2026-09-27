"""SCM-P2-CAL-001 trial-ledger and calibration provenance.

Synthetic fixtures may use this schema. Empirical records must point to actual
raw-data hashes and calibration provenance; the schema never upgrades evidence.
"""
from __future__ import annotations
from dataclasses import dataclass
import hashlib

@dataclass(frozen=True)
class CalibrationRecord:
    calibration_id: str
    sensor_id: str
    method: str
    reference_value: str
    utc_timestamp: str
    operator_role: str

@dataclass(frozen=True)
class TrialRecord:
    trial_id: str
    condition: str
    raw_sha256: str
    calibration_ids: tuple[str, ...]
    excluded: bool
    exclusion_reason: str = ""
    evidence_class: str = "UNCLASSIFIED_RECORD"

ALLOWED_CONDITIONS=("control","known-interference")

def sha256_bytes(data: bytes)->str:
    return hashlib.sha256(data).hexdigest()

def validate_trial(t: TrialRecord, calibrations: tuple[CalibrationRecord,...])->tuple[str,...]:
    errors=[]
    if t.condition not in ALLOWED_CONDITIONS: errors.append("invalid:condition")
    if len(t.raw_sha256)!=64: errors.append("invalid:raw_sha256")
    known={c.calibration_id for c in calibrations}
    if not t.calibration_ids: errors.append("missing:calibration_ids")
    for x in t.calibration_ids:
        if x not in known: errors.append(f"unknown_calibration:{x}")
    if t.excluded and not t.exclusion_reason.strip(): errors.append("missing:exclusion_reason")
    if not t.excluded and t.exclusion_reason.strip(): errors.append("unexpected:exclusion_reason")
    return tuple(errors)
