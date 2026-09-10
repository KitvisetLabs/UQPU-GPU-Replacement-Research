"""Batch 020 candidate: equal-shot target-snapshot comparison for ER6 QAOA.

The two circuits are selected from the same ideal 24x24 p=1 grid: ordinary
mean energy versus lower-tail CVaR(alpha=0.5). Both are transpiled to the same
saved IBM FakeKingston snapshot with the same transpiler seed and simulated
with identical total shot budgets over deterministic simulator seeds.

This is calibration-snapshot simulation, not live QPU evidence.
"""
from __future__ import annotations

from collections import Counter
from datetime import datetime, timezone
import json
import math
import platform

from uqpu.adapters.ibm import IBMQuantumAdapter
from uqpu.benchmark_contract import OptimizationBenchmarkContract
from uqpu.cloud import ExecutionRequirements, QuantumParadigm
from uqpu.qaoa import qaoa_program, qubo_to_ising
from uqpu.qaoa_objective_selection import compare_p1_grid_objectives
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut


def _wilson_interval(successes: int, trials: int, z: float = 1.959963984540054):
    if trials <= 0 or not 0 <= successes <= trials:
        raise ValueError("invalid binomial counts")
    p = successes / trials
    z2 = z * z
    denominator = 1.0 + z2 / trials
    center = (p + z2 / (2.0 * trials)) / denominator
    radius = z * math.sqrt((p * (1.0 - p) / trials) + z2 / (4.0 * trials * trials)) / denominator
    return max(0.0, center - radius), min(1.0, center + radius)


def _shots_for_confidence(probability: float, confidence: float = 0.99) -> int | None:
    if not 0.0 <= probability <= 1.0:
        raise ValueError("probability outside [0,1]")
    if not 0.0 < confidence < 1.0:
        raise ValueError("confidence outside (0,1)")
    if probability == 0.0:
        return None
    if probability == 1.0:
        return 1
    return math.ceil(math.log1p(-confidence) / math.log1p(-probability))


def _qiskit_circuit(instance, gamma: float, beta: float, contract_id: str):
    from qiskit import qasm3

    program = qaoa_program(instance, [gamma], [beta], shots=1, contract_id=contract_id)
    lowered = IBMQuantumAdapter().lower(
        program, ExecutionRequirements(QuantumParadigm.GATE_MODEL)
    )
    return qasm3.loads(lowered.payload)


def _evaluate_counts(counts, instance, exact_optimum: float):
    optimum_hits = 0
    histogram = Counter()
    for bitstring, count in counts.items():
        clean = bitstring.replace(" ", "")
        index = int(clean, 2)
        assignment = {i: (index >> i) & 1 for i in instance.variables}
        energy = instance.energy(assignment)
        histogram[str(energy)] += int(count)
        if math.isclose(energy, exact_optimum, rel_tol=0.0, abs_tol=1e-10):
            optimum_hits += int(count)
    return optimum_hits, dict(sorted(histogram.items()))


def run(*, shots_per_seed: int = 2048, seeds: tuple[int, ...] = (2001, 2002, 2003, 2004)):
    from qiskit import transpile
    from qiskit_aer import AerSimulator
    from qiskit_ibm_runtime.fake_provider import FakeKingston

    if type(shots_per_seed) is not int or not 1 <= shots_per_seed <= 100_000:
        raise ValueError("shots_per_seed must be an integer in 1..100000")
    if not seeds or any(type(seed) is not int for seed in seeds):
        raise ValueError("at least one integer seed is required")

    instance = seeded_erdos_renyi_maxcut(6, 0.5, 42)
    contract = OptimizationBenchmarkContract("er6", "batch012-verification-fixture", 42, 6)
    sweep = compare_p1_grid_objectives(
        instance,
        alphas=(0.5,),
        gamma_steps=24,
        beta_steps=24,
        contract_id=contract.contract_id,
    )
    mean_selection, cvar_selection = sweep.selections
    exact_optimum = sweep.exact_optimum
    backend = FakeKingston()
    simulator = AerSimulator.from_backend(backend)

    results = []
    for label, selection in (("mean_energy", mean_selection), ("cvar_alpha_0.5", cvar_selection)):
        circuit = _qiskit_circuit(instance, selection.gamma, selection.beta, contract.contract_id)
        routed = transpile(circuit, backend=backend, optimization_level=2, seed_transpiler=17)
        aggregate = Counter()
        per_seed = []
        for seed in seeds:
            counts = simulator.run(routed, shots=shots_per_seed, seed_simulator=seed).result().get_counts(0)
            aggregate.update(counts)
            hits, _ = _evaluate_counts(counts, instance, exact_optimum)
            per_seed.append({"seed": seed, "shots": shots_per_seed, "optimum_hits": hits})
        total_shots = shots_per_seed * len(seeds)
        hits, histogram = _evaluate_counts(aggregate, instance, exact_optimum)
        probability = hits / total_shots
        lower, upper = _wilson_interval(hits, total_shots)
        results.append({
            "selection": label,
            "gamma": selection.gamma,
            "beta": selection.beta,
            "ideal_expected_energy": selection.expected_energy,
            "ideal_optimum_probability": selection.optimum_probability,
            "snapshot_optimum_hits": hits,
            "snapshot_total_shots": total_shots,
            "snapshot_optimum_probability": probability,
            "snapshot_probability_wilson95": [lower, upper],
            "expected_shots_per_optimum": (1.0 / probability if probability > 0 else None),
            "shots_for_99pct_at_least_one_optimum": _shots_for_confidence(probability, 0.99),
            "routed_depth": routed.depth(),
            "routed_ops": dict(routed.count_ops()),
            "per_seed": per_seed,
            "energy_histogram": histogram,
        })

    baseline, candidate = results
    bp = baseline["snapshot_optimum_probability"]
    cp = candidate["snapshot_optimum_probability"]
    return {
        "schema": "uqpu-qaoa-objective-target-comparison-v1",
        "created_utc": datetime.now(timezone.utc).isoformat(),
        "evidence_level": "CALIBRATION_SNAPSHOT_SIMULATION",
        "backend": "FakeKingston",
        "fixture": "er6",
        "contract_id": contract.contract_id,
        "shared_parameter_grid_evaluations": sweep.evaluations,
        "shots_per_seed_per_strategy": shots_per_seed,
        "simulator_seeds": list(seeds),
        "results": results,
        "comparison": {
            "cvar_minus_mean_snapshot_probability": cp - bp,
            "cvar_over_mean_snapshot_probability_ratio": (cp / bp if bp > 0 else None),
            "mean_over_cvar_expected_shot_ratio": (
                baseline["expected_shots_per_optimum"] / candidate["expected_shots_per_optimum"]
                if baseline["expected_shots_per_optimum"] and candidate["expected_shots_per_optimum"]
                else None
            ),
        },
        "environment": {
            "python": platform.python_version(),
            "platform": platform.platform(),
            "machine": platform.machine(),
        },
        "paid_job_submitted": False,
        "real_qpu_executed": False,
        "quantum_advantage_demonstrated": False,
        "limitations": [
            "FakeKingston is a saved IBM system snapshot, not current live calibration.",
            "AerSimulator.from_backend is an approximate noise model, not exact hardware behavior.",
            "The candidate angles were selected with ideal exact statevectors; hardware CVaR optimization would itself consume finite shots.",
            "The confidence intervals quantify simulator sampling noise only, not calibration/model uncertainty.",
            "No provider billing, queueing, mitigation/QEC, network, energy, GPU/CPU/NPU baseline, or real-QPU output is measured.",
        ],
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True, allow_nan=False))
