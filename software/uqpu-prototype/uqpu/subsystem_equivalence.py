from __future__ import annotations

from dataclasses import dataclass
import math


def _finite_nonnegative(name: str, value: float) -> None:
    if not math.isfinite(value) or value < 0:
        raise ValueError(f"{name} must be finite and non-negative")


@dataclass(frozen=True)
class ComputeServiceContract:
    min_tasks_per_second: float
    max_latency_seconds: float
    min_quality: float

    def __post_init__(self) -> None:
        _finite_nonnegative("min_tasks_per_second", self.min_tasks_per_second)
        _finite_nonnegative("max_latency_seconds", self.max_latency_seconds)
        if not 0 <= self.min_quality <= 1:
            raise ValueError("min_quality must be in [0,1]")

    def accepts(self, candidate: "ComputeServiceMeasurement") -> bool:
        return (
            candidate.tasks_per_second >= self.min_tasks_per_second
            and candidate.latency_seconds <= self.max_latency_seconds
            and candidate.quality >= self.min_quality
        )


@dataclass(frozen=True)
class ComputeServiceMeasurement:
    tasks_per_second: float
    latency_seconds: float
    quality: float

    def __post_init__(self) -> None:
        _finite_nonnegative("tasks_per_second", self.tasks_per_second)
        _finite_nonnegative("latency_seconds", self.latency_seconds)
        if not 0 <= self.quality <= 1:
            raise ValueError("quality must be in [0,1]")


@dataclass(frozen=True)
class StateServiceContract:
    min_capacity_bytes: int
    min_read_bandwidth_bytes_per_second: float
    min_write_bandwidth_bytes_per_second: float
    max_read_latency_seconds: float
    max_write_latency_seconds: float
    min_retention_seconds: float
    random_access_required: bool
    persistence_required: bool
    min_recovery_probability: float = 1.0

    def __post_init__(self) -> None:
        if type(self.min_capacity_bytes) is not int or self.min_capacity_bytes < 0:
            raise ValueError("min_capacity_bytes must be a non-negative integer")
        for name, value in (
            ("min_read_bandwidth_bytes_per_second", self.min_read_bandwidth_bytes_per_second),
            ("min_write_bandwidth_bytes_per_second", self.min_write_bandwidth_bytes_per_second),
            ("max_read_latency_seconds", self.max_read_latency_seconds),
            ("max_write_latency_seconds", self.max_write_latency_seconds),
            ("min_retention_seconds", self.min_retention_seconds),
        ):
            _finite_nonnegative(name, value)
        if not 0 <= self.min_recovery_probability <= 1:
            raise ValueError("min_recovery_probability must be in [0,1]")

    def accepts(self, candidate: "StateServiceMeasurement") -> bool:
        return (
            candidate.capacity_bytes >= self.min_capacity_bytes
            and candidate.read_bandwidth_bytes_per_second >= self.min_read_bandwidth_bytes_per_second
            and candidate.write_bandwidth_bytes_per_second >= self.min_write_bandwidth_bytes_per_second
            and candidate.read_latency_seconds <= self.max_read_latency_seconds
            and candidate.write_latency_seconds <= self.max_write_latency_seconds
            and candidate.retention_seconds >= self.min_retention_seconds
            and (not self.random_access_required or candidate.random_access)
            and (not self.persistence_required or candidate.persistent)
            and candidate.recovery_probability >= self.min_recovery_probability
        )


@dataclass(frozen=True)
class StateServiceMeasurement:
    capacity_bytes: int
    read_bandwidth_bytes_per_second: float
    write_bandwidth_bytes_per_second: float
    read_latency_seconds: float
    write_latency_seconds: float
    retention_seconds: float
    random_access: bool
    persistent: bool
    recovery_probability: float

    def __post_init__(self) -> None:
        if type(self.capacity_bytes) is not int or self.capacity_bytes < 0:
            raise ValueError("capacity_bytes must be a non-negative integer")
        for name, value in (
            ("read_bandwidth_bytes_per_second", self.read_bandwidth_bytes_per_second),
            ("write_bandwidth_bytes_per_second", self.write_bandwidth_bytes_per_second),
            ("read_latency_seconds", self.read_latency_seconds),
            ("write_latency_seconds", self.write_latency_seconds),
            ("retention_seconds", self.retention_seconds),
        ):
            _finite_nonnegative(name, value)
        if not 0 <= self.recovery_probability <= 1:
            raise ValueError("recovery_probability must be in [0,1]")
