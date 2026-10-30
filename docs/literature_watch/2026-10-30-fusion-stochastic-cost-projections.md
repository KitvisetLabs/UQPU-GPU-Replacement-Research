# Literature watch — 2026-10-30: stochastic fusion-cost projections and learning-rate disagreement

**Checked:** 2026-10-30  
**Primary owner:** Lane E — fusion energy/infrastructure  
**Cross-lane interfaces:** F (cost, uncertainty, financing), G (standardization/manufacturing), H (capital allocation/publication); INV-032/033  
**Evidence class:** OFFICIAL ARXIV PREPRINT; PEER-REVIEW STATUS NOT ESTABLISHED; NOT REPRODUCED BY UQPU

## Primary source

Stefania Böhnlein, Fanny Böse, Christian von Hirschhausen, Claudia Kemfert and Alexander Wimmers, “Too cheap to meter? A stochastic analysis of projected future fusion costs,” arXiv:2606.26536 (submitted 2026-06-25). Official source: https://arxiv.org/abs/2606.26536.

## Reported result and genuine novelty

The abstract reports a stochastic analysis of projected costs across magnetic-confinement fusion (MCF), inertial-confinement fusion (ICF) and magneto-inertial fusion (MIF), with separate technology-maturity stages. For mature configurations, the authors report mean LCOE values of US$114.6/MWh (MCF), US$110.3/MWh (ICF) and US$143.9/MWh (MIF), together with implied learning rates above 30%. The abstract itself cautions that these projections are rather optimistic relative to other literature and comparable technologies such as fission.

The new-to-main contribution is a stochastic, multi-architecture cost-projection comparator that can be checked against the already indexed Tang et al. Nature Energy analysis, “Fusion power experience rates are overestimated” (2026-03-23; DOI https://doi.org/10.1038/s41560-026-02023-8), which argues that 2–8% is more defensible for the two dominant magnetic and laser-inertial approaches. The Tang et al. policy brief “Fusion power unlikely to become competitive” (2026-04-01; DOI https://doi.org/10.1038/s41560-026-02022-9) is a companion summary of that same study, not an independent dataset.

## Limitations and evidence boundaries

- The new source is an arXiv preprint, not a measured commercial-fusion cost series.
- The reported mature-stage LCOE and implied learning rates are outputs of a literature-based model; they are not observed plant costs or realized fleet learning.
- The abstract does not establish a complete UQPU-compatible net-electric boundary. Recirculating power, conversion/cooling, component lifetime/replacement, fuel cycle, maintenance/remote handling, grid delivery and decommissioning must be checked in the full source and supplementary material before transfer.
- The apparent above-30% learning-rate result is methodologically different from Tang et al.'s 2–8% technology-characteristic/expert-elicitation estimate. Do not average them or choose one without reconciling source populations, maturity transitions, FOAK/NOAK definitions, initial CAPEX, deployment doublings, cost normalization and financing assumptions.
- A modeled WACC sensitivity is not evidence that UQPU can lower its own WACC. INV-033 still separates lower financed principal/shorter capital lock-up from lower rates or risk premia.
- No fusion design, net electricity, commercial LCOE, project finance or physical advantage is demonstrated by UQPU.

## Exact FUS-001 relevance

Add the preprint as a contrasting external model in the architecture-neutral net-electric cost-driver envelope. Keep MCF, ICF and MIF as separate architecture families. Preserve FOAK CAPEX, construction time, capacity factor, plant life, fixed/variable O&M, fuel, discount rate, recirculating power, conversion/cooling, component damage/lifetime, replacement downtime/cost, remote handling, grid interface and decommissioning as separate inputs. A headline LCOE must never substitute for reliable NET delivered electricity.

The Tang 2–8% and Böhnlein et al. above-30% learning-rate estimates should be treated as competing methodology outputs, not a probability distribution or project forecast. FUS-001 should carry both until the original datasets and maturity/learning calculations are independently reconciled.

## Falsifiable follow-up

1. Pin arXiv version, full PDF/source, data, code and supplementary materials; verify whether the 590-record/56-source dataset described by secondary indexes is present in the primary archive before using that detail.
2. Reconstruct the authors' input harmonization, currency/year normalization, FOAK/NOAK mapping, probability distributions, Monte Carlo seeds and LCOE boundary from the primary source.
3. Reproduce the reported mature-stage means and implied learning-rate calculations, including uncertainty intervals and sensitivity to WACC, construction time and capacity factor.
4. Compare like-for-like against Tang et al. using the same technology families, deployment doublings, starting CAPEX, maturity definitions and cost boundaries. Report where the methods cannot be reconciled.
5. Recalculate net delivered electricity only after explicitly adding or confirming recirculating loads, conversion/cooling, replacement/outage schedules, fuel cycle, grid delivery and decommissioning.
6. Keep all results MODEL_ONLY until project-specific engineering and plant data exist. No scenario may be promoted to commercial evidence.

**Disposition:** new-to-main external cost-model comparator. The immediate value is to expose learning-rate/model uncertainty and strengthen FUS-001's negative-evidence discipline, not to validate cheap fusion.
