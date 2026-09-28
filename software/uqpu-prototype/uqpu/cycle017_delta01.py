"""Cycle 017 adversarial cross-lane fixture extensions; no external claims."""
import hashlib
import hmac
import json
import struct
from fractions import Fraction

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import ai_lineage_manifest, run_cycle014_fixture
from uqpu.cycle015_delta01 import rational_interval_composition
from uqpu.cycle016_delta01 import (
    ai_lineage_manifest_v6, component_covariance_sweep, correlation_ranking_grid,
    exact_maxcut_10_node, rational_interval_divide, same_filesystem_concurrent_replace,
    scm_nonce_scope_matrix, typed_covariance_block, zip64_central_entry_gate,
    qos_er6_reconstruction_v5, verify_custody_chain, make_custody_event,
)

LANES=("A","B","C","D","E","F","G","H","FND/EQN","SCM","AI-COST","QOS/QSVT")


def maxcut_weight_perturbation_family(graphs):
    if len(graphs) < 2:
        raise ValueError("need baseline and perturbation")
    rows=[exact_maxcut_10_node(graph) for graph in graphs]
    if len({row["state_count"] for row in rows}) != 1:
        raise AssertionError("state count")
    return {"rows":rows,"same_task":len({r["task_sha256"] for r in rows})==1,"scaling_claim":None,
            "evidence_class":"LOCAL_EXACT_CLASSICAL_FIXTURE"}


def receipt_v4_fixture(request_sha, key_id, key, invoice=None):
    if key_id is None or key is None:
        return {"receipt":None,"provider_claim":None,"status":"NULL_MISSING_KEY"}
    if invoice is not None:
        raise ValueError("unexecuted receipt invoice must be null")
    body={"schema":"receipt-v4","request_sha256":request_sha,"provider_status":"NOT_EXECUTED",
          "authorization_scope":"fixture-only","authorized":False,"key_id":key_id,"job_id":None,"invoice":None}
    raw=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    signature=hmac.new(key,raw,hashlib.sha256).hexdigest()
    return {"receipt":{**body,"signature_algorithm":"HMAC-SHA256-FIXTURE","signature":signature},
            "canonical_bytes_sha256":hashlib.sha256(raw).hexdigest(),"provider_claim":None,
            "evidence_class":"SYNTHETIC_RECEIPT_AUTHENTICATION"}


