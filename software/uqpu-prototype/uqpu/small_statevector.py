"""Bounded ideal CPU simulator for verifying the QAOA compiler gate subset.

Not a hardware noise model, scalable solver, or quantum-memory service.
The exponential allocation is capped before any state is allocated.
"""
from __future__ import annotations

import cmath
from collections import Counter
import math
import random

from .portable import PortableProgram

MAX_QUBITS = 12


def statevector(program: PortableProgram) -> tuple[complex, ...]:
    program.validate()
    if type(program.qubits) is not int or program.qubits > MAX_QUBITS:
        raise ValueError(f"verification simulator supports at most {MAX_QUBITS} qubits")
    # Validate the whole program first: measurement is terminal only.
    measured = False
    for inst in program.instructions:
        if measured:
            raise ValueError("instructions after measurement are unsupported")
        if any(type(q) is not int for q in inst.targets + inst.controls):
            raise ValueError("qubits must have integer indices")
        if inst.op == "measure_all":
            if inst.targets or inst.controls or inst.params:
                raise ValueError("measure_all has no operands")
            measured = True
        elif inst.op in {"h", "rx", "rz"}:
            arity = 0 if inst.op == "h" else 1
            if len(inst.targets) != 1 or inst.controls or len(inst.params) != arity:
                raise ValueError("invalid one-qubit gate operands")
        elif inst.op == "cx":
            if len(inst.targets) != 1 or len(inst.controls) != 1 or inst.params or inst.targets == inst.controls:
                raise ValueError("invalid CX operands")
        else:
            raise ValueError(f"unsupported verification gate: {inst.op}")
        if any(not math.isfinite(p) for p in inst.params):
            raise ValueError("rotation angles must be finite")
    state = [0j] * (1 << program.qubits)
    state[0] = 1 + 0j
    for inst in program.instructions:
        if inst.op == "measure_all":
            continue  # Return pre-measurement amplitudes; sampling is separate.
        target = 1 << inst.targets[0]
        if inst.op == "cx":
            control = 1 << inst.controls[0]
            for i in range(len(state)):
                if i & control and not i & target:
                    state[i], state[i | target] = state[i | target], state[i]
            continue
        if inst.op == "h":
            a = b = c = 1 / math.sqrt(2)
            d = -a
        elif inst.op == "rx":
            a = d = math.cos(inst.params[0] / 2)
            b = c = -1j * math.sin(inst.params[0] / 2)
        else:
            a = cmath.exp(-0.5j * inst.params[0])
            d = cmath.exp(0.5j * inst.params[0])
            b = c = 0j
        for i in range(len(state)):
            if not i & target:
                u, v = state[i], state[i | target]
                state[i], state[i | target] = a * u + b * v, c * u + d * v
    return tuple(state)


def probabilities(program: PortableProgram) -> tuple[float, ...]:
    return tuple(abs(a) ** 2 for a in statevector(program))


def sample_counts(program: PortableProgram, *, seed: int = 0) -> dict[int, int]:
    if type(program.shots) is not int or not 0 < program.shots <= 1_000_000:
        raise ValueError("verification sampling requires 1..1000000 integer shots")
    probs = probabilities(program)
    rng = random.Random(seed)
    counts = Counter()
    # Bounded batches avoid retaining one million Python sample objects.
    remaining = program.shots
    while remaining:
        size = min(remaining, 4096)
        counts.update(rng.choices(range(len(probs)), weights=probs, k=size))
        remaining -= size
    return dict(sorted(counts.items()))
