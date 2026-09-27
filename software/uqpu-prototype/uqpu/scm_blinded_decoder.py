"""SCM-GATE-002 blinded-decoder / pareidolia benchmark.

This module measures how often a decoder can appear to identify a target when
the evaluated sample contains no target information. It is a control tool, not
a detector of spirits, consciousness, or cross-realm communication.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import math
import random
from typing import Iterable, Sequence


@dataclass(frozen=True)
class BlindedTrial:
    trial_id: str
    hidden_target: str
    decoder_response: str
    primed: bool = False


@dataclass(frozen=True)
class DecoderSummary:
    trials: int
    labels: int
    exact_hits: int
    hit_rate: float
    chance_rate: float
    excess_over_chance: float
    z_score_vs_chance: float
    evidence_class: str = "MODEL_ONLY_BLINDED_CONTROL"


def commitment(value: str, salt: str) -> str:
    """Timestamping belongs outside this helper; this provides content commitment."""
    return hashlib.sha256((salt + "\x00" + value).encode("utf-8")).hexdigest()


def score_trials(trials: Iterable[BlindedTrial], labels: Sequence[str]) -> DecoderSummary:
    trials = tuple(trials)
    labels = tuple(labels)
    if not trials:
        raise ValueError("at least one trial is required")
    if len(labels) < 2 or len(set(labels)) != len(labels):
        raise ValueError("labels must contain at least two unique values")
    allowed = set(labels)
    if any(t.hidden_target not in allowed or t.decoder_response not in allowed for t in trials):
        raise ValueError("trial labels must belong to the declared label set")

    n = len(trials)
    hits = sum(t.hidden_target == t.decoder_response for t in trials)
    p0 = 1.0 / len(labels)
    rate = hits / n
    variance = n * p0 * (1.0 - p0)
    z = (hits - n * p0) / math.sqrt(variance)
    return DecoderSummary(
        trials=n,
        labels=len(labels),
        exact_hits=hits,
        hit_rate=rate,
        chance_rate=p0,
        excess_over_chance=rate - p0,
        z_score_vs_chance=z,
    )


def simulate_noise_decoder(
    labels: Sequence[str],
    *,
    trials: int = 1000,
    priming_strength: float = 0.0,
    seed: int = 20260928,
) -> tuple[BlindedTrial, ...]:
    """Generate null trials with no information path from target to response.

    priming_strength biases responses toward label[0] but hidden targets remain
    independent. This models expectation/response bias without creating a real
    information channel.
    """
    labels = tuple(labels)
    if len(labels) < 2 or len(set(labels)) != len(labels):
        raise ValueError("labels must contain at least two unique values")
    if trials <= 0:
        raise ValueError("trials must be positive")
    if not 0.0 <= priming_strength <= 1.0:
        raise ValueError("priming_strength must be in [0, 1]")

    rng = random.Random(seed)
    out = []
    for i in range(trials):
        target = rng.choice(labels)
        primed = rng.random() < priming_strength
        response = labels[0] if primed else rng.choice(labels)
        out.append(BlindedTrial(f"null-{i:06d}", target, response, primed))
    return tuple(out)
