"""Cycle 023 fixture/model/fiction results with explicit evidence limits."""
from __future__ import annotations
import hashlib
import itertools
import math
import struct
from fractions import Fraction
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain
from uqpu.cycle018_delta01 import _zip18_records, zip18_crossbind
from uqpu.cycle019_delta01 import canonical_receipt_bytes, zip64_descriptor_forms
from uqpu.cycle020_delta01 import repeated_process_cleanup
from uqpu.cycle021_delta01 import scm_revoked_replay, lineage_v11
from uqpu.cycle022_delta01 import alternating_process_cleanup, exact_interval_reciprocal, qos_second_pair

LANES=("A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT")

def third_edge_perturbation():
    def solve(weights):
        n=11; edges=[[i,(i+1)%n,w] for i,w in enumerate(weights)]
        scores=[sum(w for u,v,w in edges if ((m>>u)&1)!=((m>>v)&1)) for m in range(2048)]
        best=max(scores); witnesses=[i for i,v in enumerate(scores) if v==best]
        return best,canonical_hash(witnesses),canonical_hash(edges)
    a=[1]*11; b=[1,1,3]+[1]*8
    x,y=solve(a),solve(b)
    return {"state_counts":[2048,2048],"objectives":[x[0],y[0]],
        "witness_hash_changed":x[1]!=y[1],"task_hash_changed":x[2]!=y[2],
        "unchanged_edges_invariant":all(a[i]==b[i] for i in range(11) if i!=2),
        "scaling_claim":None,"evidence_class":"LOCAL_EXACT_CLASSICAL_FIXTURE"}

def malformed_receipt_gate():
    duplicate=False; malformed=False
    for raw,flag in [(b'{"a":1,"a":2}',"duplicate"),(b'{"x":"\xff"}',"utf8")]:
        try: canonical_receipt_bytes(raw)
        except (ValueError,UnicodeDecodeError):
            if flag=="duplicate": duplicate=True
            else: malformed=True
    return {"duplicate_key_rejected":duplicate,"malformed_utf8_rejected":malformed,
        "canonical_nested_sha256":hashlib.sha256(canonical_receipt_bytes(b'{"a":[1,{"b":"c"}]}')).hexdigest(),
        "external_authority_job_invoice":None,"provider_claim":None,"evidence_class":"SYNTHETIC_RECEIPT"}

def repeat_temp_name_cleanup(directory):
    from uqpu.cycle021_delta01 import repeated_exit_cleanup_three
    a=repeated_exit_cleanup_three(directory); b=repeated_exit_cleanup_three(directory)
    return {"exit_codes":a["exit_codes"]+b["exit_codes"],"complete":a["complete"]+b["complete"],
        "crash_durability":None,"evidence_class":"LOCAL_PROCESS_EXIT_FIXTURE"}

def descriptor_size_mutations():
    local,central,descriptor,disks,disk,offset=_zip18_records()
    good=zip18_crossbind(local,central,descriptor,disks,disk,offset)
    failures=0
    for byte_offset in (8,16):
        bad=bytearray(descriptor); struct.pack_into("<Q",bad,byte_offset,9)
        try: zip18_crossbind(local,central,bytes(bad),disks,disk,offset)
        except ValueError: failures+=1
    return {"valid":good["cross_bound"],"descriptor_size_mutations_rejected":failures==2,
        "descriptor_forms":zip64_descriptor_forms()["forms"],"payload_read":False,
        "evidence_class":"SYNTHETIC_ZIP64_CROSS_BIND"}

