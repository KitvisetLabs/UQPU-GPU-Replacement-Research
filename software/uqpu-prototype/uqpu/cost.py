from __future__ import annotations

from dataclasses import dataclass
from .resources import ResourceEstimate


@dataclass
class CostBreakdown:
    capex_amortized: float = 0.0
    energy: float = 0.0
    cooling: float = 0.0
    control: float = 0.0
    qec: float = 0.0
    memory_network: float = 0.0
    maintenance: float = 0.0
    software: float = 0.0

    @property
    def total(self) -> float:
        return sum((
            self.capex_amortized,
            self.energy,
            self.cooling,
            self.control,
            self.qec,
            self.memory_network,
            self.maintenance,
            self.software,
        ))


@dataclass
class CostModel:
    electricity_per_kwh: float = 0.12
    cooling_multiplier: float = 0.35
    capex_per_second: float = 0.005
    control_per_second: float = 0.002
    qec_per_second: float = 0.003
    memory_network_per_gb: float = 0.00002
    maintenance_fraction: float = 0.08
    software_per_second: float = 0.0005

    def estimate(self, resources: ResourceEstimate, io_bytes: int = 0) -> CostBreakdown:
        runtime = resources.total_seconds
        energy_kwh = resources.energy_joules / 3_600_000.0
        base_capex = runtime * self.capex_per_second
        energy_cost = energy_kwh * self.electricity_per_kwh
        cooling_cost = energy_cost * self.cooling_multiplier
        control_cost = runtime * self.control_per_second
        qec_cost = resources.qec_seconds * self.qec_per_second
        io_gb = io_bytes / (1024 ** 3)
        memory_cost = io_gb * self.memory_network_per_gb
        software_cost = runtime * self.software_per_second
        subtotal = base_capex + energy_cost + cooling_cost + control_cost + qec_cost + memory_cost + software_cost
        maintenance = subtotal * self.maintenance_fraction
        return CostBreakdown(
            capex_amortized=base_capex,
            energy=energy_cost,
            cooling=cooling_cost,
            control=control_cost,
            qec=qec_cost,
            memory_network=memory_cost,
            maintenance=maintenance,
            software=software_cost,
        )

    @staticmethod
    def advantage(gpu_cost_per_task: float, uqpu_cost_per_task: float) -> float:
        if gpu_cost_per_task < 0 or uqpu_cost_per_task <= 0:
            raise ValueError("costs must be positive (GPU may be zero only if not evaluated)")
        return gpu_cost_per_task / uqpu_cost_per_task
