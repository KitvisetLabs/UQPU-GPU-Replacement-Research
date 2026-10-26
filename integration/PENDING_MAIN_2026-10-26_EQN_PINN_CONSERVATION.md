# Pending-main sync record — EQN-PINN-CONSERVATION-001

**Status:** PENDING REVIEW; summary-only; source artifacts are not yet canonical main  
**Date:** 2026-10-26  
**Canonical base SHA:** c9880f2bcca274ed36fe19f83b91e7c91e41b400  
**Source PR:** [#128 — Oct 26 cycle: conservative PINN and model-discrepancy validation gate](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/128)  
**Source branch:** `research/2026-10-26-eqn-pinn-conservation-watch`  
**Source head:** `9f9b251134b1def4897407a41c9794a88bc92a49`

## Source commits and artifacts

- `70fb839a94d8ad8031e22f8721967eeb9bd7f33e` — `docs/literature_watch/2026-10-26-conservative-pinns-model-discrepancy.md`
- `06f344e3b07be57c5e77a7db01c34d2e93e0db2b` — `docs/RESEARCH_GAP_EQN_PINN_CONSERVATION_001.md`
- `1ae902b437ae5cbbb923514e8f93019176a433a9` — `research_lanes/A_quantum_programming_runtime/EQN_PINN_CONSERVATION_BENCHMARK_CONTRACT.md`
- `25e16735da7fb1d24b9a08178ba0876d64edbde3` — `integration/INT-20261026-EQN-PINN-CONSERVATION.json`
- `9f9b251134b1def4897407a41c9794a88bc92a49` — `integration/DAILY_CYCLE_2026-10-26_EQN-PINN-CONSERVATION.md`

## Research summary

The source PR records two peer-reviewed numerical-method papers: (1) Chomalí-Castro et al., *Physical Review D* 114, 076013, published 2026-10-07, DOI 10.1103/shpm-ksq9, on flux-conservative BDNK diffusion and PINN vs finite-volume comparisons; and (2) Zhang, *Physical Review Fluids* 11, 104602, published 2026-10-06, DOI 10.1103/rn1j-32n4, on RANS reconstruction with exact advection/production terms, an explicit inadequacy term and realizability constraints.

The proposed work item EQN-PINN-CONSERVATION-001 preregisters a falsifiable matched comparison among a conventional finite-volume reference, an unconstrained PINN, a constraint-aware PINN and a constraint-plus-discrepancy variant. It requires source provenance, smooth/discontinuous/held-out cases, conservation/admissibility checks, matched budgets and independent replay. No reproduction has yet been performed.

## Evidence and invariant boundary

- Evidence class: LITERATURE_ONLY / DESIGN_ONLY.
- Integration JSON parsed successfully from the source branch.
- No repository Python tests or solver reproduction were run.
- No quantum advantage, real-QPU result, new physical law, material substitution, accepted biomass fuel, net fusion electricity, financing benefit or Data-Center-to-One-Phone compression is claimed.
- INV-025/026/027 and INV-029–035, root directives 00/00A/01–06, the Kanusanan Pongpanna Model, all six multilingual public master-plan editions and D/G co-design remain preserved.
- Large append-only README.md, WORKLOG.md and RESEARCH_GAPS.md remain unchanged.

## CI and next action

The combined-status query for the canonical base returned no entries, so starting-head CI was UNKNOWN, not PASS. The source PR's exact-head hosted checks must complete before review/merge. Once PR #128 is merged, reconcile every source SHA to the resulting main SHA and update the pending status without claiming a merge prematurely.

**Next gate:** source-exact model/data acquisition and an independent evaluator; preserve null results and reject any method advantage that fails held-out, conservation/admissibility or matched-budget criteria.

Research-Sync: pending-main
