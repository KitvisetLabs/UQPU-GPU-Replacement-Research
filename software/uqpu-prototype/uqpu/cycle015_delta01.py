"""Cycle 015 bounded cross-lane fixtures; synthetic and fiction-only."""
from __future__ import annotations

import hashlib
import json
import math
import os
import subprocess
import sys
import tempfile
import time
from pathlib import Path

from uqpu.cycle013_delta01 import _is_psd, canonical_hash, weighted_maxcut_13
from uqpu.cycle014_delta01 import (
    ai_lineage_manifest,
    custody_expiry_boundary,
    fictional_transcript,
    matched_output_contract,
    model_interval_grid,
    qos_certificate_v4,
    rank_stability_bounds,
    run_cycle014_fixture,
)

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")
HEX = set("0123456789abcdef")
_U64 = (1 << 64) - 1


def _finite(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(float(value))
    except (OverflowError, TypeError, ValueError):
        return False


def _digest(value):
    return isinstance(value, str) and len(value) == 64 and set(value) <= HEX


def _nonnegative_int(value):
    return isinstance(value, int) and not isinstance(value, bool) and value >= 0


# Lane A: the seed labels permute edge presentation only. Exact enumeration is
# deterministic and exhaustive, so the fixture makes no stochastic claim.
def matched_maxcut_seed_family(n, edges, seeds, max_states=1024):
    if not isinstance(seeds, (list, tuple)) or not seeds or len(set(seeds)) != len(seeds):
        raise ValueError("seed family")
    if any(not _nonnegative_int(seed) for seed in seeds):
        raise ValueError("seed value")
    if not isinstance(max_states, int) or isinstance(max_states, bool) or not 1 <= max_states <= 1024:
        raise ValueError("state bound")
    if (1 << n) > max_states:
        raise ValueError("state bound exceeded")
    normalized = []
    for edge in edges:
        if not isinstance(edge, (list, tuple)) or len(edge) != 3:
            raise ValueError("edge shape")
        u, v, weight = edge
        if not all(isinstance(x, int) and not isinstance(x, bool) for x in edge):
            raise ValueError("edge type")
        if u == v or weight <= 0 or min(u, v) < 0 or max(u, v) >= n:
            raise ValueError("edge range")
        normalized.append([min(u, v), max(u, v), weight])
    if len({(e[0], e[1]) for e in normalized}) != len(normalized):
        raise ValueError("duplicate edge")
    normalized.sort()
    task_sha = canonical_hash({"n": n, "edges": normalized})
    rows = []
    for seed in seeds:
        presented = sorted(
            normalized,
            key=lambda e: hashlib.sha256(canonical_hash({"seed": seed, "edge": e}).encode()).hexdigest(),
        )
        oriented = [([e[1], e[0], e[2]] if (seed + e[0] + e[1]) % 2 else list(e)) for e in presented]
        exact = weighted_maxcut_13(n, oriented, cap=max_states)
        workload = {
            "workload_id": "maxcut-five-node-v1",
            "baseline": "bounded-exhaustive-classical",
            "accepted_output": "exact-max-cut-weight",
            "output_unit": "integer-weight",
            "max_states": max_states,
            "seed": seed,
        }
        result = {
            "states": exact["states"],
            "best_cut_weight": exact["best_cut_weight"],
            "optimal_state_set_sha256": exact["optimal_state_set_sha256"],
            "graph_sha256": exact["graph_sha256"],
        }
        contract = matched_output_contract(workload, result)
        rows.append({
            "seed_label": seed,
            "edge_presentation_sha256": canonical_hash(oriented),
            "task_sha256": task_sha,
            "result": result,
            "contract": contract,
        })
    if len({row["task_sha256"] for row in rows}) != 1 or len({row["result"]["best_cut_weight"] for row in rows}) != 1:
        raise AssertionError("matched family diverged")
    return {
        "state_bound": max_states,
        "maximum_states_observed": max(row["result"]["states"] for row in rows),
        "task_sha256": task_sha,
        "rows": rows,
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
        "seed_semantics": "deterministic edge presentation labels; solver is exhaustive and nonrandom",
    }


# Lane B: unexecuted v2 receipts carry explicit but null authorization and
# signature slots. This function cannot emit a successful provider claim.
def provider_receipt_v2(request_sha256, receipt):
    keys = {
        "schema", "request_sha256", "provider_status", "authorization",
        "signature", "job_id", "invoice",
    }
    if not _digest(request_sha256) or not isinstance(receipt, dict) or set(receipt) != keys:
        raise ValueError("receipt-v2 schema")
    if receipt["schema"] != "receipt-v2" or receipt["request_sha256"] != request_sha256:
        raise ValueError("receipt binding")
    if receipt["provider_status"] != "NOT_EXECUTED":
        raise ValueError("provider success requires external authorization and verified receipt")
    if any(receipt[k] is not None for k in ("authorization", "signature", "job_id", "invoice")):
        raise ValueError("missing provider evidence must remain null")
    return {
        **receipt,
        "provider_claim": None,
        "evidence_class": "SYNTHETIC_RECEIPT_ENVELOPE",
    }


# Lane C: all subprocesses stage distinct complete payloads before a parent
# barrier. The janitor touches only the reserved stale namespace.
def concurrent_subprocess_replace(directory, target_name, payloads, timeout=8.0):
    if (not isinstance(target_name, str) or not target_name or Path(target_name).name != target_name
            or not isinstance(payloads, (list, tuple)) or len(payloads) < 3
            or any(not isinstance(payload, bytes) or not payload for payload in payloads)):
        raise ValueError("writer inputs")
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / target_name
    if not target.exists():
        target.write_bytes(b"old-complete-payload")
    old = target.read_bytes()
    actions = ["replace", "exit_before_replace", "replace_then_exit"]
    children = r'''
import hashlib, json, os, sys, time, tempfile
from pathlib import Path
root = Path(sys.argv[1]); target = root / sys.argv[2]
payload = bytes.fromhex(sys.argv[3]); marker = root / sys.argv[4]
release = root / sys.argv[5]; action = sys.argv[6]
fd, staged = tempfile.mkstemp(prefix=f".{target.name}.tmp.active.", dir=root)
with os.fdopen(fd, "wb") as handle:
    handle.write(payload)
marker.write_text(json.dumps({"staged": Path(staged).name, "sha256": hashlib.sha256(payload).hexdigest()}), encoding="utf-8")
deadline = time.monotonic() + 7.0
while not release.exists():
    if time.monotonic() >= deadline:
        os._exit(24)
    time.sleep(0.005)
if action == "exit_before_replace":
    os._exit(23)
os.replace(staged, target)
if action == "replace_then_exit":
    os._exit(23)
'''
    procs = []
    marker_names = []
    active_names = []
    release = root / ".cycle015.release"
    release.unlink(missing_ok=True)
    try:
        for idx, (payload, action) in enumerate(zip(payloads[:3], actions)):
            marker_name = f".cycle015.writer.{idx}.ready"
            marker_names.append(marker_name)
            procs.append(subprocess.Popen(
                [sys.executable, "-c", children, str(root), target_name, payload.hex(), marker_name, str(release), action],
                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            ))
        deadline = time.monotonic() + timeout
        staged_records = None
        while staged_records is None:
            if all((root / name).is_file() for name in marker_names):
                try:
                    candidate = [json.loads((root / name).read_text(encoding="utf-8"))
                                 for name in marker_names]
                    if all(set(record) == {"staged", "sha256"} for record in candidate):
                        staged_records = candidate
                        break
                except (OSError, json.JSONDecodeError):
                    # A pathname can become visible before write_text closes the
                    # marker. Treat only a complete JSON record as barrier-ready.
                    pass
            if time.monotonic() >= deadline:
                raise TimeoutError("subprocess writers did not reach the barrier")
            time.sleep(0.005)
        active_names = [record["staged"] for record in staged_records]
        before = []
        for record in staged_records:
            staged = root / record["staged"]
            raw = staged.read_bytes()
            digest = hashlib.sha256(raw).hexdigest()
            if digest != record["sha256"] or raw not in payloads:
                raise AssertionError("active staged payload incomplete")
            before.append(digest)
        stale = root / f".{target_name}.tmp.stale.fixture"
        stale.write_bytes(b"stale-only")
        for path in root.iterdir():
            if path.name.startswith(f".{target_name}.tmp.stale.") and path.is_file():
                path.unlink()
        if stale.exists() or any(not (root / name).exists() for name in active_names):
            raise AssertionError("stale cleanup crossed active writer namespace")
        release.write_text("go", encoding="ascii")
        exit_codes = [proc.wait(timeout=timeout) for proc in procs]
        if exit_codes != [0, 23, 23]:
            raise AssertionError(f"unexpected writer exit codes: {exit_codes}")
        visible = target.read_bytes()
        complete = {old, *payloads[:3]}
        if visible not in complete:
            raise AssertionError("visible target is not a complete writer payload")
        return {
            "writer_count": len(procs),
            "active_payload_sha256_at_barrier": before,
            "active_names_survived_stale_cleanup": True,
            "exit_codes": exit_codes,
            "visible_sha256": hashlib.sha256(visible).hexdigest(),
            "visible_complete": True,
            "durability": "PROCESS_TERMINATION_ONLY",
            "evidence_class": "CONCURRENT_PROCESS_FIXTURE",
        }
    finally:
        for proc in procs:
            if proc.poll() is None:
                proc.kill()
                proc.wait()
        for name in marker_names:
            (root / name).unlink(missing_ok=True)
        release.unlink(missing_ok=True)


# Lane D: parse only ZIP64 metadata. The supported subset requires a complete
# central directory to fit on its declared disk; archive payload is untouched.
def zip64_multidisk_gate(zip64_end, locator, eocd, zip64_start, locator_start,
                         eocd_start, disk_sizes):
    if not all(isinstance(value, bytes) for value in (zip64_end, locator, eocd)):
        raise ValueError("metadata bytes")
    if len(zip64_end) < 56 or len(locator) != 20 or len(eocd) < 22:
        raise ValueError("metadata widths")
    if any(not _nonnegative_int(x) for x in (zip64_start, locator_start, eocd_start)):
        raise ValueError("metadata offsets")
    if not isinstance(disk_sizes, (list, tuple)) or not disk_sizes or any(not _nonnegative_int(x) or x == 0 for x in disk_sizes):
        raise ValueError("disk sizes")
    signature, record_size = __import__("struct").unpack_from("<4sQ", zip64_end)
    if signature != b"PK\x06\x06" or record_size < 44 or record_size > _U64 - 12:
        raise ValueError("ZIP64 end signature/size")
    if 12 + record_size != len(zip64_end):
        raise ValueError("ZIP64 extensible record length")
    import struct
    (made_by, needed, zip64_disk, central_disk, entries_on_disk, total_entries,
     central_size, central_offset) = struct.unpack_from("<HHIIQQQQ", zip64_end, 12)
    extensible = zip64_end[56:]
    cursor = 0
    extension_ids = []
    while cursor < len(extensible):
        if len(extensible) - cursor < 6:
            raise ValueError("truncated extensible data header")
        header_id, data_size = struct.unpack_from("<HI", extensible, cursor)
        cursor += 6
        if data_size > len(extensible) - cursor:
            raise ValueError("extensible data length")
        extension_ids.append(header_id)
        cursor += data_size
    loc_sig, locator_disk, locator_offset, total_disks = struct.unpack("<4sIQI", locator)
    if loc_sig != b"PK\x06\x07" or total_disks != len(disk_sizes) or total_disks < 1:
        raise ValueError("ZIP64 locator signature/disk count")
    if zip64_disk >= total_disks or central_disk >= total_disks or locator_disk != zip64_disk:
        raise ValueError("ZIP64 disk index")
    if zip64_start + len(zip64_end) != locator_start or locator_start + len(locator) != eocd_start:
        raise ValueError("metadata adjacency")
    if eocd_start + len(eocd) > disk_sizes[-1] or zip64_start + len(zip64_end) > disk_sizes[zip64_disk]:
        raise ValueError("metadata exceeds disk extent")
    if locator_offset != zip64_start or entries_on_disk > total_entries:
        raise ValueError("locator offset/count consistency")
    if central_offset > _U64 - central_size or central_offset + central_size > disk_sizes[central_disk]:
        raise ValueError("central directory offset/extent")
    eocd_sig, disk_no, cd_disk, entries_legacy_disk, entries_legacy_total, size_legacy, offset_legacy, comment_len = struct.unpack_from("<4sHHHHIIH", eocd)
    if eocd_sig != b"PK\x05\x06" or len(eocd) != 22 + comment_len:
        raise ValueError("EOCD signature/comment")
    def matches_or_sentinel(legacy, wide, sentinels):
        return legacy in sentinels or legacy == wide
    if not (
        matches_or_sentinel(disk_no, zip64_disk, {0xFFFF})
        and matches_or_sentinel(cd_disk, central_disk, {0xFFFF})
        and matches_or_sentinel(entries_legacy_disk, entries_on_disk, {0xFFFF})
        and matches_or_sentinel(entries_legacy_total, total_entries, {0xFFFF})
        and matches_or_sentinel(size_legacy, central_size, {0xFFFFFFFF})
        and matches_or_sentinel(offset_legacy, central_offset, {0xFFFFFFFF})
    ):
        raise ValueError("legacy ZIP fields disagree with ZIP64 values")
    return {
        "zip64_eocd_bytes": len(zip64_end),
        "extensible_data_bytes": len(extensible),
        "extension_ids": extension_ids,
        "total_disks": total_disks,
        "entries_on_disk": entries_on_disk,
        "total_entries": total_entries,
        "central_directory_disk": central_disk,
        "central_directory_offset": central_offset,
        "central_directory_size": central_size,
        "payload_read": False,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


# Lane E: hashes bind custody events; authorization changes are explicit and
# limited to registered issuer/scope pairs. Expiry is half-open: valid_from <= t < expires.
def make_custody_event(sequence, sample_sha256, path_id, issuer, scope,
                       valid_from, expires_at, previous_event_sha256):
    body = {
        "sequence": sequence,
        "sample_sha256": sample_sha256,
        "path_id": path_id,
        "issuer": issuer,
        "scope": scope,
        "valid_from": valid_from,
        "expires_at": expires_at,
        "previous_event_sha256": previous_event_sha256,
    }
    return {**body, "event_sha256": canonical_hash(body)}


def verify_custody_chain(events, issuer_scopes, now):
    from uqpu.cycle013_delta01 import _iso_day
    if not isinstance(events, list) or not events or not isinstance(issuer_scopes, dict):
        raise ValueError("custody chain")
    prior = "0" * 64
    first_sample = events[0].get("sample_sha256")
    path_id = events[0].get("path_id")
    seen_issuers = []
    for idx, event in enumerate(events):
        keys = {"sequence", "sample_sha256", "path_id", "issuer", "scope", "valid_from", "expires_at", "previous_event_sha256", "event_sha256"}
        if not isinstance(event, dict) or set(event) != keys:
            raise ValueError("custody event schema")
        body = {k: event[k] for k in keys if k != "event_sha256"}
        if (event["sequence"] != idx or event["previous_event_sha256"] != prior
                or event["sample_sha256"] != first_sample or event["path_id"] != path_id
                or not _digest(event["sample_sha256"]) or event["event_sha256"] != canonical_hash(body)):
            raise ValueError("custody hash/continuity")
        allowed = issuer_scopes.get(event["issuer"], ())
        start, expiry, current = _iso_day(event["valid_from"]), _iso_day(event["expires_at"]), _iso_day(now)
        if event["scope"] not in allowed or not start <= current < expiry:
            raise ValueError("custody issuer/scope/validity")
        prior = event["event_sha256"]
        seen_issuers.append(event["issuer"])
    return {
        "event_count": len(events),
        "final_event_sha256": prior,
        "issuer_sequence": seen_issuers,
        "same_sample_and_path": True,
        "evidence_class": "SYNTHETIC_CUSTODY_CHAIN",
        "physical_sample_claim": None,
    }


# Lane F: a finite interval model with covariance stress. Invalid covariance or
# a nonpositive denominator propagates null, never a guessed zero.
def component_covariance_sweep(component_intervals, covariance_scenarios, output_counts, sigma=1.0):
    if (not isinstance(component_intervals, list) or not component_intervals
            or any(not isinstance(x, (list, tuple)) or len(x) != 2 or any(not _finite(v) or v < 0 for v in x) or x[1] < x[0] for x in component_intervals)
            or not isinstance(covariance_scenarios, dict) or not covariance_scenarios
            or not isinstance(output_counts, list) or not _finite(sigma) or sigma < 0):
        raise ValueError("model input")
    base_low = sum(float(x[0]) for x in component_intervals)
    base_high = sum(float(x[1]) for x in component_intervals)
    if not _finite(base_low) or not _finite(base_high):
        raise ValueError("component overflow")
    output = {}
    n = len(component_intervals)
    for name, matrix in covariance_scenarios.items():
        if not isinstance(name, str) or not name:
            raise ValueError("scenario identity")
        valid = isinstance(matrix, (list, tuple)) and len(matrix) == n and _is_psd(matrix)
        rows = []
        if valid:
            variance = sum(float(matrix[i][j]) for i in range(n) for j in range(n))
            valid = _finite(variance) and variance >= -1e-10
        else:
            variance = None
        if valid:
            sd = math.sqrt(max(0.0, variance))
            low = max(0.0, base_low - sigma * sd)
            high = base_high + sigma * sd
            valid = _finite(low) and _finite(high)
        if not valid:
            rows = [{"accepted_outputs": c, "per_output_usd": None, "status": "NULL_INVALID_COVARIANCE"} for c in output_counts]
        else:
            bounds = [low, high]
            rows = model_interval_grid(bounds, output_counts)
            for row in rows:
                if row["status"] == "MODEL_ONLY":
                    row["status"] = "MODEL_ONLY_COVARIANCE_STRESS"
        output[name] = {"total_usd": [low, high] if valid else None, "outputs": rows}
    return {
        "components": len(component_intervals),
        "sigma_multiplier": float(sigma),
        "scenarios": output,
        "evidence_class": "MODEL_ONLY",
        "commercial_interpretation": None,
    }


# Lane G: a full symmetric typed covariance matrix with product dimensions and
# deterministically derived product unit labels.
def typed_covariance_block(measurands, entries):
    if not isinstance(measurands, list) or not measurands or not isinstance(entries, list):
        raise ValueError("covariance block")
    n = len(measurands)
    for item in measurands:
        if (not isinstance(item, dict) or set(item) != {"id", "unit", "dimension"}
                or not isinstance(item["id"], str) or not item["id"]
                or not isinstance(item["unit"], str) or not item["unit"]
                or not isinstance(item["dimension"], list) or not item["dimension"]
                or any(not isinstance(x, int) or isinstance(x, bool) for x in item["dimension"])):
            raise ValueError("measurand type")
    if len({item["id"] for item in measurands}) != n or len({len(item["dimension"]) for item in measurands}) != 1:
        raise ValueError("measurand identity/dimension width")
    if len(entries) != n or any(not isinstance(row, list) or len(row) != n for row in entries):
        raise ValueError("covariance matrix shape")
    values = []
    for i in range(n):
        row_values = []
        for j in range(n):
            entry = entries[i][j]
            if not isinstance(entry, dict) or set(entry) != {"value", "unit", "dimension"} or not _finite(entry["value"]):
                raise ValueError("covariance entry")
            left, right = measurands[i], measurands[j]
            expected_unit = "*".join(sorted((left["unit"], right["unit"])))
            expected_dimension = [a + b for a, b in zip(left["dimension"], right["dimension"])]
            if entry["unit"] != expected_unit or entry["dimension"] != expected_dimension:
                raise ValueError("covariance product unit/dimension")
            row_values.append(float(entry["value"]))
        values.append(row_values)
    for i in range(n):
        for j in range(n):
            if values[i][j] != values[j][i]:
                raise ValueError("covariance symmetry")
    if not _is_psd(values):
        raise ValueError("covariance not positive semidefinite")
    return {
        "measurand_order": [item["id"] for item in measurands],
        "matrix": values,
        "positive_semidefinite": True,
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


# Lane H: correlation settings and rankings are explicitly declared scenario
# alternatives. The output is a finite-grid range, not a probability interval.
def correlation_ranking_grid(baseline, alternatives):
    if not isinstance(alternatives, list) or not alternatives:
        raise ValueError("ranking alternatives")
    all_bounds = []
    rows = []
    for alternative in alternatives:
        if not isinstance(alternative, dict) or set(alternative) != {"name", "correlation", "scenario_orders", "assumption"}:
            raise ValueError("ranking alternative schema")
        matrix = alternative["correlation"]
        if (not isinstance(matrix, list) or len(matrix) != len(baseline)
                or any(not isinstance(row, list) or len(row) != len(baseline) for row in matrix)
                or any(not _finite(x) or abs(x) > 1 for row in matrix for x in row)
                or any(abs(matrix[i][i] - 1.0) > 1e-12 for i in range(len(baseline)))
                or any(abs(matrix[i][j] - matrix[j][i]) > 1e-12 for i in range(len(baseline)) for j in range(len(baseline)))
                or not _is_psd(matrix)):
            raise ValueError("correlation matrix")
        result = rank_stability_bounds(baseline, alternative["scenario_orders"])
        bounds = result["stability_bounds"]
        all_bounds.append(bounds)
        rows.append({"name": alternative["name"], "correlation": matrix, "stability_bounds": bounds, "scenario_count": result["scenario_count"], "assumption": alternative["assumption"]})
    return {
        "alternatives": rows,
        "observed_stability_range": [min(x[0] for x in all_bounds), max(x[1] for x in all_bounds)],
        "capital": None,
        "evidence_class": "ILLUSTRATIVE_SCENARIO_GRID",
        "interpretation": "finite declared alternatives; no distribution or capital estimate",
    }


# Lane FND/EQN: exact rational interval arithmetic with an explicit registered
# product table and a content hash of the governing typed-language source.
def _fraction(pair):
    from fractions import Fraction
    if (not isinstance(pair, (list, tuple)) or len(pair) != 2
            or any(not isinstance(x, int) or isinstance(x, bool) for x in pair) or pair[1] <= 0):
        raise ValueError("rational endpoint")
    return Fraction(pair[0], pair[1])


def rational_interval_composition(left, right, operation, source_bytes, unit_products=None):
    from fractions import Fraction
    keys = {"unit", "dimension", "domain_sort", "evidence_sort", "source_sha256", "lower", "upper"}
    if not isinstance(left, dict) or not isinstance(right, dict) or set(left) != keys or set(right) != keys:
        raise ValueError("typed interval schema")
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("typed source bytes")
    expected_source = hashlib.sha256(source_bytes).hexdigest()
    if left["source_sha256"] != expected_source or right["source_sha256"] != expected_source:
        raise ValueError("typed source binding")
    if left["domain_sort"] != right["domain_sort"] or left["evidence_sort"] != right["evidence_sort"]:
        raise ValueError("sort mismatch")
    if left["domain_sort"] not in ("RealModel", "Fiction") or (left["domain_sort"] == "Fiction") != (left["evidence_sort"] == "Fiction"):
        raise ValueError("cross-sort firewall")
    if (not isinstance(left["dimension"], list) or not isinstance(right["dimension"], list)
            or len(left["dimension"]) != len(right["dimension"])
            or any(not isinstance(x, int) or isinstance(x, bool) for x in left["dimension"] + right["dimension"])):
        raise ValueError("dimension vector")
    lo1, hi1, lo2, hi2 = _fraction(left["lower"]), _fraction(left["upper"]), _fraction(right["lower"]), _fraction(right["upper"])
    if lo1 > hi1 or lo2 > hi2:
        raise ValueError("interval order")
    if operation == "add":
        if left["unit"] != right["unit"] or left["dimension"] != right["dimension"]:
            raise ValueError("addition unit/dimension mismatch")
        unit, dimension = left["unit"], list(left["dimension"])
        lo, hi = lo1 + lo2, hi1 + hi2
    elif operation == "multiply":
        if not isinstance(unit_products, dict):
            raise ValueError("unit product registry")
        pair = tuple(sorted((left["unit"], right["unit"])))
        spec = unit_products.get("|".join(pair))
        dim = [a + b for a, b in zip(left["dimension"], right["dimension"])]
        if not isinstance(spec, dict) or set(spec) != {"unit", "dimension"} or spec["dimension"] != dim:
            raise ValueError("unregistered unit product")
        unit, dimension = spec["unit"], dim
        products = [lo1 * lo2, lo1 * hi2, hi1 * lo2, hi1 * hi2]
        lo, hi = min(products), max(products)
    else:
        raise ValueError("operation")
    return {
        "unit": unit,
        "dimension": dimension,
        "domain_sort": left["domain_sort"],
        "evidence_sort": left["evidence_sort"],
        "source_sha256": expected_source,
        "lower": [lo.numerator, lo.denominator],
        "upper": [hi.numerator, hi.denominator],
    }


# Lane SCM: invalid fictional transcripts are rejected; every output remains
# explicitly fiction-only and empirically uncoupled.
def scm_fictional_rejection_suite(now):
    good = {
        "fiction_only": True, "empirical_coupling": None, "seen": set(),
        "scope": "scene-alpha", "active": True, "expires_at": "2030-01-01",
    }
    cases = {
        "revoked": ({**good, "active": False}, "nonce-revoked", "scene-alpha"),
        "expired": ({**good, "expires_at": now}, "nonce-expired", "scene-alpha"),
        "replayed": ({**good, "seen": {"nonce-replay"}}, "nonce-replay", "scene-alpha"),
        "out_of_scope": (good, "nonce-scope", "scene-beta"),
    }
    results = {}
    for name, (consent, nonce, scope) in cases.items():
        try:
            fictional_transcript(consent, nonce, scope, "challenge", "challenge", now)
            results[name] = "UNEXPECTED_ACCEPT"
        except (ValueError, TypeError):
            results[name] = "REJECTED"
    if any(value != "REJECTED" for value in results.values()):
        raise AssertionError("SCM negative control accepted")
    return {"negative_controls": results, "fiction_only": True, "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


# Lane AI-COST: a v5 manifest is linked to and verifies its v4 parent. Metrics
# remain synthetic; absent inputs return a null candidate result.
def _verify_v4_parent(parent):
    expected = {"version", "source_sha256", "split_hashes", "metrics_sha256", "config_sha256", "evidence_class", "manifest_sha256"}
    if not isinstance(parent, dict) or set(parent) != expected or parent["version"] != 4:
        return False
    body = {k: parent[k] for k in expected if k != "manifest_sha256"}
    return parent["manifest_sha256"] == canonical_hash(body)


def ai_lineage_manifest_v5(parent_v4, source_bytes, splits, metrics, config):
    if not _verify_v4_parent(parent_v4):
        raise ValueError("v4 parent manifest")
    if source_bytes is None or splits is None or metrics is None or config is None:
        return {"manifest": None, "candidate_result": None, "status": "NULL_MISSING_LINEAGE"}
    current_v4 = ai_lineage_manifest(source_bytes, splits, metrics, config)
    body = {
        "version": 5,
        "parent_manifest_sha256": parent_v4["manifest_sha256"],
        "source_sha256": current_v4["source_sha256"],
        "split_hashes": current_v4["split_hashes"],
        "metrics_sha256": current_v4["metrics_sha256"],
        "config_sha256": current_v4["config_sha256"],
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
        "functional_equivalence": None,
    }
    return {"manifest": {**body, "manifest_sha256": canonical_hash(body)}, "candidate_result": None, "status": "LINEAGE_BOUND_SYNTHETIC_ONLY"}


def verify_ai_lineage_manifest_v5(manifest, parent_v4, source_bytes, splits, metrics, config):
    expected = ai_lineage_manifest_v5(parent_v4, source_bytes, splits, metrics, config)
    return manifest == expected


# Lane QOS/QSVT: compare two independent representations of a bounded 6-bit
# permutation circuit, then bind source/map/resources to the preceding v4 cert.
def _apply_gate_word(state, gate):
    if gate["op"] == "x":
        return state ^ (1 << gate["target"])
    if gate["op"] == "cx":
        return state ^ ((1 << gate["target"]) if ((state >> gate["control"]) & 1) else 0)
    raise ValueError("gate operation")


def _permutation_matrix(width, gates):
    size = 1 << width
    matrix = [[int(row == column) for column in range(size)] for row in range(size)]
    for gate in gates:
        elementary = [[0] * size for _ in range(size)]
        for column in range(size):
            if gate["op"] == "x":
                row = column ^ (1 << gate["target"])
            elif gate["op"] == "cx":
                row = column ^ (1 << gate["target"] if (column & (1 << gate["control"])) else 0)
            else:
                raise ValueError("gate operation")
            elementary[row][column] = 1
        # Compose explicit 64x64 gate matrices independently of the direct
        # bit-word simulator used for the basis-state comparison.
        matrix = [
            [sum(elementary[row][k] * matrix[k][column] for k in range(size)) for column in range(size)]
            for row in range(size)
        ]
    return matrix


def qos_er6_reconstruction_v5(parent_certificate_v4, gates):
    parent_keys = {"version", "source_sha256", "map_sha256", "resources", "previous_resources", "hardware", "evidence_class", "certificate_sha256"}
    if not isinstance(parent_certificate_v4, dict) or set(parent_certificate_v4) != parent_keys or parent_certificate_v4["version"] != 4:
        raise ValueError("parent QOS certificate")
    parent_body = {k: parent_certificate_v4[k] for k in parent_keys if k != "certificate_sha256"}
    if canonical_hash(parent_body) != parent_certificate_v4["certificate_sha256"] or parent_certificate_v4["hardware"] is not None:
        raise ValueError("parent QOS digest/hardware")
    if not isinstance(gates, list) or not gates:
        raise ValueError("ER6 gates")
    for gate in gates:
        if not isinstance(gate, dict) or gate.get("op") not in ("x", "cx"):
            raise ValueError("ER6 gate")
        wires = [gate.get("target")] + ([gate.get("control")] if gate["op"] == "cx" else [])
        if any(not isinstance(w, int) or isinstance(w, bool) or not 0 <= w < 6 for w in wires):
            raise ValueError("ER6 wire")
        if gate["op"] == "cx" and gate["control"] == gate["target"]:
            raise ValueError("ER6 control/target")
    matrix = _permutation_matrix(6, gates)
    residual = 0
    for basis in range(64):
        direct = basis
        for gate in gates:
            direct = _apply_gate_word(direct, gate)
        reconstructed = next(row for row in range(64) if matrix[row][basis] == 1)
        residual = max(residual, abs(direct - reconstructed))
        if sum(matrix[row][basis] for row in range(64)) != 1:
            raise AssertionError("non-unit column")
    source_bytes = json.dumps(gates, sort_keys=True, separators=(",", ":")).encode()
    semantic_map = {"width": 6, "bit_order": "little-endian", "input_to_output": "basis permutation"}
    current = qos_certificate_v4(
        source_bytes, semantic_map,
        {"qubits": 6, "bits": 6, "depth": len(gates), "gates": len(gates)},
        {"qubits": 6, "bits": 6, "depth": 14, "gates": 30},
    )
    body = {
        "version": 5,
        "parent_certificate_v4_sha256": parent_certificate_v4["certificate_sha256"],
        "certificate_v4": current,
        "reconstruction": "independent basis-permutation matrix versus gate-word simulation",
        "basis_states_checked": 64,
        "permutation_matrix_sha256": canonical_hash(matrix),
        "maximum_integer_residual": residual,
        "hardware": None,
        "evidence_class": "ER6_SYNTHETIC_RECONSTRUCTION",
    }
    return {**body, "reconstruction_sha256": canonical_hash(body)}


def run_cycle015_fixture(source_bytes):
    graph = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 5), (2, 4, 2), (3, 4, 4)]
    a = matched_maxcut_seed_family(5, graph, [0, 1, 7, 31], 1024)

    request_sha = canonical_hash({"request": "synthetic-unexecuted", "cycle": 15})
    b = provider_receipt_v2(request_sha, {
        "schema": "receipt-v2", "request_sha256": request_sha, "provider_status": "NOT_EXECUTED",
        "authorization": None, "signature": None, "job_id": None, "invoice": None,
    })

    with tempfile.TemporaryDirectory(prefix="uqpu-cycle015-c-") as temp:
        c = concurrent_subprocess_replace(temp, "target.bin", [b"writer-a-complete", b"writer-b-complete", b"writer-c-complete"])

    import struct
    ext = struct.pack("<HI", 0xCAFE, 3) + b"xyz"
    zip64 = struct.pack("<4sQHHIIQQQQ", b"PK\x06\x06", 44 + len(ext), 45, 45, 1, 1, 1, 1, 8, 64) + ext
    locator = struct.pack("<4sIQI", b"PK\x06\x07", 1, 128, 2)
    eocd = struct.pack("<4sHHHHIIH", b"PK\x05\x06", 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 2) + b"ok"
    d = zip64_multidisk_gate(zip64, locator, eocd, 128, 128 + len(zip64), 128 + len(zip64) + 20, [256, 256])

    sample = hashlib.sha256(b"fictional-sample-label").hexdigest()
    issuer_scopes = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-c": {"transfer"}}
    events = []
    prev = "0" * 64
    for seq, (issuer, scope) in enumerate((("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer"))):
        event = make_custody_event(seq, sample, "fictional-path-1", issuer, scope, "2026-01-01", "2027-01-01", prev)
        events.append(event)
        prev = event["event_sha256"]
    e = verify_custody_chain(events, issuer_scopes, "2026-09-28")

    cov5_zero = [[0.0 for _ in range(5)] for _ in range(5)]
    sigmas = [0.2] * 5
    cov5_outer = [[sigmas[i] * sigmas[j] for j in range(5)] for i in range(5)]
    cov5_diag = [[0.04 if i == j else 0.0 for j in range(5)] for i in range(5)]
    f = component_covariance_sweep(
        [[1, 2], [0.5, 1], [1, 2], [0.5, 1], [4, 6]],
        {"zero": cov5_zero, "independent": cov5_diag, "fully_correlated_stress": cov5_outer,
         "invalid_non_psd": [[1, 2], [2, 1]]},
        [1, 2, 4, 0],
    )

    dims = [0] * 7
    usd2 = "*".join(sorted(("USD", "USD")))
    entry = lambda value: {"value": value, "unit": usd2, "dimension": dims}
    g = typed_covariance_block(
        [{"id": "cost-a", "unit": "USD", "dimension": dims}, {"id": "cost-b", "unit": "USD", "dimension": dims}],
        [[entry(1.0), entry(0.2)], [entry(0.2), entry(0.5)]],
    )

    h = correlation_ranking_grid(
        ["A", "B", "C"],
        [
            {"name": "rho-zero", "correlation": [[1, 0, 0], [0, 1, 0], [0, 0, 1]], "scenario_orders": [["A", "B", "C"], ["A", "C", "B"], ["B", "A", "C"]], "assumption": "independent rank shocks"},
            {"name": "rho-positive", "correlation": [[1, 0.7, 0], [0.7, 1, 0], [0, 0, 1]], "scenario_orders": [["A", "B", "C"], ["B", "A", "C"], ["B", "C", "A"]], "assumption": "declared positive correlation sensitivity"},
        ],
    )

    source_sha = hashlib.sha256(source_bytes).hexdigest()
    length = [1, 0, 0, 0, 0, 0, 0]
    time_dim = [0, 0, 1, 0, 0, 0, 0]
    left = {"unit": "m", "dimension": length, "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": source_sha, "lower": [1, 2], "upper": [3, 2]}
    right = {"unit": "m", "dimension": length, "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": source_sha, "lower": [1, 4], "upper": [1, 2]}
    added = rational_interval_composition(left, right, "add", source_bytes)
    seconds = {"unit": "s", "dimension": time_dim, "domain_sort": "RealModel", "evidence_sort": "Model", "source_sha256": source_sha, "lower": [2, 1], "upper": [3, 1]}
    products = {"m|s": {"unit": "m*s", "dimension": [a + b for a, b in zip(length, time_dim)]}}
    fnd = rational_interval_composition(added, seconds, "multiply", source_bytes, products)

    scm = scm_fictional_rejection_suite("2026-09-28")

    splits = {"train": ["train-row-1", "train-row-2"], "validation": ["validation-row-1"], "test": ["test-row-1"]}
    metrics = {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}}
    config = {"optimizer": "fictional-fixture", "seed": 0, "epochs": 1}
    parent = ai_lineage_manifest(b"synthetic-ai-source-v4", splits, metrics, config)
    ai = ai_lineage_manifest_v5(parent, b"synthetic-ai-source-v5", splits, metrics, config)

    parent_qos = run_cycle014_fixture()["QOS/QSVT"]
    gates = [
        {"op": "x", "target": 0}, {"op": "cx", "control": 0, "target": 1},
        {"op": "cx", "control": 1, "target": 3}, {"op": "x", "target": 5},
        {"op": "cx", "control": 3, "target": 4},
    ]
    qos = qos_er6_reconstruction_v5(parent_qos, gates)
    return {"A": a, "B": b, "C": c, "D": d, "E": e, "F": f, "G": g, "H": h,
            "FND/EQN": fnd, "SCM": scm, "AI-COST": ai, "QOS/QSVT": qos}
