# FUS-001 research-lane note — component-level experience-rate uncertainty

**Date:** 2026-10-25  
**Primary owner:** Lane E  
**Integration owner:** Lane F  
**Evidence class:** LITERATURE_ONLY  
**Base main SHA:** 6af8ce896368ed993fe2b8278afa6082e1ecc916

## Decision

Add FUS-LR-001 as a follow-up under the existing FUS-001 cost-driver envelope. Do not assign one generic learning rate to an entire fusion plant or treat a forecast as demonstrated cost. A peer-reviewed Nature Energy analysis published 2026-03-23 reports wide first-of-a-kind CAPEX estimates and argues that assumed fusion experience rates are overestimated. The source is an uncertainty/forecast analysis, not an operating-plant measurement.

Primary literature artifact: docs/literature_watch/2026-10-25-fusion-experience-rate-uncertainty.md.

## Minimum component-level contract

For every learned component, require:
- component function and scope boundary;
- cost unit and production unit;
- first-of-a-kind baseline and source provenance;
- deployment count / cumulative production definition;
- learning-rate range, uncertainty and evidence class;
- separation of learning, redesign, scale, yield and scope changes;
- replacement lifetime and outage duration;
- material-damage, maintenance and remote-handling effects;
- construction time, financing, working capital and decommissioning impacts.

The FUS-001 denominator must remain **reliable net delivered electricity**, not fusion gain or gross thermal output. Keep recirculating electricity, capacity factor, conversion/cooling, grid interface, fuel cycle, replacement and outages inside the boundary.

## Falsifiable gate

Run FUS-001 under source-backed low/base/high learning-rate scenarios, preserving UNKNOWN when evidence does not justify a range. If a cost target or architecture ranking depends on an unsupported optimistic rate, keep it MODEL_ONLY. If ranking remains stable across plausible rates, record that robustness without promoting it to commercial proof. Avoid double counting factory learning and design improvements.

## Cross-lane and mission boundary

- E owns component/energy assumptions; F owns uncertainty, LCOE/NPV and interest accounting.
- D/G consume only validated component/process requirements; no fabrication or yield claim follows from the paper.
- H may use the sensitivity for staged capital decisions but must not infer lower WACC or economy-wide rates.
- BIO-001 remains separate; no fuel coproduct credit is introduced.
- INV-029–035 and FND-001–006 remain evidence-gated; this source establishes no new physical law, no net delivered electricity and no commercial fusion result.

## Sync debt

RESEARCH_GAPS.md and historical WORKLOG.md are large canonical files with known reconciliation debt. This note does not overwrite either file. Add FUS-LR-001 to the canonical gap ledger during a safe full-content sync; preserve existing RG IDs. No new RG number is assigned here.
