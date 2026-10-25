# Literature watch — 2026-10-25: WEST wall protection as a fusion reliability input

**Access date:** 2026-10-25  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure  
**Integration owners:** Lane F — economics/evidence; Lanes D/G — plasma-facing components, sensors, manufacturing and metrology  
**Feeds:** FUS-001, FIN-001, INV-032, INV-033, FND-001 and EQN-001–006  
**Evidence class:** OFFICIAL ARXIV PREPRINT / EXTERNAL EXPERIMENTAL OPERATION REPORT  
**UQPU project evidence promoted:** none

## Source and date

R. Mitteau, M. H. Aumeunier, L. Dubus, J. Gerardin, V. Gorse, E. Grelier, V. Moncada, S. Vives, X. Litaudon, M. Jakubowski and J. Fellinger, “WEST advanced wall protection achievements toward long pulse operation,” arXiv:2610.11871, submitted 2026-10-08.  
Primary source: https://arxiv.org/abs/2610.11871

## Genuine delta

The report describes a wall-protection workflow for long-pulse magnetic fusion operation that combines temperature/power indicators from multiple diagnostics, infrared viewing and deterministic models with machine-learning-derived indicators. Some indicators operate in real time and feed back to plasma actuators; other analyses are post-discharge forensic tools used to adjust later discharge plans. The authors report no critical wall-power event affecting campaign plans across WEST campaigns C9–C11, which totalled about 13 hours of plasma operation in 2024–2025.

The paper explicitly does **not** establish that active or AI-based wall protection caused WEST's reported 1,337-second plasma-duration record. The useful engineering signal is a reliability/control architecture and operational evidence, not a new plasma law or a demonstrated reduction in electricity cost.

## Limitations

- This is an external experimental report, not a UQPU experiment or an independently reproduced result.
- The abstract does not provide enough information to independently calculate a false-negative rate, false-alarm rate, damage avoided, lifetime extension or lifecycle-cost reduction.
- A 1,337-second plasma duration and the absence of a campaign-critical event do not establish plant availability, capacity factor, net electricity, commercial economics or fusion gain-to-electric-gain conversion.
- The evidence must not be multiplied by projected learning rates or transferred directly to a different reactor, wall material, diagnostic stack or operating regime.

## Exact UQPU relevance

- **Lane E / FUS-001 / INV-032:** reliability and wall-protection performance can affect downtime, component lifetime, maintenance and remote-handling demand. They belong in a net-delivered-electricity and lifecycle-cost ledger, but the report does not close that ledger.
- **Lanes D/G:** plasma-facing material, coating, sensor, metrology and actuator interfaces should be co-designed. Required evidence includes calibrated temperature/power uncertainty, qualified process windows, degradation distributions and component replacement intervals.
- **Lane F / FIN-001 / INV-033:** only measured changes in downtime, maintenance, component replacement or time-to-evidence can enter a financing model. Lower required principal may lower absolute interest at unchanged terms; a lower WACC or risk premium requires separate evidence.
- **FND-001 / INV-035:** diagnostic signals and ML alerts are not direct measurements of entropy production or a new thermodynamic law. Any model modification needs held-out predictions and independent validation.
- **INV-029–031:** this report does not demonstrate phone-class physical compression, Pangola-carbon functional substitution or accepted low-cost bio-oil.

## Proposed falsifiable follow-up — FUS-WEST-WP-001

1. Obtain the full paper and any released diagnostic/operational data; pin versions and hashes before analysis.
2. Freeze the target event definitions (critical wall hot spot, missed event, false alarm, operator intervention), time windows and baseline protection policy before examining outcomes.
3. Evaluate event sensitivity, false-positive rate, warning lead time, calibration error and intervention latency on held-out discharges, including operating regimes not used to tune the indicators.
4. Where records allow, compare component damage, maintenance hours, unscheduled downtime and replacement interval under matched operating conditions. Record uncertainty and confounders; do not infer causal lifetime extension from event-free campaigns alone.
5. Only after reliability metrics are independently reproduced, feed them into FUS-001 as bounded availability/maintenance scenarios alongside recirculating power, conversion/cooling, fuel cycle, grid interface, CAPEX, construction time and decommissioning.

**Pass condition:** the held-out diagnostic protocol meets preregistered event-detection/calibration thresholds and its uncertainty-bounded reliability effect survives independent review.  
**Failure condition:** event labels or raw signals are unavailable, performance does not beat the baseline, or apparent benefit disappears on held-out operating regimes.  
**Promotion boundary:** literature lead only; no commercial fusion, net-electricity, cost, financing or new-physics claim.
