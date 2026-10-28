# Batch 095 — formal-proof discovery and accepted-proof resource accounting

**Date:** 2026-10-28  
**Starting main SHA:** b3252a556b61b7e566d5e057606c1f2e917d79e8  
**Primary owner:** Lane H — literature surveillance and publication  
**Priority execution owner:** Lane A — workload/SDK semantic gate and next compiler/simulator step  
**Cross-lane interfaces:** A–H; FND-001–006; EQN-001–008; BIO-001; FUS-001; FIN-001  
**Evidence class:** OFFICIAL_PREPRINT_SURVEILLANCE / LITERATURE_ONLY for new sources; EXISTING_EXACT_HEAD_CI for the prior pinned-SDK gate  
**Hardware:** no real QPU, paid job or physical experiment

## 1. Cold-start and canonical-state audit

The current main head was resolved dynamically as b3252a556b61b7e566d5e057606c1f2e917d79e8; this run did not select a batch number from old chat context. The cycle read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, the newest Batch 094/093, relevant evidence/gaps, the A–H scoreboard, and the current CI state.

The permanent high-visibility root directives remain present: 00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md, 00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md, and 01–06 covering Pangola carbon, bio-oil, fusion electricity, finance compression, foundational physics/mathematics, and AI-assisted equation discovery. The Kanusanan Pongpanna Model and the six public multilingual editions/links (Thai, English, Chinese, Japanese, Korean and German) remain canonical strategic context. INV-025/026/027 and all eight operating lanes A–H remain active. Historical Lane I material remains a legacy workstream, not a ninth operational lane.

## 2. Priority-1 Lane A — signed-Max-Cut semantic gate reconciliation

The main-head implementation uses pinned Qiskit 2.5.2 to compare a signed-Max-Cut score operator against the declared direct, QUBO and Ising objective contracts. The frozen fixture set contains six small graphs and 74 computational-basis assignments in total. The tests check the full score vector, complete tied argmax sets, minimization of the negative score, the constant term, Qiskit's qubit-0 least-significant-bit convention, finite tolerance and a fail-closed exhaustive-size cap.

The two earlier failures are preserved, not erased: first, a fixture-ordering mismatch between itertools.product and Qiskit basis-index ordering; second, a syntax error in the JSON certificate runner's newline literal. The corrections are on main. Exact-head workflow run [#1872](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40625789742) completed successfully on 2026-10-28; its pinned Qiskit verification step passed. Cold-start handoff audit [#1094](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40625789684) also passed.

**Acceptance boundary:** this is a finite, tiny-instance algebraic SDK cross-check only. It does not run QAOA, establish target-device fidelity, show accepted-task quality, measure latency/energy/cost, or demonstrate a real-QPU advantage. A passing SDK test is not the final workload gate.

**Next Lane A gate:** freeze a small QAOA or other appropriate signed-Max-Cut circuit, compare provider-neutral lowering with exact/classical reference outputs under one identical useful-output contract, then use target-aware simulation and independent SDK checks. Record objective quality, full argmax/tie behavior, shot budget, retries, host work, memory/state/I/O, reconstruction and total cost per accepted task. No paid hardware execution is authorized.

## 3. Fresh literature delta — formal proof discovery and failure-aware evaluation

### Source A: automated theorem resolution with Lean 4 formal verification

Haocheng Ju et al., “Automated Conjecture Resolution with Formal Verification,” arXiv:2604.03789, version 2 dated 2026-06-03: https://arxiv.org/abs/2604.03789. The report combines Rethlas/Matlas theorem retrieval and informal proof construction with Archon/LeanSearch formalization and Lean 4 checking. It reports resolving a 2014 commutative-algebra problem and formalizing the result with little human intervention.

**Genuine method delta:** candidate discovery and formal verification are separate agents and separate artifacts; theorem retrieval can expose cross-domain lemmas, while formalization can reveal missing proof steps or counterexamples.

**Limitations:** this is an arXiv report, not a UQPU reproduction. Correctness applies to the frozen formal statement, axioms, imports and checked proof. It does not validate a physical model or equation. A formalization can still mistranslate the intended mathematical or physical claim, so statement-to-model faithfulness remains a separate gate.

