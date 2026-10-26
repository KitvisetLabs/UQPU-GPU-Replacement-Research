# Literature watch — Experimental environmental memory as a thermodynamic resource

**Date recorded:** 2026-10-26  
**Primary owner:** Lane H — literature watch and strategic publication  
**Cross-lane consumers:** Lane A (runtime/memory policy), Lane C (state and data movement), Lane F (evidence and economics)  
**Evidence class:** PUBLISHED EXPERIMENT + PEER-REVIEWED THEORY  
**UQPU promotion:** literature relevance only; no UQPU performance or physical-law claim promoted

## Material delta

Muruga et al., *Nature Physics*, published 2026-10-16, report an experiment extracting work from environmental memory in an optically trapped Brownian particle using a time-delayed double-measurement protocol. Their result is a physical demonstration that, in that experimental system and protocol, correlations retained in hidden bath degrees of freedom can be accessed and used to enhance work extraction. It is not a general result about software memory, quantum processors, or data-center energy.

Primary source: https://www.nature.com/articles/s41567-026-03442-w

This is distinct from Fiderer et al., *Physical Review X* 16, 041004 (published 2026-10-05; DOI 10.1103/7nds-tjr8), which derives a theoretical work-capacity objective for hidden-Markov percept–action loops. In the memoryless-agent special case, the objective is
`W = H(A) - H(S)` in units of `k_B T ln(2)` per round. The theory's binary invariant channel has action distribution `P(A=0)=1/sqrt(2)` and analytic capacity
`(1/2) log2(3/4 + 1/sqrt(2)) ≈ 0.2715533032`.
Source: https://journals.aps.org/prx/abstract/10.1103/7nds-tjr8

A related accepted *Physical Review Letters* paper by Schwarz, Kolomeisky and Godec (accepted 2026-09-25; DOI 10.1103/gwf7-6kvr) proves that entropy-production inference from coarse observations needs a sufficiently high memory order for guaranteed lower bounds; under its stated conditions, a first-order Markov estimator can create artifacts when no justified timescale separation exists.
Source: https://journals.aps.org/prl/accepted/10.1103/gwf7-6kvr

## What is genuinely new for this project

The Nature Physics experiment supplies an empirical anchor for the broader proposition that environmental memory can be an operational thermodynamic resource. The UQPU-relevant next step is not to infer an energy saving from memory reduction. It is to distinguish (i) logical predictive state, (ii) action-dependent environment feedback, (iii) memory order required for valid thermodynamic inference, and (iv) physically measured energy in a controlled implementation.

## Exact project relevance

- **FND-001:** motivates a future controlled test of whether memory-order and active-feedback distinctions change a resource-optimal policy. The experiment does not validate the UQPU model.
- **FND-002:** reinforces keeping accessible output information and reconstruction separate from internal state count; it adds no new output-information lower bound.
- **FND-003:** no quantum-speed-limit measurement or matched control result follows from this paper.
- **Lane A:** test a source-bounded channel model before implementing policy changes.
- **Lane C:** keep logical states, physical bytes, transfers, resets and calibrated joules as separate fields.
- **Lane F:** do not convert normalized work capacity or entropy into electricity cost without an experimentally validated physical mapping and a complete accounting boundary.
- **INV-029:** this is only a research-method contribution; it does not reduce the phone-class system boundary or establish physical compression.
- **INV-030–033:** no Pangola-material, accepted bio-oil, net fusion-electricity, project-principal, interest or WACC result.

## Reproducible falsifiable follow-up

1. Independently evaluate the published binary memoryless invariant channel using its stated transition matrix and analytic reference.
2. Build a passive IID-tape control with the same output marginal at the selected operating point, while explicitly noting that it is a different environment model.
3. Extend the evaluator to a finite-state memoryful agent/environment and verify stationary/asymptotic quantities independently.
4. Preregister `MEMORYLESS`, `PREDICTIVE` and `BOUNDED_MEMORY` policies, quality predicate, finite horizon, transition parameters, seeds, held-out parameter ranges, counterexamples and total resource budgets.
5. Require an independent evaluator and preserve null cases where policy rankings vanish or reverse.
6. Only after a model-level result survives should a physical memory/energy experiment be considered; it needs a calibrated meter, an explicit physical implementation of logical operations, uncertainty, and complete host/device/data-movement accounting.

## Limitations and non-claims

The reported experiment is system- and protocol-specific. The PRX work-capacity expression depends on the paper's information-reservoir, cyclic isothermal-control and channel assumptions. Neither paper demonstrates lower UQPU cost per accepted useful task, a quantum advantage, a universal thermodynamic law beyond its assumptions, or an engineering energy saving. This watch is literature synthesis, not a UQPU discovery article; it belongs in `docs/literature_watch/`, not the verified-discovery `articles/` registry.
