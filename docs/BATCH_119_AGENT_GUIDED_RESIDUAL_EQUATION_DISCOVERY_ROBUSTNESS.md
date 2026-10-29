# Batch 119 — agent-guided and residual-informed equation-discovery robustness

**Date:** 2026-10-29  
**Starting main SHA:** eaeb31118dce65cb37ee95bf93ab748b43af7b46  
**Primary owners:** Lane A for matched-error software contract; Lane H / FND-006 for literature surveillance  
**Cross-lane interfaces:** B provider routes; C data/state/memory; D/G device/manufacturing co-design; E materials/energy; F economics/evidence; H strategic publication  
**Evidence class:** SOFTWARE CONTRACT + REGRESSION TESTS + OFFICIAL PREPRINTS; EXTERNAL REPRODUCTION NOT RUN  
**Paid QPU execution:** not authorized or attempted

## 1. Canonical starting state

Resolved the newest main commit dynamically and read the project charter, version invariants, goals, README, Research Operating System, Open-Frontier Directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, latest Batch 118/117/116, living research gaps, foundational/equation-discovery modules and current Actions state. The starting head had successful UQPU prototype/invariant and autonomous cold-start handoff workflows. Thai, English, Chinese, Japanese, Korean and German public master-plan references remain intact.

No permanent root directive or invariant was removed or weakened. INV-025/026/027 remain evidence-gated; INV-029–035 remain permanent.

## 2. Fresh literature delta

Official arXiv surveillance surfaced two recent method papers not yet represented by source-specific project watches:
- LegoSR, posted 2026-10-24, uses a common Equation Intermediate Representation across seven solvers and an adaptive agent with experiment memory.
- RISR, posted 2026-10-08, uses pointwise residual structure to guide equation proposals and correction ranking.

Reported benchmark scores remain third-party claims. The method-level novelty is the combination of reusable candidate representation/experiment records and residual-informed search. Neither establishes physical truth, a new physical law or UQPU advantage. The new literature watch records sources, dates, limitations and a falsifiable follow-up.

## 3. Lane A implementation

Added a dependency-free matched held-out error helper and regression tests. It rejects train/validation/test group leakage; requires identical case IDs, at least three matched cases and SHA-256 provenance digests; reports per-case and mean candidate-to-baseline error ratios; and blocks the metric gate if mean error does not improve, any case regresses beyond the declared tolerance, or any equivalence status is not CHECKED_EQUIVALENCE.

This is a metric gate only. The helper does not verify a caller-supplied equivalence status, parse equations, run symbolic regression or establish physical validity. External papers, datasets and checkpoints were not run.

## 4. A–H status

- **A — advanced:** matched-error/group-split helper with synthetic regression tests; no external benchmark run.
- **B — maintained:** provider-neutral lowering and target-specific evidence remain separate; no new adapter or paid job.
- **C — clarified:** grouped data leakage is guarded; bytes, state preparation, transfer, memory and reconstruction remain separate cost terms.
- **D — maintained:** no device fabrication or new physical measurement; device/process claims remain evidence-gated.
- **E — maintained:** no new Pangola-carbon substitution, accepted bio-oil, net fusion electricity or cooling result.
- **F — advanced at contract level:** matched errors and worst-case regression are explicit; economics, energy and financing are unmeasured.
- **G — maintained with D/G co-design:** no yield, metrology, process-window or cost-per-good-package result is inferred.
- **H — advanced:** source-specific literature watch and reproduction gap published; strategic-finance and multilingual references preserved.

All 28 A–H pairings were reviewed in the integration report. Meaningful links are A–F, A–H, C–F, D–G, E–F and F–H; other pairs remain maintained without forced coupling or new evidence.

## 5. Foundational and equation-discovery paths

- FND-001: measured energy versus scoped thermodynamic floors remains required; no new physical energy measurement.
- FND-002: output-information bounds and exact small-instance references remain active; no general readable-memory claim.
- FND-003: matched control-versus-quantum-speed-limit measurements remain open; no new control experiment.
- FND-004: alternative physical primitives remain hypothesis-scoped and constraint-bound.
- FND-005: QFT/elementary-particle mechanism scans remain causal-chain and falsifier gated.
- FND-006: advanced at methodology/metric-contract level through grouped holdouts and matched errors; no external solver reproduction.
- EQN-001: literature watch updated; EQN-002/003: matched cross-method evaluation is a benchmark pattern, not an observed gain; EQN-004: counterexamples and worst-case regressions remain required; EQN-005: no change to the established-physics escalation gate; EQN-006: no device/system/economic consequence is inferred.

## 6. INV-029 through INV-035 and energy/finance pillars

- **INV-029:** no physical-compression milestone; external infrastructure remains inside the eventual service, energy, physical and lifecycle-cost boundary.
- **INV-030:** no elemental transmutation or Pangola-carbon substitution claim.
- **INV-031:** no accepted saleable liquid fuel or commercial-cost result; BIO-001 remains open.
- **INV-032:** no net reliable delivered fusion-electricity result; FUS-001 remains open.
- **INV-033:** no financed-principal, absolute-interest or WACC improvement measured; FIN-001 remains open.
- **INV-034:** mathematics-first research continues under mechanism, constraints and falsification gates.
- **INV-035:** AI/residual-guided methods generate hypotheses; held-out evidence, counterexamples, independent validation and experiments govern stronger claims.

The 100x and 100,000,000x targets, universal subsystem replacement and Data-Center-to-Phone remain goals. No paid QPU job was submitted.

## 7. CI and next gate

Starting-head workflows were green. Exact-head Actions for the new commit must be inspected separately; the commit message includes the required Research-Sync: main trailer.

Next highest-value gate: run the helper's synthetic tests in Actions, then pin the two source implementations and a known-equation benchmark. Preregister grouped splits, equal candidate/time/compute budgets, pointwise relative-error tolerances, equation complexity, interval calibration, counterexample handling and ID/OOD reporting before accepting external results.
