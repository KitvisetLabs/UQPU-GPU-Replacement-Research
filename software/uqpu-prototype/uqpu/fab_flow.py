from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from math import exp
from typing import Iterable


class ProcessKind(str, Enum):
    DEPOSITION = "DEPOSITION"
    LITHOGRAPHY = "LITHOGRAPHY"
    ETCH = "ETCH"
    IMPLANT_DOPING = "IMPLANT_DOPING"
    THERMAL = "THERMAL"
    CMP = "CMP"
    CLEAN = "CLEAN"
    METROLOGY = "METROLOGY"
    INSPECTION = "INSPECTION"
    BONDING_PACKAGING = "BONDING_PACKAGING"
    TEST = "TEST"


@dataclass(frozen=True)
class ProcessStep:
    name: str
    kind: ProcessKind
    cost_per_wafer_usd: float
    step_yield: float
    cycle_time_seconds: float
    energy_kwh_per_wafer: float = 0.0
    evidence_level: str = "MODEL_ONLY"
    notes: str = ""

    def validate(self) -> None:
        if self.cost_per_wafer_usd < 0:
            raise ValueError("cost_per_wafer_usd must be non-negative")
        if not (0 < self.step_yield <= 1):
            raise ValueError("step_yield must be in (0,1]")
        if self.cycle_time_seconds < 0:
            raise ValueError("cycle_time_seconds must be non-negative")
        if self.energy_kwh_per_wafer < 0:
            raise ValueError("energy_kwh_per_wafer must be non-negative")


@dataclass(frozen=True)
class DieGeometry:
    wafer_diameter_mm: float
    die_area_mm2: float
    edge_exclusion_mm: float = 3.0

    def gross_dies(self) -> float:
        if self.wafer_diameter_mm <= 0 or self.die_area_mm2 <= 0:
            raise ValueError("wafer diameter and die area must be positive")
        effective_d = self.wafer_diameter_mm - 2 * self.edge_exclusion_mm
        if effective_d <= 0:
            raise ValueError("edge exclusion leaves no usable wafer")
        wafer_area = 3.141592653589793 * (effective_d / 2.0) ** 2
        return wafer_area / self.die_area_mm2


@dataclass(frozen=True)
class FabFlowResult:
    total_process_cost_per_wafer_usd: float
    cumulative_process_yield: float
    total_cycle_time_seconds: float
    total_energy_kwh_per_wafer: float
    gross_dies_per_wafer: float
    expected_good_dies_per_wafer: float
    cost_per_good_die_usd: float


def cumulative_yield(steps: Iterable[ProcessStep]) -> float:
    y = 1.0
    for step in steps:
        step.validate()
        y *= step.step_yield
    return y


def estimate_fab_flow(
    steps: Iterable[ProcessStep],
    geometry: DieGeometry,
    *,
    defect_density_per_cm2: float = 0.0,
) -> FabFlowResult:
    steps = tuple(steps)
    if not steps:
        raise ValueError("at least one process step is required")
    if defect_density_per_cm2 < 0:
        raise ValueError("defect_density_per_cm2 must be non-negative")

    total_cost = sum(s.cost_per_wafer_usd for s in steps)
    total_time = sum(s.cycle_time_seconds for s in steps)
    total_energy = sum(s.energy_kwh_per_wafer for s in steps)
    process_yield = cumulative_yield(steps)

    gross = geometry.gross_dies()
    die_area_cm2 = geometry.die_area_mm2 / 100.0
    random_defect_yield = exp(-defect_density_per_cm2 * die_area_cm2)
    good = gross * process_yield * random_defect_yield

    if good <= 0:
        raise RuntimeError("expected good dies per wafer is zero")
    return FabFlowResult(
        total_process_cost_per_wafer_usd=total_cost,
        cumulative_process_yield=process_yield * random_defect_yield,
        total_cycle_time_seconds=total_time,
        total_energy_kwh_per_wafer=total_energy,
        gross_dies_per_wafer=gross,
        expected_good_dies_per_wafer=good,
        cost_per_good_die_usd=total_cost / good,
    )


def reference_generic_flow() -> tuple[ProcessStep, ...]:
    """MODEL_ONLY generic process-flow skeleton for architecture studies."""
    return (
        ProcessStep("blanket dielectric deposition", ProcessKind.DEPOSITION, 80, 0.9995, 45, 0.4),
        ProcessStep("lithography", ProcessKind.LITHOGRAPHY, 150, 0.9990, 30, 0.6),
        ProcessStep("anisotropic etch", ProcessKind.ETCH, 70, 0.9992, 35, 0.5),
        ProcessStep("implant/doping", ProcessKind.IMPLANT_DOPING, 55, 0.9997, 25, 0.4),
        ProcessStep("thermal activation", ProcessKind.THERMAL, 35, 0.9998, 40, 0.8),
        ProcessStep("CMP", ProcessKind.CMP, 45, 0.9996, 60, 0.3),
        ProcessStep("post-CMP clean", ProcessKind.CLEAN, 20, 0.9998, 20, 0.2),
        ProcessStep("inline metrology", ProcessKind.METROLOGY, 25, 0.9999, 15, 0.1),
        ProcessStep("defect inspection", ProcessKind.INSPECTION, 30, 0.9999, 25, 0.1),
        ProcessStep("wafer test/package allocation", ProcessKind.TEST, 60, 0.9990, 50, 0.2),
    )
