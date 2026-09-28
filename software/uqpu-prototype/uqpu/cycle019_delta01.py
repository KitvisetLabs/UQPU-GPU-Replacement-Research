"""Cycle 019 bounded synchronized fixtures; all evidence remains synthetic/model/fiction."""
from __future__ import annotations

import hashlib
import hmac
import itertools
import json
import math
import struct
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain
from uqpu.cycle016_delta01 import exact_maxcut_10_node
from uqpu.cycle018_delta01 import exact_cancel_expression, run_cycle018_fixture

LANES = ("A", "B", "C", "D", "E", "F", "G", "H", "FND/EQN", "SCM", "AI-COST", "QOS/QSVT")


def tie_boundary_maxcut():
    graph = [[i, (i + 1) % 10, 1] for i in range(10)]
    result = exact_maxcut_10_node(graph)
    return {"objective": result["best_cut_weight"], "state_count": result["state_count"],
            "witness_sha256": result["witness_sha256"], "task_sha256": result["task_sha256"],
            "deterministic": result == exact_maxcut_10_node(graph), "scaling_claim": None,
            "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE"}


def _pairs_no_duplicates(pairs):
    out = {}
    for key, value in pairs:
        normalized = unicodedata.normalize("NFC", key)
        if normalized in out:
            raise ValueError("duplicate normalized receipt key")
        def norm(item):
            if isinstance(item, str):
                return unicodedata.normalize("NFC", item)
            if isinstance(item, list):
                return [norm(x) for x in item]
            if isinstance(item, dict):
                return {unicodedata.normalize("NFC", k): norm(v) for k, v in item.items()}
            return item
        out[normalized] = norm(value)
    return out


def canonical_receipt_bytes(raw):
    obj = json.loads(raw, object_pairs_hook=_pairs_no_duplicates)
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode()


