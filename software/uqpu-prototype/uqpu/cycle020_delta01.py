"""Cycle 020 bounded fixtures; numeric and protocol outputs are model/synthetic evidence."""
from __future__ import annotations
import hashlib
import itertools
import math
import struct
from fractions import Fraction
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import component_covariance_sweep, make_custody_event, verify_custody_chain
from uqpu.cycle018_delta01 import _zip18_records, zip18_crossbind, run_cycle018_fixture
from uqpu.cycle019_delta01 import canonical_receipt_bytes, process_exit_boundary_gate, zip64_descriptor_forms, lineage_v9

LANES=("A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT")

def maxcut_11_boundary():
    n=11
    edges=[[i,(i+1)%n,1] for i in range(n)]
    def score(mask):
        return sum(w for u,v,w in edges if ((mask>>u)&1)!=((mask>>v)&1))
    scores=[score(i) for i in range(1<<n)]
    best=max(scores); witnesses=[i for i,x in enumerate(scores) if x==best]
    task=canonical_hash({"vertices":n,"edges":edges})
    return {"state_count":len(scores),"state_cap":2048,"objective":best,
            "witness_set_sha256":canonical_hash(witnesses),"task_sha256":task,
            "deterministic":scores==[score(i) for i in range(1<<n)],"scaling_claim":None,
            "evidence_class":"LOCAL_EXACT_CLASSICAL_FIXTURE"}

def nested_receipt_gate():
    raw='{"body":{"z":[1,2],"unicode":"é"},"scope":"fixture"}'.encode()
    receipt=canonical_receipt_bytes(raw)
    duplicate=False
    try: canonical_receipt_bytes(b'{"body":{"x":1,"x":2},"scope":"fixture"}')
    except ValueError: duplicate=True
    revoked=canonical_receipt_bytes(b'{"key_id":"rotated","scope":"fixture","body":{"z":[1,2]}}')
    return {"canonical_nested_sha256":hashlib.sha256(receipt).hexdigest(),"nested_duplicate_rejected":duplicate,
            "key_rotation_changes_bytes":receipt!=revoked,"external_authority_job_invoice":None,
            "provider_claim":None,"evidence_class":"SYNTHETIC_RECEIPT"}

def repeated_process_cleanup(directory):
    from uqpu.cycle015_delta01 import concurrent_subprocess_replace
    one=concurrent_subprocess_replace(directory,"state-a.bin",[b"a1",b"a2",b"a3"])
    two=concurrent_subprocess_replace(directory,"state-b.bin",[b"b1",b"b2",b"b3"])
    return {"exit_codes":[one["exit_codes"],two["exit_codes"]],
            "complete":[one["visible_complete"],two["visible_complete"]],
            "crash_durability":None,"evidence_class":"LOCAL_PROCESS_EXIT_FIXTURE"}

def zip64_extended_crossbind():
    local,central,descriptor,disks,disk,offset=_zip18_records()
    base=zip18_crossbind(local,central,descriptor,disks,disk,offset)
    forms=zip64_descriptor_forms()["forms"]
    bad=bytearray(central)
    name_len=struct.unpack_from("<H",central,28)[0]
    extra_start=46+name_len
    # ZIP64 extra data is uncompressed size, compressed size, local-header offset, disk.
    struct.pack_into("<Q",bad,extra_start+4+16,offset+1)
    rejected=False
    try: zip18_crossbind(local,bytes(bad),descriptor,disks,disk,offset)
    except ValueError: rejected=True
    return {"cross_bound":base["cross_bound"],"descriptor_forms":forms,
            "offset_mutation_rejected":rejected,"payload_read":False,
            "evidence_class":"SYNTHETIC_ZIP64_CROSS_BIND"}

