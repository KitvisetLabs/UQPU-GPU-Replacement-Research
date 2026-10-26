"""Reproduce frozen FND-001 finite-state held-out experiment (MODEL_ONLY)."""
import json
import math
import random
from pathlib import Path

from uqpu.finite_state_memory import evaluate_finite_state_channel, policy_fixtures

HELD_OUT = (0.65, 0.75, 0.85, 0.95)
BURN_IN = 10_000
SAMPLES = 250_000
BASE_SEED = 20261026


def entropy(counts):
    total = sum(counts)
    if total == 0:
        return 0.0
    return -sum((n / total) * math.log2(n / total) for n in counts if n)


def simulate(spec, seed):
    rng = random.Random(seed)
    policy, update, env = spec["policy"], spec["memory_update"], spec["environment_transition"]
    m = s = 0
    m_counts = [0] * len(policy)
    a_counts = [[0] * len(policy[0][0]) for _ in policy]
    s_counts = [[0] * len(env) for _ in policy]
    for t in range(BURN_IN + SAMPLES):
        probs = policy[m][s]
        u = rng.random()
        cum = 0.0
        a = len(probs) - 1
        for i, p in enumerate(probs):
            cum += p
            if u < cum:
                a = i
                break
        m_next_probs = update[m][s][a]
        u = rng.random()
        cum = 0.0
        m_next = len(m_next_probs) - 1
        for i, p in enumerate(m_next_probs):
            cum += p
            if u < cum:
                m_next = i
                break
        s_next_probs = env[s][a]
        u = rng.random()
        cum = 0.0
        s_next = len(s_next_probs) - 1
        for i, p in enumerate(s_next_probs):
            cum += p
            if u < cum:
                s_next = i
                break
        if t >= BURN_IN:
            m_counts[m] += 1
            a_counts[m][a] += 1
            s_counts[m][s] += 1
        m, s = m_next, s_next
    total = sum(m_counts)
    h_a_m = h_s_m = 0.0
    for m_idx, n_m in enumerate(m_counts):
        if n_m:
            h_a_m += (n_m / total) * entropy(a_counts[m_idx])
            h_s_m += (n_m / total) * entropy(s_counts[m_idx])
    return {
        "samples": SAMPLES,
        "burn_in": BURN_IN,
        "seed": seed,
        "h_action_given_memory_bits": h_a_m,
        "h_percept_given_memory_bits": h_s_m,
        "work_rate_kbt_ln2_per_round": h_a_m - h_s_m,
    }


def main():
    rows = []
    for pi, p in enumerate(HELD_OUT):
        for qi, (name, spec) in enumerate(policy_fixtures(p).items()):
            exact = evaluate_finite_state_channel(**spec)
            mc = simulate(spec, BASE_SEED + 100 * pi + qi)
            error = mc["work_rate_kbt_ln2_per_round"] - exact.work_rate_kbt_ln2_per_round
            rows.append({
                "p_stay_action0": p,
                "policy": name,
                "exact": {
                    "h_action_given_memory_bits": exact.h_action_given_memory_bits,
                    "h_percept_given_memory_bits": exact.h_percept_given_memory_bits,
                    "work_rate_kbt_ln2_per_round": exact.work_rate_kbt_ln2_per_round,
                    "stationary_residual": exact.stationary_residual,
                },
                "monte_carlo": mc,
                "mc_minus_exact_bits_per_round": error,
                "mc_check_pass": abs(error) <= 0.02,
            })
    report = {
        "date": "2026-10-26",
        "evidence_class": "MODEL_ONLY_FINITE_STATE_STATIONARY_ANALYSIS",
        "protocol": "research_lanes/F_economics_benchmarks_evidence_integration/FND001_FINITE_STATE_POLICY_PREREGISTRATION_2026-10-26.md",
        "source": "Fiderer et al., Phys. Rev. X 16, 041004 (2026-10-05), DOI 10.1103/7nds-tjr8",
        "training_p": 0.80,
        "held_out_p": list(HELD_OUT),
        "fixed_q": 0.70,
        "physical_memory_bytes": None,
        "measured_energy_joules": None,
        "accepted_useful_task_quality": None,
        "measured_cost_usd": None,
        "paid_qpu_jobs": 0,
        "rows": rows,
        "all_mc_checks_pass": all(row["mc_check_pass"] for row in rows),
    }
    path = Path(__file__).resolve().parents[1] / "results" / "fnd001_finite_state_heldout_2026-10-26.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(path),
        "all_mc_checks_pass": report["all_mc_checks_pass"],
        "rows": [{
            "p": row["p_stay_action0"],
            "policy": row["policy"],
            "exact_W": round(row["exact"]["work_rate_kbt_ln2_per_round"], 9),
            "mc_W": round(row["monte_carlo"]["work_rate_kbt_ln2_per_round"], 9),
            "error": round(row["mc_minus_exact_bits_per_round"], 9),
            "pass": row["mc_check_pass"],
        } for row in rows],
    }, indent=2))


if __name__ == "__main__":
    main()
