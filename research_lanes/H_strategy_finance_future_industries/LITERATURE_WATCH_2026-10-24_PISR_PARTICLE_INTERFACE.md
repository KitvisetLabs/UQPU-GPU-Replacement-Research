# Literature watch — 2026-10-24: physics-informed symbolic regression for particle–interface dynamics

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategic research and publication  
**Feeds:** Lane A equation-discovery pipeline; Lane D constitutive/device models; Lane E material/energy models; Lane F evidence and economics; FND-006; EQN-001–006; INV-034/035  
**Evidence class:** LITERATURE_ONLY — peer-reviewed experimental/modeling study  
**Project evidence promotion:** none

## Source and date

Teddy Lazebnik, Chen Mortenfeld and Alex Liberzon, “Physics-informed symbolic regression reveals a delayed oscillatory closure for particle–interface dynamics,” *Machine Learning: Science and Technology* 7, 055004, published **2026-09-08**, DOI: https://doi.org/10.1088/2632-2153/ae9c8b. Author-hosted full article and appendices: https://acml.teddylazebnik.com/publications/physics-informed-symbolic-regression-reveals-delayed-oscillatory/

The study applies physics-informed symbolic regression to measured trajectories of centimetre-scale spheres crossing water–salt and water–glycerol density interfaces. It reports a compact delayed, exponentially damped oscillatory force closure that improves trajectory reconstruction for transient-rich cases relative to a virtual-mass-based baseline. The paper reports repeated-search structural recovery of 17/20 runs (85%) for its full configuration and documents sensitivity to random seed, operator library, complexity limit, penalty and train/validation split.

## Genuine methodological delta

The useful result is a reproducible *workflow pattern*, not a universal new law:

1. Use domain knowledge to define candidate variables, admissible operators and hard physical constraints.
2. Search a Pareto frontier balancing predictive error and expression complexity.
3. Separate recovery of an equation family from calibration of its numerical coefficients.
4. Repeat stochastic searches and ablate operators and constraints.
5. Evaluate whole held-out trajectories and record failures as well as successful fits.

The reported operator library includes arithmetic, exponential and trigonometric operators. Removing trigonometric operators or exponential operators sharply reduced recovery of the selected family. Therefore, part of the search space was intentionally shaped by prior physical judgment; the result is not evidence that an unconstrained AI independently inferred all of the mechanism. The paper also notes that multiple coefficient combinations can yield similar trajectory errors, so fitted coefficients are not uniquely identified universal constants.

## Limitations and evidence boundary

- The calibration data cover centimetre-scale spheres at moderate Reynolds/Froude regimes; extreme regimes remain untested.
- The density field is treated as one-dimensional and steady; lateral heterogeneity, internal waves and tilted interfaces are not resolved.
- The oscillatory term is a lumped closure, not a resolved-vortex model, and is not directly validated against simultaneous flow-field measurements of wake detachment or return flow.
- The discovery process is scientist-guided rather than fully autonomous.
- The article states that the underlying data cannot be made publicly available because they contain commercially sensitive information; data are available from the authors upon reasonable request. Independent reproduction is therefore blocked unless access is obtained.
- No UQPU equation, device, material, fuel, fusion-electricity or economic result is established by this paper.

## Exact UQPU relevance

- **EQN-002:** supports a future benchmark that scores held-out predictive performance, equation-family recovery, complexity and false discoveries separately.
- **EQN-003:** motivates explicit dimensional, boundary/asymptotic, boundedness and dissipation checks before candidate acceptance.
- **EQN-004:** motivates seed repeats, operator-library ablations, shuffled/no-signal controls, counterexample search and blind validation across new parameter groups.
- **FND-006 / INV-034:** provides a concrete mathematics-first method in which model invention is allowed while proof and empirical adequacy remain separate.
- **Lane E:** the workflow may be adapted to material constitutive models or energy-system closures only with domain-specific measured data and constraints. It does not transfer the reported fluid result to Pangola carbon, bio-oil or fusion.
- **Lane F:** controller/search/evaluation cost, failed candidates and independent replay must be included in cost per accepted discriminating result.

## Proposed falsifiable follow-up — PISR-AUDIT-001

**Status: PROPOSED / NOT EXECUTED.**

### Tier 1 — synthetic pipeline audit

1. Freeze a synthetic generator with a known baseline law and a hidden delayed, damped, oscillatory term; publish hashes for equations, parameter groups, noise seeds, splits, operator set, constraints and scoring code before search.
2. Split by whole trajectory and by held-out parameter groups, not randomly interleaved points from the same trajectory.
3. Compare a baseline mechanistic model with constrained symbolic regression under identical search/evaluation budgets.
4. Preregister full-operator, no-trigonometric, no-exponential and no-delay ablations, plus repeated seeds and a deliberately misspecified simulator.
5. Include shuffled/no-signal data as a false-discovery control. Report family-recovery rate, held-out trajectory error, complexity, constraint violations, failures, compute, retries and independent replay.
6. Keep training, validation and final held-out groups immutable. No result counts if the held-out data influenced operator selection or coefficient calibration.

**Falsifiers:** the candidate fails to improve held-out trajectory prediction over the baseline; the equation family is unstable across seeds or held-out parameter groups; shuffled data yields comparable apparent discoveries; physical constraints fail; or independent replay does not reproduce the score.

### Tier 2 — source-paper reproduction

Request the original data and exact analysis artifacts from the authors. Until data access is granted, mark source-paper reproduction DATA_BLOCKED. A synthetic benchmark can validate UQPU software contracts but cannot be reported as reproduction of the published experiment.

### Physical-model escalation gate

Before any claim of a new constitutive law, require a direct statement of the incumbent assumption, the alternative equation, dimensional and symmetry checks, boundary/limiting cases, a discriminating observable, blind held-out prediction, and independent measurement. For this fluid model, a particularly useful discriminator would be simultaneous flow-field measurement capable of testing the proposed wake/recoil interpretation rather than trajectory fit alone.

## A–H relevance

- **A — programming/workloads/compiler/runtime:** use as a benchmark design pattern for equation search; no compiler or runtime advantage is demonstrated.
- **B — cloud/QPU/provider integration:** no provider or QPU execution; any later search-controller comparison remains provider-neutral and offline first.
- **C — RAM/VRAM/HBM/storage/data movement:** count dataset bytes, state reconstruction and evaluator I/O in future compute comparisons; this paper does not demonstrate memory replacement.
- **D — device/chip/process/fabrication/packaging:** no device result follows from a fluid closure.
- **E — biomass/materials/bio-oil/fusion/cooling:** method transfer is only a hypothesis requiring separate measured domain data; no Pangola, fuel or net-electricity claim.
- **F — economics/benchmarks/evidence/integration:** charge all search, controller, evaluation, retry and replay costs to the accepted result.
- **G — manufacturing equipment/software/factory:** no process window, yield or factory result.
- **H — strategic research/publication:** record the source, limitations, data-access blocker and falsifiable follow-up.

## INV-029 through INV-035 boundary

INV-029 remains the physical Data-Center-to-One-Phone target; this paper gives no physical-compression result. INV-030 has no Pangola material-substitution evidence. INV-031 has no accepted saleable-liquid or fuel-cost result. INV-032 has no net reliable delivered-electricity result. INV-033 has no principal, interest or WACC measurement. INV-034 remains an open foundational agenda. INV-035 permits imaginative candidate generation but requires independent validation before a candidate can support engineering.

No new physical law, UQPU advantage or mission-level economic result is claimed.
