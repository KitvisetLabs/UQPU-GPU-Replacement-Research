# Literature watch — 2026-10-30: quantum thermodynamics and Majorana self-testing

**Primary owner:** Lane H · **Interfaces:** FND-001 thermodynamics; FND-005 QFT/particle mechanisms; INV-034/035.  
**Evidence:** PEER-REVIEWED SINGLE-QUBIT OPTICAL EXPERIMENT + PEER-REVIEWED MATHEMATICAL SELF-TESTING FRAMEWORK; NOT REPRODUCED BY UQPU.

## Quantum strong Mpemba effect

Zhan, Gao, Xiao and Xue, “Genuine Quantum Strong Mpemba Effect by Eliminating Coherence,” *Physical Review Letters* 137, 170403, published 2026-10-22, DOI https://doi.org/10.1103/z9t9-mwgv. The authors report a controllable optical setup simulating a Davies map, verify the semigroup property and demonstrate a strong Mpemba effect in a single-qubit system by eliminating coherence associated with degenerate slowest decay modes.

**Novelty:** in this Davies-map setting, the usual unique-slowest-mode condition can be relaxed because degenerate slowest modes are purely coherent and can be removed by initial-state choice.

**Limitations:** bounded single-qubit optical simulation of open-system dynamics; not a new thermodynamic law, heat-engine result, computation speedup or lower Landauer bound. UQPU has not reconstructed the apparatus or uncertainty analysis.

**FND-001 follow-up:** reconstruct the Davies generator, slow eigenspace and coherence-elimination map; verify complete positivity, trace preservation, semigroup consistency and energy/entropy accounting; reproduce against matched initial-state and measurement controls. Reject acceleration that disappears when preparation, coherence, energy and measurement budgets are matched.

## Majorana self-testing equivalence

Michalski, Konderak, Bruzda and co-authors, “Device-independent certification of Majorana fermions and a new self-testing equivalence,” *npj Quantum Information*, published 2026-10-24, DOI https://doi.org/10.1038/s41534-026-01383-z. A related script/data record is listed at https://doi.org/10.5281/zenodo.20510597.

The paper constructs Bell inequalities from row-orthogonal, column-normalized matrices, generalizes CHSH and Gisin's elegant inequality, and under stated assumptions provides a device-independent certification route for Majorana fermions interpreted as multiqubit Clifford-algebra generators. It identifies an additional self-testing equivalence associated with joint partial transposition of state and measurements when well-defined.

**Novelty:** the extra equivalence refines what self-testing uniquely identifies.

**Limitations:** mathematical certification framework, not an experimental observation of Majorana particles in a material or a topological-device demonstration. The script archive does not validate the theorem; UQPU has not pinned or run the scripts or independently checked the proof.

**FND-005 follow-up:** formalize ROCN assumptions, Bell functionals, exact classical/quantum bounds, partial-transpose equivalence and degenerate cases; compare with prior Clifford/Majorana self-testing literature; reproduce finite classical-bound calculations from pinned scripts. Any material claim requires a separate device experiment.

Both sources are reported within established quantum theory. Neither changes thermodynamic lower bounds, QFT, the Standard Model, material properties or engineering constraints by declaration. No new physical law or alternative particle is claimed.
