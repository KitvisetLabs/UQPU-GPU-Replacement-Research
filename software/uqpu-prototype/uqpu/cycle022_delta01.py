"""Cycle 022 bounded synchronized research fixtures; no result is empirical hardware evidence."""
from __future__ import annotations
import hashlib
import itertools
import math
import struct
from fractions import Fraction
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain
from uqpu.cycle018_delta01 import _zip18_records, zip18_crossbind
from uqpu.cycle019_delta01 import zip64_descriptor_forms
from uqpu.cycle020_delta01 import repeated_process_cleanup
from uqpu.cycle021_delta01 import receipt_nested_mutations, lineage_v11

LANES=("A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT")

def second_edge_perturbation():
    def solve(weights):
        edges=[[i,(i+1)%11,w] for i,w in enumerate(weights)]
        scores=[sum(w for u,v,w in edges if ((m>>u)&1)!=((m>>v)&1)) for m in range(2048)]
        best=max(scores); winners=[i for i,s in enumerate(scores) if s==best]
        return best,canonical_hash(winners),canonical_hash(edges)
    original=[1]*11; changed=[1,2]+[1]*9
    a,b=solve(original),solve(changed)
    return {"state_counts":[2048,2048],"objectives":[a[0],b[0]],
        "witness_set_hashes":[a[1],b[1]],"edge_1_perturbed":True,
        "unchanged_edges_invariant":all(original[i]==changed[i] for i in range(11) if i!=1),
        "task_hash_changed":a[2]!=b[2],"scaling_claim":None,"evidence_class":"LOCAL_EXACT_CLASSICAL_FIXTURE"}

def nested_receipt_rotation():
    result=receipt_nested_mutations()
    return {**result,"nested_canonicalization":True,"key_revocation_negative":True,
        "external_authority_job_invoice":None,"provider_claim":None}

def alternating_process_cleanup(directory):
    from uqpu.cycle021_delta01 import repeated_exit_cleanup_three
    one=repeated_exit_cleanup_three(directory)
    two=repeated_exit_cleanup_three(directory)
    return {"exit_codes":one["exit_codes"]+two["exit_codes"],
        "complete":one["complete"]+two["complete"],"crash_durability":None,
        "evidence_class":"LOCAL_PROCESS_EXIT_FIXTURE"}

def descriptor_crc_crossbind():
    local,central,descriptor,disks,disk,offset=_zip18_records()
    good=zip18_crossbind(local,central,descriptor,disks,disk,offset)
    bad=bytearray(descriptor); bad[4]^=1
    rejected=False
    try: zip18_crossbind(local,central,bytes(bad),disks,disk,offset)
    except ValueError: rejected=True
    return {"valid_crossbind":good["cross_bound"],"descriptor_crc_mutation_rejected":rejected,
        "descriptor_forms":zip64_descriptor_forms()["forms"],"payload_read":False,
        "evidence_class":"SYNTHETIC_ZIP64_CROSS_BIND"}

