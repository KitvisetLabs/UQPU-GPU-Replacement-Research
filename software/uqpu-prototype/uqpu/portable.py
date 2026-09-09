from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Mapping, Sequence


@dataclass(frozen=True)
class PortableInstruction:
    op: str
    targets: tuple[int, ...] = ()
    controls: tuple[int, ...] = ()
    params: tuple[float, ...] = ()
    metadata: Mapping[str, Any] = field(default_factory=dict)


@dataclass(frozen=True)
class PortableProgram:
    """Provider-neutral executable quantum program.

    This intentionally represents only the execution layer. Higher-level
    UQPU Semantic IR remains responsible for workload meaning and may lower
    into different paradigms instead of gate circuits.
    """

    name: str
    qubits: int
    instructions: tuple[PortableInstruction, ...]
    shots: int = 1024
    metadata: Mapping[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.name.strip():
            raise ValueError("program name must be non-empty")
        if self.qubits <= 0:
            raise ValueError("qubits must be positive")
        if self.shots <= 0:
            raise ValueError("shots must be positive")
        for inst in self.instructions:
            for q in inst.targets + inst.controls:
                if q < 0 or q >= self.qubits:
                    raise ValueError(f"qubit index out of range: {q}")


def bell_program(shots: int = 1024) -> PortableProgram:
    return PortableProgram(
        name="bell",
        qubits=2,
        shots=shots,
        instructions=(
            PortableInstruction("h", targets=(0,)),
            PortableInstruction("cx", targets=(1,), controls=(0,)),
            PortableInstruction("measure_all"),
        ),
    )
