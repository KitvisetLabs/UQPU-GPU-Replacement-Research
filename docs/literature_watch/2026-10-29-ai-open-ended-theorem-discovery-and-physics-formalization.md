# Literature watch — open-ended AI theorem discovery and physics formalization

**Date checked:** 2026-10-29  
**Primary owner:** Lane H — literature surveillance/publication  
**Interfaces:** A (equation-discovery tooling), F (reproducibility/resource accounting), all A–H through INV-034/035  
**Evidence class:** OFFICIAL PREPRINTS / FORMALIZATION CLAIMS / NOT INDEPENDENTLY REPRODUCED BY UQPU  
**Related:** FND-006, EQN-001–EQN-006, INV-034, INV-035

## Sources and dates

1. Dos Santos, Veeriah, Havrilla, Bolt, Zuzic, Singh and Zahavy, “At the Limits of Computability: Steps Towards Autonomous AI Discovery on the Busy Beaver Frontier,” arXiv:2610.22603, submitted 2026-10-15: https://arxiv.org/abs/2610.22603
2. Zhang et al., “An AI-Assisted Formalization of the Poincaré Conjecture,” arXiv:2610.08329, submitted 2026-10-06: https://arxiv.org/abs/2610.08329
3. Krippendorf, Sarra and Tooby-Smith, “The Future of AI-assisted Physics: Discovering, Verifying and Organizing Results via Formalization,” arXiv:2610.14059, posted 2026-10-06 and updated 2026-10-15: https://arxiv.org/abs/2610.14059

## Genuine novelty

The Busy Beaver preprint reports an agent pipeline that combines pattern recognition, conjecture generation, informal reasoning and Lean proof checking to discover compact Collatz-like execution accelerations for machines in the BB(6) search frontier. The authors report eleven machines with formally verified accelerations and distinguish new discoveries from rediscoveries/proofs of community-known rules. They describe “Cryptid” classifications as provisional and subject to community acceptance. This is a concrete example of an open-ended discovery loop, not merely answering a fixed benchmark prompt.

The Poincaré formalization preprint describes a different contribution: a mathematician-prepared proof blueprint, roughly 90 milestones, parallel agent work and kernel-checked Lean formalization of an already established mathematical theorem. It reports approximately US$25,000 in model/server costs and a very large initial formal codebase. These are source-reported project-specific resource figures, not a general cost estimate for AI mathematics.

The physics-formalization perspective emphasizes a critical boundary: a proof assistant can verify a theorem relative to formal definitions and assumptions, but that does not by itself prove that the formal definitions faithfully represent the intended physical system. This distinction directly matches INV-035.

## Evidence class and limitations

These are arXiv preprints/perspective material; UQPU has not independently reproduced the pipelines or audited every proof artifact. A Lean-checked acceleration can establish the stated relation between a particular encoded machine and a formal execution rule, but it does not automatically establish that the machine halts or does not halt unless that exact conclusion is proved. “Cryptid” is not treated here as a physical category or as a theorem of non-halting. Reported new discoveries, rediscoveries and proof-only cases must remain separated.

Formal correctness also does not validate a physical interpretation, measurement model, units, causal mechanism, or external-world correspondence. The Poincaré project is formalization of existing mathematics, not a new physical law. The reported cost is context-specific and should not be transferred directly into UQPU finance forecasts.

## Exact UQPU relevance

- **FND-006 / EQN-001–EQN-006:** motivates a structured generator → candidate ranking → explicit constraints → evaluator → held-out test → counterexample search → proof/simulation → discriminating experiment pipeline. Formal proof should be attached to the exact candidate and assumptions.
- **INV-035:** separates mathematical validity from physical validity. For a candidate physical equation, a checked proof may establish algebraic consequences but cannot replace dimensional/symmetry/conservation/causality checks, empirical prediction, falsification or independent measurement.
- **Lanes A/F:** record search budget, compute/time cost, proof-check status, candidate failures, false discoveries and independent validation effort. Proof success is not workload success or economic advantage.
- **Lanes D/E/G:** only connect a formal candidate to devices, materials, biomass, fusion or manufacturing after a causal mechanism and a testable system consequence are specified.
- **Lane H / FIN-001:** source-reported project costs are a prompt to measure time-to-evidence and resource consumption, not evidence that project WACC or macro rates decline.

## Falsifiable follow-up

1. Select one synthetic, known-governing-equation benchmark with fixed units and a separate held-out parameter/regime split.
2. Compare unconstrained candidate generation against a staged, physics-constrained pipeline under equal compute/evaluation budgets.
3. Store all candidates, including false discoveries and failed proofs; run dimensional, symmetry, conservation, causality and limiting-case checks before ranking.
4. Bind each formal proof to source hash, theorem statement, assumptions, kernel-check result and independent rerun.
5. For any candidate intended as a physical law, preregister a distinct observable and a held-out prediction, then identify the experiment and independent replication path.
6. Track wall time and compute cost through accepted, rejected and undecided candidates. Do not infer that a formal theorem proves a new physical law.

No new physical law is asserted by this watch.
