"""Cycle 013 bounded acceptance contracts; synthetic or fiction-only evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import tempfile
from datetime import date
from fractions import Fraction
from pathlib import Path

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")
SI_DIMENSION_BASIS = ("L", "M", "T", "I", "Theta", "N", "J")
MAX_U64 = (1 << 64) - 1


def _validate_json_value(value):
    if value is None or isinstance(value, (str, bool)):
        return
    if isinstance(value, int) and not isinstance(value, bool):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError("non-finite JSON number")
        return
    if isinstance(value, list):
        for item in value:
            _validate_json_value(item)
        return
    if isinstance(value, dict):
        if any(not isinstance(key, str) for key in value):
            raise ValueError("JSON object keys must be strings")
        for item in value.values():
            _validate_json_value(item)
        return
    raise ValueError("value is not canonical JSON data")


def canonical_bytes(value):
    _validate_json_value(value)
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")


def canonical_hash(value):
    return hashlib.sha256(canonical_bytes(value)).hexdigest()


def exact_keys(obj, required, optional=()):
    if not isinstance(obj, dict) or set(obj) - set(required) - set(optional) or set(required) - set(obj):
        raise ValueError("schema keys")
    return obj


def _finite_number(value):
    if not isinstance(value, (int, float)) or isinstance(value, bool):
        return False
    try:
        return math.isfinite(float(value))
    except (OverflowError, TypeError, ValueError):
        return False


def _is_psd(matrix, tolerance=1e-10):
    n = len(matrix)
    if n == 0 or any(not isinstance(row, (list, tuple)) or len(row) != n for row in matrix):
        return False
    if any(not _finite_number(value) for row in matrix for value in row):
        return False
    scale = max(abs(float(value)) for row in matrix for value in row)
    if scale == 0:
        return True
    work = [[float(value) / scale for value in row] for row in matrix]
    if any(abs(work[i][j] - work[j][i]) > tolerance for i in range(n) for j in range(n)):
        return False
    # Symmetric Jacobi diagonalization avoids determinant overflow and works for
    # singular PSD matrices. The normalized matrix entries are bounded by one.
    limit = max(1, 100 * n * n)
    for _ in range(limit):
        p, q, largest = 0, 0, 0.0
        for i in range(n):
            for j in range(i + 1, n):
                if abs(work[i][j]) > largest:
                    p, q, largest = i, j, abs(work[i][j])
        if largest <= tolerance:
            break
        apq = work[p][q]
        tau = (work[q][q] - work[p][p]) / (2.0 * apq)
        t = math.copysign(1.0, tau) / (abs(tau) + math.sqrt(1.0 + tau * tau)) if tau else 1.0
        c = 1.0 / math.sqrt(1.0 + t * t)
        s = t * c
        app, aqq = work[p][p], work[q][q]
        work[p][p] = app - t * apq
        work[q][q] = aqq + t * apq
        work[p][q] = work[q][p] = 0.0
        for k in range(n):
            if k in (p, q):
                continue
            akp, akq = work[k][p], work[k][q]
            work[k][p] = work[p][k] = c * akp - s * akq
            work[k][q] = work[q][k] = s * akp + c * akq
    else:
        return False
    if any(not math.isfinite(work[i][i]) or work[i][i] < -tolerance for i in range(n)):
        return False
    return True


# Lane A — bounded exact enumeration and restart identity.
def weighted_maxcut_13(n, edges, cap=1024):
    if (not isinstance(n, int) or isinstance(n, bool) or n < 1 or n > 10
            or not isinstance(cap, int) or isinstance(cap, bool) or not 1 <= cap <= 1024
            or not edges):
        raise ValueError("state cap or empty graph")
    if (1 << n) > cap:
        raise ValueError("state cap or empty graph")
    normalized = []
    seen = set()
    for edge in edges:
        if not isinstance(edge, (tuple, list)) or len(edge) != 3:
            raise ValueError("edge shape")
        u, v, weight = edge
        if not all(isinstance(x, int) and not isinstance(x, bool) for x in (u, v, weight)):
            raise ValueError("edge integer types")
        if not (0 <= u < n and 0 <= v < n and u != v and weight > 0):
            raise ValueError("edge range/weight")
        key = tuple(sorted((u, v)))
        if key in seen:
            raise ValueError("duplicate edge")
        seen.add(key)
        normalized.append([key[0], key[1], weight])
    normalized.sort()
    scores = [
        (sum(w for u, v, w in normalized if ((state >> u) ^ (state >> v)) & 1), state)
        for state in range(1 << n)
    ]
    best = max(score for score, _ in scores)
    optimum_states = [state for score, state in scores if score == best]
    return {
        "states": len(scores),
        "best_cut_weight": best,
        "optimal_state_set_sha256": canonical_hash(optimum_states),
        "graph_sha256": canonical_hash({"n": n, "edges": normalized}),
        "restart_sha256": canonical_hash({
            "enumeration": "ascending-integer-state",
            "initial_state": 0,
            "seed": 0,
        }),
    }


# Lane B — canonical semantic request binding.
def bind_v4_request(body):
    exact_keys(body, ("schema", "payload", "token", "options", "source_commit"))
    if body["schema"] != "v4" or not isinstance(body["payload"], dict) or not isinstance(body["options"], dict):
        raise ValueError("v4 request")
    if not isinstance(body["token"], str) or not body["token"]:
        raise ValueError("semantic token")
    if not isinstance(body["source_commit"], str) or not body["source_commit"]:
        raise ValueError("source commit")
    return {**body, "binding": canonical_hash(body)}


def verify_v4_request(request):
    exact_keys(request, ("schema", "payload", "token", "options", "source_commit", "binding"))
    body = {key: request[key] for key in ("schema", "payload", "token", "options", "source_commit")}
    expected = bind_v4_request(body)
    if request["binding"] != expected["binding"]:
        raise ValueError("request semantic binding")
    return True


# Lane C — same-directory atomic replacement state machine. Cache and power-loss
# behavior are deliberately reported as uncontrolled/unmeasured.
def publish_atomic_file(directory, final_name, new_bytes, failure_point=None):
    if not isinstance(new_bytes, bytes) or not isinstance(final_name, str) or not final_name or Path(final_name).name != final_name:
        raise ValueError("target or payload")
    if failure_point not in (None, "after_stage_before_replace", "after_replace_before_report"):
        raise ValueError("failure point")
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    target = root / final_name
    active_prefix = f".{final_name}.tmp.active."
    stale_prefix = f".{final_name}.tmp.stale."
    # Only the reserved stale namespace is janitored. Active writers use random,
    # exclusive names and are never unlinked by a competing publisher.
    stale = [p for p in root.iterdir() if p.name.startswith(stale_prefix) and p.is_file()]
    for temp in stale:
        temp.unlink()
    fd, staged_name = tempfile.mkstemp(prefix=active_prefix, dir=root)
    staged = Path(staged_name)
    with os.fdopen(fd, "wb") as staged_file:
        staged_file.write(new_bytes)
    if failure_point == "after_stage_before_replace":
        staged.unlink(missing_ok=True)
        visible = target.read_bytes() if target.exists() else None
        return {
            "visible_sha256": hashlib.sha256(visible).hexdigest() if visible is not None else None,
            "visible_bytes": visible,
            "stale_temps_removed": len(stale),
            "temp_removed": not staged.exists(),
            "status": "INJECTED_FAILURE_OLD_INTACT",
            "cache_state": "UNCONTROLLED",
            "durability": "PROCESS_LOCAL_ONLY",
        }
    os.replace(staged, target)
    status = "PUBLISHED_NEW_PAYLOAD"
    if failure_point == "after_replace_before_report":
        status = "INJECTED_FAILURE_NEW_INTACT"
    visible = target.read_bytes()
    return {
        "visible_sha256": hashlib.sha256(visible).hexdigest(),
        "visible_bytes": visible,
        "stale_temps_removed": len(stale),
        "temp_removed": not staged.exists(),
        "status": status,
        "cache_state": "UNCONTROLLED",
        "durability": "PROCESS_LOCAL_ONLY",
    }


# Lane D — strict synthetic ZIP64 layout checks. This validates offsets/counts;
# it does not parse or authenticate archive payload bytes.
def zip64_layout_gate(entries, declared_count, central_start, central_end,
                      zip64_start, zip64_end, locator_start, eocd_start, file_size):
    if not isinstance(declared_count, int) or isinstance(declared_count, bool) or not (0 <= declared_count <= MAX_U64):
        raise ValueError("ZIP64 count range")
    if declared_count != len(entries):
        raise ValueError("ZIP64 entry count")
    offsets = (central_start, central_end, zip64_start, zip64_end, locator_start, eocd_start, file_size)
    if any(not isinstance(x, int) or isinstance(x, bool) or x < 0 for x in offsets):
        raise ValueError("ZIP64 offset type/range")
    if not (
        central_start <= central_end <= zip64_start < zip64_end
        and zip64_end == locator_start
        and locator_start + 20 == eocd_start
        and eocd_start + 22 <= file_size
    ):
        raise ValueError("ZIP64 record overlap/order")
    if zip64_end - zip64_start < 56:
        raise ValueError("ZIP64 end record shorter than fixed fields")
    last = central_start
    for entry in entries:
        if not isinstance(entry, (tuple, list)) or len(entry) != 2:
            raise ValueError("central-directory entry shape")
        start, end = entry
        if (not isinstance(start, int) or isinstance(start, bool)
                or not isinstance(end, int) or isinstance(end, bool)
                or start != last or end <= start or end > central_end):
            raise ValueError("central-directory entry overlap/bounds")
        last = end
    if last != central_end:
        raise ValueError("central-directory extent")
    return {
        "entries": declared_count,
        "central_directory_bytes": central_end - central_start,
        "status": "VALID_SYNTHETIC_ZIP64_LAYOUT",
        "payload_read": False,
    }


# Lane E — hash-linked custody events bind issuer and scope.
def _iso_day(value):
    if not isinstance(value, str):
        raise ValueError("date syntax")
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError("date syntax") from exc
    if parsed.isoformat() != value:
        raise ValueError("date syntax")
    return parsed


def custody_chain_13(events, issuer_scopes, now):
    if not events:
        raise ValueError("empty custody chain")
    today = _iso_day(now)
    prior = "0" * 64
    chain = []
    prior_event = None
    required = ("sample", "from", "to", "method", "unit", "expiry", "issuer", "scope", "previous")
    for event in events:
        exact_keys(event, required)
        if event["previous"] != prior or not all(isinstance(event[k], str) and event[k] for k in required[:-1]):
            raise ValueError("custody continuity/field")
        if prior_event is not None and (event["sample"] != prior_event["sample"] or event["from"] != prior_event["to"]):
            raise ValueError("custody sample/path continuity")
        if _iso_day(event["expiry"]) <= today:
            raise ValueError("custody event expired")
        if event["issuer"] not in issuer_scopes or event["scope"] not in issuer_scopes[event["issuer"]]:
            raise ValueError("issuer scope authorization")
        prior = canonical_hash(event)
        chain.append(prior)
        prior_event = event
    return chain


# Lane F — complete sparse covariance input for a five-component model interval.
def _sparse_covariance(labels, sparse):
    if (not isinstance(sparse, dict)
            or set(sparse) != {"labels", "entries", "structural_zero_pairs"}
            or not isinstance(sparse["labels"], list)
            or not isinstance(sparse["entries"], list)
            or not isinstance(sparse["structural_zero_pairs"], list)):
        return None
    if sparse["labels"] != labels:
        return None
    index = {name: i for i, name in enumerate(labels)}
    expected = {(i, j) for i in range(len(labels)) for j in range(i, len(labels))}
    matrix = [[0.0 for _ in labels] for _ in labels]
    covered = set()
    for entry in sparse["entries"]:
        if not isinstance(entry, dict) or set(entry) != {"left", "right", "value"}:
            return None
        left, right, value = entry["left"], entry["right"], entry["value"]
        if not isinstance(left, str) or not isinstance(right, str) or left not in index or right not in index or not _finite_number(value):
            return None
        i, j = sorted((index[left], index[right]))
        if (i, j) in covered:
            return None
        covered.add((i, j))
        try:
            matrix[i][j] = matrix[j][i] = float(value)
        except (OverflowError, ValueError):
            return None
    for pair in sparse["structural_zero_pairs"]:
        if (not isinstance(pair, (tuple, list)) or len(pair) != 2
                or not all(isinstance(name, str) and name in index for name in pair)):
            return None
        i, j = sorted((index[pair[0]], index[pair[1]]))
        if (i, j) in covered:
            return None
        covered.add((i, j))
    if covered != expected or not _is_psd(matrix):
        return None
    return matrix


def cost_interval_13(components, accepted_outputs, sparse_covariance):
    if not isinstance(components, list) or len(components) != 5:
        return None
    if not _finite_number(accepted_outputs) or accepted_outputs <= 0:
        return None
    names = []
    for component in components:
        if not isinstance(component, dict) or set(component) != {"name", "low", "high", "unit"}:
            return None
        if not isinstance(component["name"], str) or not component["name"] or component["unit"] != "USD":
            return None
        if not all(_finite_number(component[k]) for k in ("low", "high")) or component["low"] < 0 or component["high"] < component["low"]:
            return None
        names.append(component["name"])
    if len(set(names)) != 5:
        return None
    covariance = _sparse_covariance(names, sparse_covariance)
    if covariance is None:
        return None
    total_low = sum(c["low"] for c in components)
    total_high = sum(c["high"] for c in components)
    try:
        aggregate_variance = math.fsum(math.fsum(row) for row in covariance)
    except (OverflowError, ValueError):
        return None
    if not _finite_number(total_low) or not _finite_number(total_high) or not _finite_number(aggregate_variance):
        return None
    per_output = [total_low / accepted_outputs, total_high / accepted_outputs]
    if any(not _finite_number(value) for value in per_output) or aggregate_variance < -1e-10:
        return None
    return {
        "component_count": 5,
        "total_usd_interval": [total_low, total_high],
        "per_accepted_output_usd": per_output,
        "aggregate_variance_usd2_model": max(0.0, aggregate_variance),
        "covariance_complete": True,
        "evidence_class": "MODEL_ONLY",
    }


# Lane G — four-measurand certificate checks with ordered SI dimensions.
def covariance_certificate_13(names, matrix_order, units, dimensions, matrix,
                              unit_registry, scope, method, expires, now):
    n = len(names)
    if (n != 4 or any(not isinstance(name, str) or not name for name in names)
            or len(set(names)) != n or matrix_order != names):
        raise ValueError("measurand count or matrix order")
    if len(units) != n or len(dimensions) != n or len(matrix) != n or any(len(row) != n for row in matrix):
        raise ValueError("measurand dimensions")
    if not isinstance(scope, str) or not scope or not isinstance(method, str) or not method:
        raise ValueError("certificate metadata")
    if _iso_day(expires) <= _iso_day(now):
        raise ValueError("certificate expired")
    for unit, dimension in zip(units, dimensions):
        if unit not in unit_registry or dimension != unit_registry[unit]:
            raise ValueError("unit/dimension registry mismatch")
        if len(dimension) != len(SI_DIMENSION_BASIS) or any(not isinstance(x, int) or isinstance(x, bool) for x in dimension):
            raise ValueError("dimension vector")
    if any(not _finite_number(x) for row in matrix for x in row):
        raise ValueError("covariance value")
    if any(abs(matrix[i][j] - matrix[j][i]) > 1e-12 for i in range(n) for j in range(n)) or not _is_psd(matrix):
        raise ValueError("covariance symmetry/PSD")
    body = {
        "names": list(names), "matrix_order": list(matrix_order), "units": list(units),
        "dimensions": [list(d) for d in dimensions], "matrix": matrix,
        "scope": scope, "method": method, "expires": expires,
        "basis_order": list(SI_DIMENSION_BASIS),
    }
    return {**body, "certificate_sha256": canonical_hash(body), "status": "SYNTHETIC_VALID"}


# Lane H — correlated, held-out ranking sensitivity. Scores and shocks are assumed
# scenario inputs, not measured economics or a capital request.
def _cholesky_psd(matrix, tolerance=1e-12):
    n = len(matrix)
    lower = [[0.0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1):
            residual = matrix[i][j] - sum(lower[i][k] * lower[j][k] for k in range(j))
            if i == j:
                if residual < -tolerance:
                    raise ValueError("correlation not PSD")
                lower[i][j] = math.sqrt(max(0.0, residual))
            elif lower[j][j] > tolerance:
                lower[i][j] = residual / lower[j][j]
            elif abs(residual) > tolerance:
                raise ValueError("correlation singular inconsistency")
    return lower


def correlated_priority_sensitivity(gates, base_scores, correlation, heldout_innovations):
    n = len(gates)
    if n < 2 or len(set(gates)) != n or set(base_scores) != set(gates):
        raise ValueError("gate set")
    if any(not _finite_number(base_scores[g]) for g in gates):
        raise ValueError("base score")
    if len(correlation) != n or any(len(row) != n for row in correlation):
        raise ValueError("correlation dimensions")
    if any(not _finite_number(x) for row in correlation for x in row):
        raise ValueError("correlation values")
    if any(abs(correlation[i][j] - correlation[j][i]) > 1e-12 for i in range(n) for j in range(n)):
        raise ValueError("correlation symmetry")
    if any(abs(correlation[i][i] - 1.0) > 1e-12 for i in range(n)):
        raise ValueError("correlation diagonal")
    lower = _cholesky_psd(correlation)
    if not heldout_innovations:
        raise ValueError("held-out scenarios")
    baseline = tuple(sorted(gates, key=lambda g: (-base_scores[g], g)))
    orders = []
    for innovation in heldout_innovations:
        if len(innovation) != n or any(not _finite_number(x) for x in innovation):
            raise ValueError("held-out innovation")
        correlated = [
            sum(lower[i][j] * innovation[j] for j in range(i + 1))
            for i in range(n)
        ]
        if any(not _finite_number(value) for value in correlated):
            raise ValueError("correlated innovation overflow")
        adjusted = {gates[i]: base_scores[gates[i]] + correlated[i] for i in range(n)}
        if any(not _finite_number(value) for value in adjusted.values()):
            raise ValueError("adjusted score overflow")
        orders.append(tuple(sorted(gates, key=lambda g: (-adjusted[g], g))))
    return {
        "baseline_order": list(baseline),
        "heldout_orders": [list(order) for order in orders],
        "conditional_order_stability": sum(order == baseline for order in orders) / len(orders),
        "correlation_sha256": canonical_hash(correlation),
        "evidence_class": "ILLUSTRATIVE_CORRELATED_SCENARIO",
        "capital": None,
    }


# Lane FND/EQN — exact UMRL-031 typed interval with a verified source-byte digest.
def registered_interval_13(entry, source_bytes):
    exact_keys(entry, (
        "id", "lower", "upper", "kind", "unit", "dimension", "domain_sort",
        "source_locator", "source_sha256", "evidence", "provenance",
    ))
    if entry["id"] != "FND-EQN-013-SYN-01":
        raise ValueError("interval id")
    if not isinstance(source_bytes, bytes) or b"UMRL-031" not in source_bytes or b"q=(v,k,u" not in source_bytes:
        raise ValueError("UMRL-031 source bytes")
    if not all(isinstance(x, (tuple, list)) and len(x) == 2 and all(isinstance(y, int) and not isinstance(y, bool) for y in x) and x[1] > 0 for x in (entry["lower"], entry["upper"])):
        raise ValueError("rational interval")
    if Fraction(*entry["lower"]) > Fraction(*entry["upper"]):
        raise ValueError("interval order")
    if (entry["kind"] != "bounded_interval" or entry["unit"] != "1"
            or entry["domain_sort"] != "RealModel" or entry["provenance"] != "UMRL-031"):
        raise ValueError("quantity type tuple")
    if (not isinstance(entry["dimension"], list) or len(entry["dimension"]) != 10
            or any(not isinstance(x, int) or isinstance(x, bool) for x in entry["dimension"])
            or any(entry["dimension"])):
        raise ValueError("dimension vector")
    if entry["source_locator"] != "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md:397-412#UMRL-031":
        raise ValueError("source locator")
    if (not isinstance(entry["source_sha256"], str) or len(entry["source_sha256"]) != 64
            or any(c not in "0123456789abcdef" for c in entry["source_sha256"])
            or entry["source_sha256"] != hashlib.sha256(source_bytes).hexdigest()):
        raise ValueError("source digest")
    if entry["evidence"] != "DECLARATION_ONLY":
        raise ValueError("evidence class")
    return {
        "id": entry["id"], "interval": [list(entry["lower"]), list(entry["upper"])],
        "kind": entry["kind"], "unit": entry["unit"], "dimension": list(entry["dimension"]),
        "domain_sort": entry["domain_sort"], "source_locator": entry["source_locator"],
        "source_sha256": entry["source_sha256"], "evidence": "DECLARATION_ONLY",
    }


# Lane SCM — consent protocol remains in a fictional state space, separate from
# empirical sensing or source claims.
def consent_state_13(active=None, seen=None, revoked=None):
    return {
        "active": dict(active or {}),
        "seen": set(seen or ()),
        "revoked": set(revoked or ()),
        "fiction_only": True,
        "empirical_coupling": None,
    }


def consent_event_13(state, event, now):
    exact_keys(event, ("action", "nonce", "consent_id", "issued_at", "expires_at"))
    if (not isinstance(now, int) or isinstance(now, bool)
            or not isinstance(event["issued_at"], int) or isinstance(event["issued_at"], bool)
            or not isinstance(event["expires_at"], int) or isinstance(event["expires_at"], bool)):
        raise ValueError("consent time")
    if (not isinstance(event["nonce"], str) or not event["nonce"]
            or not isinstance(event["consent_id"], str) or not event["consent_id"]
            or event["nonce"] in state["seen"] or event["issued_at"] > now):
        raise ValueError("nonce/time")
    out = consent_state_13(state["active"], state["seen"], state["revoked"])
    expired = {key for key, value in out["active"].items() if value <= now}
    for key in expired:
        del out["active"][key]
        out["revoked"].add(key)
    action, consent_id = event["action"], event["consent_id"]
    if action == "grant":
        if consent_id in out["active"] or consent_id in out["revoked"] or event["expires_at"] <= now:
            raise ValueError("grant already used or expired")
        out["active"][consent_id] = event["expires_at"]
    elif action in ("revoke", "transition"):
        if consent_id not in out["active"] or out["active"][consent_id] <= now:
            raise ValueError("consent inactive or expired")
        if event["expires_at"] != out["active"][consent_id]:
            raise ValueError("consent expiry mismatch")
        if action == "revoke":
            del out["active"][consent_id]
            out["revoked"].add(consent_id)
    else:
        raise ValueError("consent action")
    out["seen"].add(event["nonce"])
    return out


# Lane AI-COST — third source version and explicit disjoint split assignment.
def lineage_v3(previous, source_bytes, split_rows, metrics):
    exact_keys(previous, ("version", "source_sha256", "split_hashes"))
    if (not isinstance(previous["version"], int) or isinstance(previous["version"], bool)
            or previous["version"] != 2 or not isinstance(source_bytes, bytes) or not source_bytes):
        raise ValueError("lineage predecessor/source")
    def valid_digest(value):
        return (isinstance(value, str) and len(value) == 64
                and all(char in "0123456789abcdef" for char in value))
    if not valid_digest(previous["source_sha256"]):
        raise ValueError("lineage predecessor source digest")
    if (not isinstance(previous["split_hashes"], dict)
            or set(previous["split_hashes"]) != {"train", "validation", "test"}
            or any(not valid_digest(value) for value in previous["split_hashes"].values())):
        raise ValueError("lineage predecessor split digests")
    if (not isinstance(split_rows, dict) or set(split_rows) != {"train", "validation", "test"}
            or not isinstance(metrics, dict) or set(metrics) != {"train", "validation", "test"}):
        raise ValueError("lineage split sets/metrics")
    if any(not isinstance(rows, list) or any(not isinstance(row, str) or not row for row in rows) for rows in split_rows.values()):
        raise ValueError("split row identifiers")
    if any(not isinstance(metrics[k], dict) or set(metrics[k]) != {"loss"}
           or not _finite_number(metrics[k]["loss"]) or metrics[k]["loss"] < 0
           for k in ("train", "validation", "test")):
        raise ValueError("held-out loss metric schema/value")
    normalized_splits = {k: sorted(split_rows[k]) for k in ("train", "validation", "test")}
    if any(not rows for rows in normalized_splits.values()):
        raise ValueError("empty split")
    flattened = [row for rows in normalized_splits.values() for row in rows]
    if len(flattened) != len(set(flattened)):
        raise ValueError("split overlap")
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    if source_sha == previous["source_sha256"]:
        raise ValueError("source version unchanged")
    return {
        "version": 3,
        "parent_source_sha256": previous["source_sha256"],
        "source_sha256": source_sha,
        "split_hashes": {name: canonical_hash(rows) for name, rows in sorted(normalized_splits.items())},
        "metrics": {name: {"loss": float(metrics[name]["loss"])} for name in ("train", "validation", "test")},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


# Lane QOS/QSVT — third version certificate binds source, map, resources and parent.
def certify_er6_v3(previous, new_certificate, semantic_map):
    keys = ("version", "qubits", "bits", "depth", "gates", "source_sha256", "map_sha256", "parent_certificate_sha256")
    exact_keys(previous, ("version", "qubits", "bits", "depth", "gates", "source_sha256", "map_sha256"))
    exact_keys(new_certificate, keys)
    if (not isinstance(previous["version"], int) or isinstance(previous["version"], bool)
            or not isinstance(new_certificate["version"], int) or isinstance(new_certificate["version"], bool)
            or new_certificate["version"] != previous["version"] + 1 or new_certificate["version"] != 3):
        raise ValueError("ER6 version")
    for record in (previous, new_certificate):
        for key in ("qubits", "bits"):
            if not isinstance(record[key], int) or isinstance(record[key], bool) or record[key] <= 0:
                raise ValueError("ER6 dimensions")
        for key in ("depth", "gates"):
            if not isinstance(record[key], int) or isinstance(record[key], bool) or record[key] < 0:
                raise ValueError("ER6 resources")
    if new_certificate["qubits"] != previous["qubits"] or new_certificate["bits"] != previous["bits"]:
        raise ValueError("ER6 semantic dimensions")
    if any(new_certificate[k] > previous[k] for k in ("depth", "gates")):
        raise ValueError("ER6 resource increase")
    if new_certificate["source_sha256"] == previous["source_sha256"] or new_certificate["map_sha256"] != canonical_hash(semantic_map):
        raise ValueError("ER6 source/map binding")
    for key in ("source_sha256", "map_sha256", "parent_certificate_sha256"):
        digest = new_certificate[key]
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("ER6 digest")
    for key in ("source_sha256", "map_sha256"):
        digest = previous[key]
        if not isinstance(digest, str) or len(digest) != 64 or any(c not in "0123456789abcdef" for c in digest):
            raise ValueError("ER6 predecessor digest")
    if new_certificate["parent_certificate_sha256"] != canonical_hash(previous):
        raise ValueError("ER6 parent binding")
    return {
        "version": 3,
        "certificate_sha256": canonical_hash(new_certificate),
        "parent_certificate_sha256": new_certificate["parent_certificate_sha256"],
        "resources": {key: new_certificate[key] for key in ("qubits", "bits", "depth", "gates")},
        "resource_delta": {
            "depth": new_certificate["depth"] - previous["depth"],
            "gates": new_certificate["gates"] - previous["gates"],
        },
        "source_sha256": new_certificate["source_sha256"],
        "map_sha256": new_certificate["map_sha256"],
        "hardware": None,
        "evidence_class": "ER6_SYNTHETIC_CERTIFICATE",
    }


def run_cycle013_fixture(registry_sha256, registry_source_bytes):
    # A bounded positive-weight five-node graph; a separate ten-node boundary check
    # reaches exactly 2^10 states without extrapolating beyond exhaustive enumeration.
    graph = [(0, 1, 4), (0, 2, 2), (1, 2, 3), (1, 3, 5), (2, 4, 2), (3, 4, 4)]
    a = weighted_maxcut_13(5, graph)
    boundary = weighted_maxcut_13(10, [(0, 1, 1)])
    v4 = bind_v4_request({
        "schema": "v4", "payload": {"operation": "fixture", "version": 3},
        "token": "synthetic-token-013", "options": {"priority": "normal"},
        "source_commit": "707750fb4bec7d701d2c6c35f155c3e381c72b00",
    })
    events = [
        {"sample": "synthetic-1", "from": "vault", "to": "lab", "method": "fixture-method",
         "unit": "fixture-unit", "expiry": "2030-01-01", "issuer": "issuer-a",
         "scope": "scope-synthetic", "previous": "0" * 64},
    ]
    custody = custody_chain_13(events, {"issuer-a": ["scope-synthetic"]}, "2026-09-28")
    components = [
        {"name": name, "low": low, "high": high, "unit": "USD"}
        for name, low, high in (
            ("algorithm", 1, 2), ("state-prep", 2, 3), ("provider", 3, 4),
            ("readout", 1, 2), ("retry", 0, 1),
        )
    ]
    labels = [item["name"] for item in components]
    pairs = [(labels[i], labels[j]) for i in range(len(labels)) for j in range(i, len(labels))]
    sparse = {
        "labels": labels,
        "entries": [
            {"left": name, "right": name, "value": 1.0}
            for name in labels
        ] + [{"left": "state-prep", "right": "provider", "value": 0.1}],
        "structural_zero_pairs": [
            list(pair) for pair in pairs
            if pair[0] != pair[1] and pair not in {("state-prep", "provider")}
        ],
    }
    unit_registry = {
        "m": [1, 0, 0, 0, 0, 0, 0], "s": [0, 0, 1, 0, 0, 0, 0],
        "m/s": [1, 0, -1, 0, 0, 0, 0], "J": [2, 1, -2, 0, 0, 0, 0],
    }
    covariance = [
        [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0], [0.0, 0.0, 0.0, 1.0],
    ]
    g = covariance_certificate_13(
        ["distance", "duration", "velocity", "energy"],
        ["distance", "duration", "velocity", "energy"],
        ["m", "s", "m/s", "J"],
        [unit_registry["m"], unit_registry["s"], unit_registry["m/s"], unit_registry["J"]],
        covariance, unit_registry, "synthetic-scope", "synthetic-method", "2030-01-01", "2026-09-28",
    )
    h = correlated_priority_sensitivity(
        ["provider", "state-prep", "readout"],
        {"provider": 3.0, "state-prep": 2.5, "readout": 1.8},
        [[1.0, 0.6, 0.0], [0.6, 1.0, 0.1], [0.0, 0.1, 1.0]],
        [[0.2, -0.2, 0.1], [-1.0, 1.2, 0.1]],
    )
    fnd = registered_interval_13({
        "id": "FND-EQN-013-SYN-01", "lower": [1, 1], "upper": [2, 1],
        "kind": "bounded_interval", "unit": "1", "dimension": [0] * 10,
        "domain_sort": "RealModel",
        "source_locator": "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md:397-412#UMRL-031",
        "source_sha256": registry_sha256, "evidence": "DECLARATION_ONLY", "provenance": "UMRL-031",
    }, registry_source_bytes)
    scm = consent_state_13()
    scm = consent_event_13(scm, {"action": "grant", "nonce": "g1", "consent_id": "c1", "issued_at": 10, "expires_at": 30}, 10)
    scm = consent_event_13(scm, {"action": "revoke", "nonce": "r1", "consent_id": "c1", "issued_at": 11, "expires_at": 30}, 11)
    scm = consent_event_13(scm, {"action": "grant", "nonce": "g2", "consent_id": "c2", "issued_at": 12, "expires_at": 40}, 12)
    previous_lineage = {
        "version": 2, "source_sha256": hashlib.sha256(b"synthetic-source-v2").hexdigest(),
        "split_hashes": {"train": "a" * 64, "validation": "b" * 64, "test": "c" * 64},
    }
    lineage = lineage_v3(
        previous_lineage, b"synthetic-source-v3",
        {"train": ["r1"], "validation": ["r2"], "test": ["r3"]},
        {"train": {"loss": 1.0}, "validation": {"loss": 1.1}, "test": {"loss": 1.2}},
    )
    old_cert = {
        "version": 2, "qubits": 6, "bits": 6, "depth": 18, "gates": 38,
        "source_sha256": hashlib.sha256(b"er6-source-v2-synthetic").hexdigest(),
        "map_sha256": canonical_hash({"map": "v2"}),
    }
    semantic_map = {"map": "v3", "bounded_subset": "ER6"}
    new_cert = {
        "version": 3, "qubits": 6, "bits": 6, "depth": 16, "gates": 34,
        "source_sha256": hashlib.sha256(b"er6-source-v3-synthetic").hexdigest(),
        "map_sha256": canonical_hash(semantic_map),
        "parent_certificate_sha256": canonical_hash(old_cert),
    }
    qos = certify_er6_v3(old_cert, new_cert, semantic_map)
    import tempfile
    with tempfile.TemporaryDirectory() as tempdir:
        root = Path(tempdir)
        (root / ".payload.bin.tmp.stale").write_bytes(b"stale")
        c = publish_atomic_file(root, "payload.bin", b"new-complete-payload")
    d = zip64_layout_gate(
        [(100, 120), (120, 140), (140, 160)], 3, 100, 160,
        160, 216, 216, 236, 258,
    )
    return {
        "A": {"graph": a, "cap_boundary": {"states": boundary["states"], "accepted": True}},
        "B": {"schema": v4["schema"], "binding_sha256": v4["binding"], "canonical": True},
        "C": {
            "visible_sha256": c["visible_sha256"], "stale_temps_removed": c["stale_temps_removed"],
            "temp_removed": c["temp_removed"], "cache_state": c["cache_state"],
            "durability": c["durability"], "status": c["status"],
        },
        "D": d,
        "E": {"event_hashes": custody, "issuer_scope_bound": True},
        "F": cost_interval_13(components, 2, sparse),
        "G": {
            "measurands": len(g["names"]), "basis_order": g["basis_order"],
            "certificate_sha256": g["certificate_sha256"], "status": g["status"],
        },
        "H": h,
        "FND/EQN": fnd,
        "SCM": {
            "active_consent_ids": sorted(scm["active"]), "revoked_ids": sorted(scm["revoked"]),
            "fiction_only": scm["fiction_only"], "empirical_coupling": scm["empirical_coupling"],
        },
        "AI-COST": lineage,
        "QOS/QSVT": qos,
    }
