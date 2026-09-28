"""Cycle 016 bounded synchronized fixtures; synthetic/model/fiction evidence only."""
from __future__ import annotations

import hashlib
import hmac
import math
import os
import struct
import tempfile
from fractions import Fraction
from pathlib import Path

from uqpu.cycle013_delta01 import _is_psd, canonical_hash, weighted_maxcut_13
from uqpu.cycle014_delta01 import ai_lineage_manifest, qos_certificate_v4, run_cycle014_fixture
from uqpu.cycle015_delta01 import (
    component_covariance_sweep,
    concurrent_subprocess_replace,
    correlation_ranking_grid,
    make_custody_event,
    qos_er6_reconstruction_v5,
    typed_covariance_block,
    verify_custody_chain,
)

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")


def _isfinite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


def exact_maxcut_10_node(graph):
    """Enumerate exactly 1,024 partitions and cross-check a separate evaluator."""
    n = 10
    if not isinstance(graph, list) or not graph:
        raise ValueError("graph")
    normalized = []
    for row in graph:
        if not isinstance(row, (list, tuple)) or len(row) != 3:
            raise ValueError("edge")
        u, v, w = row
        if any(not isinstance(x, int) or isinstance(x, bool) for x in row) or not (0 <= u < n and 0 <= v < n and u != v and w > 0):
            raise ValueError("edge range/weight")
        normalized.append([min(u, v), max(u, v), w])
    if len({(u, v) for u, v, _ in normalized}) != len(normalized):
        raise ValueError("duplicate edge")
    normalized.sort()
    task_sha = canonical_hash({"vertices": n, "edges": normalized})
    def score_edges(mask):
        total = 0
        for u, v, weight in normalized:
            if ((mask >> u) & 1) != ((mask >> v) & 1):
                total += weight
        return total
    scores = [score_edges(mask) for mask in range(1 << n)]
    best = max(scores)
    witnesses = [mask for mask, score in enumerate(scores) if score == best]
    # Independent check against the prior bounded exhaustive comparator.
    reference = weighted_maxcut_13(n, graph, cap=1024)
    if best != reference["best_cut_weight"] or len(scores) != reference["states"]:
        raise AssertionError("independent exact comparator disagreement")
    witness_sha = canonical_hash(witnesses)
    body = {"task_sha256": task_sha, "state_count": 1024, "best_cut_weight": best, "witness_sha256": witness_sha}
    return {**body, "result_sha256": canonical_hash(body), "reference_graph_sha256": reference["graph_sha256"],
            "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE", "scaling_claim": None}


def synthetic_receipt_v3(request_sha256, authorization_scope, key_id, fixture_key, invoice=None):
    """Verify a fixture-only HMAC tag; never represent it as provider authority."""
    if fixture_key is None or key_id is None or authorization_scope is None:
        return {"receipt": None, "provider_claim": None, "status": "NULL_MISSING_EXTERNAL_AUTHENTICATION"}
    if not isinstance(request_sha256, str) or len(request_sha256) != 64 or not isinstance(fixture_key, bytes) or not fixture_key:
        raise ValueError("receipt inputs")
    if invoice is not None:
        raise ValueError("NOT_EXECUTED fixture must leave invoice null")
    body = {
        "schema": "receipt-v3",
        "request_sha256": request_sha256,
        "provider_status": "NOT_EXECUTED",
        "authorization_scope": authorization_scope,
        "authorized": False,
        "key_id": key_id,
        "job_id": None,
        "invoice": None,
    }
    tag = hmac.new(fixture_key, canonical_hash(body).encode("ascii"), hashlib.sha256).hexdigest()
    return {**body, "signature_algorithm": "HMAC-SHA256-FIXTURE", "signature": tag,
            "evidence_class": "SYNTHETIC_RECEIPT_AUTHENTICATION", "provider_claim": None}


