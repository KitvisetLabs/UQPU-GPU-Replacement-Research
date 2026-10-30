# Research gap RG-DG-ROUTING-001 — waveguide routing and spin-qubit device transfer

**Opened:** 2026-10-30 · **Primary owner:** Lane D · **Co-owner:** Lane G  
**Interfaces:** B provider/control; C interconnect; E cryogenic energy/materials; F evidence/economics; H publication.  
**Status:** LITERATURE_ONLY / FULL SOURCE EXTRACTION AND UQPU REPRODUCTION NOT RUN.  
**Related:** INV-029/030/032/034/035; FND-003; FIN-001.

## Objective and separate source arms

Determine whether two peer-reviewed device results transfer to reproducible D/G engineering constraints. Keep their metrics separate.

- **DG-ROUTING-WAVEGUIDE-001:** Mutsenik et al., *npj Quantum Information* (2026-10-29), DOI 10.1038/s41534-026-01399-5. Two separated superconducting waveguides coupled by one transmon at 10 mK and approximately one photon at 6 GHz. Numeric transfer efficiency, uncertainty, bandwidth, insertion loss and device spread are not present in the inspected abstract.
- **DG-SPIN-TQD-001:** Matsumoto et al., *npj Quantum Information* (2026-10-24), DOI 10.1038/s41534-026-01400-1. GaAs triple-dot flopping-mode qubit; source reports >100 MHz Rabi, FNN drift feedback, 388 kHz residual frequency fluctuation and 99.56% π/2 fidelity at 4.05 ns. No multi-device yield or silicon/germanium transfer is established.

## Gates

**Gate 0 — source/device provenance:** retrieve version-of-record papers and supplements; extract geometry, process, operating point, calibration, raw/derived data and uncertainty; pin data/source hashes and licenses. Abstract-only quantities remain NOT_REPORTED, not zero.

**Gate 1 — reconstruction:** for waveguides, reconstruct the non-Hermitian Hamiltonian and transfer/coupling/dephasing parameters, then compare with a direct-coupler baseline at matched frequency, photon number and temperature. For triple-dot, reconstruct orbital-band operating map and randomized-benchmarking protocol; compare two-dot versus three-dot and feedback-on versus feedback-off under matched pulse/noise budgets.

**Gate 2 — D/G process:** require repeated devices and process lots; measure geometry tolerances, interfaces, deposition/etch, alignment, flux stability, cryogenic thermalization, packaging, metrology, defectivity, reliability, yield and cost per good die/package.

**Gate 3 — system/economics:** measure photon-transfer fidelity/efficiency, insertion loss, bandwidth, throughput, switching latency and cryogenic wall-plug energy; separately measure spin-gate fidelity/uncertainty, coherence, calibration overhead, drift and control energy. Only then calculate cost per accepted transfer/gate.

Reject transfer if narrow bias/temperature windows are not repeatable, process variation destroys the operating point, or control/packaging/cooling overhead erases the function. No UQPU device, production yield, material substitution, accepted fuel, net fusion electricity, financing or Data-Center-to-One-Phone result is established.
