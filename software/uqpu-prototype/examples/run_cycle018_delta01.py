#!/usr/bin/env python3
"""Run the Cycle 018 twelve-lane fixtures and bind the source hashes."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from uqpu.cycle018_delta01 import run_cycle018_fixture  # noqa: E402

REPO = ROOT.parents[1]
OUTPUT = REPO / "benchmarks/results/cycle018-delta01-executable-acceptance.json"
dimension_registry = REPO / "benchmarks/experiments/cycle008-delta01-typed-math-scm-registry.json"
source_paths = {
    "preregistered_gates": REPO / "benchmarks/experiments/cycle018-delta01-preregistered-gates.json",
    "implementation": ROOT / "uqpu/cycle018_delta01.py",
    "tests": ROOT / "tests/test_cycle018_delta01.py",
    "runner": Path(__file__).resolve(),
    "primary_source_review": REPO / "docs/CYCLE_018_PRIMARY_SOURCE_REVIEW_2026-09-28.md",
    "canonical_dimension_registry": dimension_registry,
    "typed_goal_registry": REPO / "benchmarks/experiments/cycle013-delta01-typed-goal-registry.json",
    "scm_fiction_contract": REPO / "docs/SCM_LOKATHIBODI_TYPED_MECHANICS_CYCLE_013_2026-09-28.md",
    "umrl_interface": REPO / "00E_UNIFIED_MATHEMATICAL_LANGUAGE_AND_DISCOVERY_LEDGER.md",
}
payload = run_cycle018_fixture(source_paths["umrl_interface"].read_bytes())
result = {
    "schema": "uqpu-cycle018-delta01-executable-acceptance-v1",
    "cycle": "018",
    "status": "PASS_LOCAL",
    "lane_count": 12,
    "evidence_class": "LOCAL_SOFTWARE_SYNTHETIC_MODEL_AND_FICTION_ONLY",
    "source_sha256": {name: hashlib.sha256(path.read_bytes()).hexdigest() for name, path in source_paths.items()},
    "source_evidence": [
        {"title": "PKWARE APPNOTE v6.3.10 FINAL", "url": "https://pkware.cachefly.net/webdocs/casestudies/APPNOTE.TXT",
         "revision_date": "2022-11-01", "sections": ["4.3.7", "4.3.9", "4.3.12"], "accessed": "2026-09-28",
         "use": "ZIP64 local/central/descriptor gate", "evidence_class": "PRIMARY_FORMAT_SPECIFICATION"},
        {"title": "Python os.replace documentation", "url": "https://docs.python.org/3/library/os.html#os.replace",
         "accessed": "2026-09-28", "use": "filesystem replacement limits", "evidence_class": "PRIMARY_RUNTIME_DOCUMENTATION"},
    ],
    "lanes": payload,
    "uncertainty": ["local process/filesystem only", "no independent ZIP producer corpus", "finite cost/ranking scenarios are not probability distributions", "custody/receipt/AI/QOS records are synthetic"],
    "nonclaims": ["no QPU/GPU performance, advantage or replacement", "no provider authorization/execution/billing or commercial result",
                  "no crash/power-loss durability, physical sample, calibration or new physical law", "no AI equivalence, capital claim or empirical SCM communication"],
}
result["payload_sha256"] = hashlib.sha256(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False, allow_nan=False).encode("utf-8")).hexdigest()
OUTPUT.parent.mkdir(parents=True, exist_ok=True)
OUTPUT.write_text(json.dumps(result, indent=2, ensure_ascii=False, allow_nan=False) + "\n", encoding="utf-8")
print(json.dumps({"artifact": str(OUTPUT), "lanes": result["lane_count"], "status": result["status"],
                  "sha256": hashlib.sha256(OUTPUT.read_bytes()).hexdigest(), "payload_sha256": result["payload_sha256"]}, indent=2))
