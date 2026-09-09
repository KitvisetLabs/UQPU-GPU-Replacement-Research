from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class MemoryFootprint:
    accelerator_bytes: int = 0
    host_ram_bytes: int = 0
    bytes_moved: int = 0
    state_prep_bytes: int = 0
    output_bytes: int = 0

    def validate(self) -> None:
        values = (
            self.accelerator_bytes,
            self.host_ram_bytes,
            self.bytes_moved,
            self.state_prep_bytes,
            self.output_bytes,
        )
        if any(v < 0 for v in values):
            raise ValueError("memory values must be non-negative")


@dataclass(frozen=True)
class MemoryCostProfile:
    accelerator_memory_usd_per_gb_second: float
    host_ram_usd_per_gb_second: float
    movement_joules_per_gb: float
    electricity_per_kwh: float = 0.12

    def validate(self) -> None:
        if self.accelerator_memory_usd_per_gb_second < 0:
            raise ValueError("accelerator memory cost must be non-negative")
        if self.host_ram_usd_per_gb_second < 0:
            raise ValueError("host RAM cost must be non-negative")
        if self.movement_joules_per_gb < 0 or self.electricity_per_kwh < 0:
            raise ValueError("energy/cost values must be non-negative")


@dataclass(frozen=True)
class MemoryCostBreakdown:
    accelerator_memory: float
    host_ram: float
    movement_energy: float
    total: float


def estimate_memory_cost(
    footprint: MemoryFootprint,
    runtime_seconds: float,
    profile: MemoryCostProfile,
) -> MemoryCostBreakdown:
    footprint.validate()
    profile.validate()
    if runtime_seconds < 0:
        raise ValueError("runtime_seconds must be non-negative")

    gb = 1024 ** 3
    accelerator = (
        footprint.accelerator_bytes / gb
        * runtime_seconds
        * profile.accelerator_memory_usd_per_gb_second
    )
    host = (
        footprint.host_ram_bytes / gb
        * runtime_seconds
        * profile.host_ram_usd_per_gb_second
    )
    moved_gb = footprint.bytes_moved / gb
    movement_j = moved_gb * profile.movement_joules_per_gb
    movement_energy = movement_j / 3_600_000.0 * profile.electricity_per_kwh
    return MemoryCostBreakdown(
        accelerator_memory=accelerator,
        host_ram=host,
        movement_energy=movement_energy,
        total=accelerator + host + movement_energy,
    )


def materialization_avoidance_ratio(
    conventional_materialized_bytes: int,
    uqpu_materialized_bytes: int,
) -> float:
    if conventional_materialized_bytes <= 0:
        raise ValueError("conventional_materialized_bytes must be positive")
    if uqpu_materialized_bytes < 0:
        raise ValueError("uqpu_materialized_bytes must be non-negative")
    return 1.0 - (uqpu_materialized_bytes / conventional_materialized_bytes)
