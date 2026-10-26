"""Source-provenance bundle contract for reproducible equation-discovery benchmarks.

A PASS checks internal consistency only. It does not fetch or authenticate the
external source, decide legal license compliance, or validate scientific truth.
"""
from __future__ import annotations

import hashlib
import json
import re
from collections.abc import Iterable, Mapping
from datetime import date
from typing import Any
from urllib.parse import urlsplit

from uqpu.split_disjointness import verify_split_manifest_records

_SCHEMA = "uqpu-dataset-source-provenance-v1"
_CERTIFICATE_SCHEMA = "uqpu-benchmark-bundle-certificate-v1"
_SHA256 = re.compile(r"[0-9a-f]{64}\Z")
_SPLITS = ("train", "validation", "test")
_MANIFEST_FIELDS = {
    "schema",
    "source_url",
    "source_revision",
    "license_id",
    "acquired_date",
    "raw_files",
    "row_count",
    "record_dataset_sha256",
    "preprocessing_sha256",
    "schema_sha256",
    "inclusion_policy_sha256",
    "exclusion_policy_sha256",
    "group_policy_sha256",
    "provenance_sha256",
}


def _canonical_bytes(value: Any) -> bytes:
    try:
        return json.dumps(
            value,
            sort_keys=True,
            separators=(",", ":"),
            ensure_ascii=False,
            allow_nan=False,
        ).encode("utf-8")
    except (TypeError, ValueError) as exc:
        raise ValueError("provenance data must be finite canonical JSON") from exc


def _digest(value: Any) -> str:
    return hashlib.sha256(_canonical_bytes(value)).hexdigest()


def _require_sha256(name: str, value: Any) -> str:
    if not isinstance(value, str) or _SHA256.fullmatch(value) is None:
        raise ValueError(f"{name} must be a lowercase 64-character SHA-256 digest")
    return value


def _text(name: str, value: Any) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be a nonempty string")
    return value.strip()


