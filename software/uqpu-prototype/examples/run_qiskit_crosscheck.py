"""Independently parse Batch 012 QASM, simulate and test synthetic routing.

Requires verification-optional-requirements.txt in a Python 3.12 environment.
No credentials, account discovery, QPU submission or backend download occurs.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
from pathlib import Path
import platform
from time import perf_counter

from uqpu.sdk_verification import classical_probabilities, terminal_measurement_map


def run(artifact_path):
    from qiskit import qasm3, transpile
    from qiskit.transpiler import CouplingMap
    data = json.loads(artifact_path.read_text())
    rows = []
    for fixture in data['fixtures']:
        reference = fixture['selected_probabilities_integer_lsb']
        for payload in fixture['providers']:
            start = perf_counter()
            text = payload['payload']
            digest = hashlib.sha256(text.encode()).hexdigest()
            if digest != payload['payload_sha256']:
                raise ValueError('input payload hash mismatch')
            circuit = qasm3.loads(text)
            original = classical_probabilities(circuit)
            routed = transpile(circuit, coupling_map=CouplingMap.from_line(circuit.num_qubits),
                basis_gates=['rz', 'sx', 'x', 'cx'], optimization_level=2, seed_transpiler=17)
            decoded = classical_probabilities(routed)
            raw_error = max(abs(a - b) for a, b in zip(original, reference))
            routed_error = max(abs(a - b) for a, b in zip(decoded, reference))
            if len(reference) != len(original) or max(raw_error, routed_error) > 1e-10:
                raise AssertionError('independent SDK distribution disagreement')
            rows.append({
                'fixture': fixture['name'], 'contract_id': fixture['contract_id'],
                'instance_sha256': fixture['instance_sha256'], 'provider_payload': payload['provider_id'],
                'qasm_sha256': digest, 'max_absolute_probability_error': raw_error,
                'max_routed_decoded_probability_error': routed_error,
                'measurement_map_after_routing': terminal_measurement_map(routed),
                'logical_cx': int(circuit.count_ops().get('cx', 0)),
                'routed_cx': int(routed.count_ops().get('cx', 0)),
                'logical_depth': circuit.depth(), 'routed_depth': routed.depth(),
                'runtime_seconds': perf_counter() - start, 'accepted': True,
                'evidence_level': 'SIMULATION',
            })
    tiers = []
    for tier in data['representative_tier_lowering']:
        for payload in tier['providers']:
            digest = hashlib.sha256(payload['payload'].encode()).hexdigest()
            if digest != payload['payload_sha256']:
                raise ValueError('input payload hash mismatch')
            circuit = qasm3.loads(payload['payload'])
            terminal_measurement_map(circuit)
            if circuit.num_qubits != tier['qubits']:
                raise AssertionError('register width changed')
            row = {'tier': tier['tier'], 'contract_id': tier['contract_id'],
                'provider_payload': payload['provider_id'], 'qubits': circuit.num_qubits,
                'qasm_sha256': digest, 'sdk_parse_passed': True, 'simulation_executed': False,
                'qpu_executed': False, 'evidence_level': 'DRY_RUN_ONLY'}
            # One synthetic routing study, no state allocation for 32+ qubits.
            if tier['tier'] == 'small' and payload['provider_id'] == 'ibm_quantum':
                start = perf_counter()
                routed = transpile(circuit, coupling_map=CouplingMap.from_line(circuit.num_qubits),
                    basis_gates=['rz', 'sx', 'x', 'cx'], optimization_level=2, seed_transpiler=17)
                row['synthetic_line_routing'] = {
                    'logical_cx': int(circuit.count_ops().get('cx', 0)),
                    'routed_cx': int(routed.count_ops().get('cx', 0)),
                    'logical_depth': circuit.depth(), 'routed_depth': routed.depth(),
                    'runtime_seconds': perf_counter() - start,
                    'measurement_map': terminal_measurement_map(routed),
                    'hardware_calibration': None,
                }
            tiers.append(row)
    root = Path(__file__).resolve().parents[1]
    return {
        'schema': 'uqpu-qiskit-crosscheck-v1', 'created_utc': datetime.now(timezone.utc).isoformat(),
        'input_artifact_sha256': hashlib.sha256(artifact_path.read_bytes()).hexdigest(),
        'executed_source_sha256': {p: hashlib.sha256((root / p).read_bytes()).hexdigest()
                                  for p in ('uqpu/sdk_verification.py', 'examples/run_qiskit_crosscheck.py')},
        'environment': {'python': platform.python_version(), 'platform': platform.platform(),
            'packages': {d.metadata['Name']: d.version for d in importlib.metadata.distributions()}},
        'synthetic_routing': {'coupling': 'bidirectional nearest-neighbor line',
            'basis_gates': ['rz', 'sx', 'x', 'cx'], 'optimization_level': 2, 'seed_transpiler': 17},
        'fixtures': rows, 'tier_parsing': tiers,
        'max_absolute_probability_error': max(r['max_absolute_probability_error'] for r in rows),
        'max_routed_decoded_probability_error': max(r['max_routed_decoded_probability_error'] for r in rows),
        'paid_job_submitted': False, 'quantum_advantage_demonstrated': False,
        'limitations': ['Qiskit is an independent simulator implementation, not independent research replication.',
            'Parsing Braket/Azure-labelled QASM in Qiskit does not establish Braket/Azure target acceptance.',
            'Synthetic line routing is not a provider topology, calibration or physical performance measurement.',
            'Transpiled 32-qubit circuit is not statevector simulated; no duration, noise, energy or cost claim.',
            '3/6/8-qubit results are ideal probability comparisons, not real-QPU results.'],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, default=Path(__file__).resolve().parents[3] / 'benchmarks/results/batch012-qaoa-verification.json')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = run(args.input)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, allow_nan=False) + '\n')
    print(json.dumps({k: result[k] for k in ('max_absolute_probability_error', 'max_routed_decoded_probability_error')}))