def verify_synthetic_receipt_v3(receipt, request_sha256, expected_scope, expected_key_id, fixture_key):
    keys = {"schema", "request_sha256", "provider_status", "authorization_scope", "authorized", "key_id", "job_id", "invoice", "signature_algorithm", "signature", "evidence_class", "provider_claim"}
    if not isinstance(receipt, dict) or set(receipt) != keys:
        return False
    if (receipt["schema"] != "receipt-v3" or receipt["request_sha256"] != request_sha256
            or receipt["authorization_scope"] != expected_scope or receipt["authorized"] is not False
            or receipt["key_id"] != expected_key_id or receipt["provider_status"] != "NOT_EXECUTED"
            or receipt["job_id"] is not None or receipt["invoice"] is not None
            or receipt["signature_algorithm"] != "HMAC-SHA256-FIXTURE" or receipt["provider_claim"] is not None
            or not isinstance(receipt["signature"], str)):
        return False
    body = {k: receipt[k] for k in ("schema", "request_sha256", "provider_status", "authorization_scope", "authorized", "key_id", "job_id", "invoice")}
    expected = hmac.new(fixture_key, canonical_hash(body).encode("ascii"), hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected, receipt["signature"])


def same_filesystem_concurrent_replace(directory, target_name, payloads):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / target_name
    target.write_bytes(b"cycle016-old-complete")
    fd, staged_name = tempfile.mkstemp(prefix=f".{target_name}.device-check.", dir=root)
    os.close(fd)
    staged = Path(staged_name)
    device_ids = (os.stat(target).st_dev, os.stat(staged).st_dev, os.stat(root).st_dev)
    staged.unlink()
    result = concurrent_subprocess_replace(root, target_name, payloads)
    if len(set(device_ids)) != 1:
        raise AssertionError("target and staging directory cross device")
    return {"device_id_match": True, "device_id_values": len(set(device_ids)), "replacement": result,
            "evidence_class": "SAME_FILESYSTEM_PROCESS_FIXTURE", "crash_durability": None}


def zip64_central_entry_gate(record, descriptor, disk_sizes):
    """Check one central entry and ZIP64 data descriptor before payload access."""
    if not isinstance(record, bytes) or not isinstance(descriptor, bytes) or not isinstance(disk_sizes, list) or not disk_sizes:
        raise ValueError("ZIP entry inputs")
    if len(record) < 46 or any(not isinstance(x, int) or isinstance(x, bool) or x <= 0 for x in disk_sizes):
        raise ValueError("ZIP entry widths")
    (sig, made, needed, flags, method, mtime, mdate, crc, comp32, uncomp32,
     name_len, extra_len, comment_len, disk_start16, internal, external,
     local_offset32) = struct.unpack_from("<4sHHHHHHIIIHHHHHII", record)
    total = 46 + name_len + extra_len + comment_len
    if sig != b"PK\x01\x02" or len(record) != total or name_len == 0:
        raise ValueError("central record length/signature")
    name = record[46:46 + name_len]
    extra = record[46 + name_len:46 + name_len + extra_len]
    if not name:
        raise ValueError("empty filename")
    zip64 = None
    pos = 0
    while pos < len(extra):
        if len(extra) - pos < 4:
            raise ValueError("truncated extra field")
        tag, size = struct.unpack_from("<HH", extra, pos)
        pos += 4
        if size > len(extra) - pos:
            raise ValueError("extra field size")
        if tag == 0x0001:
            zip64 = extra[pos:pos + size]
        pos += size
    needs_zip64 = comp32 == 0xFFFFFFFF or uncomp32 == 0xFFFFFFFF or local_offset32 == 0xFFFFFFFF or disk_start16 == 0xFFFF
    if needs_zip64 and zip64 is None:
        raise ValueError("missing ZIP64 extended information")
    cursor = 0
    values = {"uncompressed": uncomp32, "compressed": comp32, "local_offset": local_offset32, "disk": disk_start16}
    widths = {"uncompressed": 8, "compressed": 8, "local_offset": 8, "disk": 4}
    sentinels = {"uncompressed": 0xFFFFFFFF, "compressed": 0xFFFFFFFF, "local_offset": 0xFFFFFFFF, "disk": 0xFFFF}
    for key in ("uncompressed", "compressed", "local_offset", "disk"):
        if values[key] == sentinels[key]:
            if cursor + widths[key] > len(zip64):
                raise ValueError("short ZIP64 extra values")
            values[key] = int.from_bytes(zip64[cursor:cursor + widths[key]], "little")
            cursor += widths[key]
    if cursor != len(zip64 or b""):
        raise ValueError("unexpected ZIP64 extra tail")
    if values["disk"] >= len(disk_sizes) or values["local_offset"] + 30 > disk_sizes[values["disk"]]:
        raise ValueError("local header disk-relative offset")
    if len(descriptor) != 24:
        raise ValueError("ZIP64 data descriptor width")
    dd_sig, dd_crc, dd_comp, dd_uncomp = struct.unpack("<4sIQQ", descriptor)
    if dd_sig != b"PK\x07\x08" or dd_crc != crc or dd_comp != values["compressed"] or dd_uncomp != values["uncompressed"]:
        raise ValueError("data descriptor disagreement")
    return {"filename_sha256": hashlib.sha256(name).hexdigest(), "disk": values["disk"],
            "local_header_offset": values["local_offset"], "compressed_size": values["compressed"],
            "uncompressed_size": values["uncompressed"], "payload_read": False,
            "evidence_class": "SYNTHETIC_ZIP64_DIRECTORY_METADATA"}