### Source B: repeated AI-generated proofs with explicit failure disclosure

Yichen Huang, “Autonomous disproofs of the sum-product conjecture over R with GPT-5.5 Pro,” arXiv:2607.20525, submitted 2026-07-09: https://arxiv.org/abs/2607.20525. The author reports a three-stage proof-plan / construction / review pipeline, seven correct proofs in eight independent trials, and one trial that explicitly left an unresolved gap rather than claiming success. Reported reasoning usage averaged 132.4k tokens per trial; code, intermediate outputs and proofs were released.

**Genuine method delta:** repeated trials expose proof-generation variability and show why “abstain with a named gap” must count separately from verified success. The small sample also makes a single pass rate imprecise; the reported 7/8 should not be treated as a stable universal reliability estimate.

**Important limitation:** the paper's own discussion notes that the target theorem already states the existence of counterexamples and that the human disproof had appeared; this evaluates autonomous construction/recovery of a proof under a specified target, not a blind decision about whether the conjecture is true or false. The report's contamination-control claims and generated proofs still need independent reproduction. Token counts alone are not financial cost.

## 4. Method integration — proof status is not physical truth

For EQN-001–006 and FND-006, the current candidate pipeline remains:

generator -> explicit mathematical/physics constraints -> evaluator -> grouped/parameter-held-out prediction -> counterexample search -> formal proof or simulation as applicable -> discriminating experiment -> independent replication -> device/system consequence -> economics.

Formal proof status, proof provenance, candidate-equation fit, model-to-nature faithfulness and physical validation must remain distinct fields/gates. An AI-generated equation does not become a physical law because it is elegant, fits a dataset, or has a proof under chosen axioms. A checked counterexample may reject a formal candidate but does not by itself establish the correct replacement physics.

Proposed falsifiable method benchmark:
1. Freeze a small suite containing true obligations, false statements, false lemmas, known counterexamples, formalization mismatches, parser/checker failures, timeouts and resource exhaustion.
2. Compare a fixed generate-review baseline against a formal-verifier/failure-aware-replanning pipeline under equal wall-time, model-call/token, CPU/memory and retry budgets.
3. Record verified proofs, correct rejections, false acceptance, false discovery, abstentions, unresolved cases, retries, proof-checker resources and cost per accepted proof.
4. Hold out theorem families and require independent review. Reject gains that disappear under equal budgets or increase false acceptance.
5. Only after that method gate passes, apply the same protocol to a physical equation with explicit units, symmetry, conservation, causality, limiting cases, held-out prediction and a discriminating experiment.

## 5. Explicit A–H lane status

| Lane | Status this cycle | Evidence and next gate |
|---|---|---|
| A — Quantum programming/workloads/compiler/runtime | ADVANCED / SDK SEMANTICS CI-PASSED | Six frozen signed-Max-Cut fixtures, 74 basis assignments; next provider-neutral lowering and exact-reference comparison before any hardware decision. |
| B — Cloud/QPU/provider integration | MAINTAINED / NO TARGET EXECUTION | Provider-neutral direction retained for IBM Quantum, Amazon Braket, Azure Quantum, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers; simulator/dry-run first. |
| C — RAM/VRAM/HBM/storage/state/data movement | MAINTAINED / CONTRACT ONLY | State preparation, output reconstruction and I/O remain cost terms; no Hilbert-space dimension or basis count is treated as readable classical memory/storage. |
| D — Device/chip/process/fabrication/packaging | MAINTAINED / NO DEVICE MEASUREMENT | Qubit-order/operator semantics inform future mapping; no device physics or fabrication advantage measured. |
| E — Biomass/materials/bio-oil/fusion/cooling/infrastructure | MAINTAINED / OPEN EVIDENCE GATES | BIO-001 accepted-liquid cost and FUS-001 net-electric economics remain unresolved; no material, fuel or electricity result added. |
| F — Economics/benchmarks/evidence/integration | ADVANCED / EVIDENCE CLASSIFICATION | Add cost-per-accepted-proof methodology; do not convert model tokens to dollars without the actual model/pricing basis. No accepted-task cost or wall-plug energy measured. |
| G — Chip-manufacturing equipment/software/factory systems | MAINTAINED / D–G CO-DESIGN | Keep device requirements linked to process-window, metrology, packaging and test; no factory capability claim. |
| H — Kanusanan Pongpan­na Model strategy/finance/publication | ADVANCED / LITERATURE WATCH | Publish the dated source-specific article; preserve the six-language master-plan links and separate strategic ambition from evidence. |