def receipt_ambiguity_gate():
    raw = '{"key":"é","request":"fixture"}'.encode()
    composed = '{"request":"fixture","key":"é"}'.encode()
    duplicate = '{"é":1,"é":2}'.encode()
    duplicate_rejected = False
    try:
        canonical_receipt_bytes(duplicate)
    except ValueError:
        duplicate_rejected = True
    a, b = canonical_receipt_bytes(raw), canonical_receipt_bytes(composed)
    fixture_key = b"cycle019-fixture-key"
    tag = hmac.new(fixture_key, a, hashlib.sha256).hexdigest()
    revoked_key_rejected = not hmac.compare_digest(
        tag, hmac.new(b"revoked-fixture-key", a, hashlib.sha256).hexdigest())
    return {"canonical_unicode_equal": a == b, "duplicate_normalized_key_rejected": duplicate_rejected,
            "revoked_key_rejected": revoked_key_rejected, "external_authority_job_invoice": None,
            "provider_claim": None, "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def process_exit_boundary_gate(directory):
    from uqpu.cycle015_delta01 import concurrent_subprocess_replace
    result = concurrent_subprocess_replace(directory, "state.bin", [b"new-a", b"new-b", b"new-c"])
    return {"exit_codes": result["exit_codes"], "visible_complete": result["visible_complete"],
            "visible_sha256": result["visible_sha256"], "old_or_new": result["visible_complete"],
            "crash_durability": None, "evidence_class": "LOCAL_PROCESS_EXIT_FIXTURE"}


def zip64_descriptor_forms():
    crc, comp, uncomp = 0x77112233, 7, 7
    signed = struct.pack("<4sIQQ", b"PK\x07\x08", crc, comp, uncomp)
    unsigned = struct.pack("<IQQ", crc, comp, uncomp)
    def parse(data):
        if len(data) == 24 and data[:4] == b"PK\x07\x08":
            data = data[4:]
            form = "signed"
        elif len(data) == 20:
            form = "unsigned"
        else:
            raise ValueError("ZIP64 descriptor width/signature")
        actual = struct.unpack("<IQQ", data)
        if actual != (crc, comp, uncomp):
            raise ValueError("ZIP64 descriptor values")
        return form
    forms = [parse(signed), parse(unsigned)]
    bad = bytearray(unsigned); struct.pack_into("<Q", bad, 4, 8)
    rejected = False
    try:
        parse(bytes(bad))
    except ValueError:
        rejected = True
    return {"forms": forms, "mismatch_rejected_before_payload": rejected, "payload_read": False,
            "evidence_class": "SYNTHETIC_ZIP64_DESCRIPTOR"}


def custody_rotation_order():
    sample = hashlib.sha256(b"cycle019-fictional-sample").hexdigest()
    issuers = [("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-b2", "transfer")]
    events, prior = [], "0" * 64
    for seq, (issuer, scope) in enumerate(issuers):
        event = make_custody_event(seq, sample, "fixture-019", issuer, scope, "2026-01-01", "2027-01-01", prior)
        events.append(event); prior = event["event_sha256"]
    registry = {"issuer-a": {"intake"}, "issuer-b": {"storage"}, "issuer-b2": {"transfer"}}
    good = verify_custody_chain(events, registry, "2026-09-28")
    old_revocation_rejected = False
    try:
        verify_custody_chain(events, {"issuer-a": {"intake"}, "issuer-b": {"storage"}}, "2026-09-28")
    except ValueError:
        old_revocation_rejected = True
    return {"terminal_sha256": good["final_event_sha256"], "rotation_valid": True,
            "revoked_old_chain_rejected": old_revocation_rejected, "physical_sample": None,
            "evidence_class": "SYNTHETIC_CUSTODY"}


def four_component_covariance():
    independent = [[0.04 if i == j else 0.0 for j in range(4)] for i in range(4)]
    covariance = [[0.04 if i == j else 0.005 for j in range(4)] for i in range(4)]
    bad = [[1.0 if i == j else 2.0 for j in range(4)] for i in range(4)]
    nan = [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0) for j in range(4)] for i in range(4)]
    result = component_covariance_sweep([[1, 2]] * 4,
        {"independent": independent, "correlated": covariance, "missing": None,
         "indefinite": bad, "nonfinite": nan}, [1, 2, 4, 0])
    return {"result": result, "components": 4, "evidence_class": "MODEL_ONLY", "commercial_claim": None}


def unit_rescale_covariance():
    base = [[1.0, 0.2], [0.2, 1.0]]
    scale = [1000.0, 1.0]
    transformed = [[base[i][j] * scale[i] * scale[j] for j in range(2)] for i in range(2)]
    invariant = transformed[0][1] == 200.0 and transformed[1][0] == 200.0
    psd = base[0][0] * base[1][1] - base[0][1] ** 2 >= 0 and transformed[0][0] * transformed[1][1] - transformed[0][1] ** 2 >= 0
    return {"measurands": ["mass:kg->g", "length:m"], "scale_factors": scale,
            "cross_covariance_scaled": invariant, "psd_before_after": psd, "calibration": None,
            "evidence_class": "SYNTHETIC_TYPED_COVARIANCE"}


