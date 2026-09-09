from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class FabRoute:
    name: str
    min_feature_nm: float
    capex_index: float
    process_steps: int
    expected_yield: float
    throughput_wafers_per_hour: float
    evidence_level: str = "MODEL_ONLY"

    def validate(self):
        if self.min_feature_nm <= 0: raise ValueError("feature size must be positive")
        if self.capex_index <= 0: raise ValueError("capex index must be positive")
        if self.process_steps <= 0: raise ValueError("process steps must be positive")
        if not 0 < self.expected_yield <= 1: raise ValueError("yield must be in (0,1]")
        if self.throughput_wafers_per_hour <= 0: raise ValueError("throughput must be positive")

@dataclass(frozen=True)
class DeviceRequirement:
    max_feature_nm: float
    max_process_steps: int
    min_yield: float

def feasible(route: FabRoute, req: DeviceRequirement) -> bool:
    route.validate()
    return (route.min_feature_nm <= req.max_feature_nm
            and route.process_steps <= req.max_process_steps
            and route.expected_yield >= req.min_yield)

def route_score(route: FabRoute) -> float:
    route.validate()
    return route.capex_index * route.process_steps / (route.expected_yield * route.throughput_wafers_per_hour)

def select_lowest_model_cost(routes, req):
    valid=[r for r in routes if feasible(r,req)]
    return min(valid,key=route_score) if valid else None
