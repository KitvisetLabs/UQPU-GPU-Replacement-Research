from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Iterable


class LithographyKind(str, Enum):
    DUV_DRY = "DUV_DRY"
    DUV_IMMERSION = "DUV_IMMERSION"
    EUV_LOW_NA = "EUV_LOW_NA"
    EUV_HIGH_NA = "EUV_HIGH_NA"
    NANOIMPRINT = "NANOIMPRINT"
    DIRECT_WRITE = "DIRECT_WRITE"


@dataclass(frozen=True)
class FabricationRoute:
    name: str
    kind: LithographyKind
    min_feature_nm: float
    max_overlay_nm: float
    wafers_per_hour: float
    relative_tool_cost: float
    relative_process_complexity: float
    base_yield: float
    mask_required: bool
    evidence_level: str = "MODEL_ONLY"
    notes: str = ""

    def validate(self) -> None:
        if self.min_feature_nm <= 0:
            raise ValueError("min_feature_nm must be positive")
        if self.max_overlay_nm < 0:
            raise ValueError("max_overlay_nm must be non-negative")
        if self.wafers_per_hour <= 0:
            raise ValueError("wafers_per_hour must be positive")
        if self.relative_tool_cost <= 0 or self.relative_process_complexity <= 0:
            raise ValueError("relative cost/complexity must be positive")
        if not (0 < self.base_yield <= 1):
            raise ValueError("base_yield must be in (0,1]")


@dataclass(frozen=True)
class DeviceProcessRequirement:
    max_feature_nm: float
    max_overlay_nm: float
    min_yield: float
    min_wafers_per_hour: float = 0.0
    require_maskless: bool = False

    def validate(self) -> None:
        if self.max_feature_nm <= 0:
            raise ValueError("max_feature_nm must be positive")
        if self.max_overlay_nm < 0:
            raise ValueError("max_overlay_nm must be non-negative")
        if not (0 < self.min_yield <= 1):
            raise ValueError("min_yield must be in (0,1]")
        if self.min_wafers_per_hour < 0:
            raise ValueError("min_wafers_per_hour must be non-negative")


@dataclass(frozen=True)
class RouteAssessment:
    route: FabricationRoute
    feasible: bool
    blockers: tuple[str, ...]
    score: float


def assess_route(route: FabricationRoute, req: DeviceProcessRequirement) -> RouteAssessment:
    route.validate()
    req.validate()
    blockers: list[str] = []

    if route.min_feature_nm > req.max_feature_nm:
        blockers.append("feature_size")
    if route.max_overlay_nm > req.max_overlay_nm:
        blockers.append("overlay")
    if route.base_yield < req.min_yield:
        blockers.append("yield")
    if route.wafers_per_hour < req.min_wafers_per_hour:
        blockers.append("throughput")
    if req.require_maskless and route.mask_required:
        blockers.append("mask_required")

    # Lower is better. Yield loss is strongly penalized because it propagates
    # through full-stack economics. This is MODEL_ONLY architecture scoring.
    score = (
        route.relative_tool_cost
        * route.relative_process_complexity
        / route.base_yield
    )
    return RouteAssessment(route, not blockers, tuple(blockers), score)


def choose_route(
    routes: Iterable[FabricationRoute],
    req: DeviceProcessRequirement,
) -> RouteAssessment:
    assessments = [assess_route(r, req) for r in routes]
    feasible = [a for a in assessments if a.feasible]
    if not feasible:
        raise RuntimeError("no fabrication route satisfies requirements")
    return min(feasible, key=lambda a: a.score)


def reference_routes() -> tuple[FabricationRoute, ...]:
    """Architecture-study seed routes.

    Values combine public capability anchors with normalized MODEL_ONLY
    economics. They are not purchase quotations or fab guarantees.
    """
    return (
        FabricationRoute(
            "DUV dry mature-node", LithographyKind.DUV_DRY,
            min_feature_nm=65.0, max_overlay_nm=6.0,
            wafers_per_hour=300.0, relative_tool_cost=1.0,
            relative_process_complexity=1.0, base_yield=0.97,
            mask_required=True,
            notes="Mature-node/default route for control, power, sensors and many photonic/support chips."
        ),
        FabricationRoute(
            "ArF immersion DUV", LithographyKind.DUV_IMMERSION,
            min_feature_nm=38.0, max_overlay_nm=2.5,
            wafers_per_hour=295.0, relative_tool_cost=3.0,
            relative_process_complexity=1.8, base_yield=0.94,
            mask_required=True,
            notes="Public ASML NXT:2000i/2050i capability anchors; multi-patterning may extend applications."
        ),
        FabricationRoute(
            "Low-NA EUV", LithographyKind.EUV_LOW_NA,
            min_feature_nm=13.0, max_overlay_nm=1.5,
            wafers_per_hour=220.0, relative_tool_cost=9.0,
            relative_process_complexity=2.3, base_yield=0.92,
            mask_required=True,
            notes="Capability anchor based on 0.33 NA EUV resolution class; economics normalized MODEL_ONLY."
        ),
        FabricationRoute(
            "High-NA EUV", LithographyKind.EUV_HIGH_NA,
            min_feature_nm=8.0, max_overlay_nm=1.0,
            wafers_per_hour=185.0, relative_tool_cost=15.0,
            relative_process_complexity=2.7, base_yield=0.90,
            mask_required=True,
            notes="Capability anchor based on 0.55 NA High-NA EUV resolution class."
        ),
        FabricationRoute(
            "Nanoimprint", LithographyKind.NANOIMPRINT,
            min_feature_nm=14.0, max_overlay_nm=3.0,
            wafers_per_hour=80.0, relative_tool_cost=2.5,
            relative_process_complexity=1.4, base_yield=0.85,
            mask_required=True,
            notes="Canon publicly states 14 nm minimum linewidth and potential CoO reduction; route remains application/yield dependent."
        ),
        FabricationRoute(
            "Direct-write research", LithographyKind.DIRECT_WRITE,
            min_feature_nm=10.0, max_overlay_nm=5.0,
            wafers_per_hour=1.0, relative_tool_cost=0.8,
            relative_process_complexity=1.2, base_yield=0.75,
            mask_required=False,
            notes="Research/prototyping placeholder, not HVM route."
        ),
    )
