# Research gap — FUS-001 mapping to pyFECONs cost accounts

**Gap ID:** RG-FUS001-PYFECONS-ACCOUNT-MAP-2026-10-28  
**Date:** 2026-10-28  
**Primary owner:** Lane F — economics/evidence  
**Technical owner:** Lane E — fusion/infrastructure  
**Cross-lane consumers:** D/G (devices/manufacturing), H (finance/strategy)  
**Status:** REFERENCE FRAMEWORK IDENTIFIED / PINNED REPRODUCTION OPEN  
**Related:** INV-032/033, FUS-001, FIN-001

## New literature lead

Woodruff's arXiv papers document the standards-aligned FECONs/pyFECONs framework and a CATF IWG extension for architecture-specific cost drivers, uncertainty propagation, safety provisions and financing/value metrics. Public references: https://arxiv.org/abs/2601.21724 and https://arxiv.org/abs/2602.19389. Public notebook repository: https://github.com/Woodruff-Scientific-Ltd/PyFECONs-GoogleColab.

## Required closure

1. Pin exact preprint versions, code commit, license, environment, benchmark cases and input hashes.
2. Reproduce one public case before using the framework as a baseline.
3. Map FUS-001 net delivered power and all cost drivers into stable accounts; do not omit recirculating power, component replacement, fuel cycle, remote handling, cooling, grid, construction schedule or decommissioning.
4. Separate MFE/IFE/MIFE driver-specific models from shared balance-of-plant accounts; maintain a common net-electric denominator.
5. Propagate material-price, TRL, schedule, learning and financing uncertainty; preserve failed reproductions and sensitivity ranges.
6. Keep WACC/risk-premium changes as explicit scenarios unless separately evidenced; do not infer that cheaper hardware automatically changes market rates.

**Non-claims:** no commercial net-electricity cost, fusion deployment readiness or lower WACC is demonstrated by the literature framework itself.
