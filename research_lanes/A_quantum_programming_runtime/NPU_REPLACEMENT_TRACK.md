# NPU Replacement Research Track

**Primary owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lane interfaces:** B, C, D, F, G, H  
**Status:** CONCEPT / RESEARCH_PROGRAM / NOT_YET_DEMONSTRATED

## Permanent objective

Develop and test quantum/UQPU execution paths that can replace useful workloads currently assigned to Neural Processing Units (NPUs), including the extreme moonshot hypothesis that **one quantum computer or one logically unified UQPU system could replace the accepted useful-work capacity of approximately 100,000,000 competitive NPUs** for a suitable workload class, while targeting **>=100,000,000x lower total financial cost per accepted useful task**.

This is a research target, not a statement of present capability.

## What counts as NPU equivalence

NPU replacement must be judged by useful neural-application behavior, not theoretical TOPS.

An equivalence contract should freeze at least:
- model architecture and model/version hash;
- weights/checkpoint identity where applicable;
- input/output semantics and preprocessing/postprocessing;
- numeric precision, quantization and tolerances;
- task quality metric and acceptance threshold;
- batch size, sequence length and/or tensor shapes;
- latency SLO and useful throughput;
- memory footprint and memory/data-movement requirements;
- host orchestration and accelerator-support requirements;
- energy and total financial cost per accepted output.

For training/fine-tuning workloads, additionally freeze dataset/version, optimizer, convergence/quality target, update rule and time-to-target.

## Quantum-programming hypotheses to investigate

The research program may test multiple routes without assuming any will win:

1. **Quantum-native subproblem replacement** — identify neural workloads containing sampling, search, kernel, optimization or structured linear-algebra subproblems where a QPU can change the cost scaling.
2. **Semantic compilation** — transform the requested AI outcome rather than emulate NPU matrix instructions gate-for-gate.
3. **Hybrid elimination of intermediate tensors** — reduce classical activation/materialization/data-movement when the application contract allows it.
4. **Quantum feature/kernel or generative paths** — test only where equal-output quality and end-to-end cost can be measured.
5. **Fault-tolerant algorithm path** — separately model future logical-QPU algorithms when current NISQ hardware cannot satisfy the contract, with explicit QEC/resource estimates.
6. **Open-frontier path** — retain mathematically/physically plausible new algorithms or encodings under INV-027, with falsifiable scaling claims and no promotion of speculation to evidence.

## Evidence ladder

CONCEPT -> MODEL_ONLY -> SIMULATION -> SDK/TARGET-VERIFIED -> REAL_QPU -> ACCEPTED_OUTPUT -> COMPETITIVE_NPU_BASELINE -> END_TO_END_COST -> VERIFIED_ADVANTAGE

The 100-million-NPU / >=100-million-times-cost target can only be marked achieved after the final stages include equivalent accepted output, throughput/latency and complete full-stack accounting.

## Near-term benchmark program

Start with small reproducible neural contracts before scaling:
- inference workload with fixed model, test set and quality threshold;
- similarity/attention/search subproblem with end-to-end decoding;
- small optimization/training subproblem where the same final task quality can be checked;
- classical CPU/GPU/NPU baseline ladder using established optimized runtimes;
- QPU simulator/dry-run followed by bounded authorized real-QPU execution when credentials and budget permit.

## Explicit non-claims

- Qubit count is not equivalent to NPU TOPS.
- Hilbert-space dimension is not useful NPU throughput.
- A faster isolated quantum kernel is not NPU replacement if classical loading/decoding dominates.
- A simulation result is not a real-QPU advantage.
- A 10^8 target is not evidence that a 10^8 advantage currently exists.
