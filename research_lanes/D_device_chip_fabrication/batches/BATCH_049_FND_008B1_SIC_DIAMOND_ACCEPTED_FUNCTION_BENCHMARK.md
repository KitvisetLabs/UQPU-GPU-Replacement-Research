# Batch 049 — FND-008B1 SiC vs Diamond Accepted-Function Benchmark Sufficiency

**Status:** executable comparability/evidence gate  
**Primary lane:** Lane D — Device / Chip / Fabrication  
**Dependencies:** Lane E materials and process cost; Lane F benchmark/economics  
**Parent:** FND-008 Difference-to-Technology / Batch 048 prioritization  
**Date:** 2026-09-14

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: primary-source literature verification, accepted-function benchmark design, cross-paper comparability audit, executable gate/tests, frozen evidence result, documentation, PR/CI preparation and merge verification.

Attribution reflects roles in this batch only.

## Research question

Batch 048 ranked SiC spin defects ahead of diamond NV as the next **research action**, but explicitly did not claim SiC was already superior.

Batch 049 asks:

> **Does current public evidence already support an apples-to-apples SiC-vs-diamond spin-defect performance or end-to-end cost winner?**

The answer from this audit is **no**.

That is a useful result because superficially impressive numbers can be badly misleading when they mix single defects with ensembles, measured values with projected values, different frequency bands, different pulse protocols, different depths, different readouts, or incomplete hardware/cost boundaries.

## Permanent benchmark rule

```text
SAME ACCEPTED FUNCTION OR NO WINNER
```

A cross-platform winner claim requires, at minimum:

1. the same accepted function;
2. the same sensor class (`SINGLE_DEFECT` vs `ENSEMBLE`);
3. the same temperature regime;
4. the same AC/DC/protocol family;
5. overlapping declared frequency band;
6. matched defect-depth / geometry class;
7. direct measured sensitivity on both sides for a measured-performance winner;
8. equivalent acquisition/averaging/calibration rules;
9. disclosed readout and control chains;
10. for an economic winner, complete fabrication/yield/power/environment/lifecycle-cost boundaries on both sides.

If a field is unknown, that is not evidence that the field is equal.

## Current evidence audit

### SiC shallow single-divacancy sensing

The 2025 Nature Materials work on alkene-terminated 4H-SiC reports shallow single-divacancy operation at room temperature. It discusses an approximately `13 nT/sqrt(Hz)` sensitivity for an isotope-engineered single-divacancy sensor and an approximately `56 nT/sqrt(Hz)` anticipated value using observed non-optimized shallow-center parameters.

Source: https://www.nature.com/articles/s41563-025-02382-9

For this benchmark these are classified as **model-derived / anticipated from measured parameters**, not a directly matched head-to-head field-sensitivity experiment against diamond.

### Diamond shallow single-NV sensing

A 2025 Nature Communications interface-engineering study reports shallow-NV coherence improvement and calculates an AC magnetic sensitivity improvement from approximately `50` to `23 nT/sqrt(Hz)` from recorded parameters; CPMG can extend coherence beyond `1 ms`, with a calculated `16 nT/sqrt(Hz)` example under CPMG-64.

Source: https://www.nature.com/articles/s41467-025-61026-3

This is a valuable diamond datapoint, but its echo/AC protocol and geometry are not frozen to the same conditions as the SiC qNMR/pulsed-ESR example.

### Why the portable diamond number cannot be used to declare diamond the winner

A 2025 portable NV **ensemble** magnetometer reports a directly measured mean sensitivity `0.3 +/- 0.2 nT/sqrt(Hz)` in non-vector mode over `10-150 Hz`.

Source: https://www.sciencedirect.com/science/article/pii/S0925963525000020

This number is dramatically smaller than the single-defect SiC examples, but the comparison is invalid as a material winner because it changes the sensor class from one defect to an ensemble and changes the full instrument geometry/protocol.

### Electrical/readout technology is promising on both hosts

The 2025 SiC PDMR work demonstrates room-temperature coherent photoelectrical readout of a single silicon-vacancy spin and reports `1.7-2.0x` higher single-spin SNR than optimized optical readout for two measured defects within that experiment.

Source: https://www.nature.com/articles/s41467-025-58629-1

A separate 2025 diamond experiment demonstrates ambient coherent single-NV dynamics through surface-voltage/KPFM readout. Its signal response is on the order of `10 ms`, illustrating that electrical/non-optical readout has its own response-time and instrumentation tradeoffs.

Source: https://www.nature.com/articles/s41467-025-58635-3

Neither result by itself establishes a cross-host sensing or cost winner.

### SiC integration evidence

A 2026 npj Nanophotonics experiment integrates SiC V2 color centers into waveguides with photonic-crystal reflectors. Standard PLE count rates exceed `100 kcps`, approximately `125 kcps` is reported with a charge-resonance-check scheme, and the paper theoretically analyzes single-shot readout fidelity above `98%` under its cryogenic device conditions.

Source: https://www.nature.com/articles/s44310-026-00118-4

This strengthens SiC's integration case but cannot be mixed silently with room-temperature metrics; cryogenic infrastructure must be counted.

## Executable gate

`software/uqpu-prototype/uqpu/spin_defect_benchmark_gate.py` encodes the comparison contract. It rejects a performance winner if any required conditions are mismatched or missing. It separately requires a complete cost boundary for an end-to-end cost winner.

The frozen current cross-host audit contains **no pair that passes the performance-winner gate**.

Artifacts:

- `software/uqpu-prototype/uqpu/spin_defect_benchmark_gate.py`
- `software/uqpu-prototype/tests/test_spin_defect_benchmark_gate.py`
- `benchmarks/results/batch049-fnd-008b1-sic-diamond-benchmark-sufficiency.json`
- `benchmarks/external/fnd-008b1-sic-diamond-benchmark-provenance-2026-09-14.json`

## Result

Classification:

`SIC_DIAMOND_ACCEPTED_FUNCTION_BENCHMARK_SUFFICIENCY_GATE`

Evidence level:

`SOURCE_GROUNDED_COMPARABILITY_AUDIT`

The result is **not** “tie” and not “unknown which material is scientifically interesting.” It is more precise:

> **Current public evidence is not sufficiently matched to promote a SiC-vs-diamond end-to-end performance or cost winner under the project's evidence standard.**

This protects the project from optimizing against misleading cross-paper numbers while still identifying the exact experiment needed next.

## Next experimental fixture — FND-008B2

Run or reproduce a matched room-temperature **single-defect magnetic-sensing** fixture on both platforms with:

- same AC or DC protocol;
- same frequency band;
- matched defect-depth class;
- same acquisition/averaging rule;
- same calibration and accepted sensitivity target;
- direct measured sensitivity;
- laser/microwave/electrical-readout power ledger;
- readout latency and SNR;
- state preparation/control overhead;
- host/device fabrication and defect-yield ledger;
- temperature/environmental infrastructure;
- package/integration footprint;
- lifecycle cost per accepted sensing task.

A lower-cost abundant-material route may then be introduced only if it reaches the same accepted function.

## Non-claims

Batch 049 does not claim SiC beats diamond, diamond beats SiC, either host is cheaper end to end, a Pangola-derived device-grade diamond exists, a spin-defect UQPU exists, quantum advantage exists, >=100x or >=100,000,000x saving is achieved, or a new physical law has been established.
