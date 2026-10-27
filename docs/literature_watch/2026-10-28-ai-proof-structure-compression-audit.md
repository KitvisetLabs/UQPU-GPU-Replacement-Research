# Literature watch — 2026-10-28: measuring AI-generated proof structure and compression

**Access date:** 2026-10-28  
**Source:** Safal Raman Aryal, “Studying proof data with proof theory: the case of AI-generated mathematics,” arXiv:2610.25357, submitted 2026-10-18: https://arxiv.org/abs/2610.25357  
**Evidence class:** `LITERATURE_ONLY` — public preprint; not independently reproduced by UQPU  
**Primary owner:** Lane A — formal/equation evidence tooling; cross-lane review by Lane F and Lane H

## Genuine novelty

The preprint treats formally checked proof terms as data for comparative analysis, rather than using kernel acceptance as the only proof-quality signal. It compares generated proof structures with a reference library and cut-free forms, checks metric behavior against expected theorems, and discusses controls for compilation and automated tactics.

The author reports, for the studied corpora, lower realized proof compression for one AI-generated corpus than for Mathlib (31% versus 73%; 55% versus 86% for proofs without automation), and more intermediate claims that could be removed without changing the proof (40% versus 13%). The paper also reports that some apparent differences change after controlling for automation. These are author-reported corpus-level results, not universal properties of AI proofs.

## Limitations and evidence boundary

- This is a preprint and UQPU has not reproduced its parser, corpus selection, metrics or numerical results.
- Subject matter, theorem difficulty, proof-assistant version, compiler options, tactics, and corpus construction can confound comparisons.
- Proof length or compression does not establish theorem correctness, novelty, useful mathematics, empirical adequacy or a physical law.
- A kernel-checked proof only establishes a theorem relative to its formal statement and assumptions. It does not establish that the formal model accurately describes nature.
- No UQPU workload, QPU, device, material, fuel, fusion, energy, financing or mission advantage follows from this study.

## Exact UQPU relevance

The existing `formal_proof_evidence.py` contract binds the statement, proof bytes, environment and run log, and distinguishes `KERNEL_CHECKED` from `INDEPENDENTLY_REPRODUCED`. This paper suggests a separate optional diagnostic layer for proof structure and proof-engineering cost. It must not alter proof-status semantics or be used as a shortcut around EQN-001–006 / INV-035 validation.

For Lane F, proof construction and repair are computational work: when measured, report checker time, generator/inference calls, retries, CPU/GPU time, peak memory and energy separately from proof correctness. Do not infer total resource use from proof-term size alone.

## Falsifiable follow-up

1. Pin the paper version, source code if available, corpus/license, Lean and Mathlib revisions, compiler options, and the exact proof-term extraction procedure.
2. Reconstruct each metric from its definition before comparing any reported percentage. Keep raw proof size, normalized/compiled size, automation-collapsed size, removable intermediate claims and reuse/compression metrics as distinct fields.
3. Freeze subject-matter and theorem-difficulty strata; compare matched proofs and report uncertainty, failed parses and exclusions.
4. Add controls consisting of a known proof, an intentionally redundant proof, a shared-lemma proof and a proof whose automation is expanded/collapsed. Verify expected metric behavior before applying metrics to research candidates.
5. Keep formal validity, novelty, held-out mathematical generalization, physical-model adequacy and engineering economics as separate acceptance gates.

**Decision:** open a focused UQPU research gap for proof-structure metric reconstruction. No numerical claim from the preprint is adopted as project evidence, and no physical law or technology advantage is promoted.
