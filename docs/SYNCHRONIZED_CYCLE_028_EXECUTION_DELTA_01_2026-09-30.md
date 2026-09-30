# Synchronized Cycle 028 — Execution Delta 01

| Field | Value |
|---|---|
| Prepared | 2026-09-30 Asia/Bangkok |
| Branch | `research/cycle-028-delta-01-2026-09-30` |
| Base | Verified Cycle 027 metadata closeout `2c53eb591864f23f218fef1a214f4a47b03ebea0` |
| Preregistration | `1f48c41784753861ea675d52c6f2715a6ae9e80b` |
| Code/test/runner SHA | `052d08cd4a6db3c689fd37b1557fe725de17cdd4` |
| Acceptance-artifact SHA | `27b4f8cdb86fbbf48f92f071b2fca7efb80a3168` |
| GitHub Actions | [Run 36660185013](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/36660185013) on exact code SHA `052d08cd4a6db3c689fd37b1557fe725de17cdd4`: 8/8 jobs passed |
| State | Cycle 028 closed; exact-SHA GitHub Actions passed; external gates remain open |

Cycle 028 advances all twelve lanes under the [canonical parallel research portfolio](PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md). The executable acceptance artifact is [`cycle028-delta01-executable-acceptance.json`](../benchmarks/results/cycle028-delta01-executable-acceptance.json), file SHA-256 `4b40e3a7a87689ba575539fb95fd38a178e798e276d835ae5d0f9d7c773fbf07`, payload SHA-256 `267000ba351553cae0b3a3ae1d8e47ee37dbb0e4d8613fe0aa9246f37a509bc1`.

## Lane deltas

| Lane | Result | Evidence class | Remaining gate |
|---|---|---|---|
| A | Seventh/eighth 11-node fixtures each enumerate 2,048 states; changing only edge 10 changes objective 20→25 and witnesses 14→12. All 22 simultaneous dihedral task/witness transforms are hash-bound. | Local exact classical fixture | Matched QPU/GPU workload, accepted-output contract and independent classical baseline. |
| B | Equivalent negative-zero/exponent receipts canonicalize identically; byte/depth/token/magnitude, non-finite and normalized-collision controls reject. | Synthetic receipt canonicalization | Externally authorized provider key plus independently verifiable job and billing evidence. |
| C | Four alternating-target runs use two barrier-synchronized concurrent readers; every reader and parent observation is a complete old/new payload. | Local dual-reader fixture | Crash consistency, cache/flush behavior and power-loss durability. |
| D | Signed/unsigned descriptors and order-independent local/central ZIP64 extras cross-bind CRC and sizes while preserving an opaque extra; descriptor/extra mutations reject before payload access. | Synthetic ZIP64 metadata | Independent real-producer archive corpus and full interoperability. |
| E | An eight-issuer synthetic custody chain adds monotonic event-time and delegated audit scope; time reversal, cross-path substitution, removed delegation and pre-validity controls reject. | Synthetic custody | Operational issuer keys, independent custody review and a physical sample. |
| F | A twelve-component model evaluates positive/zero/negative covariance over sigma 0/1/2/4/6; missing, indefinite, non-finite and zero-output cases remain null. | Model only | Sourced measured components/covariance and an accepted-output definition. |
| G | Positive diagonal rescaling plus permutation across 16 covariance products roundtrips exactly and preserves determinant scaling, correlation, symmetry and PSD. | Synthetic typed covariance | Traceable calibration and measured covariance for declared measurands. |
| H | Twelve scenarios enumerate 288 full-grid outcomes and 12/66/220/495 leave-one/two/three/four grids; the exact finite interval is 1/32–13/32. | Finite illustrative scenario | Owner-approved priorities, sourced distributions and a validated outcome model. |
| FND/EQN | Five independently source-bound positive affine rational maps compose to [78909/30800, 2596569/492800] and invert exactly; source-order, dimension and nonmonotone controls reject. | Source-typed rational model | Independent derivation, registered-unit coverage and source-backed falsifiers. |
| SCM | A five-row fictional consent table binds monotonic transcript sequence and consent epoch; replay, skip, downgrade and revocation controls reject. | Fiction only | No empirical inference without separate authorization and external evidence. |
| AI-COST | Synthetic manifest v18 binds eight leaves into a Merkle-style provenance root plus parent and schema; all three corresponding mutations reject. | Synthetic data lineage | Real source lineage, held-out evaluation, independent baseline and equivalence test. |
| QOS/QSVT | Six inverse pairs reconstruct all 64 basis states with residual 0; six prefix hashes, program/resource accounting and an order mutation are bound under an 88-gate/6-qubit cap. | Synthetic inverse operator | Independent synthesis/reconstruction and target-specific resource/error evidence. |

## Validation and limits

- Focused Cycle 028 tests: 13 passed, 0 failed.
- Selected regression set (Cycles 018, 020 and 024–028): 91 passed, 0 failed.
- Compilation and reproducible acceptance runner: passed locally.
- Remote file verification: all four implementation/test/runner/artifact Git blob IDs exactly match the validated local files.
- Exact-SHA GitHub Actions: 8 passed, 0 failed on run `36660185013`. Passing jobs were Python 3.10, 3.11 and 3.12 tests, reference benchmark, Qiskit verification, QSP phase synthesis, QSPPACK 0.4.0 reconstruction and target-snapshot noise.

The primary-source review was refreshed on 2026-09-30: PKWARE APPNOTE v6.3.10 FINAL defines the relevant ZIP64 descriptor and local/central metadata fields, while official Python documentation states successful same-filesystem `os.replace` is an atomic rename on POSIX. The archive records are synthetic and payload bytes are not inspected. Concurrent-reader observations do not establish crash durability.

No measured QPU/GPU performance, scaling, quantum advantage, provider execution/invoice, commercial economics, capital result, crash durability, calibration, physical sample, AI equivalence, new physical law or empirical SCM result is claimed.
