# GPU Functional Coverage Matrix

A UQPU claiming eventual GPU functional replacement must cover all major workload goals, even when the internal process differs.

| Domain | GPU objective | UQPU functional target | Candidate route | Major blocker |
|---|---|---|---|---|
| Raster graphics | Produce frames | Equivalent framebuffer | semantic scene generation / reversible fallback | output bandwidth |
| Ray tracing | Light transport | Equivalent pixels | amplitude estimation / quantum sampling | oracle construction |
| Path tracing | Monte Carlo rendering | Converged image | quantum amplitude estimation | reconstruction |
| AI inference | Prediction | Same task output | QML / quantum linear algebra / sampling | state preparation |
| AI training | Optimize model | Equivalent model quality | variational optimization | iteration/readout latency |
| GEMM | Matrix product | Same numerical/downstream contract | quantum linear algebra or fallback | dense output |
| Convolution | Feature transform | Equivalent output | spectral/quantum transform | tensor output |
| Attention | Sequence interaction | Equivalent model behavior | quantum kernels/search/sampling | data movement |
| FFT | Transform | Same frequency-domain objective | QFT where contract fits | full reconstruction |
| Linear solvers | Solve Ax=b | Solution/observables | QLSA | state preparation/conditioning |
| Eigenproblems | Eigenpairs | Equivalent result | phase estimation/VQE | precision/QEC |
| Monte Carlo | Estimate expectation | Bounded-error estimate | amplitude estimation | oracle cost |
| Optimization | Min/max | Valid solution | QAOA/annealing/amplitude methods | scaling |
| Sorting | Ordered dataset | Full sorted output | reversible sort/subroutines | output lower bound |
| Search | Locate item | Same result | Grover-like search | oracle construction |
| Graph analytics | Paths/ranking | Same analytics | quantum walks/linear algebra | graph loading |
| Signal processing | Filter/transform | Same samples | QFT/transforms/fallback | streaming I/O |
| Image processing | Transform image | Same image | quantum image processing/fallback | pixel output |
| Video decode | Raw frames | Standard-compliant output | reversible codec | output bandwidth |
| Video encode | Bitstream | Standard-compliant codec | optimization + deterministic logic | exact compliance |
| Physics simulation | Dynamics/observables | Same quantities | Hamiltonian simulation | encoding/QEC |
| CFD/PDE | Fields/observables | Acceptable solver output | quantum linear/PDE methods | dense fields |
| Cryptography | Exact primitive | Exact outputs | reversible circuits | limited generic speedup |
| General kernel | Arbitrary result | Same contract | reversible synthesis fallback | severe overhead |
| Display output | Scanout | Same display signal | classical egress controller | classical I/O |
