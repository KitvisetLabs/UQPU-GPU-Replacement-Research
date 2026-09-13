"""Tests for FND-007B lattice-gauge/qudit reproduction.

Research Attribution:
- Research Owner / Principal Investigator / Research Direction: Kanutsanan Pongpanna
- AI Research Agent: OpenAI GPT-5.6 Sol
- AI-assisted contribution: reproducibility tests and evidence-boundary checks.
"""

import math

from uqpu.lattice_gauge_qudit_reproduction import (
    BASIS,
    classification,
    full_gauge_resource_ledger,
    pure_gauge_resource_ledger,
    reproduce_single_plaquette_curve,
    single_plaquette_hamiltonian,
)


def test_zero_charge_sector_has_expected_dimension_and_symmetric_hamiltonian():
    assert len(BASIS) == 18
    hamiltonian = single_plaquette_hamiltonian(1.0)
    assert len(hamiltonian) == 18
    for row in range(18):
        for column in range(18):
            assert math.isclose(
                hamiltonian[row][column],
                hamiltonian[column][row],
                rel_tol=0.0,
                abs_tol=1e-14,
            )


def test_single_plaquette_curve_reproduces_strong_to_weak_coupling_behavior():
    curve = reproduce_single_plaquette_curve()
    expectations = [row["plaquette_expectation"] for row in curve]
    assert expectations == sorted(expectations)

    expected = {
        0.01: 0.00028353531764597123,
        0.1: 0.11677802242605197,
        1.0: 0.5745823967558195,
        10.0: 0.69256480058238,
        100.0: 0.7066013009670551,
    }
    for row in curve:
        assert math.isclose(
            row["plaquette_expectation"],
            expected[row["inverse_g_squared"]],
            rel_tol=0.0,
            abs_tol=2e-9,
        )

    # Source-v3 states the d=3 weak-coupling limit approaches 1/sqrt(2).
    assert abs(expectations[-1] - 1.0 / math.sqrt(2.0)) < 6e-4


def test_appendix_g_full_gauge_table_is_reproduced():
    expected = {
        3: (5, 26, 7, 90),
        5: (5, 34, 9, 162),
        7: (5, 42, 11, 234),
    }
    for dimension, row in expected.items():
        ledger = full_gauge_resource_ledger(dimension)
        assert (
            ledger.qudit_register_size,
            ledger.qudit_cnot_count,
            ledger.qubit_register_size,
            ledger.qubit_cnot_count,
        ) == row

    d3 = full_gauge_resource_ledger(3)
    assert math.isclose(d3.qudit_approx_circuit_fidelity, 0.99**26)
    assert math.isclose(d3.qubit_approx_circuit_fidelity, 0.99**90)


def test_appendix_g_pure_gauge_table_is_reproduced():
    expected = {
        3: (3, 8, 9, 84),
        5: (3, 8, 15, 108),
        7: (3, 8, 21, 132),
    }
    for dimension, row in expected.items():
        ledger = pure_gauge_resource_ledger(dimension)
        assert (
            ledger.qudit_register_size,
            ledger.qudit_cnot_count,
            ledger.qubit_register_size,
            ledger.qubit_cnot_count,
        ) == row


def test_evidence_classification_preserves_non_claims():
    evidence = classification()
    assert evidence["classification"] == "LATTICE_QED_QUDIT_RESOURCE_AND_PLAQUETTE_REPRODUCTION"
    assert evidence["evidence_level"] == "INDEPENDENT_CLASSICAL_REPRODUCTION_OF_PUBLISHED_SMALL_MODEL"
    assert evidence["non_claims"] == {
        "real_qpu_reproduction": False,
        "quantum_advantage": False,
        "direct_elementary_particle_device": False,
        "qcd_or_quark_computer": False,
        "gpu_npu_ram_hbm_replacement": False,
        "one_hundred_million_x_saving": False,
        "new_physical_law": False,
    }
