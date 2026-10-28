"""Strict chronological holdout certificates for time-dependent model evaluation.

A PASS certifies only the supplied raw-record manifest, group disjointness and
chronological ordering. It does not authenticate a source dataset or establish
scientific generalization, physical truth, or engineering advantage.
"""
from __future__ import annotations

from collections.abc import Iterable, Mapping
from datetime import datetime, timezone
import hashlib
import json
import math
from typing import Any

from .split_disjointness import build_split_manifest, verify_split_manifest_records


_SCHEMA = "uqpu-temporal-holdout-certificate-v1"
_RAW_FIELDS = {"record_id", "group_id", "split", "payload"}
_SPLITS = ("train", "validation", "test")


def _parse_utc_timestamp(value: Any, label: str) -> datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be a nonempty ISO-8601 timestamp")
    text = value.strip()
    if text.endswith(("Z", "z")):
        text = text[:-1] + "+00:00"
    try:
        parsed = datetime.fromisoformat(text)
    except ValueError as exc:
        raise ValueError(f"{label} must be a valid ISO-8601 timestamp") from exc
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        raise ValueError(f"{label} must include an explicit UTC offset")
    return parsed.astimezone(timezone.utc)


def validate_temporal_holdout(
    records: Iterable[Mapping[str, Any]],
    *,
    timestamp_field: str = "timestamp",
    embargo_seconds: int | float = 0.0,
) -> dict[str, Any]:
    """Certify chronological, group-disjoint train/validation/test partitions.

    Each raw record must have exactly record_id, group_id, split and payload.
    The timestamp is read from payload[timestamp_field] and must include a
    timezone. Split intervals must be strictly ordered and separated by at
    least embargo_seconds. Group and content disjointness are delegated to the
    canonical split-manifest validator.

    The certificate is metadata/provenance evidence only; it cannot establish
    source authenticity, representative sampling, or out-of-distribution skill.
    """
    if not isinstance(timestamp_field, str) or not timestamp_field.strip():
        raise ValueError("timestamp_field must be a nonempty string")
    if isinstance(embargo_seconds, bool) or not isinstance(embargo_seconds, (int, float)):
        raise ValueError("embargo_seconds must be a finite nonnegative real")
    try:
        embargo = float(embargo_seconds)
    except (OverflowError, TypeError, ValueError) as exc:
        raise ValueError("embargo_seconds must be a finite nonnegative real") from exc
    if not math.isfinite(embargo) or embargo < 0:
        raise ValueError("embargo_seconds must be a finite nonnegative real")

    try:
        raw_records = list(records)
    except TypeError as exc:
        raise ValueError("records must be iterable") from exc
    if not raw_records:
        raise ValueError("records must not be empty")
    for index, record in enumerate(raw_records):
        if not isinstance(record, Mapping) or set(record) != _RAW_FIELDS:
            raise ValueError(
                f"records[{index}] must contain exactly record_id, group_id, split, and payload"
            )

    manifest = build_split_manifest(raw_records, holdout_unit="TIME_BLOCK")
    binding = verify_split_manifest_records(manifest, raw_records)

    timestamps: dict[str, list[datetime]] = {name: [] for name in _SPLITS}
    groups: dict[str, set[str]] = {name: set() for name in _SPLITS}
    for index, record in enumerate(raw_records):
        payload = record["payload"]
        if not isinstance(payload, Mapping) or timestamp_field not in payload:
            raise ValueError(
                f"records[{index}].payload must contain timestamp field {timestamp_field!r}"
            )
        timestamps[record["split"]].append(
            _parse_utc_timestamp(payload[timestamp_field], f"records[{index}].{timestamp_field}")
        )
        groups[record["split"]].add(record["group_id"])

    summary: dict[str, dict[str, Any]] = {}
    for split_name in _SPLITS:
        values = timestamps[split_name]
        if not values:
            raise ValueError(f"split {split_name!r} must not be empty")
        summary[split_name] = {
            "record_count": len(values),
            "group_count": len(groups[split_name]),
            "start_utc": min(values).isoformat(),
            "end_utc": max(values).isoformat(),
        }

    gaps = {
        "train_to_validation": (
            min(timestamps["validation"]) - max(timestamps["train"])
        ).total_seconds(),
        "validation_to_test": (
            min(timestamps["test"]) - max(timestamps["validation"])
        ).total_seconds(),
    }
    for name, gap in gaps.items():
        if gap <= 0:
            raise ValueError(f"{name} must be strictly positive; temporal partitions overlap or are out of order")
        if gap < embargo:
            raise ValueError(
                f"{name} gap {gap} seconds is below requested embargo {embargo} seconds"
            )

    manifest_bytes = json.dumps(
        manifest, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False
    ).encode("utf-8")
    return {
        "schema": _SCHEMA,
        "status": "PASS",
        "holdout_unit": "TIME_BLOCK",
        "timestamp_field": timestamp_field,
        "embargo_seconds": embargo,
        "strict_temporal_order": True,
        "dataset_sha256": manifest["dataset_sha256"],
        "split_manifest_sha256": hashlib.sha256(manifest_bytes).hexdigest(),
        "split_sha256": binding["split_sha256"],
        "raw_record_binding_verified": bool(binding.get("raw_record_binding_verified", False)),
        "split_summary": summary,
        "gaps_seconds": gaps,
        "source_authenticity_verified": False,
        "scientific_generalization_verified": False,
        "limitations": [
            "The certificate binds the supplied raw records but does not authenticate their external source or license.",
            "Chronological and group disjointness do not prove that a model generalizes to unseen physics.",
            "Physical residuals, conservation/bounds, uncertainty, compute resources and independent references require separate evaluation.",
        ],
    }
