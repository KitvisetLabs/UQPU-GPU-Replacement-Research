"""Cycle 012 fail-closed contracts; synthetic/local checks only."""
from __future__ import annotations

import hashlib
import json
import math
from itertools import product


def canonical_hash(value):
    raw = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()


def exact_keys(obj, required, optional=()):
    if not isinstance(obj, dict) or set(obj) - set(required) - set(optional) or set(required) - set(obj):
        raise ValueError("schema keys")
    return obj


def weighted_maxcut(n, edges, cap=512):
    if n < 1 or (1 << n) > cap or not edges:
        raise ValueError("state cap or empty graph")
    seen = set()
    for u, v, w in edges:
        if not (0 <= u < n and 0 <= v < n and u != v and isinstance(w, int) and w > 0):
            raise ValueError("edge")
        key = tuple(sorted((u, v)))
        if key in seen:
            raise ValueError("duplicate edge")
        seen.add(key)
    values = [(sum(w for u, v, w in edges if ((s >> u) ^ (s >> v)) & 1), s) for s in range(1 << n)]
    best = max(v for v, _ in values)
    return {"states": len(values), "best": best, "argmin_hash": canonical_hash([s for v, s in values if v == best]), "graph_hash": canonical_hash([n, sorted(edges)])}


def migrate_v3_to_v4(request, source_commit):
    exact_keys(request, ("schema", "payload", "token"), ("options",))
    if request["schema"] != "v3" or not isinstance(request["payload"], dict) or not request["token"]:
        raise ValueError("v3 request")
    options = request.get("options", {})
    exact_keys(options, (), ("deadline_ms", "priority"))
    if "deadline_ms" in options and (not isinstance(options["deadline_ms"], int) or options["deadline_ms"] <= 0):
        raise ValueError("deadline")
    if "priority" in options and options["priority"] not in {"normal", "high"}:
        raise ValueError("priority")
    body = {"schema": "v4", "payload": request["payload"], "token": request["token"], "options": options, "source_commit": source_commit}
    return {**body, "binding": canonical_hash(body)}


def zip64_directory_gate(entries, declared_count, central_start, central_end, eocd_offset, file_size):
    if declared_count != len(entries) or not (0 <= central_start <= central_end <= eocd_offset <= file_size):
        raise ValueError("directory boundaries/count")
    last = central_start
    for start, end in entries:
        if start < last or end <= start or end > central_end:
            raise ValueError("entry order/overlap")
        last = end
    if last != central_end:
        raise ValueError("central directory extent")
    return {"entries": declared_count, "central_bytes": central_end-central_start, "status": "VALID_SYNTHETIC_DIRECTORY"}


def atomic_publish_model(old_payload, new_payload, failure_point=None):
    if not isinstance(old_payload, bytes) or not isinstance(new_payload, bytes):
        raise ValueError("payload bytes")
    staged = hashlib.sha256(new_payload).hexdigest()
    if failure_point == "before_replace":
        return {"visible_sha256": hashlib.sha256(old_payload).hexdigest(), "temp_removed": True, "status": "INJECTED_FAILURE_OLD_INTACT"}
    return {"visible_sha256": staged, "temp_removed": True, "status": "PUBLISHED_NEW_PAYLOAD"}


def custody_chain(events):
    if not events:
        raise ValueError("empty chain")
    prior = "0" * 64
    out = []
    for event in events:
        exact_keys(event, ("sample", "from", "to", "method", "unit", "expiry", "previous"))
        if event["previous"] != prior or not all(event[k] for k in ("sample", "from", "to", "method", "unit", "expiry")):
            raise ValueError("custody continuity or missing field")
        prior = canonical_hash(event)
        out.append(prior)
    return out


def cost_per_output(components, outputs, covariance=None):
    if outputs <= 0 or not components:
        return None
    if any(set(c) != {"low", "high", "unit"} or c["unit"] != "USD" or c["low"] < 0 or c["high"] < c["low"] for c in components):
        return None
    total = [sum(c[k] for c in components) for k in ("low", "high")]
    if covariance is not None:
        n=len(components)
        if len(covariance)!=n or any(len(row)!=n for row in covariance) or any(covariance[i][j]!=covariance[j][i] for i in range(n) for j in range(n)):
            return None
        # PSD check by all principal minors for this bounded small matrix.
        for mask in range(1, 1<<n):
            ix=[i for i in range(n) if mask>>i&1]
            if _det([[covariance[i][j] for j in ix] for i in ix]) < -1e-12:
                return None
    return {"total_usd": total, "per_output_usd": [x/outputs for x in total], "uncertainty": "MODEL_ONLY" if covariance is not None else None}


def _det(a):
    if len(a)==1: return a[0][0]
    return sum((-1)**j*a[0][j]*_det([row[:j]+row[j+1:] for row in a[1:]]) for j in range(len(a)))


def covariance_block(names, units, matrix, scope, method, expires):
    n=len(names)
    if n < 1 or len(set(names)) != n or len(units)!=n or len(matrix)!=n or any(len(r)!=n for r in matrix):
        raise ValueError("covariance dimensions")
    if not scope or not method or not expires or any(not u for u in units):
        raise ValueError("covariance metadata")
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[j][i]: raise ValueError("asymmetry")
    for mask in range(1,1<<n):
        ix=[i for i in range(n) if mask>>i&1]
        if _det([[matrix[i][j] for j in ix] for i in ix]) < -1e-12: raise ValueError("non-PSD")
    return {"measurands":n,"scope":scope,"method":method,"expires":expires,"status":"SYNTHETIC_VALID"}


