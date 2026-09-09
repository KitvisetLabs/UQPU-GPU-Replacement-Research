from __future__ import annotations

import math
from .base import Backend, BackendAssessment
from ..ir import Workload, ResultContract
from ..resources import ResourceEstimate


class ReversibleBackend(Backend):
    name = "reversible-fallback"

    def assess(self, workload: Workload) -> BackendAssessment:
        workload.validate()
        io_bits = max(8, (workload.input_bytes + workload.output_bytes) * 8)
        op_factor = max(1, len(workload.operations))
        logical_qubits = max(32, min(2_000_000, int(math.sqrt(io_bits)) * 4 + 64 * op_factor))
        logical_depth = max(100, int(io_bits * op_factor * 0.8))
        non_clifford = max(10, int(logical_depth * 0.35))
        physical_qubits = logical_qubits * 1000
        exec_s = logical_depth * 1e-6
        qec_s = exec_s * 4.0
        meas_s = max(1e-6, workload.output_bytes / 5e9)
        energy = (exec_s + qec_s + meas_s) * 50_000.0
        return BackendAssessment(
            backend=self.name,
            supported=True,
            rationale=[
                "Universal reversible fallback preserves functional completeness.",
                "Estimate intentionally penalizes deep exact classical emulation.",
            ],
            resources=ResourceEstimate(
                logical_qubits=logical_qubits,
                physical_qubits=physical_qubits,
                logical_depth=logical_depth,
                non_clifford_gates=non_clifford,
                shots=1,
                state_prep_seconds=workload.input_bytes / 1e9,
                execution_seconds=exec_s,
                qec_seconds=qec_s,
                measurement_seconds=meas_s,
                decode_seconds=workload.output_bytes / 1e9,
                energy_joules=energy,
                confidence=0.35,
            ),
            expected_quality=1.0 if workload.contract == ResultContract.EXACT else 0.999,
            mode="Q_REVERSIBLE",
        )
