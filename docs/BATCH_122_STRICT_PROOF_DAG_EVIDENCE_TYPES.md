# Batch 122 — strict proof-DAG evidence metadata types

**Date:** 2026-10-29  
**Starting main SHA:** eae52617e5d3effa942b8f4653bb835a876cc355  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** Lane F evidence/resource economics; Lane H literature/provenance; B provider routes; C state/memory/data movement; D/G device-manufacturing co-design; E materials/energy/infrastructure  
**Evidence class:** SOFTWARE VALIDATION CONTRACT + 3 REGRESSION TESTS + REPOSITORY LITERATURE SURVEILLANCE  
**Paid QPU execution:** not authorized or attempted

## 1. Starting state and preservation

Started from the dynamically observed `main` head and inspected the charter, invariants, goals, README, Research Operating System, open-frontier directive, Kanusanan Pongpanna Model, strategic references, permanent root directives 00/00A/01–06, newest Batch 121 and its literature/gap/integration artifacts, exact-QUBO and equation-discovery gates, living research gaps, and latest GitHub Actions runs.

The latest observed main commit was `eae52617e5d3effa942b8f4653bb835a876cc355`. Its UQPU Prototype and Project Invariants Actions run completed successfully. The Batch 121 starting-head CI was green; this new commit must pass exact-head CI before this batch is CI-green.

The permanent root directives, INV-025/026/027, INV-029–035, INV-036/037, Lane A–H architecture, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain preserved. No root directive or large canonical history file was rewritten from a partial excerpt.

## 2. Fresh literature surveillance

Fresh public searches covered neuro-symbolic proof-DAG evolution (ProofEvolve, arXiv:2608.26334), near-memory QUBO/Ising context selection (p-DCIM, arXiv:2610.37033), uncertainty-aware symbolic regression (SymbolFit, arXiv:2607.19750 v2), physics-informed equation search, and thermodynamic-control/quantum-feedback bounds.

Repository searches confirmed these sources are already recorded in the current canonical literature/gap records. No additional material source that changes this cycle's acceptance gate was identified, so no duplicate literature-watch article was created. This is a negative source-deduplication result, not evidence that the field has no new work. External papers remain third-party evidence and have not been independently reproduced by UQPU.

## 3. Lane A implementation — reject booleans as process evidence

Python's `bool` type subclasses `int`. Therefore a checked node with `checker_exit_code=False` could pass a comparison against zero, a failed node with `checker_exit_code=True` could pass an `isinstance(value, int)` and nonzero check, and `independent_reproduction_count=True` could be interpreted as one reproduction.

Hardened `software/uqpu-prototype/uqpu/proof_dag_reuse.py` to require exact built-in integer types for checker exit codes and independent reproduction counts. Added three regression cases that reject those boolean values. The existing graph/split/reuse checks remain unchanged.

### Acceptance boundary

The validator still returns `METADATA_ONLY_NOT_PROOF`. The patch does not execute Lean or any proof kernel, verify semantic equivalence, establish theorem novelty, authenticate the checker, or validate physical meaning. SHA-256 values bind declared bytes; they do not prove authorship or truth.

The execution environment could not clone GitHub because DNS/network access was unavailable. No local full-suite result is claimed. GitHub Actions on the exact resulting commit is the acceptance gate.

## 4. Eight-lane review

| Lane | Status this cycle | Evidence boundary and next gate |
|---|---|---|
| A — Quantum programming/workloads/compiler/runtime | **Advanced** | Strict integer metadata checks and 3 regression tests. Next: pinned theorem-family corpus and equal-budget baseline-vs-schema-reuse comparison; maintain exact QUBO/Hamiltonian references. |
| B — Cloud/QPU/provider integration | Maintained | Provider-neutral routes preserved; no provider/target-specific job, cross-provider pricing mix or paid execution. |
| C — RAM/VRAM/HBM/storage/state/data movement | Maintained | Proof-DAG size is not classical-memory or Hilbert-space equivalence. Future memory, transfer, host work and energy require measurements. |
| D — Devices/chips/process/fabrication/packaging | Maintained | No new device/fab evidence; continuous D/G co-design retained. |
| E — Biomass/materials/bio-oil/fusion/cooling/infrastructure | Maintained | Pangola function acceptance, BIO-001 accepted-liquid cost and FUS-001 net-electric cost remain open; no commercial claim. |
| F — Economics/evidence/integration | Advanced at evidence-contract level | A metadata false-positive path is closed. No measured economics, WACC change or cost-per-accepted-result improvement. |
| G — Manufacturing equipment/software/factory systems | Maintained | Continuous D/G co-design retained; no factory yield/cost measurement. |
| H — Strategy/finance/future industries/publication | Advanced at provenance/synchronization level | Literature deduplication recorded; six-language strategic links and agent/funding context preserved. Strategy remains context, not scientific/financial proof. |