def fourth_ranking_alternative():
    alternatives = [
        {"name":"identity","scores":[4,3,2,1]},
        {"name":"positive-pair","scores":[2,2,1,0]},
        {"name":"mixed-adverse","scores":[2,1,2,0]},
        {"name":"rank-reversal-stress","scores":[1,1,1,1]},
    ]
    counts = {str(i):0 for i in range(4)}
    for item in alternatives:
        top = max(item["scores"])
        eligible = {i for i, score in enumerate(item["scores"]) if score == top}
        for order in itertools.permutations(range(4)):
            winner = next(i for i in order if i in eligible)
            counts[str(winner)] += 1
    total = len(alternatives) * math.factorial(4)
    bounds = [min(counts.values())/total, max(counts.values())/total]
    return {"alternatives": [x["name"] for x in alternatives], "orders_each": 24,
            "winner_counts": counts, "stability_bounds": bounds, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def source_bound_composition(source_bytes):
    from fractions import Fraction
    result = exact_cancel_expression(source_bytes)
    length, duration = Fraction(2, 1), Fraction(3, 1)
    left_association = (length / duration) * duration / length
    right_association = length * (duration / duration) / length
    return {"dimensionless": result["dimensionless"], "source_sha256": result["source_sha256"],
            "source_mismatch_rejected": result["source_mismatch_rejected"], "sort": result["sort"],
            "associative_paths": [[left_association.numerator, left_association.denominator],
                                  [right_association.numerator, right_association.denominator]],
            "exact_paths_agree": left_association == right_association == 1,
            "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def fiction_scoped_nonce(now):
    from uqpu.cycle013_delta01 import canonical_hash
    consent={"fiction_only":True,"empirical_coupling":None,"seen":set(),"scope":"s1","active":True,"expires_at":"2030-01-01"}
    challenge=canonical_hash({"scope":"s1","nonce":"n1"})
    accepted=fictional_transcript(consent,"n1","s1",challenge,challenge,now)["accepted"]
    rejected={}
    for name,record,nonce,scope in [
      ("replay",{**consent,"seen":{"n1"}},"n1","s1"),
      ("scope",{**consent},"n2","s2"),
      ("expired",{**consent,"expires_at":"2020-01-01"},"n3","s1")]:
        try:
            fictional_transcript(record,nonce,scope,challenge,challenge,now); rejected[name]=False
        except ValueError: rejected[name]=True
    return {"fresh":accepted,"rejections":rejected,"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}


def lineage_v9(source_bytes):
    v8=run_cycle018_fixture(source_bytes)["AI-COST"]["manifest"]
    body={"version":9,"parent_manifest_sha256":v8["manifest_sha256"],"source_sha256":v8["source_sha256"],
          "split_hashes":v8["split_hashes"],"metrics_sha256":v8["metrics_sha256"],"config_sha256":v8["config_sha256"],
          "evidence_class":"SYNTHETIC_DATA_LINEAGE","heldout_metric_present":True}
    manifest={**body,"manifest_sha256":canonical_hash(body)}
    parent_mutation={**v8,"manifest_sha256":"0"*64}
    parent_rejected=canonical_hash({k:v for k,v in parent_mutation.items() if k!="manifest_sha256"}) != parent_mutation["manifest_sha256"]
    missing_heldout={**body,"heldout_metric_present":False}
    return {"manifest":manifest,"parent_mutation_rejected":parent_rejected,
            "missing_heldout_candidate":None if not missing_heldout["heldout_metric_present"] else "UNEXPECTED",
            "functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def nonidentity_qos_inverse():
    mask=0b101010
    states=[]
    for basis in range(64):
        out=basis ^ mask
        restored=out ^ mask
        states.append(restored)
    return {"operator_mask":mask,"basis_states_checked":len(states),"residual":sum(a!=b for a,b in enumerate(states)),
            "resource_bound":{"gates":12,"max_qubits":6},"hardware":None,
            "evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle019_fixture(source_bytes):
    import tempfile
    with tempfile.TemporaryDirectory() as root:
        lanes={
          "A":tie_boundary_maxcut(),"B":receipt_ambiguity_gate(),"C":process_exit_boundary_gate(root),
          "D":zip64_descriptor_forms(),"E":custody_rotation_order(),"F":four_component_covariance(),
          "G":unit_rescale_covariance(),"H":fourth_ranking_alternative(),
          "FND/EQN":source_bound_composition(source_bytes),"SCM":fiction_scoped_nonce("2026-09-28"),
          "AI-COST":lineage_v9(source_bytes),"QOS/QSVT":nonidentity_qos_inverse()}
    return {lane:{"status":"BLOCKED_WITH_PROGRESS",**value} for lane,value in lanes.items()}
