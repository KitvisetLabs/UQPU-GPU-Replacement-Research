from __future__ import annotations

from dataclasses import dataclass

from .cloud_economics import CloudPricingProfile, CloudWorkloadUsage, cloud_cost_per_useful_task


@dataclass(frozen=True)
class OwnedHardwareEconomics:
    capex_usd: float
    lifetime_seconds: float
    utilization: float
    operating_power_watts: float
    maintenance_fraction_of_capex: float = 0.08
    electricity_usd_per_kwh: float = 0.12

    def validate(self) -> None:
        if self.capex_usd < 0:
            raise ValueError("capex must be non-negative")
        if self.lifetime_seconds <= 0:
            raise ValueError("lifetime_seconds must be positive")
        if not (0 < self.utilization <= 1):
            raise ValueError("utilization must be in (0,1]")
        if self.operating_power_watts < 0:
            raise ValueError("power must be non-negative")
        if self.maintenance_fraction_of_capex < 0 or self.electricity_usd_per_kwh < 0:
            raise ValueError("maintenance/electricity must be non-negative")


@dataclass(frozen=True)
class OwnedWorkloadUsage:
    useful_tasks: int
    active_runtime_seconds: float

    def validate(self) -> None:
        if self.useful_tasks <= 0:
            raise ValueError("useful_tasks must be positive")
        if self.active_runtime_seconds < 0:
            raise ValueError("runtime must be non-negative")


def owned_cost_per_useful_task(hw: OwnedHardwareEconomics, usage: OwnedWorkloadUsage) -> float:
    hw.validate()
    usage.validate()

    effective_lifetime = hw.lifetime_seconds * hw.utilization
    amortized_capex = hw.capex_usd * usage.active_runtime_seconds / effective_lifetime
    maintenance = (
        hw.capex_usd * hw.maintenance_fraction_of_capex
        * usage.active_runtime_seconds / hw.lifetime_seconds
    )
    energy_kwh = hw.operating_power_watts * usage.active_runtime_seconds / 3_600_000.0
    energy = energy_kwh * hw.electricity_usd_per_kwh
    return (amortized_capex + maintenance + energy) / usage.useful_tasks


@dataclass(frozen=True)
class CloudVsOwnedResult:
    cloud_cost_per_task: float
    owned_cost_per_task: float
    cheaper_route: str
    savings_ratio: float


def compare_cloud_vs_owned(
    cloud_profile: CloudPricingProfile,
    cloud_usage: CloudWorkloadUsage,
    owned_hw: OwnedHardwareEconomics,
    owned_usage: OwnedWorkloadUsage,
) -> CloudVsOwnedResult:
    if cloud_profile.currency != "USD":
        raise ValueError(
            "cloud-vs-owned comparison requires explicit FX conversion to USD"
        )
    cloud = cloud_cost_per_useful_task(cloud_profile, cloud_usage)
    owned = owned_cost_per_useful_task(owned_hw, owned_usage)
    if cloud == owned:
        return CloudVsOwnedResult(cloud, owned, "TIE", 1.0)
    if cloud < owned:
        return CloudVsOwnedResult(cloud, owned, "CLOUD", owned/cloud if cloud > 0 else float("inf"))
    return CloudVsOwnedResult(cloud, owned, "OWNED", cloud/owned if owned > 0 else float("inf"))
