"""Cycle 018 bounded synchronized fixtures; synthetic/model/fiction evidence only."""
from __future__ import annotations

import hashlib
import hmac
import math
import os
import struct
import tempfile
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_bytes, canonical_hash
from uqpu.cycle014_delta01 import ai_lineage_manifest, fictional_transcript, qos_certificate_v4, run_cycle014_fixture
from uqpu.cycle015_delta01 import (
    component_covariance_sweep, concurrent_subprocess_replace, correlation_ranking_grid,
    make_custody_event, rational_interval_composition, typed_covariance_block, verify_custody_chain,
    qos_er6_reconstruction_v5,
)
from uqpu.cycle016_delta01 import ai_lineage_manifest_v6, exact_maxcut_10_node, rational_interval_divide, zip64_central_entry_gate

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")


def _finite(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool) and math.isfinite(float(value))


GRAPH_BASE = [[0, 1, 4], [0, 3, 7], [0, 6, 2], [1, 2, 5], [1, 5, 3], [2, 3, 6],
              [2, 7, 4], [3, 4, 8], [4, 5, 2], [4, 8, 5], [5, 6, 7], [6, 7, 3],
              [7, 8, 6], [8, 9, 4], [2, 9, 1]]


def maxcut_third_perturbation():
    variants = {
        "unchanged": [list(edge) for edge in GRAPH_BASE],
        "edge_0_plus_one": [[u, v, w + (1 if i == 0 else 0)] for i, (u, v, w) in enumerate(GRAPH_BASE)],
        "edge_0_plus_two": [[u, v, w + (2 if i == 0 else 0)] for i, (u, v, w) in enumerate(GRAPH_BASE)],
    }
    rows = []
    for name, graph in variants.items():
        result = exact_maxcut_10_node(graph)
        permutation = exact_maxcut_10_node([[v, u, w] for u, v, w in reversed(graph)])
        if result["task_sha256"] != permutation["task_sha256"] or result["result_sha256"] != permutation["result_sha256"]:
            raise AssertionError("canonical edge presentation changed result")
        rows.append({"variant": name, "task_sha256": result["task_sha256"],
                     "result_sha256": result["result_sha256"], "state_count": result["state_count"],
                     "objective": result["best_cut_weight"], "witness_sha256": result["witness_sha256"],
                     "scaling_claim": None})
    if rows[0]["task_sha256"] == rows[1]["task_sha256"] or rows[1]["task_sha256"] == rows[2]["task_sha256"]:
        raise AssertionError("weight mutation did not change task identity")
    return {"variants": rows, "unchanged_edges_invariant": True, "changed_edge_index": 0,
            "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE", "scaling_claim": None}


def make_receipt_v5(request_sha256, scope, key_id, fixture_key):
    if fixture_key is None or key_id is None or scope is None:
        return {"receipt": None, "provider_claim": None, "status": "NULL_MISSING_EXTERNAL_AUTHENTICATION"}
    body = {"schema": "receipt-v5", "request_sha256": request_sha256, "provider_status": "NOT_EXECUTED",
            "authorization_scope": scope, "authorized": False, "key_id": key_id,
            "job_id": None, "invoice": None}
    signature = hmac.new(fixture_key, canonical_bytes(body), hashlib.sha256).hexdigest()
    return {"receipt": {**body, "signature_algorithm": "HMAC-SHA256-FIXTURE", "signature": signature,
                        "provider_claim": None}, "status": "SYNTHETIC_ONLY"}


def verify_receipt_v5(receipt, request_sha256, expected_scope, keyring):
    body_keys = {"schema", "request_sha256", "provider_status", "authorization_scope", "authorized", "key_id", "job_id", "invoice"}
    if not isinstance(receipt, dict) or set(receipt) != body_keys | {"signature_algorithm", "signature", "provider_claim"}:
        return False
    if (receipt["schema"] != "receipt-v5" or receipt["request_sha256"] != request_sha256
            or receipt["authorization_scope"] != expected_scope or receipt["authorized"] is not False
            or receipt["provider_status"] != "NOT_EXECUTED" or receipt["job_id"] is not None
            or receipt["invoice"] is not None or receipt["signature_algorithm"] != "HMAC-SHA256-FIXTURE"
            or receipt["provider_claim"] is not None):
        return False
    key = keyring.get(receipt["key_id"]) if isinstance(keyring, dict) else None
    if not isinstance(key, bytes) or not key:
        return False
    body = {field: receipt[field] for field in body_keys}
    expected = hmac.new(key, canonical_bytes(body), hashlib.sha256).hexdigest()
    return isinstance(receipt["signature"], str) and hmac.compare_digest(expected, receipt["signature"])


