# Literature watch — 2026-10-24: LLM-guided control of symbolic-equation search

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance, future-industry research and publication  
**Feeds:** FND-006; EQN-001–004; Lane A candidate-generation/runtime design; Lane F accepted-result economics; INV-034/INV-035  
**Evidence class:** LITERATURE_ONLY — arXiv preprint and public source repository  
**Project evidence promotion:** none

## Source and publication date

Zikai Xie, Wenmei Li, Man Luo, Jun Jiang and Linjiang Chen, “Language models guide symbolic equation discovery by controlling search,” arXiv:2607.04156, submitted 2026-07-05: https://arxiv.org/abs/2607.04156. The authors' public implementation is https://github.com/XieZikai/LLM-PySR.

The paper compares language-model roles including equation author, candidate decider and search controller. In the reported LLM-PySR workflow, a language model proposes variables, operators, transformations and search depth; PySR enumerates/fits expressions; deterministic numerical metrics govern retention. The authors report results on 74 AI-Feynman equations, seven complex formula-recovery tasks and an independent battery dataset. These are source-reported results, not reproduced by UQPU in this cycle.

## Genuine methodological delta

This is not merely another equation generator. It makes the **search policy/controller** a distinct object from (1) the equation generator, (2) the numerical symbolic-regression engine, (3) the candidate reviewer and (4) the deterministic acceptance evaluator.

That role separation is useful for UQPU because the search controller can be optimized without granting an LLM authority to certify its own equations. It complements rather than replaces the transformer formula-generation work and HarnessSR's search-harness optimization. It also creates a new failure mode to test: a controller may improve a benchmark by overfitting its operator choices, validation feedback or search budget.

## Limitations and evidence boundary

- The cited work is an arXiv preprint; this watch does not assert peer-reviewed status or independent reproduction.
- Results are tied to the authors' benchmark construction, prompts, model backbones, PySR configuration, budgets and battery-data treatment.
- A lower numerical residual or compact piecewise-linear fit does not establish causal structure, uniqueness, dimensional validity, conservation, symmetry, correct limiting behavior or a new physical law.
- Controller inference, candidate search, fitting, validation, failed iterations, data access and independent replication must be charged to one budget. Comparing only the controller's wall time with a baseline's full search cost would be invalid.
- No UQPU dataset, physical experiment, QPU, material, fuel, fusion or finance result was produced here.

## Falsifiable follow-up — EQN-002B

Run a preregistered, offline comparison on frozen equation families and data hashes:

1. **Freeze provenance:** pin the source commit, Python/Julia/PySR versions, equation grammar, model/backbone, prompt/configuration, seeds, data splits and scoring implementation. Record training, validation and held-out hashes before generation.
2. **Compare roles:** (a) fixed PySR search configuration, (b) LLM-PySR-style search controller guiding PySR, and (c) a direct transformer-formula generator where a runnable implementation and comparable budget are available. Keep an explicit known-law control and a deliberately non-identifiable training set.
3. **Match resources:** same candidate-evaluation ceiling, wall time, CPU/GPU time, data access and transfer accounting; include controller/generator calls, tokens or inference allocation, retries, fitting, reconstruction and independent replay. Record energy only when measured, never as zero when unknown.
4. **Evaluate independently:** held-out interpolation and extrapolation separately; structural recovery; complexity; dimensional/symmetry/conservation/causality checks; limiting cases; false-discovery rate; counterexample survival; calibration; seed stability; and accepted candidates per total budget. The evaluator must not be the same unverified LLM acting as sole judge.
5. **Falsifier:** reject a practical controller advantage if accepted held-out recovery does not improve under matched total budgets, if the gain disappears after all search costs are charged, or if non-identifiable/constraint-violating candidates survive.
6. **Replicate:** rerun from a clean environment and independently check at least one candidate's algebra/proof or discriminating prediction before any technology consequence is considered.

The public LLM-PySR repository exposes data, configurations and run telemetry, but this cycle did not install Julia, call a model API or reproduce the paper. The follow-up remains PROPOSED / NOT EXECUTED.

## Cross-lane relevance

- **A — workloads/compiler/runtime:** separate search-policy configuration from equation proposal and deterministic acceptance; retain hashes and failed iterations.
- **B — cloud/QPU:** no provider or QPU access is part of this work; provider-neutral no-submit rules remain unchanged.
- **C — memory/state/I/O:** formula compactness or Hilbert-space size is not readable classical storage; count data transfer and reconstruction.
- **D/G — devices/manufacturing:** no device or process requirement follows from a better symbolic fit; D/G co-design waits for a validated mechanism and measurable device consequence.
- **E — materials/energy:** the battery-data result does not establish Pangola-carbon substitution, accepted bio-oil cost or net fusion electricity.
- **F — economics/evidence:** score accepted held-out discriminating results per total generation/search/evaluation/replay budget; keep unknown energy explicit.
- **H — strategy/publication:** preserve source date, provenance, limitations and the negative-result path.

## FND/EQN and permanent mission boundary

FND-001–003 still require physical energy/time/output contracts; FND-004 requires a changed assumption and distinct observable; FND-005 remains model-scoped for QFT/particle scans; FND-006 benefits from a search-controller layer but still requires proof/experiment and independent validation. EQN-001–006 remain a staged generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system/economics chain.

INV-029 remains a physical Data-Center-to-One-Phone objective, not remote-terminal access. INV-030 permits functional material substitution/minimization/recovery/redesign, never elemental transmutation. INV-031 and INV-032 remain gated on accepted saleable liquid-energy and net reliable delivered-electricity evidence. INV-033 separates lower financed principal/time from a separately evidenced rate/WACC effect. INV-034/035 keep foundational imagination broad while established physics remains binding for present engineering claims.

No equation is promoted, no physical law is claimed, no QPU or instrument is contacted, and no project advantage is established.
