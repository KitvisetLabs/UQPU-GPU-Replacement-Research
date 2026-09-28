#!/usr/bin/env python3
"""Run Cycle 022 twelve-lane fixtures and bind the reviewed source hashes."""
import hashlib
import json
import tempfile
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from uqpu.cycle022_delta01 import run_cycle022_fixture  # noqa: E402

REPO=ROOT.parents[1]
OUTPUT=REPO/"benchmarks/results/cycle022-delta01-executable-acceptance.json"
source_paths={
 "preregistered_gates":REPO/"benchmarks/experiments/cycle022-delta01-preregistered-gates.json",
 "implementation":ROOT/"uqpu/cycle022_delta01.py",
 "tests":ROOT/"tests/test_cycle022_delta01.py",
 "runner":Path(__file__).resolve(),
 "primary_source_review":REPO/"docs/CYCLE_022_PRIMARY_SOURCE_REVIEW_2026-09-28.md",
 "shared_zip_parser":ROOT/"uqpu/cycle016_delta01.py",
 "umrl_interface":REPO/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
}
with tempfile.TemporaryDirectory() as temp:
 payload=run_cycle022_fixture(source_paths["umrl_interface"].read_bytes(),temp)
result={
 "schema":"uqpu-cycle022-delta01-executable-acceptance-v1","cycle":"022","status":"PASS_LOCAL",
 "lane_count":len(payload),"evidence_class":"LOCAL_SOFTWARE_SYNTHETIC_MODEL_AND_FICTION_ONLY",
 "source_sha256":{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in source_paths.items()},
 "source_evidence":[
  {"title":"PKWARE APPNOTE v6.3.10 FINAL","url":"https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
   "revision_date":"2022-11-01","sections":["4.3.7","4.3.9","4.3.12"],"accessed":"2026-09-28","evidence_class":"PRIMARY_FORMAT_SPECIFICATION"},
  {"title":"Python os.replace documentation","url":"https://docs.python.org/3/library/os.html#os.replace",
   "accessed":"2026-09-28","evidence_class":"PRIMARY_RUNTIME_DOCUMENTATION"}],
 "lanes":payload,
 "uncertainty":["local process/file-system observations only","synthetic ZIP64 records","finite model/ranking grids",
  "fiction-only consent and synthetic lineage"],
 "nonclaims":["no measured QPU/GPU performance or advantage","no provider authority, invoice, commercial or capital result",
  "no crash durability, calibration, physical sample, new law, AI equivalence or empirical SCM evidence"],
}
result["payload_sha256"]=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False,allow_nan=False).encode()).hexdigest()
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
OUTPUT.write_text(json.dumps(result,indent=2,ensure_ascii=False,allow_nan=False)+"\n",encoding="utf-8")
print(json.dumps({"artifact":str(OUTPUT),"lanes":result["lane_count"],"status":result["status"],
 "sha256":hashlib.sha256(OUTPUT.read_bytes()).hexdigest(),"payload_sha256":result["payload_sha256"]},indent=2))
