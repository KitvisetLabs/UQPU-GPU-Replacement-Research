# Literature watch — derivative-constrained physics-informed neural networks

**Date recorded/accessed:** 2026-10-30  
**Primary source:** Kentaro Hoshisashi, Carolyn E. Phelan, and Paolo Barucca, “Physics-informed neural networks for solving derivative-constrained partial differential equations,” *Physical Review E* 113, 055301 (published 2026-05-04).  
**Official publisher page:** https://journals.aps.org/pre/abstract/10.1103/5bbf-p6zk  
**DOI:** https://doi.org/10.1103/5bbf-p6zk  
**Evidence class:** PEER-REVIEWED METHOD PAPER / PUBLISHER ABSTRACT REVIEWED / NOT REPRODUCED BY UQPU  
**Related:** INV-034/035, FND-006, EQN-001–EQN-006; lanes A, C, E, F, H

## Genuine methodological delta

The APS publisher record describes derivative-constrained PINNs (DC-PINNs), a framework that augments PDE-residual optimization with explicit nonlinear constraints on states and derivatives. Examples listed by the authors include bounds, monotonicity, convexity, and incompressibility. The method uses automatic differentiation and self-adaptive loss balancing. The publisher abstract reports reduced constraint violations and improved physical fidelity on selected heat-diffusion, financial-volatility, and vortex-flow benchmarks.

A repository search on 2026-10-30 found no indexed record for this exact paper. This is a new-to-repository method lead, not a claim that the result was published this week. Only the official publisher page/abstract was audited in this cycle; the source implementation and benchmark data were not retrieved, licensed, pinned, or executed.

## Limitations and evidence boundary

- The reported improvements are benchmark-specific external claims. UQPU has not reproduced the experiments or independently checked the reported comparisons.
- Low PDE residual alone does not guarantee correct derivatives, constraints, boundary behavior, or out-of-domain predictions. Conversely, a low constraint-violation score does not prove the governing PDE is correct.
- Self-adaptive loss balancing and derivative evaluation add optimization/runtime work that must be measured. The publisher abstract does not establish lower total training cost, lower inference cost, better generalization for UQPU workloads, or a new constitutive law.
- The public source-code reference listed by the publisher article is https://anonymous.4open.science/r/dcpinns-ef12704/ . Its current contents, license, data, dependencies, and reproducibility were not audited here.

## Exact UQPU relevance

- **Lane A / EQN-003–004:** make physical constraints first-class evaluator outputs, separate from PDE residual and in-sample fit. Candidate acceptance should report each constraint violation, held-out error, numerical stability, and counterexamples independently.
- **Lane C:** include derivative-evaluation memory, batch size, transfer, and reconstruction costs when these methods are applied to large space-time models; no state/storage equivalence follows from a neural surrogate.
- **Lane E / BIO-001 / FUS-001:** derivative constraints could be relevant to future heat-transfer, flow, or transport surrogates only after matching the governing equations and domain. The paper does not validate Pangola conversion, upgrading, fusion plasma/plant behavior, net delivered electricity, or commercial cost.
- **Lane F / FIN-001:** compare total search/training/inference resources and cost per accepted prediction under equal budgets. No financing or time-to-evidence benefit has been measured.
- **Lane H:** retain as a source-pinned method lead with a clear no-reproduction status; do not treat the abstract as strategic or scientific proof.

## Falsifiable follow-up

1. Retrieve the source code and benchmark assets; record repository revision, license, dependency versions, dataset hashes, and source/data integrity before execution.
2. Reproduce one declared heat-diffusion-with-bounds case against the published baseline, conventional PINN, and any hard-constraint comparator under equal optimizer steps, wall time, precision, and compute budget.
3. Freeze initial/boundary conditions and grouped held-out spatial/temporal regimes before tuning. Include an adversarial case with a low PDE residual but a deliberately violated monotonicity or bound constraint.
4. Report PDE residual, each derivative-constraint violation, boundary error, held-out error, uncertainty, failed runs, peak memory, runtime, and energy when measurable. Retain negative and inconclusive outcomes.
5. Require independent review before using the method for an engineering consequence. Any candidate constitutive equation must still pass dimensional, symmetry/conservation/causality, limiting-case, counterexample, and discriminating-validation gates.

## Decision

Index DC-PINNs as a promising constraint-aware numerical method for controlled reproduction. No new physical law, quantum advantage, QPU benefit, material substitution, accepted fuel, fusion-electricity result, financing effect, or Data-Center-to-One-Phone milestone is established.
