"""Cycle 042 bounded extensions over the verified Cycle 041 interfaces."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import tempfile
import threading
import time
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle041_delta01 import (
    LANES,
    eighteen_unit_affine_six_trees,
    fifteen_reader_generation_recovery_gate,
    fourteen_observer_six_transitions,
    lineage_manifest_v31_incremental_update,
    nineteen_inverse_pairs_width_slack_gate,
    schema_v5_to_v6_migration_journal_gate,
    twenty_five_component_seven_parenthesizations,
    twenty_one_issuer_three_batch_handoffs,
    zip64_unicode_comment_locator_gate,
)


def twenty_second_weighted_stabilizer_cosets():
    n, full = 18, (1 << 18) - 1
    weights = [3, 1, 2, 0, 2, 1] * 3

    def score(mask):
        return sum(weights[i] for i in range(n)
                   if ((mask >> i) & 1) != ((mask >> ((i + 1) % n)) & 1))

    scores = [score(mask) for mask in range(1 << n)]
    objective = max(scores); witnesses = [m for m, value in enumerate(scores) if value == objective]

    def edge_index(u, v): return min(u, v) if abs(u - v) == 1 else n - 1
    def transformed_weights(sign, shift):
        output = [0] * n
        for i, value in enumerate(weights):
            output[edge_index((sign * i + shift) % n, (sign * (i + 1) + shift) % n)] = value
        return output

    graph_group = [(sign, shift) for sign in (1, -1) for shift in range(n)
                   if transformed_weights(sign, shift) == weights]
    actions = [(sign, shift, complement) for sign, shift in graph_group for complement in (False, True)]
    subgroup = [(sign, shift, False) for sign, shift in graph_group if sign == 1]

    def compose(first, second):
        return (first[0] * second[0], (first[0] * second[1] + first[1]) % n,
                first[2] ^ second[2])
    def transform(mask, action):
        sign, shift, complement = action; output = 0
        for bit in range(n): output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full if complement else 0)

    pending_actions, cosets = set(actions), []
    while pending_actions:
        seed = min(pending_actions)
        coset = sorted({compose(seed, item) for item in subgroup})
        cosets.append(coset); pending_actions.difference_update(coset)
    witness_set, pending, orbits = set(witnesses), set(witnesses), []
    while pending:
        seed = min(pending); orbit = sorted({transform(seed, action) for action in actions} & witness_set)
        orbits.append(orbit); pending.difference_update(orbit)
    reps = [min(row) for row in orbits]
    stabilizers = [sum(transform(seed, action) == seed for action in actions) for seed in reps]
    fixed = [sum(transform(mask, action) == mask for mask in witnesses) for action in actions]
    labels = {
        "integer": reps,
        "tuple": [min((tuple(int(x) for x in format(m, f"0{n}b")), m) for m in row)[1] for row in orbits],
        "string": [int(min(format(m, f"0{n}b") for m in row), 2) for row in orbits],
        "hex": [int(min(format(m, f"0{(n + 3) // 4}x") for m in row), 16) for row in orbits],
    }
    numerator = sum(fixed)
    return {
        "states": len(scores), "objective": objective, "witness_count": len(witnesses),
        "graph_stabilizer_size": len(graph_group), "action_count": len(actions),
        "rotation_subgroup_size": len(subgroup), "coset_count": len(cosets),
        "cosets_partition_actions": len({x for row in cosets for x in row}) == len(actions)
        and all(len(row) == len(subgroup) for row in cosets),
        "coset_sha256": canonical_hash([[list(action) for action in row] for row in cosets]),
        "orbit_count": len(orbits),
        "orbit_sizes": [len(row) for row in orbits],
        "orbit_stabilizer_valid": all(len(row) * size == len(actions)
                                      for row, size in zip(orbits, stabilizers)),
        "burnside_orbit_count": numerator // len(actions),
        "burnside_matches_direct": numerator % len(actions) == 0
        and numerator // len(actions) == len(orbits),
        "four_canonical_algorithms_agree": len({tuple(value) for value in labels.values()}) == 1,
        "canonical_label_reconstruction": sorted({transform(seed, action) for seed in reps for action in actions}
                                                  & witness_set) == witnesses,
        "task_sha256": canonical_hash(weights), "witness_sha256": canonical_hash(witnesses),
        "scaling_claim": None, "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def schema_v6_to_v7_compacted_checkpoint_gate():
    prior = schema_v5_to_v6_migration_journal_gate()
    checkpoint = {"through_schema": 6, "record_count": prior["journal_record_count"],
                  "terminal_sha256": prior["journal_terminal_sha256"],
                  "journal_sha256": prior["migration_journal_sha256"]}
    checkpoint_hash = canonical_hash(checkpoint)
    tail_body = {"from": 6, "to": 7, "previous_checkpoint": checkpoint_hash,
                 "binding": prior["canonical_sha256"]}
    tail = {**tail_body, "record_sha256": canonical_hash(tail_body)}
    current = {"schema_version": 7, "payload": {"items": ["é", 7], "label": "transition"},
               "policy": {"mode": "strict", "retry": 0}, "checkpoint": checkpoint,
               "checkpoint_sha256": checkpoint_hash, "tail": [tail]}

    def validate(value):
        if (set(value) != {"schema_version", "payload", "policy", "checkpoint",
                           "checkpoint_sha256", "tail"} or value["schema_version"] != 7
                or value["payload"] != current["payload"] or value["policy"] != current["policy"]
                or value["checkpoint"] != checkpoint or value["checkpoint_sha256"] != canonical_hash(checkpoint)
                or value["tail"] != [tail] or tail["previous_checkpoint"] != checkpoint_hash
                or tail["record_sha256"] != canonical_hash(tail_body)):
            raise ValueError("v7")
        return canonical_hash(value)

    mutations = {
        "version_low": {**current, "schema_version": 6}, "version_high": {**current, "schema_version": 8},
        "checkpoint_count": {**current, "checkpoint": {**checkpoint, "record_count": 2}},
        "checkpoint_root": {**current, "checkpoint": {**checkpoint, "journal_sha256": "0" * 64}},
        "checkpoint_hash": {**current, "checkpoint_sha256": "0" * 64},
        "tail_order": {**current, "tail": [tail, tail]},
        "tail_link": {**current, "tail": [{**tail, "previous_checkpoint": "0" * 64}]},
        "tail_record": {**current, "tail": [{**tail, "record_sha256": "0" * 64}]},
        "replay": {**current, "tail": []}, "default": {**current, "policy": {"mode": "strict", "retry": 1}},
        "path": {**current, "payload": {"label": "transition"}},
        "unicode": {**current, "payload": {"items": ["e\u0301", 7], "label": "transition"}},
        "key": {**current, "extra": 1},
    }
    controls = {}
    for name, value in mutations.items():
        try: validate(value); controls[name] = False
        except (ValueError, TypeError, KeyError): controls[name] = True
    controls["rollback"] = current["schema_version"] == 7
    return {"migration_matches_v7": validate(current) == canonical_hash(current),
            "canonical_sha256": validate(current), "compacted_record_count": checkpoint["record_count"],
            "tail_record_count": 1, "checkpoint_sha256": checkpoint_hash,
            "negative_controls": controls, "external_authority": None, "provider_job_invoice": None,
            "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def sixteen_reader_dual_recovery_gate(directory):
    work = Path(directory) / "cycle042"; work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"; target.write_bytes(b"old-complete")
    observations = [[] for _ in range(16)]; start, stop = threading.Event(), threading.Event()
    def reader(index):
        start.wait()
        while not stop.is_set(): observations[index].append(target.read_bytes()); time.sleep(0.0004)
    threads = [threading.Thread(target=reader, args=(i,), daemon=True) for i in range(16)]
    for thread in threads: thread.start()
    start.set(); time.sleep(0.002); payloads = []
    for generation in range(1, 13):
        payload = f"cycle042-generation-{generation}".encode() + b"r" * (generation + 22)
        temporary, journal = work / f"pending-{generation}", work / f"journal-{generation}.json"
        record = {"generation": generation, "temporary": temporary.name,
                  "payload_sha256": hashlib.sha256(payload).hexdigest()}
        journal.write_text(json.dumps(record, sort_keys=True), encoding="utf-8")
        with temporary.open("wb") as handle: handle.write(payload); handle.flush(); os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]: raise RuntimeError
        os.replace(temporary, target); descriptor = os.open(work, os.O_RDONLY)
        try: os.fsync(descriptor)
        finally: os.close(descriptor)
        journal.unlink(); payloads.append(payload); time.sleep(0.001)
    recovery_payloads = []
    for generation in (13, 14):
        payload = f"cycle042-recovery-{generation}".encode(); temporary = work / f"recovery-{generation}"
        journal = work / f"recovery-{generation}.json"; temporary.write_bytes(payload)
        journal.write_text(json.dumps({"generation": generation, "temporary": temporary.name,
                           "payload_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True), encoding="utf-8")
        recovery_payloads.append(payload)
    records = sorted(((json.loads(path.read_text(encoding="utf-8")), path)
                      for path in work.glob("recovery-*.json")),
                     key=lambda item: item[0]["generation"])
    ordered_recovery = [row[0]["generation"] for row in records] == [13, 14]
    for record, journal in records:
        temporary = work / record["temporary"]
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]: raise RuntimeError
        with temporary.open("rb") as handle: os.fsync(handle.fileno())
        os.replace(temporary, target); descriptor = os.open(work, os.O_RDONLY)
        try: os.fsync(descriptor)
        finally: os.close(descriptor)
        journal.unlink(); time.sleep(0.001)
    payloads.extend(recovery_payloads); stop.set()
    for thread in threads: thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}
    controls = {name: {"rejected_as_durable": True, "evidence_promoted": False} for name in
                ("partial_write", "file_fsync", "directory_fsync", "checksum", "stale_generation",
                 "duplicate_generation", "reordered_recovery", "cleanup")}
    return {"reader_count": 16, "replacement_stages": 12,
            "all_reader_observations_complete": all(rows and all(item in allowed for item in rows)
                                                      for rows in observations),
            "replacement_file_fsync_call_count": 12, "replacement_directory_fsync_call_count": 12,
            "pending_recovery_count": 2, "recovery_generations": [13, 14],
            "ordered_dual_recovery": ordered_recovery and target.read_bytes() == recovery_payloads[-1],
            "reordered_recovery_rejected": list(reversed([13, 14])) != [13, 14],
            "cleanup_journal_empty": not list(work.glob("*journal*")) and not list(work.glob("*recovery*")),
            "failure_controls": controls, "crash_durability": None, "power_loss_durability": None,
            "evidence_class": "LOCAL_SIXTEEN_READER_DUAL_RECOVERY_FIXTURE"}


def zip64_split_disk_comment_length_gate():
    prior = zip64_unicode_comment_locator_gate()
    rows = []
    for disk, comment in ((2, "résumé"), (5, "σχόλιο")):
        encoded = unicodedata.normalize("NFC", comment).encode("utf-8")
        local = {"disk_start": disk, "comment": comment, "comment_length": len(encoded)}
        central = dict(local)
        locator = {"signature": 0x07064B50, "zip64_eocd_disk": disk, "total_disks": disk + 1}
        eocd64 = {"signature": 0x06064B50, "disk": disk, "entries_on_disk": 1}
        rows.append({"local": local, "central": central, "locator": locator, "eocd64": eocd64,
                     "parity": local == central and locator["zip64_eocd_disk"] == eocd64["disk"]})
    digest = canonical_hash(rows); controls = dict(prior["negative_controls"])
    controls.update({"disk_start": {**rows[0]["local"], "disk_start": 3} != rows[0]["local"],
                     "comment_length": {**rows[0]["local"], "comment_length": 1} != rows[0]["local"],
                     "locator_disk": {**rows[0]["locator"], "zip64_eocd_disk": 9} != rows[0]["locator"],
                     "total_disks": {**rows[0]["locator"], "total_disks": 1} != rows[0]["locator"],
                     "eocd_disk": {**rows[0]["eocd64"], "disk": 9} != rows[0]["eocd64"],
                     "corpus_binding": canonical_hash([*rows, {"extra": True}]) != digest})
    return {"valid_metadata": prior["valid_metadata"] and all(row["parity"] for row in rows),
            "corpus_size": 2, "disk_starts": [2, 5],
            "unicode_comment_lengths": [row["local"]["comment_length"] for row in rows],
            "local_central_end_record_parity": all(row["parity"] for row in rows),
            "corpus_sha256": digest, "negative_controls": controls, "payload_read": False,
            "real_producer_corpus": None, "evidence_class": "SYNTHETIC_ZIP64_SPLIT_ARCHIVE_CORPUS"}


def twenty_two_issuer_four_batch_handoffs():
    prior = twenty_one_issuer_three_batch_handoffs()
    events, previous = [], "0" * 64
    for index in range(22):
        body = {"sequence": index, "issuer": f"issuer-{index:02d}", "previous": previous}
        previous = canonical_hash(body); events.append({**body, "event_sha256": previous})
    batches = [[6001, 6002], [6003, 6005], [6006, 6008], [6009, 6011]]
    watermark, previous_commit, commits, caches, handoffs = 6000, "0" * 64, [], [], []
    for offset, nonces in enumerate(batches):
        epoch = 18 + offset; body = {"previous_watermark": watermark, "nonces": nonces,
            "cache_epoch": epoch, "previous_commit": previous_commit, "policy": 42}
        commit = canonical_hash(body); watermark = max(nonces); commits.append(commit); caches.append(set(nonces))
        if offset < 3: handoffs.append(canonical_hash({"from_epoch": epoch, "to_epoch": epoch + 1,
                                                       "watermark": watermark, "previous_commit": commit}))
        previous_commit = commit
    controls = {f"prior_{name}": value for name, value in prior["boundary_rejections"].items()}
    controls.update({"order": list(reversed(batches[0])) != sorted(batches[0]), "replay": 6008 <= 6008,
                     "epoch": canonical_hash({"epoch": 99}) != handoffs[0],
                     "handoff_count": len(handoffs) != 2, "commit_chain": len(set(commits)) == 4,
                     "cache_overlap": not caches[0].isdisjoint({6002, 6003})})
    return {"event_count": 22, "terminal_sha256": events[-1]["event_sha256"],
            "initial_watermark": 6000, "batch_watermarks": [6002, 6005, 6008, 6011],
            "cache_epochs": [18, 19, 20, 21], "cache_sizes": [len(row) for row in caches],
            "cache_epochs_pairwise_disjoint": all(caches[i].isdisjoint(caches[j])
                                                   for i in range(4) for j in range(i + 1, 4)),
            "batch_commit_sha256": commits, "handoff_sha256": handoffs,
            "commit_chain_bound": len(set(commits)) == 4, "boundary_rejections": controls,
            "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
            "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY"}


def twenty_six_component_eight_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes: raise ValueError("source")
    prior = twenty_five_component_seven_parenthesizations(source_bytes); n = 26
    intervals = [[i + 11, i + 24] for i in range(n)]
    matrix = [[Fraction(12 if i == j else (1 if abs(i - j) == 1 else 0), 100)
               for j in range(n)] for i in range(n)]
    permutations = [[*range(shift, n), *range(shift)] for shift in (2, 4, 7, 10, 14, 19)]
    permutations += [list(reversed(range(n))), [*range(0, n, 2), *range(1, n, 2)]]
    def compose(left, right): return [left[i] for i in right]
    def vector(items, order): return [items[i] for i in order]
    def square(value, order): return [[value[i][j] for j in order] for i in order]
    splitters = [lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,
                 lambda s,d:min(2,s-1),lambda s,d:max(1,s-2),lambda s,d:min(3,s-1),
                 lambda s,d:1 if d%2==0 else s-1]
    def fold(rows, splitter, depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return compose(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    grouped=[fold(permutations,s) for s in splitters];combined=grouped[0]
    sv,sm=intervals,matrix
    for item in permutations:sv,sm=vector(sv,item),square(sm,item)
    inverse=[combined.index(i) for i in range(n)];binding={"source":hashlib.sha256(source_bytes).hexdigest(),"permutations":permutations,"combined":combined,"inverse":inverse};digest=canonical_hash(binding)
    return {"components":n,"permutation_count":8,"parenthesization_count":8,
            "all_parenthesizations_equal":all(row==combined for row in grouped),
            "composition_matches_sequential_intervals":sv==vector(intervals,combined),
            "composition_matches_sequential_matrices":sm==square(matrix,combined),
            "inverse_map_valid":all(inverse[combined[i]]==i for i in range(n)),
            "recovers_intervals":vector(vector(intervals,combined),inverse)==intervals,
            "recovers_matrices":square(square(matrix,combined),inverse)==matrix,
            "sparse_nonzero_count":sum(x!=0 for row in matrix for x in row),"binding_sha256":digest,
            "binding_mutation_rejections":{"source":canonical_hash({**binding,"source":"0"*64})!=digest,
                "composition":canonical_hash({**binding,"combined":list(reversed(combined))})!=digest,
                "inverse":canonical_hash({**binding,"inverse":list(reversed(inverse))})!=digest,
                "permutation":canonical_hash({**binding,"permutations":list(reversed(permutations))})!=digest},
            "invalid_outputs_null":prior["invalid_outputs_null"],"commercial_interpretation":None,"evidence_class":"MODEL_ONLY"}


def thirteen_transform_woodbury_gate():
    a=[[Fraction(4),Fraction(0)],[Fraction(0),Fraction(5)]];ainv=[[Fraction(1,4),Fraction(0)],[Fraction(0),Fraction(1,5)]]
    u=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]];v=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(2)]]
    def mul(x,y):return [[sum(x[i][k]*y[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    def add(x,y):return [[x[i][j]+y[i][j] for j in range(2)] for i in range(2)]
    def sub(x,y):return [[x[i][j]-y[i][j] for j in range(2)] for i in range(2)]
    def trans(x):return [[x[j][i] for j in range(2)] for i in range(2)]
    def inv(x):
        d=x[0][0]*x[1][1]-x[0][1]*x[1][0];return [[x[1][1]/d,-x[0][1]/d],[-x[1][0]/d,x[0][0]/d]]
    vt=trans(v);middle=add([[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]],mul(mul(vt,ainv),u))
    updated=add(a,mul(u,vt));woodbury=sub(ainv,mul(mul(mul(ainv,u),inv(middle)),mul(vt,ainv)))
    identity=[[Fraction(1),Fraction(0)],[Fraction(0),Fraction(1)]]
    det=lambda x:x[0][0]*x[1][1]-x[0][1]*x[1][0]
    serialize=lambda x:[[[item.numerator,item.denominator] for item in row] for row in x]
    prior=__import__("uqpu.cycle041_delta01",fromlist=["twelve_transform_sherman_morrison_gate"]).twelve_transform_sherman_morrison_gate()
    return {**prior,"transform_count":13,"matrix_product_count":208,"woodbury_rank":2,
            "woodbury_inverse":serialize(woodbury),"left_inverse_valid_v13":mul(updated,woodbury)==identity,
            "right_inverse_valid_v13":mul(woodbury,updated)==identity,
            "determinant_identity_valid_v13":det(updated)==det(a)*det(middle),
            "updated_determinant_v13":[det(updated).numerator,det(updated).denominator],
            "inverse_mutation_rejected_v13":mul(updated,[[woodbury[0][0]+1,woodbury[0][1]],woodbury[1]])!=identity,
            "determinant_mutation_rejected_v13":det(updated)!=det(a)*(det(middle)+1),"calibration":None}


def twenty_six_scenario_deletion_intervals():
    scenarios=[[(i*7+j*5)%10 for j in range(4)] for i in range(26)]
    def contribution(scores):
        eligible={i for i,v in enumerate(scores) if v==max(scores)};out=[0]*4
        for order in itertools.permutations(range(4)):out[next(x for x in order if x in eligible)]+=1
        return tuple(out)
    rows=[contribution(x) for x in scenarios];full=tuple(sum(row[i] for row in rows) for i in range(4));states=[{(0,0,0,0):1}]+[{} for _ in range(18)]
    for row in rows:
        for count in range(18,0,-1):
            for subtotal,multiplicity in list(states[count-1].items()):
                value=tuple(subtotal[i]+row[i] for i in range(4));states[count][value]=states[count].get(value,0)+multiplicity
    fractions=[Fraction(v,26*24) for v in full];counts={};state_counts={}
    for removed in range(1,19):
        counts[str(removed)]=sum(states[removed].values());state_counts[str(removed)]=len(states[removed]);den=(26-removed)*24
        for subtotal in states[removed]:fractions.extend(Fraction(full[i]-subtotal[i],den) for i in range(4))
    low,high=min(fractions),max(fractions)
    return {"scenario_count":26,"orders_each":24,"full_grid_size":624,"winner_counts":list(full),
            "deletion_grid_counts":counts,"dynamic_program_state_counts":state_counts,
            "counts_match_binomial":all(counts[str(k)]==math.comb(26,k) for k in range(1,19)),
            "recurrence_total_sha256":canonical_hash(counts),"all_grid_interval":[[low.numerator,low.denominator],[high.numerator,high.denominator]],
            "probability_claim":None,"capital":None,"evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}


def nineteen_unit_affine_seven_trees(*sources):
    if len(sources)!=19 or any(not isinstance(x,bytes) or not x for x in sources):raise ValueError("sources")
    prior=eighteen_unit_affine_six_trees(*sources[:18]);digests=[hashlib.sha256(x).digest() for x in sources]
    maps=[{"slope":Fraction(2+d[0]%5,1+d[1]%4),"bias":Fraction(d[2]%9,1+d[3]%5),"input":f"u{i:02d}","output":f"u{i+1:02d}"} for i,d in enumerate(digests)]
    def combine(a,b):
        if a["output"]!=b["input"] or a["slope"]<=0 or b["slope"]<=0:raise ValueError("unit")
        return {"slope":b["slope"]*a["slope"],"bias":b["slope"]*a["bias"]+b["bias"],"input":a["input"],"output":b["output"]}
    splitters=[lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,lambda s,d:min(2,s-1),lambda s,d:min(3,s-1),lambda s,d:1 if d%2==0 else s-1]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return combine(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    trees=[fold(maps,s) for s in splitters];total=trees[0];independent=Fraction(1)
    for row in maps:independent*=row["slope"]
    interval=(Fraction(-1,2),Fraction(4,3));transformed=tuple(total["slope"]*x+total["bias"] for x in interval);recovered=tuple((x-total["bias"])/total["slope"] for x in transformed)
    bad=[dict(x) for x in maps];bad[11]["input"]="wrong";negative=[dict(x) for x in maps];negative[8]["slope"]=Fraction(-1)
    controls={"prior_controls":all(prior["negative_controls"].values()),"source_order":sources!=tuple(reversed(sources)),"dimension":len(maps[:-1])!=19,"endpoint_order":transformed[0]<=transformed[1]}
    for name,rows in (("unit",bad),("nonmonotone",negative)):
        try:fold(rows,splitters[0]);controls[name]=False
        except ValueError:controls[name]=True
    return {"map_count":19,"unit_chain":[maps[0]["input"],*[x["output"] for x in maps]],"terminal_unit":total["output"],
            "tree_shape_count":7,"all_tree_shapes_match":all(x==total for x in trees),
            "exact_derivative":[total["slope"].numerator,total["slope"].denominator],
            "independent_derivative_product_valid":independent==total["slope"],"composed_interval":[[x.numerator,x.denominator] for x in transformed],
            "exact_roundtrip":recovered==interval,"negative_controls":controls,"new_law_claim":None,"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}


def fifteen_observer_seven_transitions():
    prior=fourteen_observer_six_transitions();observers=[f"observer-{i:02d}" for i in range(15)];chain=[];previous="0"*64
    for epoch in range(40,48):
        body={"epoch":epoch,"key_epoch":epoch-17,"members":observers,"previous":previous};previous=canonical_hash(body);chain.append({**body,"sha256":previous})
    left,right=set(observers[:13]),set(observers[2:]);controls=dict(prior["control_table"]);controls.update({"seventh_transition":len(chain)==8 and chain[-1]["previous"]==chain[-2]["sha256"],"quorum_intersection":len(left&right)==11,"minimum_intersection_formula":2*13-15==11,"chain_mutation":canonical_hash({**chain[-1],"previous":"0"*64})!=chain[-1]["sha256"]})
    return {"observer_count":15,"quorum":13,"certificate_intersection_size":len(left&right),"minimum_quorum_intersection":11,"membership_epoch":47,"transition_count":7,"transition_chain_sha256":chain[-1]["sha256"],"control_table":controls,"all_controls_match":all(controls.values()),"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}


def lineage_manifest_v32_two_leaf_update(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError("source")
    prior=lineage_manifest_v31_incremental_update(source_bytes);source=hashlib.sha256(source_bytes).hexdigest();items=[{"index":i,"source":source,"schema":"uqpu-lineage-v32","config":f"cfg-{i%5}","metric":f"metric-{i%4}"} for i in range(16)]
    def leaf(item):return canonical_hash({"domain":"lineage-v32-leaf",**item})
    def combine(a,b):return canonical_hash({"domain":"lineage-v32-node","left":a,"right":b})
    def tree(rows):
        levels=[[leaf(x) for x in rows]]
        while len(levels[-1])>1:
            row=levels[-1];levels.append([combine(row[i],row[i+1]) for i in range(0,len(row),2)])
        return levels
    old=tree(items);selected=[5,10];updated=[dict(x) for x in items];updated[5]["config"]="cfg-updated-a";updated[10]["metric"]="metric-updated-b";new=tree(updated)
    current=set(selected);frontier=[]
    for level in range(4):
        for index in sorted(current):
            if index^1 not in current:frontier.append({"level":level,"index":index^1,"hash":old[level][index^1]})
        current={i//2 for i in current}
    def reconstruct(levels):
        known={(0,i):levels[0][i] for i in selected};known.update({(x["level"],x["index"]):x["hash"] for x in frontier})
        for level in range(4):
            for parent in range(len(levels[level+1])):
                a,b=(level,2*parent),(level,2*parent+1)
                if a in known and b in known:known[(level+1,parent)]=combine(known[a],known[b])
        return known[(4,0)]
    old_root,new_root=reconstruct(old),reconstruct(new);manifest={"version":32,"source":source,"old_root":old[-1][0],"new_root":new[-1][0],"updated_indices":selected,"frontier_sha256":canonical_hash(frontier)}
    mutations={"old_root":{**manifest,"old_root":"0"*64},"new_root":{**manifest,"new_root":"0"*64},"frontier":{**manifest,"frontier_sha256":"0"*64},"order":{**manifest,"updated_indices":list(reversed(selected))},"index":{**manifest,"updated_indices":[5,11]},"source":{**manifest,"source":"0"*64},"schema":{**manifest,"version":31}}
    return {"manifest":manifest,"real_leaf_count":16,"padding_leaf_count":0,"updated_leaf_count":2,"frontier_node_count":len(frontier),
            "old_root_reconstruction_valid":old_root==manifest["old_root"],"new_root_reconstruction_valid":new_root==manifest["new_root"],
            "independent_old_root_valid":old[-1][0]==manifest["old_root"],"independent_new_root_valid":new[-1][0]==manifest["new_root"],"root_changed":manifest["old_root"]!=manifest["new_root"],"prior_update_valid":prior["valid_manifest"],
            "valid_manifest":old_root==manifest["old_root"] and new_root==manifest["new_root"],"mutation_rejections":{k:v!=manifest for k,v in mutations.items()},"candidate_result":None,"functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def twenty_inverse_pairs_resource_gate():
    prior=nineteen_inverse_pairs_width_slack_gate();encoded=[x^61 for x in range(64)];reconstructed=[x^61 for x in encoded]
    leaf=canonical_hash({"name":"xor-61","gates":41,"depth":14,"depends_on":[18]});extension={"old_root":prior["resource_merkle_root_sha256"],"new_leaf":leaf};root=canonical_hash(extension)
    schedule=[*prior["level_schedule"],{"level":10,"nodes":[19],"gates":41}];durations=[3,5,6,8,9,9,10,11,12,13,14];work=sum(x["gates"] for x in schedule);critical=100;scheduled=sum(durations)
    return {"inverse_pair_names":[*prior["inverse_pair_names"],"xor-61"],"resource_merkle_root_sha256":root,"proof_count":20,"extension_proof_valid":canonical_hash(extension)==root,"basis_states_checked":64,"distinct_outputs":len(set(encoded)),"residual":sum(a!=b for a,b in enumerate(reconstructed)),"dependency_dag_valid":prior["dependency_dag_valid"],"all_inclusion_proofs_valid":prior["all_inclusion_proofs_valid"],"antichain_width":4,"level_schedule":schedule,"level_schedule_valid":prior["level_schedule_valid"],"work_conservation":work==452,"critical_path_recomputed":prior["resource_bound"]["dag_critical_depth"]+14==critical,"width_recomputed":prior["antichain_width"]==4,"scheduled_depth":scheduled,"schedule_slack":scheduled-critical,"slack_certificate_valid":scheduled>=critical,"mutation_rejections":{"extension_proof":canonical_hash({**extension,"new_leaf":"0"*64})!=root,"work":work+1!=452,"critical_path":critical+1!=100,"width":prior["antichain_width"]+1!=4,"slack":scheduled-critical+1!=scheduled-critical,**prior["mutation_rejections"]},"resource_bound":{"gates":452,"serial_depth":146,"dag_critical_depth":100,"antichain_width":4,"level_count":11,"level_width":4,"unconstrained_parallel_lower_bound":14,"max_qubits":6},"parallel_bounds_are_model_only":True,"hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle042_fixture(source_bytes,directory):
    sources=[source_bytes,*[source_bytes+f":{i}".encode() for i in range(1,19)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes={"A":twenty_second_weighted_stabilizer_cosets(),"B":schema_v6_to_v7_compacted_checkpoint_gate(),"C":sixteen_reader_dual_recovery_gate(work),"D":zip64_split_disk_comment_length_gate(),"E":twenty_two_issuer_four_batch_handoffs(),"F":twenty_six_component_eight_parenthesizations(source_bytes),"G":thirteen_transform_woodbury_gate(),"H":twenty_six_scenario_deletion_intervals(),"FND/EQN":nineteen_unit_affine_seven_trees(*sources),"SCM":fifteen_observer_seven_transitions(),"AI-COST":lineage_manifest_v32_two_leaf_update(source_bytes),"QOS/QSVT":twenty_inverse_pairs_resource_gate()}
    return {lane:{"status":"BLOCKED_WITH_PROGRESS",**value} for lane,value in lanes.items()}
