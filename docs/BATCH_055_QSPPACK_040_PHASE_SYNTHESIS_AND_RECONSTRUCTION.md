# Eight-Lane Research Batch 055 — QSPPACK 0.4.0 phase synthesis and independent reconstruction

**Date:** 2026-09-25  
**Canonical starting commit:** `7f3ebbca3ec6a690109815b24ad0c43a5b8b9ebe`  
**Starting CI:** GitHub Actions run 35569917677, successful  
**Primary owner:** Lane A; evidence and integration owner: Lane F

## Result

The exact frozen degree-81 odd-parity polynomial fingerprint
`4364297169fe219da396c1d663680f474508a03afed93e321dc8e9d8f0bad13a`
was synthesized with pinned `qsppack==0.4.0`. Newton returned 82 finite phases
after 9 iterations with reported residual `2.6281060661048627e-15`. The phase
fingerprint is
`268d1809a8d88309df001d2c63b1f78ba5101d2b9e254c304b014ba4e8397445`.

A repository-owned complex 2x2 `W(x)` product, which does not call QSPPACK's
response evaluator, then checked 20,001 equally spaced points on [-1, 1]. Maximum
real-response residual was `1.2667644710973036e-13`; maximum unitarity residual
was `1.554312234475219e-14`. Both passed the predeclared `2e-12` and `2e-13`
tolerances. A degree-1 control also returned two phases without a dimension
mismatch.

This resolves the reproduced implementation blocker for this numerical contract.
The pinned `0.3.0` failure remains in CI as a negative control. It does not prove
global or interval-bounded approximation error, demonstrate QSVT task semantics,
execute a provider job, or establish hardware or economic advantage.

## Implementation and reproducibility

- `uqpu/qos_d23_phase_reconstruction_v040.py`: frozen phases, per-run
  fingerprinting, strict optional synthesis and independent 2x2 reconstruction.
- `tests/test_qos_d23_phase_reconstruction_v040.py`: structural, pointwise,
  grid and optional solver regression tests.
- `qsp-synthesis-v040-optional-requirements.txt`: full isolated dependency lock.
- `benchmarks/results/batch055-qos-phase-synthesis-v040-reconstruction.json`:
  raw numerical certificate and execution provenance.
- Dedicated GitHub Actions job keeps the 0.4.0 positive path separate from the
  0.3.0 negative-control job.

Local core validation: 371 tests passed, 6 optional tests skipped. Isolated
0.4.0 validation: 5 tests passed. No paid service or QPU was invoked.

## Eight-lane review

| Lane | Advance or reviewed blocker | Evidence boundary / next gate |
|---|---|---|
| A | 82 phases synthesized and independently reconstructed | `SIMULATION`; bounded QSVT fixture next |
| B | No provider submission or target claim | lowering stays closed until QSVT/resource gate |
| C | 82 phase scalars are recorded | no RAM/VRAM/storage equivalence inferred |
| D | Phase availability can later seed circuit requirements | no device requirement before resource ledger |
| E | Pangola, BIO-001 and FUS-001 reviewed | no new material/fuel/electricity measurement |
| F | Fingerprints, residuals, provenance and negative control integrated | no advantage, accepted-task cost or competitive baseline result |
| G | D/G co-design remains linked to future circuit requirements | no fabrication/process-window claim |
| H | Positive and negative software evidence published under stage gates | capital escalation awaits QSVT semantics and resources |

## Foundational and equation-discovery review

FND-001 through FND-006 and EQN-001 through EQN-006 were reviewed. This phase
sequence is a numerical software artifact under established mathematics, not an
AI-generated law or exception to present physics. It changes no thermodynamic,
information, quantum-speed-limit, causality, symmetry or conservation boundary.
No candidate equation was promoted, so no held-out prediction or physical-law
validation claim is made.

## Literature and software surveillance

The material delta was the current QSPPACK software release and its corrected
odd-parity derivative dimension. The project decision and primary sources are
recorded in the dated Lane-A software watch. Searches on 2026-09-25 found no
newer project-changing primary result in equation discovery, theorem discovery,
differentiable physics or automated experiment design. Third-party publications
remain external evidence and are not UQPU measurements.

## INV-029 through INV-035

- **INV-029 / INV-025–027:** one upstream numerical compiler gate advanced; no
  Data-Center-to-Phone or 100M-unit useful-output contract is satisfied.
- **INV-030:** biomass-carbon functional substitution remains evidence-gated;
  no transmutation or material-performance claim.
- **INV-031:** BIO-001 remains MODEL_ONLY/DATA_BLOCKED; no accepted-fuel result.
- **INV-032:** FUS-001 remains MODEL_ONLY/DATA_BLOCKED; no net-electric result.
- **INV-033:** a reproducible software gate can reduce wasted R&D effort, but no
  financed-principal, WACC or interest reduction was measured.
- **INV-034/035:** established physics and the generator-to-independent-
  validation discipline remain binding; no new physical law is claimed.

The Thai, English, Chinese, Japanese, Korean and German master-plan links, the
Kanusanan Pongpanna Model, strategic AI-agent/funding references, Priority #1 and
all permanent invariants were preserved.

## Next highest-value gate

**QOS-AUDIT-010B4:** bind the frozen phases to a small matrix/QSVT fixture,
independently verify transformed singular values and exact convention mapping,
record circuit/query/ancilla/depth and host-I/O costs, and add higher-assurance
phase validation through a second implementation or interval/error certificate.
Provider lowering, device/factory response and economics remain downstream.

## CI portability correction

The first hosted run showed that raw Newton phase floats can differ at the last
bits across numerical environments, so requiring the hosted phase SHA-256 to
equal the locally frozen vector was not a valid portability criterion. The gate
remains fail-closed but now fingerprints every returned vector and independently
reconstructs that exact vector. Phase count, finiteness, package residual and
the unchanged response/unitarity tolerances remain mandatory; no evidence
threshold was weakened.
