# Batch 042 — FND-007B Lattice-QED Qudit Reproduction

**Status:** reproducible small-model result / source-scoped  
**Primary lane:** Lane D — Quantum / Photonic / Semiconductor Devices / Fabrication / Packaging  
**Upstream foundation:** F4 elementary-particle / QFT research  
**Cross-lane dependencies:** Lane A (algorithms/runtime), Lane F (benchmark/economics/evidence)

## Research Attribution

- Research Owner / Principal Investigator / Research Direction: **Kanutsanan Pongpanna**
- Facebook: https://www.facebook.com/LoveMoneyTH
- YouTube: https://www.youtube.com/@LoveMoneyTHOfficial
- AI Research Agent: **OpenAI GPT-5.6 Sol**
- AI-assisted contribution: latest-literature triage, published Hamiltonian/resource-interface audit, independent exact reproduction, executable implementation/tests, evidence classification and research documentation.

Attribution reflects roles in this batch only.

## Question

Can the elementary-particle technology program identify a route that is already experimentally grounded, mathematically explicit and reproducible enough to serve as a real device/algorithm primitive rather than a speculative direct-quark or string-scale device claim?

## Highest-information-gain route selected

The selected route is **native-qudit quantum simulation of two-dimensional lattice QED**, based on:

- Michael Meth et al., *Simulating 2D lattice gauge theories on a qudit quantum computer*, arXiv:2310.12110v3; Nature Physics 21, 570–576 (2025), DOI 10.1038/s41567-025-02797-w.
- The experiment uses trapped `40Ca+` ions, mixed qubits/qudits, dynamical matter plus gauge fields, and a variational quantum eigensolver for a single 2D plaquette.
- Gauss' law is used to eliminate three of four gauge fields in the open single-plaquette problem, leaving four matter qubits plus one qutrit for the minimal `d=3` gauge truncation.

This is a stronger starting point than a direct isolated-quark technology hypothesis because the paper already supplies a physical platform, preparation/control/readout path, Hamiltonian, experimentally realized circuits and explicit resource comparisons.

## Independent Hamiltonian reproduction

The UQPU artifact implements source-v3 Eqs. (9)–(10) directly in the zero-total-charge sector:

```text
four matter qubits + one qutrit
-> restrict to two-up/two-down matter sector
-> 6 matter basis states * 3 electric-field states
-> exact 18-dimensional real-symmetric Hamiltonian
-> deterministic shifted power iteration
-> ground energy + plaquette expectation
```

Frozen source parameters are `m=0.1`, `Omega=5` and `d=3`.

Results:

| g^-2 | ground energy | <plaquette> |
| ---: | ---: | ---: |
| 0.01 | -2.13625748030171 | 0.000283535317646 |
| 0.1 | -9.138735278662324 | 0.116778022426052 |
| 1 | -13.413890680611074 | 0.574582396755820 |
| 10 | -20.372391698091615 | 0.692564800582380 |
| 100 | -83.9002548334451 | 0.706601300967055 |

The reproduced plaquette expectation grows monotonically from nearly zero in the strong-coupling regime toward the source-v3 stated `d=3` weak-coupling reference

```text
1/sqrt(2) = 0.7071067811865475.
```

The `g^-2=100` result differs from that reference by about `5.05e-4`.

This is an **independent classical exact finite-dimensional reproduction of the published encoded model**. It is not a reproduction of the paper's experimental trapped-ion data.

## Reproduced Appendix-G resource interface

For the full gauge single-plaquette VQE route, source-v3 Appendix G gives:

```text
native qudit:
  register = 5
  CNOT-equivalent count = 18 + 4(d-1)

comparable one-hot qubit encoding:
  register = 4 + d
  CNOT count = 18 + 36(d-1)
```

The executable ledger reproduces the source table exactly:

| d | qudit register | qudit CNOT | qubit register | qubit CNOT |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 5 | 26 | 7 | 90 |
| 5 | 5 | 34 | 9 | 162 |
| 7 | 5 | 42 | 11 | 234 |

For the pure-gauge periodic route:

```text
native qudit:
  register = 3
  CNOT-equivalent count = 8

one-hot qubit encoding:
  register = 3d
  CNOT count = 48 + 12d
```

which reproduces:

| d | qudit register | qudit CNOT | qubit register | qubit CNOT |
| ---: | ---: | ---: | ---: | ---: |
| 3 | 3 | 8 | 9 | 84 |
| 5 | 3 | 8 | 15 | 108 |
| 7 | 3 | 8 | 21 | 132 |

