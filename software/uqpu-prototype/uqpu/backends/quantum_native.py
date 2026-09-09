from __future__ import annotations

import math
from .base import Backend, BackendAssessment
from ..ir import OperationKind, Workload, ResultContract
from ..resources import ResourceEstimate


_NATIVE_KINDS = {
    OperationKind.SEARCH,
    OperationKind.EXPECTATION,
    OperationKind.SAMPLE,
    OperationKind.OPTIMIZE,
    OperationKind.LINEAR_SOLVE,
    OperationKind.EIGEN,
    OperationKind.TRACE,
}


class QuantumNativeBackend(Backend):
    name = "quantum-native"

    def assess(self, workload: Workload) -> BackendAssessment:
        workload.validate()
        kinds = {op.kind for op in workload.operations}
        native_fraction = len(kinds & _NATIVE_KINDS) / len(kinds)
        supported = native_fraction > 0
        if not supported:
            return BackendAssessment(
                backend=self.name,
                supported=False,
                rationale=["No quantum-native mapping registered for this workload."],
                resources=ResourceEstimate(confidence=0.2),
                expected_quality=0.0,
                mode="Q_NATIVE",
            )

        n = max(2, int(math.log2(max(2, workload.input_bytes + 1))))
        logical_qubits = max(32, n * 8 + 32 * len(workload.operations))
        depth = max(100, int((n ** 2) * 50 / max(native_fraction, 0.1)))
        shots = 1
        if workload.contract in {ResultContract.SAMPLED, ResultContract.PROBABILISTIC, ResultContract.BOUNDED_ERROR}:
            shots = 1024
        elif workload.output_bytes > 1_000_000:
            shots = 4096

        prep_s = workload.input_bytes / 2e9
        exec_s = depth * 2e-7
        qec_s = exec_s * 2.0
        measure_s = shots * max(2e-6, workload.output_bytes / 1e12)
        decode_s = workload.output_bytes / 2e9
        energy = (prep_s + exec_s + qec_s + measure_s + decode_s) * 20_000.0
        quality = 0.995 if workload.contract != ResultContract.EXACT else 0.85
        return BackendAssessment(
            backend=self.name,
            supported=True,
            rationale=[
                f"Quantum-native coverage fraction: {native_fraction:.2f}",
                "Estimate includes state preparation, QEC, shots, measurement and decode.",
            ],
            resources=ResourceEstimate(
                logical_qubits=logical_qubits,
                physical_qubits=logical_qubits * 500,
                logical_depth=depth,
                non_clifford_gates=int(depth * 0.2),
                shots=shots,
                state_prep_seconds=prep_s,
                execution_seconds=exec_s,
                qec_seconds=qec_s,
                measurement_seconds=measure_s,
                decode_seconds=decode_s,
                energy_joules=energy,
                confidence=0.25,
            ),
            expected_quality=quality,
            mode="Q_NATIVE",
        )
