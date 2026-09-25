# QSPPACK 0.4.0 software watch — 2026-09-25

## Material delta

The current PyPI release is `qsppack==0.4.0`, while Batch 053 deliberately
preserved the failing `0.3.0` execution as a negative control. Source inspection
shows that the newer implementation returns `n + 1` derivative components for
the odd-parity Newton Jacobian; `0.3.0` returned `n`, producing the reproduced
41-to-42 broadcast exception. The frozen polynomial was not changed.

Source inputs, accessed 2026-09-25:

- QSPPACK package/source: <https://github.com/qsppack/pyqsppack>
- Dong, Lin, Ni and Wang, *Robust iterative method for symmetric quantum signal
  processing in all parameter regimes*: <https://arxiv.org/abs/2307.12468>
- Ni and Ying, *Fast Phase Factor Finding for Quantum Signal Processing*:
  <https://arxiv.org/abs/2410.06409>

## Concrete project decision

Keep `0.3.0` as the reproducible failure control and add a separate, fully pinned
`0.4.0` lane. Require exact input and phase fingerprints, the package residual,
and a repository-owned 2x2 reconstruction before a phase vector can cross the
QOS-AUDIT-010B3 gate.

## Evidence limit and follow-up

This is a material software correction and numerical result, not a new physical
law, formal approximation certificate, QSVT workload result, real-QPU result or
economic evidence. The falsifiable follow-up is QOS-AUDIT-010B4: map the frozen
phases into a bounded matrix/QSVT fixture, verify transformed singular values and
resource counts, and seek a second implementation or interval/error certificate.

The broader 2026-09-25 surveillance of symbolic regression, neural-symbolic
equation discovery, AI theorem discovery, differentiable physics and automated
experiment design found no newer primary result that materially changes the
active experiment. This negative watch result does not imply that those fields
had no publications; it records only the project-relevance screen performed for
this cycle.
