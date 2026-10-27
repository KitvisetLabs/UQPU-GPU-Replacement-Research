# Literature watch — physics-constrained symbolic regression for turbulent boundary layers

**Watch date:** 2026-10-28  
**Source:** Xianglin Shan and Weiwei Zhang, “Physics-Constrained Symbolic Regression for Mean-Velocity and Mixing-Length Scaling in Zero-Pressure-Gradient Turbulent Boundary Layers,” arXiv:2610.35276, submitted 2026-10-26.  
**Official preprint:** https://arxiv.org/abs/2610.35276  
**Evidence class:** official preprint / data-fit model; **UQPU reproduction: NOT RUN**.

## Genuine novelty

The authors retain classical near-wall and overlap-region asymptotic structure, then use staged physics-constrained symbolic regression to identify transition functions and Reynolds-number-dependent outer corrections for mean velocity and effective mixing length in incompressible, smooth-wall, zero-pressure-gradient turbulent boundary layers. The reported mean-velocity relation is compared with 35 DNS/LES/experimental profiles over friction Reynolds numbers (Re_\tau=252) to (72{,}526); the mixing-length relation is assessed against 21 numerical profiles.

This is a useful equation-discovery pattern: preserve known asymptotic structure explicitly, constrain the candidate search, and fit only the remaining functional freedom. The formulas are domain-specific models, not newly established universal laws.

## Important limitations

- The authors state that the profiles outside the fitting stages are **not a statistically independent validation set**. The Reynolds-dependent coefficients use selected DNS/LES profiles; some reported high-(Re_\tau) limits are prescribed modelling targets rather than independently established universal constants.
- The preprint's reported agreement is external and has not been reproduced by UQPU. Data extraction, preprocessing, code/version, operator set, search seeds, selected expression, coefficient fitting and residuals must be pinned.
- The target domain is incompressible smooth-wall ZPG boundary layers. It does not directly establish performance for data-centre cooling, fusion blankets/divertors, plasma turbulence, other geometries or other constitutive regimes.
- A good fit does not prove causality, uniqueness, universal scaling or a new physical law.

## UQPU relevance

- **EQN-001/EQN-006, FND-006, INV-035:** a concrete candidate for the constrained generator → evaluator → asymptotic checks → independent holdout → counterexample workflow.
- **Lane A:** a reusable symbolic-regression audit can help keep exact equation, data split, model-selection budget and test holdout separate.
- **Lane E:** possible later relevance to thermal-fluid/cooling models only after domain-matched data and boundary conditions; no direct cooling/fusion transfer is claimed.
- **Lane F:** track model complexity, fit/holdout error, uncertainty, training/search compute, energy and total cost; no speed/cost advantage is inferred from compact equations.
- **INV-029–033:** no direct phone-compression, Pangola material, accepted bio-oil, net fusion electricity or financing result.

## Falsifiable follow-up — EQN-PCSR-TURB-001

1. Pin the arXiv version, code, data and license; freeze hashes, preprocessing and symbolic-search settings.
2. Reconstruct the reported equations and units from the source; independently check (U^+), (y^+), (eta), and (Re_\tau) are dimensionless, the no-slip/near-wall limit, logarithmic overlap behavior, wake term as (eta\to0), and the stated high-(Re_\tau) limits.
3. Reproduce the paper's in-fit profiles and residuals with fixed seeds and retain all failed searches.
4. Freeze independent profile/geometry/Reynolds-number holdouts not used for coefficient or expression selection; compare against the classical log-law/Coles and van-Driest baselines with identical metrics.
5. Search counterexamples in low-(Re_\tau), near-wall, outer-layer and measurement-sensitive regimes; report uncertainty and model complexity.
6. Promote no candidate unless the independent holdout improves the declared error/constraint objective under a matched search budget and independent replication.

**Current decision:** literature lead only. No equation is added to the executable physical-law set, no UQPU result is claimed, and no model is transferred to cooling/fusion without a domain-specific test.
