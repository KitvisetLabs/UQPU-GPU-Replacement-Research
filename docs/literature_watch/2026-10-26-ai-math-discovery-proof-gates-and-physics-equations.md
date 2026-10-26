# Literature watch — 2026-10-26: auditable AI mathematics and fusion-grid interfaces

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — strategic research publication  
**Implementation owner:** Lane A — equation-discovery contract; Lane F — evidence gates  
**Integration:** A–H; FND-001–006; EQN-001–006; INV-025–027 and INV-029–035  
**Evidence class:** LITERATURE_ONLY (official preprints, public research corpus, and an official IAEA conference abstract)  
**UQPU evidence promoted:** none

## Delta relative to the 2026-10-25 watch

The prior watch already covered ProofEvolve, graph-based constitutive discovery, physics-constrained inspection, and formal proof-search design. This update adds (1) an independent survey of a newly released large AI-generated mathematics corpus, (2) an open reproducible Lean-prover pipeline, and (3) a recent fusion long-pulse grid-interface study. These are method and engineering-driver updates, not evidence of new physical laws, quantum advantage, commercial fusion, or low-cost fuel.

## 1. Public AI-generated mathematics corpus: discovery volume is not verification

**Sources and dates**
- OpenAI's public mathematics manuscript repository, initial release announced 2026-10-06: https://github.com/openai/math
- Ying Xie, “What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics,” arXiv:2610.17090, submitted 2026-10-12: https://arxiv.org/abs/2610.17090

The corpus is reported as 722 AI-written manuscripts across 372 problem families. Xie's survey examines 38 families and extracts candidate lemmas, constructions, inequalities, and proof mechanisms while comparing them with antecedents. It explicitly describes novelty judgments as provisional, notes corrections to some claims/hypotheses/counts, and reports that the survey did not compile or kernel-check Lean developments.

**Genuine delta:** a large public candidate corpus and an independent, claim-level audit provide a concrete test bed for provenance, novelty, formalization status, dependency tracking, and negative-result retention. Manuscript count and plausible exposition are not a proof-status label. The survey is itself not a substitute for checking each source proof.

**UQPU relevance:** EQN-001–006 and FND-006 should distinguish candidate generated, mathematical argument inspected, formal statement frozen, kernel proof checked, counterexample search completed, and physical prediction independently tested. A checked theorem can establish only its formal statement under its imports/axioms; it cannot establish that the statement describes a physical system.

**Limitations:** no claim in this corpus is treated here as independently verified, novel, or physically relevant merely because it was released. Priority and correctness require source-level comparison and formal checking. No equation from the corpus is promoted into UQPU physics.

## 2. NanoProof: reproducible formal-prover infrastructure

**Source and date:** Matěj Kripner and Milan Straka, “NanoProof: Open and Efficient Automated Theorem Proving in Lean 4,” arXiv:2610.11605, submitted 2026-10-08: https://arxiv.org/abs/2610.11605

The preprint reports release of training data, extraction tooling, training pipeline, and weights for a factorized execution-guided Lean 4 prover. It reports 50.8% pass@16 on MiniF2F-Test for its evaluated model, outperforming two nearby systems in its class at substantially lower compute. This is a reproducibility and resource-accounting lead, not evidence that the system is superior to every formal prover or that a physical model is correct.

**Exact UQPU relevance:** formal proof checking can be used for algebraic identities, lower-bound derivations, and compiler/workload transformations when the theorem statement and assumptions are frozen. Pin Lean/kernel/library versions, statement and import hashes, and axiom/admission policy; record failed proof attempts and search compute. Formal proof, numerical simulation, held-out prediction, experiment, independent replication, and cost remain distinct gates.

**Falsifiable follow-up EQN-PROOF-002:** freeze a small theorem derived from a current UQPU mathematical helper; run a pinned proof checker; independently verify the statement, imports, and admission policy; then mutate one premise to create a known-invalid control. Pass only if the intended theorem checks and the mutated control fails. Record proof-search wall-clock, host resources, failures, and exact hashes. This validates a proof workflow only, not a physical law.

## 3. Fusion long-pulse grid peak shaving: useful driver, incomplete plant economics

