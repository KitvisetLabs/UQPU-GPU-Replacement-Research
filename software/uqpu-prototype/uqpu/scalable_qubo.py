from __future__ import annotations
from dataclasses import dataclass
import random
from typing import Mapping

from .optimization_baseline import QuboInstance


@dataclass(frozen=True)
class WeightedEdge:
    u: int
    v: int
    weight: float = 1.0


def maxcut_qubo(node_count: int, edges: list[WeightedEdge]) -> QuboInstance:
    if node_count < 1:
        raise ValueError("node_count must be positive")
    linear={i:0.0 for i in range(node_count)}
    quadratic={}
    for e in edges:
        if e.u == e.v or not (0 <= e.u < node_count and 0 <= e.v < node_count):
            raise ValueError("invalid edge")
        u,v=sorted((e.u,e.v))
        w=float(e.weight)
        # Minimize negative cut: -w(xu+xv-2*xu*xv)
        linear[u]-=w; linear[v]-=w
        quadratic[(u,v)]=quadratic.get((u,v),0.0)+2.0*w
    return QuboInstance(linear,quadratic)


def seeded_erdos_renyi_maxcut(node_count: int, edge_probability: float, seed: int) -> QuboInstance:
    if not 0.0 <= edge_probability <= 1.0:
        raise ValueError("edge_probability must be in [0,1]")
    rng=random.Random(seed)
    edges=[]
    for u in range(node_count):
        for v in range(u+1,node_count):
            if rng.random() < edge_probability:
                edges.append(WeightedEdge(u,v,1.0))
    return maxcut_qubo(node_count,edges)


def greedy_bitflip(instance: QuboInstance, *, restarts: int = 8, seed: int = 0) -> tuple[dict[int,int],float]:
    if restarts < 1:
        raise ValueError("restarts must be positive")
    rng=random.Random(seed); vars_=instance.variables
    best_bits={i:0 for i in vars_}; best=instance.energy(best_bits)
    for _ in range(restarts):
        bits={i:rng.randrange(2) for i in vars_}
        value=instance.energy(bits)
        improved=True
        while improved:
            improved=False
            for i in vars_:
                bits[i]^=1
                candidate=instance.energy(bits)
                if candidate < value:
                    value=candidate; improved=True
                else:
                    bits[i]^=1
        if value < best:
            best_bits=dict(bits); best=value
    return best_bits,float(best)
