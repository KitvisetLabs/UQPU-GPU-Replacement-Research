"""Reproduce Batch 012: bounded ideal simulation + existing-tier dry lowering.

Run from the installed prototype, or set PYTHONPATH=. from its directory:
python examples/run_qaoa_verification.py --output /tmp/qaoa-verification.json
No provider credentials, SDK or network calls are used.
"""
from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import asdict
from datetime import datetime, timezone
import hashlib
import json
import math
from pathlib import Path
import platform
import subprocess
from time import perf_counter

from uqpu.adapters.ibm import IBMQuantumAdapter
from uqpu.adapters.aws_braket import AWSBraketAdapter
from uqpu.adapters.azure import AzureQuantumAdapter
from uqpu.benchmark_contract import OptimizationBenchmarkContract
from uqpu.benchmark_tiers import representative_tiers
from uqpu.cloud import ExecutionRequirements, QuantumParadigm
from uqpu.optimization_baseline import demo_maxcut_triangle, exact_qubo_baseline
from uqpu.qaoa import qubo_to_ising, qaoa_program
from uqpu.qubo_serialization import to_portable_qubo
from uqpu.reference_certificate import ObjectiveReference, ReferenceKind, assess_minimization_quality
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut
from uqpu.small_statevector import probabilities, sample_counts


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()


def provider_payloads(program):
    result = []
    for adapter in (IBMQuantumAdapter(), AWSBraketAdapter(), AzureQuantumAdapter()):
        lowered = adapter.lower(program, ExecutionRequirements(QuantumParadigm.GATE_MODEL))
        dry = adapter.dry_run(lowered)
        result.append({
            'provider_id': lowered.provider_id, 'format': lowered.format,
            'payload': lowered.payload, 'metadata': dict(lowered.metadata),
            'evidence_level': dry['evidence_level'], 'paid_job_submitted': False,
            'payload_sha256': hashlib.sha256(lowered.payload.encode()).hexdigest(),
            'payload_bytes': len(lowered.payload.encode()),
        })
    return result


def simulate_fixture(name, instance, seed):
    start = perf_counter()
    obj = qubo_to_ising(instance)
    contract = OptimizationBenchmarkContract(name, 'batch012-verification-fixture', seed, len(obj.variables))
    energies = [instance.energy(obj.assignment(k)) for k in range(1 << len(obj.variables))]
    reference = exact_qubo_baseline(instance, max_variables=12)
    # A coarse deterministic p=1 grid is an experiment, not a global optimizer.
    # Ranges are chosen for these unit-weight MaxCut fixtures only.
    search_start = perf_counter()
    search = []
    best = None
    for gi in range(24):
        for bi in range(24):
            gamma, beta = math.pi * gi / 24, math.pi * bi / 24
            program = qaoa_program(instance, [gamma], [beta], shots=4096, contract_id=contract.contract_id)
            probs = probabilities(program)
            expected = sum(p * e for p, e in zip(probs, energies))
            search.append({'gamma': gamma, 'beta': beta, 'expected_objective': expected})
            if best is None or expected < best[0]:
                best = expected, program, probs
    search_seconds = perf_counter() - search_start
    expectation, program, probs = best
    counts = sample_counts(program, seed=seed)
    best_index = min(counts, key=lambda k: (energies[k], k))
    sampled_mean = sum(energies[k] * count for k, count in counts.items()) / program.shots
    optimum_probability = sum(p for p, e in zip(probs, energies) if math.isclose(e, reference.objective, abs_tol=1e-10))
    certificate = ObjectiveReference(contract.contract_id, ReferenceKind.EXACT_OPTIMUM, reference.objective,
        'exhaustive_enumeration', 'MEASURED_LOCAL', 'examples/run_qaoa_verification.py',
        'instance_sha256=' + obj.instance_sha256 + '; correctness fixture only, not a competitive baseline')
    quality = assess_minimization_quality(energies[best_index], certificate, contract.required_relative_gap)
    providers = provider_payloads(program)
    return {
        'name': name, 'contract': asdict(contract), 'contract_id': contract.contract_id,
        'instance_sha256': obj.instance_sha256, 'input': to_portable_qubo(instance).payload,
        'evidence_level': 'SIMULATION', 'noise_model': 'ideal_noiseless',
        'simulator': 'uqpu.small_statevector (CPU Python)', 'qubits': program.qubits,
        'reference': asdict(certificate), 'certificate_id': certificate.certificate_id,
        'exact_baseline_runtime_seconds': reference.runtime_seconds,
        'uniform_expected_objective': sum(energies) / len(energies),
        'selected_expected_objective': expectation, 'sampled_mean_objective': sampled_mean,
        'best_sampled_objective': energies[best_index], 'best_sampled_assignment': obj.assignment(best_index),
        'single_shot_optimum_probability_ideal': optimum_probability,
        'sampled_quality': asdict(quality), 'quantum_advantage_demonstrated': False,
        'grid': search, 'grid_evaluations': len(search), 'grid_runtime_seconds': search_seconds,
        'shots': program.shots, 'sampling_seed': seed, 'counts_integer_lsb': counts,
        'selected_probabilities_integer_lsb': probs, 'selected_program': asdict(program),
        'gate_counts_before_transpilation': dict(Counter(i.op for i in program.instructions)),
        'providers': providers, 'input_json_bytes': len(encoded(to_portable_qubo(instance).payload)),
        'counts_json_bytes': len(encoded(counts)), 'peak_memory_bytes': None,
        'dense_complex128_state_payload_bytes_model': 16 * (1 << program.qubits),
        'energy_joules': None, 'total_cost_usd': None, 'network_bytes': None,
        'wall_runtime_seconds': perf_counter() - start,
    }


