from __future__ import annotations

from typing import Any, Mapping

from ..cloud import ExecutionRequirements
from ..provider_adapter import LoweredProgram, ProviderAdapter
from ..providers import default_provider_registry
from ..portable import PortableProgram
from .common import to_openqasm3, validate_gate_program


class AzureQuantumAdapter(ProviderAdapter):
    """Azure Quantum adapter boundary.

    Azure routes execution to provider-specific targets, so dry-run metadata
    keeps target name explicit instead of pretending all Azure targets share
    one ISA.
    """

    def __init__(self, target: str = ""):
        self.profile = default_provider_registry().get("azure_quantum")
        self.target = target

    def discover(self):
        return self.profile

    def lower(self, portable_program: PortableProgram, requirements: ExecutionRequirements) -> LoweredProgram:
        if not self.profile.supports_paradigm(requirements.paradigm):
            raise ValueError("Azure Quantum profile does not support requested paradigm")
        if not self.profile.supports(requirements.capabilities):
            raise ValueError("Azure Quantum aggregate profile lacks required capabilities")
        validate_gate_program(portable_program)
        return LoweredProgram(
            provider_id=self.profile.provider_id,
            format="qiskit/openqasm3-intermediate",
            payload=to_openqasm3(portable_program),
            metadata={
                "execution_api": "qdk[azure,qiskit]",
                "target": self.target,
                "shots": portable_program.shots,
                "note": "Real lowering must be refined against the selected Azure provider target.",
            },
        )

    def dry_run(self, program: LoweredProgram) -> Mapping[str, Any]:
        return {
            "provider_id": program.provider_id,
            "format": program.format,
            "payload": program.payload,
            "metadata": dict(program.metadata),
            "evidence_level": "DRY_RUN_ONLY",
            "paid_job_submitted": False,
        }

    def submit(self, program: LoweredProgram) -> str:
        raise RuntimeError(
            "Paid Azure submission is disabled in the base prototype. "
            "Install the Azure extra, configure workspace/target credentials and use explicit consent."
        )

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("No job was submitted by the dry-run adapter.")
