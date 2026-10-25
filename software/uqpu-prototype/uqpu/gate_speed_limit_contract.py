"""Fail-closed record contract for gate-level quantum speed-limit comparisons.

This module validates provenance and interval bookkeeping only. It does not
implement a quantum-speed-limit theorem or establish a physical law.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import re

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_EVIDENCE_LEVELS = {"MODEL_ONLY", "SIMULATION", "LAB_RESULT", "PUBLISHED_EXPERIMENT"}
_TARGET_KINDS = {"SIMULATOR", "LAB_BENCH", "HARDWARE_TARGET"}
_REQUIRED_SCOPE_CHECKS = {
    "bounded_hamiltonian_spectral_width",
    "target_unitary_identity",
    "initial_final_operator_definition",
    "control_resource_boundary",
    "noise_environment_scope",
    "calibration_validity",
}


@dataclass(frozen=True)
class GateSpeedLimitRecord:
    """Provenance-bound record for one gate and one speed-limit derivation.

    Durations and uncertainties are seconds. The caller must supply a bound
    derived from a fully specified theorem implementation; this contract does
    not derive a bound from an abstract or an incomplete paper.
    """

    record_id: str
    theorem_reference: str
    theorem_source_sha256: str
    bound_derivation_sha256: str
    gate_name: str
    target_id: str
    target_kind: str
    unitary_sha256: str
    hamiltonian_model_sha256: str
    calibration_sha256: str
    observed_duration_seconds: float
    duration_uncertainty_seconds: float
    lower_bound_seconds: float
    bound_uncertainty_seconds: float
    repeat_count: int
    scope_checks: tuple[str, ...]
    observation_method: str
    evidence_level: str = "MODEL_ONLY"
    provider_job_id: str | None = None

    def validate(self) -> None:
        for name in (
            "record_id", "theorem_reference", "gate_name", "target_id",
            "observation_method",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} is required")

        for name in (
            "theorem_source_sha256", "bound_derivation_sha256", "unitary_sha256",
            "hamiltonian_model_sha256", "calibration_sha256",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not _SHA256.fullmatch(value):
                raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")

        if self.target_kind not in _TARGET_KINDS:
            raise ValueError(f"unsupported target_kind: {self.target_kind}")
        if self.evidence_level not in _EVIDENCE_LEVELS:
            raise ValueError(f"unsupported evidence_level: {self.evidence_level}")
        if not isinstance(self.scope_checks, tuple) or not self.scope_checks:
            raise ValueError("scope_checks must be a nonempty tuple")
        if any(not isinstance(item, str) or not item.strip() for item in self.scope_checks):
            raise ValueError("scope_checks entries must be nonempty strings")
        missing = _REQUIRED_SCOPE_CHECKS.difference(self.scope_checks)
        if missing:
            raise ValueError("missing scope checks: " + ", ".join(sorted(missing)))

        if not isinstance(self.repeat_count, int) or isinstance(self.repeat_count, bool) or self.repeat_count <= 0:
            raise ValueError("repeat_count must be a positive integer")

        for name in (
            "observed_duration_seconds", "duration_uncertainty_seconds",
            "lower_bound_seconds", "bound_uncertainty_seconds",
        ):
            raw = getattr(self, name)
            if isinstance(raw, bool):
                raise ValueError(f"{name} must be a finite numeric value")
            try:
                value = float(raw)
            except (TypeError, ValueError) as exc:
                raise ValueError(f"{name} must be a finite numeric value") from exc
            if not math.isfinite(value):
                raise ValueError(f"{name} must be a finite numeric value")
            if name in {"observed_duration_seconds", "lower_bound_seconds"} and value <= 0:
                raise ValueError(f"{name} must be > 0")
            if name in {"duration_uncertainty_seconds", "bound_uncertainty_seconds"} and value < 0:
                raise ValueError(f"{name} must be >= 0")

        if self.target_kind == "SIMULATOR" and self.evidence_level not in {"MODEL_ONLY", "SIMULATION"}:
            raise ValueError("simulator records cannot claim lab or published-experiment evidence")
        if self.target_kind in {"LAB_BENCH", "HARDWARE_TARGET"} and self.evidence_level not in {"LAB_RESULT", "PUBLISHED_EXPERIMENT"}:
            raise ValueError("physical target records require LAB_RESULT or PUBLISHED_EXPERIMENT evidence")
        if self.target_kind == "HARDWARE_TARGET" and not (isinstance(self.provider_job_id, str) and self.provider_job_id.strip()):
            raise ValueError("hardware-target records require a provider_job_id")
        if self.target_kind != "HARDWARE_TARGET" and self.provider_job_id is not None:
            if not isinstance(self.provider_job_id, str) or not self.provider_job_id.strip():
                raise ValueError("provider_job_id must be omitted or nonempty")

    def consistency_classification(self) -> str:
        """Compare uncertainty intervals; never labels a result a law violation."""
        self.validate()
        observed_low = max(0.0, float(self.observed_duration_seconds) - float(self.duration_uncertainty_seconds))
        observed_high = float(self.observed_duration_seconds) + float(self.duration_uncertainty_seconds)
        bound_low = max(0.0, float(self.lower_bound_seconds) - float(self.bound_uncertainty_seconds))
        bound_high = float(self.lower_bound_seconds) + float(self.bound_uncertainty_seconds)
        if observed_high < bound_low:
            return "BELOW_BOUND_REQUIRES_THEOREM_AND_METROLOGY_AUDIT"
        if observed_low >= bound_high:
            return "CONSISTENT_WITH_BOUND_INTERVAL"
        return "OVERLAPPING_UNCERTAINTY_INTERVALS"