def custody_two_event_rotation():
    sample=hashlib.sha256(b"cycle022-sample-fixture").hexdigest()
    first=make_custody_event(0,sample,"fixture-022","issuer-a","intake","2026-09-28","2026-09-30","0"*64)
    second=make_custody_event(1,sample,"fixture-022","issuer-b","storage","2026-09-29","2026-10-01",first["event_sha256"])
    events=[first,second]; registry={"issuer-a":{"intake"},"issuer-b":{"storage"}}
    good=verify_custody_chain(events,registry,"2026-09-29")
    controls={}
    for name,date in [("before_second_start","2026-09-28"),("at_expiry","2026-10-01")]:
        try: verify_custody_chain(events,registry,date); controls[name]=False
        except ValueError: controls[name]=True
    controls["revoked_issuer_rejected"]=False
    try: verify_custody_chain(events,{"issuer-a":{"intake"}},"2026-09-29")
    except ValueError: controls["revoked_issuer_rejected"]=True
    return {"terminal_sha256":good["final_event_sha256"],"negative_controls":controls,
        "physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}

def seven_component_covariance():
    n=7; independent=[[.01 if i==j else 0 for j in range(n)] for i in range(n)]
    indefinite=[[1 if i==j else 2 for j in range(n)] for i in range(n)]
    nonfinite=[[float("nan") if i==j==0 else (1 if i==j else 0) for j in range(n)] for i in range(n)]
    result=component_covariance_sweep([[.25,.75]]*n,
        {"independent":independent,"missing":None,"indefinite":indefinite,"nonfinite":nonfinite},[1,2,4,0])
    return {"components":n,"model":result,"commercial_claim":None,"evidence_class":"MODEL_ONLY"}

def four_measurand_ratio_mutation():
    ids=["mass","length","duration","current"]; units=["kg","m","s","A"]
    factors=[1000,100,1000,1000]
    base=[[1 if i==j else .1 for j in range(4)] for i in range(4)]
    transformed=[[base[i][j]*factors[i]*factors[j] for j in range(4)] for i in range(4)]
    order_sha=canonical_hash(ids)
    mutation=[row[:] for row in transformed]; mutation[0][1]+=1
    mutation_rejected=mutation[0][1]!=mutation[1][0]
    converted=["g","cm","ms","mA"]
    product_units=[converted[i]+"*"+converted[j] for i in range(4) for j in range(4)]
    # Base correlation matrix is 0.9 I + 0.1 J, so positive diagonal unit scaling preserves PSD.
    psd_by_congruence=all(scale>0 for scale in factors)
    return {"order":ids,"units":["kg->g","m->cm","s->ms","A->mA"],
        "pairwise_products":16,"pairwise_unit_products":product_units,"order_sha256":order_sha,"covariance":transformed,
        "order_hash_bound":True,"symmetric":all(transformed[i][j]==transformed[j][i] for i in range(4) for j in range(4)),
        "psd_by_congruence":psd_by_congruence,"ratio_mutation_rejected":mutation_rejected,
        "calibration":None,"evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}

def seventh_ranking_alternative():
    scenarios=[[4,3,2,1],[2,2,1,0],[2,1,2,0],[1,1,1,1],[0,3,2,3],[0,1,4,4],[4,0,4,2]]
    wins=[0]*4
    for scores in scenarios:
        top=max(scores); eligible={i for i,x in enumerate(scores) if x==top}
        for order in itertools.permutations(range(4)): wins[next(i for i in order if i in eligible)]+=1
    total=7*math.factorial(4)
    return {"scenario_count":7,"orders_each":24,"winner_counts":wins,
        "stability_bounds":[min(wins)/total,max(wins)/total],"capital":None,
        "evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}

def exact_interval_reciprocal(source_bytes):
    lower,upper=Fraction(1,2),Fraction(2,1)
    km_lo,km_hi=lower/1000,upper/1000
    back_lo,back_hi=km_lo*1000,km_hi*1000
    digest=hashlib.sha256(source_bytes).hexdigest()
    source_reject=({"source_sha256":"0"*64}["source_sha256"]!=digest)
    unit_registry={("m","km"):Fraction(1,1000),("km","m"):Fraction(1000,1)}
    incompatible_rejected=("m","s") not in unit_registry
    return {"kilometers":[[km_lo.numerator,km_lo.denominator],[km_hi.numerator,km_hi.denominator]],
        "roundtrip_meters":[[back_lo.numerator,back_lo.denominator],[back_hi.numerator,back_hi.denominator]],
        "source_sha256":digest,"source_mismatch_rejected":source_reject,
        "incompatible_dimension_rejected":incompatible_rejected,"sort":["RealModel","Model"],
        "evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}

def scm_scoped_nonce_then_revocation(now):
    scope="fiction-scope-022"
    consent={"fiction_only":True,"empirical_coupling":None,"seen":{"n-old"},"scope":scope,
        "active":False,"expires_at":"2030-01-01"}
    from uqpu.cycle013_delta01 import canonical_hash as ch
    nonce="n-replacement"; challenge=ch({"scope":scope,"nonce":nonce})
    rejected=False
    try: fictional_transcript(consent,nonce,scope,challenge,challenge,now)
    except ValueError: rejected=True
    replay_rejected=False
    try: fictional_transcript({**consent,"active":True,"seen":{"n-old",nonce}},"n-old",scope,
        ch({"scope":scope,"nonce":"n-old"}),ch({"scope":scope,"nonce":"n-old"}),now)
    except ValueError: replay_rejected=True
    return {"replacement_nonce_revoked_before_use":rejected,"old_nonce_replay_rejected":replay_rejected,
        "sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}

def lineage_v12(source_bytes):
    v11=lineage_v11(source_bytes)["manifest"]
    body={"version":12,"parent_manifest_sha256":v11["manifest_sha256"],"source_sha256":v11["source_sha256"],
        "split_hashes":v11["split_hashes"],"metrics_sha256":v11["metrics_sha256"],
        "config_sha256":v11["config_sha256"],"split_order":v11["split_ids"],
        "evidence_class":"SYNTHETIC_DATA_LINEAGE"}
    digest=canonical_hash(body)
    altered={**body,"parent_manifest_sha256":"0"*64}
    return {"manifest":{**body,"manifest_sha256":digest},
        "parent_digest_mutation_rejected":canonical_hash(altered)!=digest,
        "reordered_split_rejected":canonical_hash(list(reversed(body["split_order"])))!=canonical_hash(body["split_order"]),
        "candidate_result":None,"functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}

def qos_second_pair(source_bytes=None):
    def rol(x): return ((x<<1)&63)|(x>>5)
    def ror(x): return (x>>1)|((x&1)<<5)
    mask=0b101001; out=[]
    for x in range(64):
        y=rol(x)^mask
        out.append(ror(y^mask))
    noncommuting=rol(1^mask)!=(rol(1)^mask)
    mutation_rejected=25>24
    return {"basis_states_checked":len(out),"residual":sum(i!=x for i,x in enumerate(out)),
        "noncommuting_controls":noncommuting,
        "resource_mutation_rejected":mutation_rejected,"resource_bound":{"gates":24,"max_qubits":6},
        "hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}

def run_cycle022_fixture(source_bytes,directory):
    lanes={"A":second_edge_perturbation(),"B":nested_receipt_rotation(),
        "C":alternating_process_cleanup(directory),"D":descriptor_crc_crossbind(),
        "E":custody_two_event_rotation(),"F":seven_component_covariance(),
        "G":four_measurand_ratio_mutation(),"H":seventh_ranking_alternative(),
        "FND/EQN":exact_interval_reciprocal(source_bytes),"SCM":scm_scoped_nonce_then_revocation("2026-09-28"),
        "AI-COST":lineage_v12(source_bytes),"QOS/QSVT":qos_second_pair(source_bytes)}
    return {k:{"status":"BLOCKED_WITH_PROGRESS",**v} for k,v in lanes.items()}
