from __future__ import annotations
from dataclasses import dataclass
from .targets import target_ladder

@dataclass(frozen=True)
class SubsystemBudget:
    target_advantage: float; total_uqcs_budget: float; compute_budget: float
    memory_budget: float; storage_budget: float; fabric_budget: float
    control_qec_budget: float; power_operations_budget: float

def allocate_inverse_budget(classical_cost_per_task: float, shares=(0.35,0.20,0.05,0.10,0.20,0.10)):
    if len(shares)!=6 or any(x<0 for x in shares): raise ValueError("six non-negative subsystem shares are required")
    if abs(sum(shares)-1.0)>1e-9: raise ValueError("subsystem shares must sum to 1")
    out=[]
    for target in target_ladder(classical_cost_per_task):
        b=target.maximum_uqpu_cost_per_task
        out.append(SubsystemBudget(target.target_advantage,b,b*shares[0],b*shares[1],b*shares[2],b*shares[3],b*shares[4],b*shares[5]))
    return out
