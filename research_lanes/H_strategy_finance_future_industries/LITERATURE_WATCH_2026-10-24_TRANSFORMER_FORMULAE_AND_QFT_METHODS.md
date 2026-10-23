# Literature watch — 2026-10-24: transformer formula synthesis and proof-status accounting

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance and future-industry research  
**Feeds:** Lane A; FND-005/FND-006; EQN-001–006; integration/F; INV-029, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY` — one journal article and two public preprints/surveys  
**Project evidence promotion:** none

## Sources reviewed

1. Shuwei Wang et al., *Synthesizing Physics Formulae with Transformers*, arXiv:2610.03947, submitted 2026-10-02: https://arxiv.org/abs/2610.03947
2. Ying Xie, *What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics*, arXiv:2610.17090, submitted 2026-10-12: https://arxiv.org/abs/2610.17090
3. Simon M. Martin and Tarun Grover, *Perturbative Approach to Symmetric Mass Generation*, Physical Review Letters 137, 161601, published 2026-10-13: https://doi.org/10.1103/c9c4-xnrv

The arXiv items are preprints/surveys as observed. The PRL article is peer-reviewed journal literature. None is a UQPU experiment, material/fuel/fusion measurement, accepted-task economic result, or a newly established law for this project.

## Delta 1 — formula-distribution design can improve extrapolation, but is not physics validation

The transformer paper reports shaping the synthetic formula distribution used for pretraining and fine-tuning on noise-corrupted targets. On SRBench and LLM-SRBench, the authors report formula synthesis in about ten seconds and better extrapolation than evaluated methods at comparable budgets; search-based methods exceed its accuracy only when given one to three orders of magnitude more time in the reported comparison.

**Genuine UQPU relevance:** this suggests a distinct generator for EQN-002/003: propose compact candidates quickly, then let deterministic symbolic/numeric evaluation, constraints and adversarial counterexamples decide survival. It may reduce candidate-generation wall time, but the claimed speed is benchmark-specific and does not establish lower total compute energy, general scientific validity or a new physical law.

**Limitations:** the abstract-level evidence does not establish independent reproduction, universal out-of-distribution generalization, identifiability, causal mechanism, physical conservation or dimensional consistency. Synthetic formula distributions can encode biases; the candidate may fit observations without being the unique law. Report generator training/inference cost and search/evaluator cost together.

### Falsifiable follow-up — EQN-002/003 matched-budget benchmark

- Freeze dataset, train/validation/held-out domain hashes before generation.
- Compare transformer proposal, current symbolic-regression baseline and a random/known-law negative control under identical wall-clock, CPU/GPU-hours, energy where measurable, candidate-evaluation count and data access.
- Score held-out interpolation and extrapolation separately; equation complexity; dimensional, symmetry, conservation and causality checks; limiting cases; counterexample survival; and candidate rank stability across seeds.
- Include a known-law recovery suite and a deliberately non-identifiable dataset where distinct equations produce identical observed samples.
- Treat any score as `MODEL_ONLY`; no equation advances without proof or a discriminating experiment and independent validation.

## Delta 2 — AI-generated mathematical instruments require explicit proof-status provenance

The October survey analyzes 38 families from a collection of AI-written mathematical manuscripts and proposes extracting reusable lemmas, constructions, inequalities and proof mechanisms. Its own abstract says novelty assessments are provisional and that no Lean development was compiled or kernel-checked for the survey.

**Genuine relevance:** EQN-005 and FND-006 should distinguish (a) a candidate mathematical instrument, (b) a checked proof in a declared formal system, (c) a proof whose premises match the physical claim, and (d) an empirically supported physical hypothesis. These are different gates. A formal proof of a model theorem does not prove that the model describes nature.

**Follow-up:** add provenance fields for formal-system/version, exact source commit, kernel-check result, dependencies/axioms, premise-to-physical-assumption mapping, and independent proof replay. Missing or failed checks remain visible as negative evidence.

## Delta 3 — symmetric mass generation is a model-specific field-theory advance, not a mission-level new law

The PRL article develops an epsilon-expansion approach near the critical dimension for an interaction becoming marginal and applies it to two models, conjecturing their universal critical behavior and computing universal quantities. A related lattice Monte Carlo PRL article published 2026-10-08 reports a phase-diagram/multicritical-point result in a specified lattice-fermion model: https://doi.org/10.1103/m3pf-j37b.

**Relevance:** FND-005 may use these as examples of linking perturbative effective descriptions with lattice results and symmetry/critical-scaling observables. They do not, by themselves, imply a new elementary particle, a replacement for the Standard Model, a computational primitive, a new memory mechanism, or a route to lower fusion/bio-oil cost.

**Follow-up:** if pursued, record the exact model, dimensions, symmetry assumptions, expansion parameter, controlled regime, lattice observable, finite-size/scaling checks and an independent numerical reproduction. Require a separate device/system consequence before assigning an economic effect.

## A–I integration status

| Lane | Status this cycle | Evidence boundary |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Tightened equation-candidate numeric validation: held-out errors must be finite and validation count an integer. Regression tests added for NaN/±infinity and invalid counts. | Software contract/test only; no quantum advantage. |
| B — cloud/QPU/provider integration | No provider contact or execution. Preserve provider-neutral, no-submit boundary. | No live QPU evidence. |
| C — state/memory/storage/data movement | Formula generation does not imply readable classical state compression; require output-information accounting. | No memory/storage replacement evidence. |
| D — device/chip/process/fabrication | No device consequence demonstrated by these sources. | No device/fabrication evidence. |
| E — materials, biomass, bio-oil, fusion, cooling | No relevance sufficient to change BIO-001/FUS-001 evidence. | No material/fuel/net-electricity evidence. |
| F — economics/benchmarks/evidence | Future comparison must include total generator + evaluator compute, energy, retries and accepted-result denominator. | No cost/task, interest or WACC result. |
| G — manufacturing equipment/factory systems | No validated process requirement follows from these papers. | No manufacturing evidence. |
| H — strategy/finance/future industries | Published this literature watch and linked the candidate-generation/proof-status gates to the strategic research program. | Literature-only; no commercialization promotion. |
| I — field-agnostic contactless lift (repository extension) | Inspected; no connection to this watch and no change. | Model/contract only; no lift or field-control claim. |

## Invariant contribution

- **INV-029:** keeps data-center-to-phone claims tied to useful-output, state/I/O, physical-boundary and lifecycle-cost contracts; no compression result is claimed.
- **INV-030:** no carbon-material substitution or elemental-transmutation claim.
- **INV-031:** no accepted liquid-fuel or commercial-cost evidence.
- **INV-032:** no net delivered fusion-electricity evidence.
- **INV-033:** no financed-principal, interest-cost or WACC evidence.
- **INV-034:** adds a candidate route to formal and model-specific physics reproduction while preserving assumption-scoped claims.
- **INV-035:** reinforces generator → constraints → evaluator → held-out/generalization → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics.

INV-025/026/027 remain preserved. The 100×/100,000,000× targets and universal subsystem replacement remain goals, not demonstrated results. No AI-generated equation is promoted to a physical law.

## Next highest-value gate

Run the equation-discovery unit suite and CI after the finite-metric guard is merged. Then preregister a small known-law / non-identifiability benchmark with frozen splits and matched generator/evaluator budgets. Separately, the current Lane A execution gate remains the authorized read-only IBM target snapshot and route/native-conformance certificate; this literature watch does not authorize any QPU job.
