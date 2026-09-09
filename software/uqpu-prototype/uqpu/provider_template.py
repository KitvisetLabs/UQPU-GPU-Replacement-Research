from __future__ import annotations

from typing import Any, Mapping

from .cloud import ExecutionRequirements
from .provider_adapter import LoweredProgram
from .provider_adapters import BaseConcreteAdapter
from .provider_runtime import AdapterReadiness, SubmissionGuard


class NewProviderAdapter(BaseConcreteAdapter):
    """Copy this class when onboarding a newly launched quantum-cloud provider."""

    provider_id = "REPLACE_WITH_PROVIDER_ID"
    readiness = AdapterReadiness.SERIALIZATION_READY
    sdk_module = ""
    credential_env = ()

    def lower(self, portable_program: Any, requirements: ExecutionRequirements) -> LoweredProgram:
        return super().lower(portable_program, requirements)

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        raise NotImplementedError("implement provider SDK/API submission")

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise NotImplementedError("implement provider result normalization")
