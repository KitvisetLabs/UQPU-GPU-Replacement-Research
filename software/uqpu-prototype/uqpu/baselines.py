from __future__ import annotations

from dataclasses import dataclass

from .hardware import GPUHardwareProfile


@dataclass(frozen=True)
class GPUBenchmarkMeasurement:
    workload: str
    seconds_per_task: float
    tasks_per_run: int = 1

    def validate(self) -> None:
        if self.seconds_per_task <= 0 or self.tasks_per_run <= 0:
            raise ValueError("benchmark timing and task count must be positive")


@dataclass(frozen=True)
class GPUBaselineCost:
    workload: str
    capex_per_task: float
    electricity_per_task: float
    cooling_per_task: float
    total_per_task: float


class GPUBaselineCostModel:
    def __init__(self, profile: GPUHardwareProfile, electricity_per_kwh: float = 0.12):
        profile.validate()
        if electricity_per_kwh < 0:
            raise ValueError("electricity_per_kwh must be non-negative")
        self.profile = profile
        self.electricity_per_kwh = electricity_per_kwh

    def estimate(self, measurement: GPUBenchmarkMeasurement) -> GPUBaselineCost:
        measurement.validate()
        seconds = measurement.seconds_per_task
        capex = seconds * self.profile.amortized_capex_per_second
        watts = self.profile.board_power_watts + self.profile.system_overhead_watts
        energy_kwh = watts * seconds / 3_600_000.0
        electricity = energy_kwh * self.electricity_per_kwh
        cooling = electricity * self.profile.cooling_multiplier
        total = capex + electricity + cooling

        return GPUBaselineCost(
            workload=measurement.workload,
            capex_per_task=capex,
            electricity_per_task=electricity,
            cooling_per_task=cooling,
            total_per_task=total,
        )