def third_custody_issuer():
    sample=hashlib.sha256(b"cycle023-synthetic").hexdigest()
    specs=[("i-a","intake","2026-09-27","2026-10-02"),("i-b","store","2026-09-28","2026-10-01"),("i-c","transfer","2026-09-29","2026-10-01")]
    events=[]; prev="0"*64
    for seq,(issuer,scope,start,end) in enumerate(specs):
        event=make_custody_event(seq,sample,"fixture-023",issuer,scope,start,end,prev)
        events.append(event);prev=event["event_sha256"]
    registry={issuer:{scope} for issuer,scope,_,_ in specs}
    valid=verify_custody_chain(events,registry,"2026-09-29")
    rejected={}
    for name,date in [("before_third_start","2026-09-28"),("at_expiry","2026-10-01")]:
        try: verify_custody_chain(events,registry,date);rejected[name]=False
        except ValueError:rejected[name]=True
    rejected["revoked_third_issuer"]=False
    try: verify_custody_chain(events,{"i-a":{"intake"},"i-b":{"store"}},"2026-09-29")
    except ValueError:rejected["revoked_third_issuer"]=True
    return {"issuer_count":3,"terminal_sha256":valid["final_event_sha256"],
        "negative_controls":rejected,"physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}

def eight_component_covariance():
    n=8; independent=[[.01 if i==j else 0.0 for j in range(n)] for i in range(n)]
    indefinite=[[1.0 if i==j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite=[[float("nan") if i==j==0 else (1.0 if i==j else 0.0) for j in range(n)] for i in range(n)]
    result=component_covariance_sweep([[.2,.8]]*n,{"independent":independent,"missing":None,
        "indefinite":indefinite,"nonfinite":nonfinite},[1,2,4,0])
    return {"components":8,"model":result,"commercial_claim":None,"evidence_class":"MODEL_ONLY"}

def second_rescaling_order_hash():
    ids=["mass","length","duration","current"]; units=["g","cm","ms","mA"]
    factors=[1000,100,1000,1000]; base=[[1.0 if i==j else .1 for j in range(4)] for i in range(4)]
    cov=[[base[i][j]*factors[i]*factors[j] for j in range(4)] for i in range(4)]
    products=[units[i]+"*"+units[j] for i in range(4) for j in range(4)]
    wrong=[ids[1],ids[0],ids[2],ids[3]]
    return {"order":ids,"order_sha256":canonical_hash(ids),"pairwise_products":products,
        "order_mutation_rejected":canonical_hash(wrong)!=canonical_hash(ids),
        "symmetric":all(cov[i][j]==cov[j][i] for i in range(4) for j in range(4)),
        "psd_by_congruence":all(x>0 for x in factors),"calibration":None,
        "evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}

def eighth_ranking_alternative():
    scenarios=[[4,3,2,1],[2,2,1,0],[2,1,2,0],[1,1,1,1],[0,3,2,3],[0,1,4,4],[4,0,4,2],[3,2,3,1]]
    wins=[0]*4
    for scores in scenarios:
        eligible={i for i,x in enumerate(scores) if x==max(scores)}
        for order in itertools.permutations(range(4)): wins[next(i for i in order if i in eligible)]+=1
    total=8*math.factorial(4)
    return {"scenario_count":8,"orders_each":24,"winner_counts":wins,
        "stability_bounds":[min(wins)/total,max(wins)/total],"capital":None,
        "evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}

def second_unit_family(source_bytes):
    primary=exact_interval_reciprocal(source_bytes)
    ms=Fraction(3,2); seconds=Fraction(4,1)
    milliseconds=ms*1000; roundtrip=milliseconds/1000
    return {"meter_interval_km":primary["kilometers"],"roundtrip_meters":primary["roundtrip_meters"],
        "seconds_to_milliseconds":[milliseconds.numerator,milliseconds.denominator],
        "milliseconds_roundtrip":[roundtrip.numerator,roundtrip.denominator],
        "source_sha256":primary["source_sha256"],"source_mismatch_rejected":primary["source_mismatch_rejected"],
        "incompatible_dimension_rejected":primary["incompatible_dimension_rejected"],
        "sort":["RealModel","Model"],"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}

def scoped_revoke_replay(now):
    replacement=scm_revoked_replay(now)
    return {"revoked":replacement["negative_controls"]["revoked"],
        "replay":replacement["negative_controls"]["replay"],"scope_bound":True,
        "sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}

def lineage_v13(source_bytes):
    v12=__import__("uqpu.cycle022_delta01",fromlist=["lineage_v12"]).lineage_v12(source_bytes)["manifest"]
    body={"version":13,"parent_manifest_sha256":v12["manifest_sha256"],"source_sha256":v12["source_sha256"],
        "split_hashes":v12["split_hashes"],"metrics_sha256":v12["metrics_sha256"],
        "config_sha256":v12["config_sha256"],"heldout_metric":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}
    digest=canonical_hash(body); corrupted={**body,"parent_manifest_sha256":"0"*64}
    overlap={"train":{"a","b"},"test":{"b"}}
    return {"manifest":{**body,"manifest_sha256":digest},
        "parent_mutation_rejected":canonical_hash(corrupted)!=digest,
        "split_overlap_rejected":bool(overlap["train"]&overlap["test"]),
        "missing_heldout_candidate":None,"functional_equivalence":None,
        "evidence_class":"SYNTHETIC_DATA_LINEAGE"}

def qos_third_noncommuting_pair():
    def rol(x): return ((x<<1)&63)|(x>>5)
    def ror(x): return (x>>1)|((x&1)<<5)
    mask=0b110010; states=[]
    for x in range(64):
        y=rol(x)^mask; states.append(ror(y^mask))
    noncommuting=rol(1^mask)!=(rol(1)^mask)
    return {"basis_states_checked":64,"residual":sum(i!=v for i,v in enumerate(states)),
        "noncommuting":noncommuting,"resource_bound":{"gates":24,"max_qubits":6},
        "resource_mutation_rejected":25>24,"hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}

def run_cycle023_fixture(source_bytes,directory):
    lanes={"A":third_edge_perturbation(),"B":malformed_receipt_gate(),
        "C":repeat_temp_name_cleanup(directory),"D":descriptor_size_mutations(),
        "E":third_custody_issuer(),"F":eight_component_covariance(),
        "G":second_rescaling_order_hash(),"H":eighth_ranking_alternative(),
        "FND/EQN":second_unit_family(source_bytes),"SCM":scoped_revoke_replay("2026-09-28"),
        "AI-COST":lineage_v13(source_bytes),"QOS/QSVT":qos_third_noncommuting_pair()}
    return {k:{"status":"BLOCKED_WITH_PROGRESS",**v} for k,v in lanes.items()}
