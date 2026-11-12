# Literature watch — 2026-10-26: conservative PINNs, exact constraints, and model discrepancy

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — research publication  
**Benchmark/implementation owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Cross-lane reviewers:** Lanes C, D, E, F and G  
**Feeds:** EQN-001, EQN-003, EQN-004, EQN-006; FND-006; INV-029, INV-034, INV-035  
**Evidence class:** PEER_REVIEWED_NUMERICAL_METHODS / LITERATURE_ONLY  
**UQPU reproduction:** none  
**Canonical starting main:** c9880f2bcca274ed36fe19f83b91e7c91e41b400

## Primary sources and material delta

1. **Vicente Chomalí-Castro, Nick Clarisse, Nicki Mullins and Jorge Noronha**, “Solving Bemfica-Disconzi-Noronha-Kovtun diffusion using physics-informed neural networks,” *Physical Review D* 114, 076013, published **2026-10-07**, DOI [10.1103/shpm-ksq9](https://doi.org/10.1103/shpm-ksq9). The publisher abstract reports a flux-conservative reformulation of the relativistic BDNK diffusion equation, compared using a second-order Kurganov–Tadmor finite-volume solver and a self-adaptive PINN with exact auxiliary-condition enforcement through an output transform (SA-PINN-ACTO). Agreement is reported for smooth profiles; errors increase on discontinuous profiles. The publisher notes that the accepted manuscript will not become available until 2027-10-07, so this cycle does not claim a source-exact independent reproduction.

2. **Jincheng Zhang**, “Reconstruction of Reynolds-averaged Navier-Stokes solutions from boundary data with partial Reynolds stress transport constraints,” *Physical Review Fluids* 11, 104602, published **2026-10-06**, DOI [10.1103/rn1j-32n4](https://doi.org/10.1103/rn1j-32n4). The open-access paper formulates exact advection and production terms, groups unclosed terms into an explicit inadequacy term, enforces Reynolds-stress realizability through network design, and reconstructs fields from boundary data. These are model-structure and constraint-handling techniques; they do not identify a new universal law.

## Genuine novelty for this project

The useful cross-paper signal is a separation of three responsibilities that are often conflated in candidate-equation workflows:

- **Hard constraints:** encode conservation/flux form and admissibility conditions explicitly when the model supports them, rather than assuming a soft residual penalty guarantees them.
- **Model discrepancy:** expose unresolved or unclosed physics as an explicit inadequacy term instead of allowing a symbolic/learned candidate to absorb it silently and appear more certain than the data justify.
- **Regime-aware validation:** test smooth and discontinuous/sharp-gradient cases separately; success on smooth held-out data does not establish robustness at discontinuities or under extrapolation.

This is a method-design lesson from specific PDE applications, not evidence that PINNs outperform conventional solvers in general. It is complementary to, not a replacement for, the pending CoSR progressive-symbolic-discovery work (PR #56) or AI-Newton cross-experiment concept-discovery work (PR #111); this watch does not duplicate either pending artifact.

## Exact UQPU relevance

- **Lane A / EQN-003:** candidate generators should carry typed units, conservation constraints, admissibility predicates and explicit discrepancy terms into evaluation. A lower training residual alone is not an accepted result.
- **FND-006 / EQN-004:** add smooth, discontinuous, parameter-shifted and counterexample cases to held-out evaluation; preserve failures and uncertainty rather than selecting only the favorable regime.
- **Lane C / INV-029:** report output reconstruction, state/I/O and resource costs separately from logical model complexity. Neither a PDE residual nor an equation fit establishes phone-class physical compression.
- **Lane D and G:** device/process implications remain downstream of validated model predictions, target-aware requirements and manufacturability evidence. No device or factory change follows from these papers alone.
- **Lane E / INV-030–032:** biomass mass/energy balances, accepted-liquid yield, fusion net-electricity and cooling models should retain explicit conservation boundaries and discrepancy accounting. These papers supply no Pangola material, saleable fuel or fusion-electricity evidence.
- **Lane F / INV-033:** compare candidate and baseline on matched outputs, compute budget and full resource boundary; do not translate solver residuals into measured joules, lower CAPEX, lower interest or lower WACC.
- **Lane H:** preserve the result as a reusable research method lead inside the Kanusanan Pongpanna strategic context without promoting a numerical technique into a new physical law.

## Proposed falsifiable follow-up — EQN-PINN-CONSERVATION-001

1. Freeze the exact equation, units, boundary/initial conditions, admissibility constraints, dataset hash, solver versions, seeds and evaluation split before fitting.
2. Use the published RANS cases only where the article's data and equations can be retrieved with provenance. For BDNK, wait for an accessible source-exact equation/code package or reconstruct from cited primary sources and obtain independent review; do not infer unavailable details from the abstract.
3. Compare a conventional finite-volume baseline, an unconstrained PINN control and a hard-constraint/explicit-discrepancy variant under matched data, compute/time budget and output quality.
4. Report conservation/flux residuals, realizability/admissibility violations, smooth-regime error, discontinuity error, held-out parameter/OOD error, uncertainty calibration, wall time and host resources. Keep measured physical energy and cost as separate fields; leave them null when not measured.
5. Search counterexamples where hard constraints worsen conditioning, the inadequacy term absorbs the signal of interest, or the conventional solver is superior. Require independent implementation and replay from frozen inputs before promoting any result.

**Falsifier:** reject the proposed project-level method advantage if the constrained/discrepancy-aware variant does not improve pre-registered held-out acceptance while respecting conservation/admissibility, or if any gain disappears under an independent evaluator or matched compute budget. A failure to reproduce the method is not evidence against the underlying physical equations.

## Limits and non-claims

- No UQPU code reproduction, new equation, new physical law, theorem, anomaly or independent experiment is reported.
- No quantum execution, quantum advantage, material substitution, biomass fuel, net fusion electricity, project-finance benefit or Data-Center-to-One-Phone capability is demonstrated.
- A PINN's numerical fit is not proof of a physical law; a reformulation of an established equation is not a new law by itself.
- Current physics and conservation constraints remain binding for present engineering claims under INV-035.

## Related artifacts

- Gap: `docs/RESEARCH_GAP_EQN_PINN_CONSERVATION_001.md`
- Lane A contract: `research_lanes/A_quantum_programming_runtime/EQN_PINN_CONSERVATION_BENCHMARK_CONTRACT.md`
- Integration record: `integration/INT-20261026-EQN-PINN-CONSERVATION.json`
