# Batch 101 — predictive-interval scoring and synthetic controls

**Date:** 2026-10-28  
**Starting main SHA:** f3ca3c12b20b4fa28adfb276ae5804427f9ca2a8  
**Primary owner:** Lane A — workload/equation-discovery metrics  
**Cross-lane owners:** Lane F — evidence and resource acceptance; Lane H — source provenance/publication  
**Cross-cutting:** INV-029–035; INV-025/026/027; FND-001–006; EQN-001–008; BIO-001; FUS-001; FIN-001  
**Evidence class:** SOFTWARE_IMPLEMENTATION + SYNTHETIC_UNIT_FIXTURES  
**Execution boundary:** no real HEP data, no matched research benchmark, no real QPU, no paid job, no physical experiment

## 1. Starting-state audit

The cycle began from the latest observed main head, f3ca3c12b20b4fa28adfb276ae5804427f9ca2a8, rather than a fixed batch number. It inspected PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the eight high-visibility root directives, the current Batch 100 and equation-discovery gaps, the matched-comparison implementation/tests, recent A–H integration records, RESEARCH_GAPS.md, WORKLOG.md, the cold-start manifest and exact-head Actions.

On the starting SHA, UQPU Prototype and Project Invariants run #1945 passed and Autonomous Cold-Start Handoff Audit #1204 passed. Those results apply to the starting SHA only; this new commit must receive its own exact-head Actions. The project has no authorization for a paid QPU job.

The canonical operational map remains A–H. The legacy field-agnostic vehicle/levitation material remains preserved as a supplemental workstream, not a ninth permanent lane. The root directives 00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md, 00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md and 01–06 remain present. Thai, English, Chinese, Japanese, Korean and German master-plan links and strategic AI-agent/funding references remain preserved.

## 2. Fresh literature surveillance

Fresh public searches covered symbolic/neural-symbolic equation discovery, formal mathematical proof search, physics-informed neural operators, quantum-speed-limit/thermodynamic work, active experiment design, and lower-bound/no-go literature. Relevant surfaced sources already have repository watches or gap records, including:

- SymbolFit, arXiv:2607.19750, with v2 revised 2026-10-19: uncertainty-aware parametric fits to binned HEP spectra.
- PiT-PO, arXiv:2602.10576, version listed 2026-07-27: adaptive physics-informed equation generation.
- MPNO, arXiv:2608.25744, submitted 2026-08-26: a candidate stability-by-construction neural-operator architecture.
- Tsoukalas et al., Science, published 2026-10-08, DOI 10.1126/science.aej2213: formal proof search with Lean-based verification.
- Published quantum-speed-limit and thermodynamic-bound work already indexed under FND-003.

No materially new-to-repository source was identified in this surveillance pass. No duplicate literature article was created. Third-party results remain external evidence and are not UQPU reproduction, physical-law evidence or technology advantage.

## 3. Implementation

Added software/uqpu-prototype/uqpu/predictive_interval_metrics.py with one narrow responsibility: score supplied held-out central prediction intervals at a single preregistered nominal coverage level.

The result reports sample count, nominal coverage, empirical coverage, coverage error, mean interval width and mean interval score. The central interval score is width plus (2/alpha) times distance outside the interval, where alpha = 1 - nominal coverage. Lower interval score is better at a fixed nominal level. Inputs fail closed for empty/mismatched sequences, non-finite values, booleans/non-numeric values, invalid coverage levels, inverted bounds and non-finite derived metrics.

Added software/uqpu-prototype/tests/test_predictive_interval_metrics.py with deterministic fixtures for:
- a known-function positive control, y = 2x + 1, checking exact interval coverage/width/score;
- a null/no-signal interval fixture with one outlier, checking coverage and the proper interval-score penalty;
- a same-coverage comparison showing that uninformatively wide intervals score worse;
- invalid input and numeric-range rejection.

The fixture outcomes are expected unit-test values, not a fitted model's calibration result. The null fixture is not a false-discovery-rate test. This utility does not authenticate dataset/code/license bytes, parse held-out-group manifests, fit uncertainty models, or prove calibration from one sample. Evaluate each preregistered level (including 0.68 and 0.95) on held-out data and assess coverage jointly with width and proper score.

## 4. A–H review

