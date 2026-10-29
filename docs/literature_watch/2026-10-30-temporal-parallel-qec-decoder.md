# Literature watch — temporal-parallel Union-Find decoder hardware

**Review date:** 2026-10-30  
**Primary source:** Leo Itoh, Takuya Kasamura, Hidetsugu Irie and Junichiro Kadomoto, “Design of a Quantum Error Correction Decoder Exploiting Temporal Parallelism,” arXiv:2607.27930, submitted 2026-07-30.  
**Official source:** https://arxiv.org/abs/2607.27930  
**Evidence class:** EXTERNAL PREPRINT / RTL SIMULATION + LOGIC-SYNTHESIS ESTIMATES; NOT INDEPENDENTLY REPRODUCED BY UQPU  
**Primary owner:** Lane B — QPU/provider integration  
**Interfaces:** A workload correctness and deadline; C syndrome buffering/I/O; D device implementation; F evidence and economics; G process/equipment/yield; H publication. INV-034/035 remain cross-cutting.

## Why this is a new-to-main literature delta

The paper describes a hardware-oriented sandwich decoder: temporal windows are decoded in parallel using Union-Find, with a window dispatcher/ring buffer, two Type-1 decoders, seam pairing, a Type-2 boundary decoder and result merger. The novelty for this repository is the explicit RTL microarchitecture and matched synthesis comparison against a conventional batch Union-Find decoder, not a new physical law or a demonstrated UQPU speedup.

## Source-reported results, with evidence boundaries

- RTL cycle-count evaluation used Verilator and Stim-generated noise; threshold estimates used a Rust simulator. ASIC figures were obtained through logic synthesis using Synopsys Design Compiler for TSMC CMOS 22 nm and the ASAP7 predictive 7 nm process. These are not measurements from fabricated silicon.
- At code distance d=21 and phenomenological physical error rate p=1%, the paper reports approximately 34.9% lower mean latency and 11.5% lower worst-case latency for the sandwich decoder relative to batch Union-Find.
- At p=0.1%, the reported mean latency reduction remains about 34.6%, but worst-case latency increases by 7.2%. Therefore average latency alone is an unsafe acceptance metric.
- Under phenomenological noise, reported thresholds are about 1.6% for batch Union-Find and 1.5% for sandwich Union-Find. Under the paper's circuit-level model, both are about 0.25%; its PyMatching comparison is about 0.78% under that model. These are paper-specific simulated estimates and must not be pooled across noise models.
- The sandwich design's synthesized area is reported as roughly 1.3–1.5 times the batch design. At d=23, batch-decoder synthesis failed on the authors' synthesis host after a 450 GB virtual-memory limit was reached; this is a tooling/resource failure, not proof of a fundamental scaling limit.

Source locations: the paper's evaluation environment and noise models are in Sections V-A/V-B; cycle-count and synthesis results are in Sections V-C/V-D. The primary source is linked above.

## Exact UQPU relevance

- **A:** add decoder deadline and accepted logical-output correctness to useful-task contracts; average latency is insufficient.
- **B:** keep decoder family, source revision, provider/target, noise model and execution path pinned. A decoder result does not prove a QPU workload succeeded.
- **C:** account for ring-buffer capacity, syndrome bytes, FIFO/seam storage, transfer and reconstruction; no Hilbert-space/readable-memory equivalence is implied.
- **D/G:** co-design decoder architecture with process node, clock, area, memory structures, yield, test and packaging. A synthesized process target is not fabricated-device evidence.
- **F:** compare latency distributions, logical error rate/threshold, area, power, memory and cost under identical inputs; do not mix source probabilities with unrelated prices.
- **E/H:** no direct biomass, bio-oil, fusion, financing or industrial-economics result follows. Any downstream electricity/capital consequence needs measured system inputs and separate lifecycle accounting.

## Falsifiable follow-up

1. Retrieve the exact upstream RTL, simulator, scripts and license; pin revision and SHA-256 hashes for source, Stim-generated samples, configuration, tool versions and PDK.
2. Reproduce the paper's batch-versus-sandwich comparison on identical syndrome instances, first at d=21 and then the d=23 stress case. Keep phenomenological p=1% and p=0.1% separate; evaluate circuit-level noise separately.
3. Report mean, p95, p99 and worst latency, deadline-miss fraction, logical failure rate with uncertainty, maximum frequency, area, buffer/FIFO bytes, power if measurable, tool resource use and failed runs.
4. Check equivalence between software decoder, RTL simulation and synthesized implementation; preserve all counterexamples and failed reproductions.
5. Require independent reproduction and physical FPGA/ASIC measurements before promoting any device-level claim. Reject the speedup hypothesis if worst-case deadline misses or logical error rates worsen beyond the declared contract, or if area/power/maintenance costs erase the system benefit.

## Nonclaims

This source does not demonstrate a real UQPU decoder, quantum advantage, GPU/NPU or memory replacement, 100x/100,000,000x economics, a new physical law, Pangola material substitution, saleable low-cost bio-oil, net fusion electricity, lower WACC, or Data-Center-to-One-Phone compression. Current physical and causal constraints remain binding.
