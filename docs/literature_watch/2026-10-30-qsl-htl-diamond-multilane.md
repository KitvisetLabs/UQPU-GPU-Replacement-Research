# Cross-lane literature watch — 2026-10-30 — quantum speed limits, HTL optimization and foundry quantum photonics

**Date observed:** 2026-10-30  
**Primary owner:** Lane H — literature provenance and publication  
**Cross-lane owners:** A/B/C/D/F (quantum speed-limit and computation implications); D/G (quantum-photonic manufacturing); E/F (biomass liquid-energy and economics)  
**Purpose:** record material sources newly verified against the canonical main branch. External literature is not UQPU project evidence.

## 1. Coherence-resolved quantum speed limits

**Source:** Xuhui Xiao, Hai Wang and Xingze Qiu, “Coherent quantum speed limits,” *Physical Review A* 113, 032438, published 2026-03-24.  
**Publisher record:** https://journals.aps.org/pra/abstract/10.1103/rdpr-db6m  
**DOI:** https://doi.org/10.1103/rdpr-db6m  
**Related preprint:** arXiv:2401.01746.  
**Evidence class:** PEER-REVIEWED THEORETICAL RESULT; abstract-level review; no UQPU reproduction.

The paper derives families of unitary-dynamics bounds using Schatten-p-norm and Hellinger-distance coherence measures defined relative to the instantaneous energy eigenbasis. Its stated contribution is to separate a coherence-dependent kinematic resource from the Hamiltonian energy scale. The Landau–Zener/shortcut-to-adiabaticity example is a theoretical illustration, not a UQPU runtime measurement. The underlying idea has a 2024 preprint history; the 2026 journal record is not presented as a newly invented physical law.

**UQPU relevance:** FND-003 should distinguish energy-scale bounds from coherence-dependent bounds when defining a matched control-versus-quantum experiment. A useful-output comparison must record the state, Hamiltonian, instantaneous basis, coherence measure, energy dispersion, target-state distance, control duration and wall-plug resources. A coherence measure is not itself a speedup or an engineering resource saving.

**Limitations:** the full APS text was not available in this surveillance pass. Definitions, theorem assumptions, equality conditions and the exact relation to conventional Mandelstam–Tamm/Margolus–Levitin bounds require full-text reconstruction. No device data, accepted-task advantage or new physical limit is claimed.

## 2. Saturable speed limit for imaginary-time evolution

**Source:** Kohei Kobayashi, “Saturable quantum speed limits for imaginary-time evolution,” *Physical Review A* 113, 032618, published 2026-03-19.  
**Publisher record:** https://journals.aps.org/pra/abstract/10.1103/bln8-8xzy  
**DOI:** https://doi.org/10.1103/bln8-8xzy  
**Related preprint:** arXiv:2508.10361.  
**Evidence class:** PEER-REVIEWED THEORETICAL RESULT; abstract-level review; no UQPU reproduction.

The paper gives a geometric bound for a non-unitary imaginary-time Schrödinger evolution, using angular distance between normalized states and time-averaged energy dispersion. It reports a saturability condition when the evolution direction follows a projective-space geodesic, with analytic examples including a two-level system and imaginary-time Grover search.

**UQPU relevance:** this is a candidate comparator for FND-003 and any future imaginary-time/ground-state-search workload. Imaginary algorithmic time must never be equated with physical wall-clock time. Any implementation must account for normalization, postselection or ancilla overhead, state preparation, sampling, classical control, retries, success probability and total energy/cost per accepted output.

**Limitations:** the full APS text was not reconstructed. The bound applies to the specified non-unitary evolution model; it does not bypass unitary hardware limits or establish a physical implementation with zero overhead. No QAOA, QPU or useful-output advantage is shown.

## 3. Multiobjective HTL optimization for microalgae

**Source:** Sergio Martinez-Villarreal, Benoît Dochy, Isabelle Van De Vreken, Konstantina Vasilakou, Philippe Nimmegeers and Aurore Richel, “Multiobjective Optimization of the Hydrothermal Liquefaction of Microalgae for Cost-Effective Advanced Biofuels Production,” *Industrial & Engineering Chemistry Research* 65(27), 14446–14460.  
**Published online:** 2026-06-30; issue date 2026-07-15.  
**Publisher record:** https://pubs.acs.org/doi/10.1021/acs.iecr.6c00395  
**DOI:** https://doi.org/10.1021/acs.iecr.6c00395  
**Evidence class:** PEER-REVIEWED PROCESS-OPTIMIZATION / PROCESS-SIMULATION / TECHNO-ECONOMIC STUDY; external; full text and supporting information not independently audited.

