from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, FrozenSet, Iterable


class QuantumParadigm(str, Enum):
    GATE_MODEL = "gate_model"
    ANALOG = "analog"
    ANNEALING = "annealing"
    PHOTONIC = "photonic"
    HYBRID = "hybrid"


class ProviderStatus(str, Enum):
    ACTIVE = "active"
    PREVIEW = "preview"
    ANNOUNCED = "announced"
    RETIRED = "retired"


class Capability(str, Enum):
    MID_CIRCUIT_MEASUREMENT = "mid_circuit_measurement"
    RESET = "reset"
    CLASSICAL_FEED_FORWARD = "classical_feed_forward"
    DYNAMIC_CIRCUITS = "dynamic_circuits"
    PULSE_CONTROL = "pulse_control"
    ANALOG_HAMILTONIAN = "analog_hamiltonian"
    QUBO_ISING = "qubo_ising"
    PHOTONIC_FOCK = "photonic_fock"
    BATCH = "batch"
    SESSION = "session"
    RESERVATION = "reservation"
    SIMULATOR = "simulator"


@dataclass(frozen=True)
class ProviderProfile:
    provider_id: str
    display_name: str
    cloud: str
    paradigms: FrozenSet[QuantumParadigm]
    capabilities: FrozenSet[Capability]
    sdk: str
    program_formats: tuple[str, ...] = ()
    status: ProviderStatus = ProviderStatus.ACTIVE
    access_url: str = ""
    notes: str = ""

    def supports(self, required: Iterable[Capability]) -> bool:
        return set(required).issubset(self.capabilities)

    def supports_paradigm(self, paradigm: QuantumParadigm) -> bool:
        return paradigm in self.paradigms


@dataclass(frozen=True)
class ExecutionRequirements:
    paradigm: QuantumParadigm
    capabilities: FrozenSet[Capability] = field(default_factory=frozenset)


@dataclass(frozen=True)
class CompatibilityResult:
    provider_id: str
    compatible: bool
    missing_capabilities: tuple[str, ...]
    paradigm_supported: bool
    status: str


class ProviderRegistry:
    def __init__(self, profiles: Iterable[ProviderProfile] = ()):
        self._profiles: Dict[str, ProviderProfile] = {}
        for profile in profiles:
            self.register(profile)

    def register(self, profile: ProviderProfile) -> None:
        if not profile.provider_id.strip():
            raise ValueError("provider_id must be non-empty")
        self._profiles[profile.provider_id] = profile

    def get(self, provider_id: str) -> ProviderProfile:
        return self._profiles[provider_id]

    def all(self) -> tuple[ProviderProfile, ...]:
        return tuple(self._profiles.values())

    def compatible(self, req: ExecutionRequirements, active_only: bool = True) -> tuple[CompatibilityResult, ...]:
        out = []
        for p in self._profiles.values():
            if active_only and p.status != ProviderStatus.ACTIVE:
                continue
            paradigm_ok = p.supports_paradigm(req.paradigm)
            missing = tuple(sorted(c.value for c in req.capabilities if c not in p.capabilities))
            out.append(CompatibilityResult(
                provider_id=p.provider_id,
                compatible=paradigm_ok and not missing,
                missing_capabilities=missing,
                paradigm_supported=paradigm_ok,
                status=p.status.value,
            ))
        return tuple(out)