## 6. Foundational and equation-discovery ledger

- **FND-001:** thermodynamic-gap accounting remains a system-boundary problem. Landauer and related ideal bounds are not measured wall-plug energy; controller, reset, cooling and accepted-output work remain required.
- **FND-002:** output-information and reconstruction lower bounds remain tied to the actual useful output contract. No state-space dimension is counted as classical storage.
- **FND-003:** gate-specific quantum-speed-limit reconstruction remains open; no exact theorem reconstruction or matched control-vs-QSL measurement was added here. The non-Hermitian exceptional-point source PR #146 and pending-main record PR #147 remain open and unmerged.
- **FND-004:** alternative physical primitives remain a hypothesis scan; no experimental advantage is claimed.
- **FND-005:** QFT/elementary-particle mechanism scans remain literature/hypothesis work; no new particle mechanism is asserted.
- **FND-006:** mathematics-first invention is advanced at the workflow level through formal proof provenance and explicit failure classes.
- **EQN-001–006:** no candidate equation is promoted. EQN-007 continues to separate formal verification from physical prediction; EQN-008 continues to require matched budgets and grouped held-out comparisons.
- **BIO-001 / FUS-001 / FIN-001:** no new commercial bio-oil, net-electric fusion, lower financed principal/interest or lower WACC result is claimed.

## 7. INV-029 through INV-035 — explicit mission contribution

- **INV-029:** no phone-class physical compression. The computing path still requires end-to-end service, energy, physical boundary and lifecycle-cost contracts; the US$10T–US$100T scale remains an ambition proxy.
- **INV-030:** no Pangola-derived critical-material substitution is demonstrated; functional substitution/minimization/recovery/hybridization remain the valid pathways, never elemental transmutation.
- **INV-031:** no accepted ultra-low-cost liquid fuel is demonstrated; full preprocessing, yield, upgrading/hydrogen/catalysts, utilities, CAPEX/OPEX, logistics and financing remain in the cost boundary.
- **INV-032:** no reliable net delivered fusion electricity is demonstrated; recirculating power, lifetime/replacement, materials damage, availability, cooling and financing remain in the boundary.
- **INV-033:** the new proof-workflow proposal calls for measuring capital/time-to-evidence and actual compute resources; it does not claim lower WACC or financing rates. Lower required principal would reduce absolute interest at unchanged terms, but that effect was not measured here.
- **INV-034:** strengthened the formal-mathematics-to-physics evidence ladder and the explicit accounting of failed/undecided proof attempts.
- **INV-035:** AI may generate equations and proof candidates; established physics governs engineering claims until discriminating physical evidence supports a replacement.

## 8. Integration, synchronization and next gate

This cycle adds a source-specific literature watch, this Batch 095, a cross-lane integration report and an A–H scoreboard checkpoint. README is updated on main in the same commit so the project front page is the handoff surface. The large append-only WORKLOG.md and RESEARCH_GAPS.md are not rewritten wholesale.

The current main-head prototype/invariant workflow and cold-start audit were green before this cycle. The new documentation commit's exact-head CI must be checked after publication; the parent result is not inherited as proof of the new commit.

Open synchronization debt is explicitly retained: PR #146 (FND-003 non-Hermitian exceptional-point QSL) and PR #147 (pending-main sync) are still open and unmerged. Their branch-only artifacts must not be described as present on main. Other open historical PRs were not exhaustively reconciled in this cycle; the repository's sync ledger remains the canonical tracker.

**Next highest-value gate:** Priority #1, provider-neutral lowering and exact/classical-reference acceptance for a frozen signed-Max-Cut workload, followed by target-aware simulation. In parallel, reconstruct one gate-specific FND-003 theorem under a frozen control budget, and keep BIO-001/FUS-001/FIN-001 evidence gates active. No paid QPU job without credentials, bounded budget and explicit owner consent.
