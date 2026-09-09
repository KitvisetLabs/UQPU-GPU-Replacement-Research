from __future__ import annotations

import importlib.util
import json
import os
from dataclasses import dataclass
from typing import Any, Mapping
from urllib.request import Request, urlopen

from .cloud import ExecutionRequirements
from .provider_adapter import LoweredProgram, ProviderAdapter
from .provider_runtime import (
    AdapterHealth,
    AdapterReadiness,
    RuntimeConfig,
    SubmissionGuard,
    env_present,
    generic_dry_run,
)
from .providers import default_provider_registry


def _profile(provider_id: str):
    return default_provider_registry().get(provider_id)


def _installed(module: str) -> bool:
    return importlib.util.find_spec(module) is not None


class BaseConcreteAdapter(ProviderAdapter):
    provider_id: str
    readiness: AdapterReadiness
    sdk_module: str = ""
    credential_env: tuple[str, ...] = ()

    def __init__(self, config: RuntimeConfig | None = None):
        self.profile = _profile(self.provider_id)
        self.config = config or RuntimeConfig(self.provider_id)

    def discover(self):
        return self.profile

    def lower(self, portable_program: Any, requirements: ExecutionRequirements) -> LoweredProgram:
        return LoweredProgram(
            self.provider_id,
            self.profile.program_formats[0] if self.profile.program_formats else "provider-native",
            portable_program,
            {
                "paradigm": requirements.paradigm.value,
                "required_capabilities": sorted(c.value for c in requirements.capabilities),
                "target": self.config.target,
            },
        )

    def dry_run(self, program: LoweredProgram) -> Mapping[str, Any]:
        return generic_dry_run(program, self.config)

    def health(self) -> AdapterHealth:
        return AdapterHealth(
            provider_id=self.provider_id,
            readiness=self.readiness,
            sdk=self.profile.sdk,
            installed=(not self.sdk_module) or _installed(self.sdk_module),
            credentials_present=(not self.credential_env) or env_present(*self.credential_env),
            target=self.config.target,
        )

    def _guard(self, guard: SubmissionGuard | None, *, paid: bool = True) -> None:
        (guard or SubmissionGuard(paid_execution=paid)).assert_allowed()


class IBMQuantumAdapter(BaseConcreteAdapter):
    provider_id = "ibm_quantum"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "qiskit_ibm_runtime"
    credential_env = ("QISKIT_IBM_TOKEN", "IBM_QUANTUM_TOKEN")

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        from qiskit_ibm_runtime import QiskitRuntimeService, SamplerV2 as Sampler
        token = os.getenv("QISKIT_IBM_TOKEN") or os.getenv("IBM_QUANTUM_TOKEN")
        service = QiskitRuntimeService(token=token) if token else QiskitRuntimeService()
        backend = service.backend(self.config.target) if self.config.target else service.least_busy(operational=True, simulator=False)
        job = Sampler(mode=backend).run([program.payload], shots=self.config.shots)
        return job.job_id()

    def result(self, job_id: str) -> Mapping[str, Any]:
        from qiskit_ibm_runtime import QiskitRuntimeService
        token = os.getenv("QISKIT_IBM_TOKEN") or os.getenv("IBM_QUANTUM_TOKEN")
        service = QiskitRuntimeService(token=token) if token else QiskitRuntimeService()
        job = service.job(job_id)
        return {"job_id": job_id, "status": str(job.status()), "result": job.result()}


class AWSBraketAdapter(BaseConcreteAdapter):
    provider_id = "aws_braket"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "braket"
    credential_env = ("AWS_ACCESS_KEY_ID", "AWS_PROFILE")

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        if not self.config.target:
            raise ValueError("Amazon Braket requires target device ARN")
        from braket.aws import AwsDevice
        task = AwsDevice(self.config.target).run(program.payload, shots=self.config.shots)
        return task.id

    def result(self, job_id: str) -> Mapping[str, Any]:
        from braket.aws import AwsQuantumTask
        task = AwsQuantumTask(job_id)
        return {"job_id": job_id, "status": str(task.state()), "result": task.result()}


