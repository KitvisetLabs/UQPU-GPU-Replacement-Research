"""Executable evidence gate for the Data-Center-to-One-Phone North Star.

The owner-defined US$10T-US$100T figure is an ambition-scale proxy, not a
computational unit. This module therefore evaluates explicit service metrics
and an explicit phone-class device envelope instead of converting dollars to
compute capability.
"""
from __future__ import annotations
from dataclasses import dataclass
import math

DIRECTIONS = ("at_least", "at_most")


def _finite_nonnegative(value: float, field: str) -> float:
    value = float(value)
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{field} must be finite and non-negative")
    return value


@dataclass(frozen=True)
class ServiceMetric:
    name: str
    unit: str
    required: float
    measured: float
    direction: str
    evidence_level: str
    measured_end_to_end: bool = False

    def __post_init__(self):
        if not self.name.strip() or not self.unit.strip():
            raise ValueError("metric name and unit are required")
        if self.direction not in DIRECTIONS:
            raise ValueError("direction must be at_least or at_most")
        if not self.evidence_level.strip():
            raise ValueError("evidence_level is required")
        _finite_nonnegative(self.required, "required")
        _finite_nonnegative(self.measured, "measured")

    @property
    def passes(self) -> bool:
        if self.direction == "at_least":
            return self.measured >= self.required
        return self.measured <= self.required


@dataclass(frozen=True)
class DeviceEnvelope:
    max_price_thb: float
    max_mass_g: float
    max_volume_cm3: float
    max_sustained_power_w: float

    def __post_init__(self):
        for field in ("max_price_thb", "max_mass_g", "max_volume_cm3", "max_sustained_power_w"):
            if _finite_nonnegative(getattr(self, field), field) <= 0:
                raise ValueError(f"{field} must be positive")


@dataclass(frozen=True)
class DeviceMeasurement:
    price_thb: float
    mass_g: float
    volume_cm3: float
    sustained_power_w: float
    requires_external_compute: bool
    measured_end_to_end: bool

    def __post_init__(self):
        for field in ("price_thb", "mass_g", "volume_cm3", "sustained_power_w"):
            _finite_nonnegative(getattr(self, field), field)


@dataclass(frozen=True)
class NorthStarAssessment:
    metric_count: int
    metrics_passing: int
    coverage_fraction: float
    device_envelope_passes: bool
    external_compute_independent: bool
    evidence_complete: bool
    demonstrated: bool


def assess_north_star(
    metrics: tuple[ServiceMetric, ...],
    envelope: DeviceEnvelope,
    device: DeviceMeasurement,
) -> NorthStarAssessment:
    if not metrics:
        raise ValueError("at least one explicit service metric is required")
    passing = sum(metric.passes for metric in metrics)
    device_pass = (
        device.price_thb <= envelope.max_price_thb
        and device.mass_g <= envelope.max_mass_g
        and device.volume_cm3 <= envelope.max_volume_cm3
        and device.sustained_power_w <= envelope.max_sustained_power_w
    )
    external_independent = not device.requires_external_compute
    evidence_complete = device.measured_end_to_end and all(m.measured_end_to_end for m in metrics)
    demonstrated = passing == len(metrics) and device_pass and external_independent and evidence_complete
    return NorthStarAssessment(
        metric_count=len(metrics),
        metrics_passing=passing,
        coverage_fraction=passing / len(metrics),
        device_envelope_passes=device_pass,
        external_compute_independent=external_independent,
        evidence_complete=evidence_complete,
        demonstrated=demonstrated,
    )
