"""Exact-rational fixture for the ancilla-QFI score-class dimension condition.

Scope is deliberately narrow: a finite, strictly positive classical outcome
distribution in an already-optimal projective measurement, with local
probability derivatives and parameter-independent conditional ancilla states.
This module is a theorem-scope audit helper, not a general QFI solver, circuit
simulator, physical-law validator, or hardware claim.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from typing import Any, Iterable


def _exact_fraction(value: Fraction | int, label: str) -> Fraction:
    """Accept exact rational inputs only; never merge scores by float tolerance."""
    if isinstance(value, Fraction):
        return value
    if isinstance(value, int) and not isinstance(value, bool):
        return Fraction(value)
    raise TypeError(f"{label} must use Fraction or int, not floating-point input")


@dataclass(frozen=True)
class AncillaQfiCase:
    case_id: str
    probabilities: tuple[Fraction, ...]
    derivatives: tuple[Fraction, ...]
    ancilla_dimension: int

    def analyze(self) -> dict[str, Any]:
        if not isinstance(self.case_id, str) or not self.case_id.strip():
            raise ValueError("case_id must be non-empty")
        if not self.probabilities or len(self.probabilities) != len(self.derivatives):
            raise ValueError("probabilities and derivatives must have equal non-zero length")
        if (
            isinstance(self.ancilla_dimension, bool)
            or not isinstance(self.ancilla_dimension, int)
            or self.ancilla_dimension < 1
        ):
            raise ValueError("ancilla_dimension must be a positive integer")

        probabilities = tuple(
            _exact_fraction(value, "probability") for value in self.probabilities
        )
        derivatives = tuple(
            _exact_fraction(value, "derivative") for value in self.derivatives
        )
        if any(probability <= 0 for probability in probabilities):
            raise ValueError(
                "all probabilities must be strictly positive; rank/boundary cases "
                "need a separate contract"
            )
        if sum(probabilities, Fraction(0)) != 1:
            raise ValueError("probabilities must sum exactly to one")
        if sum(derivatives, Fraction(0)) != 0:
            raise ValueError("probability derivatives must sum exactly to zero")

        scores = tuple(
            derivative / probability
            for probability, derivative in zip(probabilities, derivatives)
        )
        fisher_information = sum(
            (
                derivative * derivative / probability
                for probability, derivative in zip(probabilities, derivatives)
            ),
            Fraction(0),
        )

        grouped: dict[Fraction, tuple[Fraction, Fraction]] = {}
        for probability, derivative, score in zip(probabilities, derivatives, scores):
            grouped_probability, grouped_derivative = grouped.get(
                score, (Fraction(0), Fraction(0))
            )
            grouped[score] = (
                grouped_probability + probability,
                grouped_derivative + derivative,
            )

        all_score_values = tuple(sorted(grouped))
        nonzero_score_values = tuple(score for score in all_score_values if score != 0)
        m_all = len(all_score_values)
        m_nonzero = len(nonzero_score_values)
        dimension_sufficient = m_all <= self.ancilla_dimension
        grouped_fisher_information = None
        exact_match = False
        if dimension_sufficient:
            grouped_fisher_information = sum(
                (
                    derivative * derivative / probability
                    for probability, derivative in grouped.values()
                ),
                Fraction(0),
            )
            exact_match = grouped_fisher_information == fisher_information

        theorem_2_no_go = m_nonzero > self.ancilla_dimension
        if theorem_2_no_go:
            status = "THEOREM_2_NO_GO_CONDITION_TRIGGERED"
        elif dimension_sufficient and exact_match:
            status = "EXACT_ORTHOGONAL_SCORE_ENCODING_MATCH"
        elif not dimension_sufficient and m_nonzero <= self.ancilla_dimension:
            status = "ZERO_SCORE_CLASS_DIMENSION_GAP"
        else:
            status = "REQUIRES_SEPARATE_REVIEW"

        return {
            "case_id": self.case_id,
            "ancilla_dimension": self.ancilla_dimension,
            "probability_normalization": str(sum(probabilities, Fraction(0))),
            "derivative_normalization": str(sum(derivatives, Fraction(0))),
            "system_classical_fisher_information": str(fisher_information),
            "distinct_nonzero_score_values": [str(score) for score in nonzero_score_values],
            "distinct_all_score_values_including_zero": [
                str(score) for score in all_score_values
            ],
            "m_nonzero": m_nonzero,
            "m_all": m_all,
            "theorem_2_no_go_condition_triggered": theorem_2_no_go,
            "orthogonal_score_encoding_dimension_sufficient": dimension_sufficient,
            "grouped_fisher_information_if_feasible": (
                None
                if grouped_fisher_information is None
                else str(grouped_fisher_information)
            ),
            "perfect_transfer_constructed_in_exact_classical_model": bool(
                dimension_sufficient and exact_match
            ),
            "status": status,
            "evidence_level": "MODEL_ONLY",
            "physical_law_claim_allowed": False,
        }


def case_from_scores(
    case_id: str,
    probabilities: Iterable[Fraction | int],
    scores: Iterable[Fraction | int],
    ancilla_dimension: int,
) -> AncillaQfiCase:
    """Build a local score fixture with exact p_i' = p_i q_i values."""
    exact_probabilities = tuple(
        _exact_fraction(value, "probability") for value in probabilities
    )
    exact_scores = tuple(_exact_fraction(value, "score") for value in scores)
    if len(exact_probabilities) != len(exact_scores):
        raise ValueError("probabilities and scores must have equal length")
    derivatives = tuple(
        probability * score
        for probability, score in zip(exact_probabilities, exact_scores)
    )
    return AncillaQfiCase(
        case_id=case_id,
        probabilities=exact_probabilities,
        derivatives=derivatives,
        ancilla_dimension=ancilla_dimension,
    )


def reference_cases() -> tuple[AncillaQfiCase, ...]:
    """Small frozen fixtures, including the zero-score and near-degenerate cases."""
    return (
        case_from_scores(
            "two_score_classes_n2",
            [Fraction(1, 4)] * 4,
            [Fraction(1), Fraction(-1), Fraction(1), Fraction(-1)],
            2,
        ),
        case_from_scores(
            "three_nonzero_score_classes_n2",
            [Fraction(1, 3)] * 3,
            [Fraction(1), Fraction(1, 10), Fraction(-11, 10)],
            2,
        ),
        case_from_scores(
            "zero_score_class_n2",
            [Fraction(1, 3)] * 3,
            [Fraction(0), Fraction(1), Fraction(-1)],
            2,
        ),
        case_from_scores(
            "near_degenerate_scores_n2",
            [Fraction(1, 3)] * 3,
            [
                Fraction(1),
                Fraction(1000000000001, 1000000000000),
                Fraction(-2000000000001, 1000000000000),
            ],
            2,
        ),
    )


def run_reference_cases() -> list[dict[str, Any]]:
    """Return deterministic JSON-compatible exact-rational case records."""
    return [case.analyze() for case in reference_cases()]
