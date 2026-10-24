# Pending-main synchronization record — 2026-10-24 PDE formalization watch

**Status:** PENDING_MAIN / REVIEW_REQUIRED  
**Primary owner:** Lane H; integration routing by Lane F  
**Work item:** EQN-PDE-001  
**Canonical main at source start:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-formal-discovery-gates`  
**Source PR:** #66 — https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/66  
**Current source head:** `17de18911f1a851e4b3b65e3e6e4c89d4f5386d2`  
**Prepared:** 2026-10-24 UTC  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_RESEARCH`  
**Main mapping:** NOT_MERGED; this record does not claim the source work is present on main.

## Source commits and process audit

This branch began at the main SHA above. Its source changes are:

- `5c7f57d84b12cceeda54ca04ec1ab180cb8518e0` — initial dated proof/witness-gated literature watch.
- `8f1330040c749d62b695402d072898535f381fa5` — added the cross-lane integration handoff. This commit omitted `Research-Sync: pending-main`; cold-start run 40080623614 correctly failed with `missing_commit_trailer:Research-Sync: pending-main`. This was a publication-process failure, not a scientific or unit-test failure.
- `d7b49ebf654fe9be52a0f564cff5eb24fd224f6a` — added a pending-main trailer and expanded the PDE-formalization source scan. Cold-start audit run 40081070377 passed.
- `17de18911f1a851e4b3b65e3e6e4c89d4f5386d2` — narrowed the article to a non-duplicative PDE-method delta and retained the pending-main trailer.

At record creation, the exact-head cold-start audit for `17de189...` was queued/in progress as run 40081127695. The UQPU test workflow for the preceding `d7b49...` commit had passed Python 3.10, 3.11 and 3.12 unit/invariant/CLI gates; the longer Qiskit/QSVT/reference jobs were queued or running. These statuses are not a full exact-head CI pass for `17de189...`; recheck hosted Actions before merge.

## Research change

The current Lane H-owned literature artifact is `docs/literature_watch/2026-10-24-proof-and-witness-gated-discovery.md`. It is deliberately scoped to Wuyang Chen, “Verifiable PDE Reasoning and Modeling with Neurosymbolics,” IJCAI 2026 Early Career Spotlight, DOI 10.24963/ijcai.2026/903, with the official proceedings URL preserved in the source artifact.

The actionable delta is an offline manufactured-solution benchmark proposal, `EQN-PDE-001`: compare formalized specifications and generated solver inputs with a hand-checked oracle; measure dimensions, boundary-condition compliance, residuals, convergence and held-out regimes; search for counterexamples; and retain proof/solver failures. A successful synthetic test remains computational evidence only. No physical law or UQPU capability is promoted.

This item is intentionally narrower than the companion AI-mathematics-ranking/proof-verification work in PR #65. It does not copy that branch's code or claim its implementation is merged.

## Changed source paths

- `docs/literature_watch/2026-10-24-proof-and-witness-gated-discovery.md` — current PDE-focused literature/method record.
- `integration/2026-10-24-formal-discovery-gates.md` — A–H cross-lane handoff, FND/EQN/BIO/FUS/FIN routing and evidence boundaries.

No canonical append-only `WORKLOG.md`, `RESEARCH_GAPS.md` or scoreboard history was replaced from a partial read. This synchronization record is additive and under 16 directory levels.

## Lane and invariant effects

- **A (Priority #1):** proposes a claim-aware offline verification subtrack; current QOS/QSVT and real-target gates are unchanged.
- **B:** no provider call, target snapshot or paid job; provider/target/pricing provenance rules remain binding.
- **C:** state/I/O/serialization/reconstruction must be accounted for; no Hilbert-space-to-classical-memory equivalence.
- **D/G:** PDE-derived device/process requirements need measurable observables and D/G co-design; no fabrication or yield result.
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
1. Confirm exact-head Actions for source SHA `17de189...`; cold-start audit must pass and all required UQPU tests must finish.
2. Review PR #66 and this sync-record PR separately; do not merge on the strength of literature alone.
3. If accepted, merge with the required `Research-Sync: main` trailer and record the resulting main SHA against every source SHA.
4. Implement EQN-PDE-001 only as a deterministic offline benchmark, with known-answer fixtures, held-out cases, counterexample witnesses, false-discovery ledger and resource accounting.
5. Reconcile outstanding branch/fork commits only within registered and accessible scope; do not claim exhaustive history coverage.