def custody_revocation_fork_suite(now):
    sample = hashlib.sha256(b"fictional-cycle16-sample").hexdigest()
    rows = [("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer")]
    events, prior = [], "0" * 64
    for seq, (issuer, scope) in enumerate(rows):
        event = make_custody_event(seq, sample, "fictional-path-16", issuer, scope, "2026-01-01", "2027-01-01", prior)
        events.append(event)
        prior = event["event_sha256"]
    registry = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-c": {"transfer"}}
    valid = verify_custody_chain(events, registry, now)
    revoked = False
    try:
        verify_custody_chain(events, {"issuer-a": {"intake"}, "issuer-c": {"transfer"}}, now)
    except ValueError:
        revoked = True
    fork = [dict(event) for event in events]
    fork[2]["previous_event_sha256"] = "f" * 64
    fork_rejected = False
    try:
        verify_custody_chain(fork, registry, now)
    except ValueError:
        fork_rejected = True
    if not revoked or not fork_rejected:
        raise AssertionError("revocation/fork control accepted")
    return {"valid_chain_events": valid["event_count"], "revoked_issuer_rejected": revoked,
            "fork_rejected": fork_rejected, "historical_hashes_immutable": True,
            "evidence_class": "SYNTHETIC_CUSTODY_NEGATIVE_CONTROL", "physical_sample_claim": None}


def cross_unit_covariance_fixture():
    length = [1, 0, 0, 0, 0, 0, 0]
    time_dim = [0, 0, 1, 0, 0, 0, 0]
    def entry(v, unit, dim):
        return {"value": v, "unit": unit, "dimension": dim}
    block = typed_covariance_block(
        [{"id": "distance", "unit": "m", "dimension": length}, {"id": "duration", "unit": "s", "dimension": time_dim}],
        [
            [entry(1.0, "m*m", [2, 0, 0, 0, 0, 0, 0]), entry(0.2, "m*s", [1, 0, 1, 0, 0, 0, 0])],
            [entry(0.2, "m*s", [1, 0, 1, 0, 0, 0, 0]), entry(1.0, "s*s", [0, 0, 2, 0, 0, 0, 0])],
        ],
    )
    return {**block, "evidence_class": "SYNTHETIC_CROSS_UNIT_COVARIANCE"}


def correlation_stress_fixture():
    baseline = ["compute", "memory", "energy", "latency"]
    return correlation_ranking_grid(baseline, [
        {"name": "independent", "correlation": [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]],
         "scenario_orders": [baseline, ["memory", "compute", "energy", "latency"]], "assumption": "identity correlation sensitivity"},
        {"name": "positive-pair", "correlation": [[1, .6, 0, 0], [.6, 1, 0, 0], [0, 0, 1, .3], [0, 0, .3, 1]],
         "scenario_orders": [["energy", "latency", "compute", "memory"], ["latency", "energy", "memory", "compute"]], "assumption": "declared positive-correlation alternative"},
    ])


