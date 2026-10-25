"""Repeated-seed synthetic calibration for the FND-001 CMI estimator.

Run with: python -m uqpu.fnd001_cmi_bias_calibration
The output is MODEL_ONLY and is not a thermodynamic measurement.
"""
from __future__ import annotations

import argparse
import json
import math
import random
import statistics
from collections.abc import Sequence

from uqpu.thermodynamic_memory_order import adjacent_lag_cmi_profile_bits


def _first_order_binary_chain(seed: int, length: int, stay_probability: float = 0.9) -> list[int]:
    rng = random.Random(seed)
    values = [rng.randrange(2)]
    for _ in range(1, length):
        previous = values[-1]
        values.append(previous if rng.random() < stay_probability else 1 - previous)
    return values


def _second_order_xor_chain(seed: int, length: int, flip_probability: float = 0.03) -> list[int]:
    rng = random.Random(seed)
    values = [rng.randrange(2), rng.randrange(2)]
    for _ in range(2, length):
        prediction = values[-1] ^ values[-2]
        values.append(prediction ^ int(rng.random() < flip_probability))
    return values


def _binary_entropy_bits(probability: float) -> float:
    if not 0.0 < probability < 1.0:
        return 0.0
    return -(probability * math.log2(probability) + (1.0 - probability) * math.log2(1.0 - probability))


def run_calibration(lengths: Sequence[int] = (500, 2000, 10000), replicates: int = 30) -> dict[str, object]:
    """Return deterministic finite-sample summaries for two known-truth processes."""
    length_values = tuple(lengths)
    if not length_values or any(not isinstance(n, int) or isinstance(n, bool) or n < 4 for n in length_values):
        raise ValueError("lengths must be a nonempty sequence of integers >= 4")
    if len(set(length_values)) != len(length_values):
        raise ValueError("lengths must not contain duplicates")
    if not isinstance(replicates, int) or isinstance(replicates, bool) or replicates < 2:
        raise ValueError("replicates must be an integer >= 2")

    truth = {
        "first_order": {0: 1.0 - _binary_entropy_bits(0.1), 1: 0.0, 2: 0.0},
        "second_order_xor": {0: 0.0, 1: 1.0 - _binary_entropy_bits(0.03), 2: 0.0},
    }
    families = (("first_order", 40000, _first_order_binary_chain), ("second_order_xor", 50000, _second_order_xor_chain))
    results: list[dict[str, object]] = []
    for family, seed_base, generator in families:
        for length in length_values:
            values_by_order = {0: [], 1: [], 2: []}
            for replicate_index in range(replicates):
                seed = seed_base + length * 10 + replicate_index
                profile = adjacent_lag_cmi_profile_bits(generator(seed, length), max_order=2)
                for order, estimate in profile.items():
                    values_by_order[order].append(estimate)
            for order, estimates in values_by_order.items():
                ordered = sorted(estimates)
                mean_value = statistics.mean(estimates)
                results.append({
                    "family": family,
                    "length": length,
                    "replicates": replicates,
                    "conditioning_order": order,
                    "analytic_truth_bits": truth[family][order],
                    "mean_bits": mean_value,
                    "mean_bias_bits": mean_value - truth[family][order],
                    "sample_sd_bits": statistics.stdev(estimates),
                    "p95_empirical_nearest_rank_bits": ordered[math.ceil(0.95 * replicates) - 1],
                })
    return {
        "schema": "uqpu-fnd001-cmi-bias-calibration-v1",
        "date": "2026-10-25",
        "evidence_class": ["MODEL_ONLY", "SYNTHETIC_KNOWN_TRUTH", "REPEATED_SEED_CALIBRATION"],
        "method": {
            "statistic": "plug-in adjacent-lag conditional mutual information in bits",
            "replicates_per_family_length": replicates,
            "lengths": list(length_values),
            "orders": [0, 1, 2],
            "seed_rule": "first_order seed=40000+length*10+replicate_index; second_order_xor seed=50000+length*10+replicate_index; replicate_index starts at 0",
            "p95": "empirical nearest-rank 95th percentile over replicates; not a confidence interval",
            "sample_sd": "sample standard deviation across independent seeded replicates",
        },
        "families": {
            "first_order": {"generator": "binary Markov chain with P(stay)=0.9", "analytic_true_cmi_bits": {str(k): v for k, v in truth["first_order"].items()}},
            "second_order_xor": {"generator": "X_t=X_(t-1) XOR X_(t-2) XOR Bernoulli(0.03)", "analytic_true_cmi_bits": {str(k): v for k, v in truth["second_order_xor"].items()}},
        },
        "results": results,
        "limitations": [
            "Only two synthetic binary generators and three default sample lengths are covered.",
            "The plug-in CMI estimator has finite-sample bias, especially when conditioning contexts are sparse.",
            "The empirical percentile from 30 replicates is descriptive and is not a calibrated decision threshold.",
            "No thermodynamic entropy production, heat, wall-plug energy, real data or physical-system parameter was measured.",
            "Do not infer Markov order without preregistered thresholds, broader null families, dependence-aware uncertainty and independent validation.",
        ],
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lengths", nargs="+", type=int, default=[500, 2000, 10000])
    parser.add_argument("--replicates", type=int, default=30)
    args = parser.parse_args()
    print(json.dumps(run_calibration(args.lengths, args.replicates), indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
