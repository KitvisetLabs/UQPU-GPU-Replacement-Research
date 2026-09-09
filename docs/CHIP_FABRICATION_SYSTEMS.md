# UQCS Chip Fabrication Systems Research

## Mission

UQCS includes research into the manufacturing equipment and process stack required to fabricate candidate quantum, photonic, semiconductor, control, memory, interconnect and packaging devices.

This is a research architecture, not a claim that an advanced fab can be built cheaply with present technology.

## Lithography tracks

### Optical lithography
Research:
- i-line and mature-node optical lithography
- KrF / ArF DUV
- ArF immersion
- multi-patterning
- overlay/metrology constraints
- resist/process integration

### EUV
Research at system/economic level:
- EUV process requirements
- mask infrastructure
- resist/process constraints
- contamination/vacuum requirements
- metrology/inspection
- yield and uptime
- total cost of ownership

The project will not assume EUV is necessary. Device architecture should be co-optimized with the cheapest fabrication route capable of meeting functional targets.

### Maskless / direct-write
Research:
- electron-beam lithography for R&D/prototyping
- laser/direct-write approaches
- nanoimprint where appropriate
- programmable/maskless methods

### Photonic/quantum-device fabrication
Research process compatibility for:
- silicon photonics
- silicon nitride photonics
- superconducting circuits
- ion-trap structures
- neutral-atom photonic/control components
- semiconductor spin devices
- detectors and control electronics

## Complete fabrication flow

```text
feedstock/material purification
 -> wafer/substrate preparation
 -> film growth/deposition
 -> lithography
 -> etch
 -> implantation/doping where required
 -> anneal
 -> planarization
 -> metallization
 -> cleaning
 -> inspection/metrology
 -> wafer test
 -> dicing
 -> advanced packaging/chiplets
 -> final test/calibration
```

Research must include deposition, etch, CMP, ion implantation/doping, thermal processing, cleaning, contamination control, vacuum, metrology, inspection, mask production, wafer handling, test and packaging—not lithography alone.

## Architecture rule

For every candidate UQCS device, solve jointly for:

1. required device feature size;
2. process complexity;
3. yield;
4. lithography class;
5. materials;
6. packaging;
7. test/calibration;
8. equipment CAPEX/OPEX;
9. throughput;
10. energy/water/consumables;
11. achievable cost per useful task.

A larger-node device that satisfies the workload at lower total cost is preferable to an unnecessarily advanced node.

## Biomass integration

Evaluate biomass-derived materials only where their purity, thermal, dielectric, mechanical, chemical or electrical properties satisfy the manufacturing function.

Candidate areas include:
- carbon materials and conductive additives
- filtration/adsorption
- selected polymers/composites
- packaging and construction materials
- energy-storage components
- process-waste recovery
- metal recovery/recycling

Do not claim semiconductor-grade substitution without contamination/purity evidence.

## Evidence

All equipment concepts must carry evidence labels. Conceptual machine designs remain CONCEPT or MODEL_ONLY until validated experimentally.
