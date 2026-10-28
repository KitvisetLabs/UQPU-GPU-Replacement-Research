"""Exact signed Max-Cut objective lowering for Lane A semantic-contract tests.

This is a classical algebraic oracle only. It does not construct QAOA circuits,
call a provider, estimate hardware resources, or establish quantum advantage.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from collections.abc import Iterable, Sequence


def _bits(values: Sequence[int] | str, expected: int) -> tuple[int, ...]:
    if isinstance(values, str):
        if any(ch not in "01" for ch in values):
            raise ValueError("bits must contain only 0 and 1")
        result = tuple(int(ch) for ch in values)
    else:
        try:
            result = tuple(values)
        except TypeError as exc:
            raise ValueError("bits must be a bit sequence") from exc
    if len(result) != expected:
        raise ValueError("bit sequence length must equal vertex_count")
    if any(type(bit) is not int or bit not in (0, 1) for bit in result):
        raise ValueError("bits must be integer 0/1 values, not booleans or floats")
    return result


def _finite_fsum(values: Iterable[float], label: str) -> float:
    """Sum finite numeric terms and fail closed if the result overflows."""
    try:
        result = math.fsum(values)
    except OverflowError as exc:
        raise ValueError(f"{label} is outside finite floating-point range") from exc
    if not math.isfinite(result):
        raise ValueError(f"{label} is outside finite floating-point range")
    return result


@dataclass(frozen=True)
class SignedMaxCutLowering:
    """Canonical direct, QUBO and Ising forms of one signed Max-Cut objective.

    Objective convention:
        C(x) = sum_(u,v) w_uv * (x_u XOR x_v), with real signed weights.

    QUBO:
        C(x) = sum_v linear[v] * x_v
               + sum_(u,v) quadratic[u,v] * x_u * x_v

    Ising:
        s_v = 1 - 2*x_v
        C(s) = ising_constant + sum_(u,v) J_uv * s_u * s_v
    """
    vertex_count: int
    edges: tuple[tuple[int, int, float], ...]
    qubo_linear: tuple[float, ...]
    qubo_quadratic: tuple[tuple[int, int, float], ...]
    ising_constant: float
    ising_couplings: tuple[tuple[int, int, float], ...]

    def direct_score(self, bits: Sequence[int] | str) -> float:
        x = _bits(bits, self.vertex_count)
        return _finite_fsum(
            (weight for u, v, weight in self.edges if x[u] ^ x[v]),
            "direct objective score",
        )

    def qubo_score(self, bits: Sequence[int] | str) -> float:
        x = _bits(bits, self.vertex_count)
        return _finite_fsum(
            [self.qubo_linear[i] * x[i] for i in range(self.vertex_count)]
            + [coefficient * x[u] * x[v]
               for u, v, coefficient in self.qubo_quadratic],
            "QUBO objective score",
        )

    def ising_score(self, bits: Sequence[int] | str) -> float:
        x = _bits(bits, self.vertex_count)
        spins = tuple(1 - 2 * bit for bit in x)
        return _finite_fsum(
            [self.ising_constant]
            + [coefficient * spins[u] * spins[v]
               for u, v, coefficient in self.ising_couplings],
            "Ising objective score",
        )


def compile_signed_maxcut(
    vertex_count: int, edges: Iterable[tuple[int, int, int | float]]
) -> SignedMaxCutLowering:
    """Lower a signed weighted graph into algebraic QUBO and Ising forms.

    Edges are (u, v, weight). Undirected edges are normalized and sorted.
    Duplicate edges, self-loops, invalid vertices, booleans, and non-finite
    weights are rejected rather than silently changing the objective.
    """
    if isinstance(vertex_count, bool) or not isinstance(vertex_count, int) or vertex_count < 1:
        raise ValueError("vertex_count must be a positive integer")
    try:
        raw_edges = tuple(edges)
    except TypeError as exc:
        raise ValueError("edges must be iterable") from exc

    normalized: list[tuple[int, int, float]] = []
    seen: set[tuple[int, int]] = set()
    for edge in raw_edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 3:
            raise ValueError("each edge must be a (u, v, weight) triple")
        u, v, raw_weight = edge
        if type(u) is not int or type(v) is not int:
            raise ValueError("edge endpoints must be integer vertex indices")
        if not (0 <= u < vertex_count and 0 <= v < vertex_count):
            raise ValueError("edge endpoint is outside vertex_count")
        if u == v:
            raise ValueError("self-loops are not accepted")
        if isinstance(raw_weight, bool) or not isinstance(raw_weight, (int, float)):
            raise ValueError("edge weight must be a finite real number")
        try:
            weight = float(raw_weight)
        except (OverflowError, ValueError) as exc:
            raise ValueError("edge weight must be a finite real number") from exc
        if not math.isfinite(weight):
            raise ValueError("edge weight must be a finite real number")
        pair = (min(u, v), max(u, v))
        if pair in seen:
            raise ValueError("duplicate undirected edge")
        seen.add(pair)
        normalized.append((pair[0], pair[1], weight))
    normalized.sort(key=lambda item: (item[0], item[1]))

    linear_terms: list[list[float]] = [[] for _ in range(vertex_count)]
    quadratic: list[tuple[int, int, float]] = []
    couplings: list[tuple[int, int, float]] = []
    weights: list[float] = []
    for u, v, weight in normalized:
        linear_terms[u].append(weight)
        linear_terms[v].append(weight)
        qubo_coefficient = -2.0 * weight
        ising_coupling = -0.5 * weight
        if not math.isfinite(qubo_coefficient) or not math.isfinite(ising_coupling):
            raise ValueError("derived QUBO/Ising coefficient is outside finite floating-point range")
        quadratic.append((u, v, qubo_coefficient))
        couplings.append((u, v, ising_coupling))
        weights.append(weight)

    return SignedMaxCutLowering(
        vertex_count=vertex_count,
        edges=tuple(normalized),
        qubo_linear=tuple(
            _finite_fsum(terms, "QUBO linear coefficient") for terms in linear_terms
        ),
        qubo_quadratic=tuple(quadratic),
        ising_constant=_finite_fsum(
            (0.5 * weight for weight in weights), "Ising constant"
        ),
        ising_couplings=tuple(couplings),
    )