**Source and date:** Ling Zhang, “Research on peak shaving of grid capacity for BESS PCS energy storage topology in long-pulse operation of nuclear fusion,” presented 2026-10-21 at the IAEA Third Technical Meeting on Long-Pulse Operation of Fusion Devices (2026-10-20 to 2026-10-23): https://conferences.iaea.org/event/452/contributions/42958/

The conference abstract describes a battery-energy-storage power-conversion model for smoothing pulse-load demand. Its reported model result reduces grid-side peak power from approximately 212.0 kW to 107.2 kW (about 49.4%). Treat this as an abstract-reported model/simulation result, not measured plant performance. It does not report the complete storage energy capacity, round-trip losses, lifetime/replacement, parasitic load, capital cost, grid tariff, or fusion plant's net delivered electricity.

**Exact UQPU relevance:** FUS-001 should separate peak-power and grid-interface sizing from annual net kWh and lifecycle cost. A lower peak may reduce required installed grid/PCS capacity, but storage CAPEX, losses, degradation, maintenance, construction, financing, and availability may offset that benefit. No fusion-cost scenario should change until the full energy/time series and cost boundary are available.

**Falsifiable follow-up FUS-GRID-001:** obtain the underlying time-series and model, freeze baseline and BESS dispatch/control, independently reproduce peak reduction, and report peak kW, energy throughput, state of charge, round-trip losses, availability, degradation, installed power/energy, lifecycle replacement, and total annualized cost. Compare against no-storage and alternative grid-control baselines on the same pulse schedule. A peak reduction alone does not pass the net-electricity or cost gate.

## 4. Equation-discovery contract change and experiment

The repository's equation-candidate record already captured baseline/proposed equation, units, constraints, limiting cases, falsifier, observable, held-out error, provenance, and independent-validation plan. This cycle makes several previously implicit requirements explicit: incumbent assumption, dimensional/symmetry/conservation/causality checks, counterexample-search plan/status/notes, held-out prediction, proof-or-discriminating-experiment plan, formal-proof status/notes, and false-discovery status/notes.

The fields are governance metadata, not automated proof. A user-entered status cannot substitute for a reproducible checker artifact. The promotion guard remains conservative: physical-candidate discussion still requires an allowed empirical evidence class, independent validation, held-out improvement, no unresolved counterexample search, and no unresolved false-discovery flag. Even that guard is not a declaration of universal law.

**Follow-up:** the new unit tests should reject missing physics/falsification fields, unrecorded proof status, missing counterexample details, and candidates marked as counterexamples or false discoveries. CI is the authoritative validation gate for this commit.

## Cross-lane integration and non-claims

- **A:** improve the candidate contract; next run a frozen identical-useful-output workload through reference/bound checks and competitive CPU/GPU/NPU baselines.
- **B:** keep provider-neutral lowering and target-specific prices/probabilities separate; no credentials, provider execution, shots, or paid jobs used.
- **C:** keep state-space size distinct from readable RAM/VRAM/HBM/storage; no physical-memory or data-movement savings measured.
- **D/G:** formal/model gates may screen device/material equations; no fabrication, yield, device, or factory result follows.
- **E:** the IAEA abstract contributes only a grid-interface driver candidate; no Pangola-carbon substitution, saleable bio-oil, or commercial fusion result.
- **F:** record proof-search resources and full storage/energy/lifecycle cost as separate quantities; no accepted-task economic advantage or WACC effect measured.
- **H:** preserve the multilingual Ketskaew Chulamani / Kanusanan Pongpanna master-plan links and strategic AI-agent/funding context; strategy is not empirical evidence.

**INV-029:** no phone-class physical compression or lifecycle-cost result.  
**INV-030:** no elemental transmutation or critical-material substitution claim.  
**INV-031:** no saleable liquid yield, upgrading balance, or fuel-cost result.  
**INV-032:** no net reliable delivered fusion-electricity result.  
**INV-033:** no measured principal, interest, risk premium, or WACC change.  
**INV-034:** advances auditable mathematics-first hypothesis workflow only.  
**INV-035:** strengthens equation discovery, formal-proof metadata, counterexample tracking, held-out prediction, and independent evidence separation.

FND-001–006 and EQN-001–006 remain active. No new physical law, real-QPU advantage, or commercial technology result is claimed.