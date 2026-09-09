from __future__ import annotations

from .cloud_economics import CloudPricingKind, CloudPricingProfile


def official_pricing_snapshot_2026_09() -> tuple[CloudPricingProfile, ...]:
    return (
        CloudPricingProfile(
            "ibm_quantum", "Pay-As-You-Go",
            CloudPricingKind.PER_SECOND,
            per_second=96.0/60.0,
            source_url="https://www.ibm.com/quantum/products",
        ),
        CloudPricingProfile(
            "ibm_quantum_flex", "Flex",
            CloudPricingKind.PER_SECOND,
            per_second=72.0/60.0,
            source_url="https://www.ibm.com/quantum/products",
        ),
        CloudPricingProfile(
            "ibm_quantum_premium", "Premium",
            CloudPricingKind.PER_SECOND,
            per_second=48.0/60.0,
            source_url="https://www.ibm.com/quantum/products",
        ),
        CloudPricingProfile(
            "aws_braket_rigetti_cepheus", "Braket On-Demand Rigetti Cepheus",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.000425,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "aws_braket_iqm_garnet", "Braket On-Demand IQM Garnet",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.00145,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "aws_braket_iqm_emerald", "Braket On-Demand IQM Emerald",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.00160,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "aws_braket_quera_aquila", "Braket On-Demand QuEra Aquila",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.01000,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "aws_braket_aqt_ibex_q1", "Braket On-Demand AQT IBEX-Q1",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.02350,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "aws_braket_ionq_forte", "Braket On-Demand IonQ Forte",
            CloudPricingKind.PER_TASK_SHOT,
            per_task=0.30,
            per_shot=0.08000,
            source_url="https://aws.amazon.com/braket/pricing/",
        ),
        CloudPricingProfile(
            "azure_ionq_aria", "Azure IonQ Aria PAYG no mitigation",
            CloudPricingKind.PER_GATE_SHOT,
            per_one_qubit_gate_shot=0.000220,
            per_two_qubit_gate_shot=0.000975,
            minimum_program_price=12.4166,
            source_url="https://learn.microsoft.com/en-us/azure/quantum/pricing",
        ),
        CloudPricingProfile(
            "azure_ionq_forte", "Azure IonQ Forte PAYG no mitigation",
            CloudPricingKind.PER_GATE_SHOT,
            per_one_qubit_gate_shot=0.0001645,
            per_two_qubit_gate_shot=0.001121,
            minimum_program_price=25.7899,
            source_url="https://learn.microsoft.com/en-us/azure/quantum/pricing",
        ),
        CloudPricingProfile(
            "azure_pasqal_fresnel", "Azure Pasqal Fresnel PAYG",
            CloudPricingKind.PER_QPU_HOUR,
            currency="EUR",
            per_qpu_hour=3000.0,
            source_url="https://learn.microsoft.com/en-us/azure/quantum/pricing",
        ),
        CloudPricingProfile(
            "azure_rigetti_cepheus", "Azure Rigetti Cepheus PAYG",
            CloudPricingKind.PER_TIME_INCREMENT,
            time_increment_seconds=0.010,
            per_time_increment=0.02,
            source_url="https://learn.microsoft.com/en-us/azure/quantum/pricing",
        ),
    )
