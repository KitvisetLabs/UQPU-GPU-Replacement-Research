# Literature watch — 2026-10-30: transmon-waveguide routing cell and triple-dot spin-qubit control

**Primary owner:** Lane D · **D/G co-design:** continuous · **Interfaces:** B/C/E/F/G/H  
**Evidence:** TWO DISTINCT PEER-REVIEWED EXTERNAL DEVICE EXPERIMENTS; NOT REPRODUCED BY UQPU.  
**Work item:** DG-DEVICE-TRANSFER-001 · **Gap:** ../RESEARCH_GAP_DG_WAVEGUIDE_AND_SPIN_QUBIT_TRANSFER_2026-10-30.md.

## Source 1 — transmon-mediated waveguide coupling

Mutsenik et al., “Experimental characterization of the qubit-mediated coupling between two waveguides,” *npj Quantum Information*, published 2026-10-29, DOI https://doi.org/10.1038/s41534-026-01399-5. The article reports two spatially separated superconducting waveguides coupled through one transmon, operated at 10 mK with approximately one input photon at approximately 6 GHz. Steady-state and time-domain measurements reconstruct relaxation, dephasing, waveguide-qubit coupling and cross-waveguide photon-transfer efficiency. The reported behavior is consistent with a non-Hermitian Hamiltonian formalism; flux bias, temperature and photon number limit performance, and photon dressing is observed at high photon number.

**Novelty:** an experimentally characterized basic cell for microwave-photon transfer between separated waveguides.

**Limitations:** the abstract does not state numeric transfer efficiency, uncertainty, bandwidth, insertion loss, device spread or control overhead. Retrieve full text/supplement before engineering use. One cell is not a scalable network or low-cost interconnect. UQPU has not reproduced the experiment.

## Source 2 — triple-dot spin-qubit orbital-band engineering

Matsumoto et al., “High-fidelity flopping-mode single-spin operation via triple-dot orbital-band engineering,” *npj Quantum Information*, published 2026-10-24, DOI https://doi.org/10.1038/s41534-026-01400-1. The authors report a GaAs triple-dot flopping-mode qubit with a third-dot tuning parameter that flattens qubit-frequency dependence while retaining spin-charge hybridization. The abstract reports Rabi frequencies above 100 MHz, feedforward-neural-network feedback for slow drift, 388 kHz residual frequency-fluctuation standard deviation and 99.56% π/2 fidelity at 4.05 ns.

**Novelty:** an additional post-fabrication electrical degree of freedom loosens the speed-versus-detuning-noise trade-off.

**Limitations:** GaAs-specific single-device evidence; no silicon/germanium transfer, multi-device yield, multi-qubit gate, packaged-system energy or lifecycle cost. FNN feedback is a control method, not a new physical law.

## Exact UQPU relevance and follow-up

- **C:** measure transfer efficiency/fidelity, bandwidth, latency, buffering and interconnect bytes; this is not RAM/VRAM/HBM/storage.
- **D/G:** extract geometry, process, interfaces, flux stability, orbital operating points, cryogenic test, metrology, packaging, process window, device spread, defectivity and yield.
- **B:** map only characterized target/control interfaces.
- **E/F:** measure cryogenic wall-plug energy and yield-adjusted cost per accepted transfer/gate; no fusion or fuel inference.
- **H:** source-attributed research only.

Retrieve full papers/supplements, extract numeric parameters and uncertainty, reconstruct the waveguide Hamiltonian and triple-dot operating-point/RB protocols, then compare with matched direct-coupler and two-dot/no-feedback controls. Require repeated devices and held-out process/temperature/bias conditions. Do not pool photon-transfer and spin-gate metrics.

No UQPU device, fabrication, yield, material substitution, accepted fuel, net fusion electricity, financing or Data-Center-to-One-Phone advantage is established.
