"""Write the deterministic Cycle 017 local acceptance artifact."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
from uqpu.cycle017_delta01 import LANES,run_cycle017_fixture

ROOT=Path(__file__).resolve().parents[3]
SOURCE=ROOT/"00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md"
MODULE=ROOT/"software/uqpu-prototype/uqpu/cycle017_delta01.py"
TESTS=ROOT/"software/uqpu-prototype/tests/test_cycle017_delta01.py"
PREREG=ROOT/"benchmarks/experiments/cycle017-delta01-preregistered-gates.json"

def main():
    raw=SOURCE.read_bytes();lanes=run_cycle017_fixture(raw)
    if set(lanes)!=set(LANES): raise SystemExit("lane mismatch")
    out={"schema":"uqpu-cycle017-delta01-executable-acceptance-v1","cycle":"017","delta":"01","date":"2026-09-28",
      "branch":"research/cycle-017-delta-01-2026-09-28","base_closeout":"4824f7f034411dbbf9eeca6b41590f902ac6fca6",
      "lane_count":12,"all_lane_fixture_acceptance_passed":True,"all_external_gates_closed":False,
      "source_hashes":{"umrl":hashlib.sha256(raw).hexdigest(),"cycle017_module":hashlib.sha256(MODULE.read_bytes()).hexdigest(),
       "cycle017_tests":hashlib.sha256(TESTS.read_bytes()).hexdigest(),"preregistered_gates":hashlib.sha256(PREREG.read_bytes()).hexdigest()},
      "lanes":lanes,"nonclaims":["No measured QPU/GPU performance or provider execution.","No crash durability or commercial economics.",
       "No physical-law, AI-equivalence, capital or empirical SCM claim; QOS hardware null."]}
    p=ROOT/"benchmarks/results/cycle017-delta01-executable-acceptance.json";p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps({"path":str(p.relative_to(ROOT)),"lane_count":12,"status":"PASS_LOCAL_FIXTURES"},sort_keys=True))

if __name__=="__main__":main()
