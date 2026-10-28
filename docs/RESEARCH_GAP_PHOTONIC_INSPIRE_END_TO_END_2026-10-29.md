# Research gap RG-D-PHOTONIC-INSPIRE-END-TO-END-001 — physical photonic training acceptance

**Opened:** 2026-10-29
**Primary owner:** Lane D — device/chip/process/fabrication/packaging
**Interfaces:** A (workload equivalence), C (I/O and memory/data movement), F (evidence/economics), G (manufacturing/metrology)
**Status:** OPEN / PEER-REVIEWED-LITERATURE-ONLY-FOR-UQPU / REPRODUCTION NOT STARTED
**Source:** https://doi.org/10.1038/s43588-026-01057-y
**Related:** INV-025–027, INV-029, INV-034–035, EQN-001–010

## Objective

Determine whether in-situ physical gradient descent on photonic integrated circuits produces a repeatable end-to-end benefit for a frozen useful workload after optical power, measurement, control, data conversion, calibration, host computation, device variability and lifecycle cost are counted.

## Starting evidence

The 2026-10-05 *Nature Computational Science* paper reports INSPIRE, 0.26% relative error for trained matrices, training through scattering media for matrices larger than the number of native tunable elements, 251-fold model compression, and 136-fold task-specific training acceleration. These are third-party experimental results in the paper's scope. UQPU has not reproduced them. Source data are stated to be available; code/model/training procedure is linked at https://doi.org/10.5281/zenodo.21918485.

## Acceptance contract

All compared methods must use the same frozen workload and accepted-output predicate. Record:

- workload, dataset and train/validation/test manifest hashes; task quality, precision and acceptance threshold;
- matrix dimensions, topology, native tunable-element count, device identity, wavelength range, temperature and calibration epoch;
- physical output error and uncertainty, task-level quality, generalization across held-out devices/topologies/wavelengths and repeatability;
- training and inference wall time, throughput, latency distribution, repetitions and accepted tasks;
- laser, optical source, tuning/heater, control, detector/readout, ADC/DAC, host-compute and cooling energy where measurable;
- optical losses, input/output bytes, calibration data, transfer/reconstruction time, peak host memory and failure/retry rate;
- fabrication yield, packaging, drift, service life, maintenance, replacement and amortized capital;
- total cost and energy per accepted useful task, with unknown components explicitly unpriced rather than set to zero.

Compare at least digital training, in-silico photonic training and in-situ training on the same output contract. A parameter-count reduction or training-speed multiplier alone cannot pass the acceptance gate.

## Falsifiers / next decisive experiment

1. Pin and hash the paper data/code and dependencies; reproduce the paper's stated matrix-error metric from a clean environment.
2. Freeze the workload and all three baselines before testing; do not select the test set or task after seeing the results.
3. Repeat on a second physical device and on held-out wavelength/temperature/topology conditions.
4. Compare full-system energy and cost per accepted task. Reject the advantage hypothesis if physical readout/control, calibration, host compute, optical loss, yield or maintenance erases the task-level gain.
5. Require independent replication before promoting beyond source-reported experimental evidence.

## Nonclaims

This gap is not evidence that photonics replaces a GPU/NPU, that optical state space equals readable classical memory, or that the Data-Center-to-One-Phone goal is achieved. It establishes no 100x or 100,000,000x advantage, no Pangola/material substitution, no bio-oil/fusion/finance result, and no new physical law. Current thermodynamic, causal, information and measurement constraints remain binding.