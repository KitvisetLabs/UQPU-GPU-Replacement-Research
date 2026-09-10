from __future__ import annotations
from dataclasses import dataclass
import math

SUBSYSTEMS=("gpu","cpu","ram","vram","storage")

@dataclass(frozen=True)
class ReplacementContract:
    subsystem: str
    conventional_units: int
    conventional_cost_per_unit_task: float
    uqpu_total_cost_per_accepted_task: float
    accepted_output_equivalent: bool
    measured_end_to_end: bool

    def __post_init__(self):
        if self.subsystem not in SUBSYSTEMS: raise ValueError("unsupported subsystem")
        if type(self.conventional_units) is not int or self.conventional_units < 1: raise ValueError("conventional_units must be positive integer")
        for x in (self.conventional_cost_per_unit_task,self.uqpu_total_cost_per_accepted_task):
            if not math.isfinite(x) or x <= 0: raise ValueError("costs must be finite and positive")

    @property
    def conventional_total_cost(self):
        return self.conventional_units*self.conventional_cost_per_unit_task

    @property
    def financial_advantage(self):
        return self.conventional_total_cost/self.uqpu_total_cost_per_accepted_task

    def moonshot_status(self, target_units=100_000_000, target_advantage=100_000_000.0):
        scale=self.conventional_units>=target_units
        econ=self.financial_advantage>=target_advantage
        demonstrated=scale and econ and self.accepted_output_equivalent and self.measured_end_to_end
        return {"scale_target_met":scale,"economic_target_met":econ,
          "equivalence_verified":self.accepted_output_equivalent,
          "end_to_end_measured":self.measured_end_to_end,
          "demonstrated":demonstrated}

def required_uqpu_cost(conventional_total_cost: float,target_advantage: float=100_000_000.0):
    if not math.isfinite(conventional_total_cost) or conventional_total_cost<=0: raise ValueError("conventional_total_cost must be finite and positive")
    if not math.isfinite(target_advantage) or target_advantage<=0: raise ValueError("target_advantage must be finite and positive")
    return conventional_total_cost/target_advantage
