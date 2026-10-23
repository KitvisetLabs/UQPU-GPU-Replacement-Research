# Pending research sync — PR #53 PISR literature/gap delta

**Date:** 2026-10-24  
**Status:** PENDING_MAIN_REVIEW — this record is a discoverability summary, not a claim that source-branch work is merged.  
**Canonical main at source start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-equation-discovery-audit-v2`  
**Source head at this record:** `76f6f5957e280893e713f1983f0390a4995675a9`  
**Source PR:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/53  
**Sync PR:** pending creation from this branch.

## Purpose and delta

PR #53 continues the 2026-10-24 equation-discovery / offline experiment-design cycle. Its branch is 21 commits ahead of main at the time of this audit. The earlier branch work hardens held-out equation metrics, adds the dependency-free offline experiment-plan contract and adversarial tests, and publishes dated watches/integration contracts for transformer formula synthesis, experiment design, formal proof search, constitutive-law discovery, continuous-QEC limits, LLM-guided symbolic-search control and a model-scoped Gaussian quantum-repeater no-go theorem.

This sync delta adds a new peer-reviewed-method literature watch for physics-informed symbolic regression (PISR) on particle/interface dynamics, integration record INT-20261024-007, a literature-watch index entry, and the standalone PISR-AUDIT-001 data/generalization gap.

## New PISR-AUDIT-001 result

Lazebnik, Mortenfeld and Liberzon, *Machine Learning: Science and Technology* 7, 055004 (published 2026-09-08; DOI 10.1088/2632-2153/ae9c8b), report a scientist-guided, physics-constrained symbolic-regression closure for centimetre-scale spheres crossing density interfaces. Their paper reports repeated-seed and operator-ablation analysis. It is external literature only, not a UQPU result.

The source states that its commercially sensitive underlying data are not publicly available at publication. UQPU source-paper reproduction is therefore **DATA_BLOCKED** until the authors provide data and sufficient artifacts. PISR-AUDIT-001 proposes a separate synthetic audit with frozen whole-trajectory and held-out parameter-group splits, repeated seeds, no-trigonometric/no-exponential/no-delay ablations, shuffled/no-signal false-discovery controls, explicit physical constraints and independent replay. It has **not been executed**. Synthetic results, if later obtained, must not be called reproduction of the published experiment or a new physical law.

## Current evidence and CI

- Current source PR head: `76f6f5957e280893e713f1983f0390a4995675a9`.
- Exact-head workflow run 980: https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40037638198.
- At the latest poll, Python 3.10, 3.11 and 3.12 jobs passed; 11 QSVT/reference jobs remained queued. Full exact-head CI is not closed.
- The preceding source head `68a41c762d51fa790179241b1a489bdca1dab2d3` had workflow run 974 succeed across the reported prototype/invariant, QSVT and reference-benchmark jobs. That pass does not replace the current-head check.
- Open PR #48 and PR #51 also have successful workflow runs on their inspected heads (#840 and #936 respectively), but they remain unmerged and overlap with PR #53's shared equation-discovery/handoff files. Reconcile conflicts and rerun CI before merging.
- The append-only `WORKLOG.md`, `DECISIONS.md` and `RESEARCH_GAPS.md` were not overwritten from partial content.

## A–H and cross-cutting implications

- **A:** equation-metric integrity and offline experiment-plan validation are software-contract work; EXP-DESIGN-002 and PISR-AUDIT-001 remain unexecuted.
- **B:** provider-neutral no-submit policy remains; no provider was contacted.
- **C:** state/output, readable classical bytes, transfer and reconstruction remain distinct; no memory/storage replacement result.
- **D/G:** no device, process-window, fabrication, yield or factory evidence; D/G co-design remains downstream of validated device requirements.
- **E:** no Pangola material qualification, accepted bio-oil/fuel, net reliable delivered fusion electricity or cooling measurement.
- **F:** resource and evidence boundaries are explicit; no cost per accepted useful task advantage, interest reduction or WACC change measured.
- **H:** literature and strategy artifacts added; Lane I remains auxiliary and does not replace the permanent A–H architecture.

FND-001–006 and EQN-001–006 remain evidence-gated. INV-029 through INV-035 are preserved: Data-Center-to-One-Phone is not achieved; Pangola material substitution is not demonstrated; commercial ultra-low-cost bio-oil and fusion electricity are not demonstrated; no financing/WACC effect is measured; no new physical law is claimed. INV-025/026/027 and the 100,000,000-unit moonshots remain falsifiable goals.

The eight permanent root directives, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain preserved.

## Files added by the PISR delta

- `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_PISR_PARTICLE_INTERFACE.md`
- `docs/literature_watch/2026-10-24-pisr-particle-interface.md`
- `integration/INT-20261024-007-pisr-particle-interface.md`
- `research_lanes/H_strategy_finance_future_industries/gaps/PISR-AUDIT-001_DATA_AND_GENERALIZATION.md`
- `integration/COLD_START_HANDOFF_MANIFEST.json` updated with required-reading, gap and next-action state.

## Next highest-value gate

Finish workflow run 980 on the exact source head; then implement the synthetic PISR-AUDIT-001 fixture and deterministic scorer with held-out parameter groups and false-discovery controls. Request the original source data before claiming reproduction. Reconcile PRs #48–#53 conflict-aware; no merge or main synchronization is claimed here.

**Authorization boundary:** no paid QPU job, provider contact, instrument experiment, purchase, hazardous test or external funding action was authorized or performed.

Research-Sync: pending-main
