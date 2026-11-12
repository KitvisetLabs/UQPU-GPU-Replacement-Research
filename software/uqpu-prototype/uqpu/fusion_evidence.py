"""Fail-closed evidence boundary between fusion plasma milestones and net electricity.

This module classifies the completeness/consistency of a reported evidence record.
It is not a fusion model, a plant-performance prediction, or a techno-economic
analysis. In particular, plasma temperature or fusion power alone never promotes
a record to net-electricity evidence.
"""
from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
import math


class FusionEvidenceLevel(str, Enum):
    NO_SYSTEM_DATA = "NO_SYSTEM_DATA"
    PLASMA_OR_FUSION_MILESTONE_ONLY = "PLASMA_OR_FUSION_MILESTONE_ONLY"
    ELECTRIC_ACCOUNTING_INCOMPLETE = "ELECTRIC_ACCOUNTING_INCOMPLETE"
    ELECTRIC_ACCOUNTING_INCONSISTENT = "ELECTRIC_ACCOUNTING_INCONSISTENT"
    NET_OUTPUT_NONPOSITIVE = "NET_OUTPUT_NONPOSITIVE"
    NET_ELECTRICITY_ACCOUNTING_CONSISTENT = "NET_ELECTRICITY_ACCOUNTING_CONSISTENT"


@dataclass(frozen=True)
class FusionEvidenceRecord:
    """Source-bound record; power values are watts, times seconds, temperatures keV."""

    source_uri: str
    electron_temperature_kev: float | None = None
    ion_temperature_kev: float | None = None
    density_per_m3: float | None = None
    confinement_time_s: float | None = None
    fusion_power_w: float | None = None
    gross_electric_power_w: float | None = None
    recirculating_electric_power_w: float | None = None
    other_parasitic_power_w: float | None = None
    grid_delivery_losses_w: float | None = None
    net_delivered_electric_power_w: float | None = None
    meter_boundary: str = ""
    averaging_duration_s: float | None = None
    repeated_pulses: int | None = None
    capacity_factor: float | None = None

    def validate(self) -> None:
        if not isinstance(self.source_uri, str) or not self.source_uri.strip():
            raise ValueError("source_uri is required")
        positive_fields = (
            "electron_temperature_kev",
            "ion_temperature_kev",
            "density_per_m3",
            "confinement_time_s",
            "averaging_duration_s",
        )
        nonnegative_fields = (
            "fusion_power_w",
            "gross_electric_power_w",
            "recirculating_electric_power_w",
            "other_parasitic_power_w",
            "grid_delivery_losses_w",
        )
        for name in positive_fields:
            value = getattr(self, name)
            if value is not None and (not math.isfinite(float(value)) or float(value) <= 0):
                raise ValueError(f"{name} must be finite and > 0 when supplied")
        for name in nonnegative_fields:
            value = getattr(self, name)
            if value is not None and (not math.isfinite(float(value)) or float(value) < 0):
                raise ValueError(f"{name} must be finite and >= 0 when supplied")
        net = self.net_delivered_electric_power_w
        if net is not None and not math.isfinite(float(net)):
            raise ValueError("net_delivered_electric_power_w must be finite when supplied")
        if self.repeated_pulses is not None and (
            isinstance(self.repeated_pulses, bool)
            or not isinstance(self.repeated_pulses, int)
            or self.repeated_pulses < 0
        ):
            raise ValueError("repeated_pulses must be an integer >= 0")
        if self.capacity_factor is not None and (
            not math.isfinite(float(self.capacity_factor))
            or not 0.0 <= float(self.capacity_factor) <= 1.0
        ):
            raise ValueError("capacity_factor must be finite and within [0, 1]")


def classify_fusion_evidence(
    record: FusionEvidenceRecord,
    *,
    relative_tolerance: float = 1e-3,
    absolute_tolerance_w: float = 1.0,
) -> FusionEvidenceLevel:
    """Classify evidence completeness, never scientific truth or plant viability.

    A consistent electricity record must state a meter boundary and averaging
    duration, and satisfy:
      net_delivered = gross_electric - recirculating - other_parasitic - grid_losses

    The final class does not establish repeatability, availability, capacity
    factor, fuel-cycle closure, safety, lifecycle cost, or commercial viability.
    """
    record.validate()
    if not math.isfinite(relative_tolerance) or relative_tolerance < 0:
        raise ValueError("relative_tolerance must be finite and >= 0")
    if not math.isfinite(absolute_tolerance_w) or absolute_tolerance_w < 0:
        raise ValueError("absolute_tolerance_w must be finite and >= 0")

    plasma_fields = (
        record.electron_temperature_kev,
        record.ion_temperature_kev,
        record.density_per_m3,
        record.confinement_time_s,
        record.fusion_power_w,
    )
    electric_fields = (
        record.gross_electric_power_w,
        record.recirculating_electric_power_w,
        record.other_parasitic_power_w,
        record.grid_delivery_losses_w,
        record.net_delivered_electric_power_w,
    )
    if not any(value is not None for value in plasma_fields + electric_fields):
        return FusionEvidenceLevel.NO_SYSTEM_DATA
    if not any(value is not None for value in electric_fields):
        return FusionEvidenceLevel.PLASMA_OR_FUSION_MILESTONE_ONLY
    if (
        any(value is None for value in electric_fields)
        or not record.meter_boundary.strip()
        or record.averaging_duration_s is None
    ):
        return FusionEvidenceLevel.ELECTRIC_ACCOUNTING_INCOMPLETE

    expected = (
        record.gross_electric_power_w
        - record.recirculating_electric_power_w
        - record.other_parasitic_power_w
        - record.grid_delivery_losses_w
    )
    measured = record.net_delivered_electric_power_w
    tolerance = max(
        absolute_tolerance_w,
        relative_tolerance * max(abs(expected), abs(measured), 1.0),
    )
    if abs(measured - expected) > tolerance:
        return FusionEvidenceLevel.ELECTRIC_ACCOUNTING_INCONSISTENT
    if measured <= 0:
        return FusionEvidenceLevel.NET_OUTPUT_NONPOSITIVE
    return FusionEvidenceLevel.NET_ELECTRICITY_ACCOUNTING_CONSISTENT