def lower_tier(tier):
    start = perf_counter()
    instance, contract = tier.instance(), tier.contract()
    program = qaoa_program(instance, [0.6], [0.25], contract_id=contract.contract_id)
    providers = provider_payloads(program)
    return {
        'tier': tier.name, 'contract_id': contract.contract_id,
        'instance_sha256': program.metadata['instance_sha256'], 'qubits': program.qubits,
        'evidence_level': 'DRY_RUN_ONLY', 'parameter_selection': 'fixed unoptimized inspection angles',
        'gate_counts_before_transpilation': dict(Counter(i.op for i in program.instructions)),
        'providers': providers, 'classical_lowering_runtime_seconds': perf_counter() - start,
        'simulation_executed': False, 'qpu_executed': False,
        'hardware_connectivity_validated': False, 'output_quality': None,
        'dense_complex128_state_payload_bytes_model': 16 * (1 << program.qubits),
    }


def run():
    root = Path(__file__).resolve().parents[1]
    paths = ['uqpu/qaoa.py', 'uqpu/small_statevector.py', 'examples/run_qaoa_verification.py']
    try:
        base = subprocess.check_output(['git', 'rev-parse', 'HEAD'], cwd=root, text=True).strip()
    except (FileNotFoundError, subprocess.CalledProcessError):
        base = None
    return {
        'schema': 'uqpu-qaoa-verification-v1', 'created_utc': datetime.now(timezone.utc).isoformat(),
        'source_checkout_head': base,
        'executed_source_sha256': {p: hashlib.sha256((root / p).read_bytes()).hexdigest() for p in paths},
        'environment': {'python': platform.python_version(), 'platform': platform.platform(), 'machine': platform.machine()},
        'paid_job_submitted': False, 'quantum_advantage_demonstrated': False,
        'fixtures': [simulate_fixture('triangle', demo_maxcut_triangle(), 12),
                     simulate_fixture('er6', seeded_erdos_renyi_maxcut(6, 0.5, 42), 42),
                     simulate_fixture('er8', seeded_erdos_renyi_maxcut(8, 0.4, 73), 73)],
        'representative_tier_lowering': [lower_tier(t) for t in representative_tiers()],
        'limitations': ['Ideal CPU simulation only for 3/6/8-qubit fixtures; no noise or QPU execution.',
            'Exhaustive reference is a correctness oracle, not a competitive runtime baseline.',
            'Grid expectations are exact statevector calculations; 4096 pseudorandom shots apply only to each selected circuit.',
            'The grid is not certified optimal, and best-of-shots quality is not expected-objective quality.',
            'Memory payload model excludes Python objects, temporaries, probabilities and search records.',
            'Provider payloads are inspection only; no SDK parse, ISA transpilation, routing or target acceptance.',
            'Runtime includes classical simulation/search; no end-to-end economic ratio is established.'],
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = run()
    text = json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + '\n'
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text)
    else:
        print(text, end='')
