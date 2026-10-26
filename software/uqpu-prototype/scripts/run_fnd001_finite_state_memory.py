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
    return h_a_m, h_s_m, h_a_m - h_s_m


def main():
    rows = []
    for pi, p in enumerate(HELD_OUT):
        for qi, (name, spec) in enumerate(policy_fixtures(p).items()):
            exact = evaluate_finite_state_channel(**spec)
            mc_a, mc_s, mc_w = simulate(spec, BASE_SEED + 100 * pi + qi)
            exact_w = exact.work_rate_kbt_ln2_per_round
            error = mc_w - exact_w
            rows.append({
                "p_stay_action0": p,
                "policy": name,
                "h_action_given_memory_bits": exact.h_action_given_memory_bits,
                "h_percept_given_memory_bits": exact.h_percept_given_memory_bits,
                "exact_work_rate_kbt_ln2_per_round": exact_w,
                "monte_carlo_work_rate_kbt_ln2_per_round": mc_w,
                "mc_minus_exact_bits_per_round": error,
                "stationary_residual": exact.stationary_residual,
                "mc_check_pass": abs(error) <= 0.02,
            })
    report = {
        "date": "2026-10-26",
        "evidence_class": "MODEL_ONLY_FINITE_STATE_STATIONARY_ANALYSIS",
        "source": {
            "title": "Information Thermodynamics of Agents: The Work Capacity of Channels with Memory",
            "authors": "Lukas J. Fiderer, Paul C. Barth, Isaac D. Smith, Hans J. Briegel",
            "journal": "Physical Review X 16, 041004",
            "published": "2026-10-05",
            "doi": "10.1103/7nds-tjr8",
        },
        "preregistration": "research_lanes/F_economics_benchmarks_evidence_integration/FND001_FINITE_STATE_POLICY_PREREGISTRATION_2026-10-26.md",
        "training_p": 0.80,
        "held_out_p": list(HELD_OUT),
        "fixed_q": 0.70,
        "monte_carlo": {
            "burn_in": BURN_IN,
            "samples_per_policy_parameter": SAMPLES,
            "base_seed": BASE_SEED,
            "acceptance_tolerance_bits_per_round": 0.02,
            "all_12_checks_pass": all(row["mc_check_pass"] for row in rows),
        },
        "results": rows,
        "conclusion": {
            "objective_ranking": "PREDICTIVE (0) > MEMORYLESS (negative) > BOUNDED_MEMORY (more negative) at all four frozen held-out points",
            "falsification_note": "No ranking reversal appeared in this selected toy family; that is not evidence of a universal ordering.",
            "limitations": [
                "Toy controlled Markov channel only",
                "No matched useful-task semantics or quality gate",
                "No physical memory bytes or implementation energy",
                "No device, real-QPU, accepted-task cost, or commercial claim",
            ],
            "physical_memory_bytes": None,
            "measured_energy_joules": None,
            "accepted_useful_task_quality": None,
            "measured_cost_usd": None,
            "paid_qpu_jobs": 0,
        },
    }
    path = Path(__file__).resolve().parents[1] / "results" / "fnd001_finite_state_heldout_2026-10-26.json"
    path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "output": str(path),
        "all_mc_checks_pass": report["monte_carlo"]["all_12_checks_pass"],
        "rows": [{
            "p": row["p_stay_action0"],
            "policy": row["policy"],
            "exact_W": round(row["exact_work_rate_kbt_ln2_per_round"], 9),
            "mc_W": round(row["monte_carlo_work_rate_kbt_ln2_per_round"], 9),
            "error": round(row["mc_minus_exact_bits_per_round"], 9),
            "pass": row["mc_check_pass"],
        } for row in rows],
    }, indent=2))


if __name__ == "__main__":
    main()
