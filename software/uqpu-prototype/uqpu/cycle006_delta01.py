"""Cycle 006 Delta 01: bounded scale, provenance, and adversarial gates.

All measurements in this module are local software measurements or synthetic
protocol fixtures.  No function submits provider work, authorizes spending,
fabricates materials, handles human data, or promotes source metadata into a
hardware, commercial, biological, paranormal, or physical-law claim.
"""
from __future__ import annotations

import binascii
from copy import deepcopy
from datetime import date, datetime, timezone
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import resource
import statistics
import struct
import tempfile
from time import perf_counter_ns
from typing import Any
import zlib

from .ai_training_baseline import BaselineConfig, _dataset
from .cycle003_delta01 import canonical_json_bytes
from .cycle005_delta01 import (
    COST_COMPONENTS,
    benchmark_scale_case,
    build_braket_dry_run_packet,
    build_capital_dependency_graph,
    build_material_evidence_registry,
)


ZENODO_RECORD_URL = "https://zenodo.org/records/14257632"
ZENODO_API_URL = "https://zenodo.org/api/records/14257632"
ZENODO_ARCHIVE_URL = (
    "https://zenodo.org/records/14257632/files/data_upload.zip?download=1"
)


def _sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def _sha256_json(value: Any) -> str:
    return _sha256_bytes(canonical_json_bytes(value))


def _float_summary(values: list[float], suffix: str) -> dict[str, int | float]:
    if len(values) < 1 or any(not math.isfinite(value) or value < 0 for value in values):
        raise ValueError("summary values must be finite and non-negative")
    return {
        "repetitions": len(values),
        f"minimum_{suffix}": min(values),
        f"median_{suffix}": statistics.median(values),
        f"maximum_{suffix}": max(values),
    }


def summarize_scale_repetitions(rows: list[dict]) -> dict:
    """Aggregate fresh-process scale rows without extrapolating a scaling law."""
    if len(rows) < 3:
        raise ValueError("at least three fresh-process repetitions are required")
    keys = ("node_count", "seed", "edge_probability", "edge_count")
    reference = {key: rows[0][key] for key in keys}
    for row in rows:
        if any(row[key] != reference[key] for key in keys):
            raise ValueError("scale repetition fixture drift")
    exact_statuses = {row["exact"]["stop_reason"] for row in rows}
    exact_states = {row["exact"]["states_evaluated"] for row in rows}
    exact_complete = {row["exact"]["complete"] for row in rows}
    heuristic_objectives = {row["heuristic"]["objective"] for row in rows}
    if len(exact_statuses) != 1 or len(exact_states) != 1 or len(exact_complete) != 1:
        raise ValueError("exact completion status drift across repetitions")
    if len(heuristic_objectives) != 1:
        raise ValueError("deterministic heuristic objective drift")
    bests = {row["exact"]["best_objective"] for row in rows}
    if len(bests) != 1:
        raise ValueError("best observed objective drift")
    complete = rows[0]["exact"]["complete"]
    return {
        "schema": "uqpu-cycle006-local-maxcut-repeated-scale-v1",
        **reference,
        "fresh_process_per_repetition": True,
        "exact": {
            "complete": complete,
            "stop_reason": rows[0]["exact"]["stop_reason"],
            "states_evaluated": rows[0]["exact"]["states_evaluated"],
            "total_state_space": rows[0]["exact"]["total_state_space"],
            "best_observed_objective": rows[0]["exact"]["best_objective"],
            "optimum_claim_allowed": complete,
            "elapsed": _float_summary(
                [row["exact"]["elapsed_seconds"] for row in rows], "seconds"
            ),
        },
        "heuristic": {
            "method": rows[0]["heuristic"]["method"],
            "restarts": rows[0]["heuristic"]["restarts"],
            "objective": rows[0]["heuristic"]["objective"],
            "objective_gap_to_exact": (
                rows[0]["heuristic"]["objective_gap_to_exact"] if complete else None
            ),
            "elapsed": _float_summary(
                [row["heuristic"]["elapsed_seconds"] for row in rows], "seconds"
            ),
        },
        "process_peak_rss": {
            **_float_summary(
                [float(row["process_peak_rss"]["value"]) for row in rows], "kib"
            ),
            "semantics": "fresh-process ru_maxrss high-water mark on Linux, not incremental solver memory",
        },
        "environment": rows[0]["environment"],
        "evidence_class": "REPEATED_LOCAL_CLASSICAL_SOFTWARE_SCREEN_NOT_SCALING_LAW",
        "non_claims": [
            "No asymptotic scaling fit or extrapolation is performed.",
            "A state-cap row reports best observed objective, not an optimum.",
            "Generated fixtures are not a competitive benchmark suite.",
            "No power, energy, GPU, provider, QPU, or hardware-neutral result is measured.",
        ],
    }


def validate_provider_request_shape(body: dict) -> list[str]:
    required_strings = (
        "action",
        "clientToken",
        "deviceArn",
        "outputS3Bucket",
        "outputS3KeyPrefix",
    )
    errors = []
    for field in required_strings:
        if not isinstance(body.get(field), str) or not body[field].strip():
            errors.append(f"{field}_missing_or_empty")
    shots = body.get("shots")
    if not isinstance(shots, int) or isinstance(shots, bool) or shots < 1:
        errors.append("shots_must_be_positive_integer")
    return errors


def build_provider_receipt_gate(manifest: dict) -> dict:
    dry_run = build_braket_dry_run_packet(manifest)
    action = dry_run["request_body"]["action"]
    structurally_complete_fixture = {
        "action": action,
        "clientToken": "SYNTHETIC-NONCE-NOT-SUBMITTED",
        "deviceArn": "SYNTHETIC-DEVICE-ARN-NOT-ROUTABLE",
        "outputS3Bucket": "synthetic-not-created",
        "outputS3KeyPrefix": "cycle006/schema-test-only",
        "shots": 8192,
    }
    negative_bodies = {
        "missing_account_fields": dry_run["request_body"],
        "zero_shots": {**structurally_complete_fixture, "shots": 0},
        "empty_action": {**structurally_complete_fixture, "action": ""},
        "boolean_shots": {**structurally_complete_fixture, "shots": True},
    }
    corpus = [
        {"case_id": case_id, "errors": validate_provider_request_shape(body)}
        for case_id, body in negative_bodies.items()
    ]
    if any(not row["errors"] for row in corpus):
        raise AssertionError("negative request corpus unexpectedly accepted")
    if validate_provider_request_shape(structurally_complete_fixture):
        raise AssertionError("synthetic complete shape fixture failed")
    receipt = {
        "receipt_id": None,
        "provider": None,
        "backend": None,
        "task_arn_or_job_id": None,
        "request_sha256": None,
        "response_sha256": None,
        "requested_at_utc": None,
        "completed_at_utc": None,
        "shots_requested": None,
        "shots_completed": None,
        "accepted_outputs": None,
        "billing_record_sha256": None,
        "billing_currency": None,
        "billing_amount": None,
    }
    return {
        "schema": "uqpu-cycle006-provider-request-and-receipt-gate-v1",
        "dry_run": dry_run,
        "negative_request_corpus": corpus,
        "synthetic_complete_shape": {
            "sha256": _sha256_json(structurally_complete_fixture),
            "shape_valid": True,
            "provider_validated": False,
            "submitted": False,
        },
        "execution_receipt_schema_fields": list(receipt),
        "execution_receipt": receipt,
        "receipt_complete": False,
        "submission_surface_present": False,
        "submission_authorized": False,
        "evidence_class": "LOCAL_NEGATIVE_VALIDATION_AND_RECEIPT_SCHEMA_NO_PROVIDER_EXECUTION",
    }