At an assumed independent CNOT fidelity of `0.99`, the source approximation `F_circuit ~= F_CNOT^N` gives, for example, approximately `0.770` versus `0.405` for the `d=3` full-gauge qudit/qubit counts and `0.923` versus `0.430` for the `d=3` pure-gauge counts. These are simplified gate-count-derived fidelity proxies, not measured UQPU hardware fidelity.

## Technology interpretation

The positive result is narrower—and more useful—than a speculative claim:

```text
QED / elementary-particle gauge theory
-> lattice gauge formulation
-> Gauss-law elimination of redundant gauge fields
-> native high-dimensional qudit representation
-> smaller register and lower entangling-gate burden for this construction
-> experimentally grounded candidate primitive for particle-physics simulation
```

The useful principle is therefore not "use a quark as a bit." It is that **particle-physics structure can expose constrained high-dimensional state spaces for which hardware-native qudits may be a better computational representation than forcing every degree of freedom into binary qubits**.

This principle can later be tested in QCD-adjacent SU(3) settings.

## Latest adjacent literature checked

### Experimentally grounded U(1) / QED route

Meth et al. demonstrate the basic 2D lattice-QED building block with matter and gauge fields on a trapped-ion qudit processor and explicitly report qudit-vs-qubit resource formulas.

- https://doi.org/10.1038/s41567-025-02797-w
- https://arxiv.org/abs/2310.12110

### SU(3) / QCD-adjacent route

Mathew & Raychowdhury, *Protecting gauge symmetries in the dynamics of SU(3) lattice gauge theories*, Communications Physics 8, 313 (2025), study symmetry protection for 1+1D SU(3) in the loop-string-hadron formulation and emphasize preservation of the physical Hilbert space under noise.

- https://doi.org/10.1038/s42005-025-02230-x

This is a promising `FND-007B4` target because it moves from U(1) toward the gauge group of QCD while keeping the research question at the simulation/control level instead of claiming direct quark logic.

### 2025 qudit dynamics proposals

Recent work also develops resource-efficient qudit circuits for 2+1D quantum-link electrodynamics and qudit simulations of hadron scattering:

- https://arxiv.org/abs/2507.12589
- https://arxiv.org/abs/2507.12614

These are useful follow-on candidates, but this batch does not treat their proposed circuits as hardware-demonstrated results.

## Evidence classification

`LATTICE_QED_QUDIT_RESOURCE_AND_PLAQUETTE_REPRODUCTION`

Evidence level:

`INDEPENDENT_CLASSICAL_REPRODUCTION_OF_PUBLISHED_SMALL_MODEL`

What is now supported:

- an experimentally grounded elementary-particle/QED technology route exists;
- the encoded single-plaquette Hamiltonian can be independently reconstructed and solved;
- the strong-to-weak coupling plaquette behavior is reproduced numerically;
- the paper's native-qudit versus one-hot-qubit register/CNOT formulas are reproduced exactly;
- for this source construction, native qudits have a concrete representation/circuit-complexity advantage.

## Non-claims

This batch does **not** establish:

- a UQPU real-QPU reproduction of the experiment;
- quantum computational advantage over the best classical method;
- an end-to-end economic advantage;
- a direct elementary-particle or quark computer;
- a QCD simulation performed by UQPU;
- GPU/NPU/RAM/DRAM/HBM replacement;
- `>=100x`, `>=100,000,000x`, billion-fold or Data-Center-to-One-Phone savings;
- a new physical law.

The source's qudit-vs-qubit comparison is architecture/construction-specific. It is not a universal lower bound proving that every qubit encoding is worse than every qudit encoding.

## Executable artifacts

- `software/uqpu-prototype/uqpu/lattice_gauge_qudit_reproduction.py`
- `software/uqpu-prototype/tests/test_lattice_gauge_qudit_reproduction.py`
- `benchmarks/results/batch042-fnd-007b-lattice-qed-qudit-reproduction.json`

## Next gates

1. **FND-007B2 — independent implementation cross-check:** reconstruct the same `d=3` Hamiltonian with a second independent SDK/implementation and compare the full spectrum and plaquette observables.
2. **FND-007B3 — noisy/economic ledger:** add finite-shot/noise, state-preparation, measurement/readout, control time, host work and hardware/cost assumptions; do not compare only CNOT counts.
3. **FND-007B4 — SU(3)/QCD-adjacent reproduction:** reproduce one symmetry-protection result from the 2025 SU(3) LSH work, with explicit gauge-violation metric and noise/protection sweep.
4. **FND-007C — string/holography route:** keep separate and require mapping from mathematical structure to a realizable workload before resource claims.
