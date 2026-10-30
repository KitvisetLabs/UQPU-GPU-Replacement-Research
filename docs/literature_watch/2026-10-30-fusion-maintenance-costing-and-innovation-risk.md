# Literature watch — fusion maintenance scheduling, open costing models and innovation risk

**Date:** 2026-10-30  
**Owners:** Lane E (FUS-001), Lane F (FIN-001), Lane H publication  
**Evidence class:** PEER-REVIEWED SCENARIO MODEL + OPEN-SOURCE COSTING SOFTWARE + OFFICIAL WORKING PAPER  
**Status:** NEW SOURCE DELTA / NO UQPU REPRODUCTION / NO COMMERCIAL COST CLAIM

## 1. Schwartz et al. — maintenance scheduling changes the value of fusion availability

**Source:** Jacob A. Schwartz, Wilson Ricks, Egemen Kolemen and Jesse D. Jenkins, “Valuing Maintenance Strategies for Fusion Plants as Part of a Future Electricity Grid,” *Journal of Fusion Energy* 45:15 (2026), DOI [10.1007/s10894-026-00551-5](https://doi.org/10.1007/s10894-026-00551-5). Received 2025-07-02; accepted 2026-01-19. [Publisher-independent full PDF hosted by Princeton ZERO Lab](https://zero.lab.princeton.edu/wp-content/uploads/2026/02/Schwartz-et-al.-2026-Valuing-Maintenance-Strategies-for-Fusion-Plants-as-Part-of-a-Future-Electricity-Grid.pdf).

**Evidence class:** Peer-reviewed primary research; GenX electricity-system scenario analysis, not measured fusion-plant operating data.

**Genuine novelty:** The paper models scheduled maintenance explicitly in a 2050 decarbonized U.S. Eastern Interconnection. Its scenario includes 100 GW of net-nameplate fusion capacity, 563 resource clusters across 20 zones and hourly dispatch. The paper finds that seasonal scheduling can make plant value up to 15% higher than a naive value estimate proportional only to annual availability. Some cases favor replacing fractions of a blanket in shorter blocks across multiple years over one longer outage, even when average availability is lower. It also models parasitic power during maintenance and finite blanket cost/durability in later sections.

**Important model assumptions and limits:**
- The paper uses scenario-specific electricity-price time series and a GenX capacity-expansion/operations model; it does not measure a commercial plant.
- The modeled operating parasitic loads include 5% active and 10% passive fractions of gross capacity; maintenance-period passive load is varied at 0%, 50% and 100%. The authors characterize the selected loads as optimistic relative to contemporary designs.
- The headline 15% is a marginal-value result in the modeled market, not a 15% LCOE reduction, not a net-electricity measurement and not a universal maintenance multiplier.
- Blanket replacement cost/durability, maintenance duration and start/stop time are scenario inputs. Actual component irradiation damage, remote handling, hot-cell cost, recommissioning and plant-specific schedules still require engineering evidence.
- The study does not close fuel-cycle, licensing, decommissioning or complete lifecycle finance for a real UQPU-relevant plant.

**Exact project relevance:** FUS-001/INV-032 should model maintenance calendar, outage duration/frequency, partial versus whole-component replacement, component durability and replacement cost, parasitic draw during outages, recirculating power during operation, seasonal dispatch value, remote-handling time and net delivered MWh together. Annual availability alone is insufficient.

**Falsifiable follow-up:** Pin the GenX version and input data; reproduce one published maintenance case; vary maintenance start month, block duration/frequency, replacement fraction/cost, blanket full-power-year durability, restart time and maintenance parasitic load. Compare (a) naive availability scaling, (b) price-aware scheduling and (c) a full capacity-expansion solution. Report net MWh, gross/net power, annualized replacement cost, total system value and sensitivity. Do not promote scenario output beyond MODEL_ONLY until independently reproduced and calibrated to measured component/plant data.

## 2. 1cFE — open costing software and target-backcasting screen

**Initiative:** [1¢/kWh Fusion Energy](https://1cf.energy/), an Astera Institute-supported techno-economic residency. The official site states that the residency concluded in September 2026 and that its publications, models and tools remain available. Original website content is labelled CC BY 4.0; the two inspected code repositories declare MIT.

**Open-source pins:**
- [1costingfe](https://github.com/1cFE/1costingfe/tree/44434d9fa95a1105621edc9927a8abe587703e81), inspected at commit `44434d9fa95a1105621edc9927a8abe587703e81`; [MIT license](https://github.com/1cFE/1costingfe/blob/44434d9fa95a1105621edc9927a8abe587703e81/LICENSE).
- [one-cent-envelope](https://github.com/1cFE/one-cent-envelope/tree/b317102fcd19ae63ac7a49712ec924ef64d00e33), inspected at commit `b317102fcd19ae63ac7a49712ec924ef64d00e33`; [MIT license](https://github.com/1cFE/one-cent-envelope/blob/b317102fcd19ae63ac7a49712ec924ef64d00e33/LICENSE).

**Genuine novelty:** The envelope makes several finance and net-output drivers explicit in one screening equation:

[
E=8.76,CF,quad
CRF=\frac{r}{1-(1+r)^{-L}},quad
IDC=\frac{(1+r)^T-1}{T\ln(1+r)},quad
SFF=\frac{r}{(1+r)^N-1}
]

[
LCOE=\frac{C(CRF\cdot IDC+s\cdot SFF)}{E(1-f)}+\frac{F}{E}+V.
]

Here (f) is the recirculating fraction, (r) real cost of capital, (T) construction time, (L) plant life, (CF) capacity factor, (s) replacement share and (N) replacement interval; (C,F,V) are gross-capital, fixed-O&M and variable-O&M/fuel inputs. This makes gross-to-net conversion, financing during construction, recurring replacement, availability and O&M visible rather than hiding them in a single headline number.

The 1costingfe README describes a five-layer, customer-first costing framework with multiple confinement concepts and fuels, CAS cost accounts, sensitivity/backcasting and annualized scheduled replacement (CAS72). Its pinned source declares `SIZING_FEATURES_ENABLED = False` and `MODELS_0D_ENABLED = False` for the released build: it therefore costs a supplied physics operating point rather than proving a self-consistent reactor design or deriving a validated plasma solution in that release.

**Limits:** The envelope explicitly excludes taxes, decommissioning, land, fuel-price risk, grid/firming costs and heat/other-product revenue. Both repositories are models/tools, not plant measurements or validated commercial forecasts. Default assumptions, units, cost-account provenance, fuel cycle, component lifetime, uncertainty and physics consistency require independent audit. No external test suite was run in this cycle.

**Exact project relevance:** FUS-001 should use these as reproducibility targets and comparison structures, not as adopted truth. The full project envelope must additionally include tritium breeding/fuel cycle, neutron damage, remote maintenance, cooling, grid interfaces, decommissioning, construction schedule, component replacement, uncertainty and financing. FIN-001 should keep principal, interest, construction-time lock-up and cost-of-capital parameters separate.

**Falsifiable follow-up:** At the pinned commits, install cleanly, run the declared tests and reproduce one documented example. Independently recompute the envelope equation with unit/limit tests; compare gross/net output, recirculating fraction, CRF, IDC, SFF and replacement discounting against 1costingfe. Audit every default input and cost account to a primary source. Record all divergences as counterexamples; no model result is commercial evidence.

## 3. Banco de España Working Paper 2628 — innovation hurdle rate versus financial cost of capital

**Source:** Craig A. Chikis, Jonathan Goldberg and David López-Salido, “The innovator’s risk premium: Sticky hurdle rates, the cost of capital, and creative destruction,” Banco de España Working Paper 2628, dated 2026-09-22. [Official publication and abstract](https://www.bde.es/wbe/en/publicaciones/analisis-economico-investigacion/documentos-trabajo/the-innovators-risk-premium-sticky-hurdle-rates-the-cost-of-capital-and-creative-destruction.html).

**Evidence class:** Official central-bank working paper; theoretical/calibrated model, not a UQPU financing observation and not peer-reviewed journal evidence.

**Genuine novelty:** The paper distinguishes firms’ internal investment hurdle rates from their financial cost of capital. Its model attributes a widening gap to an innovator’s premium for undiversifiable innovation risk and imperfect pledgeability of innovation profits. In the model, higher undiversifiable risk can lower the financial cost of capital while hurdle rates remain sticky or rise. This warns against treating a lower hurdle rate, lower WACC, lower debt coupon and lower absolute interest as interchangeable outcomes.

**Limitations:** The paper is a calibrated Schumpeterian model, not an estimate for KitvisetLabs, a quantum-computing project or fusion project. It does not establish that any UQPU intervention lowers WACC or the economy-wide interest rate. The full PDF was linked by the publisher but timed out during this retrieval; only the official publication page and abstract were reviewed.

**Exact project relevance:** FIN-001/INV-033 must separately measure financed principal, debt coupon/interest cashflows, financial cost of capital/WACC, internal hurdle rate, innovation/project risk premium, collateral/pledgeability, working capital and time-to-evidence. A reduction in principal directly lowers absolute interest at unchanged terms; a change in hurdle rate or risk premium needs separate financing evidence.

**Falsifiable follow-up:** Build a project-level financing ledger with dated capital tranches, debt/equity mix, outstanding principal, actual coupon/fees, interest schedule, WACC method, internal hurdle rate, stage-gate decisions, collateral/pledgeability and evidence dates. Test whether shorter time-to-evidence or lower technical risk changes actual financing terms or only internal hurdle rates. Keep principal and rate effects as separate causal hypotheses.

## 4. Cross-pillar disposition

- **FUS-001 / INV-032:** maintenance and replacement schedules, recirculating power and financing now have better public model structures; no net reliable fusion electricity or commercial cost is demonstrated.
- **FIN-001 / INV-033:** hurdle-rate versus financial-cost-of-capital separation is strengthened; no UQPU principal, interest, WACC or risk-premium reduction is measured.
- **BIO-001 / INV-030/031:** no new Pangola-specific feedstock, carbon substitution, accepted liquid-fuel yield or cost evidence was found in this pass. Existing flash-Joule literature remains a transfer hypothesis only.
- **INV-029:** no data-center-to-phone service, physical-compression, energy or lifecycle-cost gate is passed.
- **INV-034/035:** no new physical law or equation is proposed. Current physics remains binding; all AI-discovered alternatives remain hypotheses until full falsification and independent validation.

No paid provider job, fusion experiment, hazardous test or commercial claim is authorized by this literature watch.
