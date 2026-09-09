from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Mapping

from .cloud import ExecutionRequirements, ProviderProfile


@dataclass(frozen=True)
class LoweredProgram:
    provider_id: str
    format: str
    payload: Any
    metadata: Mapping[str, Any]


class ProviderAdapter(ABC):
    """Provider SDK boundary.

    Vendor SDK imports must live inside concrete adapter modules only.
    The UQPU semantic compiler must remain provider-agnostic.
    """

    profile: ProviderProfile

    @abstractmethod
    def discover(self) -> ProviderProfile:
        raise NotImplementedError

    @abstractmethod
    def lower(self, portable_program: Any, requirements: ExecutionRequirements) -> LoweredProgram:
        raise NotImplementedError

    @abstractmethod
    def dry_run(self, program: LoweredProgram) -> Mapping[str, Any]:
        raise NotImplementedError

    @abstractmethod
    def submit(self, program: LoweredProgram) -> str:
        """Submit a real job and return provider job id.

        Concrete adapters should require explicit credentials/budget and
        should never silently submit paid jobs.
        """
        raise NotImplementedError

    @abstractmethod
    def result(self, job_id: str) -> Mapping[str, Any]:
        raise NotImplementedError
