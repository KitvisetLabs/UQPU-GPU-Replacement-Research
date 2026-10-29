# Literature watch — physics-informed scaling-exponent identifiability

**Date recorded/accessed:** 2026-10-30  
**Primary source:** Gnankan Landry Regis N’Guessan and Bum Jun Kim, “Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks,” Proceedings of the 43rd International Conference on Machine Learning, PMLR 306:91419–91445 (2026).  
**Official publisher page:** https://proceedings.mlr.press/v306/n-guessan26a.html  
**Evidence class:** PEER-REVIEWED CONFERENCE PAPER / EXTERNAL METHOD; NOT REPRODUCED BY UQPU  
**Related:** INV-034/035, FND-006, EQN-001–EQN-006; lanes A, C, D, E, F, G, H.

## Genuine delta

A repository search on 2026-10-30 found no existing watch for this specific paper. The authors introduce a physics-informed power-law basis whose exponents are trainable and report an identifiability result under stated conditions. The publisher abstract reports recovery tests for singularity exponents in two-dimensional Laplace and singular Poisson problems, including a 40-configuration wedge benchmark. These are author-reported results on their evaluated problem classes, not UQPU results.

The useful methodological distinction is between (1) whether the experiment/design identifies a parameter within a specified model family and (2) whether that model family is the correct description of the physical system. A low fit error alone cannot answer either question globally.

## Relevance and limitations

- **FND-006 / EQN-001:** power-law exponents can be explicit candidate parameters for known-law recovery and scaling analysis.
- **EQN-002 / FND-002:** input/output range and measurement precision can determine whether an exponent is identifiable; state-space size or a fit score does not establish useful-output advantage.
- **Lanes D/G:** scaling exponents may inform device/material constitutive models only after the variables, units, regime and measurement process are pinned.
- **Lane E:** possible later relevance to biomass conversion or fusion transport models is conditional on suitable domain-specific data; this paper does not validate BIO-001 or FUS-001.
- **Lane F:** any future comparison must include candidate search, fit, selection, held-out scoring, compute/memory and experiment costs.
- **Lane H:** preserve the source as a staged research lead, not a funding or market claim.

The present review used the official publisher abstract/page. UQPU has not pinned or audited the method implementation, data, license, environment or supplementary material and has not reproduced the paper. Reported benchmark percentages and errors remain source-attributed. This is not a new physical law.

## Project follow-up

A small classical log-linear baseline has been added for synthetic positive data under the restricted model y = a x^mu. Its checks cover exact exponent recovery, prediction at a held-out scale, exponent invariance under rescaling the x-units, and rejection of a degenerate/near-degenerate design. Seven local synthetic test methods passed. This baseline is not MSN-PINN, not a reproduction of the paper and not evidence that an unknown physical law has been discovered.

The next controlled benchmark must pin source code/data/license, preregister group-disjoint fit/selection/test sets, compare a classical baseline and the paper's method under equal hard budgets, test noisy and misspecified alternatives, enforce dimensional/boundary/symmetry/conservation constraints as applicable, retain failed candidates and false discoveries, and report held-out error plus CPU/GPU/memory/I/O/energy/cost where measurable. Independent review is required before any external-method result is promoted.

## Decision

Index the paper as a new-to-repository methodology lead. Keep all candidate equations under the existing generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics gate. No physical law, device benefit, QPU advantage, material substitution, fuel/electricity result or financing effect is established.
