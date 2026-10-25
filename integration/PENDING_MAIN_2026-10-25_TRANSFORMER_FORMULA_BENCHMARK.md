# Pending-main sync record — transformer formula discovery benchmark

**Date:** 2026-10-25  
**Canonical starting main SHA:** 70796ef8b918fe2e95382bc49cd7016a825db7e1  
**Source repository:** KitvisetLabs/UQPU-GPU-Replacement-Research  
**Source branch:** research/2026-10-25-transformer-formula-benchmark  
**Source branch head SHA:** f7ff45e4bc0164c7a842d20ab1833096b4cc1a6e  
**PR:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/98  
**Status:** PENDING_REVIEW / NOT_MERGED_TO_MAIN

## Objective and change summary

The two source-branch commits add:
- software/uqpu-prototype/uqpu/formula_discovery_benchmark.py
- software/uqpu-prototype/tests/test_formula_discovery_benchmark.py
- docs/literature_watch/2026-10-25-transformer-physics-formula-synthesis.md
- docs/RESEARCH_GAP_RG046_TRANSFORMER_FORMULA_GENERALIZATION.md
- docs/BATCH_064_TRANSFORMER_FORMULA_DISCOVERY_GENERALIZATION.md
- integration/INT-20261025-021-TRANSFORMER-FORMULA-GENERALIZATION.json
- benchmarks/results/formula-discovery-benchmark-contract-smoke-2026-10-25.json

The work responds to the official arXiv v1 preprint arXiv:2610.03947, submitted 2026-10-02. The paper reports fast formula synthesis and improved extrapolation on selected benchmark tasks, but also a scale-shift failure regime and substantial reported model-training resources. The new helper enforces a fair-comparison metadata contract; it does not reproduce the external model or certify physical truth.

## Validation and current CI state

- Local synthetic contract tests: 15/15 pass under Python 3.13.
- Main starting SHA 70796ef8b918fe2e95382bc49cd7016a825db7e1: Prototype/Invariants workflow and Cold-Start Handoff Audit passed.
- Updated PR head f7ff45e4bc0164c7a842d20ab1833096b4cc1a6e passed the Python 3.10/3.11/3.12 test matrix. Extended QSP/QSVT, reference-benchmark and Qiskit workflows remain in progress, so no full-workflow pass is claimed yet.
- No model weights downloaded, external benchmark reproduced, paid QPU job submitted, physical experiment performed, fabrication/purchase/funding action authorized, or physical law promoted.

## A–H and invariant effects

- A: adds a reusable equation-discovery comparison contract; no QPU/workload advantage.
- B: no provider integration or execution changes.
- C: records peak memory, tokens and optional energy; no memory-replacement claim.
- D: no device/process/packaging evidence.
- E: no Pangola material, accepted bio-oil or net-fusion-electricity evidence.
- F: owns the benchmark/evidence contract and RG-046.
- G: training resource provenance can inform future equipment/factory models; no fabrication result.
- H: publishes the dated watch and links training amortization to FIN-001.
- INV-029: no physical data-center-to-phone compression.
- INV-030: no critical-material substitution or elemental transmutation.
- INV-031: BIO-001 remains open; no accepted-fuel cost evidence.
- INV-032: FUS-001 remains open; no reliable net-electricity/lifecycle-cost evidence.
- INV-033: model training resource accounting is now explicit, but dollar costs, amortization volume and financing-rate effects are unmeasured.
- INV-034/035: expands equation-candidate generation while retaining incumbent constraints, held-out tests, counterexamples, experiments and independent validation.

## Canonical sync debt

The code and detailed research artifacts remain on the PR branch until review/merge. This main-branch record is a discoverability summary only; it does not imply that the branch files or results have been merged. Do not rewrite the large append-only RESEARCH_GAPS.md or WORKLOG.md from partial history. After PR CI completes, review the exact head, reconcile any base drift, and record the final source-SHA → main-SHA mapping only if merged.

**Next gate:** inspect current-head Python 3.10/3.11/3.12 and project workflow results; then require pinned source/model/data hashes, verified row-level split disjointness, ≥30 seeds per arm, matched budgets and training-plus-inference cost per accepted formula before any scientific promotion.

Research-Sync: main