class AzureQuantumAdapter(BaseConcreteAdapter):
    provider_id = "azure_quantum"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "qdk"
    credential_env = ("AZURE_QUANTUM_RESOURCE_ID", "AZURE_QUANTUM_CONNECTION_STRING", "AZURE_TENANT_ID")

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        if not self.config.target:
            raise ValueError("Azure Quantum requires target id")
        # Azure target formats vary. Use the workspace target submit path when
        # an already provider-native payload is supplied.
        from qdk.azure import Workspace
        resource_id = os.getenv("AZURE_QUANTUM_RESOURCE_ID")
        connection = os.getenv("AZURE_QUANTUM_CONNECTION_STRING")
        if resource_id:
            workspace = Workspace(resource_id=resource_id)
        elif connection:
            workspace = Workspace.from_connection_string(connection)
        else:
            raise RuntimeError("AZURE_QUANTUM_RESOURCE_ID or AZURE_QUANTUM_CONNECTION_STRING is required")
        target = workspace.get_targets(self.config.target)
        kwargs = dict(self.config.options)
        kwargs.setdefault("shots", self.config.shots)
        job = target.submit(program.payload, **kwargs)
        return job.id

    def result(self, job_id: str) -> Mapping[str, Any]:
        from qdk.azure import Workspace
        resource_id = os.getenv("AZURE_QUANTUM_RESOURCE_ID")
        connection = os.getenv("AZURE_QUANTUM_CONNECTION_STRING")
        if resource_id:
            workspace = Workspace(resource_id=resource_id)
        elif connection:
            workspace = Workspace.from_connection_string(connection)
        else:
            raise RuntimeError("AZURE_QUANTUM_RESOURCE_ID or AZURE_QUANTUM_CONNECTION_STRING is required")
        job = workspace.get_job(job_id)
        return {"job_id": job_id, "status": str(job.details.status), "result": job.get_results()}


class IonQDirectAdapter(BaseConcreteAdapter):
    provider_id = "ionq_direct"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    credential_env = ("IONQ_API_KEY",)

    api_base = "https://api.ionq.co/v0.4"

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=self.config.target != "simulator")
        key = os.getenv("IONQ_API_KEY")
        if not key:
            raise RuntimeError("IONQ_API_KEY is required")
        payload = program.payload if isinstance(program.payload, dict) else {
            "type": "ionq.circuit.v1",
            "backend": self.config.target or "simulator",
            "shots": self.config.shots,
            "input": program.payload,
        }
        payload.setdefault("backend", self.config.target or "simulator")
        payload.setdefault("shots", self.config.shots)
        req = Request(
            f"{self.api_base}/jobs",
            data=json.dumps(payload).encode(),
            headers={"Authorization": f"apiKey {key}", "Content-Type": "application/json"},
            method="POST",
        )
        with urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode())
        return body["id"]

    def result(self, job_id: str) -> Mapping[str, Any]:
        key = os.getenv("IONQ_API_KEY")
        req = Request(f"{self.api_base}/jobs/{job_id}", headers={"Authorization": f"apiKey {key}"})
        with urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())


class RigettiQCSAdapter(BaseConcreteAdapter):
    provider_id = "rigetti_qcs"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "pyquil"
    credential_env = ("QCS_SETTINGS_APPLICATIONS_PYQUIL_QVM_URL", "QCS_SETTINGS_FILE_PATH")

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        if not self.config.target:
            raise ValueError("Rigetti QCS requires quantum_processor_id target")
        from pyquil import get_qc
        qc = get_qc(self.config.target)
        executable = qc.compile(program.payload)
        result = qc.run(executable)
        # pyQuil's high-level run may be synchronous; expose a synthetic id
        # while retaining the result for callers that use execute_sync().
        self._last_result = result
        return f"rigetti-sync:{id(result)}"

    def result(self, job_id: str) -> Mapping[str, Any]:
        if hasattr(self, "_last_result") and job_id.startswith("rigetti-sync:"):
            return {"job_id": job_id, "status": "completed", "result": self._last_result}
        raise RuntimeError("Rigetti high-level adapter currently retrieves results synchronously")


class DWaveLeapAdapter(BaseConcreteAdapter):
    provider_id = "dwave_leap"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "dwave"
    credential_env = ("DWAVE_API_TOKEN",)

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        from dwave.system import DWaveSampler, EmbeddingComposite
        sampler = EmbeddingComposite(DWaveSampler(solver={"name": self.config.target} if self.config.target else None))
        payload = program.payload
        if isinstance(payload, dict) and "Q" in payload:
            sample = sampler.sample_qubo(payload["Q"], num_reads=self.config.shots)
        elif isinstance(payload, dict) and "h" in payload and "J" in payload:
            sample = sampler.sample_ising(payload["h"], payload["J"], num_reads=self.config.shots)
        else:
            raise ValueError("D-Wave payload must contain Q or h/J")
        self._last_result = sample
        return f"dwave-sync:{id(sample)}"

    def result(self, job_id: str) -> Mapping[str, Any]:
        if hasattr(self, "_last_result") and job_id.startswith("dwave-sync:"):
            return {"job_id": job_id, "status": "completed", "result": self._last_result}
        raise RuntimeError("D-Wave high-level adapter currently retrieves results synchronously")


