# Feasibility, Barriers and Non-Negotiable Limits

## 1. Current QPUs are not GPU replacements
As of 2026, major practical quantum architectures remain hybrid. UQPU is a future architecture research target.

## 2. Hilbert-space size is not classical memory capacity
An n-qubit pure state lives in a 2^n-dimensional state space, but this does not provide random classical readout of 2^n amplitudes. Measurement returns samples. Claims of "exponential memory" must state how data is loaded, queried, measured, and how many repetitions are required.

## 3. Input lower bounds
If a workload provides N unstructured classical values and all must influence the result, reading the input can itself cost Ω(N) in ordinary memory models. Quantum algorithms can avoid this only under structural assumptions such as efficient oracles, generative input, compressed representation, or specialized memory access.

## 4. Output lower bounds
If an application demands N explicit classical outputs, writing them costs at least proportional to output size. This directly affects framebuffer generation, decoded video, dense tensors, full sorting, and large simulation fields.

## 5. Reversible arithmetic overhead
Exact classical arithmetic can be mapped to reversible circuits, but garbage must be uncomputed, ancillas are required, non-Clifford gates can dominate fault-tolerant cost, and floating-point logic is large. Reversible fallback is therefore a completeness proof, not a likely performance path.

## 6. Quantum advantage is problem-specific
No known theorem gives quantum speedup for every parallel classical task. A UQPU may support every GPU function while outperforming GPUs on only a subset.

## 7. Latency
Frame rendering, interactive AI, video processing, and control loops are latency-sensitive. Long fault-tolerant execution or very large shot counts may fail real-time contracts.

## 8. Error correction
Resource estimates must include physical error rate, code distance, logical error target, physical qubits per logical qubit, syndrome rate, decoding latency, and non-Clifford resources.

## 9. Classical electronics remain allowed
GPU functional replacement does not mean elimination of classical computing. CPU, memory controllers, cryogenic control, DAC/ADC, QEC decoders, display/PCIe controllers, and network interfaces are permitted support components.