def benchmark_directory_durable_io(payload: dict, repetitions: int = 11) -> dict:
    """Measure atomic local publication with file and, where supported, directory fsync."""
    if type(repetitions) is not int or repetitions < 3:
        raise ValueError("repetitions must be an integer of at least three")
    encoded = canonical_json_bytes(payload)
    digest = _sha256_bytes(encoded)
    publish_ns = []
    read_ns = []
    directory_fsync_supported = hasattr(os, "O_DIRECTORY")
    directory_fsync_completed = directory_fsync_supported
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle006-") as temporary:
        directory = Path(temporary)
        final = directory / "published.json"
        for repetition in range(repetitions):
            staging = directory / f"staging-{repetition}.json"
            started = perf_counter_ns()
            with staging.open("wb") as handle:
                handle.write(encoded)
                handle.flush()
                os.fsync(handle.fileno())
            os.replace(staging, final)
            if directory_fsync_supported:
                try:
                    descriptor = os.open(directory, os.O_RDONLY | os.O_DIRECTORY)
                    try:
                        os.fsync(descriptor)
                    finally:
                        os.close(descriptor)
                except OSError:
                    directory_fsync_completed = False
            publish_ns.append(perf_counter_ns() - started)
            started = perf_counter_ns()
            recovered = final.read_bytes()
            read_ns.append(perf_counter_ns() - started)
            if _sha256_bytes(recovered) != digest:
                raise ValueError("published payload hash mismatch")
    peak_rss = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return {
        "schema": "uqpu-cycle006-local-atomic-directory-durability-v1",
        "payload": {"bytes": len(encoded), "sha256": digest},
        "timing": {
            "write_file_fsync_atomic_replace_directory_fsync": {
                "repetitions": repetitions,
                "minimum_ns": min(publish_ns),
                "median_ns": statistics.median(publish_ns),
                "maximum_ns": max(publish_ns),
            },
            "post_publish_read_uncontrolled_cache_state": {
                "repetitions": repetitions,
                "minimum_ns": min(read_ns),
                "median_ns": statistics.median(read_ns),
                "maximum_ns": max(read_ns),
            },
        },
        "durability_boundary": {
            "file_fsync_completed": True,
            "atomic_replace_completed": True,
            "directory_fsync_supported": directory_fsync_supported,
            "directory_fsync_completed": directory_fsync_completed,
            "device_flush_attested": False,
            "power_loss_survival_tested": False,
        },
        "cache_control": {
            "method": None,
            "supported_in_unprivileged_protocol": False,
            "attempted": False,
            "reason": "Dropping or proving kernel cache state requires host-level controls unavailable to this portable test.",
        },
        "process_peak_rss": {
            "value": peak_rss,
            "unit": "KiB on Linux; platform-dependent elsewhere",
            "semantics": "fresh worker process high-water mark when invoked through the Cycle 006 runner",
        },
        "evidence_class": "LOCAL_FILE_AND_DIRECTORY_FSYNC_MEASUREMENT_NOT_STORAGE_SERVICE_DURABILITY",
        "non_claims": [
            "No device flush or power-loss survival is verified.",
            "The read is not labeled cold or warm.",
            "No provider, cloud, network, QPU, energy, or device-memory measurement is inferred.",
        ],
    }


def parse_zip_central_directory_tail(
    tail_bytes: bytes, *, range_start: int, archive_size: int
) -> dict:
    """Parse a conventional single-disk ZIP EOCD and central directory from a tail range."""
    if range_start < 0 or archive_size <= range_start:
        raise ValueError("invalid archive range")
    if range_start + len(tail_bytes) != archive_size:
        raise ValueError("tail range must end at the archive boundary")
    signature = b"PK\x05\x06"
    eocd_index = tail_bytes.rfind(signature)
    if eocd_index < 0 or len(tail_bytes) - eocd_index < 22:
        raise ValueError("ZIP EOCD not present in supplied tail")
    (
        _, disk, central_disk, entries_disk, entries_total, central_size,
        central_offset, comment_length,
    ) = struct.unpack_from("<4s4H2LH", tail_bytes, eocd_index)
    if disk or central_disk or entries_disk != entries_total:
        raise ValueError("multi-disk ZIP is outside the protocol")
    if len(tail_bytes) - eocd_index - 22 != comment_length:
        raise ValueError("EOCD comment length mismatch")
    central_start = central_offset - range_start
    central_end = central_start + central_size
    if central_start < 0 or central_end > eocd_index:
        raise ValueError("central directory is not fully covered by tail range")
    entries = []
    position = central_start
    while len(entries) < entries_total:
        if tail_bytes[position:position + 4] != b"PK\x01\x02":
            raise ValueError(f"invalid central-directory signature at row {len(entries)}")
        values = struct.unpack_from("<4s6H3L5H2L", tail_bytes, position)
        (
            _, _, _, flag, method, _, _, crc32, compressed_size,
            uncompressed_size, name_length, extra_length, entry_comment_length,
            _, _, _, local_header_offset,
        ) = values
        name_bytes = tail_bytes[position + 46:position + 46 + name_length]
        encoding = "utf-8" if flag & 0x800 else "cp437"
        path = name_bytes.decode(encoding)
        pure = PurePosixPath(path)
        if pure.is_absolute() or ".." in pure.parts:
            raise ValueError("unsafe archive path")
        entries.append({
            "path": path,
            "directory": path.endswith("/"),
            "compression_method": method,
            "crc32": f"{crc32:08x}",
            "compressed_size": compressed_size,
            "uncompressed_size": uncompressed_size,
            "local_header_offset": local_header_offset,
        })
        position += 46 + name_length + extra_length + entry_comment_length
    if position != central_end:
        raise ValueError("central directory size or entry count mismatch")
    files = [entry for entry in entries if not entry["directory"]]
    methods: dict[str, int] = {}
    for entry in entries:
        key = str(entry["compression_method"])
        methods[key] = methods.get(key, 0) + 1
    return {
        "tail_range": {
            "start": range_start,
            "end_inclusive": archive_size - 1,
            "bytes": len(tail_bytes),
            "sha256": _sha256_bytes(tail_bytes),
        },
        "eocd": {
            "disk": disk,
            "central_directory_disk": central_disk,
            "entries": entries_total,
            "central_directory_size": central_size,
            "central_directory_offset": central_offset,
            "comment_length": comment_length,
        },
        "inventory_summary": {
            "entries": len(entries),
            "files": len(files),
            "directories": len(entries) - len(files),
            "compressed_file_bytes_sum": sum(entry["compressed_size"] for entry in files),
            "uncompressed_file_bytes_sum": sum(entry["uncompressed_size"] for entry in files),
            "compression_method_entry_counts": methods,
        },
        "entries": entries,
    }


def recover_zip_member_from_range(range_bytes: bytes, expected_path: str) -> dict:
    if len(range_bytes) < 30 or range_bytes[:4] != b"PK\x03\x04":
        raise ValueError("local ZIP header missing")
    (
        _, _, flag, method, _, _, crc32, compressed_size, uncompressed_size,
        name_length, extra_length,
    ) = struct.unpack_from("<4s5H3L2H", range_bytes, 0)
    name = range_bytes[30:30 + name_length].decode("utf-8" if flag & 0x800 else "cp437")
    if name != expected_path:
        raise ValueError("local member path mismatch")
    start = 30 + name_length + extra_length
    compressed = range_bytes[start:start + compressed_size]
    if len(compressed) != compressed_size:
        raise ValueError("member range does not cover compressed payload")
    if method == 0:
        raw = compressed
    elif method == 8:
        raw = zlib.decompress(compressed, -15)
    else:
        raise ValueError("unsupported ZIP compression method")
    actual_crc = binascii.crc32(raw) & 0xFFFFFFFF
    if len(raw) != uncompressed_size or actual_crc != crc32:
        raise ValueError("member size or CRC mismatch")
    return {
        "path": name,
        "compression_method": method,
        "compressed_size": compressed_size,
        "uncompressed_size": uncompressed_size,
        "crc32": f"{crc32:08x}",
        "sha256": _sha256_bytes(raw),
        "content": raw,
    }