def receipt_v5_mutation_matrix():
    keyring = {"fixture-k1": b"cycle018-fixture-key-1", "fixture-k2": b"cycle018-fixture-key-2"}
    request = canonical_hash({"cycle": 18, "payload": "synthetic"})
    one = make_receipt_v5(request, "fixture-only", "fixture-k1", keyring["fixture-k1"])["receipt"]
    two = make_receipt_v5(request, "fixture-only", "fixture-k2", keyring["fixture-k2"])["receipt"]
    cases = {
        "canonical_reordering": verify_receipt_v5(dict(reversed(list(two.items()))), request, "fixture-only", keyring),
        "rotated_key": verify_receipt_v5(one, request, "fixture-only", keyring) and verify_receipt_v5(two, request, "fixture-only", keyring),
        "scope_mutation_rejected": not verify_receipt_v5({**two, "authorization_scope": "other"}, request, "fixture-only", keyring),
        "request_mutation_rejected": not verify_receipt_v5({**two, "request_sha256": "0" * 64}, request, "fixture-only", keyring),
        "invoice_mutation_rejected": not verify_receipt_v5({**two, "invoice": {"amount": 1}}, request, "fixture-only", keyring),
        "key_rotation_mutation_rejected": not verify_receipt_v5({**two, "key_id": "fixture-k1"}, request, "fixture-only", keyring),
    }
    if not all(cases.values()):
        raise AssertionError("receipt-v5 canonical/key-rotation mutations")
    return {"cases": cases, "missing_external_authority_key_job_invoice": None,
            "provider_claim": None, "evidence_class": "SYNTHETIC_RECEIPT_V5"}


def _safe_target(target_name):
    return isinstance(target_name, str) and target_name not in ("", ".", "..") and Path(target_name).name == target_name and "/" not in target_name and "\\" not in target_name and "\x00" not in target_name


def stale_stage_exit_collision_gate(directory, target_name, payloads):
    if not _safe_target(target_name):
        raise ValueError("unsafe target-name collision")
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / target_name
    target.write_bytes(b"cycle018-complete-old")
    concurrent = concurrent_subprocess_replace(root, target_name, payloads)
    # Once all writers exit, the stale janitor may remove only the stale namespace.
    stale = root / f".{target_name}.tmp.stale.exit"
    stale.write_bytes(b"abandoned-after-process-exit")
    active = root / f".{target_name}.tmp.active.fixture"
    active.write_bytes(b"live-active-stage")
    for path in root.iterdir():
        if path.name.startswith(f".{target_name}.tmp.stale."):
            path.unlink()
    if not active.exists() or stale.exists():
        raise AssertionError("cleanup crossed active-stage namespace")
    active.unlink()
    leftovers = []
    for path in root.iterdir():
        if path.name.startswith(f".{target_name}.tmp.active."):
            path.unlink()
            leftovers.append(path.name)
    visible = target.read_bytes()
    if visible not in {b"cycle018-complete-old", *payloads} or not concurrent["visible_complete"]:
        raise AssertionError("target incomplete after stale-stage cleanup")
    return {"unsafe_name_rejected_before_write": True, "process_exit_codes": concurrent["exit_codes"],
            "live_name_survived_stale_cleanup": True, "stale_stage_removed_after_exit": True,
            "orphan_names_removed_after_all_exits": len(leftovers), "visible_payload_complete": True,
            "crash_durability": None, "evidence_class": "LOCAL_PROCESS_FIXTURE"}


def _zip18_records():
    name = b"cycle018.bin"
    crc, comp, uncomp, offset, disk, flags = 0x88112233, 8, 8, 64, 1, 8
    local = struct.pack("<4sHHHHHIIIHH", b"PK\x03\x04", 45, flags, 0, 0, 0, 0, 0, 0, len(name), 0) + name
    payload = struct.pack("<QQQI", uncomp, comp, offset, disk)
    extra = struct.pack("<HH", 1, len(payload)) + payload
    central = struct.pack("<4sHHHHHHIIIHHHHHII", b"PK\x01\x02", 45, 45, flags, 0, 0, 0,
                          crc, 0xFFFFFFFF, 0xFFFFFFFF, len(name), len(extra), 0, 0xFFFF, 0, 0, 0xFFFFFFFF) + name + extra
    descriptor = struct.pack("<4sIQQ", b"PK\x07\x08", crc, comp, uncomp)
    return local, central, descriptor, [128, 256], disk, offset


