# Literature watch — AI-generated mathematical instruments and corpus provenance

**Watch date:** 2026-10-28  
**Primary source:** Ying Xie, “What the Machine Invented: Mining New Mathematical Instruments from OpenAI's October 2026 Release of AI-Generated Mathematics,” arXiv:2610.17090, posted 2026-10-12.  
**Source:** https://arxiv.org/abs/2610.17090  
**Underlying public corpus:** https://github.com/openai/math  
**Evidence class:** `LITERATURE_ONLY` — external preprint/survey; not an independent UQPU reproduction.

## What is genuinely new for this cycle

The survey examines an initial public collection of 722 AI-written mathematical manuscripts arranged into 372 problem families, samples 38 families across several mathematical areas, and records candidate mathematical “instruments” (lemmas, constructions, inequalities and proof mechanisms), antecedents, caveats, formalization status and dependencies. It also reports cross-family patterns and provisional novelty assessments.

The useful methodological delta is not the raw manuscript count. It is the structured intermediate layer between a headline theorem claim and a reusable mathematical tool: **claim → instrument → antecedents/dependencies → caveats → formalization status**. This is a potentially useful index for the UQPU mathematics-first discovery ledger and for deciding which claims deserve costly reconstruction.

## Evidence class and limitations

The source explicitly says novelty judgments are provisional or mixed; selected source comparisons correct some statements, hypotheses and counts but do not establish priority or certify the underlying proofs. It reports that no Lean development was compiled or kernel-checked for the survey. Therefore this source is a survey and triage aid, not a proof certificate, novelty certificate or physical result. No claim from the collection has been accepted as an UQPU theorem.

This complements, rather than replaces, Batch 083's source watch on proof-term structure and compression ([arXiv:2610.25357](https://arxiv.org/abs/2610.25357)). The two sources address different stages: instrument/provenance extraction versus proof-structure diagnostics. Neither substitutes for formal checking or independent reconstruction.

## Exact UQPU relevance

- **Lane A / FND-006 / EQN-001–006:** add an auditable candidate-triage stage before implementing an equation or theorem hypothesis. Preserve source revision, exact claim text/hash, dependencies, known antecedents, proof status, counterexamples and failed reconstruction.
- **INV-035:** AI may propose and organize candidate mathematics; established physics remains binding for present engineering claims. For any physical-equation challenge, the incumbent assumption, dimensional and symmetry checks, conservation/causality, limiting cases, held-out prediction, falsifier and independent validation path remain mandatory.
- **Lane F:** if this triage layer is later implemented, measure indexing, formalization, proof checking, independent review, retries, host compute, memory and energy where available. A faster search process is not a lower cost per accepted useful task until the entire accepted-output contract is measured.
- **Lane H:** preserve the source and caveats in the public research record and keep the multilingual Kanusanan Pongpanna Model and strategic AI-agent/funding references as strategy context, not scientific evidence.
- **Lanes B–E and G:** relevance is indirect. This survey does not demonstrate QPU performance, memory/storage replacement, new devices, material substitution, accepted Pangola-derived fuel, net fusion electricity or factory yield.

## Proposed falsifiable follow-up

1. Pin the exact arXiv source version, public-corpus commit, licenses, selected manuscript hashes, Lean/Mathlib revision, compiler options and extraction-tool revision.
2. Select three instrument/claim records from one family. Independently reconstruct the claim, its antecedents and dependency graph; record all discrepancies rather than silently repairing them.
3. Attempt formalization in the pinned proof assistant. Report parse failures, incomplete proofs, kernel-check results and time/resources separately. A survey entry is not treated as checked unless the actual artifact is compiled and kernel-checked.
4. Include positive controls (a known theorem with an established proof), negative controls (an intentionally false or over-strong claim), duplicate/redundant claims and a benign tactic/automation change. Test whether the proposed provenance and size fields detect these conditions.
5. Require a second independent reconstruction. If statement hashes, dependencies or proof results cannot be reproduced, downgrade or reject the record as a decision signal.
6. Keep mathematical correctness, novelty, held-out generalization, physical adequacy and engineering/economic consequence as separate gates. For any physical candidate, continue the full INV-035 hypothesis contract.

## Stop rules

Do not rank theorems or equations by manuscript count, informal elegance or unnormalized proof size. Do not infer scientific priority from the survey's provisional novelty labels. Do not promote any mathematical instrument into a new physical law, technology advantage or economic claim without its own proof, discriminating experiment or other appropriate independent evidence.

## Decision

Add this source as a **supplementary corpus-provenance reference under RG-048**, not as a separate competing proof metric and not as a new gap that duplicates RG-048. No code or acceptance status is changed in this cycle. The next gate is the pinned, small-sample reconstruction described above.