def priority_sensitivity(gates, scenarios, held_out):
    if len(gates)<2 or not scenarios or not held_out or any(set(s)!=set(gates) or any(v<=0 for v in s.values()) for s in scenarios+held_out):
        raise ValueError("priority scenarios")
    def order(s): return tuple(sorted(gates,key=lambda g:(-s[g],g)))
    seen={order(s) for s in scenarios}
    reversals=sum(order(s)!=order(scenarios[0]) for s in scenarios)
    return {"orderings":len(seen),"reversals":reversals,"held_out_orders":[order(s) for s in held_out],"capital":None}


def typed_interval(value, registered_dimension, source_sha):
    if not source_sha or len(source_sha)!=64 or not isinstance(value, list) or len(value)!=2 or value[0]>value[1]:
        raise ValueError("interval/source")
    if not isinstance(registered_dimension,list) or len(registered_dimension)!=10 or any(not isinstance(x,int) for x in registered_dimension):
        raise ValueError("registered dimension")
    return {"interval":value,"dimension":registered_dimension,"source_sha256":source_sha,"evidence":"DECLARATION_ONLY"}


def consent_transition(state, event):
    exact_keys(event,("action","nonce","consent_id"))
    if not event["nonce"] or not event["consent_id"] or event["nonce"] in state["seen"]: raise ValueError("nonce replay")
    out={"active":set(state["active"]),"seen":set(state["seen"])}
    if event["action"]=="grant":
        if event["consent_id"] in out["active"]: raise ValueError("already active")
        out["active"].add(event["consent_id"])
    elif event["action"]=="revoke":
        if event["consent_id"] not in out["active"]: raise ValueError("revoke inactive consent")
        out["active"].remove(event["consent_id"])
    elif event["action"]=="transition":
        if event["consent_id"] not in out["active"]: raise ValueError("consent not active")
    else: raise ValueError("action")
    out["seen"].add(event["nonce"])
    return out


def lineage_manifest(source_bytes, splits, metrics):
    if set(splits)!={"train","validation","test"} or not source_bytes or set(metrics)!={"train","validation","test"}:
        raise ValueError("lineage completeness")
    flattened=[r for rows in splits.values() for r in rows]
    if len(flattened)!=len(set(flattened)) or any(not metrics[k] for k in metrics): raise ValueError("overlap or metrics")
    return {"source_sha256":hashlib.sha256(source_bytes).hexdigest(),"split_hashes":{k:canonical_hash(sorted(v)) for k,v in sorted(splits.items())},"metrics":metrics}


def migrate_er6(old, new):
    exact_keys(old,("version","qubits","bits","depth","gates","source_sha256"))
    exact_keys(new,("version","qubits","bits","depth","gates","source_sha256"))
    if new["version"]<=old["version"] or new["qubits"]!=old["qubits"] or new["bits"]!=old["bits"] or new["source_sha256"]==old["source_sha256"]:
        raise ValueError("ER6 identity/version")
    if any(new[k]>old[k] for k in ("depth","gates")) or any(new[k]<=0 for k in ("depth","gates")):
        raise ValueError("resource bound must decrease")
    return {"version":new["version"],"resource_delta":{"depth":new["depth"]-old["depth"],"gates":new["gates"]-old["gates"]},"hardware":None}


def run_cycle012_fixture():
    return {
        "A": weighted_maxcut(4,[(0,1,2),(1,2,3),(2,3,1),(0,3,4)]),
        "B": migrate_v3_to_v4({"schema":"v3","payload":{"x":1},"token":"n-1"},"fixture-commit"),
        "C": atomic_publish_model(b"old",b"new"),
        "D": zip64_directory_gate([(10,20),(20,30)],2,10,30,32,40),
        "E": {"chain":custody_chain([{"sample":"s1","from":"a","to":"b","method":"m1","unit":"u","expiry":"2030","previous":"0"*64}])},
        "F": cost_per_output([{"low":1,"high":2,"unit":"USD"} for _ in range(4)],2),
        "G": covariance_block(["x","y","z"],["u","u","u"],[[1,0,0],[0,1,0],[0,0,1]],"fixture","synthetic","2030"),
        "H": priority_sensitivity(["a","b"],[{"a":2,"b":1},{"a":1,"b":2}],[{"a":1,"b":2}]),
        "FND/EQN": typed_interval([1,2],[0]*10,"a"*64),
        "SCM": {"fiction_only":True,"empirical_coupling":None},
        "AI-COST": lineage_manifest(b"synthetic-v2",{"train":["a"],"validation":["b"],"test":["c"]},{"train":{"loss":1},"validation":{"loss":1},"test":{"loss":1}}),
        "QOS/QSVT": migrate_er6({"version":1,"qubits":6,"bits":6,"depth":20,"gates":40,"source_sha256":"a"*64},{"version":2,"qubits":6,"bits":6,"depth":18,"gates":38,"source_sha256":"b"*64})
    }
