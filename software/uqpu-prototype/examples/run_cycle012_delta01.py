#!/usr/bin/env python3
"""Generate the bounded Cycle 012 synthetic acceptance artifact."""
import hashlib
import json
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from uqpu.cycle012_delta01 import run_cycle012_fixture  # noqa: E402

REPO=ROOT.parents[1]
OUTPUT=REPO/"benchmarks/results/cycle012-delta01-executable-acceptance.json"
payload=run_cycle012_fixture()
source_paths={
    "preregistered_gates":REPO/"benchmarks/experiments/cycle012-delta01-preregistered-gates.json",
    "module":ROOT/"uqpu/cycle012_delta01.py",
    "tests":ROOT/"tests/test_cycle012_delta01.py",
    "runner":Path(__file__).resolve(),
}
result={
    "schema":"uqpu-cycle012-delta01-executable-acceptance-v1",
    "cycle":"012",
    "evidence_class":"LOCAL_SYNTHETIC_FICTION_ONLY_DECLARATION",
    "lane_count":12,
    "status":"PASS_LOCAL",
    "source_sha256":{name:hashlib.sha256(path.read_bytes()).hexdigest() for name,path in source_paths.items()},
    "lanes":payload,
    "nonclaims":["no QPU or GPU result","no measured material or cost","no physical-law result","SCM is fiction-only; empirical coupling remains null"],
}
result["payload_sha256"]=hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()
OUTPUT.parent.mkdir(parents=True,exist_ok=True)
OUTPUT.write_text(json.dumps(result,indent=2,ensure_ascii=False)+"\n",encoding="utf-8")
print(json.dumps({"artifact":str(OUTPUT),"lane_count":12,"status":"PASS_LOCAL","sha256":hashlib.sha256(OUTPUT.read_bytes()).hexdigest()},indent=2))