def build_zenodo_range_evidence(
    api_record: dict,
    tail_bytes: bytes,
    *,
    tail_range_start: int,
    readme_range_bytes: bytes,
    readme_range_start: int,
    http_observations: dict,
    capture_code_commit: str,
) -> dict:
    if not re.fullmatch(r"[0-9a-f]{40}", capture_code_commit):
        raise ValueError("capture_code_commit must be a full lowercase Git SHA-1")
    files = api_record.get("files", [])
    if len(files) != 1 or files[0].get("key") != "data_upload.zip":
        raise ValueError("unexpected Zenodo file inventory")
    archive = files[0]
    archive_size = archive["size"]
    central = parse_zip_central_directory_tail(
        tail_bytes, range_start=tail_range_start, archive_size=archive_size
    )
    readme_entry = next(
        (entry for entry in central["entries"] if entry["path"] == "data_upload/README.md"),
        None,
    )
    if readme_entry is None or readme_entry["local_header_offset"] != readme_range_start:
        raise ValueError("README central-directory/local-range mismatch")
    recovered = recover_zip_member_from_range(
        readme_range_bytes, "data_upload/README.md"
    )
    if recovered["crc32"] != readme_entry["crc32"]:
        raise ValueError("README central/local CRC mismatch")
    readme = recovered.pop("content").decode("utf-8")
    required_phrases = [
        "pandas data frames",
        'pd.read_parquet("first_d3_bit_flip")',
        "nbar: storage mean photon number",
        "num_cycles: The number of cycles",
        "The logical state is the xor",
        "The syndromes take values of 0,1, and 2",
        "syndrome state 0 represents even, 1 represents an erasure, and 2 represents odd",
    ]
    missing = [phrase for phrase in required_phrases if phrase not in readme]
    if missing:
        raise ValueError(f"README semantic anchors missing: {missing}")
    metadata = api_record["metadata"]
    return {
        "schema": "uqpu-cycle006-zenodo-range-and-central-directory-evidence-v1",
        "capture_code_commit": capture_code_commit,
        "source": {
            "record_url": ZENODO_RECORD_URL,
            "api_url": ZENODO_API_URL,
            "archive_url": ZENODO_ARCHIVE_URL,
            "access_date": "2026-09-28",
            "api_response_sha256": http_observations["api_response_sha256"],
            "publication_date": metadata["publication_date"],
            "title": metadata["title"],
            "resource_type": metadata["resource_type"],
            "access_right": metadata.get("access_right"),
            "license": metadata.get("license"),
        },
        "archive": {
            "name": archive["key"],
            "bytes": archive_size,
            "publisher_checksum": archive["checksum"],
            "full_archive_downloaded": False,
            "full_archive_checksum_recomputed": False,
            "http_observations": http_observations,
        },
        "central_directory": central,
        "readme_range": {
            "range_start": readme_range_start,
            "returned_bytes": len(readme_range_bytes),
            "range_sha256": _sha256_bytes(readme_range_bytes),
            "member": recovered,
        },
        "readme_semantics": {
            "cycle_length_microseconds": 2.8,
            "bit_flip": {
                "format": "Apache Parquet readable as pandas DataFrame",
                "index_fields": ["nbar", "S{i}_initial_state", "num_cycles", "shot"],
                "columns": "final state of each storage mode plus logical XOR state",
                "storage_state_encoding": {"0": "|alpha>", "1": "|-alpha>"},
            },
            "phase_flip": {
                "format": "Apache Parquet readable as pandas DataFrame",
                "hierarchy": ["code section", "storage mean photon number", "number of cycles"],
                "axis": "experiment shot",
                "column_families": [
                    "S{i}_initial_state", "S{i}_final_state", "A{i}_syndrome_{j}"
                ],
                "storage_parity_encoding": {"0": "even", "1": "odd"},
                "syndrome_encoding": {"0": "even", "1": "erasure", "2": "odd"},
                "cycle_enumerator_file": "all_cycle_numbers",
            },
        },
        "analysis_state": {
            "parquet_payload_retrieved": False,
            "data_values_read": False,
            "basis_resolved_rates_extracted": False,
            "uncertainty_definition_extracted": False,
            "project_reproduction": False,
        },
        "evidence_class": "PRIMARY_API_PLUS_RANGE_VERIFIED_ARCHIVE_METADATA_AND_README_NOT_DATA_ANALYSIS",
        "non_claims": [
            "Only the archive tail and README member range were retrieved.",
            "No Parquet payload, experimental value, fit, uncertainty, or confidence interval was analyzed.",
            "The publisher MD5 was not recomputed over the full archive.",
            "No project device, logical-memory performance, or physical-law result is created.",
        ],
    }


def validate_material_registry_v2(registry: dict, *, as_of: date) -> dict:
    errors_by_id: dict[str, list[str]] = {}
    seen = set()
    study_lot = registry.get("study_lot_id")
    for slot in registry.get("slots", []):
        prerequisite_id = slot.get("prerequisite_id")
        errors = []
        if not prerequisite_id or prerequisite_id in seen:
            errors.append("missing_or_duplicate_prerequisite_id")
        seen.add(prerequisite_id)
        evidence = slot.get("evidence", {})
        digest = evidence.get("sha256")
        if not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest):
            errors.append("sha256_missing_or_malformed")
        expected_uri = f"artifact://sha256/{digest}" if isinstance(digest, str) else None
        if evidence.get("artifact_uri") != expected_uri:
            errors.append("artifact_uri_not_content_addressed")
        for field in ("issuer_or_operator", "date", "reviewer", "scope_id"):
            if not evidence.get(field):
                errors.append(f"{field}_missing")
        if evidence.get("scope_id") not in (None, registry.get("study_id")):
            errors.append("scope_id_mismatch")
        if prerequisite_id in {"DMF-PR-02", "DMF-PR-03"}:
            if not study_lot:
                errors.append("study_lot_id_missing")
            if evidence.get("sample_lot_id") != study_lot:
                errors.append("sample_lot_id_mismatch")
        if prerequisite_id in {"DMF-PR-01", "DMF-PR-07"}:
            valid_until = evidence.get("valid_until")
            try:
                parsed = date.fromisoformat(valid_until) if valid_until else None
            except ValueError:
                parsed = None
            if parsed is None:
                errors.append("valid_until_missing_or_invalid")
            elif parsed < as_of:
                errors.append("evidence_expired")
        errors_by_id[prerequisite_id or "<missing>"] = errors
    required = {f"DMF-PR-{index:02d}" for index in range(1, 10)}
    missing_ids = sorted(required - seen)
    for prerequisite_id in missing_ids:
        errors_by_id[prerequisite_id] = ["slot_missing"]
    passing = sorted(key for key, errors in errors_by_id.items() if not errors)
    return {
        "schema": "uqpu-cycle006-material-registry-validation-v2",
        "as_of": as_of.isoformat(),
        "errors_by_prerequisite": errors_by_id,
        "passing_prerequisite_ids": passing,
        "required_count": 9,
        "passing_count": len(passing),
        "ready": len(passing) == 9,
        "fabrication_authorized": False,
        "evidence_class": "FAIL_CLOSED_REGISTRY_VALIDATION_NO_MATERIAL_EVIDENCE",
    }


