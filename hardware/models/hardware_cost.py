from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class HardwareLayerCost:
    fabrication_usd: float = 0.0
    photonics_usd: float = 0.0
    memory_usd: float = 0.0
    packaging_usd: float = 0.0
    control_usd: float = 0.0
    cryogenic_usd: float = 0.0
    interconnect_usd: float = 0.0
    test_calibration_usd: float = 0.0

    @property
    def total_capex(self) -> float:
        return sum((
            self.fabrication_usd,
            self.photonics_usd,
            self.memory_usd,
            self.packaging_usd,
            self.control_usd,
            self.cryogenic_usd,
            self.interconnect_usd,
            self.test_calibration_usd,
        ))


@dataclass(frozen=True)
class SystemEconomics:
    capex: HardwareLayerCost
    lifetime_seconds: float
    utilization: float
    operating_power_watts: float
    electricity_per_kwh: float = 0.12
    maintenance_fraction: float = 0.08

    def validate(self) -> None:
        if self.lifetime_seconds <= 0:
            raise ValueError("lifetime_seconds must be positive")
        if not (0 < self.utilization <= 1):
            raise ValueError("utilization must be in (0,1]")
        if self.operating_power_watts < 0:
            raise ValueError("operating_power_watts must be non-negative")

    def cost_per_task(self, task_seconds: float) -> float:
        self.validate()
        if task_seconds <= 0:
            raise ValueError("task_seconds must be positive")
        amortized = (
            self.capex.total_capex
            / (self.lifetime_seconds * self.utilization)
            * task_seconds
        )
        energy_kwh = self.operating_power_watts * task_seconds / 3_600_000.0
        energy = energy_kwh * self.electricity_per_kwh
        maintenance = amortized * self.maintenance_fraction
        return amortized + energy + maintenance