def verify_receipt_v4_fixture(result,request_sha,key_id,key,revoked_keys=()):
    receipt=result.get("receipt") if isinstance(result,dict) else None
    if not receipt or key_id in set(revoked_keys) or receipt.get("key_id")!=key_id or receipt.get("request_sha256")!=request_sha:
        return False
    body={k:receipt[k] for k in ("schema","request_sha256","provider_status","authorization_scope","authorized","key_id","job_id","invoice")}
    raw=json.dumps(body,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode("utf-8")
    expected=hmac.new(key,raw,hashlib.sha256).hexdigest()
    return hmac.compare_digest(expected,receipt.get("signature","")) and receipt.get("provider_status")=="NOT_EXECUTED" and receipt.get("invoice") is None and result.get("provider_claim") is None


def safe_same_device_replace(directory,target,payloads):
    from pathlib import Path
    if not isinstance(target,str) or not target or Path(target).name!=target or target in (".",".."):
        raise ValueError("target collision/path traversal")
    return same_filesystem_concurrent_replace(directory,target,payloads)


def _central_record(name=b"sample.bin"):
    extra_payload=struct.pack("<QQQI",8,8,64,1)
    extra=struct.pack("<HH",1,len(extra_payload))+extra_payload
    fields=(b"PK\x01\x02",45,45,8,0,0,0,0x12345678,0xffffffff,0xffffffff,len(name),len(extra),0,0xffff,0,0,0xffffffff)
    return struct.pack("<4sHHHHHHIIIHHHHHII",*fields)+name+extra


def zip64_local_central_crossbind(local_header,central,descriptor,disk_sizes):
    if not isinstance(local_header,bytes) or len(local_header)<30:
        raise ValueError("local header")
    sig,needed,flags,method,mtime,mdate,crc,comp,uncomp,name_len,extra_len=struct.unpack_from("<4s5H3I2H",local_header)
    if sig!=b"PK\x03\x04" or len(local_header)!=30+name_len+extra_len:
        raise ValueError("local header length/signature")
    name=local_header[30:30+name_len]
    _,_,_,cflags,cmethod,_,_,ccrc,_,_,cname_len,cextra_len,comment_len,disk,internal,external,offset=struct.unpack_from("<4sHHHHHHIIIHHHHHII",central)
    central_name=central[46:46+cname_len]
    parsed=zip64_central_entry_gate(central,descriptor,disk_sizes)
    if name!=central_name or flags!=cflags or method!=cmethod or not (flags & 0x0008) or len(name)!=name_len:
        raise ValueError("local/central identity mismatch")
    return {"central":parsed,"local_central_match":True,"data_descriptor_flag":True,"payload_read":False,
            "evidence_class":"SYNTHETIC_ZIP64_CROSS_BIND"}


def custody_truncation_duplicate_suite(now):
    sample=hashlib.sha256(b"cycle017-fictional-sample").hexdigest(); prev="0"*64; events=[]
    for seq,(issuer,scope) in enumerate((("i1","intake"),("i2","storage"),("i3","transfer"))):
        e=make_custody_event(seq,sample,"fiction-path",issuer,scope,"2026-01-01","2027-01-01",prev);events.append(e);prev=e["event_sha256"]
    issuers={"i1":{"intake"},"i2":{"storage"},"i3":{"transfer"}}
    expected_head=events[-1]["event_sha256"]
    def verify_complete(rows):
        chain=verify_custody_chain(rows,issuers,now)
        if len(rows)!=3 or chain["final_event_sha256"]!=expected_head:
            raise ValueError("custody completion receipt")
        return chain
    valid=verify_complete(events)
    truncated=False;duplicate=False
    try: verify_complete(events[:2])
    except ValueError: truncated=True
    dup=[dict(x) for x in events];dup[2]["sequence"]=1
    try: verify_complete(dup)
    except ValueError: duplicate=True
    return {"valid_events":valid["event_count"],"truncated_chain_rejected":truncated,"duplicate_sequence_rejected":duplicate,
            "physical_sample_claim":None,"evidence_class":"SYNTHETIC_CUSTODY_NEGATIVE_CONTROL"}


def shared_covariance_grid():
    return component_covariance_sweep([[1,2],[2,3]],
      {"independent":[[.25,0],[0,.25]],"shared":[[.25,.25],[.25,.25]],"invalid":[[1,2],[2,1]]},[1,2,4,0])


def three_measurand_covariance():
    dims={"m":[1,0,0,0,0,0,0],"s":[0,0,1,0,0,0,0],"kg":[0,1,0,0,0,0,0]}
    units=["m","s","kg"];ids=["length","duration","mass"]
    ms=[{"id":i,"unit":u,"dimension":dims[u]} for i,u in zip(ids,units)]
    entries=[]
    for i,ui in enumerate(units):
        row=[]
        for j,uj in enumerate(units):
            unit="*".join(sorted((ui,uj)));d=[a+b for a,b in zip(dims[ui],dims[uj])]
            row.append({"value":1.0 if i==j else 0.0,"unit":unit,"dimension":d})
        entries.append(row)
    return typed_covariance_block(ms,entries)


def adverse_ranking_grid():
    base=["compute","memory","energy","latency"]
    return correlation_ranking_grid(base,[
      {"name":"center","correlation":[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]],"scenario_orders":[base,["memory","compute","energy","latency"],["compute","energy","memory","latency"]],"assumption":"baseline and two adjacent swaps"},
      {"name":"adverse","correlation":[[1,.8,0,0],[.8,1,0,0],[0,0,1,.4],[0,0,.4,1]],"scenario_orders":[["latency","energy","memory","compute"],["energy","latency","compute","memory"],["memory","energy","latency","compute"]],"assumption":"predeclared adverse order set"}])


