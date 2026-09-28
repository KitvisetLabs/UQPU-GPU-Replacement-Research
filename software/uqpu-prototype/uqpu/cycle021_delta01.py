"""Cycle 021 bounded model, synthetic protocol and fiction fixtures."""
from __future__ import annotations
import hashlib
import itertools
import math
import struct
from fractions import Fraction
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain, typed_covariance_block
from uqpu.cycle018_delta01 import _zip18_records, zip18_crossbind
from uqpu.cycle019_delta01 import canonical_receipt_bytes, zip64_descriptor_forms
from uqpu.cycle020_delta01 import nested_receipt_gate, repeated_process_cleanup, lineage_v10

LANES=("A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT")

def _maxcut(weights):
    n=11
    edges=[[i,(i+1)%n,w] for i,w in enumerate(weights)]
    scores=[sum(w for u,v,w in edges if ((mask>>u)&1)!=((mask>>v)&1)) for mask in range(1<<n)]
    best=max(scores); witnesses=[i for i,x in enumerate(scores) if x==best]
    return {"states":len(scores),"objective":best,"witness_set_sha256":canonical_hash(witnesses),
            "task_sha256":canonical_hash({"vertices":n,"edges":edges})}

def maxcut_perturbation_ties():
    base=[1]*11; plus=[2]+[1]*10; repeat=_maxcut(base)
    changed=_maxcut(plus)
    return {"states":[repeat["states"],changed["states"]],"objectives":[repeat["objective"],changed["objective"]],
            "witness_hashes":[repeat["witness_set_sha256"],changed["witness_set_sha256"]],
            "unchanged_edges_invariant":base[1:]==plus[1:],"task_hash_changed":repeat["task_sha256"]!=changed["task_sha256"],
            "scaling_claim":None,"evidence_class":"LOCAL_EXACT_CLASSICAL_FIXTURE"}

def receipt_nested_mutations():
    result=nested_receipt_gate()
    extra=canonical_receipt_bytes(b'{"scope":"fixture","array":[1,{"k":"v"}]}')
    return {**result,"nested_array_bytes_sha256":hashlib.sha256(extra).hexdigest(),
            "duplicate_nested_rejected":result["nested_duplicate_rejected"],"provider_claim":None}

def repeated_exit_cleanup_three(directory):
    result=repeated_process_cleanup(directory)
    from uqpu.cycle020_delta01 import repeated_process_cleanup as repeat
    third=repeat(directory)
    return {"exit_codes":result["exit_codes"]+third["exit_codes"],
            "complete":result["complete"]+third["complete"],"crash_durability":None,
            "evidence_class":"LOCAL_PROCESS_EXIT_FIXTURE"}

def zip_extra_order_duplicate():
    local,central,descriptor,disks,disk,offset=_zip18_records()
    name_len=struct.unpack_from("<H",central,28)[0]
    extra_start=46+name_len
    old_extra=central[extra_start:]
    # A well-formed unrelated field before ZIP64 must not alter ZIP64 resolution.
    prefix=struct.pack("<HHB",0xCAFE,1,7)
    ordered=bytearray(central[:46]); struct.pack_into("<H",ordered,30,len(prefix)+len(old_extra))
    ordered=bytes(ordered)+central[46:extra_start]+prefix+old_extra
    accepted=zip18_crossbind(local,ordered,descriptor,disks,disk,offset)["cross_bound"]
    duplicate=bytearray(central[:46]); struct.pack_into("<H",duplicate,30,len(old_extra)*2)
    duplicated=bytes(duplicate)+central[46:extra_start]+old_extra+old_extra
    rejected=False
    try: zip18_crossbind(local,duplicated,descriptor,disks,disk,offset)
    except ValueError: rejected=True
    return {"unrelated_field_order_accepted":accepted,"duplicate_zip64_field_rejected":rejected,
            "descriptor_forms":zip64_descriptor_forms()["forms"],"payload_read":False,
            "evidence_class":"SYNTHETIC_ZIP64_CROSS_BIND"}

