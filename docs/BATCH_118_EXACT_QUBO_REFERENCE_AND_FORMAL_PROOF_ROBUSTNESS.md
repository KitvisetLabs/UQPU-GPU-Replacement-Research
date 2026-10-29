# Batch 118 — exact QUBO references and formal-proof robustness

**Date:** 2026-10-29  
**Starting main SHA:** bdcecb4f0fc375e5020ee4dcf67c2a39a90de93c  
**Primary work owners:** Lane A (small-QUBO reference) and Lane H/FND-006 (formal-proof literature gate)  
**Cross-lane interfaces:** B provider routing; C state/data movement; D/G device and manufacturing co-design; E materials/energy; F economics/evidence; H strategic publication  
**Cross-cutting:** INV-025–035, FND-001–006, EQN-001–006, BIO-001, FUS-001, FIN-001  
**Evidence class:** REPRODUCIBLE SOFTWARE REFERENCE + REGRESSION TESTS; OFFICIAL ICLR 2026 LITERATURE; NO APPLICATION OR HARDWARE RUN  
**Paid QPU execution:** not authorized or attempted

## 1. Starting-state integrity

Re-resolved `main` from the newest committed state rather than a fixed batch number. Reviewed the project charter, version invariants, goals, README, operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, Batch 117 and Batch 116, the matched RAG gap, FND-006 reproduction gap and current Actions runs. All six language master-plan links (Thai, English, Chinese, Japanese, Korean and German) remain in `STRATEGIC_PLAN_REFERENCES.md`. No permanent root directive was removed or rewritten.

At the starting head, the UQPU prototype/invariant workflow and autonomous cold-start handoff audit both reported success. The new commit must be checked separately.

## 2. Lane A implementation — small-QUBO reference certificate

Added `software/uqpu-prototype/uqpu/qubo_reference.py` and regression tests. The helper exhaustively evaluates all (2^n) assignments for (n le 20), fixes one upper-triangle QUBO convention, parses decimal coefficients deterministically, preserves all tied minima, and emits SHA-256 hashes for both the normalized problem and certificate. It rejects duplicate terms, noncanonical index order, invalid coefficients, invalid indices and oversized instances.

The local self-test covered a unique optimum, tied optima, decimal summation, term-order/hash invariance and validation errors. The committed unit tests cover the same boundaries. This is an exact objective reference for small declared QUBOs, not a proof of feasibility for constraints external to the QUBO.

**Application boundary:** the real RAG manifest, group-disjoint query split, embeddings, objective hashes and downstream quality thresholds are still missing. Batch 117 remains PREREGISTERED_NOT_RUN. No CPU/GPU comparison, p-DCIM execution, QAOA simulation or real-QPU run is claimed by this helper.

## 3. Fresh literature surveillance — formal proof robustness

The search surfaced the official ICLR 2026 proceedings paper **“EvolProver: Advancing Automated theorem proving by Evolving Formalized Problems via Symmetry and Difficulty”**:
https://proceedings.iclr.cc/paper_files/paper/2026/hash/5dd362ce4612db239b1b755d86819ef6-Abstract-Conference.html

The reported method evolves formal theorem data using AST-level syntactic symmetry, semantic-domain translations and difficulty changes. The source reports pass@32 metrics on several formal-math benchmarks. The genuine UQPU relevance is to test whether formal equation-discovery/proof pipelines survive equivalent reformulations and held-out theorem families. The limitations and falsifiable follow-up are recorded in the new [literature watch](literature_watch/2026-10-29-evolprover-formal-proof-robustness.md) and [FND-006 gap](RESEARCH_GAP_FND006_EVOLPROVER_FORMALIZATION_ROBUSTNESS_2026-10-29.md).

Fresh searches also rechecked LLM-PySR search control (arXiv:2607.04156) and physics-constrained constitutive-model inspection (arXiv:2605.23754); these already have canonical watch coverage, so no duplicate articles were created.

## 4. Explicit A–H status

- **A — advanced:** deterministic small-QUBO objective oracle, hashable certificates and regression tests; RAG application remains blocked on real frozen manifests.
- **B — reviewed/maintained:** provider-neutral routes remain intact; simulator/dry-run first; no credentials or paid QPU job assumed.
- **C — interface clarified:** QUBO coefficient/objective hashes and exact small-instance state enumeration are now reproducible; this is not readable-memory or general RAM/VRAM/HBM/storage replacement.
- **D — maintained:** no new device fabrication or yield evidence; continue device/package co-design against measurable functions.
- **E — reviewed:** no new Pangola-carbon, accepted bio-oil, fusion net-electricity, cooling or infrastructure result.
- **F — advanced:** explicit objective-reference and evidence-boundary gap; total accepted-task economics remain unmeasured.
- **G — maintained with D/G co-design:** no fab-tool, process-control, yield or cost-per-good-package result is inferred from external roadmaps.
- **H — advanced:** new ICLR literature watch and FND-006 robustness gap; the strategic model and multilingual public links remain canonical context.

## 5. INV-029 through INV-035 and foundational paths

- **INV-029:** no physical compression milestone. Full external compute, memory, networking, energy, cooling and lifecycle costs remain in the eventual boundary.
- **INV-030:** no elemental transmutation or carbon-material substitution claim.
- **INV-031:** no accepted liquid fuel or commercial bio-oil cost result.
- **INV-032:** no net delivered fusion-electricity or lifecycle-cost result.
- **INV-033:** no financed-principal, interest-expense or WACC improvement measured.
- **INV-034:** FND-006 gains a falsifiable formal-robustness literature lead; FND-001–005 are maintained without new physical-bound claims.
- **INV-035:** AI-generated candidates remain hypotheses; proof correctness, physical validity, independent experiment and engineering economics are separate gates.

EQN-001 literature surveillance is updated. EQN-002/003 can use the exact QUBO oracle as a reference-design pattern. EQN-004/005 remain speculative and evidence-gated; EQN-006 remains blocked on independent formal/physical validation. BIO-001, FUS-001 and FIN-001 receive no new measured commercial evidence.

## 6. Current gaps and next highest-value gate

1. Freeze a versioned RAG workload manifest: query groups, candidate passages, embedding/configuration hashes, context budget, QUBO terms, objective/feasibility contract and downstream answer acceptance margins.
2. Independently recompute and verify the small-instance QUBO certificate; compare CPU/GPU and QAOA simulation using identical problem hashes.
3. Keep exact objective, external feasibility, answer quality and full-stack cost as distinct gates.
4. For FND-006, pin a proof environment and run AST-equivalent transformations plus held-out theorem-family/difficulty tests; retain all failed, timed-out and semantically invalid cases.
5. Query Actions on this exact new head and repair feasible failures without promoting a green software test to a scientific result.

## Non-claims

No QPU execution, quantum advantage, 100x/100,000,000x economics, universal subsystem replacement, new physical law, material substitution, accepted bio-oil, net fusion electricity, reduced WACC or Data-Center-to-One-Phone completion is established.
