# Batch 136 — provenance-parser integrity guard and AI-science strategy watch

**Date:** 2026-10-30  
**Starting canonical main SHA:** `7603db37e2e907e7d549a54916b129c7b093446f`  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — evidence, reproducibility and economics  
**Publication/strategic owner:** Lane H  
**Cross-lane interfaces:** B provider portability; C state/data semantics; D/G device and manufacturing; E materials/bio-oil/fusion; INV-034/035 across A–H  
**Evidence class:** SOFTWARE TEST GUARD + OFFICIAL GOVERNMENT STRATEGY REPORT / NO ALGORITHM REPRODUCTION

## 1. Canonical start and invariants

The current `main` head was resolved from GitHub at `7603db37e2e907e7d549a54916b129c7b093446f` (2026-10-29, “Add sparse state-preparation asset provenance preflight”). The cycle read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the permanent root directives 00/00A/01–06, Batch 135/134/133/132, the current sparse-state-preparation asset manifest/test/gap, RESEARCH_GAPS.md, and the A–H scoreboard.

The canonical architecture remains A–H with Lane A at Priority #1, D/G co-design, the shared integration hub, one primary owner per artifact and a maximum of 16 directory levels. The Thai, English, Chinese, Japanese, Korean and German strategic-plan links and recorded AI-agent/funding context remain preserved. INV-025/026/027 and INV-029–035 remain binding.

The combined-status endpoint returned an empty status list for the starting SHA, so this cycle does not infer green CI from an absent status. Exact-head Actions checks must be observed after the proposed change.

## 2. Lane A — harden JSON provenance parsing

The existing `SPARSE_STATEPREP_TOFFOLI_ASSET_PROVENANCE_V1.json` manifest is source-metadata-only and explicitly records that the archive was not downloaded, its publisher MD5 was not recomputed, SHA-256 is absent, dependencies were not audited and the upstream algorithm was not reproduced. The associated test parsed it with ordinary `json.loads`, which silently accepts duplicate object keys and keeps the last value. That is an avoidable provenance ambiguity even though the current manifest contains no duplicate keys.

Added a test-only `object_pairs_hook` that rejects duplicate JSON keys at every nesting level, plus a synthetic regression test proving that conflicting repeated fields such as `evidence_class` raise a `ValueError`. The manifest itself is unchanged; no source-asset, algorithm or theorem status is promoted.

**Verification boundary:** the source change is committed to the research branch for CI validation. No local full-suite execution is claimed in this report. A passing guard would establish parser behavior only, not upstream asset integrity or algorithm correctness.

## 3. Fresh literature surveillance

Searches covered symbolic/neural-symbolic equation discovery, AI theorem/proof discovery, physics-informed modeling, automated experiment design, new bounds/no-go results, sparse state preparation, biomass conversion, fusion and R&D finance.

- The peer-reviewed Rupprecht–Wölk sparse-isometry/Toffoli result (Quantum, published 2026-09-10; DOI 10.22331/q-2026-09-10-2208), Luo–Li sparse-state T-count preprint (arXiv:2608.00414), ProofEvolve (arXiv:2608.26334), PiT-PO (arXiv:2602.10576), SymbolFit (arXiv:2607.19750) and the CoSR publication-status conflict are already indexed in existing project watches/gaps. No duplicate article was created for them.
- New-to-repository source: DOE Office of Science Advisory Committee, “Genesis Mission Frameworks: Advancing the Frontiers of American Discovery,” published 2026-09-25. The official summary discusses integrated AI/HPC/quantum/experimental-facility infrastructure, AI-assisted fusion engineering, critical-magnet material search/recycling and bioeconomy ambitions. A dated source-specific watch was added at [the literature-watch article](literature_watch/2026-10-30-doe-genesis-ai-accelerated-science.md).
- **Evidence class and limitation:** official advisory/strategy report, not a peer-reviewed experiment or measured cost model. Its pilot-plant and AI-enabled outcomes are ambitions, not evidence that fusion electricity, accepted fuel, material substitution or economic savings have been delivered.

## 4. A–H status

