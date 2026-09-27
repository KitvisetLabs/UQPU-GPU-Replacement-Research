"""SCM replication manifest binds validated transcript hashes to independent runs."""
from dataclasses import dataclass

@dataclass(frozen=True)
class ReplicationRecord:
    site_id:str; operator_id:str; hardware_id:str; calibration_id:str
    protocol_version:str; transcript_sha256:str; raw_data_sha256:str
    evidence_class:str="REPLICATION_PROVENANCE_ONLY"

def validate_replication(records):
    e=[]
    seen=set()
    for i,r in enumerate(records):
        for n in ("site_id","operator_id","hardware_id","calibration_id","protocol_version","transcript_sha256","raw_data_sha256"):
            if not getattr(r,n).strip():e.append(f"{i}:missing:{n}")
        if r.site_id in seen:e.append(f"{i}:duplicate_site:{r.site_id}")
        seen.add(r.site_id)
        for n in ("transcript_sha256","raw_data_sha256"):
            v=getattr(r,n)
            if v and (len(v)!=64 or any(c not in "0123456789abcdef" for c in v.lower())):
                e.append(f"{i}:invalid_sha256:{n}")
    return tuple(e)