def _valid_cost_fixture() -> dict:
    provider = "SYNTHETIC-PROVIDER"
    execution = "SYNTHETIC-EXECUTION"
    return {
        "currency": "USD",
        "execution_identity": {
            "provider_id": provider,
            "execution_id": execution,
            "workload_contract_id": "SYNTHETIC-CONTRACT",
        },
        "components": {
            name: {
                "amount": 1.0,
                "currency": "USD",
                "provider_id": provider,
                "execution_id": execution,
            }
            for name in COST_COMPONENTS
        },
        "accepted_outputs": {
            "count": 5,
            "provider_id": provider,
            "execution_id": execution,
            "workload_contract_id": "SYNTHETIC-CONTRACT",
        },
        "classical_baseline": {
            "matched": True,
            "workload_contract_id": "SYNTHETIC-CONTRACT",
        },
    }


def validate_complete_cost_v2(ledger: dict) -> dict:
    errors = []
    identity = ledger.get("execution_identity", {})
    provider = identity.get("provider_id")
    execution = identity.get("execution_id")
    contract = identity.get("workload_contract_id")
    if not provider:
        errors.append("provider_id_missing")
    if not execution:
        errors.append("execution_id_missing")
    if not contract:
        errors.append("workload_contract_id_missing")
    expected_currency = ledger.get("currency")
    if not expected_currency:
        errors.append("ledger_currency_missing")
    total = 0.0
    components = ledger.get("components", {})
    for name in COST_COMPONENTS:
        component = components.get(name)
        if not isinstance(component, dict):
            errors.append(f"component_missing:{name}")
            continue
        amount = component.get("amount")
        if (
            not isinstance(amount, (int, float))
            or isinstance(amount, bool)
            or not math.isfinite(amount)
            or amount < 0
        ):
            errors.append(f"amount_invalid:{name}")
        else:
            total += float(amount)
        if component.get("currency") != expected_currency:
            errors.append(f"currency_mismatch:{name}")
        if component.get("provider_id") != provider:
            errors.append(f"provider_mismatch:{name}")
        if component.get("execution_id") != execution:
            errors.append(f"execution_mismatch:{name}")
    accepted = ledger.get("accepted_outputs", {})
    count = accepted.get("count")
    if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
        errors.append("accepted_output_count_invalid")
    for field, expected in (
        ("provider_id", provider),
        ("execution_id", execution),
        ("workload_contract_id", contract),
    ):
        if accepted.get(field) != expected:
            errors.append(f"accepted_outputs_{field}_mismatch")
    baseline = ledger.get("classical_baseline", {})
    if baseline.get("matched") is not True:
        errors.append("matched_classical_baseline_missing")
    if baseline.get("workload_contract_id") != contract:
        errors.append("classical_baseline_contract_mismatch")
    complete = not errors
    return {
        "complete": complete,
        "errors": errors,
        "total_cost": total if complete else None,
        "cost_per_accepted_output": total / count if complete else None,
        "currency": expected_currency if complete else None,
        "refusal_active": not complete,
    }


def build_cost_adversarial_gate() -> dict:
    valid = _valid_cost_fixture()
    cases = {}
    missing = deepcopy(valid)
    del missing["components"]["storage"]
    cases["missing_component"] = missing
    negative = deepcopy(valid)
    negative["components"]["labor"]["amount"] = -1.0
    cases["negative_amount"] = negative
    non_finite = deepcopy(valid)
    non_finite["components"]["queue"]["amount"] = "NaN"
    cases["non_finite_or_non_numeric_amount"] = non_finite
    mixed_currency = deepcopy(valid)
    mixed_currency["components"]["network_transfer"]["currency"] = "EUR"
    cases["mixed_currency"] = mixed_currency
    cross_provider = deepcopy(valid)
    cross_provider["components"]["provider_actual_bill"]["provider_id"] = "OTHER"
    cases["cross_provider"] = cross_provider
    acceptance_mismatch = deepcopy(valid)
    acceptance_mismatch["accepted_outputs"]["execution_id"] = "OTHER"
    cases["unmatched_acceptance"] = acceptance_mismatch
    baseline_mismatch = deepcopy(valid)
    baseline_mismatch["classical_baseline"]["workload_contract_id"] = "OTHER"
    cases["unmatched_baseline"] = baseline_mismatch
    corpus = []
    for case_id, ledger in cases.items():
        result = validate_complete_cost_v2(ledger)
        if result["complete"]:
            raise AssertionError(f"adversarial cost case accepted: {case_id}")
        corpus.append({"case_id": case_id, "errors": result["errors"]})
    valid_result = validate_complete_cost_v2(valid)
    if not valid_result["complete"]:
        raise AssertionError("synthetic arithmetic control did not pass")
    current = {
        "currency": None,
        "execution_identity": {},
        "components": {},
        "accepted_outputs": {},
        "classical_baseline": {},
    }
    return {
        "schema": "uqpu-cycle006-cost-adversarial-gate-v2",
        "current_evidence": validate_complete_cost_v2(current),
        "negative_corpus": corpus,
        "synthetic_arithmetic_control": {
            **valid_result,
            "evidence_class": "SYNTHETIC_SCHEMA_ARITHMETIC_NOT_COMMERCIAL_EVIDENCE",
        },
        "rg028_status": "OPEN_DATA_CREDENTIAL_AUTHORIZATION_AND_COMPLETENESS_BLOCKED",
        "evidence_class": "ADVERSARIAL_COMPLETE_COST_VALIDATION_NO_BILL_OR_ECONOMIC_RESULT",
    }


def _chain_event(event: dict) -> dict:
    row = dict(event)
    row["event_sha256"] = _sha256_json(row)
    return row


def build_synthetic_custody_fixture() -> dict:
    stages = [
        "feedstock_receipt", "feedstock_preparation", "resin_mix",
        "cure", "coupon_metrology", "vna_measurement",
    ]
    events = []
    previous_hash = "0" * 64
    previous_lot = "SYN-LOT-0"
    for index, stage in enumerate(stages, start=1):
        output_lot = f"SYN-LOT-{index}"
        event = _chain_event({
            "event_id": f"SYN-EVENT-{index}",
            "stage": stage,
            "timestamp_utc": f"2026-09-28T00:{index:02d}:00+00:00",
            "actor": f"synthetic-actor-{index}",
            "input_lot_ids": [previous_lot],
            "output_lot_ids": [output_lot],
            "procedure_revision": "SYNTHETIC-V1",
            "artifact_sha256": hashlib.sha256(f"synthetic-{index}".encode()).hexdigest(),
            "previous_event_sha256": previous_hash,
        })
        events.append(event)
        previous_hash = event["event_sha256"]
        previous_lot = output_lot
    return {
        "events": events,
        "measurement_time_utc": "2026-09-28T00:06:00+00:00",
        "calibration": {
            "certificate_sha256": hashlib.sha256(b"synthetic-calibration").hexdigest(),
            "valid_from": "2026-09-01T00:00:00+00:00",
            "valid_until": "2026-10-01T00:00:00+00:00",
            "instrument_session_id": "SYNTHETIC-SESSION",
        },
        "matched_control": {
            "control_coupon_id": "SYNTHETIC-CONTROL",
            "same_protocol_revision": True,
            "instrument_session_id": "SYNTHETIC-SESSION",
        },
        "uncertainty": {
            "unit": "dB",
            "components_standard": [0.1, 0.2, 0.05],
            "coverage_factor": 2.0,
        },
    }


