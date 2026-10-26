# Research gap RG-EQN-008 — matched cross-method equation-discovery comparison

**Date opened:** 2026-10-26  
**Status:** OPEN — protocol hypothesis recorded; no external method independently reproduced  
**Primary owner:** Lane A — quantum programming/runtime and equation-discovery tooling  
**Cross-lane owners:** Lane F — evidence/benchmark/cost policy; Lane H — literature publication  
**Related:** FND-006; EQN-001–006; RG-EQN-007; RG040; INV-034/035  
**Literature watch:** docs/literature_watch/2026-10-26-progressive-equation-discovery-comparison.md

## Objective

Determine whether progressive symbolic composition, transformer formula generation, language-model search control, or learned structural guidance improves the rate of accepted equations under matched total resources and strict physical/math constraints. Do not assume any method wins because its own paper reports strong results.

## Current evidence

- CoSR is represented by an APS accepted-paper record dated 2026-10-06.
- Transformer formula synthesis, LLM-PySR search control and L2G-SR are represented by official arXiv preprints dated 2026-10-02, 2026-07-05 and 2026-10-14, respectively.
- Main contains a dated synthesis article and this open gap. Existing implementation proposals remain in open PR #56, PR #98 and PR #104 at the time of inspection; PR metadata reported mergeable=false. Their code and test claims are not treated as merged main-branch evidence.
- The main-branch equation-candidate gate now separates formal-proof metadata from empirical validation and requires explicit counterexample/false-discovery state. That is a governance/schema improvement, not a physical truth classifier.

## Blocking unknowns

- No matched cross-method run has been executed on frozen, law-family-disjoint datasets.
- No independent reproduction of the papers' headline benchmark results was performed.
- No accepted formula, physical-law discovery, QPU advantage, measured energy saving or commercial/economic result follows from this gap record.
- Learned structural scores can leak target structure or reward expression-form similarity without improving prediction or physical validity.
- A proof-checked statement can still formalize an inadequate model of nature; empirical definitions and assumptions need independent scrutiny.

## Unlock criteria

1. Resolve/rebase pending implementation PRs without silently duplicating the canonical Lane A interface; inspect exact changed paths and exact-head CI before merge.
2. Freeze dataset/model/source hashes, units, preprocessing, expression grammar, train/validation/test law-family membership and resource budgets before tuning.
3. Compare one-shot symbolic regression, progressive composition, transformer generation, search control and structural guidance using at least 30 preregistered seeds where compute permits.
4. Include held-out scales, unit/equivalence transformations, noise/correlation, counterexample search, false discoveries, failed searches, retries and full training-plus-inference cost.
5. Require held-out prediction and constraint checks; structural recovery is scored only when a known target or declared equivalence class exists.
6. For physical-law candidates, require incumbent assumptions, dimensional/symmetry/conservation/causality checks, limiting cases, a discriminating observable, a held-out prediction, experiment or proof as appropriate, and independent validation.

## Falsification / stop rules

The claimed method advantage fails if it vanishes on law-family-disjoint or scale-shift tests, is explained by unequal total resources, increases counterexamples or constraint violations, or only improves a structural score without improving accepted held-out predictions. Preserve all negative and failed-search outcomes. No candidate equation advances to a physical-law claim by declaration.

## Synchronization debt

This standalone gap is not yet merged into the append-heavy RESEARCH_GAPS.md. Keep the dated record intact until a safe reconciliation can append it without truncating existing history.
