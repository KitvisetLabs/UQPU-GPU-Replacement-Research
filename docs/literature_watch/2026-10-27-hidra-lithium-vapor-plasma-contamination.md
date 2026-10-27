# Literature watch — 2026-10-27: HIDRA lithium vapor, plasma contamination and net-loss interpretation

**Date accessed:** 2026-10-27  
**Primary source:** Rabel Rizkallah et al., “Rapid Vapor-Driven Plasma Contamination and Suppressed Net Lithium Surface Loss in the HIDRA Stellarator,” *Journal of Fusion Energy* 45, article 39 (2026), published 2026-06-10.  
**Official source:** https://link.springer.com/article/10.1007/s10894-026-00582-y  
**Evidence class:** PEER-REVIEWED EXPERIMENT / MODEL-REFERENCED MASS-BALANCE ESTIMATE  
**Primary owner:** Lane E — fusion materials, energy and infrastructure  
**Co-design:** Lanes D/G — plasma-facing materials, deposition/process controls and metrology  
**Evaluation owner:** Lane F — net-electricity/lifecycle economics and uncertainty  
**Cross-cutting:** FUS-001, INV-032, INV-033

## Genuine result

In HIDRA stellarator experiments with hydrogen and helium plasmas, the paper reports an inferred effective lithium net-loss suppression factor (R_{\mathrm{eff}}) between about 0.91 and unity. The authors define this as a model-referenced mass-balance quantity that absorbs local redeposition/recycling and possible reduction of effective evaporation through surface conditioning. High-temperature operation also drove lithium release that rapidly made the plasma lithium-dominated, and the attempted operating conditions did not sustain a stable vapor-shielding-relevant regime.

This is useful because it separates **net surface loss** from **gross evaporation**: a low inferred net loss does not by itself imply low plasma contamination, stable operation, or a reactor-ready lithium surface.

## Limitations and evidence boundary

- HIDRA's modeled heat fluxes in this campaign were orders of magnitude below those in linear plasma devices or tokamak divertors; the authors explicitly describe lithium-driven cooling/temperature locking conservatively and do not claim definitive full vapor shielding.
- (R_{\mathrm{eff}}) is an effective, model-referenced estimate, not a direct universal redeposition constant. Surface chemistry, droplet geometry, local recycling and reference evaporation-model uncertainty are folded into it.
- Initial lithium mass has an estimated uncertainty of roughly 15%; temperature is measured below the surface; high-power operation was limited by plasma instability and lithium contamination.
- The study does not establish tritium retention/recovery in a reactor, neutron-damaged component lifetime, availability, recirculating power, net saleable electricity or levelized cost.
- The finding is not a commercial-fusion milestone and cannot be extrapolated directly to ITER/DEMO or another reactor without matched geometry, heat-flux, fuel-cycle and materials conditions.

## Exact UQPU / fusion-finance relevance

**FUS-001 / INV-032:** keep separate variables for gross Li evaporation, net Li loss, redeposition/return, plasma impurity burden, temperature-locking stability, recovery/capture, cleanup time, component lifetime and downtime. The apparent retention benefit and contamination penalty must be modeled together.

**Lane D/G co-design:** any proposed capture, coating, surface-conditioning or metrology improvement needs a defined process window, diagnostic uncertainty, repeatability and maintainability. A surface-material result alone does not imply a manufacturing yield or reactor availability improvement.

**INV-033:** translate only validated effects into required CAPEX/OPEX, replacement and maintenance intervals, working capital, construction schedule and absolute interest at fixed financing terms. Do not infer a lower WACC or financing rate.

**INV-029:** this is a potential input to reliable energy/cooling economics, not evidence for data-center-to-phone compression.

## Falsifiable follow-up

1. Pin the article version, supplementary data and any source datasets by exact URL/version and SHA-256.
2. Reconstruct the mass-balance estimate and uncertainty from raw initial/final Li inventory, surface-temperature trace, reference evaporation curve, exposure time, RGA/spectroscopy and geometry. Preserve the distinction between observed quantities and model-inferred terms.
3. Preregister matched power/position conditions and independently replicate both net-loss and plasma-contamination diagnostics. Explicitly include cases where (R_{\mathrm{eff}}\) is high but plasma contamination prevents stable operation.
4. Test a capture/control intervention against a matched untreated condition; measure net loss, plasma impurity, stability, recovery fraction, maintenance burden and component condition.
5. Only after independent replication, propagate distributions—not point estimates—through the FUS-001 plant boundary for fuel inventory/recovery, availability, replacement, remote handling, recirculating power and net delivered electricity.
6. Falsify the proposed engineering benefit if improved apparent retention fails to improve stable operation or net-electric/lifecycle economics after added capture, cleanup and maintenance costs.

**Current project status:** LITERATURE_ONLY for UQPU/FUS-001 integration. The experiment itself is peer-reviewed evidence about HIDRA conditions; no reactor-level or project-level performance is promoted.
