from __future__ import annotations

from .provider_hardware import HardwareSnapshot


def market_snapshot_2026_09() -> tuple[HardwareSnapshot, ...]:
    """Official-source market snapshot, 2026-09.

    Metrics with ambiguous modality semantics are deliberately left unset.
    Roadmap values are explicitly marked ROADMAP, not current hardware.
    """
    return (
        HardwareSnapshot(
            "ibm_quantum","Heron","gate_model",
            physical_qubits=156,
            cloud_accessible=True,
            evidence_date="2026-09",
            source_url="https://www.ibm.com/quantum/hardware",
            notes="IBM lists Heron r2/r3 with 156 programmable qubits; logical-qubit field intentionally unset for current Heron."
        ),
        HardwareSnapshot(
            "ibm_starling_roadmap","Starling (roadmap)","gate_model",
            logical_qubits=200,
            max_operations_claimed=100_000_000,
            cloud_accessible=False,
            evidence_date="2029 target",
            evidence_level="ROADMAP",
            source_url="https://www.ibm.com/quantum/hardware",
            notes="Planned fault-tolerant system; not current cloud hardware."
        ),
        HardwareSnapshot(
            "quantinuum_nexus","Helios","gate_model",
            physical_qubits=98,
            logical_qubits=50,
            single_qubit_fidelity=0.999975,
            two_qubit_fidelity=0.99921,
            cloud_accessible=True,
            evidence_date="2026-09",
            source_url="https://www.quantinuum.com/products-solutions/quantinuum-systems/helios"
        ),
        HardwareSnapshot(
            "ionq_roadmap_2026","IonQ 2026 roadmap","gate_model",
            physical_qubits=100,
            logical_qubits=12,
            cloud_accessible=True,
            evidence_date="2026 roadmap",
            evidence_level="ROADMAP",
            source_url="https://www.ionq.com/roadmap",
            notes="Roadmap range is 100-256+ physical qubits; lower bound stored for conservative machine-readable comparison."
        ),
        HardwareSnapshot(
            "pasqal_cloud","1024-atom register milestone","analog",
            physical_qubits=1024,
            cloud_accessible=True,
            evidence_date="2026-04-14",
            source_url="https://www.pasqal.com/blog/defect-free-1024-atom-registers-scaling-to-1000-qubits/",
            notes="Register milestone; not equivalent to a 1024-qubit fault-tolerant gate-model computer."
        ),
        HardwareSnapshot(
            "quera","Aquila","analog",
            physical_qubits=256,
            cloud_accessible=True,
            evidence_date="2026-09",
            source_url="https://aws.amazon.com/braket/quantum-computers/quera/"
        ),
        HardwareSnapshot(
            "rigetti_qcs","Cepheus-1-108Q","gate_model",
            physical_qubits=108,
            single_qubit_fidelity=0.999,
            two_qubit_fidelity=0.991,
            cloud_accessible=True,
            evidence_date="2026-04-07",
            source_url="https://www.rigetti.com/what-we-build"
        ),
        HardwareSnapshot(
            "dwave_leap","Advantage2","annealing",
            physical_qubits=4400,
            cloud_accessible=True,
            evidence_date="2025-05-20",
            source_url="https://support.dwavesys.com/hc/en-us/articles/32105885880087-D-Wave-s-Advantage2-Quantum-Computer-Now-Generally-Available",
            notes="Annealing qubits; not comparable one-for-one to gate-model qubits."
        ),
        HardwareSnapshot(
            "oqc_cloud","Toshiko","gate_model",
            physical_qubits=32,
            cloud_accessible=True,
            evidence_date="2026-09",
            source_url="https://oqc.tech/access/oqc-cloud/"
        ),
        HardwareSnapshot(
            "oqc_genesis_roadmap","Genesis","gate_model",
            logical_qubits=16,
            cloud_accessible=False,
            evidence_date="2026 target",
            evidence_level="ROADMAP",
            source_url="https://oqc.tech/tech/technical-roadmap",
            notes="OQC roadmap describes 16 logical qubits and 1e-3 logical error rate."
        ),
    )
