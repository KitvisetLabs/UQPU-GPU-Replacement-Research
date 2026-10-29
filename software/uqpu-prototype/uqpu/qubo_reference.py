"""Exhaustive objective references for small binary QUBO instances.

Convention: E(x) = sum(q_ij * x_i * x_j), with each unordered pair
represented exactly once using 0 <= i <= j < n. Coefficients are parsed
through Decimal(str(value)) so the certificate is deterministic for the
declared decimal inputs. This is an objective oracle, not a feasibility
proof for constraints that are external to the QUBO.
"""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from hashlib import sha256
from itertools import product
import json
from collections.abc import Iterable

MAX_EXACT_QUBO_VARIABLES = 20
_CONVENTION = "E(x)=sum(q_ij*x_i*x_j); each pair appears once with 0<=i<=j<n"


def _as_decimal(value: object, field_name: str) -> Decimal:
    if isinstance(value, bool):
        raise ValueError(f"{field_name} must be a finite decimal number")
    try:
        result = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError) as exc:
        raise ValueError(f"{field_name} must be a finite decimal number") from exc
    if not result.is_finite():
        raise ValueError(f"{field_name} must be a finite decimal number")
    return result


def _decimal_text(value: Decimal) -> str:
    if value == 0:
        return "0"
    return format(value.normalize(), "f")


def exact_qubo_reference(
    num_variables: int,
    terms: Iterable[tuple[int, int, int | float | str]],
) -> dict[str, object]:
    """Return a reproducible exhaustive minimum and SHA-256 certificate.

    Args:
        num_variables: Positive binary-variable count; hard-capped at 20.
        terms: Unique (i, j, coefficient) terms with i <= j. Combine duplicate
            coefficients before calling this function.

    The returned optimum covers every one of the 2**n bitstrings. If feasibility
    is imposed outside the QUBO objective, it must be checked separately.
    """
    if (
        not isinstance(num_variables, int)
        or isinstance(num_variables, bool)
        or num_variables <= 0
    ):
        raise ValueError("num_variables must be a positive integer")
    if num_variables > MAX_EXACT_QUBO_VARIABLES:
        raise ValueError(
            f"exact reference is limited to {MAX_EXACT_QUBO_VARIABLES} variables"
        )

    normalized: list[tuple[int, int, Decimal]] = []
    seen: set[tuple[int, int]] = set()
    for term in terms:
        if not isinstance(term, (tuple, list)) or len(term) != 3:
            raise ValueError("each term must be (i, j, coefficient)")
        i, j, raw_coefficient = term
        if any(
            not isinstance(index, int) or isinstance(index, bool)
            for index in (i, j)
        ):
            raise ValueError("term indices must be integers")
        if i < 0 or j < 0 or i >= num_variables or j >= num_variables:
            raise ValueError("term index out of range")
        if i > j:
            raise ValueError("terms must use canonical upper-triangle indices i <= j")
        if (i, j) in seen:
            raise ValueError(
                "duplicate QUBO term; combine coefficients before certification"
            )
        seen.add((i, j))
        normalized.append((i, j, _as_decimal(raw_coefficient, "coefficient")))
    normalized.sort(key=lambda row: (row[0], row[1]))

    problem = {
        "schema_version": 1,
        "num_variables": num_variables,
        "objective_sense": "MINIMIZE",
        "convention": _CONVENTION,
        "terms": [
            {"i": i, "j": j, "coefficient": _decimal_text(coefficient)}
            for i, j, coefficient in normalized
        ],
    }
    canonical_problem = json.dumps(
        problem, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    problem_sha256 = sha256(canonical_problem.encode("utf-8")).hexdigest()

    best_energy: Decimal | None = None
    optimal_bitstrings: list[str] = []
    for bits in product((0, 1), repeat=num_variables):
        energy = sum(
            (
                coefficient * bits[i] * bits[j]
                for i, j, coefficient in normalized
            ),
            Decimal(0),
        )
        bitstring = "".join(str(bit) for bit in bits)
        if best_energy is None or energy < best_energy:
            best_energy = energy
            optimal_bitstrings = [bitstring]
        elif energy == best_energy:
            optimal_bitstrings.append(bitstring)

    # num_variables is positive, so at least one assignment is always evaluated.
    assert best_energy is not None
    certificate_payload = {
        "schema_version": 1,
        "problem_sha256": problem_sha256,
        "optimum_energy": _decimal_text(best_energy),
        "optimal_bitstrings": optimal_bitstrings,
        "evaluated_assignments": 1 << num_variables,
        "reference_kind": "EXHAUSTIVE_BINARY_ENUMERATION",
        "claim_boundary": (
            "small-instance objective reference only; not a feasibility proof "
            "for constraints external to the QUBO"
        ),
    }
    canonical_certificate = json.dumps(
        certificate_payload, sort_keys=True, separators=(",", ":"), ensure_ascii=True
    )
    return {
        **certificate_payload,
        "certificate_sha256": sha256(canonical_certificate.encode("utf-8")).hexdigest(),
        "problem": problem,
    }
