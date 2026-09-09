from __future__ import annotations

from typing import Any, Mapping

from ..cloud import ExecutionRequirements
from ..provider_adapter import LoweredProgram, ProviderAdapter
from ..providers import default_provider_registry
from ..portable import PortableProgram
from .common import to_openqasm3, validate_gate_program


class AWSBraketAdapter(ProviderAdapter):
    """Amazon Braket gate-model adapter using OpenQASM 3 inspection payloads."""

    def __init__(self, device_arn: str = ""):
        self.profile = default_provider_registry().get("aws_braket")
        self.device_arn = device_arn

    def discover(self):
        return self.profile

    def lower(self, portable_program: PortableProgram, requirements: ExecutionRequirements) -> LoweredProgram:
        if not self.profile.supports_paradigm(requirements.paradigm):
            raise ValueError("AWS Braket profile does not support requested paradigm")
        if not self.profile.supports(requirements.capabilities):
            raise ValueError("AWS Braket profile lacks required capabilities")
        validate_gate_program(portable_program)
        qasm = to_openqasm3(portable_program)
        return LoweredProgram(
            provider_id=self.profile.provider_id,
            format="openqasm3",
            payload=qasm,
            metadata={
                "execution_api": "amazon-braket-sdk",
                "device_arn": self.device_arn,
                "shots": portable_program.shots,
                "submission_shape": "AwsDevice(device_arn).run(program, shots=shots)",
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
            "Paid Braket submission is disabled in the base prototype. "
            "Install the AWS extra, configure credentials/device ARN and use explicit consent."
        )

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("No job was submitted by the dry-run adapter.")
