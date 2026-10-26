"""Source-bounded exact-channel evaluator for the FND-001 active-memory track.

The objective follows the memoryless-agent special case of Fiderer et al.,
Phys. Rev. X 16, 041004 (2026), Eq. (17): W = H(A) - H(S). Work rates are
normalized to k_B T ln(2) per round. This is an analytic/model calculation,
not a physical-energy or software-energy estimator.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import math
from collections.abc import Sequence
from typing import Any

_TOLERANCE = 1e-12
_SOURCE_TITLE = "Information Thermodynamics of Agents: The Work Capacity of Channels with Memory"
_SOURCE_DOI = "10.1103/7nds-tjr8"


def _distribution(name: str, values: Sequence[float]) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)) or not isinstance(values, Sequence) or not values:
        raise ValueError(f"{name} must be a nonempty probability sequence")
    parsed: list[float] = []
    for value in values:
        if isinstance(value, bool):
            raise ValueError(f"{name} entries must be finite probabilities")
        try:
            probability = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} entries must be finite probabilities") from exc
        if not math.isfinite(probability) or probability < 0.0 or probability > 1.0:
            raise ValueError(f"{name} entries must be finite probabilities in [0, 1]")
        parsed.append(probability)
    if not math.isclose(math.fsum(parsed), 1.0, rel_tol=0.0, abs_tol=_TOLERANCE):
        raise ValueError(f"{name} must sum to one within {_TOLERANCE:g}")
    return tuple(parsed)


def entropy_bits(probabilities: Sequence[float]) -> float:
    """Shannon entropy in bits for a validated finite distribution."""
    p = _distribution("probabilities", probabilities)
    return -math.fsum(value * math.log2(value) for value in p if value > 0.0)


@dataclass(frozen=True)
class ChannelWorkRate:
    action_probabilities: tuple[float, ...]
    percept_probabilities: tuple[float, ...]
    action_entropy_bits: float
    percept_entropy_bits: float
    work_rate_kbt_ln2_per_round: float


def evaluate_memoryless_invariant_channel(
    action_probabilities: Sequence[float],
    transition_by_action: Sequence[Sequence[float]],
) -> ChannelWorkRate:
    """Evaluate W = H(A)-H(S) for a memoryless invariant action-to-percept channel.

    Each row of transition_by_action is P(S | A=a), in action-alphabet order.
    The agent has a single memory state, so the conditional entropies in Eq. (17)
    reduce to ordinary Shannon entropies. No physical protocol, wall-plug energy,
    or implementation cost is inferred.
    """
    actions = _distribution("action_probabilities", action_probabilities)
    if (
        isinstance(transition_by_action, (str, bytes))
        or not isinstance(transition_by_action, Sequence)
        or len(transition_by_action) != len(actions)
    ):
        raise ValueError("transition_by_action must contain one row per action")
    rows = tuple(
        _distribution(f"transition row {index}", row)
        for index, row in enumerate(transition_by_action)
    )
    output_width = len(rows[0])
    if output_width == 0 or any(len(row) != output_width for row in rows):
        raise ValueError("all transition rows must have the same nonzero output width")

    output = _distribution(
        "percept_probabilities",
        tuple(
            math.fsum(actions[a] * rows[a][s] for a in range(len(actions)))
            for s in range(output_width)
        ),
    )
    action_entropy = entropy_bits(actions)
    percept_entropy = entropy_bits(output)
    return ChannelWorkRate(
        action_probabilities=actions,
        percept_probabilities=output,
        action_entropy_bits=action_entropy,
        percept_entropy_bits=percept_entropy,
        work_rate_kbt_ln2_per_round=action_entropy - percept_entropy,
    )


def evaluate_passive_iid_tape(
    action_probabilities: Sequence[float],
    source_probabilities: Sequence[float],
) -> ChannelWorkRate:
    """Evaluate the product/passive-tape objective H(A)-H(S).

    The source distribution is fixed independently of actions. This is a
    different environment assumption from active feedback even when its output
    marginal matches one active-channel operating point.
    """
    actions = _distribution("action_probabilities", action_probabilities)
    source = _distribution("source_probabilities", source_probabilities)
    action_entropy = entropy_bits(actions)
    source_entropy = entropy_bits(source)
    return ChannelWorkRate(
        action_probabilities=actions,
        percept_probabilities=source,
        action_entropy_bits=action_entropy,
        percept_entropy_bits=source_entropy,
        work_rate_kbt_ln2_per_round=action_entropy - source_entropy,
    )


def build_reference_report() -> dict[str, Any]:
    """Build the analytic binary-channel fixture and its passive marginal control."""
    p_action_zero = 1.0 / math.sqrt(2.0)
    active = evaluate_memoryless_invariant_channel(
        (p_action_zero, 1.0 - p_action_zero),
        (
            (1.0, 0.0),  # P(S=0|A=0)=1
            (0.5, 0.5),  # P(S=0|A=1)=P(S=1|A=1)=1/2
        ),
    )
    published_capacity = 0.5 * math.log2(0.75 + 1.0 / math.sqrt(2.0))
    passive = evaluate_passive_iid_tape(
        (0.5, 0.5),
        active.percept_probabilities,
    )
    same_marginal = all(
        math.isclose(a, b, rel_tol=0.0, abs_tol=_TOLERANCE)
        for a, b in zip(active.percept_probabilities, passive.percept_probabilities)
    )
    return {
        "schema": "uqpu-fnd001-exact-channel-reference-v1",
        "work_item_id": "FND001-ACTIVE-MEMORY-001",
        "date": "2026-10-26",
        "evidence_class": "MODEL_ONLY_ANALYTIC_REFERENCE_REPRODUCTION",
        "source": {
            "title": _SOURCE_TITLE,
            "publication": "Physical Review X 16, 041004",
            "published": "2026-10-05",
            "doi": _SOURCE_DOI,
            "equation": "Eq. (17), memoryless-agent special case; binary channel in Eq. (22) and capacity in Eq. (23)",
        },
        "units": "normalized work capacity in k_B T ln(2) per round; not joules",
        "active_feedback": {
            **asdict(active),
            "published_analytic_capacity_kbt_ln2_per_round": published_capacity,
            "absolute_reference_error": abs(
                active.work_rate_kbt_ln2_per_round - published_capacity
            ),
            "tolerance": _TOLERANCE,
        },
        "passive_iid_tape_control": {
            **asdict(passive),
            "capacity_for_this_iid_source_kbt_ln2_per_round": math.log2(2.0)
            - entropy_bits(active.percept_probabilities),
            "same_output_marginal_as_active_operating_point": same_marginal,
        },
        "comparison": {
            "passive_minus_active_normalized_work_rate": (
                passive.work_rate_kbt_ln2_per_round
                - active.work_rate_kbt_ln2_per_round
            ),
            "interpretation": (
                "A mathematical contrast between different environment assumptions; "
                "not a matched physical implementation, accepted-task benefit, or energy saving."
            ),
        },
        "validation": {
            "active_channel_matches_published_analytic_reference": math.isclose(
                active.work_rate_kbt_ln2_per_round,
                published_capacity,
                rel_tol=0.0,
                abs_tol=_TOLERANCE,
            ),
            "passive_control_uses_fixed_action_independent_source": True,
            "output_marginals_match_at_the_selected_operating_point": same_marginal,
            "physical_memory_bytes": None,
            "measured_energy_joules": None,
            "measured_cost_usd": None,
            "provider_jobs": 0,
            "qpu_shots": 0,
            "physical_experiments": 0,
            "accepted_useful_task_comparison": False,
        },
        "claims_promoted": [],
        "non_claims": [
            "physical work extraction measured by UQPU",
            "software or hardware energy advantage",
            "predictive-versus-bounded-memory policy ranking",
            "real-QPU advantage",
            "new physical law",
            "material substitution, saleable bio-oil, fusion net electricity, financing-rate change",
            "Data-Center-to-One-Phone or 100,000,000x achievement",
        ],
        "next_gate": (
            "Extend to a finite-state memoryful agent/environment with frozen transition "
            "matrices; independently check the stationary/asymptotic objective; then run "
            "held-out policy comparisons and preserve null/counterexample cases."
        ),
    }


if __name__ == "__main__":
    print(json.dumps(build_reference_report(), indent=2, sort_keys=True))