def validate_custody_fixture(fixture: dict) -> list[str]:
    errors = []
    required_stages = [
        "feedstock_receipt", "feedstock_preparation", "resin_mix",
        "cure", "coupon_metrology", "vna_measurement",
    ]
    events = fixture.get("events", [])
    if [event.get("stage") for event in events] != required_stages:
        errors.append("stage_order_or_completeness_failure")
    previous_hash = "0" * 64
    previous_outputs = None
    previous_time = None
    for event in events:
        stored_hash = event.get("event_sha256")
        unhashed = {key: value for key, value in event.items() if key != "event_sha256"}
        if stored_hash != _sha256_json(unhashed):
            errors.append(f"event_hash_mismatch:{event.get('event_id')}")
        if event.get("previous_event_sha256") != previous_hash:
            errors.append(f"previous_hash_mismatch:{event.get('event_id')}")
        if previous_outputs is not None and not (
            set(event.get("input_lot_ids", [])) & previous_outputs
        ):
            errors.append(f"lot_chain_break:{event.get('event_id')}")
        try:
            timestamp = datetime.fromisoformat(event["timestamp_utc"])
        except (KeyError, ValueError):
            timestamp = None
            errors.append(f"timestamp_invalid:{event.get('event_id')}")
        if timestamp is not None and previous_time is not None and timestamp <= previous_time:
            errors.append(f"timestamp_not_increasing:{event.get('event_id')}")
        if timestamp is not None:
            previous_time = timestamp
        previous_hash = stored_hash
        previous_outputs = set(event.get("output_lot_ids", []))
    try:
        measurement = datetime.fromisoformat(fixture["measurement_time_utc"])
        valid_from = datetime.fromisoformat(fixture["calibration"]["valid_from"])
        valid_until = datetime.fromisoformat(fixture["calibration"]["valid_until"])
        if not valid_from <= measurement <= valid_until:
            errors.append("calibration_not_valid_at_measurement")
    except (KeyError, ValueError):
        errors.append("calibration_or_measurement_time_invalid")
    calibration_session = fixture.get("calibration", {}).get("instrument_session_id")
    control = fixture.get("matched_control", {})
    if control.get("same_protocol_revision") is not True:
        errors.append("matched_control_protocol_mismatch")
    if control.get("instrument_session_id") != calibration_session:
        errors.append("matched_control_instrument_session_mismatch")
    uncertainty = fixture.get("uncertainty", {})
    components = uncertainty.get("components_standard", [])
    coverage = uncertainty.get("coverage_factor")
    if (
        not components
        or any(not isinstance(value, (int, float)) or value < 0 for value in components)
        or not isinstance(coverage, (int, float))
        or coverage <= 0
        or not uncertainty.get("unit")
    ):
        errors.append("uncertainty_budget_invalid")
    return errors


def build_custody_adversarial_gate() -> dict:
    valid = build_synthetic_custody_fixture()
    if validate_custody_fixture(valid):
        raise AssertionError("synthetic valid custody control failed")
    cases = {}
    broken = deepcopy(valid)
    broken["events"][3]["previous_event_sha256"] = "f" * 64
    cases["broken_hash_chain"] = broken
    expired = deepcopy(valid)
    expired["calibration"]["valid_until"] = "2026-09-27T00:00:00+00:00"
    cases["expired_calibration"] = expired
    unmatched = deepcopy(valid)
    unmatched["matched_control"]["instrument_session_id"] = "OTHER"
    cases["unmatched_control"] = unmatched
    results = []
    for case_id, fixture in cases.items():
        errors = validate_custody_fixture(fixture)
        if not errors:
            raise AssertionError(f"custody adversarial case accepted: {case_id}")
        results.append({"case_id": case_id, "errors": errors})
    return {
        "schema": "uqpu-cycle006-custody-dag-and-uncertainty-gate-v1",
        "synthetic_valid_control_sha256": _sha256_json(valid),
        "synthetic_valid_control_errors": [],
        "negative_corpus": results,
        "operational_events": [],
        "operational_ready": False,
        "evidence_class": "SYNTHETIC_CUSTODY_VALIDATION_NO_PHYSICAL_SAMPLE_OR_MEASUREMENT",
    }


def derive_capital_blockers(
    dependency_graph: dict, evidence_status: dict[str, bool]
) -> dict:
    rows = []
    for gate in dependency_graph["gates"]:
        unresolved = [
            prerequisite
            for prerequisite in gate["prerequisite_ids"]
            if evidence_status.get(prerequisite) is not True
        ]
        rows.append({
            "gate_id": gate["gate_id"],
            "prerequisite_ids": gate["prerequisite_ids"],
            "unresolved_prerequisite_ids": unresolved,
            "all_prerequisites_satisfied": not unresolved,
            "status": "NOT_AUTHORIZED",
            "capital_at_risk_thb": None,
            "decision": None,
        })
    return {
        "schema": "uqpu-cycle006-derived-capital-blockers-v1",
        "gates": rows,
        "funding_or_purchase_authorized": False,
        "derivation_rule": "Any unresolved prerequisite forces NOT_AUTHORIZED; this research workflow cannot authorize capital even when a schema passes.",
        "evidence_class": "DERIVED_BLOCKER_LIST_NO_FINANCIAL_DECISION",
    }


def _append_only_events(actor: str, actions: list[tuple[str, str | None]]) -> list[dict]:
    previous = "0" * 64
    events = []
    for sequence, (action, artifact_sha256) in enumerate(actions, start=1):
        event = {
            "sequence": sequence,
            "actor": actor,
            "action": action,
            "artifact_sha256": artifact_sha256,
            "previous_event_sha256": previous,
        }
        event["event_sha256"] = _sha256_json(event)
        previous = event["event_sha256"]
        events.append(event)
    return events


def build_scm_role_packages(cycle005_scm: dict) -> tuple[dict, dict, dict]:
    score_commitment = cycle005_scm["pre_registered_reveal_rule"][
        "score_commitment_sha256"
    ]
    public_sha = cycle005_scm["input_public_file_sha256"]
    truth_sha = cycle005_scm["input_custodian_file_sha256"]
    scorer_events = _append_only_events(
        "synthetic_scorer_role",
        [
            ("RECEIVE_PUBLIC_REFERENCE", public_sha),
            ("COMMIT_SCORES", score_commitment),
            ("CLOSE_SCORING", score_commitment),
        ],
    )
    scorer = {
        "schema": "uqpu-cycle006-scm-scorer-role-package-v1",
        "cycle005_public_file_sha256": public_sha,
        "score_commitment_sha256": score_commitment,
        "events": scorer_events,
        "condition_labels_or_truth_present": False,
        "role": "SYNTHETIC_SCORER",
        "operating_system_or_account_isolation": False,
    }
    scorer_sha = _sha256_json(scorer)
    custodian_events = _append_only_events(
        "synthetic_custodian_role",
        [
            ("RECEIVE_SCORER_CLOSE_REFERENCE", scorer_events[-1]["event_sha256"]),
            ("AUTHORIZE_SYNTHETIC_REVEAL", scorer_sha),
            ("REVEAL_EXISTING_SYNTHETIC_TRUTH_REFERENCE", truth_sha),
        ],
    )
    custodian = {
        "schema": "uqpu-cycle006-scm-custodian-role-package-v1",
        "cycle005_truth_file_sha256": truth_sha,
        "required_scorer_final_event_sha256": scorer_events[-1]["event_sha256"],
        "scorer_package_canonical_sha256": scorer_sha,
        "events": custodian_events,
        "role": "SYNTHETIC_CUSTODIAN",
        "operating_system_or_account_isolation": False,
    }
    audit = {
        "schema": "uqpu-cycle006-scm-reveal-order-audit-v1",
        "scorer_package_canonical_sha256": scorer_sha,
        "custodian_package_canonical_sha256": _sha256_json(custodian),
        "scorer_final_event_sha256": scorer_events[-1]["event_sha256"],
        "custodian_first_event_artifact_sha256": custodian_events[0]["artifact_sha256"],
        "reveal_order_valid": True,
        "separate_repository_or_site": False,
        "human_or_physical_data": False,
        "evidence_class": "SYNTHETIC_SEPARATE_ROLE_PACKAGES_NOT_OPERATIONAL_BLINDING",
    }
    errors = validate_scm_role_packages(scorer, custodian, audit)
    if errors:
        raise AssertionError(f"generated SCM packages failed validation: {errors}")
    return scorer, custodian, audit