def exact_divide_then_multiply(source_bytes):
    sha=hashlib.sha256(source_bytes).hexdigest();base={"domain_sort":"RealModel","evidence_sort":"Model","source_sha256":sha}
    left={**base,"unit":"m","dimension":[1,0,0,0,0,0,0],"lower":[2,1],"upper":[4,1]}
    right={**base,"unit":"s","dimension":[0,0,1,0,0,0,0],"lower":[2,1],"upper":[4,1]}
    ratio=rational_interval_divide(left,right,source_bytes,{"m|s":{"unit":"m/s","dimension":[1,0,-1,0,0,0,0]}})["result"]
    seconds={**base,"unit":"s","dimension":[0,0,1,0,0,0,0],"lower":[2,1],"upper":[3,1]}
    product=rational_interval_composition(ratio,seconds,"multiply",source_bytes,{"m/s|s":{"unit":"m","dimension":[1,0,0,0,0,0,0]}})
    return {"ratio":ratio,"composed_length":product,"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}


def ai_lineage_v7(source_bytes):
    splits={"train":["t1"],"validation":["v1"],"test":["x1"]};metrics={"train":{"loss":1.0},"validation":{"loss":1.1},"test":{"loss":1.2}};cfg={"seed":7}
    v4=ai_lineage_manifest(b"v4",splits,metrics,cfg)
    v5body={"version":5,"parent_manifest_sha256":v4["manifest_sha256"],"source_sha256":v4["source_sha256"],"split_hashes":v4["split_hashes"],"metrics_sha256":v4["metrics_sha256"],"config_sha256":v4["config_sha256"],"evidence_class":"SYNTHETIC_DATA_LINEAGE","functional_equivalence":None}
    v5={**v5body,"manifest_sha256":canonical_hash(v5body)}
    v6=ai_lineage_manifest_v6(v5,b"v6",splits,metrics,cfg)["manifest"]
    fresh=ai_lineage_manifest(b"v7",splits,metrics,cfg)
    body={"version":7,"parent_manifest_sha256":v6["manifest_sha256"],"source_sha256":fresh["source_sha256"],"split_hashes":fresh["split_hashes"],"metrics_sha256":fresh["metrics_sha256"],"config_sha256":fresh["config_sha256"],"evidence_class":"SYNTHETIC_DATA_LINEAGE","functional_equivalence":None}
    manifest={**body,"manifest_sha256":canonical_hash(body)}
    return {"manifest":manifest,"candidate_result":None,"equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def second_qos_operator():
    parent=run_cycle014_fixture()["QOS/QSVT"]
    gates=[{"op":"cx","control":0,"target":2},{"op":"x","target":4},{"op":"cx","control":2,"target":5}]
    return qos_er6_reconstruction_v5(parent,gates)


def run_cycle017_fixture(source_bytes):
    base=[[0,1,4],[0,3,7],[0,6,2],[1,2,5],[1,5,3],[2,3,6],[2,7,4],[3,4,8],[4,5,2],[4,8,5],[5,6,7],[6,7,3],[7,8,6],[8,9,4],[2,9,1]]
    perturbed=[row[:] for row in base];perturbed[0][2]+=1;perturbed[4][2]+=2
    a=maxcut_weight_perturbation_family([base,perturbed])
    key=b"cycle017 fixture key";request=canonical_hash({"cycle":17,"kind":"fixture"});receipt=receipt_v4_fixture(request,"key-rotate-a",key)
    b={**receipt,"verified":verify_receipt_v4_fixture(receipt,request,"key-rotate-a",key),"revoked_rejected":not verify_receipt_v4_fixture(receipt,request,"key-rotate-a",key,["key-rotate-a"])}
    import tempfile
    with tempfile.TemporaryDirectory(prefix="uqpu-cycle017-") as d:c=safe_same_device_replace(d,"state.bin",[b"a-complete",b"b-complete",b"c-complete"])
    name=b"sample.bin";extra_payload=struct.pack("<QQQI",8,8,64,1);extra=struct.pack("<HH",1,len(extra_payload))+extra_payload
    args=(b"PK\x01\x02",45,45,8,0,0,0,0x12345678,0xffffffff,0xffffffff,len(name),len(extra),0,0xffff,0,0,0xffffffff)
    central=struct.pack("<4sHHHHHHIIIHHHHHII",*args)+name+extra
    local=struct.pack("<4s5H3I2H",b"PK\x03\x04",45,8,0,0,0,0,0,0,len(name),0)+name
    descriptor=struct.pack("<4sIQQ",b"PK\x07\x08",0x12345678,8,8)
    dmeta=zip64_local_central_crossbind(local,central,descriptor,[128,256])
    e=custody_truncation_duplicate_suite("2026-09-28");f=shared_covariance_grid();g=three_measurand_covariance();h=adverse_ranking_grid()
    fn=exact_divide_then_multiply(source_bytes);scm=scm_nonce_scope_matrix("2026-09-28");ai=ai_lineage_v7(source_bytes);qos=second_qos_operator()
    return {"A":a,"B":b,"C":c,"D":dmeta,"E":e,"F":f,"G":g,"H":h,"FND/EQN":fn,"SCM":scm,"AI-COST":ai,"QOS/QSVT":qos}
