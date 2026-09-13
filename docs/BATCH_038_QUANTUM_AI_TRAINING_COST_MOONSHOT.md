# Batch 038 — Quantum / Hybrid AI Training Cost Moonshot Gate

**Date:** 2026-09-13  
**Primary lane:** A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lane dependencies:** B / C / D / F  
**Gate:** `AI-COST-001`  
**Evidence level:** `ANALYTIC_ACCOUNTING_NECESSARY_CONDITION_WITH_LITERATURE_MAP`  
**Classification:** `AI_TRAINING_COST_MOONSHOT_NECESSARY_CONDITION_GATE_ESTABLISHED`

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** public-literature triage, cost-compression formulation, analytic necessary-condition derivation, executable implementation, test/result generation, evidence classification and research-note preparation.

Attribution describes roles in this batch only.

## Executive result

The project owner added a high-priority moonshot: investigate whether AI-training/service capability represented by an ambition-scale conventional-infrastructure proxy of **US$10 trillion to US$100 trillion** can eventually be delivered for only **tens of thousands of Thai baht**.

This is a target, not an observed result. The US$10–100 trillion range is an owner-defined ambition-scale proxy and is not asserted to be the market value or construction cost of any one existing data center.

Batch 038 establishes the first reproducible necessary-condition gate and shows that the existing `100,000,000x` moonshot is not sufficient for the stricter canonical example.

Using a frozen accounting snapshot of `33.045 THB/USD` and a canonical target of `50,000 THB`:

- target cost = `US$1,513.088213...`;
- `US$10T -> 50,000 THB` requires `6.609e9x` compression;
- `US$100T -> 50,000 THB` requires `6.609e10x` compression;
- `100,000,000x` compression would still cost `3,304,500 THB` from the US$10T proxy and `33,045,000 THB` from the US$100T proxy.

Therefore the research target has moved beyond an isolated 100-million-fold accelerator claim. Reaching the new moonshot requires end-to-end architectural compression.

## 1. Necessary residual-cost theorem for the accounting model

Split normalized baseline cost into

- a residual/non-accelerated fraction `r`, and
- an accelerated fraction `1-r` that receives reduction factor `S`.

Then

`C_new / C_base = r + (1-r)/S`.

As `S -> infinity`,

`C_new / C_base -> r`.

This is an Amdahl-style accounting identity, not a quantum-computing theorem. It yields a hard necessary condition for any architecture represented by this decomposition: the residual fraction itself must already lie below the total target fraction.

For `50,000 THB`:

- US$10T case: `r <= 1.5130882130428204e-10`;
- US$100T case: `r <= 1.5130882130428203e-11`.

A conventional-looking residual of only `1e-6` would produce an infinite-accelerator floor of

- `330,450,000 THB` for the US$10T baseline proxy;
- `3,304,500,000 THB` for the US$100T baseline proxy.

Thus speeding up matrix multiplication, gradient evaluation, attention or another dominant kernel is not enough if data loading, memory, communication, readout, classical control, energy/cooling or capital cost remain at ordinary fractions of today's end-to-end system.

## 2. Literature routes and what they actually support

### Quantum training of classical neural networks

Zlokapa, Neven and Lloyd (`arXiv:2107.09200`) give a quantum algorithm for a specified wide/deep neural-network setting and identify conditions under which sparse quantum linear-system methods can yield very strong training-set-size scaling. Importantly, the paper itself makes efficient state preparation and readout conditions part of the end-to-end speedup story. This makes the route relevant to UQPU, but not evidence that general LLM/frontier-model training is already exponentially cheaper.

Allcock et al. (`arXiv:1812.03089`) provide quantum feedforward-network training/evaluation algorithms with favorable network-dimension scaling under quantum memory/data-access assumptions. UQPU should reproduce a small instance, then price the memory/data-access contract rather than counting only algorithmic queries.

### Backpropagation and quantum gradients

Bowles, Wierichs and Park (`arXiv:2306.14962`) identify structured parameterized circuits whose gradient-estimation scaling can approach classical backpropagation and report roughly two orders of magnitude reduction in a toy 16-qubit training setting. This is valuable algorithm/interface evidence, not an end-to-end frontier-AI cost result.

Abbas et al. (`arXiv:2305.13362`) analyze the difficulty of reusing quantum information as classical backpropagation does and show that matching backpropagation scaling is impossible in their setting without access to multiple copies of a state. This is a direct warning that quantum training cost must include information-reuse/measurement structure.