def _validate_event_chain(events: list[dict]) -> list[str]:
    errors = []
    previous = "0" * 64
    for expected_sequence, event in enumerate(events, start=1):
        if event.get("sequence") != expected_sequence:
            errors.append("sequence_mismatch")
        if event.get("previous_event_sha256") != previous:
            errors.append("previous_event_hash_mismatch")
        unhashed = {key: value for key, value in event.items() if key != "event_sha256"}
        if event.get("event_sha256") != _sha256_json(unhashed):
            errors.append("event_hash_mismatch")
        previous = event.get("event_sha256")
    return errors


def validate_scm_role_packages(scorer: dict, custodian: dict, audit: dict) -> list[str]:
    errors = []
    errors.extend(f"scorer:{error}" for error in _validate_event_chain(scorer.get("events", [])))
    errors.extend(
        f"custodian:{error}" for error in _validate_event_chain(custodian.get("events", []))
    )
    if scorer.get("condition_labels_or_truth_present") is not False:
        errors.append("truth_or_condition_leak_in_scorer")
    scorer_sha = _sha256_json(scorer)
    custodian_sha = _sha256_json(custodian)
    scorer_final = scorer.get("events", [{}])[-1].get("event_sha256")
    if custodian.get("required_scorer_final_event_sha256") != scorer_final:
        errors.append("custodian_scorer_close_reference_mismatch")
    if custodian.get("scorer_package_canonical_sha256") != scorer_sha:
        errors.append("custodian_scorer_package_hash_mismatch")
    if custodian.get("events", [{}])[0].get("artifact_sha256") != scorer_final:
        errors.append("reveal_before_or_without_scorer_close")
    if audit.get("scorer_package_canonical_sha256") != scorer_sha:
        errors.append("audit_scorer_hash_mismatch")
    if audit.get("custodian_package_canonical_sha256") != custodian_sha:
        errors.append("audit_custodian_hash_mismatch")
    if audit.get("scorer_final_event_sha256") != scorer_final:
        errors.append("audit_scorer_final_event_mismatch")
    return errors


def freeze_ai_dataset_contract(
    batch039: dict, *, baseline_file_sha256: str, generator_module_sha256: str
) -> dict:
    workload = batch039["workload"]
    config = BaselineConfig(
        train_examples=workload["train_examples"],
        test_examples=workload["held_out_examples"],
        hidden_width=16,
        epochs=workload["epochs"],
        learning_rate=0.2,
        seed=workload["seed"],
    )
    def freeze(rows):
        return [
            {"x1_hex": x1.hex(), "x2_hex": x2.hex(), "label": int(label)}
            for x1, x2, label in rows
        ]
    train = freeze(_dataset(config.train_examples, config.seed + 1))
    held_out = freeze(_dataset(config.test_examples, config.seed + 2))
    gate = {
        "schema": "uqpu-cycle006-ai-dataset-content-contract-v1",
        "baseline_file_sha256": baseline_file_sha256,
        "generator_module_sha256": generator_module_sha256,
        "generator": "random.Random(seed).uniform(-1,1); label=1 iff x1*x2>=0",
        "seed_policy": {"base": config.seed, "train": config.seed + 1, "held_out": config.seed + 2},
        "representation": "IEEE-754 Python float.hex strings plus integer label",
        "train": {"examples": len(train), "canonical_sha256": _sha256_json(train)},
        "held_out": {
            "examples": len(held_out),
            "canonical_sha256": _sha256_json(held_out),
        },
        "quality_gate": {
            "held_out_accuracy_minimum": batch039["accepted_capability_contract"][
                "held_out_accuracy_minimum"
            ],
            "held_out_binary_cross_entropy_maximum": batch039[
                "accepted_capability_contract"
            ]["held_out_binary_cross_entropy_maximum"],
        },
        "candidate_result": None,
        "measured_candidate_cost": None,
        "measured_candidate_energy": None,
        "evidence_class": "FROZEN_TOY_DATASET_CONTENT_HASHES_NO_CANDIDATE_RESULT",
    }
    return gate


_QASM_LINE_PATTERNS = (
    ("header", re.compile(r"OPENQASM 3\.0;")),
    ("include", re.compile(r'include "stdgates\.inc";')),
    ("qubit", re.compile(r"qubit\[(\d+)\] q;")),
    ("bit", re.compile(r"bit\[(\d+)\] c;")),
    ("h", re.compile(r"h q\[(\d+)\];")),
    ("cx", re.compile(r"cx q\[(\d+)\], q\[(\d+)\];")),
    ("rz", re.compile(r"rz\(([-+0-9.eE]+)\) q\[(\d+)\];")),
    ("rx", re.compile(r"rx\(([-+0-9.eE]+)\) q\[(\d+)\];")),
    ("measure", re.compile(r"c\[(\d+)\] = measure q\[(\d+)\];")),
)


def parse_frozen_qasm_subset(text: str) -> list[dict]:
    statements = []
    for line_number, raw in enumerate(text.splitlines(), start=1):
        line = raw.strip()
        if not line:
            continue
        for kind, pattern in _QASM_LINE_PATTERNS:
            match = pattern.fullmatch(line)
            if match:
                statements.append({"kind": kind, "arguments": list(match.groups())})
                break
        else:
            raise ValueError(f"unsupported QASM statement at line {line_number}: {line}")
    return statements


def dump_frozen_qasm_subset(statements: list[dict]) -> str:
    lines = []
    for statement in statements:
        kind = statement["kind"]
        args = statement["arguments"]
        if kind == "header":
            line = "OPENQASM 3.0;"
        elif kind == "include":
            line = 'include "stdgates.inc";'
        elif kind == "qubit":
            line = f"qubit[{args[0]}] q;"
        elif kind == "bit":
            line = f"bit[{args[0]}] c;"
        elif kind == "h":
            line = f"h q[{args[0]}];"
        elif kind == "cx":
            line = f"cx q[{args[0]}], q[{args[1]}];"
        elif kind in {"rz", "rx"}:
            line = f"{kind}({args[0]}) q[{args[1]}];"
        elif kind == "measure":
            line = f"c[{args[0]}] = measure q[{args[1]}];"
        else:
            raise ValueError(f"unsupported AST kind: {kind}")
        lines.append(line)
    return "\n".join(lines) + "\n"


def build_qasm_roundtrip_gate(manifest: dict) -> dict:
    rows = []
    for candidate in manifest["lane_a_b_c_qos"]["paired_circuits"]:
        original = candidate["openqasm_3"]
        first_ast = parse_frozen_qasm_subset(original)
        canonical = dump_frozen_qasm_subset(first_ast)
        second_ast = parse_frozen_qasm_subset(canonical)
        if first_ast != second_ast:
            raise AssertionError("QASM subset AST round-trip drift")
        rows.append({
            "candidate_id": candidate["candidate_id"],
            "input_sha256": _sha256_bytes(original.encode()),
            "canonical_sha256": _sha256_bytes(canonical.encode()),
            "canonical_equals_input": canonical == original,
            "ast_sha256": _sha256_json(first_ast),
            "statement_count": len(first_ast),
            "roundtrip_ast_equal": True,
        })
    transpile_receipt = {
        "provider": None,
        "backend": None,
        "sdk_and_version": None,
        "calibration_timestamp": None,
        "input_qasm_sha256": None,
        "transpiled_artifact_sha256": None,
        "layout": None,
        "physical_depth": None,
        "physical_two_qubit_gate_count": None,
        "duration_seconds": None,
    }
    return {
        "schema": "uqpu-cycle006-qasm-subset-roundtrip-and-transpile-receipt-v1",
        "grammar_scope": "frozen ER6 OpenQASM 3 subset only",
        "rows": rows,
        "all_roundtrips_passed": all(row["roundtrip_ast_equal"] for row in rows),
        "provider_transpile_receipt": transpile_receipt,
        "provider_transpile_receipt_complete": False,
        "hardware_executed": False,
        "evidence_class": "CANONICAL_SUBSET_AST_ROUNDTRIP_NOT_GENERAL_PARSER_OR_PROVIDER_TRANSPILE",
    }


