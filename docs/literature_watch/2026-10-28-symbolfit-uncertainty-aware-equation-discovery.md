# Literature watch — uncertainty-aware symbolic discovery for binned HEP spectra

**Watch date:** 2026-10-28  
**Evidence class:** EXTERNAL_METHOD_RESULT / AUTHOR-REPORTED_PREPRINT; UQPU reproduction not performed  
**Primary invariants:** INV-034, INV-035  
**Owners:** Lane H — source synthesis/publication; Lane A — matched protocol; Lane F — uncertainty and resource accounting  
**Related gap:** [RG-EQN-008](../RESEARCH_GAP_EQN008_MATCHED_DISCOVERY_COMPARISON.md)

## Primary source and date

Ho Fung Tsoi, Dylan Rankin, Cecile Caillol, Miles Cranmer, Sridhara Dasu, Javier Duarte, Philip Harris and Elliot Lipeles, “Machine Can Automatically Discover Parametric Functions to Model HEP Data,” arXiv:2607.19750. The official arXiv record shows v1 submitted **2026-07-22** and v2 revised **2026-10-19**. It is associated with the proceedings of ICHEP 2026.

- Official source: https://arxiv.org/abs/2607.19750
- v2 record: https://arxiv.org/abs/2607.19750v2

Repository search for “SymbolFit” and “2607.19750” found no prior mention in this project, so this is a new-to-repository source, not a claim that the paper itself is newly published.

## Genuine methodological delta

The paper introduces **SymbolFit**, pairing symbolic regression with uncertainty modeling for parametric fits to binned high-energy-physics spectra. The abstract reports 560 independent seeded runs across seven simple fit configurations, generation of more than 1,000 candidate functions, approximately unit chi-squared per degree of freedom for fits to CMS and ATLAS Run-2 dijet spectra, and rediscovery of previously used dijet/UA2 functions in 111 runs.

The project-relevant novelty is not “AI discovered a new physical law.” It is a domain-specific example of treating repeated-run stability and uncertainty modeling as part of a symbolic-fit workflow, rather than scoring only the best-fitting expression. Rediscovery of a known function is a useful positive control, not evidence of a novel law.

## Limitations and evidence boundary

- The reported results are author-reported for a particular binned HEP analysis, candidate grammar, fitting procedure and uncertainty model. They are not a general result for all symbolic regression, physical systems or UQPU workloads.
- A fit with chi-squared/NDF near one does not alone establish correct uncertainty calibration, identifiability, absence of selection bias, or the physical interpretation of the function.
- Repeated seeds are not automatically independent scientific replications; they may share data, model assumptions, search grammar and selection rules.
- UQPU has not independently reproduced the results. Code, dataset versions, licenses, acquisition provenance and exact uncertainty construction still need byte-level verification before a reproduction claim.
- This result says nothing directly about real-QPU advantage, Data-Center-to-One-Phone compression, critical-material substitution, accepted biomass fuel, net fusion electricity or project financing rates.

## Exact UQPU relevance

Add a **separate HEP_BINNED_PARAMETRIC_FIT task class** under the existing RG-EQN-008 comparison plan. Do not pool its results with LLM-SRBench law-recovery scores, general physical-law discovery tasks or interactive experiment-design benchmarks such as ClosureBench.

For any matched reproduction:

1. Pin and hash raw binned inputs, source/version/license/acquisition record, code revision, candidate grammar, fit/likelihood configuration, uncertainty model, preprocessing, runtime/dependencies and all method configuration.
2. Freeze disjoint training/validation/test spectra or analysis conditions before tuning; preserve a known-function rediscovery control and a null/no-signal control. If synthetic signal injections are used, keep injection parameters blind to the fitting arms.
3. Use at least 30 shared preregistered seeds where feasible, identical hard wall-clock/CPU/memory/accelerator/candidate/token/cost ceilings, and one cost basis. Count training plus inference and failed searches.
4. Report held-out predictive score, parameter/function stability, residual diagnostics, nominal-interval coverage at preregistered levels (for example 68% and 95%), interval width, a proper predictive score, false-positive/false-discovery behavior on null controls, counterexamples, constraint violations and full resource use.
5. Define coverage tolerances and the primary endpoint before unblinding. Coverage alone is insufficient: arbitrarily wide intervals must not win, so assess coverage jointly with interval width and predictive score. Do not infer a method winner from overlapping or non-overlapping marginal intervals alone; use a preregistered paired analysis appropriate to the task.
6. Independently verify artifact bytes and record-level split disjointness. A declared SHA-256 string is provenance metadata, not proof that a source or dataset was authentic or correctly split.

## Falsifiable follow-up and stop rules

Run the pinned known-function and null controls first. Reject a claimed uncertainty-aware advantage if nominal intervals materially under-cover under the preregistered calibration test, if coverage is obtained only by uninformatively wide intervals, if false-positive behavior worsens, or if the advantage disappears on held-out spectra/conditions or under equal total resources. Preserve every failed seed, rejected function and counterexample.

A successful reproduction would establish only the bounded HEP fitting result. Any proposed new constitutive or physical law must still pass the project's dimensional, symmetry, conservation, causality, limiting-case, held-out prediction, counterexample, proof/experiment and independent-validation gates. Current physical laws remain binding for engineering claims.
