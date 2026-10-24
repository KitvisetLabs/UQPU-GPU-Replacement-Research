"""Evidence-gated Landauer-gap diagnostics for accepted useful tasks.

The ratio produced here is a bookkeeping diagnostic, not thermodynamic
efficiency and not a claim that wall-plug energy equals heat dissipated during
logical erasure. The erased-bit count must be independently justified; it is
never inferred from output width or Hilbert-space dimension.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Any

from .fundamental_limits import landauer_minimum_joule

_ALLOWED_EVIDENCE_LEVELS = {
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
_MEASURED_EVIDENCE_LEVELS = {
    "LAB_RESULT",
    "PUBLISHED_EXPERIMENT",
    "PROTOTYPE",
    "PRODUCTION_DATA",
}
_ALLOWED_ENERGY_SCOPES = {
    "FULL_SYSTEM_WALL_PLUG",
    "QPU_SUBSYSTEM",
    "HOST_SUBSYSTEM",
    "OTHER_SUBSYSTEM",
}


def _finite_nonnegative(name: str, value: float) -> float:
    if isinstance(value, bool):
        raise ValueError(f"{name} must be numeric, not boolean")
    number = float(value)
    if not math.isfinite(number) or number < 0.0:
        raise ValueError(f"{name} must be finite and >= 0")
    return number


def _finite_positive(name: str, value: float) -> float:
    number = _finite_nonnegative(name, value)
    if number <= 0.0:
        raise ValueError(f"{name} must be > 0")
    return number


@dataclass(frozen=True)
class ThermodynamicGapObservation:
    """Inputs for a workload-level FND-001 diagnostic.

    total_wall_plug_joules must cover attempt_count attempts, including
    failed/retried work inside the declared energy boundary. Dividing by
    accepted_count therefore charges failed work to accepted outputs.
    irreversible_erased_bits_per_accepted_task is optional because output
    bits, state-space size and qubit count do not establish an erasure count.
    """

    workload_contract_id: str
    attempt_count: int
    accepted_count: int
    total_wall_plug_joules: float
    energy_scope: str
    temperature_kelvin: float
    temperature_basis: str
    evidence_level: str
    energy_provenance: str = ""
    accepted_output_provenance: str = ""
    measurement_window: str = ""
    irreversible_erased_bits_per_accepted_task: float | None = None
    erasure_accounting_basis: str = ""
    erasure_provenance: str = ""

    def validate(self) -> None:
        if not self.workload_contract_id.strip():
            raise ValueError("workload_contract_id is required")
        if isinstance(self.attempt_count, bool) or not isinstance(self.attempt_count, int):
            raise ValueError("attempt_count must be an integer")
        if isinstance(self.accepted_count, bool) or not isinstance(self.accepted_count, int):
            raise ValueError("accepted_count must be an integer")
        if self.attempt_count < 1:
            raise ValueError("attempt_count must be >= 1")
        if self.accepted_count < 0 or self.accepted_count > self.attempt_count:
            raise ValueError("accepted_count must be between 0 and attempt_count")
        _finite_nonnegative("total_wall_plug_joules", self.total_wall_plug_joules)
        _finite_positive("temperature_kelvin", self.temperature_kelvin)
        if self.energy_scope not in _ALLOWED_ENERGY_SCOPES:
            raise ValueError("energy_scope is not a governed scope")
        if not self.temperature_basis.strip():
            raise ValueError("temperature_basis is required")
        if self.evidence_level not in _ALLOWED_EVIDENCE_LEVELS:
            raise ValueError("evidence_level is not in the governed project taxonomy")

        if self.evidence_level in _MEASURED_EVIDENCE_LEVELS:
            for field_name in (
                "energy_provenance",
                "accepted_output_provenance",
                "measurement_window",
            ):
                if not getattr(self, field_name).strip():
                    raise ValueError(
                        f"{field_name} is required for measured evidence levels"
                    )

        erased_bits = self.irreversible_erased_bits_per_accepted_task
        if erased_bits is not None:
            _finite_nonnegative("irreversible_erased_bits_per_accepted_task", erased_bits)
            if not self.erasure_accounting_basis.strip():
                raise ValueError("erasure_accounting_basis is required when erased bits are supplied")
            if not self.erasure_provenance.strip():
                raise ValueError("erasure_provenance is required when erased bits are supplied")


def evaluate_thermodynamic_gap(
    observation: ThermodynamicGapObservation,
) -> dict[str, Any]:
    """Return a fail-closed FND-001 report without promoting evidence.

    wall-plug energy per accepted task divided by the ideal Landauer heat floor
    is a diagnostic only. The quantities have different physical meanings. A
    ratio below one requests a boundary/accounting audit and is not declared a
    violation of thermodynamics.
    """
    observation.validate()

    accepted = observation.accepted_count
    erased_bits = observation.irreversible_erased_bits_per_accepted_task
    report: dict[str, Any] = {
        "schema": "uqpu-fnd001-thermodynamic-gap-v1",
        "workload_contract_id": observation.workload_contract_id,
        "attempt_count": observation.attempt_count,
        "accepted_count": accepted,
        "total_wall_plug_joules": float(observation.total_wall_plug_joules),
        "energy_scope": observation.energy_scope,
        "temperature_kelvin": float(observation.temperature_kelvin),
        "temperature_basis": observation.temperature_basis,
        "evidence_level": observation.evidence_level,
        "energy_provenance": observation.energy_provenance or None,
        "accepted_output_provenance": observation.accepted_output_provenance or None,
        "measurement_window": observation.measurement_window or None,
        "irreversible_erased_bits_per_accepted_task": (
            float(erased_bits) if erased_bits is not None else None
        ),
        "erasure_accounting_basis": observation.erasure_accounting_basis or None,
        "erasure_provenance": observation.erasure_provenance or None,
        "wall_plug_joules_per_accepted_task": None,
        "landauer_floor_joules_per_accepted_task": None,
        "wall_plug_to_landauer_floor_ratio": None,
        "status": None,
        "eligible_for_fnd001_gap_analysis": False,
        "project_advantage_claim_allowed": False,
        "interpretation": (
            "Diagnostic only: wall-plug energy is not identical to Landauer heat; "
            "the ratio does not establish thermodynamic efficiency or advantage."
        ),
        "nonclaims": [
            "erased bits are not inferred from output bits, qubit count, or Hilbert-space dimension",
            "the ideal Landauer floor is not an engineering energy target",
            "a computed ratio does not prove a new physical law or mission-level advantage",
        ],
    }

    if accepted == 0:
        report["status"] = "NO_ACCEPTED_OUTPUTS"
        return report

    energy_per_accepted = float(observation.total_wall_plug_joules) / accepted
    report["wall_plug_joules_per_accepted_task"] = energy_per_accepted

    if erased_bits is None:
        report["status"] = "BLOCKED_ERASURE_ACCOUNTING"
        return report

    floor = landauer_minimum_joule(float(erased_bits), float(observation.temperature_kelvin))
    report["landauer_floor_joules_per_accepted_task"] = floor
    if floor == 0.0:
        report["status"] = "ZERO_ERASURE_FLOOR_RATIO_UNDEFINED"
        return report

    ratio = energy_per_accepted / floor
    report["wall_plug_to_landauer_floor_ratio"] = ratio
    if ratio < 1.0:
        report["status"] = "BOUNDARY_AUDIT_REQUIRED"
    else:
        report["status"] = "DIAGNOSTIC_ONLY"

    report["eligible_for_fnd001_gap_analysis"] = (
        observation.energy_scope == "FULL_SYSTEM_WALL_PLUG"
        and observation.evidence_level in _MEASURED_EVIDENCE_LEVELS
        and bool(observation.energy_provenance.strip())
        and bool(observation.accepted_output_provenance.strip())
        and bool(observation.measurement_window.strip())
        and bool(observation.erasure_accounting_basis.strip())
        and bool(observation.erasure_provenance.strip())
    )
    return report
