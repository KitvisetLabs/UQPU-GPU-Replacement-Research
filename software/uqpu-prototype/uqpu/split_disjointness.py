"""Manifest-level proof of record and group disjointness for equation benchmarks.

A PASS certifies only the supplied manifest's declared IDs and hashes. It does
not prove that source data are authentic, scientifically representative, or that
any discovered equation is a physical law.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Mapping
from typing import Any, Iterable

_SCHEMA = "uqpu-split-manifest-v1"
_CERTIFICATE_SCHEMA = "uqpu-split-disjointness-certificate-v1"
_SHA256 = re.compile(r"[0-9a-f]{64}\\Z")
_SPLITS = ("train", "validation", "test")
_HOLDOUT_UNITS = {
    "LAW_FAMILY", "MATERIAL_FAMILY", "FLUID_PAIR", "SCALE", "GEOMETRY",
    "TIME_BLOCK", "DEVICE_FAMILY", "COMPOSITE_GROUP",
}
_RECORD_FIELDS = {"record_id", "group_id", "record_sha256"}


def _require_sha256(name: str, value: Any) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{name} must be a lowercase 64-character SHA-256 hex digest")
    return value


def _canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value, sort_keys=True, separators=(",", ":"), ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("manifest must be canonicalizable finite JSON data") from exc


def _sha256(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _nonempty_text(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value


def _normalize_records(split_name: str, records: Any) -> list[dict[str, str]]:
    if not isinstance(records, list) or not records:
        raise ValueError(f"splits.{split_name} must be a nonempty list")
    normalized: list[dict[str, str]] = []
    for index, record in enumerate(records):
        if not isinstance(record, Mapping) or set(record) != _RECORD_FIELDS:
            raise ValueError(
                f"splits.{split_name}[{index}] must contain exactly record_id, group_id, record_sha256"
            )
        normalized.append({
            "record_id": _nonempty_text("record_id", record["record_id"]),
            "group_id": _nonempty_text("group_id", record["group_id"]),
            "record_sha256": _require_sha256("record_sha256", record["record_sha256"]),
        })
    return sorted(normalized, key=lambda row: row["record_id"])


def validate_split_manifest(
    manifest: Mapping[str, Any], *,
    expected_dataset_sha256: str | None = None,
    expected_holdout_unit: str | None = None,
    expected_group_count: int | None = None,
    expected_manifest_sha256: str | None = None,
) -> dict[str, Any]:
    """Validate actual manifest entries and return a reproducible certificate.

    Canonical split hashes are SHA-256 over each split's record list sorted by
    record_id, serialized as UTF-8 JSON with sorted keys and compact separators.
    The held-out group hash is over the sorted unique test group IDs plus the
    declared holdout unit. Arrays in the source manifest are order-insensitive.
    """
    if not isinstance(manifest, Mapping):
        raise ValueError("manifest must be a JSON object")
    if set(manifest) != {"schema", "dataset_sha256", "holdout_unit", "splits"}:
        raise ValueError("manifest must contain exactly schema, dataset_sha256, holdout_unit, splits")
    if manifest.get("schema") != _SCHEMA:
        raise ValueError(f"schema must equal {_SCHEMA}")
    dataset_sha = _require_sha256("dataset_sha256", manifest.get("dataset_sha256"))
    holdout_unit = manifest.get("holdout_unit")
    if holdout_unit not in _HOLDOUT_UNITS:
        raise ValueError("holdout_unit must declare a supported group-disjoint unit")
    if expected_dataset_sha256 is not None and dataset_sha != expected_dataset_sha256:
        raise ValueError("dataset_sha256 does not match the preregistered comparison")
    if expected_holdout_unit is not None and holdout_unit != expected_holdout_unit:
        raise ValueError("holdout_unit does not match the preregistered comparison")

    raw_splits = manifest.get("splits")
    if not isinstance(raw_splits, Mapping) or set(raw_splits) != set(_SPLITS):
        raise ValueError("splits must contain exactly train, validation, and test")
    splits = {name: _normalize_records(name, raw_splits[name]) for name in _SPLITS}

    record_id_split: dict[str, str] = {}
    record_hash_split: dict[str, str] = {}
    group_splits: dict[str, set[str]] = {}
    for split_name, records in splits.items():
        for record in records:
            record_id = record["record_id"]
            if record_id in record_id_split:
                raise ValueError(
                    f"record_id {record_id!r} occurs in both {record_id_split[record_id]} and {split_name}"
                )
            record_id_split[record_id] = split_name
            record_hash = record["record_sha256"]
            if record_hash in record_hash_split:
                raise ValueError(
                    f"record_sha256 {record_hash} is duplicated across records/splits "
                    f"({record_hash_split[record_hash]} and {split_name})"
                )
            record_hash_split[record_hash] = split_name
            group_splits.setdefault(record["group_id"], set()).add(split_name)

    leaked_groups = {group: names for group, names in group_splits.items() if len(names) > 1}
    if leaked_groups:
        group, names = sorted(leaked_groups.items())[0]
        raise ValueError(f"group_id {group!r} leaks across splits: {', '.join(sorted(names))}")

    split_hashes = {name: _sha256(records) for name, records in splits.items()}
    test_groups = sorted({record["group_id"] for record in splits["test"]})
    heldout_group_hash = _sha256({
        "schema": "uqpu-heldout-groups-v1",
        "holdout_unit": holdout_unit,
        "groups": test_groups,
    })
    normalized_manifest = {
        "schema": _SCHEMA,
        "dataset_sha256": dataset_sha,
        "holdout_unit": holdout_unit,
        "splits": splits,
    }
    manifest_hash = _sha256(normalized_manifest)
    if expected_manifest_sha256 is not None:
        _require_sha256("expected_manifest_sha256", expected_manifest_sha256)
        if manifest_hash != expected_manifest_sha256:
            raise ValueError("canonical manifest hash does not match the preregistered hash")
    if expected_group_count is not None:
        if isinstance(expected_group_count, bool) or not isinstance(expected_group_count, int) or expected_group_count < 1:
            raise ValueError("expected_group_count must be an integer >= 1")
        if len(test_groups) != expected_group_count:
            raise ValueError("test group count does not match the preregistered comparison")

    return {
        "schema": _CERTIFICATE_SCHEMA,
        "status": "PASS",
        "dataset_sha256": dataset_sha,
        "holdout_unit": holdout_unit,
        "canonical_manifest_sha256": manifest_hash,
        "split_sha256": split_hashes,
        "heldout_group_manifest_sha256": heldout_group_hash,
        "record_counts": {name: len(splits[name]) for name in _SPLITS},
        "group_counts": {
            name: len({record["group_id"] for record in splits[name]}) for name in _SPLITS
        },
        "test_group_count": len(test_groups),
        "record_level_disjoint": True,
        "group_level_disjoint": True,
        "limitations": [
            "Certificate validates manifest declarations and hashes, not the truth or provenance of raw source data.",
            "A disjoint split is necessary but not sufficient for scientific validity, identifiability, or physical-law status.",
        ],
    }


def validate_comparison_manifest(runs: Iterable[Any], manifest: Mapping[str, Any]) -> dict[str, Any]:
    """Bind a split manifest to a matched comparison's declared hashes and groups."""
    records = tuple(runs)
    if not records:
        raise ValueError("at least two methods and 30 matched seeds are required")
    # Import lazily so manifest validation remains usable without comparator setup.
    from .equation_discovery_comparison import validate_matched_comparison

    methods = validate_matched_comparison(records)
    reference = records[0]
    certificate = validate_split_manifest(
        manifest,
        expected_dataset_sha256=reference.dataset_sha256,
        expected_holdout_unit=reference.holdout_unit,
        expected_group_count=reference.heldout_group_count,
    )
    for run in records:
        for split_name in _SPLITS:
            field = f"{split_name}_split_sha256"
            if getattr(run, field) != certificate["split_sha256"][split_name]:
                raise ValueError(f"{field} does not match the canonical manifest content")
        if run.heldout_group_manifest_sha256 != certificate["heldout_group_manifest_sha256"]:
            raise ValueError("heldout_group_manifest_sha256 does not match the canonical test groups")
    return {
        "schema": "uqpu-matched-comparison-with-split-certificate-v1",
        "method_ids": list(methods),
        "manifest_content_verified": True,
        "partition_certificate": certificate,
        "evidence_class": "MANIFEST_LEVEL_PARTITION_CERTIFICATE_ONLY",
        "non_claims": [
            "No proof of raw-data authenticity or scientific representativeness.",
            "No proof that a candidate equation is true, unique, or a physical law.",
            "No demonstrated QPU, material, fuel, electricity, or economic advantage.",
        ],
    }
