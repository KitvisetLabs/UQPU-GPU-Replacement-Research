# Literature watch — 2026-10-24: equation discovery, material inverse design, and source-status audit

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy / future-industry research and publication  
**Feeds:** Lanes A, C, D, E, F, G, H; FND-001–006; EQN-001–006; INV-029, INV-030, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY`; accepted-journal records and official preprints, with an unresolved CoSR manuscript-content provenance question  
**Project evidence promotion:** none

## Fresh sources and status

### 1. AI-Newton: concept-driven physical-law discovery

The Physical Review Research accepted-paper page lists You-Le Fang, Dong-Shan Jian, Xiang Li, and Yan-Qing Ma, “AI-Newton: A concept-driven physical law discovery system without prior physical knowledge,” accepted 2026-10-09. The associated arXiv preprint is [arXiv:2504.01538](https://arxiv.org/abs/2504.01538), submitted 2025-04-02. The abstract describes concept proposals from multi-experiment data and progressive generalization; it reports rediscovery of mechanics laws on a noisy experimental dataset.

The accepted-paper date is a publication-status update, not a newly discovered physical law. This cycle reviewed the official accepted-page abstract and arXiv record, not a complete final-version methods audit. Evidence class remains LITERATURE_ONLY.

**UQPU relevance:** a candidate generator family for EQN-003 and a staged-generalization pattern for EQN-006. Test whether concept generation improves out-of-domain structure recovery over direct symbolic regression under the same search, compute, and data budgets. No reported law is treated as a UQPU result.

### 2. CoSR: accepted journal page, unresolved manuscript-content provenance

The Physical Review Research accepted-paper page lists Mingkun Xia and Weiwei Zhang, “Data-driven progressive discovery of physical laws,” accepted 2026-10-06, DOI [10.1103/f2kp-pp4q](https://doi.org/10.1103/f2kp-pp4q). The [official arXiv HTML record](https://arxiv.org/abs/2603.13727), dated 2026-03-14, currently displays the CoSR abstract and a full HTML methods/results body that match the paper title.

A third-party [Pith review of arXiv:2603.13727](https://pith.science/paper/2603.13727) reports that the supplied PDF/full text for version 2 appears to be an unrelated CHI paper, “It Became My Buddy, But I'm Not Afraid to Disagree” (arXiv:2603.13717), and therefore treats the empirical claims as uncheckable. This is a credible artifact/provenance warning, but it is **not** an official arXiv withdrawal notice. During this cycle the PDF bytes and final journal version were not independently retrieved, and the current arXiv HTML page shows no withdrawal notice.

**Decision:** classify this as an unresolved manuscript-content/version provenance question, not as a verified withdrawal or retraction. Do not score CoSR performance or treat it as a trusted baseline until the actual version-of-record, PDF content, code/data version, and any correction/editorial status are reconciled. The HTML body alone does not settle whether the distributable PDF artifact is correct.

### 3. Thermodynamic speed limits in isolated quantum systems

The Physical Review Research accepted-paper page lists Rikuya Kobashi's “Thermodynamic speed limits in isolated quantum systems,” accepted 2026-10-06, DOI [10.1103/k16k-nx74](https://doi.org/10.1103/k16k-nx74). The [official arXiv preprint](https://arxiv.org/abs/2609.12520) was submitted 2026-09-11. It derives generalized second-law inequalities for Gibbs and selected observational entropies using a quantum-Wasserstein distance between coarse-grained states, then obtains lower bounds on operation time through average entropy-production rates.

**UQPU relevance:** a candidate mathematical input to FND-001/FND-003 because it links a declared state-transformation distance, a coarse-graining choice, entropy production, and a time lower bound. It is not a universal circuit-latency bound. Applicability depends on the isolated-unitary protocol, coarse-graining and entropy definitions, initial-state assumptions, and distance convention. A pseudo-metric can assign zero distance to distinct density matrices.

**Falsifiable follow-up:** reproduce one analytically solvable two-level case; freeze the initial/final states and coarse-graining projectors; independently compute the bound and units; then compare it with applicable Margolus–Levitin/Mandelstam–Tamm bounds and a matched control-time measurement. A discrepancy is first a reproduction issue, not evidence of speedup or new physics.

### 4. PiT-PO: physics-informed adaptive equation generation

The official [arXiv preprint, arXiv:2602.10576](https://arxiv.org/abs/2602.10576), dated 2026-02-11, proposes Physics-informed Token-regularized Policy Optimization (PiT-PO). The authors describe an in-search reinforcement-learning loop that updates an LLM generator from candidate-evaluation feedback, combines hierarchical physical constraints with token-level penalties, and reports symbolic-regression benchmark results plus a periodic-hill turbulence-model application.

**Genuine method delta:** unlike a static prompt-only generator, this design attempts to adapt the proposal policy during search. It suggests an EQN-003 generator candidate, but not a reason to trust its equations automatically.

**Limitations and audit requirement:** the reported benchmark and turbulence claims have not been independently reproduced by this project. The Support Exclusion Theorem, its assumptions, the token-penalty construction, physical-constraint definitions, compute budget, ablations, and held-out data selection all need independent scrutiny. A reward penalty for dimensional or domain constraints is not itself proof that all physical constraints are satisfied.

### 5. LLM-PySR: language model as search controller, not judge

The official [arXiv preprint, arXiv:2607.04156](https://arxiv.org/abs/2607.04156), dated 2026-07-05, compares roles for an LLM as equation author, candidate decider, or symbolic-regression search controller. The controller variant lets the LLM guide variables, operators, transformations and search depth while a numerical symbolic-regression engine fits expressions and deterministic metrics govern retention. The authors report tests over 74 AI-Feynman equations, seven formula-recovery tasks, and a battery dataset.

**Genuine method delta:** it separates broad hypothesis-space navigation from numerical fitting and final candidate selection. This aligns with INV-035's rule that AI may guide imagination while evidence and deterministic tests govern acceptance.

**Limitations:** reported benchmark composition, data splitting, wall-clock/compute parity, uncertainty, and the battery relation's causal status require independent review. A compact held-out predictor is not automatically a physical law or mechanism.

### 6. Materials inverse design with symbolic regression — published 2026-10-23

Peiyi Li's [Scientific Reports article, “Machine learning-driven inverse design of high-hardness multi-principal element alloys through symbolic regression”](https://www.nature.com/articles/s41598-026-74491-7), was published 2026-10-23 (DOI [10.1038/s41598-026-74491-7](https://doi.org/10.1038/s41598-026-74491-7)). It combines symbolic-regression-derived descriptors, a CatBoost hardness surrogate, and three metaheuristic search methods. The article reports test-set R² = 0.885 and RMSE = 77.2 HV, plus 22 candidate compositions passing its physical/domain screening, with predicted hardness from 716.6 to 783.1 HV.

**Genuine novelty for this cycle:** a newly published, materials-specific example of interpretable feature construction feeding inverse composition search, relevant to the Lane D/G device/manufacturing co-design and Lane E materials-search method stack.

**Limitations:** agreement among search algorithms using the same surrogate is not a proof of global optimality. The article says processing and microstructure variables are future work; it does not establish that these 22 candidates were experimentally fabricated and validated. Refractory W/Mo are reported as primary strengthening elements, so this is not evidence of carbon replacing critical elements. No Pangola-derived material or electronics function was tested.

**UQPU/INV-030 follow-up:** adapt the methodology, not its hardness predictions, to a functional-unit benchmark for candidate carbon composites/coatings, recovery media, hybrid contacts, and reduced-metal architectures. Compare the exact function required against the incumbent using relevant electrical/thermal conductivity, contact resistance, strength, stability, lifetime, process energy, yield, recyclability and cost. Record direct substitution as unsuitable wherever the function cannot be met; never infer elemental transmutation or universal material replacement.

## What changed for this repository

- The newly surfaced PiT-PO and LLM-PySR papers support testing adaptive-generator and search-controller roles as separate candidate families, not merging generation with acceptance.
- The 2026-10-23 alloy inverse-design paper adds a current Lane E/D/G methods lead, but only for a carefully scoped materials-screening protocol.
- CoSR has a manuscript-content provenance warning from a third-party review, while the current official arXiv HTML page shows CoSR content and no withdrawal notice. The PDF/version discrepancy remains unresolved; the earlier cycle must not label this a verified withdrawal.
- The thermodynamic-speed-limit paper adds a bounded FND-001/FND-003 reproduction candidate; it does not supersede existing limits.
- Targeted searches on 2026-10-24 did not establish new project evidence for Pangola carbon substitution, accepted bio-oil/fuel, net fusion electricity, quantum advantage, or project financing. This is a bounded surveillance pass, not an exhaustive systematic review.

## Falsifiable follow-up plan

1. Retrieve the actual CoSR version-2 PDF and final journal version; compare title, body, equations, code, dataset and version metadata. Seek an official correction/editorial notice if a mismatch remains. Until resolved, exclude CoSR from scored baselines.
2. Retrieve and compare the full accepted AI-Newton version against its preprint; freeze source and dataset versions.
3. Reproduce the thermodynamic-speed-limit result on an analytically solvable two-level state before comparing bounds or control times.
4. Compare direct symbolic regression, concept-driven generation, PiT-PO-style adaptive generation, LLM-controlled symbolic-regression search, progressive composition (only after provenance resolution), and a non-physics-aware negative control under equal data, wall-clock, host-resource, candidate-evaluation, and search budgets.
5. Freeze train/held-out split provenance and numeric-grid fingerprints before candidate selection; test known laws, multiple equally predictive laws, confounding, noise, out-of-distribution contexts, dimensional distractors, symmetry/conservation violations, counterexamples, and false-discovery rates.
6. For materials, separate surrogate ranking from physical-screen and experimental validation. Use a declared functional unit and incumbent benchmark; include processing/microstructure, reliability, yield, and lifecycle cost before claiming any critical-material reduction.
7. Any successful synthetic or surrogate benchmark remains MODEL_ONLY until the relevant physical experiment/proof, discriminating observable, independent replication, device/system consequence, and economics gate passes.

## Invariant contribution and non-claims

- **INV-029:** no phone-class physical-compression evidence; only a candidate-screening method route.
- **INV-030:** no Pangola carbon, critical-material substitution, recovery, or transmutation demonstrated.
- **INV-031:** no commercial bio-oil/fuel evidence.
- **INV-032:** no net delivered fusion-electricity evidence.
- **INV-033:** no interest-rate, WACC, or project-finance improvement measured.
- **INV-034:** expands mathematics-first candidate-generation and speed-limit reproduction routes; no new physical result.
- **INV-035:** separates generator search control from deterministic evaluation and preserves dimensions, symmetry, conservation, causality, held-out prediction, falsifiers, and independent validation as binding gates.

No item in this note is a verified UQPU discovery. It belongs in the literature-watch area, not the root-level INV-037 verified-discovery registry.
