"""SCM-GATE-001 synthetic multimodal null-characterization helpers.

This module does not model spirits or cross-realm physics. It generates ordinary
sensor noise plus known injected interference so the SCM program can quantify
false-positive behavior before any anomalous-source experiment.
"""

from __future__ import annotations

from dataclasses import dataclass
import math
import random
from typing import Iterable


@dataclass(frozen=True)
class SensorChannel:
    name: str
    noise_sigma: float
    interference_gain: float = 1.0


@dataclass(frozen=True)
class NullRunSummary:
    samples: int
    channels: int
    threshold_sigma: float
    channel_exceedances: int
    coincidence_exceedances: int
    injected_events: int
    evidence_class: str = "MODEL_ONLY_SYNTHETIC_CONTROL"


def _z(value: float, sigma: float) -> float:
    if sigma <= 0:
        raise ValueError("noise_sigma must be positive")
    return abs(value) / sigma


def simulate_null_run(
    channels: Iterable[SensorChannel],
    *,
    samples: int = 10_000,
    threshold_sigma: float = 4.0,
    coincidence_channels: int = 2,
    interference_probability: float = 0.001,
    interference_sigma: float = 8.0,
    seed: int = 20260927,
) -> NullRunSummary:
    """Generate a deterministic synthetic ordinary-cause control run.

    A common-mode interference event represents mundane contamination that can
    trigger multiple sensors simultaneously. This deliberately demonstrates why
    coincidence alone is not evidence of a nonordinary source.
    """
    ch = tuple(channels)
    if not ch:
        raise ValueError("at least one channel is required")
    if samples <= 0:
        raise ValueError("samples must be positive")
    if threshold_sigma <= 0:
        raise ValueError("threshold_sigma must be positive")
    if not 1 <= coincidence_channels <= len(ch):
        raise ValueError("coincidence_channels out of range")
    if not 0.0 <= interference_probability <= 1.0:
        raise ValueError("interference_probability must be in [0, 1]")

    rng = random.Random(seed)
    channel_exceedances = 0
    coincidence_exceedances = 0
    injected_events = 0

    for _ in range(samples):
        injected = rng.random() < interference_probability
        common = rng.gauss(0.0, interference_sigma) if injected else 0.0
        injected_events += int(injected)

        hits = 0
        for sensor in ch:
            value = rng.gauss(0.0, sensor.noise_sigma)
            if injected:
                value += common * sensor.noise_sigma * sensor.interference_gain
            if _z(value, sensor.noise_sigma) >= threshold_sigma:
                channel_exceedances += 1
                hits += 1
        if hits >= coincidence_channels:
            coincidence_exceedances += 1

    return NullRunSummary(
        samples=samples,
        channels=len(ch),
        threshold_sigma=threshold_sigma,
        channel_exceedances=channel_exceedances,
        coincidence_exceedances=coincidence_exceedances,
        injected_events=injected_events,
    )


def gaussian_two_sided_tail(threshold_sigma: float) -> float:
    """Ideal two-sided Gaussian tail probability for a single independent channel."""
    if threshold_sigma < 0:
        raise ValueError("threshold_sigma must be non-negative")
    return math.erfc(threshold_sigma / math.sqrt(2.0))


DEFAULT_CHANNELS = (
    SensorChannel("magnetic", 1.0, 1.0),
    SensorChannel("rf", 1.0, 1.2),
    SensorChannel("acoustic", 1.0, 0.7),
    SensorChannel("thermal", 1.0, 0.3),
    SensorChannel("vibration", 1.0, 0.8),
    SensorChannel("optical", 1.0, 0.2),
)
