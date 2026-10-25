# Literature watch — 2026-10-25: lithium fuel retention as a fusion lifecycle-cost variable

**Accessed:** 2026-10-25  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure  
**Integration owner:** Lane F — evidence, lifecycle economics and integration  
**Co-design:** Lanes D/G — plasma-facing material/process windows and manufacturing  
**Feeds:** FUS-001; INV-032; INV-034; INV-035  
**Evidence class:** PEER_REVIEWED_EXPERIMENT + OFFICIAL_RESEARCH_SUMMARY  
**Project evidence promotion:** none; no UQPU or commercial fusion measurement

## Executive delta

The U.S. Department of Energy Office of Science highlighted a peer-reviewed DIII-D study on 2026-10-15. The underlying paper, published in *Nuclear Materials and Energy* in 2025, compares deuterium retention in pre-lithiated samples with lithium–deuterium co-deposits produced during lithium-powder injection. This is a useful, narrowly scoped material/fuel-cycle input for FUS-001 because retained fuel affects fuel inventory, recovery, maintenance and plant availability. It does not establish net-electricity cost or commercial reactor performance.

## Primary source and evidence class

M. Morbey et al., “Deuterium retention in pre-lithiated samples and Li–D co-deposits in the DIII-D tokamak,” *Nuclear Materials and Energy* 43, article 101915 (2025), DOI: https://doi.org/10.1016/j.nme.2025.101915. The official DOE Office of Science summary was published 2026-10-15: https://science.osti.gov/fes/Highlights/2026/10a. DOE's public summary: https://www.energy.gov/science/fes/articles/limiting-fuel-retention-lithium-future-fusion-devices.

The reported result is conditional: below lithium's melting point, deuterium retention in pre-lithiated samples was similar across the tested coating thicknesses, while in-situ lithium powder injection produced substantial Li–D co-deposition and removed more deuterium from the plasma/fuel inventory. The authors identify co-deposits, rather than pre-deposited lithium thickness alone, as a major retention factor under the studied conditions. The next planned study concerns behavior when co-deposited lithium/fuel enters liquid-lithium conditions.

## Limits and non-claims

- The experiment concerns specific DIII-D H-mode far scrape-off-layer exposures and sample/conditioning conditions, not a complete power plant.
- The measured isotope is deuterium. Extrapolation to tritium inventories, breeding blankets, reactor-scale wall geometry, long-duration operation or commercial fuel-cycle losses needs separate evidence.
- The DOE summary is not a new experiment; it describes the peer-reviewed study.
- Liquid-lithium behavior is explicitly a follow-up, not an established result of this experiment.
- No net-electricity, recirculating-power, plant availability, maintenance cost, commercial LCOE, fuel self-sufficiency or financing result is measured here.
- This result does not show Pangola carbon replacing lithium or any critical material; it does not support elemental transmutation or a new physical law.

## Exact UQPU / energy relevance

For **INV-032 / FUS-001**, add fuel retention and recovery as explicit plant variables alongside blanket/divertor lifetime, remote handling, maintenance, component replacement, recirculating power and capacity factor. A plausible material improvement is valuable only if it survives a system boundary that includes fuel processing/recovery, contamination, waste handling, downtime, reliability and net delivered electricity.

For **Lanes D/G**, the process window is not just initial coating thickness: deposition route, cold-wall accumulation, co-deposit formation, operating temperature, erosion and the route from coupon to manufacturable plasma-facing component must be tracked together. D/G co-design remains mandatory.

For **INV-033 / FIN-001**, a fuel-retention change can affect capital tied up in fuel inventory, replacement/cleanup, maintenance time and technical risk. A resulting reduction in financed principal may lower absolute interest at unchanged terms; any claim about WACC or market rates needs separate financing evidence.

For **INV-029**, this is an enabling subsystem question only. No phone-class physical compression or data-center service-equivalence claim follows.

## Proposed falsifiable follow-up — FUS-LI-001

Create a provenance-bound table from the paper and its supplementary data with sample location, plasma/exposure conditions, lithium application method, coating thickness, temperature regime, co-deposit amount, deuterium retained, measurement uncertainty, repeat count and analysis method. Freeze source-file hashes and distinguish reported measurements from inferred values.

Then preregister a matched follow-up that tests the proposed mechanism across conditioning method, co-deposit formation and relevant temperature regimes, including the authors' liquid-lithium question when suitable evidence becomes available. Require mass balance for fuel introduced, retained, recovered and unaccounted for; independent replication; and a stated uncertainty interval. Falsify the proposed plant-level relevance if the effect does not persist under matched conditions or if its contribution is dominated by unrelated system losses.

Only after measured retention/recovery data and a validated reactor-system model exist should the result enter FUS-001 net-electric cost envelopes. Until then, classify it as an external materials/fuel-cycle evidence lead, not commercial fusion evidence.
