"""Graph-level ledger checks for reusable formal-proof discovery artifacts.

This module validates metadata and dependency structure only. It does not run
Lean or another kernel, prove semantic equivalence, establish theorem novelty,
or turn formal mathematics into empirical physics.
"""
from __future__ import annotations

from collections import Counter
from collections.abc import Iterable, Mapping
import re

_SHA256 = re.compile(r"^[0-9a-f]{64}$")
_STATUSES = frozenset({
    "CANDIDATE", "PARTIAL", "KERNEL_CHECKED",
    "INDEPENDENTLY_REPRODUCED", "FAILED", "INCONCLUSIVE",
})
_SPLITS = frozenset({"train", "validation", "test"})


def _strings(name: str, value: object, *, allow_empty: bool = False) -> tuple[str, ...]:
    if isinstance(value, (str, bytes)) or not isinstance(value, Iterable):
        raise ValueError(f"{name} must be a collection of strings")
    items = tuple(value)
    if not allow_empty and not items:
        raise ValueError(f"{name} must not be empty")
    if any(not isinstance(x, str) or not x.strip() for x in items):
        raise ValueError(f"{name} entries must be nonempty strings")
    if len(set(items)) != len(items):
        raise ValueError(f"{name} contains duplicates")
    return items


def _digest(value: object, field: str, *, required: bool) -> None:
    if not isinstance(value, str):
        raise ValueError(f"{field} must be a string")
    if not value and not required:
        return
    if not _SHA256.fullmatch(value):
        raise ValueError(f"{field} must be a lowercase SHA-256 digest")


