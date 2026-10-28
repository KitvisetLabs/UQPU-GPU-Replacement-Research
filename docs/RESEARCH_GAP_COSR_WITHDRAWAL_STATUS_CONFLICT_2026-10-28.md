# Research gap — CoSR publication-status conflict and safe equation-discovery reuse

**Gap ID:** RG-EQN-COSR-STATUS-CONFLICT-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane H — literature/provenance  
**Cross-lane owners:** Lane A (candidate protocol), Lane E (physical-model transfer), Lane F (evidence gate)  
**Status:** OPEN / LITERATURE_ONLY / SOURCE_VERSION_UNRESOLVED  
**Related:** INV-034–035, FND-006, EQN-001–EQN-006  
**Watch:** [progressive symbolic regression and formal theorem discovery](literature_watch/2026-10-28-progressive-symbolic-regression-status-and-formal-theorem-discovery.md)

## Observed conflict

The official APS Physical Review Research accepted-paper page for “Data-driven progressive discovery of physical laws” (Xia and Zhang; DOI 10.1103/f2kp-pp4q) says accepted 2026-10-06. The same-title arXiv record, arXiv:2603.13727, currently says “withdrawn by Mingkun Xia”; its author comment states that methodological flaws were found in the Rayleigh–Bénard convection case and that the paper needs retraction.

This gap records the conflict rather than guessing whether the accepted record represents a corrected version. No UQPU source reproduction, dataset audit or independent result is claimed.

## Why it matters

A progressive symbolic-regression workflow could be useful for EQN-001–EQN-006 and FND-006, but an unresolved source flaw can contaminate method selection and downstream claims. A regression fit or staged expression chain does not establish a physical law. Transfer to BIO-001, FUS-001 or thermal-fluid models requires matched governing equations, units, parameter ranges and held-out validation.

## Unlock conditions

1. Identify the exact accepted manuscript and its version history; resolve whether the RBC flaw was corrected, removed from scope or remains unresolved.
2. Pin a legitimate version, code/data license, hashes, dependencies, solver configuration and source revision before reproduction.
3. Preregister a comparison of one-shot versus staged symbolic regression under equal budgets, with a known-law synthetic test and a physically relevant but independent benchmark.
4. Use disjoint grouped/parameter-held-out data, explicit dimensional/symmetry/conservation checks, limiting cases and adversarial counterexamples.
5. Preserve all false discoveries, failed candidates and undecided outcomes; independent review is mandatory.
6. Only then consider transfer to a specific UQPU, biomass, material, fusion-auxiliary or finance model. A technology claim still needs device/system consequence and end-to-end economics.

## Closure rule

Do not close this gap on publisher acceptance alone, an abstract, or a fit score. Close only after source-status reconciliation and the independent reproduction gate. Until then, classification remains LITERATURE_ONLY; no new physical law or mission-level advantage is inferred.
