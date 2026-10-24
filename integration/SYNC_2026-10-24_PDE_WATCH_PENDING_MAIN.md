# Pending-main synchronization record — 2026-10-24 PDE and constitutive-model watch

**Status:** PENDING_MAIN / REVIEW_REQUIRED  
**Primary owner:** Lane H; integration routing by Lane F  
**Work items:** EQN-PDE-001; conditional MAT-CONST-001  
**Canonical main at source start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-formal-discovery-gates`  
**Source PR:** #66 — https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/66  
**Current source head:** `3b1136deba60eeb43ed665fc13f1ae10498928f7`  
**Prepared:** 2026-10-24 UTC  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_RESEARCH`  
**Main mapping:** NOT_MERGED; this record does not claim the source work is present on main.

## Source commits and process audit

This branch began at the main SHA above. Its source changes are:

- `5c7f57d84b12cceeda54ca04ec1ab180cb8518e0` — initial dated proof/witness-gated literature watch.
- `8f1330040c749d62b695402d072898535f381fa5` — added the cross-lane integration handoff. This commit omitted `Research-Sync: pending-main`; cold-start run 40080623614 correctly failed with `missing_commit_trailer:Research-Sync: pending-main`. This was a publication-process failure, not a scientific or unit-test failure.
- `d7b49ebf654fe9be52a0f564cff5eb24fd224f6a` — added the pending-main trailer and expanded the PDE-formalization source scan. Cold-start audit run 40081070377 passed.
- `17de18911f1a851e4b3b65e3e6e4c89d4f5386d2` — narrowed the article to a non-duplicative PDE-method delta and retained the pending-main trailer. Exact-head cold-start audit run 40081127695 passed.
- `3b1136deba60eeb43ed665fc13f1ae10498928f7` — added a separately scoped physics-informed alloy constitutive-model surveillance signal and conditional MAT-CONST-001 follow-up. This commit includes `Research-Sync: pending-main`; exact-head UQPU CI is still running.

**Latest exact-head CI snapshot for `3b1136d...`:** Python 3.10, 3.11 and 3.12 unit/invariant/CLI jobs passed. QSP phase synthesis, phase reconstruction, reference benchmark, target-snapshot identity and no-submit target transpilation passed on the same run. QSVT bounded-prefix/eight-query/ten-query, Qiskit verification and routed-probe jobs remained in progress at the latest poll; do not report a full CI pass yet.

The cold-start audit for the actual source commit `17de189...` passed, and the audit for the sync-record commit `cc2e346...` passed. A separate branch-creation event on the unchanged main SHA failed with `missing_commit_trailer:Research-Sync: pending-main`; its artifact shows all A–I manifests and 36 pair records passed. This is the known synthetic branch-creation defect tracked by PR #60, not a source-commit failure. PR #60 was updated with this reproduction; its fix remains unmerged.

## Research change

The current Lane H-owned literature artifact is `docs/literature_watch/2026-10-24-proof-and-witness-gated-discovery.md`. It records two distinct third-party method signals:

1. Wuyang Chen, “Verifiable PDE Reasoning and Modeling with Neurosymbolics,” IJCAI 2026 Early Career Spotlight, DOI 10.24963/ijcai.2026/903.
2. Prashil S. Joshi, Diksha Mahadule and Rajesh K. Khatirkar, “Physics-Informed Residual Deep Learning for Constitutive Modeling of Hot Deformation and Dynamic Recrystallization in a Mo-Rich α+β Titanium Alloy,” arXiv:2607.13467, submitted 2026-07-15.

The first motivates `EQN-PDE-001`: an offline manufactured-solution benchmark with a hidden hand-checked oracle, dimensional and boundary checks, residual/convergence tests, held-out regimes, counterexample fixtures and full resource accounting. The second motivates conditional `MAT-CONST-001` only after a specific material/process and qualified data are selected. Neither source establishes a UQPU result, new physical law, Pangola material property, manufacturing yield, commercial fuel/electricity or economic advantage.

This item remains distinct from the companion AI-mathematics-ranking/proof-verification work in PR #65. It does not copy that branch's code or claim its implementation is merged.

## Changed source paths

- `docs/literature_watch/2026-10-24-proof-and-witness-gated-discovery.md` — PDE formalization and physics-informed constitutive-model surveillance.
- `integration/2026-10-24-formal-discovery-gates.md` — A–H cross-lane handoff, FND/EQN/BIO/FUS/FIN routing and evidence boundaries.

No canonical append-only `WORKLOG.md`, `RESEARCH_GAPS.md` or scoreboard history was replaced from a partial read. This synchronization record is additive and under 16 directory levels.

## Lane and invariant effects

- **A (Priority #1):** proposes claim-aware offline verification; current QOS/QSVT and real-target gates are unchanged.
- **B:** no provider call, target snapshot or paid job; provider/target/pricing provenance rules remain binding.
- **C:** state/I/O/serialization/reconstruction must be accounted for; no Hilbert-space-to-classical-memory equivalence.
- **D/G:** PDE/constitutive-derived device/process requirements need measurable observables and D/G co-design; no fabrication or yield result.
- **E:** no Pangola material, accepted bio-oil, fuel, net fusion electricity or cooling measurement.
- **F:** validation compute/time-to-evidence must be counted; no project WACC or macro interest-rate claim.
- **H:** preserves the Kanusanan Pongpanna Model and Thai/English/Chinese/Japanese/Korean/German strategic references.
- **Lane I:** the repository's additional field-agnostic vehicle lane remains separate and contract-only; this research gives it no lift/propulsion evidence and does not replace A–H.

**INV-029:** no phone-class physical compression demonstrated.  
**INV-030:** no elemental transmutation or functional material substitution demonstrated.  
**INV-031:** no commercial bio-oil/fuel result.  
**INV-032:** no commercial fusion/net-electricity result.  
**INV-033:** no measured principal, interest, WACC or macro-rate effect.  
**INV-034:** formal-to-solver research path proposed; no new fundamental result.  
**INV-035:** alternative equations remain hypotheses until constraints, held-out tests, falsification and independent validation pass.

INV-025/026/027 remain unchanged and evidence-gated. The 100× and 100,000,000× goals remain unverified.

## Sync debt and next action

**Sync debt:** all source changes above remain outside canonical `main` until PR #66 (or a reviewed equivalent) is merged. This record itself is a separate PR so the canonical branch can discover the pending work without falsely treating it as merged.

Next actions:
1. Recheck exact-head CI for `3b1136d...`; all QSVT/Qiskit/routed-probe jobs must finish without failure.
2. Review PR #66 and this sync-record PR separately; do not merge on the strength of literature alone.
3. Review PR #60's branch-creation-event fix and merge only after required checks; preserve full audits for actual commits.
4. If accepted, merge with the required `Research-Sync: main` trailer and record the resulting main SHA against every source SHA.
5. Implement EQN-PDE-001 only as a deterministic offline benchmark. Consider MAT-CONST-001 only after a specific candidate material/process and qualified data are available.
6. Reconcile outstanding branch/fork commits only within registered and accessible scope; do not claim exhaustive history coverage.
