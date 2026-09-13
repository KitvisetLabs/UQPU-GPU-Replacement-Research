# PRIORITY RESEARCH PROGRAM — QUANTUM / HYBRID AI TRAINING COST COMPRESSION

## Moonshot objective: US$10–100 trillion ambition-scale infrastructure -> tens of thousands of Thai baht

**Status:** Active priority research / moonshot target / not demonstrated  
**Primary lane owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lane dependencies:** Lane B (QPU/provider execution), Lane C (memory/data movement), Lane D (device feasibility), Lane F (economics/benchmark/evidence)  
**Program gate:** `AI-COST-003` ideal VQC reproduction + hybrid readout repair completed; next `AI-COST-003B/003C` and `AI-COST-004`  

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** literature triage, cost-compression formulation, necessary-condition analysis, classical accepted-capability baseline/resource ledger, public VQC reproduction, readout-interface audit/repair, executable tests/results and research documentation.

Attribution describes roles in this program and does not assign work beyond contributions actually performed.

## Mission

Investigate whether AI-training and AI-service capability that would conventionally be associated with an **ambition-scale infrastructure-value proxy of approximately US$10 trillion to US$100 trillion** can eventually be delivered by an end-to-end system whose total lifecycle cost is only **tens of thousands of Thai baht**.

This number is deliberately extreme. It is a research target, not a forecast.

The US$10–100 trillion figure is an **owner-defined ambition-scale proxy**. It is **not** a claim that any single existing data center presently costs or is valued at US$10–100 trillion.

A valid success claim must preserve an explicit functional contract: model capability/quality, training data, accepted-output quality, training or adaptation time, inference/service requirements, reliability, memory/state, networking, energy, hardware lifetime and all required external infrastructure. A phone or compact device acting merely as a terminal to a remote data center does not satisfy the physical-compression target.

## Why the old 100,000,000x target is not enough for the canonical example

Batch 038 freezes an accounting snapshot of `33.045 THB/USD` on 2026-09-13 only for reproducible arithmetic. Using a canonical target of `50,000 THB` gives about `US$1,513.09`.

Therefore:

- `US$10 trillion -> 50,000 THB` requires approximately **6.609 billion-fold** cost compression.
- `US$100 trillion -> 50,000 THB` requires approximately **66.09 billion-fold** cost compression.

Thus `100,000,000x` remains a useful intermediate moonshot but is insufficient for this stricter canonical objective.

## Necessary-condition gate

Let `r` be the fraction of baseline end-to-end cost that remains classical/non-accelerated, and let `S` be the speedup or cost reduction applied to the accelerated fraction. The normalized cost is

`C_new / C_base = r + (1-r)/S`.

Even with an infinitely cheap accelerated component (`S -> infinity`), the end-to-end floor is `r`.

For the canonical `50,000 THB` target:

- from a `US$10 trillion` proxy, `r` must be no larger than about `1.5131e-10`;
- from a `US$100 trillion` proxy, `r` must be no larger than about `1.5131e-11`.

This means a quantum accelerator that leaves ordinary data loading, memory, networking, control, readout, energy, cooling, hardware amortization or other infrastructure at conventional cost fractions cannot reach the moonshot merely by making one compute kernel faster.

## Research families to pursue

Lane A may investigate, reproduce, combine or invent approaches including:

1. quantum algorithms for training classical neural networks where rigorous complexity assumptions can be exposed;
2. quantum linear-algebra / optimization primitives with complete state preparation and readout;
3. parameterized quantum circuits with backpropagation-like gradient scaling and explicit trainability tests;
4. quantum kernels / feature maps with provable learning advantage on well-defined task families;
5. quantum reservoir / physical neural computing where training is shifted to inexpensive classical readout layers;
6. native-quantum-data learning, where expensive classical-to-quantum loading may be avoidable;
7. QRAM/resource-state memory and streaming/state-preparation architectures;
8. hybrid quantum-classical training pipelines that compress optimizer state, activations, communication, memory and data movement rather than accelerating FLOPs alone;
9. new mathematically explicit algorithms invented inside UQPU, provided every claimed advantage is falsifiable and benchmarked against competitive classical methods.

## Evidence ladder

No approach may be promoted directly from an asymptotic theorem or simulator result to a moonshot cost claim.

Required progression:

