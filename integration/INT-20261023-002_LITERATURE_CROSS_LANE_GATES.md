# INT-20261023-002 — literature-to-system gate crosswalk

**Primary owner:** Lane F — evidence/economics/integration  
**Status:** PROPOSED / LITERATURE_ONLY  
**Source packet:** supplemental literature watch, 2026-10-23  
**No physical/economic claim promotion**

## Edge 1 — provider roadmap to D/G manufacturing and A/B execution

- **Source:** IonQ official Superion 256 announcement, 2026-09-08; vendor-reported integrated electronic control and foundry/manufacturing milestones.
- **Lanes:** B → A, with D/G co-design and F accounting.
- **Hypothesis:** a semiconductor-integrated control architecture may change manufacturability, packaging, control-electronics and target-interface requirements relative to laser-based trapped-ion platforms.
- **Falsifier:** target metadata or independently measured manufacturing/resource data show no relevant change in the declared workload, reliability or cost boundary.
- **Required evidence:** target availability and exact instruction/connectivity/timing data; independently verified circuit conformance; gate/readout calibration provenance; yield, lifecycle and measured energy/cost only when credible data exist.
- **Current status:** no target or physical comparison measured by UQPU; roadmap only.

## Edge 2 — biomass-derived carbon to one component function

- **Source:** Hegazy et al., Biomass and Bioenergy 211 (2026) 109142, DOI 10.1016/j.biombioe.2026.109142; spruce-bark carbon experiment.
- **Lanes:** E → D/G, with F lifecycle accounting.
- **Hypothesis:** a specified biomass-derived carbon process may satisfy one predeclared component property at lower lifecycle cost than its incumbent material.
- **Falsifier:** Pangola/residue sample fails the component property/reliability gate, or catalyst recovery/process energy/lifecycle cost erases the function-matched advantage.
- **Required evidence:** named feedstock, process mass/energy balance, catalyst recovery/residuals, application-specific material tests, matched incumbent and lifecycle cost.
- **Current status:** literature-only; spruce-bark results are not Pangola results and do not establish metal replacement.

## Edge 3 — fusion cost accounts to FIN-001

- **Sources:** arXiv:2601.21724 and arXiv:2602.19389, pyFECONs/FECONs costing methodology and extensions.
- **Lanes:** E ↔ F ↔ H, with D/G subsystem inputs when validated.
- **Hypothesis:** a shared auditable cost-account crosswalk can make FUS-001 scenario boundaries and FIN-001 principal/interest/time-to-evidence calculations more complete and comparable across architectures.
- **Falsifier:** independent reconstruction cannot reproduce published worked examples within declared tolerances, or critical net-electric/lifecycle/finance accounts are missing or double-counted.
- **Required evidence:** version/license check, public-code reproducibility, input provenance, net-electric normalization, uncertainty propagation, matched accounting and independent review.
- **Current status:** method crosswalk proposed; no commercial fusion or lower-WACC claim.

## Shared integration rules

Every edge uses an identical functional contract, records nulls instead of invented data, preserves source hashes/version/date, includes negative tests and false-discovery outcomes, and requires independent validation before system/economic promotion. No edge authorizes paid QPU jobs, purchases, hazardous processing or funding commitments. INV-029 remains the final physical-compression gate; INV-030–033 require their own functionally matched material/fuel/electricity/finance evidence; INV-034/035 keep present physics binding and generated hypotheses falsifiable.