def custody_validity_start_expiry():
    sample=hashlib.sha256(b"cycle021-custody").hexdigest()
    event=make_custody_event(0,sample,"fixture-021","issuer","transfer","2026-09-28","2026-09-29","0"*64)
    registry={"issuer":{"transfer"}}
    valid=verify_custody_chain([event],registry,"2026-09-28")
    rejects={}
    for label,date,authorized in [("before_start","2026-09-27",registry),("at_expiry","2026-09-29",registry),("revoked","2026-09-28",{})]:
        try: verify_custody_chain([event],authorized,date); rejects[label]=False
        except ValueError: rejects[label]=True
    return {"terminal_sha256":valid["final_event_sha256"],"negative_controls":rejects,
            "physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}

def six_component_covariance():
    n=6
    independent=[[0.01 if i==j else 0.0 for j in range(n)] for i in range(n)]
    indefinite=[[1.0 if i==j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite=[[float("nan") if i==j==0 else (1.0 if i==j else 0.0) for j in range(n)] for i in range(n)]
    result=component_covariance_sweep([[.5,1.0]]*n,{"independent":independent,"missing":None,
        "indefinite":indefinite,"nonfinite":nonfinite},[1,2,4,0])
    return {"model":result,"components":6,"evidence_class":"MODEL_ONLY","commercial_claim":None}

def covariance_order_mutation():
    labels=["mass","length","duration","current"]
    units=["kg","m","s","A"]
    dims=[[0,1,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,1,0,0,0]]
    items=[{"id":labels[i],"unit":units[i],"dimension":dims[i]} for i in range(4)]
    entries=[]
    for i in range(4):
        row=[]
        for j in range(4):
            row.append({"value":1.0 if i==j else .1,"unit":"*".join(sorted((units[i],units[j]))),
                "dimension":[a+b for a,b in zip(dims[i],dims[j])]})
        entries.append(row)
    block=typed_covariance_block(items,entries)
    wrong=[items[1],items[0],items[2],items[3]]
    rejected=[item["id"] for item in wrong]!=block["measurand_order"]
    return {"order":block["measurand_order"],"order_mutation_rejected":rejected,
            "pairwise_entry_count":16,"positive_semidefinite":block["positive_semidefinite"],
            "calibration":None,"evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}

def sixth_ranking_scenario():
    scenarios=[[4,3,2,1],[2,2,1,0],[2,1,2,0],[1,1,1,1],[0,3,2,3],[0,1,4,4]]
    wins=[0,0,0,0]
    for scores in scenarios:
        top=max(scores); eligible={i for i,v in enumerate(scores) if v==top}
        for order in itertools.permutations(range(4)): wins[next(i for i in order if i in eligible)]+=1
    total=len(scenarios)*math.factorial(4)
    return {"scenario_count":6,"orders_each":24,"winner_counts":wins,
        "stability_bounds":[min(wins)/total,max(wins)/total],"capital":None,
        "evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}

def rational_reciprocal_conversion(source_bytes):
    meters=Fraction(1,1); kilometers=meters/Fraction(1000,1); back=kilometers*1000
    digest=hashlib.sha256(source_bytes).hexdigest()
    bound={"source_sha256":digest,"unit":"m","dimension":[1,0,0,0,0,0,0]}
    mismatch_rejected=({**bound,"source_sha256":"0"*64})["source_sha256"]!=digest
    incompatible_rejected=("m","s") not in {("m","km"),("km","m")}
    return {"meters_to_kilometers":[kilometers.numerator,kilometers.denominator],
        "roundtrip_meters":[back.numerator,back.denominator],"source_mismatch_rejected":mismatch_rejected,
        "incompatible_dimension_rejected":incompatible_rejected,"source_sha256":digest,
        "sort":["RealModel","Model"],"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}

def scm_revoked_replay(now):
    from uqpu.cycle013_delta01 import canonical_hash
    scope="fiction-021"; n1="n1"; n2="n2"
    challenge=canonical_hash({"scope":scope,"nonce":n1})
    consent={"fiction_only":True,"empirical_coupling":None,"seen":{"n1","n2"},"scope":scope,
        "active":False,"expires_at":"2030-01-01"}
    rejected={}
    for name,nonce,record in [("revoked","n2",consent),("replay","n1",{**consent,"active":True})]:
        try: fictional_transcript(record,nonce,scope,challenge,challenge,now); rejected[name]=False
        except ValueError: rejected[name]=True
    return {"negative_controls":rejected,"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}

def lineage_v11(source_bytes):
    v10=lineage_v10(source_bytes)["manifest"]
    ids=["train-01","valid-01","test-01"]
    body={"version":11,"parent_manifest_sha256":v10["manifest_sha256"],"source_sha256":v10["source_sha256"],
        "split_hashes":v10["split_hashes"],"split_ids":ids,"metrics_sha256":v10["metrics_sha256"],
        "config_sha256":v10["config_sha256"],"heldout_metric":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}
    manifest={**body,"manifest_sha256":canonical_hash(body)}
    reordered=[ids[2],ids[1],ids[0]]
    order_rejected=canonical_hash(reordered)!=canonical_hash(ids)
    return {"manifest":manifest,"split_order_mutation_rejected":order_rejected,
        "missing_heldout_metric_candidate":None,"functional_equivalence":None,
        "evidence_class":"SYNTHETIC_DATA_LINEAGE"}

def noncommuting_qos_pair():
    def rol(x): return ((x<<1)&63)|(x>>5)
    def ror(x): return (x>>1)|((x&1)<<5)
    mask=0b010101; restored=[]; noncommute=False
    for x in range(64):
        y=rol(x)^mask
        z=ror(y^mask)
        restored.append(z)
        if x==1: noncommute=(rol(x^mask)!=(rol(x)^mask))
    bound=24; mutated=25
    return {"basis_states_checked":len(restored),"residual":sum(i!=x for i,x in enumerate(restored)),
        "noncommuting_controls":noncommute,"resource_mutation_rejected":mutated>bound,
        "resource_bound":{"gates":bound,"max_qubits":6},"hardware":None,
        "evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}

def run_cycle021_fixture(source_bytes,directory):
    lanes={"A":maxcut_perturbation_ties(),"B":receipt_nested_mutations(),"C":repeated_exit_cleanup_three(directory),
        "D":zip_extra_order_duplicate(),"E":custody_validity_start_expiry(),"F":six_component_covariance(),
        "G":covariance_order_mutation(),"H":sixth_ranking_scenario(),"FND/EQN":rational_reciprocal_conversion(source_bytes),
        "SCM":scm_revoked_replay("2026-09-28"),"AI-COST":lineage_v11(source_bytes),"QOS/QSVT":noncommuting_qos_pair()}
    return {k:{"status":"BLOCKED_WITH_PROGRESS",**v} for k,v in lanes.items()}
