from __future__ import annotations
from dataclasses import dataclass

@dataclass(frozen=True)
class ConventionalSystemCost:
    cpu: float=0.0; gpu: float=0.0; accelerator_memory: float=0.0
    host_memory: float=0.0; storage: float=0.0; interconnect_network: float=0.0
    power_cooling: float=0.0; operations: float=0.0
    def validate(self):
        if any(v < 0 for v in self.__dict__.values()): raise ValueError("system cost components must be non-negative")
    @property
    def total(self):
        self.validate(); return sum(self.__dict__.values())

@dataclass(frozen=True)
class UQCSSystemCost:
    quantum_compute: float=0.0; photonics: float=0.0; classical_control: float=0.0
    memory: float=0.0; storage: float=0.0; interconnect_network: float=0.0
    qec: float=0.0; power_cooling: float=0.0; operations: float=0.0
    def validate(self):
        if any(v < 0 for v in self.__dict__.values()): raise ValueError("system cost components must be non-negative")
    @property
    def total(self):
        self.validate(); return sum(self.__dict__.values())

@dataclass(frozen=True)
class SystemAdvantage:
    classical_cost_per_task: float; uqcs_cost_per_task: float; ratio: float
    reaches_100x: bool; reaches_100m_x: bool

def compare_system_cost(classical: ConventionalSystemCost, uqcs: UQCSSystemCost) -> SystemAdvantage:
    if classical.total <= 0: raise ValueError("classical total cost must be positive")
    if uqcs.total <= 0: raise ValueError("UQCS total cost must be positive")
    ratio=classical.total/uqcs.total
    return SystemAdvantage(classical.total,uqcs.total,ratio,ratio>=100,ratio>=100_000_000)
