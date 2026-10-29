# Research gap MAT-PANGOLA-CARBON-001 — functional transfer from biomass carbon studies to Pangola

**Opened:** 2026-10-30  
**Primary owner:** Lane E — materials, biomass, energy and infrastructure  
**Interfaces:** D/G material and process qualification; F lifecycle cost/evidence; H strategic publication  
**Status:** SOURCE SURVEILLANCE COMPLETE / PANGOLA TRANSFER NOT TESTED  
**Evidence class:** EXTERNAL PEER-REVIEWED STUDIES + PROJECT TEST CONTRACT  
**Related invariants:** INV-029, INV-030, INV-031, INV-032, INV-033, INV-034, INV-035  
**Literature watch:** `docs/literature_watch/2026-10-30-pangola-carbon-thermochemical-transfer.md`  
**Lane contract:** `research_lanes/E_materials_energy_cooling_infrastructure/PANGOLA_CARBON_THERMOCHEMICAL_TRANSFER_CONTRACT_2026-10-30.md`

## Objective

Determine whether Pangola grass or another explicitly identified agricultural-residue stream can be converted into a carbon material that satisfies one named electronics/device/infrastructure function at lower lifecycle cost or lower critical-material loading. The goal is functional substitution, minimization, recovery/recycling, hybridization or architecture redesign—not elemental transmutation.

## Source facts versus project hypotheses

1. Ikhwan et al. (2026-10-11), DOI 10.1016/j.biortech.2026.136053, compare woodchip combustion, pyrolysis and carbonization under a gate-to-gate LCA/TEA. The abstract reports that carbon-black-like product value and assumed carbon-black price strongly affect the carbonization economics. Its US$13/t and US$1.42/kg figures are scenario-specific and must not be copied as Pangola prices.
2. Hegazy et al. (2026-03-02), DOI 10.1016/j.biombioe.2026.109142, characterize Fe/Mo-assisted graphitization of spruce-bark-derived carbon. Their reported structural/conductivity changes are source-specific, not Pangola data and not a semiconductor qualification.
3. No UQPU material sample, batch, process yield, conductivity, device performance or accepted functional cost was measured in this cycle.

## Work-item contract

- **ID / lane:** MAT-PANGOLA-CARBON-001 / E.
- **Objective:** evaluate one predeclared functional substitution candidate from a traceable dry-basis Pangola/residue lot.
- **Input:** lot identity, source location/season, moisture, ash, elemental composition, contaminants, full process recipe and matched reference material.
- **Output/acceptance:** a named component-level property envelope, accepted-spec yield, durability/reproducibility and lifecycle cost per accepted functional unit.
- **Evidence level:** literature-only until assets/material samples are verified; then MODEL_ONLY/LAB_RESULT as appropriate, never promoted without independent validation.
- **Cost boundary:** feedstock collection/drying, conversion yield, utilities, catalyst use/recovery, wastewater, CAPEX/OPEX, rejects, logistics, financing and end-of-life.
- **Dependencies:** Lane D/G target requirements; Lane F cost/LCA boundary; independent analytical methods; catalyst recovery and waste-handling data.
- **Status:** READY_FOR_BENCHMARK_DESIGN; NOT_TESTED.
- **Blocker/unlock:** no Pangola batch and no named target component/property envelope have been tested; unlock by freezing both before synthesis.
- **Artifact:** literature watch, this gap and Lane E contract.

## Minimal experiment and fail conditions

Use at least a process blank, untreated feedstock control, catalyst-free carbonization/HTC control, and a small catalyst-assisted arm only if it has a defined reason. Record dry feed mass, liquid/gas/solid yields, all energy inputs, catalyst additions/recovery, wash water, waste, and uncertainty. Measure XRD/Raman, elemental O/C, ash/residual metals, conductivity with defined specimen geometry, surface area, stability and batch-to-batch variation.

Reject the substitution hypothesis if any critical specification is missed; if contaminants or durability fail; if independent batches fail to replicate; or if full cost, catalyst recovery, energy, logistics and financing erase the benefit. Never promote a good Raman ratio or conductivity alone to a device-level replacement claim.

## Integration boundary

- **INV-030:** only functional equivalence/minimization/recovery/hybridization/redesign is admissible.
- **INV-031 / BIO-001:** price accepted liquid-energy/fuel separately; char credits must be non-double-counted and cannot hide upgrading costs.
- **INV-032 / FUS-001:** no fusion material or electricity benefit is inferred without a component-specific test and net-electricity accounting.
- **INV-033 / FIN-001:** capital and financing effects are scenarios until required principal, time-to-evidence and interest are measured.
- **INV-034/035:** current material physics remains binding; any new constitutive equation must pass dimensional, symmetry/conservation, held-out and independent validation gates.

**Next action:** select one component-level target and reference material with D/G; then preregister the matched sample and cost protocol before laboratory work.