class QuantinuumNexusAdapter(BaseConcreteAdapter):
    provider_id = "quantinuum_nexus"
    readiness = AdapterReadiness.REAL_SUBMIT_IMPLEMENTED
    sdk_module = "qnexus"
    credential_env = ("QNEXUS_API_KEY",)

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        self._guard(guard, paid=True)
        import qnexus as qnx
        if not self.config.target:
            raise ValueError("Quantinuum Nexus requires target backend")
        ref = qnx.circuits.upload(circuit=program.payload, name=self.config.options.get("name", "uqpu-job"))
        job = qnx.execute.start_execute_job(
            circuits=[ref],
            n_shots=[self.config.shots],
            backend_config=qnx.BackendConfig(device_name=self.config.target),
        )
        return str(getattr(job, "id", job))

    def result(self, job_id: str) -> Mapping[str, Any]:
        import qnexus as qnx
        job = qnx.jobs.get(job_id)
        return {"job_id": job_id, "status": str(getattr(job, "status", "unknown")), "result": job}


class AggregatorRoutedAdapter(BaseConcreteAdapter):
    readiness = AdapterReadiness.AGGREGATOR_ROUTED
    routes: tuple[str, ...] = ()

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        raise RuntimeError(
            f"{self.provider_id} is prepared through aggregator routes {self.routes}; "
            "select aws_braket or azure_quantum with the provider target"
        )

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("retrieve the result through the selected aggregator adapter")


class IQMAdapter(AggregatorRoutedAdapter):
    provider_id = "iqm_resonance"
    routes = ("aws_braket",)
    sdk_module = "iqm"


class PasqalAdapter(AggregatorRoutedAdapter):
    provider_id = "pasqal_cloud"
    routes = ("azure_quantum",)
    sdk_module = "pulser"


class QuEraAdapter(AggregatorRoutedAdapter):
    provider_id = "quera"
    routes = ("aws_braket",)
    sdk_module = "bloqade"


class QuandelaAdapter(BaseConcreteAdapter):
    provider_id = "quandela_cloud"
    readiness = AdapterReadiness.SERIALIZATION_READY
    sdk_module = "perceval"

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        raise RuntimeError("Quandela direct remote submission requires account-specific RPC configuration; serialization/dry-run is ready")

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("Quandela direct result retrieval requires configured remote processor")


class OQCAdapter(BaseConcreteAdapter):
    provider_id = "oqc_cloud"
    readiness = AdapterReadiness.SERIALIZATION_READY

    def submit(self, program: LoweredProgram, guard: SubmissionGuard | None = None) -> str:
        raise RuntimeError("OQC direct runtime API must be configured for the account; serialization/dry-run is ready")

    def result(self, job_id: str) -> Mapping[str, Any]:
        raise RuntimeError("OQC direct result retrieval requires configured runtime endpoint")


ADAPTERS = {
    "ibm_quantum": IBMQuantumAdapter,
    "aws_braket": AWSBraketAdapter,
    "azure_quantum": AzureQuantumAdapter,
    "ionq_direct": IonQDirectAdapter,
    "rigetti_qcs": RigettiQCSAdapter,
    "dwave_leap": DWaveLeapAdapter,
    "iqm_resonance": IQMAdapter,
    "quantinuum_nexus": QuantinuumNexusAdapter,
    "pasqal_cloud": PasqalAdapter,
    "quera": QuEraAdapter,
    "quandela_cloud": QuandelaAdapter,
    "oqc_cloud": OQCAdapter,
}


def adapter_for(provider_id: str, config: RuntimeConfig | None = None) -> BaseConcreteAdapter:
    try:
        cls = ADAPTERS[provider_id]
    except KeyError as exc:
        raise KeyError(f"no adapter registered for {provider_id}") from exc
    return cls(config)


def adapter_health_matrix() -> tuple[AdapterHealth, ...]:
    return tuple(adapter_for(pid).health() for pid in ADAPTERS)
