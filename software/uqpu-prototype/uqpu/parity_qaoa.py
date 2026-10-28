"""Higher-order parity-QAOA prototype with exact small-instance certificates.

This is a provider-neutral circuit generator and classical reference model.
It does not submit QPU jobs or establish an advantage. Cycle-parity penalties
are represented as higher-order Z strings and compiled to CNOT/RZ phase gadgets.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import itertools
import json
import math
from typing import Sequence

from .parity_encoding import ParityEncoding
from .portable import PortableInstruction, PortableProgram


@dataclass(frozen=True)
class ParityQAOACertificate:
    objective_sha256: str
    physical_qubits: int
    states_evaluated: int
    optimum_energy: float
    optimal_assignments: tuple[tuple[int, ...], ...]
    feasible_optimum_energy: float
    feasible_optimal_assignments: tuple[tuple[int, ...], ...]
    all_ground_states_feasible: bool


@dataclass(frozen=True)
class ParityQAOAObjective:
    encoding: ParityEncoding
    edge_costs: tuple[float, ...]
    penalty_weight: float
    instance_sha256: str

    @property
    def physical_qubits(self) -> int:
        return self.encoding.physical_qubit_count

    @property
    def offset(self) -> float:
        # c*z = c/2 - (c/2)Z and lambda*(1-product(Z))/2.
        return sum(self.edge_costs) / 2 + (
            self.penalty_weight * len(self.encoding.cycle_constraints) / 2
        )

    @property
    def linear_z(self) -> tuple[float, ...]:
        return tuple(-cost / 2 for cost in self.edge_costs)

    @property
    def cycle_z_terms(self) -> tuple[tuple[tuple[int, ...], float], ...]:
        coefficient = -self.penalty_weight / 2
        return tuple((cycle, coefficient) for cycle in self.encoding.cycle_constraints)

    @staticmethod
    def _bits(values: Sequence[int] | str, expected: int) -> tuple[int, ...]:
        if isinstance(values, str):
            if any(ch not in "01" for ch in values):
                raise ValueError("physical_bits must contain only 0 and 1")
            bits = tuple(int(ch) for ch in values)
        else:
            try:
                bits = tuple(values)
            except TypeError as exc:
                raise ValueError("physical_bits must be a bit sequence") from exc
        if len(bits) != expected:
            raise ValueError("physical_bits length must equal physical_qubits")
        if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
            raise ValueError("physical_bits entries must be integer bits 0 or 1")
        return bits

    def violated_cycle_count(self, physical_bits: Sequence[int] | str) -> int:
        bits = self._bits(physical_bits, self.physical_qubits)
        return sum(sum(bits[index] for index in cycle) % 2 for cycle in self.encoding.cycle_constraints)

    def is_feasible(self, physical_bits: Sequence[int] | str) -> bool:
        return self.violated_cycle_count(physical_bits) == 0

    def energy(self, physical_bits: Sequence[int] | str) -> float:
        bits = self._bits(physical_bits, self.physical_qubits)
        return sum(cost * bit for cost, bit in zip(self.edge_costs, bits)) + (
            self.penalty_weight * self.violated_cycle_count(bits)
        )

    def decode(self, physical_bits: Sequence[int] | str) -> tuple[int, ...]:
        return self.encoding.decode_physical(physical_bits)

    def exact_certificate(self, *, max_qubits: int = 24) -> ParityQAOACertificate:
        """Enumerate a bounded physical register and certify its ground states."""
        if type(max_qubits) is not int or max_qubits < 1:
            raise ValueError("max_qubits must be a positive integer")
        n = self.physical_qubits
        if n > max_qubits:
            raise ValueError("exact parity certificate exceeds max_qubits")
        assignments = tuple(itertools.product((0, 1), repeat=n))
        scored = tuple((bits, self.energy(bits)) for bits in assignments)
        optimum = min(value for _, value in scored)
        ground = tuple(bits for bits, value in scored if math.isclose(
            value, optimum, rel_tol=1e-12, abs_tol=1e-12
        ))
        feasible_scored = tuple((bits, value) for bits, value in scored if self.is_feasible(bits))
        feasible_optimum = min(value for _, value in feasible_scored)
        feasible_ground = tuple(bits for bits, value in feasible_scored if math.isclose(
            value, feasible_optimum, rel_tol=1e-12, abs_tol=1e-12
        ))
        return ParityQAOACertificate(
            objective_sha256=self.instance_sha256,
            physical_qubits=n,
            states_evaluated=len(assignments),
            optimum_energy=optimum,
            optimal_assignments=ground,
            feasible_optimum_energy=feasible_optimum,
            feasible_optimal_assignments=feasible_ground,
            all_ground_states_feasible=all(self.is_feasible(bits) for bits in ground),
        )


def parity_qaoa_objective(
    encoding: ParityEncoding,
    edge_costs: Sequence[float],
    *,
    penalty_weight: float,
) -> ParityQAOAObjective:
    """Create a fail-closed minimization objective over edge-parity bits.

    Each violated even-cycle constraint costs penalty_weight. If cycles exist,
    require penalty_weight > 2*sum(abs(edge_costs)); this ensures no infeasible
    bitstring can beat every feasible bitstring under the declared objective.
    """
    if not isinstance(encoding, ParityEncoding):
        raise ValueError("encoding must be a ParityEncoding")
    try:
        costs = tuple(float(value) for value in edge_costs)
    except (TypeError, ValueError) as exc:
        raise ValueError("edge_costs must be finite numeric values") from exc
    if len(costs) != encoding.physical_qubit_count:
        raise ValueError("edge_costs length must equal the number of graph edges")
    if any(not math.isfinite(value) for value in costs):
        raise ValueError("edge_costs must be finite")
    penalty = float(penalty_weight)
    if not math.isfinite(penalty) or penalty < 0:
        raise ValueError("penalty_weight must be finite and >= 0")
    if encoding.cycle_constraints and penalty <= 2 * sum(abs(value) for value in costs):
        raise ValueError("penalty_weight must exceed twice the sum of absolute edge costs")
    canonical = {
        "vertex_count": encoding.vertex_count,
        "edges": encoding.edges,
        "cycle_constraints": encoding.cycle_constraints,
        "edge_costs": costs,
        "penalty_weight": penalty,
        "objective": "minimize sum(edge_cost*edge_bit) + penalty per odd cycle",
    }
    digest = hashlib.sha256(json.dumps(
        canonical, sort_keys=True, separators=(",", ":"), allow_nan=False
    ).encode("utf-8")).hexdigest()
    return ParityQAOAObjective(encoding, costs, penalty, digest)


def parity_qaoa_program(
    objective: ParityQAOAObjective,
    gammas: Sequence[float],
    betas: Sequence[float],
    *,
    shots: int = 1024,
    contract_id: str = "",
) -> PortableProgram:
    """Compile higher-order cycle penalties to provider-neutral CNOT/RZ gadgets.

    The cost Hamiltonian is H = offset + sum(h_e Z_e) +
    sum_cycle(-penalty_weight/2) product_e(Z_e). The offset is global phase
    only and is recorded in metadata. The mixer is the standard product RX
    mixer; cycle feasibility is encouraged by the penalty, not preserved by
    the mixer. Output acceptance must therefore check cycle parity and decode.
    """
    if not len(gammas) or len(gammas) != len(betas):
        raise ValueError("equal non-empty gamma and beta sequences are required")
    if any(not math.isfinite(float(value)) for value in [*gammas, *betas]):
        raise ValueError("QAOA angles must be finite")
    if type(shots) is not int or shots <= 0:
        raise ValueError("shots must be a positive integer")
    if not isinstance(objective, ParityQAOAObjective):
        raise ValueError("objective must be a ParityQAOAObjective")

    n = objective.physical_qubits
    instructions = [PortableInstruction("h", targets=(q,)) for q in range(n)]
    for gamma, beta in zip(gammas, betas):
        for q, coefficient in enumerate(objective.linear_z):
            if coefficient:
                instructions.append(PortableInstruction(
                    "rz", targets=(q,), params=(2 * float(gamma) * coefficient,)
                ))
        for cycle, coefficient in objective.cycle_z_terms:
            if len(cycle) == 1:
                instructions.append(PortableInstruction(
                    "rz", targets=(cycle[0],), params=(2 * float(gamma) * coefficient,)
                ))
                continue
            # Compute Z-string parity onto the last qubit, apply RZ, then uncompute.
            chain = tuple(zip(cycle[:-1], cycle[1:]))
            for control, target in chain:
                instructions.append(PortableInstruction("cx", targets=(target,), controls=(control,)))
            instructions.append(PortableInstruction(
                "rz", targets=(cycle[-1],), params=(2 * float(gamma) * coefficient,)
            ))
            for control, target in reversed(chain):
                instructions.append(PortableInstruction("cx", targets=(target,), controls=(control,)))
        instructions.extend(
            PortableInstruction("rx", targets=(q,), params=(2 * float(beta),))
            for q in range(n)
        )
    if any(not math.isfinite(param) for inst in instructions for param in inst.params):
        raise ValueError("QAOA rotation overflow")
    instructions.append(PortableInstruction("measure_all"))
    program = PortableProgram("higher-order-parity-qaoa", n, tuple(instructions), shots, {
        "algorithm": "higher_order_parity_QAOA",
        "layers": len(gammas),
        "gammas": [float(value) for value in gammas],
        "betas": [float(value) for value in betas],
        "contract_id": contract_id,
        "instance_sha256": objective.instance_sha256,
        "vertex_count": objective.encoding.vertex_count,
        "edge_order": [list(edge) for edge in objective.encoding.edges],
        "cycle_constraints": [list(cycle) for cycle in objective.encoding.cycle_constraints],
        "edge_costs": list(objective.edge_costs),
        "penalty_weight": objective.penalty_weight,
        "variable_order": list(range(n)),
        "bit_order": "qubit_0_is_integer_lsb",
        "objective_sense": "minimize",
        "objective_offset": objective.offset,
        "omitted_global_phase": True,
        "feasibility_preserving_mixer": False,
        "acceptance_requires_cycle_parity_and_decode": True,
        "evidence_level": "PROTOTYPE",
    })
    program.validate()
    return program
