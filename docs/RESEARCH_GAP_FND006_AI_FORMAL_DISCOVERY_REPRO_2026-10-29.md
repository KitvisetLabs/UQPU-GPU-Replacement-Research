# Research gap RG-FND006-AI-FORMAL-DISCOVERY-REPRO-001 — discovery, proof and physical meaning

**Opened:** 2026-10-29  
**Primary owner:** Lane H — strategy and research publication  
**Interfaces:** A (candidate generation/tooling), F (resource/evidence accounting), all lanes through INV-034/035  
**Status:** OPEN / PREPRINTS-ONLY / UQPU-REPRODUCTION-NOT-STARTED  
**Sources:** https://arxiv.org/abs/2610.22603 ; https://arxiv.org/abs/2610.08329 ; https://arxiv.org/abs/2610.14059

## Objective

Build a reproducible AI-assisted discovery protocol that separates (1) candidate novelty, (2) formal correctness under declared assumptions, (3) empirical/physical validity, (4) engineering consequence, and (5) mission economics. The objective is not to copy a preprint's claimed discovery, but to test whether the project's own equation-discovery workflow reduces false discoveries and time-to-evidence.

## Current evidence

The Busy Beaver preprint reports formally verified execution-acceleration rules for eleven BB(6) machines, with a mixture of novel discoveries, rediscoveries and proof cases. The Poincaré formalization preprint reports a milestone-driven AI/human formalization workflow for a known mathematical theorem. A physics-formalization perspective argues that proof checking alone does not guarantee that formal definitions match the intended physical semantics. These are external reports, not UQPU reproduction.

## Acceptance contract

- Freeze one synthetic known-law dataset and one independent held-out regime before search.
- Run candidate generators with equal compute/evaluation budgets; record candidate source, expression hash, units, domain, assumptions, constraints, training/held-out errors and search cost.
- Apply dimensional, symmetry, conservation, causality and limiting-case checks before candidate acceptance.
- Run counterexample search and classify outcomes as found, not found, or inconclusive; do not equate no counterexample found with proof.
- Bind formal proof status to exact source and theorem hashes, assumptions, proof assistant/version and kernel-check result. Record failed and undecided proofs.
- For physics-facing candidates, define a discriminating observable, held-out prediction, experiment/proof, independent replication path and the point at which engineering/economic consequences could be measured.
- Keep proof correctness, physical validity, device/system feasibility and economic advantage as separate gates.
- Track time and compute cost per candidate and per independently accepted result, including false discoveries and failures.

## Falsifiers and unlock criteria

The method fails its first gate if a candidate does not recover the known law within the declared tolerance, violates a required physical constraint, fails on the held-out regime, or cannot reproduce its proof-check record. Any physical claim remains blocked if it lacks a discriminating observable and independent experimental validation. A reduction in search cost is accepted only if measured under matched budgets and replicated runs.

## Next cheapest decisive experiment

Use a deterministic synthetic equation with known units, symmetry and limiting behavior; compare a plain symbolic-regression baseline with a staged constrained candidate pipeline. Do not use a speculative particle/QFT hypothesis as the first test. Preserve all failed candidates and proof failures.

## Nonclaims

No new physical law, theorem about nature, QPU advantage, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone result is established. Current physical equations remain binding for engineering claims.
