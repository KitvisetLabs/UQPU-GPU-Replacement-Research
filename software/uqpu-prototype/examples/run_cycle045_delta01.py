"""Generate the source-bound Cycle 045 executable acceptance artifact."""
from __future__ import annotations
import hashlib,json,os,re,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];PROTOTYPE=ROOT/"software"/"uqpu-prototype";sys.path.insert(0,str(PROTOTYPE))
from uqpu.cycle045_delta01 import run_cycle045_fixture  # noqa: E402
MODULE=PROTOTYPE/"uqpu"/"cycle045_delta01.py";TESTS=PROTOTYPE/"tests"/"test_cycle045_delta01.py";OUTPUT=ROOT/"benchmarks"/"results"/"cycle045-delta01-executable-acceptance.json"
def file_sha256(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
    environment=dict(os.environ);environment["PYTHONPATH"]=str(PROTOTYPE)+os.pathsep+environment.get("PYTHONPATH","")
    test_run=subprocess.run([sys.executable,"-m","unittest","discover","-s",str(PROTOTYPE/"tests"),"-p","test_cycle045_delta01.py","-v"],cwd=ROOT,env=environment,text=True,capture_output=True)
    if test_run.returncode:raise SystemExit(test_run.stdout+test_run.stderr)
    summary=re.search(r"Ran (\d+) tests?",test_run.stdout+test_run.stderr)
    if not summary:raise RuntimeError("unittest summary unavailable")
    compile_run=subprocess.run([sys.executable,"-m","py_compile",str(MODULE),str(TESTS),str(Path(__file__))],cwd=ROOT,env=environment,text=True,capture_output=True)
    if compile_run.returncode:raise SystemExit(compile_run.stdout+compile_run.stderr)
    source=b"Cycle 045 quotient, lineage-seal, five-recovery and five-leaf multiproof source\n"
    with tempfile.TemporaryDirectory() as root:lanes=run_cycle045_fixture(source,root)
    artifact={"schema":"uqpu-cycle045-delta01-executable-acceptance-v1","cycle":"045","status":"PASS_LOCAL_FIXTURES_EXTERNAL_GATES_OPEN","lane_count":len(lanes),"branch":"research/cycle-045-delta-01-2026-10-01","base_cycle044_closeout_sha":"c15c80390b432da5f10af0fa3c509e2891a01cbb","preregistration_commit_sha":"b4e6a76a7b73e4496a34bc74e7d8c5cee2ff5646","implementation_commit_sha":"8dcec1cf8d1554c2fe0d5f0ed68f4c0374229830","focused_tests_commit_sha":"c7cd3fc3aef7b6ee3e18edb11d787793f8c8db88",
      "source_identity":{"preregistered_gates_git_blob_sha":"449956bffe41076f3de5bff694dcd9d50d0402dc","portfolio_git_blob_sha":"27a8da9b68c6e896c67b38e9e6a49525c181dc73","implementation_git_blob_sha":"0024a6c4d24f96fea0d88001402611c037e852e5","focused_tests_git_blob_sha":"d5c20a14672b1cb0575abf6fed4d89ad281739e3","implementation_sha256":file_sha256(MODULE),"focused_tests_sha256":file_sha256(TESTS),"runner_sha256":file_sha256(Path(__file__)),"typed_source_sha256":hashlib.sha256(source).hexdigest()},
      "lanes":lanes,"validation":{"focused_tests_passed":int(summary.group(1)),"focused_tests_failed":0,"py_compile":"PASS","acceptance_runner":"PASS"},
      "source_evidence":[{"title":"PKWARE APPNOTE v6.3.10 FINAL","url":"https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT","source_date":"2022-11-01","access_date":"2026-10-01","evidence_class":"PRIMARY_FORMAT_SPECIFICATION"},{"title":"Python os.replace documentation","url":"https://docs.python.org/3/library/os.html#os.replace","access_date":"2026-10-01","evidence_class":"PRIMARY_RUNTIME_DOCUMENTATION"},{"title":"Python os.fsync documentation","url":"https://docs.python.org/3/library/os.html#os.fsync","access_date":"2026-10-01","evidence_class":"PRIMARY_RUNTIME_DOCUMENTATION"}],
      "assumptions":["All inputs are bounded fixtures or models.","Injected five-journal recovery does not establish crash or power-loss durability.","Custody hashes are synthetic, not signatures.","SCM records are fiction-only."],"uncertainty":["Provider, hardware, durability, interoperability, custody, calibration, decision, lineage and equivalence gates remain open."],"nonclaims":["No measured QPU/GPU performance, scaling or quantum advantage.","No provider execution, invoice, commercial economics or capital result.","No crash durability, signature claim, calibration, physical sample, new physical law, AI equivalence or empirical SCM result."]}
    unsigned=json.dumps(artifact,sort_keys=True,separators=(",",":"),allow_nan=False).encode();artifact["payload_sha256"]=hashlib.sha256(unsigned).hexdigest();OUTPUT.parent.mkdir(parents=True,exist_ok=True);OUTPUT.write_text(json.dumps(artifact,indent=2,sort_keys=True,allow_nan=False)+"\n",encoding="utf-8")
    print(json.dumps({"lanes":len(lanes),"focused_tests_passed":int(summary.group(1)),"payload_sha256":artifact["payload_sha256"],"output_sha256":file_sha256(OUTPUT)},sort_keys=True))
if __name__=="__main__":main()
