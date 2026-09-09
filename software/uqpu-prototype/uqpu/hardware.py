from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class QuantumHardwareProfile:
    name: str
    physical_error_rate: float
    qec_threshold: float
    logical_cycle_seconds: float
    measurement_seconds: float
    state_prep_bandwidth_bytes_s: float
    decode_bandwidth_bytes_s: float
    control_power_watts: float
    cooling_power_watts: float
    capex_usd: float
    lifetime_seconds: float
    utilization: float = 0.7

    def validate(self) -> None:
        if not (0 < self.physical_error_rate < 1):
            raise ValueError("physical_error_rate must be in (0,1)")
        if not (0 < self.qec_threshold < 1):
            raise ValueError("qec_threshold must be in (0,1)")
        if self.physical_error_rate >= self.qec_threshold:
            raise ValueError("physical_error_rate must be below qec_threshold")
        if self.logical_cycle_seconds <= 0 or self.measurement_seconds <= 0:
            raise ValueError("timings must be positive")
        if self.state_prep_bandwidth_bytes_s <= 0 or self.decode_bandwidth_bytes_s <= 0:
            raise ValueError("bandwidths must be positive")
        if self.capex_usd < 0 or self.lifetime_seconds <= 0:
            raise ValueError("invalid capex/lifetime")
        if not (0 < self.utilization <= 1):
            raise ValueError("utilization must be in (0,1]")

    @property
    def amortized_capex_per_second(self) -> float:
        self.validate()
        return self.capex_usd / (self.lifetime_seconds * self.utilization)


@dataclass(frozen=True)
class GPUHardwareProfile:
    name: str
    capex_usd: float
    lifetime_seconds: float
    utilization: float
    board_power_watts: float
    system_overhead_watts: float
    cooling_multiplier: float = 0.25

    def validate(self) -> None:
        if self.capex_usd < 0 or self.lifetime_seconds <= 0:
            raise ValueError("invalid capex/lifetime")
        if not (0 < self.utilization <= 1):
            raise ValueError("utilization must be in (0,1]")
        if self.board_power_watts < 0 or self.system_overhead_watts < 0:
            raise ValueError("power must be non-negative")
        if self.cooling_multiplier < 0:
            raise ValueError("cooling_multiplier must be non-negative")

    @property
    def amortized_capex_per_second(self) -> float:
        self.validate()
        return self.capex_usd / (self.lifetime_seconds * self.utilization)
