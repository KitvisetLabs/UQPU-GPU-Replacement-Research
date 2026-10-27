# Research gap — RG-LBE-PINO-REPRO-001: physics-informed lattice-Boltzmann surrogate reproduction and break-even

**Opened:** 2026-10-28  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure modeling  
**Cross-lane owners:** Lane A — workloads/benchmark contract; Lane C — state/memory/data movement; Lane D/G — device and manufacturing thermal-fluid context; Lane F — evidence and economics; Lane H — literature publication  
**Status:** OPEN / LITERATURE_ONLY / SOURCE-DATA-AND-CODE-PINNING-PENDING  
**Related:** INV-011, INV-029, INV-032–035; FND-006; EQN-001–006; BIO-001; FUS-001; FIN-001  
**Primary source:** Xue et al., *Nature Communications* 17, 9243 (2026), https://doi.org/10.1038/s41467-026-75730-1

## Objective

Determine whether a physics-informed neural operator trained on lattice-Boltzmann distribution fields can provide a reproducible, stable, cost-effective surrogate for a narrowly declared fluid-dynamics workload. This is a simulation-method gate; it is not yet a model for Pangola chemistry, bio-oil upgrading, fusion-plasma dynamics or a specific cooling plant.

## Current evidence and boundary

The peer-reviewed article reports long-time prediction using moment-matching and lattice-equivariance constraints, with case-specific speedups against its own lattice-Boltzmann simulations. The authors also describe a bounded reuse window because current models are trained per case over relatively narrow geometries and parameter ranges. UQPU has not pinned the article's dataset/code, reproduced a case, audited physical residuals, or measured training-plus-inference break-even.

**Evidence class:** `LITERATURE_ONLY`. Source-reported simulation speedups are not UQPU measurements and do not demonstrate physical or commercial benefit.

## Blocking unknowns

- Exact source dataset/code revision, license, hashes and simulator configuration.
- Independent reconstruction of one reference case and unit conversions.
- Whether held-out trajectory/configuration splits avoid temporal leakage.
- Long-horizon stability and moment/conservation residuals outside training settings.
- Peak state memory, training cost, data-generation cost, transfers, inference energy and the number of queries needed for break-even.
- Whether any actual biomass process, fusion auxiliary system or device-cooling workload shares the governing equations and parameter domain closely enough for transfer.

## Unlock protocol

1. Pin the paper version, data/code sources, licenses, hashes, model configuration and reference-solver revision.
2. Freeze one input/output contract, acceptance threshold, initial/boundary conditions, lattice/collision model and held-out split before training.
3. Reproduce the reference case with independent checks; retain every failed seed, run, parse and counterexample.
4. Check local moments, lattice symmetry/equivariance, positivity/stability and long-horizon error; report uncertainty, not only the best seed.
5. Compare against the original solver and a simple surrogate under equal output tolerance. Count preprocessing, reference data, training, validation, inference, peak memory, I/O, energy and operational costs.
6. Only after a successful simulation reproduction may a separate real-process validation plan be proposed. A new domain needs its own data and falsifiers.

## Falsifiers and stop rules

- Fail if the source example cannot be reproduced from pinned artifacts but is described as reproduced.
- Fail if a nominal speedup violates the common output-quality threshold, depends on held-out leakage, or hides data/training cost.
- Reject transfer if invariants or error degrade outside the declared geometry/parameter domain.
- Do not infer net fusion electricity, fuel yield, Pangola material performance, QPU advantage, reduced WACC or physical compression from a surrogate result.

## Cross-lane implications

- **A:** use explicit equivalent-output contracts; no quantum speedup claim.
- **B:** provider-neutral and simulator-first; no real or paid QPU submission is authorized.
- **C:** account for the complete distribution-field state, memory, checkpoint and transfer costs; never equate Hilbert-space dimension with readable RAM/storage.
- **D/G:** preserve continuous device/factory co-design; no fabrication or cooling-device result is demonstrated.
- **E:** candidate method only for matched hydrodynamic subproblems; BIO-001 and FUS-001 remain open.
- **F:** break-even must include source-data generation, training, validation, inference count, energy and lifecycle cost; FIN-001 financing inputs remain independently sourced.
- **H:** keep the six-language public plan and strategic AI-agent/funding references intact while separating strategic intent from evidence.

**Next gate:** pin the source data/code and reproduce one trajectory/configuration with invariant checks before considering transfer to any UQPU energy or infrastructure task.