def validate_unified_math_registries(registry: dict, scm_registry: dict) -> dict:
    """Fail closed on missing goal/equation/type links in the Cycle 006 formalism."""
    expected_lanes = {
        "A", "B", "C", "D", "E", "F", "G", "H",
        "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
    }
    expected_services = {
        "graphics and rendering",
        "ray and path tracing",
        "AI training",
        "AI inference",
        "tensor and matrix computation",
        "scientific and HPC workloads",
        "simulation",
        "signal, image, and video processing",
        "data analytics",
        "general-purpose parallel compute",
        "optimization and search",
        "arbitrary-kernel fallback",
    }
    errors: list[str] = []
    if registry.get("schema") != "uqpu-unified-mathematical-goal-registry-v0.1":
        errors.append("unified_registry_schema_mismatch")
    if set(registry.get("lanes", [])) != expected_lanes:
        errors.append("unified_registry_lane_set_mismatch")
    if set(registry.get("service_portfolio", [])) != expected_services:
        errors.append("service_portfolio_mismatch")

    equations = registry.get("equations", [])
    equation_ids = [row.get("equation_id") for row in equations]
    expected_equations = {f"UMRL-{index:03d}" for index in range(1, 31)}
    if len(equation_ids) != len(set(equation_ids)):
        errors.append("duplicate_umrl_equation_id")
    if set(equation_ids) != expected_equations:
        errors.append("umrl_equation_set_mismatch")
    equation_owner_coverage = set()
    required_equation_fields = {
        "equation_id", "name", "kind", "expression", "domain", "assumptions",
        "variables", "uncertainty_rule", "falsifier", "claim_ceiling", "owner_lanes",
    }
    for row in equations:
        equation_id = row.get("equation_id", "<missing>")
        if not required_equation_fields.issubset(row):
            errors.append(f"equation_required_field_missing:{equation_id}")
        if not row.get("assumptions") or not row.get("variables"):
            errors.append(f"equation_empty_assumptions_or_variables:{equation_id}")
        owners = set(row.get("owner_lanes", []))
        if not owners or not owners <= expected_lanes:
            errors.append(f"equation_owner_invalid:{equation_id}")
        equation_owner_coverage.update(owners)
        for variable in row.get("variables", []):
            if not all(variable.get(field) for field in ("symbol", "meaning", "unit_or_type")):
                errors.append(f"equation_variable_incomplete:{equation_id}")

    goals = registry.get("goal_contracts", [])
    goal_ids = [row.get("goal_id") for row in goals]
    if len(goal_ids) != len(set(goal_ids)):
        errors.append("duplicate_goal_id")
    if len(goals) < 20:
        errors.append("canonical_goal_count_below_twenty")
    goal_owner_coverage = set()
    lane_interfaces: dict[str, dict[str, set[str]]] = {
        lane: {"goal_ids": set(), "equation_ids": set()} for lane in expected_lanes
    }
    required_goal_fields = {
        "goal_id", "title", "owner_lanes", "equation_ids",
        "decision_predicate", "required_observables", "uncertainty_rule",
        "evidence_minimum", "status", "non_claims",
    }
    for goal in goals:
        goal_id = goal.get("goal_id", "<missing>")
        if not required_goal_fields.issubset(goal):
            errors.append(f"goal_required_field_missing:{goal_id}")
        if goal.get("status") != "OPEN":
            errors.append(f"goal_not_open_without_evidence:{goal_id}")
        references = set(goal.get("equation_ids", []))
        if not references or not references <= expected_equations:
            errors.append(f"goal_equation_reference_invalid:{goal_id}")
        if not goal.get("required_observables") or not goal.get("non_claims"):
            errors.append(f"goal_observable_or_nonclaim_missing:{goal_id}")
        owners = set(goal.get("owner_lanes", []))
        if not owners or not owners <= expected_lanes:
            errors.append(f"goal_owner_invalid:{goal_id}")
        goal_owner_coverage.update(owners)
        for lane in owners & expected_lanes:
            lane_interfaces[lane]["goal_ids"].add(goal_id)
            lane_interfaces[lane]["equation_ids"].update(references)

    if equation_owner_coverage != expected_lanes:
        errors.append("equation_lane_coverage_incomplete")
    if goal_owner_coverage != expected_lanes:
        errors.append("goal_lane_coverage_incomplete")

    if scm_registry.get("schema") != (
        "uqpu-cycle006-scm-lokathibodi-mathematical-formalism-v0.1"
    ):
        errors.append("scm_math_registry_schema_mismatch")
    scm_equations = scm_registry.get("equations", [])
    scm_equation_ids = [row.get("equation_id") for row in scm_equations]
    expected_scm_equations = {f"SCM-MATH-{index:03d}" for index in range(1, 20)}
    if len(scm_equation_ids) != len(set(scm_equation_ids)):
        errors.append("duplicate_scm_equation_id")
    if set(scm_equation_ids) != expected_scm_equations:
        errors.append("scm_equation_set_mismatch")
    for row in scm_equations:
        equation_id = row.get("equation_id", "<missing>")
        required = {
            "equation_id", "name", "expression", "epistemic_layer",
            "assumptions", "variables", "falsifier", "canon_uses",
            "real_world_status",
        }
        if not required.issubset(row):
            errors.append(f"scm_equation_required_field_missing:{equation_id}")
        if not row.get("assumptions") or not row.get("variables"):
            errors.append(f"scm_equation_empty_assumptions_or_variables:{equation_id}")
        for variable in row.get("variables", []):
            if not all(variable.get(field) for field in ("symbol", "meaning", "unit_or_type")):
                errors.append(f"scm_equation_variable_incomplete:{equation_id}")

    device_ids = {row.get("device_id") for row in scm_registry.get("device_ladder", [])}
    if device_ids != {"SCM-1", "SCM-2", "SCM-3", "SCM-4", "SCM-5", "ATTHAN-CONTROL"}:
        errors.append("scm_device_ladder_mismatch")
    for device in scm_registry.get("device_ladder", []):
        if not set(device.get("dependencies", [])) <= expected_scm_equations:
            errors.append(f"scm_device_dependency_invalid:{device.get('device_id')}")
    volumes = scm_registry.get("volume_map", [])
    if {row.get("volume") for row in volumes} != {1, 2, 3, 4, 5}:
        errors.append("lokathibodi_volume_map_incomplete")
    for volume in volumes:
        if not set(volume.get("equation_ids", [])) <= expected_scm_equations:
            errors.append(f"volume_equation_reference_invalid:{volume.get('volume')}")
    firewall = scm_registry.get("epistemic_firewall", {})
    if firewall.get("real_null") != "g_SR = 0" or not firewall.get("forbidden_cast"):
        errors.append("scm_epistemic_firewall_missing")
    scm_goal = next((goal for goal in goals if goal.get("goal_id") == "GOAL-SCM"), {})
    if set(scm_goal.get("supplemental_equation_ids", [])) != expected_scm_equations:
        errors.append("scm_goal_supplemental_equation_set_mismatch")
    lane_interfaces["SCM"]["equation_ids"].update(expected_scm_equations)

    serialized_interfaces = {
        lane: {
            "goal_ids": sorted(values["goal_ids"]),
            "equation_ids": sorted(values["equation_ids"]),
        }
        for lane, values in sorted(lane_interfaces.items())
    }
    return {
        "schema": "uqpu-cycle006-unified-math-registry-validation-v1",
        "errors": errors,
        "formal_specification_valid": not errors,
        "umrl_equation_count": len(equations),
        "scm_equation_count": len(scm_equations),
        "goal_count": len(goals),
        "lane_count": len(expected_lanes),
        "service_family_count": len(registry.get("service_portfolio", [])),
        "device_stage_count": len(scm_registry.get("device_ladder", [])),
        "lokathibodi_volume_count": len(volumes),
        "all_goal_states_open": all(goal.get("status") == "OPEN" for goal in goals),
        "empirical_spiritual_claim": False,
        "physical_law_claim": False,
        "mission_achievement_claim": False,
        "lane_interfaces": serialized_interfaces,
        "evidence_class": "STRUCTURAL_VALIDATION_OF_FORMAL_SPECIFICATIONS_NOT_SCIENTIFIC_VALIDATION",
    }