def _source_url(value: Any) -> str:
    value = _text("source_url", value)
    parsed = urlsplit(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValueError("source_url must be an absolute HTTPS URL")
    return value


def _source_revision(value: Any) -> str:
    value = _text("source_revision", value)
    if value.casefold() in {"main", "master", "latest", "head", "develop", "trunk"}:
        raise ValueError("source_revision must not be a mutable branch alias")
    return value


def _acquired_date(value: Any) -> str:
    value = _text("acquired_date", value)
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("acquired_date must use YYYY-MM-DD") from exc
    if parsed.isoformat() != value:
        raise ValueError("acquired_date must use canonical YYYY-MM-DD")
    return value


def _normalize_raw_files(raw_files: Any) -> list[dict[str, str]]:
    if not isinstance(raw_files, list) or not raw_files:
        raise ValueError("raw_files must be a nonempty list")
    normalized: list[dict[str, str]] = []
    seen: set[str] = set()
    for index, item in enumerate(raw_files):
        if not isinstance(item, Mapping) or set(item) != {"path", "sha256"}:
            raise ValueError(f"raw_files[{index}] must contain exactly path and sha256")
        path = _text(f"raw_files[{index}].path", item["path"])
        if path.startswith("/") or "\\" in path or any(part in {".", ".."} for part in path.split("/")):
            raise ValueError("raw file paths must be normalized relative POSIX paths")
        if path in seen:
            raise ValueError(f"raw file path {path!r} is duplicated")
        seen.add(path)
        normalized.append({
            "path": path,
            "sha256": _require_sha256(f"raw_files[{index}].sha256", item["sha256"]),
        })
    return sorted(normalized, key=lambda item: item["path"])


def _split_manifest_summary(split_manifest: Any) -> tuple[str, int]:
    if not isinstance(split_manifest, Mapping):
        raise ValueError("split_manifest must be a mapping")
    if split_manifest.get("schema") != "uqpu-split-manifest-v1":
        raise ValueError("split_manifest has an unsupported schema")
    dataset_sha256 = _require_sha256(
        "split_manifest.dataset_sha256", split_manifest.get("dataset_sha256")
    )
    splits = split_manifest.get("splits")
    if not isinstance(splits, Mapping) or set(splits) != set(_SPLITS):
        raise ValueError("split_manifest must contain train, validation, and test")
    row_count = 0
    for name in _SPLITS:
        rows = splits[name]
        if not isinstance(rows, list) or not rows:
            raise ValueError(f"split_manifest.splits.{name} must be a nonempty list")
        row_count += len(rows)
    return dataset_sha256, row_count


def _validate_common_fields(manifest: Mapping[str, Any]) -> dict[str, Any]:
    source_url = _source_url(manifest.get("source_url"))
    source_revision = _source_revision(manifest.get("source_revision"))
    license_id = _text("license_id", manifest.get("license_id"))
    acquired_date = _acquired_date(manifest.get("acquired_date"))
    raw_files = _normalize_raw_files(manifest.get("raw_files"))
    row_count = manifest.get("row_count")
    if isinstance(row_count, bool) or not isinstance(row_count, int) or row_count < 1:
        raise ValueError("row_count must be a positive integer")
    result: dict[str, Any] = {
        "schema": _SCHEMA,
        "source_url": source_url,
        "source_revision": source_revision,
        "license_id": license_id,
        "acquired_date": acquired_date,
        "raw_files": raw_files,
        "row_count": row_count,
        "record_dataset_sha256": _require_sha256(
            "record_dataset_sha256", manifest.get("record_dataset_sha256")
        ),
    }
    for name in (
        "preprocessing_sha256",
        "schema_sha256",
        "inclusion_policy_sha256",
        "exclusion_policy_sha256",
        "group_policy_sha256",
    ):
        result[name] = _require_sha256(name, manifest.get(name))
    return result


def build_dataset_provenance(
    *,
    source_url: str,
    source_revision: str,
    license_id: str,
    acquired_date: str,
    raw_files: list[Mapping[str, Any]],
    split_manifest: Mapping[str, Any],
    preprocessing_sha256: str,
    schema_sha256: str,
    inclusion_policy_sha256: str,
    exclusion_policy_sha256: str,
    group_policy_sha256: str,
) -> dict[str, Any]:
    """Build a canonical provenance manifest linked to a split manifest.

    Raw-file digests must be computed from the acquired bytes by the caller.
    This function validates their format and binds them into the manifest; it
    does not download the source or independently verify those bytes.
    """
    dataset_sha256, row_count = _split_manifest_summary(split_manifest)
    body = {
        "schema": _SCHEMA,
        "source_url": _source_url(source_url),
        "source_revision": _source_revision(source_revision),
        "license_id": _text("license_id", license_id),
        "acquired_date": _acquired_date(acquired_date),
        "raw_files": _normalize_raw_files(raw_files),
        "row_count": row_count,
        "record_dataset_sha256": dataset_sha256,
        "preprocessing_sha256": _require_sha256("preprocessing_sha256", preprocessing_sha256),
        "schema_sha256": _require_sha256("schema_sha256", schema_sha256),
        "inclusion_policy_sha256": _require_sha256("inclusion_policy_sha256", inclusion_policy_sha256),
        "exclusion_policy_sha256": _require_sha256("exclusion_policy_sha256", exclusion_policy_sha256),
        "group_policy_sha256": _require_sha256("group_policy_sha256", group_policy_sha256),
    }
    manifest = {**body, "provenance_sha256": _digest(body)}
    validate_dataset_provenance(manifest, split_manifest)
    return manifest


def validate_dataset_provenance(
    manifest: Mapping[str, Any],
    split_manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Validate provenance-manifest integrity and linkage to the declared split."""
    if not isinstance(manifest, Mapping) or set(manifest) != _MANIFEST_FIELDS:
        raise ValueError("provenance manifest has missing or unknown fields")
    if manifest.get("schema") != _SCHEMA:
        raise ValueError("unsupported provenance schema")
    body = _validate_common_fields(manifest)
    dataset_sha256, row_count = _split_manifest_summary(split_manifest)
    if body["record_dataset_sha256"] != dataset_sha256:
        raise ValueError("provenance dataset digest does not match split manifest")
    if body["row_count"] != row_count:
        raise ValueError("provenance row_count does not match split manifest")
    expected = _digest(body)
    supplied = _require_sha256("provenance_sha256", manifest.get("provenance_sha256"))
    if supplied != expected:
        raise ValueError("provenance_sha256 does not match canonical manifest fields")
    return {
        "schema": _CERTIFICATE_SCHEMA,
        "status": "PASS",
        "provenance_sha256": supplied,
        "dataset_sha256": dataset_sha256,
        "row_count": row_count,
        "source_authenticated": False,
        "license_legal_reviewed": False,
        "scientific_validity_established": False,
    }


def validate_benchmark_bundle(
    *,
    split_manifest: Mapping[str, Any],
    raw_records: Iterable[Mapping[str, Any]],
    provenance_manifest: Mapping[str, Any],
) -> dict[str, Any]:
    """Preflight raw-record binding, split disjointness, and provenance linkage."""
    split_certificate = verify_split_manifest_records(split_manifest, raw_records)
    provenance_certificate = validate_dataset_provenance(provenance_manifest, split_manifest)
    if split_certificate.get("status") != "PASS" or provenance_certificate.get("status") != "PASS":
        raise ValueError("benchmark bundle did not pass all preflight certificates")
    return {
        "schema": _CERTIFICATE_SCHEMA,
        "status": "PASS",
        "dataset_sha256": provenance_certificate["dataset_sha256"],
        "provenance_sha256": provenance_certificate["provenance_sha256"],
        "row_count": provenance_certificate["row_count"],
        "raw_record_binding_verified": bool(split_certificate.get("raw_record_binding_verified")),
        "split_disjointness_verified": True,
        "source_authenticated": False,
        "license_legal_reviewed": False,
        "scientific_validity_established": False,
    }
