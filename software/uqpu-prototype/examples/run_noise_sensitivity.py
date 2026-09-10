"""Batch 014: finite-shot sensitivity under an explicitly synthetic readout channel."""
import json, math
from uqpu.optimization_baseline import demo_maxcut_triangle, exact_qubo_baseline
from uqpu.scalable_qubo import seeded_erdos_renyi_maxcut
from uqpu.qaoa import qaoa_program, qubo_to_ising
from uqpu.small_statevector import probabilities
from uqpu.noise_experiments import independent_bitflip_distribution, sample_distribution

def fixture(name,instance,seed):
    obj=qubo_to_ising(instance); energies=[instance.energy(obj.assignment(k)) for k in range(1<<len(obj.variables))]
    ref=exact_qubo_baseline(instance,max_variables=12).objective
    best=None
    for gi in range(24):
      for bi in range(24):
        g,b=math.pi*gi/24,math.pi*bi/24
        p=probabilities(qaoa_program(instance,[g],[b]))
        exp=sum(x*y for x,y in zip(p,energies))
        if best is None or exp<best[0]: best=(exp,g,b,p)
    _,g,b,ideal=best
    rows=[]
    for e in (0.0,0.005,0.01,0.02,0.05):
      dist=independent_bitflip_distribution(ideal,len(obj.variables),e)
      optimum_p=sum(p for p,en in zip(dist,energies) if math.isclose(en,ref,abs_tol=1e-10))
      expected=sum(p*en for p,en in zip(dist,energies))
      for shots in (128,512,2048,8192):
        counts=sample_distribution(dist,shots,seed=seed+shots+round(e*100000))
        hit=sum(c for k,c in counts.items() if math.isclose(energies[k],ref,abs_tol=1e-10))
        rows.append({"readout_bitflip_probability":e,"shots":shots,"expected_objective":expected,
          "optimum_probability_per_shot":optimum_p,"observed_optimum_hits":hit,
          "observed_optimum_hit_fraction":hit/shots})
    return {"name":name,"qubits":len(obj.variables),"exact_optimum":ref,"selected_gamma":g,"selected_beta":b,
      "selected_ideal_expected_objective":best[0],"rows":rows}

out={"schema":"uqpu-batch014-synthetic-readout-sensitivity-v1","evidence_level":"SYNTHETIC_NOISE_SIMULATION",
 "noise_model":"independent symmetric classical bit flip applied after ideal circuit measurement",
 "calibrated_hardware_model":False,"paid_job_submitted":False,"quantum_advantage_demonstrated":False,
 "fixtures":[fixture("triangle",demo_maxcut_triangle(),12),
 fixture("er6",seeded_erdos_renyi_maxcut(6,0.5,42),42),
 fixture("er8",seeded_erdos_renyi_maxcut(8,0.4,73),73)],
 "limitations":["Readout-only synthetic channel; no gate, coherence, crosstalk, leakage, drift or routing noise.",
 "Finite-shot draws are pseudorandom CPU simulation, not QPU samples.","No cost or speed advantage is inferred."]}
print(json.dumps(out,sort_keys=True,indent=2))