def build_cycle006_packet(
    *,
    code_commit: str,
    scale_rows: list[dict],
    durable_io: dict,
    manifest: dict,
    batch039: dict,
    batch039_sha256: str,
    ai_generator_module_sha256: str,
    archive_evidence: dict,
    archive_evidence_sha256: str,
    cycle005_scm: dict,
    unified_math_registry: dict,
    unified_math_registry_sha256: str,
    scm_math_registry: dict,
    scm_math_registry_sha256: str,
) -> tuple[dict, dict, dict, dict]:
    if not re.fullmatch(r"[0-9a-f]{40}", code_commit):
        raise ValueError("code_commit must be a full lowercase Git SHA-1")
    if len(scale_rows) != 2 or [row["node_count"] for row in scale_rows] != [18, 24]:
        raise ValueError("Cycle 006 requires ordered n=18 complete and n=24 capped rows")
    if not scale_rows[0]["exact"]["complete"]:
        raise ValueError("n=18 case must complete exact enumeration")
    if scale_rows[1]["exact"]["complete"] or scale_rows[1]["exact"]["stop_reason"] != "STATE_CAP":
        raise ValueError("n=24 case must demonstrate state-cap termination")
    registry = build_material_evidence_registry()
    registry["study_lot_id"] = None
    registry_validation = validate_material_registry_v2(registry, as_of=date(2026, 9, 28))
    cost = build_cost_adversarial_gate()
    custody = build_custody_adversarial_gate()
    graph = build_capital_dependency_graph()
    evidence_status = {f"DMF-PR-{index:02d}": False for index in range(1, 10)}
    evidence_status.update({
        "BOS-DATA-LOCAL-CHECKSUM": False,
        "BOS-DATA-LICENSE": archive_evidence["source"]["license"] == {"id": "cc-by-4.0"},
        "BOS-DATA-FORMAT": archive_evidence["readme_semantics"]["bit_flip"]["format"].startswith("Apache Parquet"),
        "BOS-DATA-COLUMNS": bool(archive_evidence["readme_semantics"]["phase_flip"]["column_families"]),
        "BOS-BASIS-UNCERTAINTY-MAP": False,
        "BOS-MATCHED-DEVICE-RESOURCES": False,
    })
    capital = derive_capital_blockers(graph, evidence_status)
    scorer, custodian, reveal_audit = build_scm_role_packages(cycle005_scm)
    math_validation = validate_unified_math_registries(
        unified_math_registry, scm_math_registry
    )
    if not math_validation["formal_specification_valid"]:
        raise ValueError(f"unified mathematical registries invalid: {math_validation['errors']}")
    math_summary = {
        "canonical_document": "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
        "goal_registry": "benchmarks/experiments/cycle006-delta01-unified-math-goal-registry.json",
        "goal_registry_sha256": unified_math_registry_sha256,
        "scm_document": "docs/SCM_LOKATHIBODI_MIND_MENTAL_FACTORS_CONTROL_FORMALISM_V0_1_2026-09-28.md",
        "scm_registry": "benchmarks/experiments/cycle006-delta01-scm-lokathibodi-math-registry.json",
        "scm_registry_sha256": scm_math_registry_sha256,
        "validation": math_validation,
        "umce_status": "OPEN_ALL_GOALS_REQUIRE_GOAL_SPECIFIC_EVIDENCE",
        "new_physical_law_claim": False,
        "spiritual_channel_claim": False,
        "evidence_class": "PROJECT_FORMAL_SPECIFICATION_AND_STRUCTURAL_VALIDATION_ONLY",
    }
    archive_summary = {
        "artifact": "benchmarks/evidence/cycle006-delta01-zenodo-range-metadata.json",
        "artifact_sha256": archive_evidence_sha256,
        "license": archive_evidence["source"]["license"],
        "archive_bytes": archive_evidence["archive"]["bytes"],
        "central_directory_summary": archive_evidence["central_directory"]["inventory_summary"],
        "readme_member": archive_evidence["readme_range"]["member"],
        "readme_semantics": archive_evidence["readme_semantics"],
        "analysis_state": archive_evidence["analysis_state"],
        "evidence_class": archive_evidence["evidence_class"],
    }
    packet = {
        "schema": "uqpu-cycle006-delta01-integrated-gates-v1",
        "cycle": "006",
        "delta": "01",
        "status": "LOCAL_MEASUREMENTS_RANGE_VERIFIED_METADATA_AND_ADVERSARIAL_GATES_NO_EVIDENCE_PROMOTION",
        "generator_code_commit": code_commit,
        "lanes": {
            "A": {
                "repeated_scale_cases": scale_rows,
                "evidence_class": "REPEATED_LOCAL_CLASSICAL_SOFTWARE_SCREEN_NOT_SCALING_LAW",
            },
            "B": build_provider_receipt_gate(manifest),
            "C": durable_io,
            "D": {
                **archive_summary,
                "service_mapping_advanced": True,
                "basis_resolved_rates_extracted": False,
                "uncertainty_extracted": False,
                "project_reproduction": False,
            },
            "E": {"registry": registry, "validation": registry_validation},
            "F": cost,
            "G": custody,
            "H": capital,
            "FND/EQN": {
                **archive_summary,
                "unified_mathematical_language": math_summary,
            },
            "SCM": {
                "scorer_package": "benchmarks/experiments/cycle006-delta01-scm-scorer-package.json",
                "custodian_package": "benchmarks/results/cycle006-delta01-scm-custodian-package.json",
                "reveal_audit": "benchmarks/results/cycle006-delta01-scm-reveal-audit.json",
                "validation_errors": [],
                "operational_blinding": False,
                "fictional_mathematical_formalism": math_summary,
                "evidence_class": "SYNTHETIC_SEPARATE_ROLE_PACKAGES_NOT_OPERATIONAL_BLINDING",
            },
            "AI-COST": freeze_ai_dataset_contract(
                batch039,
                baseline_file_sha256=batch039_sha256,
                generator_module_sha256=ai_generator_module_sha256,
            ),
            "QOS/QSVT": build_qasm_roundtrip_gate(manifest),
        },
        "unified_mathematical_language": math_summary,
        "evidence_boundary": [
            "A/C measurements are local process/software observations only and support no scaling, energy, GPU, provider, or QPU claim.",
            "B contains negative schema tests and an empty receipt; it cannot submit work.",
            "D and FND/EQN retrieve only two byte ranges plus official API metadata; no Parquet payload or experimental value is analyzed.",
            "E/G/H are empty operational gates tested with synthetic controls; no material, sample, purchase, or capital decision exists.",
            "F adversarially refuses incomplete or mismatched ledgers; its passing control is synthetic arithmetic only.",
            "SCM role packages remain synthetic and co-located, not operational blinding or source evidence.",
            "The UQPU/SCM equations are project specifications and fictional/protocol models; structural validation is not validation of a physical law, spiritual channel, mind control, portal, or mission achievement.",
            "AI-COST freezes toy sample hashes but has no candidate result, measured energy, or cost.",
            "QOS/QSVT validates a narrow repository grammar round-trip, not general OpenQASM semantics, provider transpilation, or hardware.",
        ],
    }
    return packet, scorer, custodian, reveal_audit
