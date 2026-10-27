# SDC-REPRO-001 — Scaffolded DNA computation: reproduction, energy and lifecycle-cost gate

**Primary owner:** Lane E — Biomass / advanced materials / energy / cooling / infrastructure  
**Status:** OPEN / LITERATURE_ONLY / UQPU_REPRODUCTION_NOT_RUN  
**Opened:** 2026-10-28  
**Feeds:** FND-001, FND-004, FND-006, EQN-001–006, INV-029/034/035; lanes A/C/D/G/F/H  
**Source:** Stérin et al., *Nature* 657, 646–652 (2026), https://doi.org/10.1038/s41586-026-10996-5

## Hypothesis and competing explanation

**Hypothesis:** for a narrow reusable molecular program, SDC may have a different error/energy/control trade-off from an electronic implementation because its binding-energy landscape favours target configurations.

**Competing explanation:** sequence design, strand/scaffold inventory, reagent preparation, reporting, annealing, fluorescence readout, failures, instrument overhead and limited workload generality offset any benefit. Niche usefulness would not imply lower all-in cost or energy.

## Frozen contract

Record article version/DOI, source-data/protocol URLs and hashes, licenses, sequences/concentrations/lots, program/input distribution, exact truth table, decoder, acceptance predicate, CPU reference, batches, operator/instrument, temperature profile, timing, calibration, exclusions and uncertainty method. Include preparation, heating/annealing, reporting/readout, equipment, labour, waste, retries and reuse.

Start with one small truth-table program; gate larger addition on successful reconstruction.

## Metrics

For (N_a) accepted outputs from (N_r) attempted preparations:
- acceptance fraction (p_a=N_a/N_r);
- throughput = accepted outputs per end-to-end wall-clock time;
- energy per accepted result = measured wall-plug energy for required attempts/shared preparation divided by (N_a);
- all-in cost per accepted result = strands/scaffold/reporting + reagents + energy/utilities + labour + allocated instrument/capital + waste/retries, divided by (N_a), with setup allocation explicit.

The FND-001 helper `landauer_gap_ratio_for_accepted_task` computes only
[
G_L=\frac{E_{\mathrm{measured,accepted-task}}}{N_{\mathrm{erase}}k_B T\ln 2}
]
for a positive finite erasure count matched to the same task and one appropriate temperature. This is an ideal floor for those erasures, **not** total device energy. A ratio below one triggers a boundary/count/temperature/uncertainty audit, not a new-physics claim. Multi-temperature stages require a stage-resolved sum.

## Protocol and falsifiers

1. Pin source artifacts/licenses and freeze task contract/CPU reference before tuning.
2. Run at least 30 independent preparations per program/control across three batches as an initial screen; preregister confidence intervals/exclusions.
3. Preserve every failed run, no-read, wrong output, counterexample and null.
4. Use blind inputs and concentration/anneal variations; reject broad generalization if quality/yield collapses outside the source regime.
5. Measure wall-plug energy, time, quality/yield, inventory, I/O, instrument/labour, strand/reagent cost, waste and reuse.
6. Compare identical inputs/outputs/acceptance with an optimized CPU. Do not mix provider/QPU prices or probabilities.

Stop if source/license cannot be pinned, output semantics differ, failed runs are excluded, setup costs are hidden, quality fails or the result is presented as general-purpose based on a narrow case.

## A–H integration

- **A:** exact workload and accepted-output contract; CPU baseline; no quantum-advantage claim.
- **B:** no provider job required; cloud/QPU paths remain provider-neutral and simulator-first.
- **C:** count molecular inventory, reporting/readout, persistence and transfer; no state-space-to-storage equivalence.
- **D:** characterize the primitive and operating conditions; no chip claim.
- **E:** owns reproduction and materials/energy accounting; no Pangola/bio-oil/fusion result.
- **F:** audit energy/cost and uncertainty; separate ideal floor from wall-plug energy.
- **G:** after repeatability, derive assembly/metrology/automation/yield requirements.
- **H:** publish only evidence-gated outcomes and preserve the Kanusanan Pongpanna Model and six language editions.

**Next action:** pin the source bundle and reproduce one small truth-table program with blind inputs and controls. Keep OPEN until independent reproduction and full-cost gates pass.
