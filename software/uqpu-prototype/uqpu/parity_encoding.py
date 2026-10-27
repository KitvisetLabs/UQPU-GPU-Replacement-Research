"""Deterministic graph-parity baseline for QAOA encoding audits.

This module is a classical correctness oracle for the logical-to-edge-parity
map. It does not compile circuits, implement QAOA, or claim quantum advantage.
"""
from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from typing import Iterable, Sequence


@dataclass(frozen=True)
class ParityEncoding:
    """Canonical edge-parity representation of an undirected graph.

    Physical bit z_e represents x_u XOR x_v for edge e=(u,v). Each fundamental
    cycle contributes an independent XOR constraint requiring even parity.
    """
    vertex_count: int
    edges: tuple[tuple[int, int], ...]
    cycle_constraints: tuple[tuple[int, ...], ...]
    components: tuple[tuple[int, ...], ...]

    @property
    def physical_qubit_count(self) -> int:
        """Return the number of edge variables; this is not a hardware estimate."""
        return len(self.edges)

    @property
    def cycle_rank(self) -> int:
        """Return the number of independent fundamental-cycle constraints."""
        return len(self.cycle_constraints)

    @staticmethod
    def _bits(values: Sequence[int] | str, expected_len: int, field: str) -> tuple[int, ...]:
        if isinstance(values, str):
            if any(character not in "01" for character in values):
                raise ValueError(f"{field} must contain only 0 and 1")
            bits = tuple(int(character) for character in values)
        else:
            try:
                bits = tuple(values)
            except TypeError as exc:
                raise ValueError(f"{field} must be a bit sequence") from exc
        if len(bits) != expected_len:
            raise ValueError(f"{field} length must equal {expected_len}")
        if any(type(bit) is not int or bit not in (0, 1) for bit in bits):
            raise ValueError(f"{field} entries must be integer bits 0 or 1")
        return bits

    def encode_logical(self, logical_bits: Sequence[int] | str) -> tuple[int, ...]:
        """Map vertex bits to canonical edge-parity bits."""
        logical = self._bits(logical_bits, self.vertex_count, "logical_bits")
        return tuple(logical[u] ^ logical[v] for u, v in self.edges)

    def is_valid_physical(self, physical_bits: Sequence[int] | str) -> bool:
        """Return whether a well-formed edge assignment satisfies every cycle."""
        physical = self._bits(physical_bits, self.physical_qubit_count, "physical_bits")
        return all(sum(physical[index] for index in cycle) % 2 == 0
                   for cycle in self.cycle_constraints)

    def decode_physical(self, physical_bits: Sequence[int] | str) -> tuple[int, ...]:
        """Decode a valid edge assignment with the smallest vertex of each
        connected component fixed to zero, removing the component-wise global
        flip ambiguity. Invalid parity assignments fail closed.
        """
        physical = self._bits(physical_bits, self.physical_qubit_count, "physical_bits")
        if not self.is_valid_physical(physical):
            raise ValueError("physical_bits violate one or more cycle-parity constraints")

        adjacency: list[list[tuple[int, int]]] = [[] for _ in range(self.vertex_count)]
        for edge_index, (u, v) in enumerate(self.edges):
            adjacency[u].append((v, physical[edge_index]))
            adjacency[v].append((u, physical[edge_index]))

        logical: list[int | None] = [None] * self.vertex_count
        for component in self.components:
            root = min(component)
            logical[root] = 0
            queue = deque([root])
            while queue:
                u = queue.popleft()
                for v, parity in adjacency[u]:
                    proposed = logical[u] ^ parity  # type: ignore[operator]
                    if logical[v] is None:
                        logical[v] = proposed
                        queue.append(v)
                    elif logical[v] != proposed:
                        raise ValueError("physical_bits are inconsistent with the graph")

        return tuple(int(bit) for bit in logical)


def build_parity_encoding(
    vertex_count: int, edges: Iterable[tuple[int, int]]
) -> ParityEncoding:
    """Build a stable spanning-forest cycle basis for a simple undirected graph.

    Edges are normalized and sorted, so the physical-bit order and constraint
    identities are deterministic. Self-loops and duplicate undirected edges
    are rejected rather than silently changing the encoding.
    """
    if type(vertex_count) is not int or vertex_count < 1:
        raise ValueError("vertex_count must be an integer >= 1")
    try:
        raw_edges = list(edges)
    except TypeError as exc:
        raise ValueError("edges must be an iterable of endpoint pairs") from exc

    normalized: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for raw in raw_edges:
        if not isinstance(raw, (tuple, list)) or len(raw) != 2:
            raise ValueError("each edge must be a pair of integer endpoints")
        u, v = raw
        if type(u) is not int or type(v) is not int:
            raise ValueError("edge endpoints must be integer vertices")
        if not (0 <= u < vertex_count and 0 <= v < vertex_count):
            raise ValueError("edge endpoints must be inside [0, vertex_count)")
        if u == v:
            raise ValueError("self-loops are not supported")
        edge = tuple(sorted((u, v)))
        if edge in seen:
            raise ValueError("duplicate undirected edges are not supported")
        seen.add(edge)
        normalized.append(edge)

    canonical_edges = tuple(sorted(normalized))
    parent = list(range(vertex_count))
    rank = [0] * vertex_count

    def find(vertex: int) -> int:
        while parent[vertex] != vertex:
            parent[vertex] = parent[parent[vertex]]
            vertex = parent[vertex]
        return vertex

    def union(left: int, right: int) -> bool:
        root_left, root_right = find(left), find(right)
        if root_left == root_right:
            return False
        if rank[root_left] < rank[root_right]:
            root_left, root_right = root_right, root_left
        parent[root_right] = root_left
        if rank[root_left] == rank[root_right]:
            rank[root_left] += 1
        return True

    tree_adjacency: list[list[tuple[int, int]]] = [[] for _ in range(vertex_count)]
    non_tree_edges: list[tuple[int, int, int]] = []
    for edge_index, (u, v) in enumerate(canonical_edges):
        if union(u, v):
            tree_adjacency[u].append((v, edge_index))
            tree_adjacency[v].append((u, edge_index))
        else:
            non_tree_edges.append((u, v, edge_index))

    groups: dict[int, list[int]] = {}
    for vertex in range(vertex_count):
        groups.setdefault(find(vertex), []).append(vertex)
    components = tuple(sorted(
        (tuple(sorted(group)) for group in groups.values()),
        key=lambda component: component[0],
    ))

    constraints: list[tuple[int, ...]] = []
    for u, v, closing_edge_index in non_tree_edges:
        previous: dict[int, tuple[int | None, int | None]] = {u: (None, None)}
        queue = deque([u])
        while queue and v not in previous:
            node = queue.popleft()
            for neighbor, edge_index in tree_adjacency[node]:
                if neighbor not in previous:
                    previous[neighbor] = (node, edge_index)
                    queue.append(neighbor)
        if v not in previous:
            raise RuntimeError("spanning-forest path missing for a non-tree edge")

        path_edge_indices: list[int] = []
        node = v
        while node != u:
            previous_node, edge_index = previous[node]
            path_edge_indices.append(int(edge_index))
            node = int(previous_node)
        constraints.append(tuple(sorted(path_edge_indices + [closing_edge_index])))

    return ParityEncoding(
        vertex_count=vertex_count,
        edges=canonical_edges,
        cycle_constraints=tuple(constraints),
        components=components,
    )
