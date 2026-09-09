from __future__ import annotations
from dataclasses import dataclass
from itertools import product
from time import perf_counter
from typing import Mapping


@dataclass(frozen=True)
class QuboInstance:
    linear: Mapping[int, float]
    quadratic: Mapping[tuple[int, int], float]
    constant: float = 0.0

    @property
    def variables(self) -> tuple[int, ...]:
        ids=set(self.linear)
        for i,j in self.quadratic:
            ids.add(i); ids.add(j)
        return tuple(sorted(ids))

    def energy(self, bits: Mapping[int, int]) -> float:
        e=self.constant+sum(w*bits.get(i,0) for i,w in self.linear.items())
        e+=sum(w*bits.get(i,0)*bits.get(j,0) for (i,j),w in self.quadratic.items())
        return float(e)


@dataclass(frozen=True)
class ClassicalBaselineResult:
    assignment: dict[int,int]
    objective: float
    runtime_seconds: float
    states_evaluated: int
    method: str = "exact_enumeration"


def exact_qubo_baseline(instance: QuboInstance, max_variables: int = 24) -> ClassicalBaselineResult:
    vars_=instance.variables
    if len(vars_)>max_variables:
        raise ValueError("exact baseline intentionally capped; use a competitive solver for larger instances")
    t0=perf_counter()
    best_bits=None; best=float("inf"); count=0
    for values in product((0,1),repeat=len(vars_)):
        bits=dict(zip(vars_,values))
        value=instance.energy(bits); count+=1
        if value<best:
            best=value; best_bits=bits
    return ClassicalBaselineResult(best_bits or {},best,perf_counter()-t0,count)


def demo_maxcut_triangle() -> QuboInstance:
    # Minimize negative cut value for a 3-node unit-weight triangle.
    return QuboInstance(
        linear={0:-2.0,1:-2.0,2:-2.0},
        quadratic={(0,1):2.0,(0,2):2.0,(1,2):2.0},
    )
