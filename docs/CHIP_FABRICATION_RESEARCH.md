# UQCS Chip Fabrication Route Research

## Objective

Build the lowest-total-cost manufacturable path for UQCS components rather than assuming every chip must use the most advanced lithography.

## Current verified anchors

### DUV
ASML describes immersion DUV as a workhorse of advanced logic and memory manufacturing. Its public product information states that the NXT:2050i can reach 295 wafers/hour and the NXT:2000i lists production resolution around 38–40 nm. ASML also emphasizes that many chip layers can use older/dry lithography more cost-effectively.

Sources:
- https://www.asml.com/en/products/duv-lithography-systems
- https://www.asml.com/en/products/duv-lithography-systems/twinscan-nxt2050i
- https://www.asml.com/en/products/duv-lithography-systems/twinscan-nxt2000i

### EUV
ASML states that 0.33 NA NXE EUV systems have a 13 nm resolution class and High-NA 0.55 NA EXE systems reach an 8 nm resolution class. In July 2026 ASML reported Intel using High-NA EUV in high-volume manufacturing for selected Intel 18A layers.

Sources:
- https://www.asml.com/en/products/euv-lithography-systems
- https://www.asml.com/en/news/press-releases/2026/high-na-euv-reaches-new-readiness-milestone

### Nanoimprint
Canon's FPA-1200NZ2C documentation states a minimum linewidth of 14 nm and argues that eliminating projection optics may reduce cost of ownership for suitable applications.

Source:
- https://global.canon/en/product/indtech/semicon/fpa1200nz2c.html

### Integrated patterning research
imec's current advanced-patterning program explicitly combines lithography, materials, etch and metrology. In 2026 its High-NA pilot infrastructure includes the EXE:5200 and current work on stochastic defects, reliability, yield, resist chemistry and metrology.

Sources:
- https://www.imec-int.com/en/expertise/cmos-advanced/patterning
- https://www.imec-int.com/en/press/imec-demonstrates-extension-chemically-amplified-resists-high-na-euv-lithography

## UQCS fabrication strategy

Use a route-selection hierarchy:

1. mature dry DUV where device function permits;
2. immersion DUV when overlay/feature requirements demand it;
3. nanoimprint where throughput/yield/process integration are acceptable;
4. low-NA EUV only for layers that economically require it;
5. High-NA EUV only when device/system economics justify the tighter patterning;
6. direct-write or other low-throughput routes for research/prototypes where masks/HVM are not justified.

This supports the project goal because many quantum, photonic, control, sensor, power and packaging devices do not automatically benefit from the smallest CMOS node.

## MODEL_ONLY selector

`uqpu.fabrication_routes` now provides:
- device process requirements;
- route capability profiles;
- explicit blockers;
- a normalized economics/yield score;
- least-modeled-cost feasible route selection;
- explicit failure if no current route meets the requirement.

The normalized tool/process/yield values are architecture-study placeholders and must be calibrated before economic claims.

## Critical gaps

- scanner/tool capital and service cost calibration;
- layer-count/multi-patterning cost;
- mask set cost and lifetime;
- stochastic defect models;
- resist/process chemistry cost and yield;
- etch/deposition/CMP process integration;
- metrology/inspection cost;
- wafer-stage/overlay architecture;
- cleanroom, vacuum and contamination-control costs;
- local supply-chain feasibility;
- yield learning;
- packaging/test interactions.

## Research rule

A route that fails a requirement is not discarded from the project. Its blockers become a research gap with explicit unlock criteria.
