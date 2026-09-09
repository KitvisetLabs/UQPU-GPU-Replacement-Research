from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
import os
from typing import Any, Mapping

from .provider_adapter import LoweredProgram


class AdapterReadiness(str, Enum):
    SERIALIZATION_READY = "serialization_ready"
    SIMULATOR_READY = "simulator_ready"
    REAL_SUBMIT_IMPLEMENTED = "real_submit_implemented"
    AGGREGATOR_ROUTED = "aggregator_routed"
    DISCOVERY_ONLY = "discovery_only"


@dataclass(frozen=True)
class RuntimeConfig:
    provider_id: str
    target: str = ""
    shots: int = 1000
    options: Mapping[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if not self.provider_id:
            raise ValueError("provider_id is required")
        if self.shots <= 0:
            raise ValueError("shots must be positive")


@dataclass(frozen=True)
class SubmissionGuard:
    paid_execution: bool = False
    explicit_consent: bool = False
    max_budget_usd: float | None = None

    def assert_allowed(self) -> None:
        if self.paid_execution and not self.explicit_consent:
            raise PermissionError("paid QPU execution requires explicit consent")
        if self.max_budget_usd is not None and self.max_budget_usd < 0:
            raise ValueError("max_budget_usd must be non-negative")


@dataclass(frozen=True)
class AdapterHealth:
    provider_id: str
    readiness: AdapterReadiness
    sdk: str
    installed: bool
    credentials_present: bool
    target: str
    notes: str = ""


def env_present(*names: str) -> bool:
    return any(bool(os.getenv(n)) for n in names)


def generic_dry_run(program: LoweredProgram, config: RuntimeConfig) -> Mapping[str, Any]:
    config.validate()
    return {
        "provider_id": config.provider_id,
        "target": config.target,
        "shots": config.shots,
        "format": program.format,
        "metadata": dict(program.metadata),
        "status": "DRY_RUN_ONLY",
        "payload_type": type(program.payload).__name__,
    }
