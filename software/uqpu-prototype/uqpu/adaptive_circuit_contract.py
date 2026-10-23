"""Provider-neutral contract for adaptive quantum-circuit capabilities.

This contract validates provenance and declared capability fields only. It does
not contact providers, authorize jobs, or establish workload quality/economics.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
import math
import re
from urllib.parse import urlparse

_ALLOWED_EVIDENCE_CLASSES = {
    "OFFICIAL_PROVIDER_DOCUMENTATION",
    "SIMULATION_ONLY",
    "DRY_RUN_ONLY",
    "MODEL_ONLY",
}
_UTC_TIMESTAMP = re.compile(
    r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d+)?Z$"
)
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class AdaptiveCircuitCapability:
    provider_id: str
    target_id: str
    api_version: str
    evidence_class: str
    source_uri: str
    source_checked_utc: str
    source_sha256: str
    supports_mid_circuit_measurement: bool | None
    supports_reset: bool | None
    supports_classical_conditionals: bool | None
    max_mid_circuit_measurements: int | None = None
    max_conditional_depth: int | None = None
    measurement_feedback_latency_seconds: float | None = None

    def validate(self) -> None:
        for name in (
            "provider_id",
            "target_id",
            "api_version",
            "source_uri",
            "source_checked_utc",
            "source_sha256",
        ):
            value = getattr(self, name)
            if not isinstance(value, str) or not value.strip():
                raise ValueError(f"{name} is required")
        if self.evidence_class not in _ALLOWED_EVIDENCE_CLASSES:
            raise ValueError(
                "unknown evidence_class; hardware results require a separate execution certificate"
            )
        parsed = urlparse(self.source_uri)
        if parsed.scheme != "https" or not parsed.netloc:
            raise ValueError("source_uri must be an HTTPS provenance URL")
        if not _UTC_TIMESTAMP.fullmatch(self.source_checked_utc):
            raise ValueError("source_checked_utc must be RFC3339 UTC ending in Z")
        try:
            datetime.fromisoformat(self.source_checked_utc[:-1] + "+00:00")
        except ValueError as exc:
            raise ValueError("source_checked_utc is not a valid timestamp") from exc
        if not _SHA256.fullmatch(self.source_sha256):
            raise ValueError("source_sha256 must be a lowercase SHA-256 digest")

        for name in (
            "supports_mid_circuit_measurement",
            "supports_reset",
            "supports_classical_conditionals",
        ):
            value = getattr(self, name)
            if value is not None and not isinstance(value, bool):
                raise ValueError(f"{name} must be True, False, or None")

        for name in ("max_mid_circuit_measurements", "max_conditional_depth"):
            value = getattr(self, name)
            if value is not None and (
                isinstance(value, bool) or not isinstance(value, int) or value < 0
            ):
                raise ValueError(f"{name} must be a non-negative integer or None")

        if self.max_mid_circuit_measurements is not None:
            if (
                self.supports_mid_circuit_measurement is False
                and self.max_mid_circuit_measurements > 0
            ):
                raise ValueError("measurement limit contradicts unsupported measurement")
            if (
                self.supports_mid_circuit_measurement is True
                and self.max_mid_circuit_measurements == 0
            ):
                raise ValueError("zero measurement limit contradicts supported measurement")
        if self.max_conditional_depth is not None:
            if (
                self.supports_classical_conditionals is False
                and self.max_conditional_depth > 0
            ):
                raise ValueError("conditional-depth limit contradicts unsupported conditionals")
            if (
                self.supports_classical_conditionals is True
                and self.max_conditional_depth == 0
            ):
                raise ValueError("zero conditional-depth limit contradicts supported conditionals")

        latency = self.measurement_feedback_latency_seconds
        if latency is not None:
            if isinstance(latency, bool) or not isinstance(latency, (int, float)):
                raise ValueError("measurement_feedback_latency_seconds must be numeric or None")
            if not math.isfinite(latency) or latency < 0:
                raise ValueError(
                    "measurement_feedback_latency_seconds must be finite and non-negative"
                )

    @property
    def supports_adaptive_control(self) -> bool:
        """True for target-specific documented capability, not execution permission.

        This is only a lowering/capability gate. It does not establish successful
        hardware execution, accepted output quality, speedup, or economic advantage.
        """
        try:
            self.validate()
        except (AttributeError, TypeError, ValueError):
            return False
        return (
            self.evidence_class == "OFFICIAL_PROVIDER_DOCUMENTATION"
            and self.supports_mid_circuit_measurement is True
            and self.supports_reset is True
            and self.supports_classical_conditionals is True
        )