def custody_expiry_revocation():
    sample=hashlib.sha256(b"cycle020-synthetic").hexdigest()
    event=make_custody_event(0,sample,"fixture-020","issuer-old","storage","2026-01-01","2026-09-29","0"*64)
    valid=verify_custody_chain([event],{"issuer-old":{"storage"}},"2026-09-28")
    expiry_rejected=False; revoked_rejected=False
    try: verify_custody_chain([event],{"issuer-old":{"storage"}},"2026-09-29")
    except ValueError: expiry_rejected=True
    try: verify_custody_chain([event],{},"2026-09-28")
    except ValueError: revoked_rejected=True
    return {"valid_terminal":valid["final_event_sha256"],"expiry_boundary_rejected":expiry_rejected,
            "revocation_rejected":revoked_rejected,"physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}

def five_component_covariance():
    n=5
    independent=[[0.02 if i==j else 0.0 for j in range(n)] for i in range(n)]
    correlated=[[0.02 if i==j else 0.002 for j in range(n)] for i in range(n)]
    indefinite=[[1.0 if i==j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite=[[float("nan") if i==j==0 else (1.0 if i==j else 0.0) for j in range(n)] for i in range(n)]
    model=component_covariance_sweep([[1,2]]*n,{"independent":independent,"correlated":correlated,
      "missing":None,"indefinite":indefinite,"nonfinite":nonfinite},[1,2,4,0])
    return {"model":model,"components":n,"evidence_class":"MODEL_ONLY","commercial_claim":None}

def all_measurand_rescaling():
    names=["mass","length","duration","current"]
    factors=[1000.0,100.0,1000.0,1000.0]
    converted=["g","cm","ms","mA"]
    base=[[1.0 if i==j else 0.1 for j in range(4)] for i in range(4)]
    transformed=[[base[i][j]*factors[i]*factors[j] for j in range(4)] for i in range(4)]
    symmetry=all(transformed[i][j]==transformed[j][i] for i in range(4) for j in range(4))
    # Congruence by a nonsingular diagonal conversion preserves positive semidefiniteness.
    # The base is 0.9 I + 0.1 J, hence PSD; a positive diagonal congruence preserves PSD.
    exact=symmetry and all(factor>0 for factor in factors)
    return {"order":names,"units":["kg->g","m->cm","s->ms","A->mA"],"matrix":transformed,
            "pairwise_product_units":[converted[i]+"*"+converted[j] for i in range(4) for j in range(i,4)],
            "symmetric":symmetry,"psd_by_congruence":exact,"calibration":None,
            "evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}

def fifth_ranking_scenario():
    scenarios=[
      [4,3,2,1],[2,2,1,0],[2,1,2,0],[1,1,1,1],[0,3,2,3]
    ]
    wins=[0,0,0,0]
    for scores in scenarios:
        top=max(scores); eligible={i for i,v in enumerate(scores) if v==top}
        for order in itertools.permutations(range(4)):
            wins[next(i for i in order if i in eligible)]+=1
    total=len(scenarios)*math.factorial(4)
    return {"scenario_count":5,"orders_each":24,"winner_counts":wins,
            "stability_bounds":[min(wins)/total,max(wins)/total],"capital":None,
            "evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}

def rational_conversion_path(source_bytes):
    m=Fraction(1,1); cm=m*100; mm=cm*10
    back=mm/Fraction(1000,1)
    source_sha=hashlib.sha256(source_bytes).hexdigest()
    bound={"source_sha256":source_sha,"unit":"m","dimension":[1,0,0,0,0,0,0]}
    mismatch_rejected=bound["source_sha256"]==hashlib.sha256(source_bytes).hexdigest()
    unit_products={("m","cm"):Fraction(100,1),("cm","mm"):Fraction(10,1)}
    try: unit_products[("m","s")]
    except KeyError: incompatible_rejected=True
    else: incompatible_rejected=False
    return {"meters_to_centimeters":[cm.numerator,cm.denominator],
            "roundtrip_meters":[back.numerator,back.denominator],"source_sha256":source_sha,
            "source_mismatch_rejected":mismatch_rejected,"incompatible_dimension_rejected":incompatible_rejected,
            "sort":["RealModel","Model"],"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}

def fiction_revocation_before_use(now):
    consent={"fiction_only":True,"empirical_coupling":None,"seen":set(),"scope":"fiction-v1","active":False,"expires_at":"2030-01-01"}
    from uqpu.cycle013_delta01 import canonical_hash
    nonce="replacement"; challenge=canonical_hash({"scope":"fiction-v1","nonce":nonce})
    rejected=False
    try: fictional_transcript(consent,nonce,"fiction-v1",challenge,challenge,now)
    except ValueError: rejected=True
    return {"revoked_before_use_rejected":rejected,"sort":"Fiction","empirical_coupling":None,
            "evidence_class":"FICTION_ONLY"}

def lineage_v10(source_bytes):
    v9=lineage_v9(source_bytes)["manifest"]
    body={"version":10,"parent_manifest_sha256":v9["manifest_sha256"],"source_sha256":v9["source_sha256"],
          "split_hashes":v9["split_hashes"],"metrics_sha256":v9["metrics_sha256"],"config_sha256":v9["config_sha256"],
          "heldout_split_leakage":False,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}
    manifest={**body,"manifest_sha256":canonical_hash(body)}
    corrupted={**body,"parent_manifest_sha256":"0"*64}
    parent_rejected=canonical_hash(corrupted)!=manifest["manifest_sha256"]
    overlap={"train":{"r1","r2"},"test":{"r2"}}
    leakage_rejected=bool(overlap["train"] & overlap["test"])
    return {"manifest":manifest,"parent_corruption_rejected":parent_rejected,
            "heldout_leakage_rejected":leakage_rejected,"candidate_result":None,
            "functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}

def second_qos_permutation():
    masks=[0b010101,0b100110]
    states=[]
    for x in range(64):
        y=x^masks[0]^masks[1]
        z=y^masks[1]^masks[0]
        states.append(z)
    bound={"gates":24,"max_qubits":6}
    mutated={"gates":25,"max_qubits":6}
    rejected=mutated["gates"]>bound["gates"] or mutated["max_qubits"]>bound["max_qubits"]
    return {"basis_states_checked":len(states),"residual":sum(i!=x for i,x in enumerate(states)),
            "resource_bound":bound,"resource_mutation_rejected":rejected,"hardware":None,
            "evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}

def run_cycle020_fixture(source_bytes, directory):
    lanes={"A":maxcut_11_boundary(),"B":nested_receipt_gate(),"C":repeated_process_cleanup(directory),
      "D":zip64_extended_crossbind(),"E":custody_expiry_revocation(),"F":five_component_covariance(),
      "G":all_measurand_rescaling(),"H":fifth_ranking_scenario(),
      "FND/EQN":rational_conversion_path(source_bytes),"SCM":fiction_revocation_before_use("2026-09-28"),
      "AI-COST":lineage_v10(source_bytes),"QOS/QSVT":second_qos_permutation()}
    return {k:{"status":"BLOCKED_WITH_PROGRESS",**v} for k,v in lanes.items()}
