"""QUBO -> Ising -> portable QAOA, with explicit objective and bit conventions.

QUBO terms are summed exactly as QuboInstance.energy defines them, including
both orientations of a pair and diagonal terms (x*x == x). No rescaling of
the objective is performed. Compilation is not evidence of QPU execution.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import math
from typing import Sequence

from .optimization_baseline import QuboInstance
from .portable import PortableInstruction, PortableProgram


@dataclass(frozen=True)
class IsingObjective:
    variables: tuple[int, ...]
    offset: float
    z: tuple[float, ...]
    zz: tuple[tuple[int, int, float], ...]
    instance_sha256: str

    def assignment(self, basis_index: int) -> dict[int, int]:
        if type(basis_index) is not int or not 0 <= basis_index < (1 << len(self.variables)):
            raise ValueError("basis index outside the objective register")
        return {v: (basis_index >> q) & 1 for q, v in enumerate(self.variables)}

    def energy(self, basis_index: int) -> float:
        bits = self.assignment(basis_index)
        spins = [1 - 2 * bits[v] for v in self.variables]
        return self.offset + sum(h * s for h, s in zip(self.z, spins)) + sum(
            j * spins[a] * spins[b] for a, b, j in self.zz
        )


def qubo_to_ising(instance: QuboInstance) -> IsingObjective:
    """Use x=(1-Z)/2; preserve constants for decoding and quality checks."""
    variables = instance.variables
    if not variables or any(type(v) is not int or v < 0 for v in variables):
        raise ValueError("at least one non-negative integer variable ID is required")
    coefficients = [instance.constant, *instance.linear.values(), *instance.quadratic.values()]
    if any(not math.isfinite(float(w)) for w in coefficients):
        raise ValueError("QUBO coefficients must be finite")
    pos = {v: q for q, v in enumerate(variables)}
    linear = [float(instance.linear.get(v, 0.0)) for v in variables]
    pairs: dict[tuple[int, int], float] = {}
    for (u, v), weight in sorted(instance.quadratic.items()):
        a, b = sorted((pos[u], pos[v]))
        if a == b:
            linear[a] += float(weight)
        else:
            pairs[a, b] = pairs.get((a, b), 0.0) + float(weight)
    offset = float(instance.constant) + sum(linear) / 2
    z = [-w / 2 for w in linear]
    zz = []
    for (a, b), weight in sorted(pairs.items()):
        if weight == 0:
            continue
        j = weight / 4
        offset += j
        z[a] -= j
        z[b] -= j
        zz.append((a, b, j))
    if not all(math.isfinite(v) for v in [offset, *z, *(j for _, _, j in zz)]):
        raise ValueError("QUBO transformation overflow")
    canonical = {
        "variables": variables, "constant": float(instance.constant),
        "linear": linear, "pairs": [[a, b, w] for (a, b), w in sorted(pairs.items()) if w != 0],
    }
    digest = hashlib.sha256(json.dumps(canonical, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()).hexdigest()
    return IsingObjective(variables, offset, tuple(z), tuple(zz), digest)


def qaoa_program(instance: QuboInstance, gammas: Sequence[float], betas: Sequence[float],
                 *, shots: int = 1024, contract_id: str = "") -> PortableProgram:
    """Prepare product_k exp(-i beta_k sum X) exp(-i gamma_k H) |+>.

    The offset contributes only a global phase and is carried as metadata.
    CX-RZ(2*gamma*J)-CX realizes exp(-i*gamma*J*Zi*Zj).
    Variable IDs map to ascending qubits; qubit 0 is the integer LSB.
    """
    if not len(gammas) or len(gammas) != len(betas):
        raise ValueError("equal non-empty gamma and beta sequences are required")
    if any(not math.isfinite(float(t)) for t in [*gammas, *betas]):
        raise ValueError("QAOA angles must be finite")
    if type(shots) is not int or shots <= 0:
        raise ValueError("shots must be a positive integer")
    obj = qubo_to_ising(instance)
    n = len(obj.variables)
    instructions = [PortableInstruction("h", targets=(q,)) for q in range(n)]
    for gamma, beta in zip(gammas, betas):
        for q, h in enumerate(obj.z):
            if h:
                instructions.append(PortableInstruction("rz", targets=(q,), params=(2 * gamma * h,)))
        for a, b, j in obj.zz:
            instructions.extend((
                PortableInstruction("cx", targets=(b,), controls=(a,)),
                PortableInstruction("rz", targets=(b,), params=(2 * gamma * j,)),
                PortableInstruction("cx", targets=(b,), controls=(a,)),
            ))
        instructions.extend(PortableInstruction("rx", targets=(q,), params=(2 * beta,)) for q in range(n))
    if any(not math.isfinite(p) for instruction in instructions for p in instruction.params):
        raise ValueError("QAOA rotation overflow")
    instructions.append(PortableInstruction("measure_all"))
    program = PortableProgram("qubo-qaoa", n, tuple(instructions), shots, {
        "algorithm": "QAOA", "layers": len(gammas), "gammas": list(gammas), "betas": list(betas),
        "contract_id": contract_id, "instance_sha256": obj.instance_sha256,
        "variable_order": list(obj.variables), "bit_order": "qubit_0_is_integer_lsb",
        "objective_sense": "minimize", "objective_offset": obj.offset,
        "omitted_global_phase": True, "evidence_level": "PROTOTYPE",
    })
    program.validate()
    return program
