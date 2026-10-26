# Literature watch — 2026-10-26: comparing progressive, transformer, search-controlled and structure-guided equation discovery

**Accessed:** 2026-10-26  
**Primary publication owner:** Lane H — strategy and research publication  
**Implementation owner:** Lane A — workloads, compiler/runtime and equation-discovery tooling  
**Evaluation owner:** Lane F — benchmark design, evidence and cost accounting  
**Feeds:** FND-006; EQN-001–006; INV-034/035; cross-lane model work in A–H  
**Evidence class:** LITERATURE_ONLY — one accepted-paper record and three official preprints; no UQPU reproduction or physical-law promotion

## Why this is a material synthesis

Four recent methods intervene at different points in the equation-discovery pipeline. That is more useful for UQPU than treating them as interchangeable “AI discovers physics” systems:

1. **Progressive composition.** Mingkun Xia and Weiwei Zhang, “Data-driven progressive discovery of physical laws,” *Physical Review Research*, accepted 2026-10-06, DOI 10.1103/f2kp-pp4q. The Chain of Symbolic Regression (CoSR) approach builds interpretable knowledge units in stages, rather than fitting one large expression in one step. The accepted-paper record reports examples in convection, pipe flow, laser–metal interaction and aerodynamic scaling. Official source: https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q
2. **Formula generation and extrapolation.** Shuwei Wang et al., “Synthesizing Physics Formulae with Transformers,” arXiv:2610.03947, submitted 2026-10-02. The preprint reports that changing the training distribution of formulae and using noise-corrupted targets improves extrapolation in its evaluated synthetic benchmarks. Official source: https://arxiv.org/abs/2610.03947
3. **Search control.** Zikai Xie et al., “Language models guide symbolic equation discovery by controlling search,” arXiv:2607.04156, submitted 2026-07-05. LLM-PySR assigns the language model the role of proposing search operators/variables/depth while numerical symbolic regression and deterministic metrics govern fitting and retention. Official source: https://arxiv.org/abs/2607.04156
4. **Structural guidance.** Letian Huang et al., “L2G-SR: Learning to Guide LLM-based Symbolic Regression,” arXiv:2610.20685, submitted 2026-10-14. The preprint trains a structural verifier from expression-form supervision and uses it alongside numerical fit during search. Official source: https://arxiv.org/abs/2610.20685

The synthesis is a **benchmark-design hypothesis**, not a ranking of these methods. Progressive composition, generator generalization, search control and structural verification are separable interventions; a single end-to-end score cannot tell which component caused an apparent gain.

## Limitations and evidence boundary

- CoSR is represented here by the APS accepted-paper record; the final version and supplemental materials should be checked before attempting a faithful reproduction.
- The other three sources are arXiv preprints. Reported benchmark results are source claims, not independently reproduced UQPU results.
- Symbolic recovery metrics are meaningful only when the target equation or an equivalence class is known. Real experimental systems may not have a uniquely identifiable equation.
- A structurally similar expression can still be numerically wrong, non-identifiable, dimensionally inconsistent or outside its domain. A low prediction error can also hide an invalid mechanism or fail under extrapolation.
- Formal proof of a statement does not prove that the formal definitions faithfully represent the intended physical system. Conversely, a fit or simulation does not establish a new physical law.
- No external weights, external dataset, paid provider, QPU job, shots, physical experiment, material test, fuel test, fusion-plant test or project-finance change was performed for this watch.

## Exact UQPU relevance across A–H

- **A — Workloads/compiler/runtime:** candidate discovery can help generate and audit workload transformations, cost models and algorithm hypotheses. It must not replace equivalent-useful-output contracts, reference/bound certificates or CPU/GPU/NPU baselines.
- **B — Cloud/QPU integration:** compare methods on a provider-neutral workload contract first. Do not mix one target's success probability with another target's price or calibration.
- **C — Memory/state/data movement:** require explicit input/output information, reconstruction, state materialization and transfer accounting; formula complexity is not a proxy for readable memory or device energy.
- **D — Devices/process/fabrication:** constitutive and device models may be candidate targets only where data, units, operating domains and independent measurements exist.
- **E — Biomass/materials/fusion/infrastructure:** pyrolysis, upgrading and plasma/thermal models could supply later test cases, but none of these papers demonstrates Pangola substitution, accepted bio-oil or net fusion electricity.
- **F — Economics/evidence:** compare total cost per accepted formula or model, including rejected searches, retries, training/inference compute, memory, wall time and energy where measured. Amortize training cost once per frozen model hash, not once per random seed; do not mix incompatible cost boundaries.
- **G — Manufacturing equipment/factory systems:** only promote a discovered process relation after process-specific metrology, yield/defect data, held-out lots and independent validation; D/G co-design remains continuous.
- **H — Strategy/publication:** retain source provenance and negative results, and preserve the multilingual strategic master-plan context without treating it as empirical evidence.

## Proposed falsifiable follow-up — EQN-CROSSMETHOD-001

1. Freeze source/version hashes, equation-family IDs, dataset IDs, units, preprocessing, allowed expression grammar, model hashes and the split manifest before model selection.
2. Use law-family-disjoint train/validation/test splits, plus held-out scale ranges, controlled noise/correlation, unit/equivalence transformations and at least 30 preregistered seeds where compute permits. Keep raw-data hashes and split membership independently verifiable.
3. Compare a one-shot symbolic-regression baseline against progressive composition, transformer generation, search control and structural guidance under the same total wall-time and compute budget. If a learned verifier is trained on synthetic target structures, keep test law families disjoint and hide target structure at inference.
4. Count training, inference, search, candidate evaluation, retries, failed runs and rejected candidates. Report CPU/GPU time, tokens, memory, wall time and calibrated energy when available; do not count training cost repeatedly across seeds.
5. Report held-out and extrapolation error, constraint violations, limiting-case failures, counterexamples, false discoveries, structural recovery only when ground truth is known, seed stability, and total cost per accepted formula.
6. For any physical candidate, separately specify dimensional/symmetry/conservation/causality checks, incumbent assumption, discriminating observable, held-out physical prediction, proof or experiment, and independent replication. No symbolic score can satisfy that gate by itself.

**Falsifier:** reject the proposed method advantage if it disappears under law-family-disjoint or scale-shift evaluation, fails to survive matched total-resource accounting, increases counterexamples/constraint violations, or improves structural distance without improving accepted held-out predictions. Retain failures rather than tuning on the sealed test set.

## Main-branch synchronization note

At inspection on 2026-10-26, the main branch already recorded these sources in its late reconciliation note, while implementation work remained on open PRs #56 (CoSR contract), #98 (transformer comparison) and #104 (structural guidance). Their PR metadata reported mergeable=false; this cycle does not assume their code is on main and does not merge them without a fresh exact-head review. This article adds a cross-method synthesis and shared falsification protocol rather than duplicating their implementation.

**Non-claims:** no physical law is established; no quantum advantage, Data-Center-to-Phone compression, Pangola material substitution, accepted bio-oil, commercial fusion electricity, lower WACC or interest saving is demonstrated.
