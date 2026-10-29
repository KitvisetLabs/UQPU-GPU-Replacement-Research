# Batch 124 — exact-statement cross-split leakage guard

**Date:** 2026-10-29  
**Starting main SHA:** 3ac90c6697029f3c8e636640f4a5b36983f53157  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** Lane F — split integrity and accepted-result economics; Lane H — provenance/literature; INV-034/035 and FND-006  
**Evidence class:** SOFTWARE METADATA CONTRACT + SYNTHETIC REGRESSION TEST ADDED  
**Paid QPU execution:** not authorized or attempted

## 1. Starting-state audit

Resolved the current main head dynamically rather than assuming a batch number. Inspected the charter, version invariants, goals, README, research operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, permanent root directives 00/00A/01–06, Batch 123, its focused gap and integration report, the proof-DAG validator/tests, current FND-006 proof-reuse gaps, research-lane architecture, and latest available CI/status records.

INV-025/026/027, INV-029–035, the eight-lane A–H architecture, the six public Thai/English/Chinese/Japanese/Korean/German strategic-plan links, and recorded strategic AI-agent/funding context remain preserved.

## 2. Lane A change: exact statement identity across splits

Batch 123 rejected invalid dependency edges between held-out splits, but a separate metadata edge case remained: two different claim-family IDs could carry the exact same `statement_sha256` in different splits. The family-to-split check would not detect that overlap because the family identifiers differ.

The proof-DAG validator now maintains a statement-digest-to-split map and fails closed when the same exact statement digest appears in more than one of `train`, `validation`, and `test`. A synthetic regression test covers a train/test duplicate with distinct claim-family IDs. Existing parent-edge rules remain in force.

This is deliberately an **exact-byte identity guard**, not semantic theorem-equivalence detection. Different encodings, alpha-renaming, normalization differences, hidden shared assumptions, corpus contamination, or dishonest split manifests can still evade it. A hash identifies the bytes supplied; it does not authenticate the source or prove semantic independence.

## 3. Verification and CI

An isolated sanity check of the new split-map logic passed two cases: distinct digests across train/test are accepted, and an identical digest across train/test is rejected. This is not the repository's unit suite.

The repository's full test suite was not run locally because this runtime cannot resolve GitHub for a fresh clone. The latest available combined-status query returned no status records, and the connector's commit-workflow lookup returned no workflow runs for the exact head. Therefore **exact-head GitHub Actions is unverified/pending**, not passed. No theorem kernel was run.

## 4. Literature surveillance delta

Fresh public surveillance revisited symbolic/neural-symbolic equation discovery, theorem generation and counterexample search, physics-informed/constitutive modeling, quantum thermodynamic limits, and workload/QUBO evidence. Repository searches showed that the currently relevant primary-source leads—including ProofEvolve (arXiv:2608.26334), SymbolFit v2 (arXiv:2607.19750, revised 2026-10-19), Learning to Disprove (arXiv:2603.19514v2, revised 2026-10-14), the physics-formalization perspective (arXiv:2610.14059), and the GraphED constitutive-law paper (*Science Advances*, 2026-09-11)—are already recorded in dated watch/gap artifacts. No new-to-repository primary result was found that changes this cycle's acceptance gate; no duplicate literature article was created.

These remain external source claims, not UQPU reproductions. No equation, theorem, physical law, or technology advantage was promoted.

## 5. Eight-lane status

