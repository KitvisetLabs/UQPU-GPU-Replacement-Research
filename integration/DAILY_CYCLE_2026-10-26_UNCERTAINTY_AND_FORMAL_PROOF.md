# Eight-Lane UQPU cycle — 2026-10-26 — uncertainty-aware equation-discovery comparison and proof-search gate

**Canonical starting main:** 85e4a5edb9d0e9f6d121c2af6994ed9968f455d6  
**Primary implementation owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence/integration owner:** Lane F — benchmark uncertainty, reproducibility and economics  
**Publication owner:** Lane H — literature surveillance and strategic research  
**Evidence class:** SOFTWARE_CONTRACT + UNIT_TESTS_TO_BE_CONFIRMED_BY_EXACT-HEAD_CI + LITERATURE_ONLY; no physical/commercial claim promoted

## Canonical starting-state audit

Read the current PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root directives 00, 00A, and 01–06, the latest canonical Batch 066 plus Batches 064–065 and 057–058, RESEARCH_GAPS.md, RG-EQN-008, RG040, RG050, the current integration records, all A–H lane READMEs, and the exact-head Actions runs.

Main was at 85e4a5edb9d0e9f6d121c2af6994ed9968f455d6 at cycle start. Batch 066 is the newest canonical numbered batch; no fixed batch number was assumed as a selector. Root directives, the permanent Ketskaew Chulamani / Kanusanan Pongpanna Model, strategic AI-agent/funding references and the Thai/English/Chinese/Japanese/Korean/German public master-plan links remain present. INV-025/026/027 and INV-029–035 remain preserved. D/G co-design remains explicit. The auxiliary Lane I directory does not supersede A–H. Large append-only RESEARCH_GAPS.md and WORKLOG.md were not replaced from partial excerpts.

## Fresh literature surveillance

The fresh search rechecked symbolic regression, neural-symbolic equation discovery, AI/formal theorem discovery, differentiable/physics-informed modelling, automated experiment design, effective/constitutive laws, lower bounds/no-go theorems, experimentally motivated model changes, credible anomalies, fusion, biomass/materials and energy/finance.

- The APS accepted-paper record for Xia & Zhang's Chain of Symbolic Regression (CoSR), accepted 2026-10-06, is already covered by docs/literature_watch/2026-10-26-progressive-equation-discovery-comparison.md; no duplicate article was created. The source argues for progressive composition of interpretable knowledge units, but its reported examples are not a UQPU reproduction.
- A distinct peer-reviewed formal-proof-search result by Tsoukalas et al., Science (2026-10-08; DOI 10.1126/science.aej2213), was source-checked and published as docs/literature_watch/2026-10-26-formal-proof-search-open-problem-scaling.md. Its reported benchmark counts motivate a proof-kernel/statement/dependency gate; they do not establish physical-law truth.
- No new source found in this pass changes the accepted-liquid boundary for BIO-001, the full net-reliable-electricity boundary for FUS-001, or measured project-principal/interest/WACC status for FIN-001.

## Implementation delta

Extended software/uqpu-prototype/uqpu/equation_discovery_comparison.py and its tests to emit marginal 95% Wilson intervals for each method's accepted-candidate rate and paired seed-level acceptance counts/difference. The output schema is versioned to uqpu-equation-discovery-matched-comparison-v2.

This improves uncertainty visibility without promoting a winner: the intervals assume exchangeable Bernoulli seed outcomes for the frozen benchmark and do not account for tuning or multiple comparisons; paired counts are descriptive only and no p-values are generated. The current test fixture is synthetic test data, not a method benchmark. No CoSR/transformer/search-control/structural-guidance run was executed.

## Explicit A–H status

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** comparator now reports acceptance uncertainty and matched-seed outcome counts; regression tests added. Next: execute a preregistered >=30-seed comparison on frozen law-family-disjoint data, then a separate identical-useful-output QUBO/QAOA or other workload gate with reference/bound certificates and competitive CPU/GPU/NPU baselines.
- **B — Cloud/QPU/provider integration:** provider-neutral interfaces retained for IBM Quantum, Braket, Azure Quantum, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers. Simulator/dry-run first; no credentials, provider execution or paid QPU jobs.
- **C — RAM/VRAM/HBM/storage/state/data movement:** logical state cardinality remains distinct from readable classical memory/storage. Physical bytes, transfers, I/O, persistence, reconstruction and energy are not inferred from the equation-discovery benchmark.
- **D — Devices/chips/process/fabrication/packaging:** inspected as a continuous lane; no new device/process/packaging result. Preserve co-design with G and require measurable process/yield/lifetime consequences before promotion.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** inspected; no new accepted liquid fuel, functional Pangola-carbon substitution, or net delivered fusion-electricity evidence. Maintain full feedstock/upgrading and fusion recirculating-power/lifecycle boundaries.
- **F — Economics/benchmarks/evidence/integration:** uncertainty and paired-outcome fields added; provider/target costs must remain matched. No accepted-task cost advantage, energy saving, financing principal/interest reduction or WACC change demonstrated.
- **G — Manufacturing equipment/software/factory systems:** continuous D/G co-design retained; no manufacturing-equipment or factory-yield evidence promoted.
- **H — Ketskaew Chulamani / Kanusanan Pongpanna Model strategy, finance and future industries:** new dated formal-proof-search literature watch; multilingual master-plan links and strategic AI-agent/funding context preserved. Strategy and mathematical proof remain distinct from empirical evidence.

