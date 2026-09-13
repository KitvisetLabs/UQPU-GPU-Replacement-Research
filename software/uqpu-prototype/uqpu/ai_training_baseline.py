"""Reproducible classical AI-training baseline for AI-COST-002.

Evidence level: executable classical software baseline + analytic resource ledger.
This module does not establish quantum advantage, real-QPU AI training, or any
moonshot cost reduction.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import math
import random
import statistics
import time

RESEARCH_ATTRIBUTION = {
    "research_owner_principal_investigator_research_direction": "Kanutsanan Pongpanna",
    "facebook": "https://www.facebook.com/LoveMoneyTH",
    "youtube": "https://www.youtube.com/@LoveMoneyTHOfficial",
    "ai_research_agent": "OpenAI GPT-5.6 Sol",
    "ai_assisted_contribution": (
        "classical baseline design, exact resource-ledger derivation, executable "
        "implementation, tests, reference measurement and research documentation"
    ),
}


@dataclass(frozen=True)
class BaselineConfig:
    train_examples: int = 256
    test_examples: int = 256
    hidden_width: int = 16
    epochs: int = 800
    learning_rate: float = 0.2
    seed: int = 1234
    scalar_bytes: int = 8


@dataclass(frozen=True)
class CostScenario:
    host_power_w: float = 65.0
    electricity_usd_per_kwh: float = 0.10
    host_capex_usd: float = 500.0
    host_lifetime_years: float = 3.0
    utilization_fraction: float = 0.5


def _dataset(n: int, seed: int) -> list[tuple[float, float, float]]:
    rng = random.Random(seed)
    rows: list[tuple[float, float, float]] = []
    for _ in range(n):
        x1 = rng.uniform(-1.0, 1.0)
        x2 = rng.uniform(-1.0, 1.0)
        y = 1.0 if x1 * x2 >= 0.0 else 0.0
        rows.append((x1, x2, y))
    return rows


def parameter_count(config: BaselineConfig) -> int:
    # W1: 2H, b1: H, W2: H, b2: 1 -> 4H+1.
    return 4 * config.hidden_width + 1


def exact_training_operation_ledger(config: BaselineConfig) -> dict[str, int]:
    """Count scalar arithmetic/nonlinear operations for this exact implementation.

    Counts are source-level algorithmic operations, not ISA instructions/FLOPs.
    tanh/exp/div are reported separately rather than converted to FLOP equivalents.
    """
    h = config.hidden_width
    samples = config.train_examples * config.epochs

    # Per training sample:
    # forward: hidden = 2H mul + 2H add + H tanh
    # output = H mul + H add + one sigmoid (1 add, 1 div, 1 exp)
    # dz = p-y -> 1 add/sub
    # backward per hidden unit = 6 mul + 5 add
    per_sample_mul = 9 * h
    per_sample_add = 8 * h + 2
    per_sample_tanh = h
    per_sample_exp = 1
    per_sample_div = 1

    # Full-batch SGD update per epoch: per hidden unit 8 mul + 4 add,
    # plus output bias 2 mul + 1 add.
    per_epoch_update_mul = 8 * h + 2
    per_epoch_update_add = 4 * h + 1

    return {
        "training_samples_processed": samples,
        "multiply": samples * per_sample_mul + config.epochs * per_epoch_update_mul,
        "add_subtract": samples * per_sample_add + config.epochs * per_epoch_update_add,
        "tanh": samples * per_sample_tanh,
        "exp": samples * per_sample_exp,
        "division": samples * per_sample_div,
    }


def tensor_payload_ledger(config: BaselineConfig) -> dict[str, int]:
    """Return machine-independent dense FP64 payload and minimum traffic proxies.

    These are logical tensor payload bytes, not Python process RSS and not DRAM/HBM
    measurements. They are intended to freeze a comparison contract for later
    quantum/hybrid routes.
    """
    params = parameter_count(config)
    b = config.scalar_bytes
    dataset_bytes = config.train_examples * 3 * b
    parameter_bytes = params * b
    gradient_bytes = parameter_bytes
    activation_stream_bytes = (config.hidden_width + 1) * b
    minimum_dataset_read_bytes = dataset_bytes * config.epochs
    # Lower-bound-ish optimizer traffic proxy: one read and one write per parameter
    # per epoch, excluding cache effects and interpreter/object overhead.
    optimizer_parameter_traffic_bytes = parameter_bytes * 2 * config.epochs
    return {
        "parameter_payload_bytes": parameter_bytes,
        "gradient_payload_bytes": gradient_bytes,
        "train_dataset_payload_bytes": dataset_bytes,
        "streaming_activation_payload_bytes_per_example": activation_stream_bytes,
        "logical_peak_payload_bytes_streaming": (
            parameter_bytes + gradient_bytes + dataset_bytes + activation_stream_bytes
        ),
        "minimum_dataset_read_bytes_over_training": minimum_dataset_read_bytes,
        "optimizer_parameter_traffic_bytes": optimizer_parameter_traffic_bytes,
    }


def _initial_parameters(config: BaselineConfig) -> tuple[list[list[float]], list[float], list[float], float]:
    rng = random.Random(config.seed)
    w1 = [[rng.uniform(-0.5, 0.5) for _ in range(2)] for _ in range(config.hidden_width)]
    b1 = [0.0] * config.hidden_width
    w2 = [rng.uniform(-0.5, 0.5) for _ in range(config.hidden_width)]
    return w1, b1, w2, 0.0


def _evaluate(
    data: list[tuple[float, float, float]],
    w1: list[list[float]],
    b1: list[float],
    w2: list[float],
    b2: float,
) -> dict[str, float]:
    correct = 0
    loss = 0.0
    for x1, x2, y in data:
        hidden = [math.tanh(w1[j][0] * x1 + w1[j][1] * x2 + b1[j]) for j in range(len(w2))]
        z = sum(w2[j] * hidden[j] for j in range(len(w2))) + b2
        p = 1.0 / (1.0 + math.exp(-z))
        correct += int((p >= 0.5) == (y >= 0.5))
        p_clip = min(max(p, 1e-15), 1.0 - 1e-15)
        loss += -(y * math.log(p_clip) + (1.0 - y) * math.log(1.0 - p_clip))
    return {"accuracy": correct / len(data), "binary_cross_entropy": loss / len(data)}


def train_baseline(config: BaselineConfig = BaselineConfig()) -> dict:
    """Train the deterministic 2-H-1 MLP and return accepted-capability metrics."""
    train = _dataset(config.train_examples, config.seed + 1)
    test = _dataset(config.test_examples, config.seed + 2)
    w1, b1, w2, b2 = _initial_parameters(config)

    started = time.perf_counter()
    for _ in range(config.epochs):
        gw1 = [[0.0, 0.0] for _ in range(config.hidden_width)]
        gb1 = [0.0] * config.hidden_width
        gw2 = [0.0] * config.hidden_width
        gb2 = 0.0

        for x1, x2, y in train:
            hidden = [
                math.tanh(w1[j][0] * x1 + w1[j][1] * x2 + b1[j])
                for j in range(config.hidden_width)
            ]
            z = sum(w2[j] * hidden[j] for j in range(config.hidden_width)) + b2
            p = 1.0 / (1.0 + math.exp(-z))
            dz = p - y
            for j in range(config.hidden_width):
                gw2[j] += dz * hidden[j]
                dh = dz * w2[j] * (1.0 - hidden[j] * hidden[j])
                gw1[j][0] += dh * x1
                gw1[j][1] += dh * x2
                gb1[j] += dh
            gb2 += dz

        inv_n = 1.0 / config.train_examples
        for j in range(config.hidden_width):
            w2[j] -= config.learning_rate * gw2[j] * inv_n
            w1[j][0] -= config.learning_rate * gw1[j][0] * inv_n
            w1[j][1] -= config.learning_rate * gw1[j][1] * inv_n
            b1[j] -= config.learning_rate * gb1[j] * inv_n
        b2 -= config.learning_rate * gb2 * inv_n

    elapsed_s = time.perf_counter() - started
    return {
        "config": asdict(config),
        "parameter_count": parameter_count(config),
        "train_metrics": _evaluate(train, w1, b1, w2, b2),
        "test_metrics": _evaluate(test, w1, b1, w2, b2),
        "measured_training_wall_seconds": elapsed_s,
        "operation_ledger": exact_training_operation_ledger(config),
        "tensor_payload_ledger": tensor_payload_ledger(config),
    }


def cost_from_runtime(runtime_seconds: float, scenario: CostScenario = CostScenario()) -> dict[str, float]:
    """Map a measured runtime into an explicit scenario cost model.

    Power and monetary inputs are assumptions unless independently measured.
    The output must therefore be labeled MODELLED_SCENARIO_COST, not measured TCO.
    """
    if runtime_seconds <= 0:
        raise ValueError("runtime_seconds must be positive")
    if scenario.host_power_w <= 0 or scenario.electricity_usd_per_kwh < 0:
        raise ValueError("power must be positive and electricity price non-negative")
    if scenario.host_capex_usd < 0 or scenario.host_lifetime_years <= 0:
        raise ValueError("invalid host capital/lifetime assumptions")
    if not 0 < scenario.utilization_fraction <= 1:
        raise ValueError("utilization_fraction must be in (0, 1]")

    energy_kwh = scenario.host_power_w * runtime_seconds / 3_600_000.0
    electricity_cost = energy_kwh * scenario.electricity_usd_per_kwh
    amortized_usd_per_hour = scenario.host_capex_usd / (
        scenario.host_lifetime_years * 365.0 * 24.0 * scenario.utilization_fraction
    )
    amortized_compute_cost = amortized_usd_per_hour * runtime_seconds / 3600.0
    return {
        "energy_kwh_model": energy_kwh,
        "electricity_cost_usd_model": electricity_cost,
        "host_amortization_usd_per_hour_model": amortized_usd_per_hour,
        "host_amortization_cost_usd_model": amortized_compute_cost,
        "electricity_plus_host_amortization_usd_model": electricity_cost + amortized_compute_cost,
    }


def median_reference_run(repetitions: int = 3, config: BaselineConfig = BaselineConfig()) -> dict:
    """Execute repeated training and report median runtime plus deterministic metrics."""
    if repetitions < 1:
        raise ValueError("repetitions must be at least 1")
    runs = [train_baseline(config) for _ in range(repetitions)]
    runtimes = [run["measured_training_wall_seconds"] for run in runs]
    result = dict(runs[0])
    result["measured_training_wall_seconds"] = statistics.median(runtimes)
    result["runtime_repetitions"] = repetitions
    result["runtime_samples_seconds"] = runtimes
    return result
