"""SCM-GATE-003 prospective cryptographic challenge-response protocol.

This module supplies protocol mechanics for testing source-dependent information.
It does not assume or identify a spiritual, post-mortem, or cross-realm source.
"""

from __future__ import annotations

from dataclasses import dataclass
import hashlib
import hmac
import math
import secrets
from typing import Sequence


@dataclass(frozen=True)
class ChallengeCommitment:
    trial_id: str
    target_commitment: str
    scoring_commitment: str


@dataclass(frozen=True)
class FrozenResponse:
    trial_id: str
    response: str
    response_commitment: str


@dataclass(frozen=True)
class RevealedTrial:
    trial_id: str
    target: str
    target_salt: str
    scoring_rule: str
    scoring_salt: str
    response: str
    response_salt: str


@dataclass(frozen=True)
class ChallengeScore:
    trials: int
    labels: int
    exact_hits: int
    hit_rate: float
    chance_rate: float
    verified_bits: float
    evidence_class: str = "PROTOCOL_ONLY_NO_SOURCE_CLAIM"


def _digest(value: str, salt: str) -> str:
    return hashlib.sha256((salt + "\x00" + value).encode("utf-8")).hexdigest()


def new_salt(bytes_: int = 32) -> str:
    if bytes_ < 16:
        raise ValueError("salt must contain at least 128 bits")
    return secrets.token_hex(bytes_)


def commit_challenge(
    trial_id: str,
    target: str,
    target_salt: str,
    scoring_rule: str,
    scoring_salt: str,
) -> ChallengeCommitment:
    if not trial_id or not target or not scoring_rule:
        raise ValueError("trial_id, target and scoring_rule are required")
    return ChallengeCommitment(
        trial_id,
        _digest(target, target_salt),
        _digest(scoring_rule, scoring_salt),
    )


def freeze_response(trial_id: str, response: str, response_salt: str) -> FrozenResponse:
    if not trial_id or not response:
        raise ValueError("trial_id and response are required")
    return FrozenResponse(trial_id, response, _digest(response, response_salt))


def verify_reveal(
    committed: ChallengeCommitment,
    frozen: FrozenResponse,
    revealed: RevealedTrial,
) -> bool:
    if not (committed.trial_id == frozen.trial_id == revealed.trial_id):
        return False
    checks = (
        hmac.compare_digest(committed.target_commitment, _digest(revealed.target, revealed.target_salt)),
        hmac.compare_digest(committed.scoring_commitment, _digest(revealed.scoring_rule, revealed.scoring_salt)),
        hmac.compare_digest(frozen.response_commitment, _digest(revealed.response, revealed.response_salt)),
    )
    return all(checks)


def score_exact_trials(trials: Sequence[RevealedTrial], labels: Sequence[str]) -> ChallengeScore:
    labels = tuple(labels)
    if len(labels) < 2 or len(set(labels)) != len(labels):
        raise ValueError("labels must contain at least two unique values")
    if not trials:
        raise ValueError("at least one trial is required")
    allowed = set(labels)
    if any(t.target not in allowed or t.response not in allowed for t in trials):
        raise ValueError("target/response outside declared labels")
    if any(t.scoring_rule != "exact-match-v1" for t in trials):
        raise ValueError("unsupported or non-precommitted scoring rule")

    n = len(trials)
    hits = sum(t.target == t.response for t in trials)
    p0 = 1.0 / len(labels)
    # Conservative descriptive information credit: only excess exact hits above
    # chance earn bits; this is not a significance test or source identifier.
    excess_hits = max(0.0, hits - n * p0)
    verified_bits = excess_hits * math.log2(len(labels))
    return ChallengeScore(n, len(labels), hits, hits / n, p0, verified_bits)