def rational_interval_divide(left, right, source_bytes, unit_ratios):
    keys = {"unit", "dimension", "domain_sort", "evidence_sort", "source_sha256", "lower", "upper"}
    if not isinstance(left, dict) or not isinstance(right, dict) or set(left) != keys or set(right) != keys:
        raise ValueError("typed interval schema")
    digest = hashlib.sha256(source_bytes).hexdigest()
    if left["source_sha256"] != digest or right["source_sha256"] != digest:
        raise ValueError("source binding")
    if left["domain_sort"] != right["domain_sort"] or left["evidence_sort"] != right["evidence_sort"]:
        raise ValueError("sort mismatch")
    lo_b, hi_b = Fraction(*right["lower"]), Fraction(*right["upper"])
    if lo_b <= 0 <= hi_b:
        return {"result": None, "status": "NULL_ZERO_CROSSING_DENOMINATOR"}
    ratio = unit_ratios.get(f"{left['unit']}|{right['unit']}")
    if not isinstance(ratio, dict):
        raise ValueError("unregistered quotient unit")
    dim = [a - b for a, b in zip(left["dimension"], right["dimension"])]
    if ratio.get("dimension") != dim:
        raise ValueError("quotient dimension mismatch")
    lo_a, hi_a = Fraction(*left["lower"]), Fraction(*left["upper"])
    candidates = [lo_a / lo_b, lo_a / hi_b, hi_a / lo_b, hi_a / hi_b]
    lo, hi = min(candidates), max(candidates)
    return {"result": {"unit": ratio["unit"], "dimension": dim, "domain_sort": left["domain_sort"],
                       "evidence_sort": left["evidence_sort"], "source_sha256": digest,
                       "lower": [lo.numerator, lo.denominator], "upper": [hi.numerator, hi.denominator]},
            "status": "EXACT_RATIONAL_MODEL"}


