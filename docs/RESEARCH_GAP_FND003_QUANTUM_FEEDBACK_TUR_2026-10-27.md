# Research gap — FND-003 quantum-feedback TUR reproduction and precision-cost boundary

**Gap ID:** RG-FND003-QUANTUM-FEEDBACK-TUR-REPRODUCTION-001  
**Opened:** 2026-10-27  
**Primary owner:** Lane A — equation reconstruction and finite-dimensional reference  
**Measurement/economics owner:** Lane F  
**Publication owner:** Lane H  
**Related:** FND-001, FND-003, FND-006, EQN-001–006, INV-034/035  
**Status:** OPEN — primary-source equations pinned; no independent reproduction or UQPU implementation

## Objective

Reproduce the finite-time thermodynamic uncertainty relation for monitored quantum jumps with Markovian feedback from Honma and Vu, then determine whether any later device-level application can be measured without conflating entropy production, mutual information, intrinsic work, wall-plug energy, latency, or monetary cost.

## Pinned source and result

- Honma and Vu, *Physical Review Letters* 137, 160406 (published 2026-10-16), DOI 10.1103/6d8l-94pv.
- Official preprint: arXiv:2602.22651v2 (revised 2026-10-22; PDF dated 2026-10-23).
- Primary-source watch: \`docs/literature_watch/2026-10-27-quantum-feedback-tur-precision-cost.md\`.
- The paper's model includes a finite-dimensional system weakly coupled to a thermal environment, monitored quantum jumps, instantaneous Markovian feedback, local detailed balance, and unital feedback maps. The derivation sets \(\hbar=k_B=1\).
- Main result: \(\operatorname{Var}[J]/\langle J\rangle^2 \geq 2(1+\delta_J)^2/\Sigma\), with \(\Sigma=S_{\mathrm{tot}}-I\geq0\) and a nontrivial auxiliary-dynamics correction \(\delta_J\). The short-time rate bound and activity-refined bound are separate checks.

## Why this is a separate gap from Batch 080

Batch 080 addresses conditional work bounds when a controller has quantum side information. This gap concerns current precision/fluctuations under a specific monitored-jump and feedback model. The work bound and TUR are complementary but not interchangeable; neither is a direct computation-speed, wall-plug-energy, or accepted-task-economics result.

## Preregistered reproduction protocol

1. Freeze the APS version, arXiv v2, all parameter values, current definition and units before implementation.
2. Independently transcribe Eqs. 1–18, including the feedback master equation, local-detailed-balance condition, information term, tilted generator, auxiliary \(\phi\) dynamics and correction \(\delta_J\).
3. Implement the three-level clock model with two independent routes: (a) tilted-Liouvillian derivatives for cumulants and (b) a trajectory estimator with uncertainty intervals.
4. Test \(\Sigma\geq0\), Eq. 15 over finite durations, the short-time Eq. 17 limit, the no-feedback and classical limits, and Eq. 18 only if the dynamical-activity definition is independently reproduced.
5. Use held-out parameter combinations, numerical-step convergence, trajectory-count convergence and uncertainty intervals. A statistically supported violation, sign mismatch, or failure of the required limit is a failure, not a reason to adjust the theorem.
6. Record the failed cases and all source assumptions. Do not select only parameter regimes that satisfy the bound.
7. Keep entropy/information accounting separate from measured joules and currency. If later mapped to hardware, instrument measurement, control, actuation and reset at a named physical boundary.

## Acceptance gate

The gap is closed only when the independent implementation reproduces the source's finite-dimensional reference results and limiting cases, with a reproducibility manifest, tests, numerical tolerances and counterexample report. A source-matching simulation remains SIMULATION_ONLY/MODEL_ONLY; it does not establish a UQPU advantage or a new physical law.

## Mission relevance and exclusions

- FND-001/FND-003: strengthens the theoretical precision/thermodynamic-cost comparison only after reproduction.
- INV-034/035: follows a source-pinned, falsifiable, assumption-explicit equation-validation process.
- INV-029–033: no measurable contribution established; no phone-compression, critical-material substitution, accepted bio-oil, net fusion electricity, interest-rate or WACC claim.
- INV-025–027 and all permanent root directives remain binding. No paid QPU execution is authorized by this gap.