| Lane | This cycle | Evidence boundary / next gate |
|---|---|---|
| **A — quantum programming/workloads/compiler/runtime** | Added duplicate-key rejection to the sparse-state asset-provenance regression test. | Run exact-head CI; later retrieve/hash the exact archive and independently reproduce small circuits. No algorithm reproduction yet. |
| **B — cloud/QPU/provider integration** | Provider-neutral boundary retained; no target or job changed. | Continue simulator/dry-run first; no paid QPU execution without credentials, bounded budget and explicit consent. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Provenance JSON parsing is made unambiguous; state dimension, classical description bytes, transfer and reconstruction remain distinct. | Measure bytes/I/O and output reconstruction separately from qubit count or Hilbert-space dimension. |
| **D — devices/chip/process/fabrication/packaging** | No device or fabrication result. | Map only independently reproduced logical resources into depth, routing, ancilla, QEC, reliability and packaging requirements. |
| **E — biomass/materials/bio-oil/fusion/cooling/infrastructure** | Added a strategy-level DOE AI-science watch; no BIO-001, INV-030 or FUS-001 result. | Convert any adopted proposal into feedstock/material/net-electric measurable contracts and independently validated cost drivers. |
| **F — economics/benchmarks/evidence/integration** | Parser ambiguity is now an explicit test failure; evidence class remains source metadata only. | Keep model values separate from accepted-task cost, commercial fuel, net electricity and financing evidence. |
| **G — manufacturing equipment/software/factory systems** | D/G co-design remains active; DOE material-search/recycling ideas are strategic leads only. | Require device specifications, process windows, yield, lifetime and cost-per-good-device evidence. |
| **H — strategic plan/finance/publication** | Added the dated DOE source watch; preserved the multilingual master-plan links and AI-agent/funding references. | Translate strategy into milestone, funding and time-to-evidence hypotheses; do not treat a roadmap as technical or financing proof. |

## 5. Foundational and equation-discovery path

- **FND-001:** no new thermodynamic-gap measurement; Landauer/energy-time bounds remain conditional on their stated operations and assumptions.
- **FND-002:** no new output-information lower bound; classical output requirements remain explicit.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** no alternative physical primitive passes a discriminating test.
- **FND-005:** no new QFT/particle mechanism or device consequence.
- **FND-006:** the parser guard improves reproducibility metadata; AI theorem/equation candidates remain subject to formal checking, held-out families and counterexample search.
- **EQN-001–EQN-006:** no new candidate equation is promoted. The required chain remains generator → explicit constraints → evaluator → held-out/generalization → counterexample → proof/simulation → discriminating experiment → independent replication → device/system consequence → economics.

## 6. INV-029 through INV-035 and moonshot boundaries

- **INV-029:** no service-capability, energy, physical-compression or lifecycle-cost contract passed; remote infrastructure cannot be hidden behind a phone terminal.
- **INV-030:** no Pangola-carbon functional substitution, recovery or critical-material reduction measured; no transmutation claim.
- **INV-031:** no accepted Pangola-derived liquid fuel or target-cost commercial result.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no lower financed principal, absolute interest, project WACC or economy-wide rate measured. Principal/duration effects remain separate from rate effects.
- **INV-034:** broad foundational search remains active; current physical limits stay binding.
- **INV-035:** provenance and falsifiability remain mandatory; no AI-generated equation is a physical law by declaration.

INV-025/026/027 remain falsifiable, subsystem-specific and evidence-gated. The 100×/100,000,000× goals remain targets. Quantum state dimension is not readable classical storage, and NPU equivalence requires real neural-workload semantics and quality.

## 7. Integration and next gate

This batch is linked from the root README and the A–H integration hub. The lane A test, literature watch, integration report and machine-readable integration record share stable work ID `QA-PROV-DUPKEY-001`. The strategic master-plan files and six-language source links are not edited.

**Next highest-value gate:** obtain exact-head GitHub Actions results for the duplicate-key guard; repair any feasible failure. In Lane A, continue the controlled archive retrieval/hash/dependency-audit/independent-small-instance gate. In parallel, convert the DOE report's AI-for-fusion/material/bioeconomy priorities into testable proposals only when concrete datasets, baselines and engineering metrics are available.

No paid QPU job was submitted. No real-QPU, material, fuel, fusion, financing, new-physics or mission-level advantage is claimed.

Research-Sync: main