def zip18_crossbind(local, central, descriptor, disk_sizes, actual_disk, actual_offset):
    if not isinstance(local, bytes) or len(local) < 30:
        raise ValueError("local header truncated")
    sig, ver, flags, method, mtime, mdate, crc, c32, u32, nlen, elen = struct.unpack_from("<4sHHHHHIIIHH", local)
    if sig != b"PK\x03\x04" or len(local) != 30 + nlen + elen or nlen == 0:
        raise ValueError("local header shape")
    central_result = zip64_central_entry_gate(central, descriptor, disk_sizes)
    c_sig, made, needed, cflags, cmethod, ct, cd, ccrc, ccomp, cuncomp, cn, ce, cc, cdisk, ci, cx, coffset = struct.unpack_from("<4sHHHHHHIIIHHHHHII", central)
    local_name, central_name = local[30:30+nlen], central[46:46+cn]
    if flags != cflags or method != cmethod or local_name != central_name:
        raise ValueError("local/central flags/method/name mismatch")
    if actual_disk != central_result["disk"] or actual_offset != central_result["local_header_offset"]:
        raise ValueError("local/central disk/offset mismatch")
    if flags & 8:
        if crc not in (0, ccrc) or c32 not in (0, 0xFFFFFFFF) or u32 not in (0, 0xFFFFFFFF):
            raise ValueError("streaming local placeholder mismatch")
    elif crc != ccrc or c32 != central_result["compressed_size"] or u32 != central_result["uncompressed_size"]:
        raise ValueError("local/central CRC/size mismatch")
    extent = actual_offset + len(local) + central_result["compressed_size"] + len(descriptor)
    if extent > disk_sizes[actual_disk]:
        raise ValueError("entry extent exceeds disk")
    return {"name_sha256": hashlib.sha256(local_name).hexdigest(), "disk": actual_disk,
            "offset": actual_offset, "sizes": [central_result["compressed_size"], central_result["uncompressed_size"]],
            "cross_bound": True, "payload_read": False, "evidence_class": "SYNTHETIC_ZIP64_CROSS_BIND"}


def custody_terminal_revocation_suite(now):
    sample = hashlib.sha256(b"cycle018-synthetic-custody-sample").hexdigest()
    entries = [("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer")]
    events, prior = [], "0" * 64
    for seq, (issuer, scope) in enumerate(entries):
        item = make_custody_event(seq, sample, "fixture-018", issuer, scope, "2026-01-01", "2027-01-01", prior)
        events.append(item)
        prior = item["event_sha256"]
    registry = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-c": {"transfer"}}
    valid = verify_custody_chain(events, registry, now)
    if valid["final_event_sha256"] != events[-1]["event_sha256"]:
        raise AssertionError("terminal head mismatch")
    negatives = {}
    for name, candidate, allowed in [
        ("truncated", events[:-1], registry),
        ("replayed", [events[0], events[1], events[1]], registry),
        ("reordered", [events[0], events[2], events[1]], registry),
        ("revoked_issuer", events, {"issuer-a": {"intake"}, "issuer-b": {"storage"}}),
    ]:
        try:
            if name == "truncated" and len(candidate) != 3:
                raise ValueError("expected terminal count")
            observed = verify_custody_chain(candidate, allowed, now)
            if observed["final_event_sha256"] != events[-1]["event_sha256"]:
                raise ValueError("terminal head mismatch")
            negatives[name] = False
        except ValueError:
            negatives[name] = True
    if not all(negatives.values()):
        raise AssertionError("invalid custody chain accepted")
    return {"terminal_event_sha256": valid["final_event_sha256"], "negative_controls": negatives,
            "physical_sample_claim": None, "evidence_class": "SYNTHETIC_CUSTODY_NEGATIVE_CONTROL"}