## Foundational and equation-discovery status

- **FND-001:** finite-state active-memory objective and exact-channel reproductions remain MODEL_ONLY mathematical evidence; physical work/heat, bytes, joules and accepted-task quality remain unmeasured.
- **FND-002:** output-information/reconstruction lower-bound contract remains active; no readable-memory equivalence inferred from Hilbert-space size.
- **FND-003:** matched control-vs-quantum-speed-limit measurement remains an open experimental gate; no physical speed-limit advantage measured.
- **FND-004:** alternative physical primitives remain hypotheses requiring a causal mechanism, baseline and discriminating experiment.
- **FND-005:** QFT/elementary-particle mechanism scans remain theory/literature only; no device consequence or new law.
- **FND-006:** strengthened the formal-proof/statement-faithfulness and uncertainty-aware equation-discovery pipeline; this is software/method work only.
- **EQN-001–006:** candidate generation remains separate from constraints, held-out prediction, counterexample search, proof, experiment and independent replication. The new watch adds a concrete proof-kernel/axiom/dependency audit proposal. No AI-generated equation is promoted to a physical law.

## INV-029–035 contribution and evidence boundaries

- **INV-029:** capability/energy/physical-boundary/lifecycle-cost framing preserved; no phone-class physical compression result.
- **INV-030:** functional substitution/minimization/recovery/recycling/redesign preserved; no elemental transmutation or measured material substitution.
- **INV-031:** accepted liquid-energy function and full upgrading/logistics/finance boundary preserved; no commercial bio-oil evidence.
- **INV-032:** reliable net delivered electricity and full lifecycle boundary preserved; no commercial fusion or net-electricity result.
- **INV-033:** lower principal can directly lower absolute interest at unchanged terms; no project-finance measurement or WACC/rate effect in this cycle.
- **INV-034:** mathematics-first deep-frontier agenda remains active and evidence-gated.
- **INV-035:** AI may generate alternatives, but formal proof, empirical model adequacy and physical validation remain separate gates.

INV-025/026/027 and the 100× / 100,000,000× targets remain falsifiable goals, not demonstrated results. No Hilbert-space dimension was counted as readable classical storage, and NPU equivalence remains quality/precision/latency/throughput/memory/data-movement/cost based, not TOPS-only.

## Current gaps, CI and synchronization

- RG-EQN-008 remains OPEN: no matched cross-method run, no independent reproduction, and no method advantage established.
- RG040 remains OPEN: finite-state work-capacity output has no matched physical memory/energy or accepted-useful-task evidence.
- RG050 remains OPEN: the reported MTF electron-temperature milestone does not establish Lawson criterion, net electricity, availability or lifecycle cost.
- The aggregate RESEARCH_GAPS.md remains unsynchronized with several standalone gap records; this cycle preserves explicit sync debt rather than replacing the large append-only file.
- Open PRs for method-specific equation discovery, provider-matched execution, PINN validation and other frontier work remain non-canonical until their exact diffs, dependencies and CI are reconciled. No blind cherry-pick or merge was performed.
- Parent exact-head Actions at cycle start: UQPU Prototype and Project Invariants run 40305066005 SUCCESS (Python 3.10/3.11/3.12, reference benchmark, Qiskit and QSP/QSVT jobs all successful); Autonomous Cold-Start Handoff Audit run 40305066021 SUCCESS. This cycle's new code requires its own exact-head Actions result before the implementation delta is considered CI-verified.
- Paid QPU jobs: 0. No credentials, budget, material experiment, funding action or physical-energy measurement used.

## Next highest-value gate

After exact-head CI, freeze the equation-discovery dataset, law-family-disjoint splits, grammar, unit schema, acceptance rule, tool revisions, seed set and complete resource ceiling; run >=30 matched seeds per method with held-out scales, counterexamples, false discoveries and total cost. In parallel, prioritize a Lane-A accepted-useful-output workload with exact reference/bound certificates and competitive CPU/GPU/NPU baselines. Keep RG040, RG050 and BIO-001/FUS-001/FIN-001 evidence gates open until the required physical and economic balances are measured.
