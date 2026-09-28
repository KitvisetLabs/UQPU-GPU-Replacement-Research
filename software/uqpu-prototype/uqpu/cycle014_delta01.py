"""Cycle 014 bounded cross-lane contracts; fixtures are synthetic or fiction-only."""
from __future__ import annotations

import hashlib
import json
import math
import os
import struct
import subprocess
import sys
import tempfile
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash, weighted_maxcut_13

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")
HEX = set("0123456789abcdef")


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and set(value) <= HEX


def _number(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(float(value))
    except (OverflowError, ValueError):
        return False


def matched_output_contract(workload, result):
    keys = {"workload_id", "baseline", "accepted_output", "output_unit", "max_states", "seed"}
    if not isinstance(workload, dict) or set(workload) != keys:
        raise ValueError("workload contract schema")
    if any(not isinstance(workload[k], str) or not workload[k] for k in ("workload_id", "baseline", "accepted_output", "output_unit")):
        raise ValueError("workload identity")
    if (not isinstance(workload["max_states"], int) or isinstance(workload["max_states"], bool)
            or not 1 <= workload["max_states"] <= 1024
            or not isinstance(workload["seed"], int) or isinstance(workload["seed"], bool) or workload["seed"] < 0):
        raise ValueError("workload bounds")
    if not isinstance(result, dict) or not result:
        raise ValueError("accepted output")
    return {
        "workload_sha256": canonical_hash(workload),
        "result_sha256": canonical_hash(result),
        "baseline": workload["baseline"],
        "accepted_output": workload["accepted_output"],
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
        "scaling_claim": None,
    }


def provider_receipt_envelope(request_sha256, receipt):
    if not _digest(request_sha256):
        raise ValueError("request digest")
    required = {"schema", "request_sha256", "provider_status", "job_id", "invoice"}
    if not isinstance(receipt, dict) or set(receipt) != required or receipt["schema"] != "receipt-v1":
        raise ValueError("receipt schema")
    if receipt["request_sha256"] != request_sha256:
        raise ValueError("receipt/request binding")
    status = receipt["provider_status"]
    if status == "NOT_EXECUTED":
        if receipt["job_id"] is not None or receipt["invoice"] is not None:
            raise ValueError("unexecuted receipt must leave job and invoice null")
    elif status == "SUCCEEDED":
        invoice = receipt["invoice"]
        if (not isinstance(receipt["job_id"], str) or not receipt["job_id"]
                or not isinstance(invoice, dict) or set(invoice) != {"invoice_id", "amount_usd"}
                or not isinstance(invoice["invoice_id"], str) or not invoice["invoice_id"]
                or not _number(invoice["amount_usd"]) or invoice["amount_usd"] < 0):
            raise ValueError("executed receipt provenance")
    else:
        raise ValueError("provider status")
    return {**receipt, "evidence_class": "SYNTHETIC_RECEIPT_ENVELOPE"}


def subprocess_replace_boundary(directory, target_name, new_bytes, boundary):
    if boundary not in ("before_replace", "after_replace") or not isinstance(new_bytes, bytes):
        raise ValueError("replacement boundary")
    root = Path(directory)
    target = root / target_name
    script = r'''
import os, sys, tempfile
from pathlib import Path
root = Path(sys.argv[1])
target = root / sys.argv[2]
boundary = sys.argv[3]
payload = bytes.fromhex(sys.argv[4])
fd, staged = tempfile.mkstemp(prefix=f".{target.name}.tmp.active.", dir=root)
with os.fdopen(fd, "wb") as handle:
    handle.write(payload)
if boundary == "after_replace":
    os.replace(staged, target)
os._exit(23)
'''
    proc = subprocess.run(
        [sys.executable, "-c", script, str(root), target_name, boundary, new_bytes.hex()],
        check=False, capture_output=True, text=True,
    )
    if proc.returncode != 23:
        raise RuntimeError("child process did not stop at named boundary")
    visible = target.read_bytes() if target.exists() else None
    return {
        "visible": visible,
        "status": "OLD_COMPLETE" if boundary == "before_replace" else "NEW_COMPLETE",
        "process_exit": proc.returncode,
        "durability": "PROCESS_TERMINATION_ONLY",
    }


def zip64_metadata_gate(zip64_end, locator, eocd, zip64_start, locator_start, eocd_start):
    if not all(isinstance(value, bytes) for value in (zip64_end, locator, eocd)):
        raise ValueError("metadata bytes")
    if len(zip64_end) != 56 or len(locator) != 20 or len(eocd) < 22:
        raise ValueError("metadata widths")
    signature, record_size = struct.unpack_from("<4sQ", zip64_end)
    if signature != b"PK\x06\x06" or record_size != 44:
        raise ValueError("ZIP64 end signature/size")
    _, disk, recorded_offset, total_disks = struct.unpack("<4sIQI", locator)
    if disk != 0 or recorded_offset != zip64_start or total_disks != 1:
        raise ValueError("ZIP64 locator")
    if zip64_start + len(zip64_end) != locator_start or locator_start + len(locator) != eocd_start:
        raise ValueError("metadata adjacency")
    eocd_sig, disk_no, central_disk, _, _, _, _, comment_len = struct.unpack_from("<4sHHHHIIH", eocd)
    if eocd_sig != b"PK\x05\x06" or disk_no != 0 or central_disk != 0 or len(eocd) != 22 + comment_len:
        raise ValueError("EOCD signature/comment/disk fields")
    return {
        "zip64_eocd_bytes": len(zip64_end),
        "locator_bytes": len(locator),
        "eocd_comment_bytes": comment_len,
        "payload_read": False,
        "status": "VALID_SYNTHETIC_METADATA",
    }


def custody_expiry_boundary(event, now):
    from uqpu.cycle013_delta01 import _iso_day
    expires = _iso_day(event["expiry"])
    current = _iso_day(now)
    if expires <= current:
        return {"valid": False, "reason": "EXPIRED"}
    return {"valid": True, "remaining_days": (expires - current).days, "evidence_class": "SYNTHETIC_CUSTODY"}


def model_interval_grid(total_interval, output_counts):
    if (not isinstance(total_interval, (list, tuple)) or len(total_interval) != 2
            or any(not _number(v) or v < 0 for v in total_interval) or total_interval[1] < total_interval[0]):
        raise ValueError("total interval")
    if not isinstance(output_counts, list) or not output_counts:
        raise ValueError("output grid")
    rows = []
    for count in output_counts:
        if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
            rows.append({"accepted_outputs": count, "per_output_usd": None, "status": "NULL_NONPOSITIVE_DENOMINATOR"})
            continue
        interval = [total_interval[0] / count, total_interval[1] / count]
        if any(not _number(value) for value in interval):
            raise ValueError("interval overflow")
        rows.append({"accepted_outputs": count, "per_output_usd": interval, "status": "MODEL_ONLY"})
    return rows


def covariance_product_dimension(left, right):
    if (not isinstance(left, (list, tuple)) or not isinstance(right, (list, tuple))
            or len(left) != 7 or len(right) != 7
            or any(not isinstance(x, int) or isinstance(x, bool) for x in list(left) + list(right))):
        raise ValueError("SI dimension vector")
    return [a + b for a, b in zip(left, right)]


def rank_stability_bounds(baseline, scenario_orders):
    if (not isinstance(baseline, list) or not baseline or len(set(baseline)) != len(baseline)
            or not isinstance(scenario_orders, list) or not scenario_orders):
        raise ValueError("ranking set")
    if any(not isinstance(order, list) or set(order) != set(baseline) for order in scenario_orders):
        raise ValueError("scenario ranking")
    stable_fraction = sum(order == baseline for order in scenario_orders) / len(scenario_orders)
    return {
        "stability_bounds": [stable_fraction, stable_fraction],
        "scenario_count": len(scenario_orders),
        "capital": None,
        "evidence_class": "ILLUSTRATIVE_SCENARIO_GRID",
    }


def rational_interval_add(left, right):
    exact = {"unit", "dimension", "domain_sort", "evidence_sort", "source_sha256"}
    if not isinstance(left, dict) or not isinstance(right, dict) or set(left) != exact | {"lower", "upper"} or set(right) != exact | {"lower", "upper"}:
        raise ValueError("typed interval schema")
    if any(left[key] != right[key] for key in exact) or left["domain_sort"] not in ("RealModel", "Fiction"):
        raise ValueError("typed interval sort mismatch")
    if left["domain_sort"] == "Fiction" and left["evidence_sort"] != "Fiction":
        raise ValueError("fiction evidence sort")
    if left["domain_sort"] == "RealModel" and left["evidence_sort"] == "Fiction":
        raise ValueError("undeclared Fic-to-Emp cast")
    def pair(value):
        if (not isinstance(value, (list, tuple)) or len(value) != 2
                or any(not isinstance(x, int) or isinstance(x, bool) for x in value) or value[1] <= 0):
            raise ValueError("rational endpoint")
        return value[0], value[1]
    from fractions import Fraction
    lo1, hi1 = Fraction(*pair(left["lower"])), Fraction(*pair(left["upper"]))
    lo2, hi2 = Fraction(*pair(right["lower"])), Fraction(*pair(right["upper"]))
    lo, hi = lo1 + lo2, hi1 + hi2
    return {
        **{key: left[key] for key in exact},
        "lower": [lo.numerator, lo.denominator],
        "upper": [hi.numerator, hi.denominator],
    }


def fictional_transcript(consent, nonce, scope, challenge, response, now):
    from uqpu.cycle013_delta01 import _iso_day
    if consent.get("fiction_only") is not True or consent.get("empirical_coupling") is not None:
        raise ValueError("fiction/empirical firewall")
    if (not isinstance(nonce, str) or not nonce or nonce in consent.get("seen", set())
            or scope != consent.get("scope") or challenge != response or consent.get("active") is not True
            or _iso_day(consent.get("expires_at")) <= _iso_day(now)):
        raise ValueError("fictional consent/transcript")
    return {"accepted": True, "sort": "Fiction", "nonce": nonce, "empirical_claim": None}


def ai_lineage_manifest(source_bytes, splits, metrics, config):
    if not isinstance(source_bytes, bytes) or not source_bytes or not isinstance(config, dict) or not config:
        raise ValueError("AI source/config")
    if not isinstance(splits, dict) or set(splits) != {"train", "validation", "test"}:
        raise ValueError("AI splits")
    if any(not isinstance(rows, list) or not rows or any(not isinstance(row, str) or not row for row in rows) for rows in splits.values()):
        raise ValueError("AI split rows")
    rows = [row for split in splits.values() for row in split]
    if len(rows) != len(set(rows)):
        raise ValueError("AI split overlap")
    if not isinstance(metrics, dict) or set(metrics) != {"train", "validation", "test"}:
        raise ValueError("AI metrics")
    normalized_metrics = {}
    for split, metric in metrics.items():
        if not isinstance(metric, dict) or set(metric) != {"loss"} or not _number(metric["loss"]) or metric["loss"] < 0:
            raise ValueError("AI loss schema")
        normalized_metrics[split] = {"loss": float(metric["loss"])}
    body = {
        "version": 4,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "split_hashes": {name: canonical_hash(sorted(splits[name])) for name in ("train", "validation", "test")},
        "metrics_sha256": canonical_hash(normalized_metrics),
        "config_sha256": canonical_hash(config),
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    return {**body, "manifest_sha256": canonical_hash(body)}


def qos_certificate_v4(source_bytes, semantic_map, resources, previous_resources):
    required = {"qubits", "bits", "depth", "gates"}
    if not isinstance(source_bytes, bytes) or not source_bytes or not isinstance(semantic_map, dict):
        raise ValueError("QOS source/map")
    if not isinstance(resources, dict) or set(resources) != required or not isinstance(previous_resources, dict) or set(previous_resources) != required:
        raise ValueError("QOS resource schema")
    for values in (resources, previous_resources):
        if any(not isinstance(values[k], int) or isinstance(values[k], bool) or values[k] < (1 if k in ("qubits", "bits") else 0) for k in required):
            raise ValueError("QOS resource value")
    if resources["qubits"] != previous_resources["qubits"] or resources["bits"] != previous_resources["bits"]:
        raise ValueError("QOS semantic dimensions changed")
    if any(resources[k] > previous_resources[k] for k in ("depth", "gates")):
        raise ValueError("QOS resource increase")
    body = {
        "version": 4,
        "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
        "map_sha256": canonical_hash(semantic_map),
        "resources": dict(resources),
        "previous_resources": dict(previous_resources),
        "hardware": None,
        "evidence_class": "ER6_SYNTHETIC_CERTIFICATE",
    }
    return {**body, "certificate_sha256": canonical_hash(body)}


def run_cycle014_fixture():
    graph = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 5), (2, 4, 2), (3, 4, 4)]
    exact = weighted_maxcut_13(5, graph)
    workload = {
        "workload_id": "maxcut-five-node-v1", "baseline": "bounded-exhaustive-classical",
        "accepted_output": "exact-max-cut-weight", "output_unit": "integer-weight",
        "max_states": 32, "seed": 0,
    }
    a = matched_output_contract(workload, {"optimum": exact["best_cut_weight"], "states": exact["states"]})
    request_hash = canonical_hash({"request": "fixture", "cycle": 14})
    b = provider_receipt_envelope(request_hash, {
        "schema": "receipt-v1", "request_sha256": request_hash, "provider_status": "NOT_EXECUTED",
        "job_id": None, "invoice": None,
    })
    root = Path(tempfile.mkdtemp(prefix="uqpu-cycle014-"))
    (root / "target.bin").write_bytes(b"old-complete")
    before = subprocess_replace_boundary(root, "target.bin", b"new-complete", "before_replace")
    for path in root.glob(".target.bin.tmp.active.*"):
        path.unlink()
    after = subprocess_replace_boundary(root, "target.bin", b"new-complete", "after_replace")
    (root / "target.bin").unlink(missing_ok=True)
    for path in root.iterdir():
        path.unlink(missing_ok=True)
    root.rmdir()
    c = {"before": before["status"], "after": after["status"], "durability": "PROCESS_TERMINATION_ONLY"}
    zip64 = struct.pack("<4sQHHIIQQQQ", b"PK\x06\x06", 44, 45, 45, 0, 0, 1, 1, 60, 100)
    locator = struct.pack("<4sIQI", b"PK\x06\x07", 0, 100, 1)
    eocd = struct.pack("<4sHHHHIIH", b"PK\x05\x06", 0, 0, 1, 1, 60, 100, 3) + b"abc"
    d = zip64_metadata_gate(zip64, locator, eocd, 100, 156, 176)
    e = custody_expiry_boundary({"expiry": "2030-01-01"}, "2026-09-28")
    f = model_interval_grid([7, 12], [1, 2, 4, 0])
    g = covariance_product_dimension([1, 0, 0, 0, 0, 0, 0], [1, 0, -1, 0, 0, 0, 0])
    h = rank_stability_bounds(["a", "b"], [["a", "b"], ["b", "a"], ["a", "b"]])
    source = hashlib.sha256(b"typed-source-fixture").hexdigest()
    base = {"unit": "1", "dimension": [0] * 10, "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": source}
    fnd = rational_interval_add({**base, "lower": [1, 2], "upper": [3, 2]},
                                {**base, "lower": [1, 4], "upper": [1, 2]})
    scm = fictional_transcript({"fiction_only": True, "empirical_coupling": None, "seen": set(), "scope": "scene-1",
                                "active": True, "expires_at": "2030-01-01"},
                               "fresh-1", "scene-1", "challenge", "challenge", "2026-09-28")
    ai = ai_lineage_manifest(b"model-bytes-v4",
        {"train": ["t1"], "validation": ["v1"], "test": ["x1"]},
        {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}},
        {"optimizer": "fixture", "seed": 0})
    qos = qos_certificate_v4(b"er6-v4-source", {"map": "v4"},
        {"qubits": 6, "bits": 6, "depth": 14, "gates": 30},
        {"qubits": 6, "bits": 6, "depth": 16, "gates": 34})
    return {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g, "H": h,
            "FND/EQN": fnd, "SCM": scm, "AI-COST": ai, "QOS/QSVT": qos}
