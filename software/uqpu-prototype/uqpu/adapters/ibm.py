from __future__ import annotations

from typing import Any, Mapping

from ..cloud import ExecutionRequirements
from ..provider_adapter import LoweredProgram, ProviderAdapter
from ..providers import default_provider_registry
from ..portable import PortableProgram
from .common import dry_run_payload, to_openqasm3, validate_gate_program


class IBMQuantumAdapter(ProviderAdapter):
    """IBM Quantum adapter.

    Dry-run output uses OpenQASM 3 as a portable inspection format.
    Real execution is intentionally explicit and requires qiskit +
    qiskit-ibm-runtime, credentials, a backend and user consent/budget.
    """

    def __init__(self):
        self.profile = default_provider_registry().get("ibm_quantum")

    def discover(self):
        return self.profile

    def lower(self, portable_program: PortableProgram, requirements: ExecutionRequirements) -> LoweredProgram:
        if not self.profile.supports_paradigm(requirements.paradigm):
            raise ValueError("IBM profile does not support requested paradigm")
        if not self.profile.supports(requirements.capabilities):
            raise ValueError("IBM profile lacks required capabilities")
        validate_gate_program(portable_program)
        qasm = to_openqasm3(portable_program)
        return LoweredProgram(
            provider_id=self.profile.provider_id,
            format="openqasm3-inspection",
            payload=qasm,
            metadata={
                "execution_api": "qiskit-ibm-runtime",
                "preferred_primitive": "SamplerV2",
                "note": "Real execution must transpile to backend ISA before SamplerV2/Executor submission.",
                "shots": portable_program.shots,
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
            "Paid IBM submission is disabled in the base prototype. "
            "Install the IBM extra and use a credentialed execution plugin with explicit consent."
        )

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("No job was submitted by the dry-run adapter.")