def three_component_covariance_sweep():
    independent = [[.09, 0, 0], [0, .04, 0], [0, 0, .01]]
    correlated = [[.09, .03, .015], [.03, .04, .01], [.015, .01, .01]]
    invalid = [[1, 2, 0], [2, 1, 0], [0, 0, 1]]
    nonfinite = [[float("nan"), 0, 0], [0, 1, 0], [0, 0, 1]]
    result = component_covariance_sweep([[2, 3], [1, 2], [.5, 1.5]],
                                        {"independent": independent, "correlated": correlated,
                                         "invalid": invalid, "nonfinite": nonfinite}, [1, 2, 4, 0])
    return {**result, "evidence_class": "MODEL_ONLY", "commercial_interpretation": None}


def covariance_block_with_expected_order(items, entries, expected_order):
    if [item.get("id") for item in items] != expected_order:
        raise ValueError("covariance measurand order differs from preregistration")
    block = typed_covariance_block(items, entries)
    block["order_sha256"] = canonical_hash(expected_order)
    return block


def four_measurand_covariance_order_gate():
    items = [
        {"id": "length", "unit": "m", "dimension": [1, 0, 0, 0, 0, 0, 0]},
        {"id": "mass", "unit": "kg", "dimension": [0, 1, 0, 0, 0, 0, 0]},
        {"id": "duration", "unit": "s", "dimension": [0, 0, 1, 0, 0, 0, 0]},
        {"id": "current", "unit": "A", "dimension": [0, 0, 0, 1, 0, 0, 0]},
    ]
    ids = [item["id"] for item in items]
    entries = []
    for i, left in enumerate(items):
        row = []
        for j, right in enumerate(items):
            unit = "*".join(sorted((left["unit"], right["unit"])))
            dimension = [a + b for a, b in zip(left["dimension"], right["dimension"])]
            row.append({"value": 1.0 if i == j else 0.1, "unit": unit, "dimension": dimension})
        entries.append(row)
    block = covariance_block_with_expected_order(items, entries, ids)
    if block["measurand_order"] != ids:
        raise AssertionError("covariance order mismatch")
    return {**block, "calibration": None,
            "evidence_class": "SYNTHETIC_TYPED_FOUR_MEASURAND_COVARIANCE"}


def three_adverse_ranking_alternatives():
    baseline = ["compute", "memory", "energy", "latency"]
    identity = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    positive = [[1, .5, 0, 0], [.5, 1, 0, 0], [0, 0, 1, .4], [0, 0, .4, 1]]
    anti = [[1, .2, 0, 0], [.2, 1, 0, 0], [0, 0, 1, -.3], [0, 0, -.3, 1]]
    permutations = [baseline, ["memory", "compute", "energy", "latency"],
                    ["energy", "latency", "compute", "memory"], ["latency", "energy", "memory", "compute"]]
    alternatives = [
        {"name": "identity", "correlation": identity, "scenario_orders": permutations, "assumption": "identity scenario"},
        {"name": "positive-pairs", "correlation": positive, "scenario_orders": permutations[::-1], "assumption": "positive pair stress"},
        {"name": "mixed-adverse", "correlation": anti, "scenario_orders": permutations[1:] + permutations[:1], "assumption": "mixed signed pair stress"},
    ]
    result = correlation_ranking_grid(baseline, alternatives)
    return {**result, "declared_alternatives": 3,
            "declared_order_count": sum(row["scenario_count"] for row in result["alternatives"]),
            "capital": None, "evidence_class": "ILLUSTRATIVE_SCENARIO_GRID"}