The publisher abstract describes a multivariable framework combining experimental design, process simulation and techno-economic analysis to optimize the yield/quality/economics trade-off. It reports distinct temperature/residence-time optima by scale: 287 °C/30 min for small capacity and 304 °C/12 min for upscaled capacity. Relative to yield-based optimization, the reported minimum fuel selling price (MFSP) falls 5.16% and 19.27%, respectively, and hydrotreatment hydrogen demand falls by up to 4.50%. The abstract still reports high MFSP values of 13.04 €/L and 3.77 €/L, with material economic uncertainty.

**UQPU relevance:** BIO-001 should optimize accepted final-liquid quality and cost, not raw bio-crude yield alone. The study is a useful objective-function and scale-dependence comparator for Lane E/F and process-equipment design in D/G.

**Limitations:** microalgae are not Pangola or the project's local agricultural residue. No feedstock transfer, commercial Pangola price, net-energy gain or project cost follows from the abstract. The article and supporting information must be reconstructed before using its response surfaces, hydrogen, cost or scale assumptions.

## 4. Foundry-enabled diamond quantum microchiplets

**Source:** Jawaher Almutlaq et al., “Foundry-Enabled Patterning of Diamond Quantum Microchiplets for Scalable Quantum Photonics,” *Nano Letters* 26(26), 8474–8481.  
**Published online:** 2026-05-07; issue date 2026-07-08.  
**Publisher record:** https://pubs.acs.org/doi/10.1021/acs.nanolett.6c01048  
**DOI:** https://doi.org/10.1021/acs.nanolett.6c01048  
**Related preprint:** arXiv:2601.20025.  
**Evidence class:** PEER-REVIEWED FABRICATION DEMONSTRATION; abstract and supporting-information metadata reviewed; no UQPU reproduction.

The reported process uses high-precision silicon masks fabricated in commercial foundries and transferred to diamond by microtransfer printing. The abstract reports hundreds of diamond quantum microchiplets, controlled coupling to quantum emitters, improved optical performance and a replaceable-chiplet route for heterogeneous integration. The authors disclose relevant company-founder interests; this must be retained in provenance review.

**UQPU relevance:** a concrete D/G co-design example: move demanding pattern definition into a mature foundry flow, transfer the patterned structures to a specialized material, then qualify chiplet-level optical performance, packaging and replaceability. It is a useful manufacturing hypothesis for photonic integration, not a generic recipe for superconducting, silicon-spin or every quantum modality.

**Limitations:** the abstract does not provide enough information to quantify production yield, throughput, defect density, transfer yield, reliability, cost per good chiplet or system-level quantum advantage. The full paper and supplement were not independently audited; no UQPU equipment/process result is claimed.

## 5. Cross-lane synthesis and falsifiable follow-up

- **FND-003 / A-D:** reconstruct both QSL theorems from full text; compare assumptions, dimensions, equality conditions and limiting cases. Test coherence-dependent bounds on held-out Hamiltonian families. Keep imaginary time distinct from physical time and account for every implementation overhead.
- **BIO-001 / E-F-G:** retrieve the HTL paper and supplement; reconstruct response surfaces and MFSP; compare yield-only versus accepted-liquid objective functions; then run matched Pangola HTL/pyrolysis experiments with complete mass, energy, upgrading, hydrogen, catalyst-life, utility, CAPEX/OPEX and logistics ledgers.
- **D/G:** retrieve the diamond paper and supplement; record mask dimensions, transfer yield, resonance distributions, emitter-coupling statistics, optical loss, defect/replacement rate, packaging and cost per qualified chiplet. Compare against direct-on-diamond fabrication using identical acceptance criteria.
- **F/H:** do not turn literature cost scenarios into project economics. Tie future financing to measured milestone cashflows, financed principal, absolute interest, capital lock-up time and risk; estimate hurdle-rate/WACC changes separately.

**Non-claims:** no new physical law, QPU advantage, Pangola material/fuel result, commercial fusion electricity, measured financing improvement or Data-Center-to-One-Phone milestone is established.
