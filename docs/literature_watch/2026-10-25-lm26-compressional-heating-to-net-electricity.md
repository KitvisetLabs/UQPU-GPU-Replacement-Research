# Literature watch — 2026-10-25: LM26 compressional heating is a plasma milestone, not net electricity

**Accessed:** 2026-10-25  
**Primary owner:** Lane E — biomass/materials/energy/cooling/infrastructure  
**Integration owner:** Lane F — economics, evidence and cross-lane integration  
**Co-design:** Lanes D/G — device, lithium-liner, diagnostics, manufacturability and service life  
**Feeds:** FUS-001, FIN-001, INV-032, INV-033, INV-034  
**Evidence class:** OFFICIAL PREPRINT + OFFICIAL UKAEA/GOV.UK ANNOUNCEMENT  
**UQPU project evidence promoted:** none

## Primary sources and dates

1. P. Carle et al., “Thomson Scattering Measurement of 1 keV Electron Temperature on Lawson Machine 26,” arXiv:2610.11769, submitted 2026-10-08: https://arxiv.org/abs/2610.11769
2. S. J. Howard et al., “Compressional heating above 1 keV on the LM26 magnetized target fusion machine,” arXiv:2610.11890, submitted 2026-10-08: https://arxiv.org/abs/2610.11890
3. UK Atomic Energy Authority, “UKAEA, General Fusion announce Magnetised Target Fusion milestone,” published 2026-10-08: https://www.gov.uk/government/news/ukaea-general-fusion-announce-magnetised-target-fusion-milestone

The arXiv papers are official preprints, not evidence that peer review is complete. The UKAEA announcement reports the same milestone and describes the papers as being submitted for peer review.

## What is genuinely new

For the Lawson Machine 26 (LM26) magnetized-target-fusion experiment, the reported peak electron temperature is **1180 ± 65 eV** from filtered X-ray diodes, supported by adjacent Thomson-scattering measurement of **1090 ± 40 eV**. The paper reports a deuterium-ion temperature of **459 ± 33 eV inferred from neutron yield**, not a direct equivalent of the electron-temperature diagnostic. It also describes radial compression by a factor of 2.75 and coordinated observations of magnetic-flux compression, electron heating, ion heating and neutron production.

The narrow but meaningful milestone is that the LM26 low-speed solid-lithium-liner compression approach has experimentally reached electron temperatures above 1 keV with multiple diagnostic channels. It is evidence about plasma compression and diagnostic capability in this device.

## Limitations and non-claims

- Electron temperature above 1 keV is not the Lawson criterion; temperature, density and energy-confinement time must be considered together.
- The cited result does not establish net fusion energy, net electric output, a positive grid-meter balance, plant availability, capacity factor, commercial reliability or lifecycle cost.
- Neutron-yield-inferred ion temperature is an inference with its own model and uncertainty; it must not be silently relabeled as a direct measurement.
- The UKAEA announcement says the program's next temperature milestone is 10 keV and that Lawson-criterion progress remains ahead.
- No UQPU experiment, project-owned plasma result, financing result or new physical law follows from this external milestone.

## Exact UQPU / energy / material / finance relevance

For **FUS-001 / INV-032**, add the source-bounded diagnostic milestone to the architecture-neutral evidence ledger, but keep plant net-electricity closure as a separate gate. The next system boundary remains:

`fusion core/driver -> pulse energy and recovery -> fusion/thermal output -> conversion -> gross electric power -> recirculating and parasitic loads -> grid losses -> net delivered MWh -> availability and replacement -> CAPEX/OPEX/fuel cycle/financing/decommissioning -> lifecycle cost per net MWh`.

For **D/G co-design**, the solid lithium liner, theta-pinch compression hardware, diagnostics access, component recovery/replacement and repeatability are relevant design variables. A single successful shot does not establish manufacturing yield, lifetime or maintenance interval.

For **FIN-001 / INV-033**, a well-defined milestone may inform time-to-evidence and capital-lock-up tracking only if actual project expenditures and schedules are supplied. It does not establish a lower WACC or financing rate.

For **INV-029**, fusion is a possible infrastructure enabler, not evidence that data-center-scale useful capability has been physically compressed into one phone.

## Proposed falsifiable follow-up

1. Pin the source-paper versions, diagnostic definitions, shot identifiers and available supplementary/raw-data hashes.
2. Reconstruct electron-temperature, inferred ion-temperature, density, confinement-time and neutron-yield records with uncertainty and diagnostic provenance kept separate.
3. Record the actual driver/compression energy and recovery boundary for each shot; do not infer these from temperature alone.
4. Before any plant-level claim, require time-aligned gross electric generation, recirculating power, other parasitic loads, grid-delivery losses, an explicit meter boundary and averaging interval.
5. Use repeated-pulse and outage data to estimate availability/capacity factor; propagate component lifetime, lithium handling, maintenance, conversion/cooling, fuel-cycle, construction, financing and decommissioning uncertainty into cost per net MWh.
6. Independently reproduce the diagnostic inference or clearly retain it as source-reported; preserve negative shots and uncertainty.

The new executable helper `software/uqpu-prototype/uqpu/fusion_evidence.py` encodes only a fail-closed accounting boundary. Its highest evidence class means that the supplied electric-power terms are internally consistent; it does **not** certify a real plant, reliable electricity, positive energy gain, safety or economic viability.
