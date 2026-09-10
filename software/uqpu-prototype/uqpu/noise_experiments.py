"""Bounded classical readout-noise experiments for verified small circuits.

This is a synthetic measurement-channel model, not a calibrated QPU noise model.
"""
from __future__ import annotations
import math, random
from collections import Counter


def independent_bitflip_distribution(probabilities, qubits: int, error_probability: float):
    if type(qubits) is not int or not 0 <= qubits <= 12:
        raise ValueError("qubits must be an integer in 0..12")
    if len(probabilities) != 1 << qubits:
        raise ValueError("probability vector size does not match qubits")
    e=float(error_probability)
    if not math.isfinite(e) or not 0 <= e <= 0.5:
        raise ValueError("error_probability must be finite and in [0, 0.5]")
    if any((not math.isfinite(float(p)) or p < 0) for p in probabilities):
        raise ValueError("invalid probability vector")
    if not math.isclose(sum(probabilities),1.0,rel_tol=1e-10,abs_tol=1e-10):
        raise ValueError("probabilities must sum to one")
    out=[0.0]*(1<<qubits)
    for source,p in enumerate(probabilities):
        if not p: continue
        for target in range(1<<qubits):
            flips=(source^target).bit_count()
            out[target]+=p*((1-e)**(qubits-flips))*(e**flips)
    return tuple(out)


def sample_distribution(probabilities, shots: int, *, seed: int=0):
    if type(shots) is not int or not 0 < shots <= 1_000_000:
        raise ValueError("shots must be an integer in 1..1000000")
    rng=random.Random(seed)
    counts=Counter()
    remaining=shots
    while remaining:
        size=min(remaining,4096)
        counts.update(rng.choices(range(len(probabilities)),weights=probabilities,k=size))
        remaining-=size
    return dict(sorted(counts.items()))
