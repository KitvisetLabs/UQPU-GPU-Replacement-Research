from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ResourceEstimate:
    logical_qubits: int = 0
    physical_qubits: int = 0
    logical_depth: int = 0
    non_clifford_gates: int = 0
    shots: int = 1
    state_prep_seconds: float = 0.0
    execution_seconds: float = 0.0
    qec_seconds: float = 0.0
    measurement_seconds: float = 0.0
    decode_seconds: float = 0.0
    energy_joules: float = 0.0
    confidence: float = 0.5

    @property
    def total_seconds(self) -> float:
        return (
            self.state_prep_seconds
            + self.execution_seconds
            + self.qec_seconds
            + self.measurement_seconds
            + self.decode_seconds
        )