def scm_nonce_scope_matrix(now):
    from uqpu.cycle014_delta01 import fictional_transcript
    scope, nonce = "fiction-scene-16", "cycle16-nonce"
    challenge = canonical_hash({"scope": scope, "nonce": nonce, "question": "fictional-control"})
    base = {"fiction_only": True, "empirical_coupling": None, "seen": set(), "scope": scope,
            "active": True, "expires_at": "2030-01-01"}
    cases = {
        "valid_fiction": (base, nonce, scope, challenge, challenge),
        "revoked": ({**base, "active": False}, nonce, scope, challenge, challenge),
        "replayed": ({**base, "seen": {nonce}}, nonce, scope, challenge, challenge),
        "scope_mutation": (base, nonce, "other-scope", challenge, challenge),
        "response_mutation": (base, nonce, scope, challenge, "wrong-response"),
        "expired": ({**base, "expires_at": now}, nonce, scope, challenge, challenge),
    }
    out = {}
    for name, (consent, n, s, ch, resp) in cases.items():
        try:
            accepted = fictional_transcript(consent, n, s, ch, resp, now)["accepted"]
            out[name] = "ACCEPTED_FICTION_ONLY" if accepted else "REJECTED"
        except ValueError:
            out[name] = "REJECTED"
    if out["valid_fiction"] != "ACCEPTED_FICTION_ONLY" or any(out[k] != "REJECTED" for k in out if k != "valid_fiction"):
        raise AssertionError("fiction transcript boundary")
    return {"cases": out, "challenge_sha256": challenge, "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def ai_lineage_manifest_v6(parent_v5, source_bytes, splits, metrics, config):
    keys = {"version", "parent_manifest_sha256", "source_sha256", "split_hashes", "metrics_sha256", "config_sha256", "evidence_class", "functional_equivalence", "manifest_sha256"}
    if not isinstance(parent_v5, dict) or set(parent_v5) != keys or parent_v5["version"] != 5:
        raise ValueError("parent v5 manifest")
    body_parent = {k: parent_v5[k] for k in keys if k != "manifest_sha256"}
    if canonical_hash(body_parent) != parent_v5["manifest_sha256"]:
        raise ValueError("parent v5 digest")
    if any(x is None for x in (source_bytes, splits, metrics, config)):
        return {"manifest": None, "candidate_result": None, "status": "NULL_MISSING_LINEAGE"}
    lineage = ai_lineage_manifest(source_bytes, splits, metrics, config)
    body = {"version": 6, "parent_manifest_sha256": parent_v5["manifest_sha256"],
            "source_sha256": lineage["source_sha256"], "split_hashes": lineage["split_hashes"],
            "metrics_sha256": lineage["metrics_sha256"], "config_sha256": lineage["config_sha256"],
            "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
    return {"manifest": {**body, "manifest_sha256": canonical_hash(body)}, "candidate_result": None, "status": "LINEAGE_BOUND_SYNTHETIC_ONLY"}


def verify_ai_v6(candidate, parent_v5, source_bytes, splits, metrics, config):
    return candidate == ai_lineage_manifest_v6(parent_v5, source_bytes, splits, metrics, config)


def qos_mutation_gate():
    parent = run_cycle014_fixture()["QOS/QSVT"]
    gates = [{"op": "x", "target": 0}, {"op": "cx", "control": 0, "target": 1}, {"op": "cx", "control": 1, "target": 3}]
    bound = qos_er6_reconstruction_v5(parent, gates)
    mutated_parent = dict(parent)
    mutated_parent["certificate_sha256"] = "0" * 64
    parent_rejected = False
    try:
        qos_er6_reconstruction_v5(mutated_parent, gates)
    except ValueError:
        parent_rejected = True
    semantic_map = {"width": 6, "bit_order": "little-endian", "input_to_output": "basis permutation"}
    source = b"source-bound-qos-fixture"
    resources = {"qubits": 6, "bits": 6, "depth": len(gates), "gates": len(gates)}
    previous = {"qubits": 6, "bits": 6, "depth": 14, "gates": 30}
    current_certificate = qos_certificate_v4(source, semantic_map, resources, previous)
    source_mutation_rejected = current_certificate != qos_certificate_v4(b"changed-source", semantic_map, resources, previous)
    map_mutation_rejected = current_certificate != qos_certificate_v4(source, {"width": 7}, resources, previous)
    resource_rejected = False
    try:
        qos_certificate_v4(b"mutated-source", {"map": "mutated"},
                           {"qubits": 6, "bits": 6, "depth": 15, "gates": 31},
                           {"qubits": 6, "bits": 6, "depth": 14, "gates": 30})
    except ValueError:
        resource_rejected = True
    if not parent_rejected or not resource_rejected or not source_mutation_rejected or not map_mutation_rejected:
        raise AssertionError("QOS mutation gate")
    return {"bound_parent_sha256": parent["certificate_sha256"], "maximum_integer_residual": bound["maximum_integer_residual"],
            "parent_mutation_rejected": parent_rejected, "source_mutation_rejected": source_mutation_rejected,
            "semantic_map_mutation_rejected": map_mutation_rejected, "resource_regression_rejected": resource_rejected,
            "hardware": None, "evidence_class": "ER6_SYNTHETIC_CERTIFICATE_MUTATION"}


def run_cycle016_fixture(source_bytes):
    graph = [[0, 1, 4], [0, 3, 7], [0, 6, 2], [1, 2, 5], [1, 5, 3], [2, 3, 6],
             [2, 7, 4], [3, 4, 8], [4, 5, 2], [4, 8, 5], [5, 6, 7], [6, 7, 3], [7, 8, 6], [8, 9, 4], [2, 9, 1]]
    a = exact_maxcut_10_node(graph)
    request_sha = canonical_hash({"cycle": 16, "request": "fixture-only"})
    fixture_key = b"uqpu-cycle016-test-only-key"
    receipt = synthetic_receipt_v3(request_sha, "fixture-only", "test-key-01", fixture_key)
    b = {"receipt": receipt,
         "signature_verified": verify_synthetic_receipt_v3(receipt, request_sha, "fixture-only", "test-key-01", fixture_key),
         "provider_claim": None, "evidence_class": "SYNTHETIC_RECEIPT_AUTHENTICATION"}
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle016-c-") as tmp:
        c = same_filesystem_concurrent_replace(tmp, "state.bin", [b"writer-a", b"writer-b", b"writer-c"])

    name = b"sample.bin"
    extra_payload = struct.pack("<QQQI", 8, 8, 64, 1)
    extra = struct.pack("<HH", 0x0001, len(extra_payload)) + extra_payload
    central = struct.pack(
        "<4sHHHHHHIIIHHHHHII", b"PK\x01\x02",
        45, 45, 0, 0, 0, 0,
        0x12345678, 0xFFFFFFFF, 0xFFFFFFFF,
        len(name), len(extra), 0, 0xFFFF, 0,
        0, 0xFFFFFFFF,
    ) + name + extra
    descriptor = struct.pack("<4sIQQ", b"PK\x07\x08", 0x12345678, 8, 8)
    d = zip64_central_entry_gate(central, descriptor, [128, 256])

    e = custody_revocation_fork_suite("2026-09-28")
    covariance = [[0.0] * 5 for _ in range(5)]
    for i in range(5):
        covariance[i][i] = 0.04
    invalid = [[1.0, 2.0], [2.0, 1.0]]
    nonfinite = [[float("nan") if i == j else 0.0 for j in range(5)] for i in range(5)]
    f = component_covariance_sweep([[1, 2], [0.5, 1], [1, 2], [0.5, 1], [4, 6]],
                                   {"independent": covariance, "invalid": invalid, "nonfinite": nonfinite}, [1, 2, 4, 0])

    g = cross_unit_covariance_fixture()
    h = correlation_stress_fixture()
    digest = hashlib.sha256(source_bytes).hexdigest()
    left = {"unit": "m", "dimension": [1, 0, 0, 0, 0, 0, 0], "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": digest, "lower": [2, 1], "upper": [4, 1]}
    right = {"unit": "s", "dimension": [0, 0, 1, 0, 0, 0, 0], "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": digest, "lower": [2, 1], "upper": [4, 1]}
    fn = rational_interval_divide(left, right, source_bytes, {"m|s": {"unit": "m/s", "dimension": [1, 0, -1, 0, 0, 0, 0]}})
    fzero = rational_interval_divide(left, {**right, "lower": [-1, 1], "upper": [1, 1]}, source_bytes,
                                     {"m|s": {"unit": "m/s", "dimension": [1, 0, -1, 0, 0, 0, 0]}})
    fnd = {"positive_denominator": fn, "zero_crossing_denominator": fzero}

    scm = scm_nonce_scope_matrix("2026-09-28")
    splits = {"train": ["t1"], "validation": ["v1"], "test": ["x1"]}
    metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
    config = {"optimizer": "fixture", "seed": 1}
    parent_v4 = ai_lineage_manifest(b"cycle016-ai-parent-v4", splits, metrics, config)
    parent_v5 = {
        "version": 5, "parent_manifest_sha256": parent_v4["manifest_sha256"],
        "source_sha256": parent_v4["source_sha256"], "split_hashes": parent_v4["split_hashes"],
        "metrics_sha256": parent_v4["metrics_sha256"], "config_sha256": parent_v4["config_sha256"],
        "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None,
    }
    parent_v5["manifest_sha256"] = canonical_hash(parent_v5)
    ai = ai_lineage_manifest_v6(parent_v5, b"cycle016-ai-source-v6", splits, metrics, config)

    qos = qos_mutation_gate()
    return {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g, "H": h,
            "FND/EQN": fnd, "SCM": scm, "AI-COST": ai, "QOS/QSVT": qos}