def validate_proof_dag(nodes: Iterable[Mapping[str, object]]) -> dict[str, object]:
    """Fail closed on invalid proof-DAG metadata, split leakage and unsafe reuse.

    Required per-node fields: node_id, claim_family, split, status,
    statement_sha256, parents, residual_premises. Checked/failed nodes must bind
    a proof-evidence record and checker log to immutable source/checker metadata.
    Reused schemas must point to a training-split, kernel-checked or independently
    reproduced source node and expose residual premises explicitly.
    """
    if isinstance(nodes, (str, bytes)) or not isinstance(nodes, Iterable):
        raise ValueError("nodes must be an iterable of node mappings")
    rows = tuple(nodes)
    if not rows:
        raise ValueError("nodes must not be empty")

    by_id: dict[str, dict[str, object]] = {}
    family_split: dict[str, str] = {}
    for raw in rows:
        if not isinstance(raw, Mapping):
            raise ValueError("each node must be a mapping")
        node = dict(raw)
        for field in (
            "node_id", "claim_family", "split", "status",
            "statement_sha256", "parents", "residual_premises",
        ):
            if field not in node:
                raise ValueError(f"{field} is required")
        for field in ("node_id", "claim_family", "split", "status"):
            if not isinstance(node.get(field), str) or not str(node[field]).strip():
                raise ValueError(f"{field} is required")
        node_id = str(node["node_id"])
        family = str(node["claim_family"])
        split = str(node["split"])
        status = str(node["status"])
        if node_id in by_id:
            raise ValueError(f"duplicate node_id: {node_id}")
        if split not in _SPLITS:
            raise ValueError(f"unknown split for {node_id}: {split}")
        if status not in _STATUSES:
            raise ValueError(f"unknown status for {node_id}: {status}")
        previous_split = family_split.get(family)
        if previous_split is not None and previous_split != split:
            raise ValueError(f"claim family leakage across splits: {family}")
        family_split[family] = split
        _digest(node.get("statement_sha256"), f"{node_id}.statement_sha256", required=True)
        parents = _strings(f"{node_id}.parents", node["parents"], allow_empty=True)
        residuals = _strings(
            f"{node_id}.residual_premises",
            node["residual_premises"],
            allow_empty=True,
        )
        node["parents"] = parents
        node["residual_premises"] = residuals
        by_id[node_id] = node

    for node_id, node in by_id.items():
        dependencies = list(node["parents"])
        reuse_from = node.get("reused_schema_from", "")
        if not isinstance(reuse_from, str):
            raise ValueError(f"{node_id}.reused_schema_from must be a string")
        if reuse_from:
            if not reuse_from.strip():
                raise ValueError(f"{node_id}.reused_schema_from must be a nonempty ID or empty")
            if reuse_from not in dependencies:
                raise ValueError(f"{node_id} must list reused schema source as a parent")
            if reuse_from not in by_id:
                raise ValueError(f"{node_id} references missing schema source: {reuse_from}")
            source = by_id[reuse_from]
            if source["split"] != "train":
                raise ValueError(f"{node_id} schema source must be in train split")
            if source["status"] not in {"KERNEL_CHECKED", "INDEPENDENTLY_REPRODUCED"}:
                raise ValueError(f"{node_id} schema source is not verified")
            if not node["residual_premises"] and node.get("residual_premises_closed") is not True:
                raise ValueError(
                    f"{node_id} must expose residual premises or certify residual_premises_closed"
                )
        for parent in dependencies:
            if parent not in by_id:
                raise ValueError(f"{node_id} references missing parent: {parent}")

        status = node["status"]
        checked_or_failed = status in {
            "KERNEL_CHECKED", "INDEPENDENTLY_REPRODUCED", "FAILED"
        }
        for field in ("proof_record_sha256", "checker_run_sha256"):
            _digest(node.get(field, ""), f"{node_id}.{field}", required=checked_or_failed)
        if checked_or_failed:
            revision = node.get("source_revision", "")
            if not isinstance(revision, str) or not re.fullmatch(
                r"(?:[0-9a-f]{40}|[0-9a-f]{64})", revision
            ):
                raise ValueError(f"{node_id}.source_revision must be an immutable revision")
            for field in ("checker_name", "checker_version"):
                if not isinstance(node.get(field), str) or not str(node[field]).strip():
                    raise ValueError(f"{node_id}.{field} is required")
            exit_code = node.get("checker_exit_code")
            if status in {"KERNEL_CHECKED", "INDEPENDENTLY_REPRODUCED"} and exit_code != 0:
                raise ValueError(f"{node_id} checked status requires checker_exit_code=0")
            if status == "FAILED":
                if not isinstance(exit_code, int) or exit_code == 0:
                    raise ValueError(f"{node_id} FAILED status requires nonzero checker_exit_code")
                if not isinstance(node.get("failure_reason"), str) or not node["failure_reason"].strip():
                    raise ValueError(f"{node_id} FAILED status requires failure_reason")
        if status == "INDEPENDENTLY_REPRODUCED":
            count = node.get("independent_reproduction_count", 0)
            if not isinstance(count, int) or count < 1:
                raise ValueError(f"{node_id} requires independent_reproduction_count >= 1")
        if status == "INCONCLUSIVE" and not str(node.get("failure_reason", "")).strip():
            raise ValueError(f"{node_id} INCONCLUSIVE status requires failure_reason")

    # Three-colour DFS detects cycles; reuse edges must also be explicit parents.
    colours: dict[str, int] = {}

    def visit(node_id: str) -> None:
        colour = colours.get(node_id, 0)
        if colour == 1:
            raise ValueError(f"proof DAG contains a cycle at {node_id}")
        if colour == 2:
            return
        colours[node_id] = 1
        for parent in by_id[node_id]["parents"]:
            visit(parent)
        colours[node_id] = 2

    for node_id in by_id:
        visit(node_id)

    counts = Counter(str(node["status"]) for node in by_id.values())
    return {
        "metadata_gate_passed": True,
        "evidence_class": "METADATA_ONLY_NOT_PROOF",
        "node_count": len(by_id),
        "status_counts": dict(sorted(counts.items())),
        "claim_family_count": len(family_split),
        "reused_schema_count": sum(bool(node.get("reused_schema_from")) for node in by_id.values()),
        "failed_attempt_count": counts["FAILED"],
        "inconclusive_count": counts["INCONCLUSIVE"],
        "claim_boundary": (
            "Validates graph bookkeeping, split separation and declared proof provenance only; "
            "does not execute a proof checker, prove semantic equivalence, establish novelty, "
            "or establish empirical physical truth."
        ),
    }