### Trainability versus advantage

The 2025 Nature Reviews Physics barren-plateau review documents gradient suppression as a central trainability barrier. A 2025 Nature Communications perspective further collects evidence that several structures used to avoid barren plateaus may also enable classical simulation. UQPU therefore adopts a two-sided gate: **trainable is not enough; the trainable model must also resist competitive classical simulation where advantage is claimed.**

### State preparation / QRAM

The 2026 resource-state QRAM paper provides a current architecture for fast/error-correctable queries. It is relevant because many attractive QML complexities presume coherent data access. UQPU treats QRAM as a separately costed device/service, never as a free oracle.

### Rigorous task-specific QML advantage

Liu, Arunachalam and Temme (Nature Physics 2021) prove an end-to-end speedup for a constructed supervised-learning task with classical data access. A 2026 npj Quantum Information result generalizes how quantum computational advantages can induce QML advantages for defined task families. These results establish that rigorous learning advantages are possible in principle for particular problems; they do not establish cheap general-purpose frontier-model training.

## 3. Research portfolio for the moonshot

The next work is intentionally multi-route. Candidate routes include quantum linear-system training, structured quantum backpropagation, task-specific quantum feature maps, native-quantum-data learning, quantum reservoir/physical neural computing, QRAM/state-preparation co-design, optimizer-state compression, communication avoidance and new UQPU algorithms.

Every route is judged against the same end-to-end functional unit rather than FLOPs alone.

Required ledgers include at least:

- accepted model/task quality;
- training/adaptation wall time;
- data ingest and state preparation;
- optimizer/gradient work;
- activations/intermediate state;
- parameter storage/update;
- DRAM/HBM/SRAM/storage footprint;
- interconnect/network traffic;
- QPU logical and physical resources;
- QEC/error mitigation/shots/retries;
- classical host/control/readout;
- energy/cooling;
- hardware amortization, maintenance and financing;
- total cost per accepted trained capability.

## 4. Reproducible artifacts

- `00B_QUANTUM_AI_TRAINING_COST_COMPRESSION_MOONSHOT.md`
- `software/uqpu-prototype/uqpu/quantum_ai_training_cost_gate.py`
- `software/uqpu-prototype/tests/test_quantum_ai_training_cost_gate.py`
- `benchmarks/results/batch038-quantum-ai-training-cost-moonshot-gate.json`
- `benchmarks/external/quantum-ai-training-literature-2026-09-13.json`

## 5. Next gates

### `AI-COST-002` — frozen functional-equivalence baseline

Define one concrete AI-training capability contract that can be run classically today. It must specify dataset/task, architecture/model size, quality threshold, training budget, wall time, hardware, memory, network, energy and monetary cost. The first benchmark should be small enough to reproduce cheaply but structurally expose the same cost ledger used for larger targets.

### `AI-COST-003` — reproduce one strongest quantum/hybrid route

Implement at least one open algorithmic route under identical task semantics. Candidate first choices are a small structured quantum-gradient/backpropagation experiment or a quantum-linear-system training fixture. State preparation and readout must be explicit.

### `AI-COST-004` — residual-cost destruction map

For every classical residual component, identify whether the route accelerates it, eliminates it, compresses it, moves it elsewhere, or leaves it unchanged. Any component exceeding the moonshot residual threshold blocks the canonical target and becomes a primary research problem.

### Cross-lane gates

- **Lane B:** executable provider/QPU realization only after bounded-cost authorization.
- **Lane C:** memory/data-movement/state-preparation contract.
- **Lane D:** physical QRAM/QPU/control feasibility and resource estimates.
- **Lane F:** competitive classical baseline and complete lifecycle economics.

## Non-claims

Batch 038 does **not** demonstrate or claim:

- that an existing single data center costs US$10–100 trillion;
- that the owner-defined US$10–100 trillion ambition proxy has been physically compressed;
- real-QPU frontier AI training;
- general quantum advantage for AI training;
- 100,000,000x, 6.609-billion-fold or 66.09-billion-fold realized cost reduction;
- GPU/NPU/RAM/DRAM/HBM replacement;
- a tens-of-thousands-of-baht equivalent of frontier data-center capability;
- a new law of physics.

The new contribution is a reproducible target contract, literature map and necessary end-to-end residual-cost gate. It is designed to reject seductive kernel-only speedups that cannot satisfy the actual economic mission.