| Lane | Status | Next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Advanced the EQN-008 uncertainty-scoring utility and deterministic tests. Priority-1 signed-Max-Cut remains the higher execution gate. | Run exact-head CI, then pinned-SDK signed-Max-Cut reconstruction against exhaustive direct/QUBO/Ising values and the complete argmax set; proceed to provider-neutral lowering and target-aware simulation only after semantic agreement. |
| B — cloud/QPU/provider integration | Provider-neutral adapter strategy maintained; no credentials, budget or paid execution. | Simulator/dry-run first; keep provider, target, calibration, pricing and result provenance matched. |
| C — RAM/VRAM/HBM/storage/state/data movement | Readable classical storage remains distinct from Hilbert-space dimension; no storage replacement result. | Preserve input/output bytes, state preparation, transfer, memory, reconstruction, host compute and persistence semantics under identical useful-output contracts. |
| D — device/chip/process/fabrication/packaging | Device/fabrication scope maintained; no new device result. | Require target-specific device/control evidence, reliability, metrology and package/process constraints before transfer. |
| E — Pangola/materials/bio-oil/fusion/cooling/infrastructure | BIO-001 and FUS-001 remain open; no accepted fuel or reliable net-electricity evidence. | Close accepted-liquid mass/energy/yield/upgrading/full-cost and fusion net-delivered lifecycle-cost gates separately. |
| F — economics/benchmarks/evidence/integration | Advanced the scoring contract; no method ranking or economics measured. | Pair interval coverage with width, proper score, false-discovery controls and total training/inference resources under one cost basis. |
| G — chip-manufacturing equipment/software/factory systems | Continuous D/G co-design preserved; no yield or cost-per-good-device result. | Link future design claims to process windows, defectivity, metrology, rework, yield and cost per good die/package. |
| H — strategy/finance/future-industry research/publication | Fresh surveillance recorded; existing source watches retained; multilingual master-plan/funding context preserved. | Maintain cold-start-ready publication and evidence boundaries without duplicating already covered literature. |

INV-034 and INV-035 remain upstream across all eight lanes. No lane is suspended. Legacy Lane I artifacts remain preserved outside the A–H operational map.

## 5. Foundations, equations and permanent mission

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-vs-QSL measurement, FND-004 alternative physical primitives, FND-005 QFT/particle mechanism scans and FND-006 mathematics-first invention remain active. This metric helper does not change fundamental_limits.py, frontier_hypothesis.py or equation_discovery.py, and does not alter EQN-001–008 acceptance criteria.

- **INV-029:** the US$10T–US$100T figure remains an ambition-scale proxy; physical Data-Center-to-One-Phone compression must include external infrastructure, energy, service quality, reliability, form factor and lifecycle cost.
- **INV-030:** biomass carbon may support functional substitution, minimization, recovery/recycling, hybridization or redesign; no elemental transmutation.
- **INV-031:** no commercial ultra-low-cost accepted bio-oil/biofuel result.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost result.
- **INV-033:** no lower WACC/risk-premium result; reducing financed principal reduces absolute interest only at unchanged terms.
- **INV-034:** mathematics-first deep-frontier research continues under present physical constraints and falsification gates.
- **INV-035:** a better interval score or symbolic fit is not a physical law; any candidate still needs dimensional/symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search, proof/experiment and independent validation.

INV-025/026/027 remain evidence-gated moonshots. No qubit count is treated as readable RAM/storage. NPU comparison still requires task semantics, quality, precision, latency, throughput, memory movement and total cost, not TOPS alone. BIO-001, FUS-001 and FIN-001 remain open.

## 6. Synchronization, CI and next gate

This commit updates the README front page, integration hub index, cold-start handoff manifest, WORKLOG.md and RESEARCH_GAPS.md alongside the code, tests, Batch 101 and this integration report. Append-only logs were fetched in full and extended at their exact ends; no prior history was replaced. The commit message carries the required Research-Sync: main trailer.

**Starting-head CI:** core/invariant run #1945 and cold-start audit #1204 passed on f3ca3c12b20b4fa28adfb276ae5804427f9ca2a8. **Resulting-head CI:** pending until Actions runs on the new commit complete; a parent pass does not transfer.

Next highest-value gate is A-GATE-SIGNED-MAXCUT-SDK-001: pin a specific SDK/environment, independently compare operator eigenvalues and optimizer-sign convention against the frozen signed-Max-Cut contract and exhaustive references, preserve the complete maximizer set, then move to target-aware simulation. In parallel, verify SymbolFit source/code/data/license bytes and use the new scoring utility in a preregistered synthetic calibration harness before any real HEP data. No paid QPU execution is authorized.