`literature/theory -> executable toy reproduction -> competitive classical baseline -> data-loading/readout contract -> memory/I/O contract -> logical-resource estimate -> fault-tolerant/physical-resource estimate -> measured or defensibly priced system -> end-to-end accepted-capability cost`.

## Current reproducible baseline — Batch 039 / AI-COST-002

The first classical accepted-capability comparison point is frozen in `docs/BATCH_039_AI_COST_002_CLASSICAL_BASELINE.md` and `benchmarks/results/batch039-ai-cost-002-classical-baseline.json`.

It uses a deterministic non-linear XOR-quadrant task with a pure-Python dense `2 -> 16 -> 1` MLP, 65 parameters, 256 training examples, 256 held-out examples and 800 full-batch epochs. The accepted-capability contract is held-out accuracy `>=0.98` and BCE `<0.19`; the frozen reference reached `0.98046875` held-out accuracy and `0.17734677266198473` BCE.

The baseline additionally freezes exact source-level arithmetic/nonlinear counts and logical FP64 payload/traffic proxies. Runtime measurement is kept separate from energy/cost assumptions. Any quantum/hybrid route must use the same task/quality semantics or document and justify an equivalent reformulation, and it must count state preparation, shots/readout and classical residual work rather than comparing only an isolated quantum kernel.

This toy baseline is a **benchmark-contract scaffold**, not a frontier-model baseline or evidence that the moonshot is close to being achieved.

## First quantum/hybrid comparison — Batch 040 / AI-COST-003

Batch 040 reproduces the public two-qubit VQC architecture from Seilkhan & Taizhanov (`arXiv:2602.24220v1`, public code pinned at `d7dd995db6a19295235c48483fe1abb108d9022d`) against the exact Batch-039 task/quality contract using an independent pure-Python ideal-statevector implementation.

The depth-2 public `<Z0>` route obtains held-out accuracy `0.95703125` and BCE `0.37888043300038676`, so it **fails** the frozen `>=0.98 / <0.19` accepted-capability gate in this UQPU reproduction.

The interface audit identifies an exact structural issue: for the final layer, four nominal parameters `[8,9,10,11]` have zero influence on `<Z0>` under the published `CNOT(0->1)` measurement interface. Replacing the readout with parity `<Z0 Z1>` reduces the exactly inactive final-layer tail to `[8,11]` and raises held-out accuracy to `0.9921875`, although raw BCE remains `0.3774990388898494`.

A minimal two-scalar classical calibration `p=sigmoid(a*m+b)`, fitted on training expectations only, then yields held-out accuracy `0.984375` and BCE `0.12508869380594245`. Therefore the **toy accepted-capability quality contract is reached in ideal simulation by the repaired hybrid readout**.

This is not a cost advantage. A straightforward 12-parameter parameter-shift deployment would require a circuit-equivalent ledger of `1,600,000` training circuit evaluations for the frozen 256-example / 250-epoch route, corresponding to `204,800,000` shots at 128 shots/circuit or `1,638,400,000` shots at 1,024 shots/circuit before retries, QEC/error mitigation, reset/readout, queueing or host/control overhead. These counts are resource-pressure proxies, not measured hardware costs and not proof that parameter-shift is optimal.

Canonical note: `docs/BATCH_040_AI_COST_003_VQC_REPRODUCTION_AND_READOUT_REPAIR.md`.

Next research must attack both sides simultaneously:

- `AI-COST-003B`: independently reconstruct the parity candidate in Qiskit/PennyLane and quantify finite-shot/noise degradation;
- `AI-COST-003C`: reduce the training circuit-evaluation burden under the same accepted-capability contract;
- `AI-COST-004`: map and destroy residual end-to-end cost across loading, readout, control, memory, communication, energy and lifecycle infrastructure.

## Non-claims

This program does **not** currently demonstrate:

- a US$10–100 trillion data center compressed to tens of thousands of baht;
- a 6.6-billion-fold or 66-billion-fold realized cost advantage;
- a 100,000,000x realized advantage;
- general AI/LLM training on a real QPU;
- quantum advantage for practical frontier-model training;
- cheaper quantum/hybrid training than the Batch-039 classical baseline;
- GPU/NPU/RAM/DRAM/HBM replacement;
- a real-QPU end-to-end economic advantage;
- a new physical law.

Negative/no-go results are first-class outputs. If a cost floor rules out the target under a particular architecture, the program must publish that result rather than hide it.
