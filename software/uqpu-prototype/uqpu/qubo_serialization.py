from __future__ import annotations

from dataclasses import dataclass
from .optimization_baseline import QuboInstance


@dataclass(frozen=True)
class QuboPayload:
    format: str
    payload: dict
    notes: str = ""


def to_dwave_qubo(instance: QuboInstance) -> QuboPayload:
    q={}
    for i,w in instance.linear.items():
        q[(i,i)]=float(w)
    for (i,j),w in instance.quadratic.items():
        key=(min(i,j),max(i,j))
        q[key]=q.get(key,0.0)+float(w)
    return QuboPayload(
        format="dwave-qubo",
        payload={"Q":q,"offset":float(instance.constant)},
        notes="Compatible with UQPU DWaveLeapAdapter QUBO payload convention; offset is metadata unless downstream sampler supports it.",
    )


def to_portable_qubo(instance: QuboInstance) -> QuboPayload:
    return QuboPayload(
        format="uqpu-qubo-v1",
        payload={
            "linear":{str(i):float(w) for i,w in instance.linear.items()},
            "quadratic":[[int(i),int(j),float(w)] for (i,j),w in sorted(instance.quadratic.items())],
            "constant":float(instance.constant),
        },
        notes="Provider-neutral QUBO representation for routing/lowering.",
    )
