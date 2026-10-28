# Research gap — Planckian quantum dynamical entropy rate

**Gap ID:** RG-FND001-PLANCKIAN-ENTROPY-RATE-REPRO-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane F — evidence/reproduction gate  
**Cross-lane owners:** Lane H (literature surveillance), FND-001 (thermodynamic/information accounting), FND-003 (speed-limit boundary)  
**Status:** OPEN / LITERATURE_ONLY / NO_UQPU_REPRODUCTION  
**Source:** docs/literature_watch/2026-10-28-planckian-quantum-dynamical-entropy-bound.md

## Objective

Independently test the paper’s explicit rate formula and the restricted Planckian bound for its stated continuous-monitoring scheme, while keeping the broader universal bound labelled conjectural.

## Blockers

- No UQPU implementation or independent reproduction of the Keldysh/retarded Green-function integral exists yet.
- The thermodynamic and long-time limits must be approximated through finite-size/time-step scaling with uncertainties; a finite simulation cannot directly prove a universal limit.
- The broad conjecture extends beyond the specific Gaussian mesoscopic-observable scheme for which the paper derives its explicit bound.
- The information-gain rate is not a computation runtime, Landauer heat, wall-plug energy or cost/task measurement.

## Unlock protocol

1. Pin arXiv:2507.20914v5 and the peer-reviewed DOI 10.1103/wd91-v58h; record equation numbers, units, normalization, observable scaling, measurement strength and source hashes.
2. Independently implement the rate integral and validate it on analytic limiting cases before matching published finite-size numerical results.
3. Reproduce the mixed-field Ising-chain calculation at L=6, 8, 10 with the published parameters and measurement protocol; report finite-size and time-step residuals.
4. Enforce the fluctuation-dissipation relation for the claimed tighter bound; separately label the looser bound obtained when it is ignored.
5. Test one predeclared extension across an operator class or temperature range away from thermal criticality. Record counterexamples and inconclusive cases.
6. Keep entropy rate, purification rate, heat, reset/controller energy and accepted-task wall-plug energy in separate ledgers.

## Acceptance and closure

Close only after an independent implementation, a source-pinned reproduction, dimensional/limiting-case checks and an explicit uncertainty/counterexample report. A numerical reproduction would validate only that calculation, not the universal conjecture. No FND-003 runtime limit, physical-law promotion, QPU advantage or fusion/economic claim follows automatically.
