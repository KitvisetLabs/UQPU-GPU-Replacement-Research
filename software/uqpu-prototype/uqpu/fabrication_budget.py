from __future__ import annotations

from dataclasses import dataclass

from .fab_flow import FabFlowResult
from .inverse_system import SubsystemBudget


@dataclass(frozen=True)
class ManufacturingDeployment:
    devices_per_system: int
    lifetime_useful_tasks_per_device: float
    package_and_test_cost_per_device_usd: float = 0.0

    def validate(self) -> None:
        if self.devices_per_system <= 0:
            raise ValueError("devices_per_system must be positive")
        if self.lifetime_useful_tasks_per_device <= 0:
            raise ValueError("lifetime_useful_tasks_per_device must be positive")
        if self.package_and_test_cost_per_device_usd < 0:
            raise ValueError("package/test cost must be non-negative")


@dataclass(frozen=True)
class FabricationBudgetAssessment:
    target_advantage: float
    compute_budget_per_task_usd: float
    manufacturing_budget_fraction: float
    manufacturing_budget_per_task_usd: float
    max_manufacturing_cost_per_device_usd: float
    max_fab_cost_per_good_die_usd: float
    modeled_fab_cost_per_good_die_usd: float
    package_and_test_cost_per_device_usd: float
    modeled_manufacturing_cost_per_task_usd: float
    budget_headroom_per_task_usd: float
    passes_budget: bool
    evidence_level: str = "MODEL_ONLY"


def assess_fabrication_against_inverse_budget(
    budget: SubsystemBudget,
    fab: FabFlowResult,
    deployment: ManufacturingDeployment,
    *,
    manufacturing_fraction_of_compute_budget: float,
) -> FabricationBudgetAssessment:
    deployment.validate()
    if not (0 < manufacturing_fraction_of_compute_budget <= 1):
        raise ValueError("manufacturing fraction must be in (0,1]")
    if fab.cost_per_good_die_usd < 0:
        raise ValueError("fab cost per good die must be non-negative")

    allowed_per_task = (
        budget.compute_budget * manufacturing_fraction_of_compute_budget
    )
    max_cost_per_device = (
        allowed_per_task
        * deployment.lifetime_useful_tasks_per_device
        / deployment.devices_per_system
    )
    max_fab_cost = max(
        0.0,
        max_cost_per_device - deployment.package_and_test_cost_per_device_usd,
    )

    actual_device_cost = (
        fab.cost_per_good_die_usd
        + deployment.package_and_test_cost_per_device_usd
    )
    actual_per_task = (
        actual_device_cost
        * deployment.devices_per_system
        / deployment.lifetime_useful_tasks_per_device
    )
    headroom = allowed_per_task - actual_per_task

    return FabricationBudgetAssessment(
        target_advantage=budget.target_advantage,
        compute_budget_per_task_usd=budget.compute_budget,
        manufacturing_budget_fraction=manufacturing_fraction_of_compute_budget,
        manufacturing_budget_per_task_usd=allowed_per_task,
        max_manufacturing_cost_per_device_usd=max_cost_per_device,
        max_fab_cost_per_good_die_usd=max_fab_cost,
        modeled_fab_cost_per_good_die_usd=fab.cost_per_good_die_usd,
        package_and_test_cost_per_device_usd=deployment.package_and_test_cost_per_device_usd,
        modeled_manufacturing_cost_per_task_usd=actual_per_task,
        budget_headroom_per_task_usd=headroom,
        passes_budget=headroom >= 0,
    )
