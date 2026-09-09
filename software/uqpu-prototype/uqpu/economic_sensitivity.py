from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterable

from .cloud_economics import CloudPricingProfile, CloudWorkloadUsage, cloud_cost_per_useful_task
from .cloud_vs_owned import OwnedHardwareEconomics, OwnedWorkloadUsage, owned_cost_per_useful_task


@dataclass(frozen=True)
class FxConversion:
    from_currency: str
    to_currency: str
    rate: float
    as_of_date: str
    source: str
    evidence_level: str = "OFFICIAL_OR_MARKET_SNAPSHOT"

    def validate(self) -> None:
        if self.rate <= 0:
            raise ValueError("FX rate must be positive")
        if not self.from_currency or not self.to_currency:
            raise ValueError("currencies are required")
        if not self.as_of_date or not self.source:
            raise ValueError("dated FX provenance is required")


def convert_cloud_profile(profile: CloudPricingProfile, fx: FxConversion) -> CloudPricingProfile:
    fx.validate()
    if profile.currency != fx.from_currency:
        raise ValueError("FX source currency does not match profile currency")
    multiplier = fx.rate
    return replace(
        profile,
        currency=fx.to_currency,
        per_second=profile.per_second * multiplier,
        per_task=profile.per_task * multiplier,
        per_shot=profile.per_shot * multiplier,
        per_one_qubit_gate_shot=profile.per_one_qubit_gate_shot * multiplier,
        per_two_qubit_gate_shot=profile.per_two_qubit_gate_shot * multiplier,
        minimum_program_price=profile.minimum_program_price * multiplier,
        per_qpu_hour=profile.per_qpu_hour * multiplier,
        per_time_increment=profile.per_time_increment * multiplier,
        evidence_level=f"{profile.evidence_level}+FX",
    )


@dataclass(frozen=True)
class CrossoverPoint:
    parameter: str
    value: float
    cloud_cost_per_task: float
    owned_cost_per_task: float
    preferred_route: str
    ratio: float


def _classify(cloud: float, owned: float) -> tuple[str, float]:
    if cloud == owned:
        return "TIE", 1.0
    if cloud < owned:
        return "CLOUD", owned / cloud if cloud > 0 else float("inf")
    return "OWNED", cloud / owned if owned > 0 else float("inf")


def sweep_owned_utilization(
    cloud_profile: CloudPricingProfile,
    cloud_usage: CloudWorkloadUsage,
    owned_hw: OwnedHardwareEconomics,
    owned_usage: OwnedWorkloadUsage,
    utilizations: Iterable[float],
) -> list[CrossoverPoint]:
    if cloud_profile.currency != "USD":
        raise ValueError("convert cloud pricing to USD before comparison")
    cloud = cloud_cost_per_useful_task(cloud_profile, cloud_usage)
    out = []
    for value in utilizations:
        hw = replace(owned_hw, utilization=float(value))
        owned = owned_cost_per_useful_task(hw, owned_usage)
        route, ratio = _classify(cloud, owned)
        out.append(CrossoverPoint("owned_utilization", float(value), cloud, owned, route, ratio))
    return out


def sweep_owned_capex(
    cloud_profile: CloudPricingProfile,
    cloud_usage: CloudWorkloadUsage,
    owned_hw: OwnedHardwareEconomics,
    owned_usage: OwnedWorkloadUsage,
    capex_values: Iterable[float],
) -> list[CrossoverPoint]:
    if cloud_profile.currency != "USD":
        raise ValueError("convert cloud pricing to USD before comparison")
    cloud = cloud_cost_per_useful_task(cloud_profile, cloud_usage)
    out = []
    for value in capex_values:
        if value < 0:
            raise ValueError("CAPEX values must be non-negative")
        hw = replace(owned_hw, capex_usd=float(value))
        owned = owned_cost_per_useful_task(hw, owned_usage)
        route, ratio = _classify(cloud, owned)
        out.append(CrossoverPoint("owned_capex_usd", float(value), cloud, owned, route, ratio))
    return out


def find_route_transition(points: Iterable[CrossoverPoint]) -> tuple[CrossoverPoint, CrossoverPoint] | None:
    points = tuple(points)
    for left, right in zip(points, points[1:]):
        if left.preferred_route != right.preferred_route:
            return left, right
    return None


@dataclass(frozen=True)
class CostEnvelope:
    low: float
    central: float
    high: float

    def validate(self) -> None:
        if self.low < 0 or self.central < 0 or self.high < 0:
            raise ValueError("costs must be non-negative")
        if not (self.low <= self.central <= self.high):
            raise ValueError("cost envelope must satisfy low <= central <= high")


@dataclass(frozen=True)
class RobustRouteAssessment:
    cloud: CostEnvelope
    owned: CostEnvelope
    classification: str


def robust_route_assessment(cloud: CostEnvelope, owned: CostEnvelope) -> RobustRouteAssessment:
    cloud.validate()
    owned.validate()
    if cloud.high < owned.low:
        status = "ROBUST_CLOUD"
    elif owned.high < cloud.low:
        status = "ROBUST_OWNED"
    else:
        status = "UNCERTAIN_OVERLAP"
    return RobustRouteAssessment(cloud, owned, status)