| Lane | This-cycle disposition | Evidence class | Next gate |
|---|---|---|---|
| A — programming/workloads/compiler/runtime | Added exact statement-digest split guard and synthetic regression | Software contract; isolated logic check only | Exact-head CI, then pinned theorem-family corpus and kernel-checked reproduction |
| B — cloud/QPU/provider integration | Provider-neutral adapter paths retained; no paid or hardware job | Maintained / no target job | Simulator/dry-run and provider/target-paired quality-price evidence |
| C — RAM/VRAM/HBM/storage/state/data movement | No classical-memory equivalence inferred from proof-DAG or Hilbert-space size | No new measurement | Measure peak memory, state/I/O, transfer, reconstruction, host work and energy on matched workload |
| D — device/chip/process/fabrication/packaging | Device scope retained; no new physical-device evidence | No new measurement | Co-design target-native constraints with Lane G; record process window and measured yield |
| E — biomass/materials/bio-oil/fusion/cooling/infrastructure | BIO-001 and FUS-001 remain open; no material, accepted-fuel or net-electricity claim | No new commercial evidence | Pangola mass/energy/product acceptance and full accepted-liquid cost; net reliable delivered-electricity envelope |
| F — economics/benchmarks/evidence/integration | Exact statement overlap added to split-integrity gates | Metadata contract only | Equal-budget cost per independently accepted result, including failed/false discoveries and timeouts |
| G — manufacturing equipment/software/factory systems | D/G co-design retained; no factory measurement | No new measurement | Cost per good die/package, process-window, metrology and yield evidence |
| H — strategy/finance/publication | Literature deduplication and strategic preservation checked | Source triage / documentation | Preserve six-language links and agent/funding references; separate strategy from empirical finance claims |

INV-034 and INV-035 remain upstream cross-cutting requirements for all eight lanes. This cycle does not claim independent multi-agent execution.

## 6. Foundational physics and equation discovery

FND-001 thermodynamic-gap accounting, FND-002 output-information lower bounds, FND-003 matched control-versus-quantum-speed-limit measurement, FND-004 alternative physical primitives, FND-005 QFT/elementary-particle mechanism scans, and FND-006 mathematics-first invention remain active. EQN-001–006 and the repository's broader equation-discovery successors still require explicit incumbent assumptions, units, symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search, proof/simulation as applicable, a discriminating experiment, and independent validation.

The change contributes only to FND-006 evidence hygiene. It neither changes `fundamental_limits.py`, `frontier_hypothesis.py`, or `equation_discovery.py` nor produces a candidate physical equation. Current physical limits remain binding.

## 7. Permanent mission/invariant contribution

- **INV-029:** no physical Data-Center-to-One-Phone closure; remote infrastructure must still count toward the final boundary.
- **INV-030:** Pangola/agricultural-residue carbon remains a functional substitution/minimization/recovery/recycling/hybridization/redesign strategy; no elemental transmutation.
- **INV-031:** BIO-001 accepted liquid-energy/fuel cost remains open; crude bio-oil is not finished fuel.
- **INV-032:** FUS-001 net reliable delivered-electricity cost remains open; no commercial low-cost fusion claim.
- **INV-033:** no measured reduction in financed principal, absolute interest, project WACC, or economy-wide rates.
- **INV-034:** deep-frontier research remains constrained by explicit mechanisms, known limits, falsifiers and evidence gates.
- **INV-035:** AI may generate hypotheses; proof, physical validity, engineering consequence and economics remain distinct acceptance gates.
- **INV-025/026/027:** the 100,000,000-GPU and universal 100,000,000-unit moonshots remain unproven and workload/subsystem-contract dependent.

## 8. Open gaps and next highest-value gate

1. Obtain exact-head Actions for the validator and new regression test; do not infer CI success from a parent commit.
2. Pin an external theorem-family corpus, exact source/license, proof assistant/kernel, dependency lock and environment.
3. Freeze and audit split manifests; check both exact statement hashes and normalized/semantic equivalence where feasible.
4. Compare baseline proof search against schema reuse under equal compute/time budgets on theorem-family-disjoint held-out tasks.
5. Independently rerun held-out kernel-checked artifacts and record accepted results, residual premises, changed/invalid statements, failed and inconclusive proofs, timeouts, peak memory, wall time, energy where measurable, and cost per independently accepted result.

**Non-claims:** no formal proof was executed; no theorem novelty, new physical law, real-QPU advantage, material substitution, accepted bio-oil, net fusion electricity, financing-rate change, or mission-level economic/physical compression was demonstrated.

Research-Sync: main