def exact_cancel_expression(source_bytes):
    digest = hashlib.sha256(source_bytes).hexdigest()
    typed = {"domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": digest}
    length = {**typed, "unit": "m", "dimension": [1, 0, 0, 0, 0, 0, 0], "lower": [2, 1], "upper": [4, 1]}
    time = {**typed, "unit": "s", "dimension": [0, 0, 1, 0, 0, 0, 0], "lower": [2, 1], "upper": [4, 1]}
    speed = rational_interval_divide(length, time, source_bytes, {"m|s": {"unit": "m/s", "dimension": [1, 0, -1, 0, 0, 0, 0]}})["result"]
    recovered = rational_interval_composition(speed, time, "multiply", source_bytes,
                                               {"m/s|s": {"unit": "m", "dimension": [1, 0, 0, 0, 0, 0, 0]}})
    unity = rational_interval_divide(recovered, length, source_bytes,
                                     {"m|m": {"unit": "1", "dimension": [0, 0, 0, 0, 0, 0, 0]}})["result"]
    mismatch_rejected = False
    try:
        rational_interval_divide(length, {**length, "source_sha256": "0" * 64}, source_bytes,
                                 {"m|m": {"unit": "1", "dimension": [0, 0, 0, 0, 0, 0, 0]}})
    except ValueError:
        mismatch_rejected = True
    if not mismatch_rejected:
        raise AssertionError("source mismatch accepted")
    return {"speed": {"unit": speed["unit"], "lower": speed["lower"], "upper": speed["upper"]},
            "recovered_length": {"unit": recovered["unit"], "lower": recovered["lower"], "upper": recovered["upper"]},
            "dimensionless": {"unit": unity["unit"], "lower": unity["lower"], "upper": unity["upper"]},
            "source_mismatch_rejected": mismatch_rejected, "source_sha256": digest,
            "sort": [unity["domain_sort"], unity["evidence_sort"]], "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def scm_nonce_replacement_scope_transition(now):
    scope = "fiction-scope-v1"
    challenge1 = canonical_hash({"scope": scope, "nonce": "n1"})
    consent = {"fiction_only": True, "empirical_coupling": None, "seen": set(), "scope": scope,
               "active": True, "expires_at": "2030-01-01"}
    first = fictional_transcript(consent, "n1", scope, challenge1, challenge1, now)["accepted"]
    replaced_nonce = "n2"
    challenge2 = canonical_hash({"scope": scope, "nonce": replaced_nonce})
    after_first = {**consent, "seen": {"n1"}}
    replacement = fictional_transcript(after_first, replaced_nonce, scope, challenge2, challenge2, now)["accepted"]
    def rejected(candidate_consent, nonce, candidate_scope, challenge):
        try:
            fictional_transcript(candidate_consent, nonce, candidate_scope, challenge, challenge, now)
        except ValueError:
            return True
        return False
    replay = rejected({**after_first, "seen": {"n1", "n2"}}, "n1", scope, challenge1)
    new_scope = "fiction-scope-v2"
    scope_transition_rejected = rejected(after_first, "n3", new_scope, challenge2)
    cases = {"fresh": first, "replacement_nonce": replacement, "replay_rejected": replay,
             "unconsented_scope_transition_rejected": scope_transition_rejected}
    if not all(cases.values()):
        raise AssertionError("SCM consent/nonce boundary")
    return {"cases": cases, "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def ai_lineage_manifest_v8(parent_v7, source_bytes, splits, metrics, config):
    keys = {"version", "parent_manifest_sha256", "source_sha256", "split_hashes", "metrics_sha256", "config_sha256", "evidence_class", "functional_equivalence", "manifest_sha256"}
    if not isinstance(parent_v7, dict) or set(parent_v7) != keys or parent_v7["version"] != 7:
        raise ValueError("parent v7")
    parent_body = {k: v for k, v in parent_v7.items() if k != "manifest_sha256"}
    if canonical_hash(parent_body) != parent_v7["manifest_sha256"]:
        raise ValueError("parent v7 digest")
    if any(x is None for x in (source_bytes, splits, metrics, config)):
        return {"manifest": None, "candidate_result": None, "status": "NULL_MISSING_LINEAGE"}
    if (not isinstance(source_bytes, bytes) or not source_bytes or not isinstance(splits, dict)
            or set(splits) != {"train", "validation", "test"} or not isinstance(metrics, dict)
            or set(metrics) != {"train", "validation", "test"} or not isinstance(config, dict) or not config):
        return {"manifest": None, "candidate_result": None, "status": "NULL_INCOMPLETE_LINEAGE"}
    if any(not isinstance(splits[key], list) or not splits[key] for key in ("train", "validation", "test")):
        return {"manifest": None, "candidate_result": None, "status": "NULL_INCOMPLETE_SPLIT"}
    if any(not isinstance(metrics[key], dict) or not metrics[key] for key in ("train", "validation", "test")):
        return {"manifest": None, "candidate_result": None, "status": "NULL_MISSING_HELDOUT_METRIC"}
    split_hashes = {key: canonical_hash(sorted(splits[key], key=str)) for key in ("train", "validation", "test")}
    body = {"version": 8, "parent_manifest_sha256": parent_v7["manifest_sha256"],
            "source_sha256": hashlib.sha256(source_bytes).hexdigest(), "split_hashes": split_hashes,
            "metrics_sha256": canonical_hash(metrics), "config_sha256": canonical_hash(config),
            "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
    return {"manifest": {**body, "manifest_sha256": canonical_hash(body)}, "candidate_result": None,
            "status": "LINEAGE_BOUND_SYNTHETIC_ONLY"}


def qos_inverse_operator_pair():
    parent = run_cycle014_fixture()["QOS/QSVT"]
    forward = [{"op": "x", "target": 1}, {"op": "cx", "control": 1, "target": 4}, {"op": "x", "target": 5}]
    inverse = list(reversed(forward))
    pair = forward + inverse
    reconstruction = qos_er6_reconstruction_v5(parent, pair)
    source = b"cycle018-inverse-operator-fixture"
    semantic = {"width": 6, "bit_order": "little-endian", "pair": "U then U-inverse"}
    current = {"qubits": 6, "bits": 6, "depth": 6, "gates": 6}
    previous = {"qubits": 6, "bits": 6, "depth": 8, "gates": 8}
    cert = qos_certificate_v4(source, semantic, current, previous)
    parent_rejected = False
    try:
        qos_er6_reconstruction_v5({**parent, "certificate_sha256": "f" * 64}, pair)
    except ValueError:
        parent_rejected = True
    resource_rejected = False
    try:
        qos_certificate_v4(source, semantic, {**current, "depth": 9, "gates": 9}, previous)
    except ValueError:
        resource_rejected = True
    if not parent_rejected or not resource_rejected:
        raise AssertionError("QOS inverse pair mutation gate")
    return {"basis_states_checked": reconstruction["basis_states_checked"],
            "residual": reconstruction["maximum_integer_residual"],
            "resource_certificate_sha256": cert["certificate_sha256"],
            "resource_regression_rejected": resource_rejected, "parent_mutation_rejected": parent_rejected,
            "hardware": None, "evidence_class": "ER6_SYNTHETIC_INVERSE_PAIR"}


def run_cycle018_fixture(source_bytes):
    a = maxcut_third_perturbation()
    b = receipt_v5_mutation_matrix()
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle018-c-") as root:
        c = stale_stage_exit_collision_gate(root, "state.bin", [b"writer-a", b"writer-b", b"writer-c"])
    local, central, descriptor, disks, disk, offset = _zip18_records()
    d = zip18_crossbind(local, central, descriptor, disks, disk, offset)
    e = custody_terminal_revocation_suite("2026-09-28")
    f = three_component_covariance_sweep()
    g = four_measurand_covariance_order_gate()
    h = three_adverse_ranking_alternatives()
    fnd = exact_cancel_expression(source_bytes)
    scm = scm_nonce_replacement_scope_transition("2026-09-28")
    splits = {"train": ["t1", "t2"], "validation": ["v1"], "test": ["x1"]}
    metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
    config = {"seed": 18, "optimizer": "fixture"}
    p4 = ai_lineage_manifest(b"cycle018-ai-v4", splits, metrics, config)
    p5body = {"version": 5, "parent_manifest_sha256": p4["manifest_sha256"], "source_sha256": p4["source_sha256"],
              "split_hashes": p4["split_hashes"], "metrics_sha256": p4["metrics_sha256"], "config_sha256": p4["config_sha256"],
              "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
    p5 = {**p5body, "manifest_sha256": canonical_hash(p5body)}
    p6 = ai_lineage_manifest_v6(p5, b"cycle018-ai-v6", splits, metrics, config)["manifest"]
    p7body = {"version": 7, "parent_manifest_sha256": p6["manifest_sha256"], "source_sha256": p6["source_sha256"],
              "split_hashes": p6["split_hashes"], "metrics_sha256": p6["metrics_sha256"], "config_sha256": p6["config_sha256"],
              "evidence_class": "SYNTHETIC_DATA_LINEAGE", "functional_equivalence": None}
    p7 = {**p7body, "manifest_sha256": canonical_hash(p7body)}
    ai = ai_lineage_manifest_v8(p7, b"cycle018-ai-v8", splits, metrics, config)
    qos = qos_inverse_operator_pair()
    return {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g, "H": h,
            "FND/EQN": fnd, "SCM": scm, "AI-COST": ai, "QOS/QSVT": qos}
