# Batch 083 — AI-generated proof structure and equation-discovery evidence gates

**Date:** 2026-10-28  
**Canonical starting head:** `aa35c5908ff412971f8a7f52b78fb596f45f4d8f`  
**Primary owner:** Lane A — formal/equation evidence tooling  
**Cross-lane owners:** Lane F — evidence/resource economics; Lane H — literature/publication  
**Evidence classes:** `LITERATURE_ONLY`; proposed diagnostic remains unimplemented  
**Status:** Source-pinned research delta and falsifiable gap; no new theorem, physical law or technology advantage claimed

## Research question

Can proof-structure measurements add useful diagnostics to AI-assisted equation discovery while preserving the separation among formal correctness, proof efficiency, mathematical novelty, physical-model adequacy and engineering value?

## Literature delta

Aryal, “Studying proof data with proof theory: the case of AI-generated mathematics,” arXiv:2610.25357 (2026-10-18), analyzes proof-term structure, redundancy and compression in selected formal-proof corpora. The author reports lower realized proof compression and more removable intermediate claims for one AI-generated corpus than for Mathlib; some differences change after controlling for automation. These are preprint-reported corpus results, not UQPU measurements or universal properties of AI-generated proofs.

The new watch is `docs/literature_watch/2026-10-28-ai-proof-structure-compression-audit.md`; focused gap RG-048 is `docs/RESEARCH_GAP_AI_PROOF_STRUCTURE_METRICS_2026-10-28.md`.

## Research decision

Do not add an unverified proof-compression score to the current equation-candidate acceptance rule. The next safe step is to reconstruct the source metrics and establish positive/negative controls against a pinned proof corpus and toolchain. The existing exact-byte `formal_proof_evidence.py` contract remains unchanged. Proof efficiency is optional diagnostic metadata; it cannot upgrade `KERNEL_CHECKED` to `INDEPENDENTLY_REPRODUCED`, certify novelty, or validate a physical model.

## A–H status

- **A — Quantum programming/workloads/compiler/runtime (Priority #1):** RG-EQN-008 remains the canonical matched equation-discovery interface; DIGEST, MOSAIC-SR, STRIDE and other methods remain candidate arms, not reproduced winners. RG-048 proposes a proof-structure audit downstream of the existing formal-proof byte-binding contract.
- **B — Cloud/QPU/provider integration:** provider-neutral adapters and no-submit posture retained. No paid or free hardware job was submitted or authorized.
- **C — RAM/VRAM/HBM/storage/state/data movement:** keep proof bytes, proof AST counts, quantum state, readable classical memory and transfer costs distinct. No memory/storage replacement evidence.
- **D — Device/chip/process/packaging:** no device or fabrication evidence changed.
- **E — Biomass/materials/bio-oil/fusion/cooling:** BIO-001 still lacks Pangola-specific accepted-liquid mass/energy/quality/cost closure; FUS-001 remains literature-derived sensitivity/accounting work, not net-electric or commercial-cost evidence.
- **F — Economics/benchmarks/evidence/integration:** resource accounting should include proof generation/checking, retries, host compute, memory and energy when measured; no accepted-task cost advantage was measured.
- **G — Manufacturing equipment/software/factory systems:** D/G co-design remains mandatory; no process-window, yield or cost-per-good-device result.
- **H — Kanusanan Pongpanna Model, finance and publication:** publish the dated source watch and preserve the Thai, English, Chinese, Japanese, Korean and German public master-plan links and strategic AI-agent/funding references.

## Foundational and permanent-invariant status

- **FND-001:** quantum-feedback/work/precision literature remains assumption-scoped; no UQPU thermodynamic or wall-plug measurement.
- **FND-002:** output-information lower-bound path remains distinct from Hilbert-space dimension and readable storage; no new result.
- **FND-003:** matched control-versus-quantum-speed-limit and quantum-feedback TUR reproduction remain open; no matched physical measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new QFT/elementary-particle mechanism validated.
- **FND-006 / EQN-001–006:** formal proof provenance remains distinct from empirical physical-law status; RG-048 adds a proposed proof-structure metric reconstruction gate, not a new equation.
- **INV-029:** Data-Center-to-One-Phone remains an unachieved physical-compression goal; US$10T–US$100T remains an ambition-scale proxy.
- **INV-030:** no elemental transmutation and no demonstrated Pangola-carbon functional substitution.
- **INV-031:** no commercial ultra-low-cost bio-oil/fuel result.
- **INV-032:** no commercial fusion or reliable net-delivered-electricity cost result.
- **INV-033:** no measured reduction in financed principal, absolute interest, risk premium or WACC from a project intervention.
- **INV-034/035:** frontier search remains open; current physical laws bind engineering claims and AI-generated equations require falsification and independent validation.
- **INV-025/026/027:** 100,000,000-GPU and universal 100,000,000-unit moonshots remain falsifiable targets; no qubit-count/readable-memory equivalence or 100x/100,000,000x economic result is claimed.

## Validation and synchronization

The previous core workflow #1818 completed with 15/15 jobs successful on parent commit `2a44518c2738070dbf72eec6f29179b7f3bfbad1`; cold-start audit #1026 also passed on that parent. The handoff-sync head `aa35c5908ff412971f8a7f52b78fb596f45f4d8f` had no combined status entries when inspected, so parent success is not treated as exact-head validation. This documentation-only batch does not claim local code tests or a fresh hosted CI result.

The large append-heavy `RESEARCH_GAPS.md` and `WORKLOG.md` are not rewritten from partial snapshots. RG-048 is published as a focused gap; aggregate reconciliation remains a separate sync task. No paid QPU job was submitted.

## Next highest-value gate

Pin and reconstruct the source's proof-structure metric definitions, then validate them on a small proof corpus with matched theorem strata, a fixed Lean/Mathlib toolchain, known shared-lemma and redundant-claim controls, and a held-out sample. Only after that gate passes should optional diagnostics be added to the formal-proof evidence interface. In parallel, continue the existing Lane A matched equation-discovery comparison and Lane E/F BIO-001/FUS-001 accounting gates.
