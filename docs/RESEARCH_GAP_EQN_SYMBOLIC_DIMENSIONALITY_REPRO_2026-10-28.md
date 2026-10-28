# Research gap — dimensionality-aware equation-discovery reproduction

**Gap ID:** RG-EQN-SYMBOLIC-DIMENSIONALITY-REPRO-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane F — evidence/reproducibility contract  
**Method owner:** Lane H — literature/provenance; Lane A — comparator implementation  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Related:** INV-034–035, FND-006, EQN-001–EQN-008, BIO-001, FUS-001, FIN-001  
**Source watch:** [2026-10-28 dimensionality-aware and adaptive equation discovery](literature_watch/2026-10-28-symbolic-regression-symfm-pitpo.md)

## Objective

Test whether state reconstruction plus learned active-subspace reduction and symbolic extraction (SymFM-style), or policy-optimized physics-informed candidate generation (PiT-PO-style), improves the rate of independently accepted equations over matched numerical and search-controller baselines without losing important variables, worsening out-of-distribution generalization, or hiding false discoveries.

## Current evidence and blockers

- SymFM's public preprint and code repository describe three implemented stages: partial-observation state estimation, active-subspace projection and hierarchical KAN/symbolic extraction. The proposed Transformer foundation encoder is not implemented.
- The repository reports both positive and negative results and documents a corrected SEIRD split/metric issue. This is a useful audit trail, not independent replication.
- PiT-PO is currently treated as an external preprint claim. A runnable version, training configuration, data provenance, exact resource accounting and independently reproducible held-out evaluation have not been verified in UQPU.
- No candidate method has been run in this project for this gap. No physical equation, commercial model or engineering advantage is promoted.

## Falsifiable acceptance contract

1. Pin exact source revisions, dependency lockfiles, dataset/license and SHA-256 hashes for raw data, splits, preprocessing, equation grammar, unit schema, acceptance rule and held-out group manifest.
2. Use known-law synthetic systems to test identifiability, missing/noisy observations, dimensionality reduction, and adversarial cases where a low-variance variable controls the governing law.
3. Compare one-shot numerical SR, search-controller SR, an independent staged search, SymFM-style active-subspace SR and PiT-PO only if executable code/configuration is available. Equalize wall-clock, CPU-core time, accelerator time, peak memory, candidate evaluations, generated tokens/model calls, retries and total cost ceiling.
4. Preregister at least 30 seeds per method and group-disjoint held-out tests by law family and at least one of scale/geometry/material/device family. Preserve failed and undecided runs.
5. Acceptance requires predeclared equation recovery or prediction thresholds, dimensional/symmetry/conservation/causality checks, limiting cases, counterexample search, false-discovery rate, and independent review. A lower fit error alone cannot pass.
6. For BIO-001/FUS-001 transfer, bind a real process boundary and independently measured mass/energy or thermal-fluid data before assessing a surrogate. For device/manufacturing transfer, use independent process-window/metrology data. Only then assess downstream system economics.

## Dependencies and next action

- Lane A/F: implement the preregistered comparison through the existing equation_discovery_comparison.py contract; first audit that its run records bind method revision, data/split hashes and the same hard resource budget.
- Lane H: resolve provenance/version status and obtain a reproducible PiT-PO implementation before adding it as an executed comparator.
- Lane E: identify a single candidate constitutive relation only after the synthetic protocol passes.
- Lane F: record cost per accepted equation and time-to-evidence, not token count alone.

**Sync debt:** RESEARCH_GAPS.md is an 80-KB append-oriented canonical ledger. This focused gap is published as a standalone dated artifact to avoid a risky whole-file rewrite; add its ID to the next safe ledger append. Until then, the standalone gap and this batch are canonical for this specific issue.

## Closure rule

Do not close on a paper abstract, author's metric, training reward, one successful seed, or a symbolic-regression fit. Close only after independent reproduction, adversarial/held-out acceptance and a clearly stated downstream experiment. No current physical limit or established equation is displaced by this gap.
