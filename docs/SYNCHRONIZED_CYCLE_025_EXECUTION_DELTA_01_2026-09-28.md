# Synchronized Cycle 025 — Execution Delta 01

| Field | Value |
|---|---|
| Prepared | 2026-09-29 Asia/Bangkok |
| Branch | `research/cycle-025-delta-01-2026-09-28` |
| Base | Verified Cycle 024 metadata closeout `17fa4a1ed10c1e5a2a2bfd3bd073eaa212e09275` |
| Preregistration | `2e6676f9f344381d8997c4cf42ae4cd8a5f46dfc` |
| Code/test/runner SHA | `0c2cd5037e491ebe8965ad8c58365af84f8b8153` |
| Acceptance-artifact SHA | `43a65b9c498e108bd0226f0fa194c77dcc1e6bdc` |
| GitHub Actions | [Run 36466008712](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/36466008712) on exact code SHA `0c2cd5037e491ebe8965ad8c58365af84f8b8153`: 8/8 jobs passed |
| State | Cycle 025 closed; exact-SHA GitHub Actions passed; external gates remain open |

Cycle 025 advances all twelve lanes under the [canonical parallel research portfolio](PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md). The executable acceptance artifact is [`cycle025-delta01-executable-acceptance.json`](../benchmarks/results/cycle025-delta01-executable-acceptance.json), file SHA-256 `48e03c6e7a37895761c1d65f39661619582f485d3b122c2633251af84e89be90`, payload SHA-256 `f1d486aebbb9a3f646441c0db483e681866fbc54999bc370cd5bd466e22bcbe4`.

## Lane deltas

| Lane | Result | Evidence class | Remaining gate |
|---|---|---|---|
| A | The fourth and fifth 11-node fixtures each enumerate 2,048 states; changing only edge 8 changes the exact objective 11→13 and complete witness count 20→18, with distinct bound witness hashes. | Local exact classical fixture | Matched QPU/GPU workload, accepted-output contract and independent classical baseline. |
| B | Reordered nested numeric/boolean/null receipts canonicalize identically; a 256-byte cap and non-finite/NFC-collision controls reject. | Synthetic receipt canonicalization | Externally authorized provider key plus independently verifiable job and billing evidence. |
| C | Four controlled three-writer process runs alternate between two targets, classify every visible digest and recover only complete old/new payloads. | Local process-termination fixture | Crash consistency, cache/flush behavior and power-loss durability. |
| D | Signed/unsigned descriptors cross-bind CRC and sizes; CRC/size, duplicate-extra and declared-order mutations reject before payload access. | Synthetic ZIP64 metadata | Independent real-producer archive corpus and full interoperability; the extra-field order rule is a declared fixture policy, not a general format claim. |
| E | A five-issuer synthetic custody chain verifies to its terminal digest; pre-validity and revocation-effective boundary controls reject. | Synthetic custody | Operational issuer keys, independent custody review and a physical sample. |
| F | A nine-component covariance model sweeps sigma 0.5/1/2/3 while missing, indefinite, non-finite and zero-output cases remain null. | Model only | Sourced measured components/covariance and an accepted-output definition. |
| G | A third four-measurand rescaling plus axis permutation and exact inverse cover all 16 covariance products with bound order/dimension hashes. | Synthetic typed covariance | Traceable calibration and measured covariance for declared measurands. |
| H | Nine declared scenarios enumerate 216 candidate orders; full and nine leave-one-out grids produce the exact finite interval 5/32–11/32. | Finite illustrative scenario | Owner-approved priorities, sourced distributions and a validated outcome model. |
| FND/EQN | Two independently source-bound rational interval maps compose and invert exactly; source and dimension mutations reject. | Source-typed rational model | Independent derivation, registered-unit coverage and source-backed falsifiers. |
| SCM | A seven-row fictional consent table adds challenge mismatch and post-expiry replacement controls; only the valid replacement accepts. | Fiction only | No empirical inference without separate authorization and external evidence. |
| AI-COST | Synthetic manifest v15 binds split/held-out membership hashes and metric schema; held-out, metric and parent mutations reject. | Synthetic data lineage | Real source lineage, held-out evaluation, independent baseline and equivalence test. |
| QOS/QSVT | Three pairwise non-commuting inverse pairs reconstruct all 64 basis states with residual 0 under a declared 28-gate/6-qubit bound. | Synthetic inverse operator | Independent synthesis/reconstruction and target-specific resource/error evidence. |

## Validation and limits

- Focused Cycle 025 tests: 13 passed, 0 failed.
- Selected regression set (Cycles 018, 020, 024 and 025): 52 passed, 0 failed.
- Compilation and reproducible acceptance runner: passed locally.
- Remote file verification: all four implementation/test/runner/artifact Git blob IDs exactly match the validated local files.
- Exact-SHA GitHub Actions: 8 passed, 0 failed on run `36466008712`. Passing jobs were Python 3.10, 3.11 and 3.12 tests, reference benchmark, Qiskit verification, QSP phase synthesis, QSPPACK 0.4.0 reconstruction and target-snapshot noise.

Primary-source boundaries are recorded in the preregistration and executable artifact: PKWARE APPNOTE v6.3.10 FINAL (revised 2022-11-01) for ZIP64 metadata, and official Python `os.replace` documentation for process replacement. The archive records are synthetic and payload bytes are not inspected. Process exits do not establish crash durability. All other inputs are fixture, model, typed-rational or fiction-only data.

No measured QPU/GPU performance, scaling, quantum advantage, provider execution/invoice, commercial economics, capital result, crash durability, calibration, physical sample, AI equivalence, new physical law or empirical SCM result is claimed.
