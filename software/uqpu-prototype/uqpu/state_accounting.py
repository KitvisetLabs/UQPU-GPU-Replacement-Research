from __future__ import annotations
from dataclasses import dataclass


@dataclass(frozen=True)
class StateAccounting:
    input_bytes: int
    intermediate_bytes_materialized: int
    output_bytes: int
    persistent_bytes: int
    host_memory_seconds: float = 0.0
    transfer_bytes: int = 0

    def validate(self) -> None:
        vals=(self.input_bytes,self.intermediate_bytes_materialized,self.output_bytes,self.persistent_bytes,self.transfer_bytes)
        if any(v<0 for v in vals):
            raise ValueError("byte counts must be non-negative")
        if self.host_memory_seconds<0:
            raise ValueError("host_memory_seconds must be non-negative")

    @property
    def total_materialized_bytes(self) -> int:
        self.validate()
        return self.input_bytes+self.intermediate_bytes_materialized+self.output_bytes+self.persistent_bytes

    @property
    def total_data_movement_bytes(self) -> int:
        self.validate()
        return self.transfer_bytes+self.input_bytes+self.output_bytes


def materialization_reduction_ratio(classical: StateAccounting, uqpu: StateAccounting) -> float:
    c=classical.total_materialized_bytes
    q=uqpu.total_materialized_bytes
    if c<=0:
        raise ValueError("classical materialization must be positive")
    return max(0.0,(c-q)/c)
