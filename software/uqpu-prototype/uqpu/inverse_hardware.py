from __future__ import annotations

from dataclasses import dataclass
from math import log10
from typing import Iterable

from .inverse_system import SubsystemBudget


@dataclass(frozen=True)
class HardwareRequirementTarget:
    target_advantage: float
    max_total_cost_per_task: float
    max_compute_cost_per_task: float
    max_memory_cost_per_task: float
    max_storage_cost_per_task: float
    max_fabric_cost_per_task: float
    max_control_qec_cost_per_task: float
    max_power_operations_cost_per_task: float
    min_utilization: float
    max_operating_power_watts: float
    min_effective_bandwidth_gbps: float
    max_photonic_loss_db: float
    min_fabrication_yield: float


def derive_hardware_requirements(
    budgets: Iterable[SubsystemBudget],
    *,
    reference_task_seconds: float,
    reference_bandwidth_gbps: float,
    reference_power_watts: float,
    reference_loss_db: float,
    base_yield: float = 0.70,
) -> list[HardwareRequirementTarget]:
    if reference_task_seconds <= 0:
        raise ValueError("reference_task_seconds must be positive")
    if reference_bandwidth_gbps <= 0:
        raise ValueError("reference_bandwidth_gbps must be positive")
    if reference_power_watts <= 0:
        raise ValueError("reference_power_watts must be positive")
    if reference_loss_db < 0:
        raise ValueError("reference_loss_db must be non-negative")
    if not (0 < base_yield <= 1):
        raise ValueError("base_yield must be in (0,1]")

    out = []
    for b in budgets:
        scale = max(1.0, b.target_advantage / 100.0)
        decades = log10(scale)

        # MODEL_ONLY inverse-design heuristics. These are monotonic
        # architecture-search constraints, not hardware predictions.
        min_utilization = min(0.995, 0.70 + 0.04 * decades)
        max_power = reference_power_watts / (scale ** 0.35)
        min_bandwidth = reference_bandwidth_gbps * (scale ** 0.20)
        max_loss = reference_loss_db / (scale ** 0.15) if reference_loss_db > 0 else 0.0
        min_yield = min(0.999, base_yield + 0.025 * decades)

        out.append(HardwareRequirementTarget(
            target_advantage=b.target_advantage,
            max_total_cost_per_task=b.total_uqcs_budget,
            max_compute_cost_per_task=b.compute_budget,
            max_memory_cost_per_task=b.memory_budget,
            max_storage_cost_per_task=b.storage_budget,
            max_fabric_cost_per_task=b.fabric_budget,
            max_control_qec_cost_per_task=b.control_qec_budget,
            max_power_operations_cost_per_task=b.power_operations_budget,
            min_utilization=min_utilization,
            max_operating_power_watts=max_power,
            min_effective_bandwidth_gbps=min_bandwidth,
            max_photonic_loss_db=max_loss,
            min_fabrication_yield=min_yield,
        ))
    return out
