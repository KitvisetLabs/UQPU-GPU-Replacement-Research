# Literature watch — conservative and time-aware PDE-surrogate evaluation

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance/publication  
**Execution interface:** Lane A — reusable metrics and benchmark contracts  
**Cross-lane consumers:** C (state/data movement), D/G (device/process and manufacturing models), E (materials/energy/thermal-fluid systems), F (evidence/economics)  
**Evidence class:** LITERATURE_ONLY; UQPU-side metric implementation has synthetic unit fixtures only  
**Related:** INV-034, INV-035, FND-006, EQN-001–EQN-010, BIO-001, FUS-001, FIN-001

## Why this watch matters

Fresh searches of the official Proceedings of Machine Learning Research (PMLR) volume for ICML 2026 found three relevant methods not previously indexed in this repository: FluxNet, TINNs and Heavy-tailed PINNs. These are methods for solving or learning PDE solutions, not discoveries of new physical laws. Their useful contribution to UQPU is to sharpen the acceptance contract for time-dependent physical surrogates: fit error alone is insufficient; conservation, physical bounds, temporal generalization, residual behavior and full compute resources must be reported separately.

## 1. FluxNet — conservation and physical bounds by construction

**Primary source:** Zishuo Lan, Junjie Li, Lei Wang and Jincheng Wang, “FluxNet: Learning Capacity-Constrained Local Transport Operators for Conservative and Bounded PDE Surrogates,” *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306:62530–62559 (2026). Official record: https://proceedings.mlr.press/v306/lan26c.html. Code link published by the authors: https://github.com/Lan-zs/FluxNet.

The paper parameterizes cumulative transport between cells and reports a discrete update that conserves the specified quantity by construction, with modular heads for lower/upper bounds. The authors evaluate on four named benchmark families: 1D convection–diffusion, 2D shallow water, 1D traffic flow and 2D Cahn–Hilliard. Their abstract reports exact discrete conservation and structural bound preservation on those tasks.

**Genuine novelty for this project:** a learned surrogate should be evaluated against its governing invariant and admissible state range, not only its prediction loss. This motivates an explicit metric utility that reports conservation drift and bound violations as separate acceptance signals.

**Limits:** “by construction” applies to the paper's specified discrete update and applicable conservation-law class; it is not a guarantee for arbitrary PDEs, boundary conditions, discretizations, data pipelines or physical systems. The project has not audited the upstream source/license, reproduced a benchmark, or independently verified the authors' results.

## 2. TINNs — time-conditioned spatial representations

**Primary source:** Chen-Yang Dai, Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai and Chieh-Hsin Lai, “TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs,” *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306:22358–22384 (2026). Official record: https://proceedings.mlr.press/v306/dai26a.html. Author code link: https://github.com/CYDai-ml/TINN.

TINNs parameterize network weights as a learned function of time, allowing the effective spatial representation to evolve rather than forcing one fixed feature representation to cover all times. The authors report up to 4× improved relative L2 error and 10× faster convergence on their tested time-dependent PDEs.

**Genuine novelty for this project:** time-dependent surrogates need an explicitly temporal held-out regime. Random point-level splits can make interpolation appear to be temporal extrapolation; the benchmark should freeze the time split before model selection and report long-rollout stability.

**Limits:** the “up to” figures are author-reported results on the paper's tasks, not a general multiplier. No UQPU reproduction, equal-budget comparison, physical experiment or economic comparison has been run.

## 3. Heavy-tailed PINNs — residual distribution matters

**Primary source:** Jephte Abijuru et al., “Heavy-tailed Physics-Informed Neural Networks,” *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306:211–239 (2026). Official record: https://proceedings.mlr.press/v306/abijuru26b.html.

The paper argues that PDE residuals during PINN training can be heterogeneous and heavy-tailed, making a fixed-variance Gaussian/MSE assumption poorly matched to some tasks. It proposes a Student-t residual model with an expectation–maximization procedure and reports improved accuracy/robustness on its benchmark suite.

**Genuine novelty for this project:** residual summaries should include distributional diagnostics and worst-case behavior; a low mean residual alone can hide a small set of catastrophic points.

**Limits:** this does not establish that a heavy-tailed model wins on every PDE. The project has not reproduced the optimizer, inspected all training configurations, or independently confirmed the reported results.

## Exact UQPU relevance

- **Lane A / EQN-001–EQN-010:** the new software/uqpu-prototype/uqpu/pde_surrogate_metrics.py helper scores supplied trajectories for normalized conservation drift and lower/upper-bound violations. It does not fit a surrogate, compute PDE residuals, or discover equations. It is a narrow acceptance component, not a competing equation-discovery comparator.
- **Lane C:** every later comparison must report spatial resolution, cell weights, state/field bytes, peak memory, data movement and output reconstruction. Grid size or latent-state dimension alone is not a useful-output contract.
- **Lanes D/G:** a surrogate result does not establish device, process, yield or factory feasibility. Any deployment model must bind to the actual discretization, control/readout and manufacturing assumptions.
- **Lane E / BIO-001:** a conservative model could eventually help study mass balances in feedstock conversion or upgrading only if the chosen process actually has the specified conserved quantity and the input data are traceable. It does not establish Pangola-carbon material substitution or accepted bio-oil yield/cost.
- **Lane E / FUS-001:** a PDE surrogate could be a screening tool for thermal-fluid or transport models, but fusion net-electricity, component lifetime and lifecycle economics remain separate evidence gates.
- **Lane F / FIN-001:** runtime, CPU/GPU time, peak memory, failed runs and cost per accepted result must be recorded under matched resource budgets. Faster convergence is not automatically lower total cost.
- **INV-034/035:** the methods inform model evaluation, not the truth of an equation. Established governing equations remain binding; a better surrogate fit is not a new physical law.

## Falsifiable follow-up

1. Pin source revision, license, dataset acquisition, numerical reference solver, PDE, initial/boundary conditions, spatial discretization, cell weights, parameter ranges and acceptance rules before running any upstream model.
2. Use a time-block holdout for temporal tasks and a parameter/geometry group holdout where relevant. Keep the test region blind until method selection is frozen.
3. Compare each method only within a matched task class and identical useful-output/resource contract. Do not pool solver tasks with symbolic equation-discovery tasks or combine incomparable benchmark scores.
4. Report held-out relative L2 error, PDE residual, initial/boundary errors, normalized conservation drift, bound-violation rate and maximum violation, long-rollout stability, peak memory, wall/CPU/accelerator time and total cost. Retain failed seeds and counterexamples.
5. Reproduce a small synthetic known-solution case first, then a public benchmark only after source/license and data provenance are checked. If conservation, bounds or temporal generalization fail despite low training loss, reject the claimed physical-surrogate acceptance.
6. Treat all external numerical results as LITERATURE_ONLY until independently reproduced. No method winner, physical law, material/fuel/electricity advantage or cost advantage is promoted by this watch.

## Decision

This source set changes the evaluation method to investigate, not UQPU's physics or mission evidence. The project implemented only a generic metric helper and deterministic synthetic tests. The FluxNet/TINNs/Heavy-tailed PINN implementations, scientific benchmark, source audit, target-aware hardware test and economic comparison remain unrun.
