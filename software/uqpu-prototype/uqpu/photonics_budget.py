from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class PhotonicsBudget:
    target_advantage: float
    fabric_budget_per_task: float
    max_total_loss_db: float
    min_detector_efficiency: float
    min_source_efficiency: float
    min_switch_success_probability: float


def derive_photonics_budget(
    target_advantage: float,
    fabric_budget_per_task: float,
    *,
    reference_loss_db: float = 3.0,
    base_detector_efficiency: float = 0.90,
    base_source_efficiency: float = 0.80,
    base_switch_success: float = 0.95,
) -> PhotonicsBudget:
    if target_advantage <= 0:
        raise ValueError("target_advantage must be positive")
    if fabric_budget_per_task < 0:
        raise ValueError("fabric_budget_per_task must be non-negative")
    scale = max(1.0, target_advantage / 100.0)
    loss = reference_loss_db / (scale ** 0.12)
    detector = min(0.9999, base_detector_efficiency + 0.02 * (scale ** 0.08 - 1.0))
    source = min(0.9999, base_source_efficiency + 0.025 * (scale ** 0.08 - 1.0))
    switch = min(0.99999, base_switch_success + 0.01 * (scale ** 0.08 - 1.0))
    return PhotonicsBudget(target_advantage, fabric_budget_per_task, loss, detector, source, switch)