INV-034 and INV-035 continue to feed all eight lanes. No claim of parallel independent-agent execution is made.

## 5. Foundational and equation-discovery scoreboard

- **FND-001 — thermodynamic-gap accounting:** active; complete-cycle energy boundary and measurement-only theorem reconstruction remain open. Measurement backaction, feedback, controller work, memory/reset and heat flows must be separately accounted.
- **FND-002 — output-information lower bounds:** exact small-instance references remain available; no general new lower bound or demonstrated quantum advantage.
- **FND-003 — matched control vs quantum-speed-limit measurement:** experiment remains open.
- **FND-004 — alternative physical primitives:** hypothesis-gated; no bypass of known constraints.
- **FND-005 — QFT/elementary-particle mechanism scans:** mechanism-gated; no new credible anomaly or device consequence from this cycle.
- **FND-006 — mathematics-first invention:** metadata gate hardened; external ProofEvolve reproduction and held-out proof-search comparison remain open.
- **EQN-001–EQN-006:** no candidate was promoted to a physical law. Continue generator → constraints → evaluator → held-out test → counterexample search → proof/simulation → discriminating experiment → independent replication → device/system consequence → economics. False discoveries and failed attempts remain first-class.
- **BIO-001 / FUS-001 / FIN-001:** still open/model-only where applicable; no commercial fuel, net delivered fusion electricity, or measured financing-rate reduction.

## 6. INV-029–INV-035 mission check

- **INV-029:** no Data-Center-to-One-Phone physical-compression milestone; remote infrastructure must remain inside the system boundary.
- **INV-030:** no elemental transmutation or universal material-substitution claim; function-specific Pangola-carbon substitution/minimization/recovery remains a measured materials task.
- **INV-031:** no accepted ultra-low-cost bio-oil/fuel result; full feedstock-to-saleable-liquid energy/cost boundary remains required.
- **INV-032:** no commercial fusion-electricity result; net reliable delivered electricity and full lifecycle cost remain required.
- **INV-033:** no measured WACC reduction; lower financed principal can reduce absolute interest at unchanged terms, but financing-rate effects need separate evidence.
- **INV-034:** foundational mathematics/physics frontier remains active under explicit mechanism and falsification gates.
- **INV-035:** AI-generated equations remain hypotheses until units, symmetries, conservation, causality, limits, held-out prediction, falsifier, experiment/proof and independent validation gates pass.

INV-025/026 100-million-unit moonshots and INV-027 open-frontier research remain goals with subsystem-specific useful-output contracts. NPU evaluation must use actual workload quality/precision/latency/throughput/memory/data movement/cost, not TOPS alone. Quantum state-space size is not readable classical storage.

## 7. Result, gaps and next gate

**Positive result:** closed a specific boolean-to-integer metadata validation loophole and added targeted regression tests.

**Negative/remaining evidence:** no local clone/test run because of network/DNS restrictions; no external theorem corpus, Lean kernel, equal-budget proof search, independent held-out proof reproduction, real QPU, physical device, material, fuel, electricity or financing experiment was run.

**Next highest-value gate:** require the exact-head GitHub Actions workflow to pass, then pin the external proof-search environment and theorem corpus, preregister theorem-family-disjoint splits, compare baseline proof search against schema reuse under equal compute/time budgets, and independently re-run held-out kernel-check results. Record invalid/changed statements, residual premises, failed proofs, timeouts, peak memory, wall time, energy where measurable and cost per independently accepted result.
