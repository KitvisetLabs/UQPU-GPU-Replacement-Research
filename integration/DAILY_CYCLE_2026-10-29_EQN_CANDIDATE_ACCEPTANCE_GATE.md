# Daily integration — 2026-10-29 — accuracy-plus-stability equation-candidate gate

**Starting main:** 17e3c8ff96d4dc7a95001e39186387cf8ccca28d  
**Primary owner:** Lane A  
**Integration/evidence owner:** Lane F  
**Literature/provenance owner:** Lane H  
**Evidence class:** SOFTWARE_DIAGNOSTIC / MODEL_ONLY

## Integrated change

The existing equation-stability proxy is now paired with an explicit candidate acceptance function. Held-out normalized RMS error, separately measured perturbation amplification, constraint violations and numerical failures are all gates; no one metric can compensate for another. A constant candidate with zero sensitivity is a mandatory negative control. The helper is not EIC and does not validate physical semantics.

## A–H interfaces

- A supplies candidate outputs, held-out references and preregistered scales/thresholds.
- B contributes no execution claims; provider routes and paid-job consent gates are unchanged.
- C retains separate classical output, state, memory, transfer and reconstruction accounting.
- D retains the molecular spin–photon replication gate; no new device measurement.
- E retains INV-030/BIO-001/FUS-001 function and net-energy gates.
- F owns acceptance, false-discovery and matched-resource accounting.
- G keeps D/G process/yield/cost co-design open.
- H maintains source provenance, literature deduplication and the strategic/multilingual plan.

All 28 A–H pairs were reviewed. INV-034/035 feed every lane. FND-006 and EQN-002/EQN-004 gain a stronger candidate-evaluation gate only; FND-001–005 and the remaining EQN-001–006 program stay evidence-gated.

## Mission boundary and sync

INV-029–033 remain goals with no newly demonstrated physical-compression, material, accepted-fuel, net-fusion-electricity, or finance advantage. INV-025/026/027 and INV-036/037 remain preserved. README, integration index, scoreboard, living gap register and work log are synchronized in one commit. Exact-head CI is pending. No paid QPU job was submitted.

**Next gate:** exact-head Actions, then frozen family-disjoint known-law tests with null/constant and ill-conditioned controls under equal budgets.
