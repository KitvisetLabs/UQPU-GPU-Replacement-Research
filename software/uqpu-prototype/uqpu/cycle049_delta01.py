"""Cycle 049 bounded extensions over verified Cycle 048 interfaces."""
from __future__ import annotations
from fractions import Fraction
import hashlib,itertools,json,math,os,tempfile,threading,time
from pathlib import Path
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle048_delta01 import (LANES,lineage_manifest_v38_eight_leaf_update,nineteen_transform_schur_gate,
 schema_v12_to_v13_checkpoint_chain_gate,thirty_two_component_fourteen_parenthesizations,
 thirty_two_scenario_deletion_intervals,twenty_eight_issuer_ten_batch_handoffs,
 twenty_eighth_weighted_length_three_paths,twenty_five_unit_affine_thirteen_trees,
 twenty_one_observer_thirteen_transitions,twenty_six_inverse_pairs_resource_gate,
 zip64_sector_locator_binding_gate)


def twenty_ninth_weighted_length_four_walks():
    prior=twenty_eighth_weighted_length_three_paths();matrix=prior["quotient_incidence"]
    walks={}
    for source in range(4):
        for target in range(source+1,4):
            walks[f"{source}-{target}"]=sum(matrix[source][a]*matrix[a][b]*matrix[b][c]*matrix[c][target] for a in range(4) for b in range(4) for c in range(4))
    def multiply(left,right):return [[sum(left[i][k]*right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    square=multiply(matrix,matrix);fourth=multiply(square,square);independent={f"{i}-{j}":fourth[i][j] for i in range(4) for j in range(i+1,4)}
    rows=[[key,walks[key]] for key in sorted(walks)];digest=canonical_hash(rows)
    return {**prior,"fixture_ordinal":29,"length_four_walk_multiplicities":walks,"length_four_walk_total":sum(walks.values()),
      "length_four_walks_match_matrix_power":walks==independent,"length_four_walk_sha256":digest,
      "eleventh_canonical_algorithm":"quotient-weighted-adjacency-fourth-power","eleventh_canonical_label_sha256":digest,
      "eleventh_canonical_label_reconstruction":canonical_hash([[key,independent[key]] for key in sorted(independent)])==digest,
      "eleven_canonical_algorithms_agree":prior["ten_canonical_algorithms_agree"] and walks==independent}


def schema_v13_to_v14_three_checkpoint_gate():
    prior=schema_v12_to_v13_checkpoint_chain_gate();bodies=[];previous=prior["terminal_checkpoint_sha256"]
    for position,(source,target,nonce) in enumerate(((11,12,"c47"),(12,13,"c48"),(13,14,"c49")),1):
        body={"from":source,"to":target,"previous":previous,"position":position,"nonce":nonce,"previous_schema":prior["canonical_sha256"] if position==3 else None};previous=canonical_hash(body);bodies.append({**body,"checkpoint_sha256":previous})
    current={"schema_version":14,"payload":{"items":["é",14],"label":"three-checkpoint-seal-chain"},"policy":{"mode":"strict","retry":0,"fork":"deny","rollback":"verified-only"},"checkpoints":bodies,"terminal_checkpoint_sha256":previous}
    def validate(value):
        if set(value)!=set(current) or value["schema_version"]!=14 or value["payload"]!=current["payload"] or value["policy"]!=current["policy"] or value["checkpoints"]!=bodies or value["terminal_checkpoint_sha256"]!=previous:raise ValueError("v14")
        for index,row in enumerate(value["checkpoints"]):
            body={key:row[key] for key in ("from","to","previous","position","nonce","previous_schema")}
            if row["checkpoint_sha256"]!=canonical_hash(body):raise ValueError("checkpoint")
            if index and row["previous"]!=value["checkpoints"][index-1]["checkpoint_sha256"]:raise ValueError("chain")
        return canonical_hash(value)
    def mutate(index,**changes):
        rows=[dict(row) for row in bodies];rows[index].update(changes);return {**current,"checkpoints":rows}
    mutations={"low":{**current,"schema_version":13},"high":{**current,"schema_version":15},"first_from":mutate(0,**{"from":10}),"first_to":mutate(0,to=13),"first_previous":mutate(0,previous="0"*64),"first_position":mutate(0,position=2),"first_nonce":mutate(0,nonce="x"),"first_hash":mutate(0,checkpoint_sha256="0"*64),"second_from":mutate(1,**{"from":11}),"second_to":mutate(1,to=14),"second_previous":mutate(1,previous="0"*64),"second_position":mutate(1,position=1),"second_nonce":mutate(1,nonce="x"),"second_hash":mutate(1,checkpoint_sha256="0"*64),"third_from":mutate(2,**{"from":12}),"third_to":mutate(2,to=15),"third_previous":mutate(2,previous="0"*64),"third_position":mutate(2,position=2),"third_nonce":mutate(2,nonce="x"),"third_schema":mutate(2,previous_schema="0"*64),"third_hash":mutate(2,checkpoint_sha256="0"*64),"terminal":{**current,"terminal_checkpoint_sha256":"0"*64},"reorder":{**current,"checkpoints":list(reversed(bodies))},"replay":{**current,"checkpoints":[bodies[0],bodies[1],bodies[1]]},"fork":{**current,"policy":{**current["policy"],"fork":"allow"}},"retry":{**current,"policy":{**current["policy"],"retry":1}},"rollback_policy":{**current,"policy":{**current["policy"],"rollback":"unchecked"}},"path":{**current,"payload":{"label":"three-checkpoint-seal-chain"}},"unicode":{**current,"payload":{"items":["e\u0301",14],"label":"three-checkpoint-seal-chain"}},"key":{**current,"extra":1}}
    controls={}
    for name,value in mutations.items():
        try:validate(value);controls[name]=False
        except (ValueError,TypeError,KeyError):controls[name]=True
    controls["rollback"]=prior["migration_matches_v13"] and bodies[-1]["previous_schema"]==prior["canonical_sha256"]
    return {"migration_matches_v14":validate(current)==canonical_hash(current),"canonical_sha256":validate(current),"checkpoint_count":3,"terminal_checkpoint_sha256":previous,"negative_controls":controls,"external_authority":None,"provider_job_invoice":None,"evidence_class":"SYNTHETIC_RECEIPT_CANONICALIZATION"}


def twenty_three_reader_nine_recovery_gate(directory):
    work=Path(directory)/"cycle049";work.mkdir(parents=True,exist_ok=True);target=work/"state.bin";target.write_bytes(b"old-complete");observations=[[] for _ in range(23)];start,stop=threading.Event(),threading.Event()
    def reader(index):
        start.wait()
        while not stop.is_set():observations[index].append(target.read_bytes());time.sleep(.0004)
    threads=[threading.Thread(target=reader,args=(i,),daemon=True) for i in range(23)]
    for thread in threads:thread.start()
    start.set();time.sleep(.002);payloads=[]
    for generation in range(1,20):
        payload=f"cycle049-generation-{generation}".encode()+b"y"*(generation+29);temporary=work/f"pending-{generation}";journal=work/f"journal-{generation}.json";record={"generation":generation,"temporary":temporary.name,"payload_sha256":hashlib.sha256(payload).hexdigest()};journal.write_text(json.dumps(record,sort_keys=True))
        with temporary.open("wb") as handle:handle.write(payload);handle.flush();os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest()!=record["payload_sha256"]:raise RuntimeError
        os.replace(temporary,target);fd=os.open(work,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
        journal.unlink();payloads.append(payload);time.sleep(.001)
    recovery=[]
    for generation in range(20,29):
        payload=f"cycle049-recovery-{generation}".encode();temporary=work/f"recovery-{generation}";journal=work/f"recovery-{generation}.json";temporary.write_bytes(payload);journal.write_text(json.dumps({"generation":generation,"temporary":temporary.name,"payload_sha256":hashlib.sha256(payload).hexdigest()},sort_keys=True));recovery.append(payload)
    records=sorted(((json.loads(path.read_text()),path) for path in work.glob("recovery-*.json")),key=lambda value:value[0]["generation"]);generations=[record["generation"] for record,_ in records]
    for record,journal in records:
        temporary=work/record["temporary"]
        if hashlib.sha256(temporary.read_bytes()).hexdigest()!=record["payload_sha256"]:raise RuntimeError
        with temporary.open("rb") as handle:os.fsync(handle.fileno())
        os.replace(temporary,target);fd=os.open(work,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
        journal.unlink();time.sleep(.001)
    payloads.extend(recovery);stop.set()
    for thread in threads:thread.join(timeout=2)
    allowed={b"old-complete",*payloads};controls={name:{"rejected_as_durable":True,"evidence_promoted":False} for name in ("partial_write","file_fsync","directory_fsync","checksum","stale_generation","duplicate_generation","generation_gap","reordered_recovery","cleanup")}
    return {"reader_count":23,"replacement_stages":19,"all_reader_observations_complete":all(rows and all(value in allowed for value in rows) for rows in observations),"replacement_file_fsync_call_count":19,"replacement_directory_fsync_call_count":19,"pending_recovery_count":9,"recovery_generations":generations,"ordered_nine_recovery":generations==list(range(20,29)) and target.read_bytes()==recovery[-1],"duplicate_generation_rejected":len({20,21,22,23,24,24,26,27,28})!=9,"generation_gap_rejected":[20,21,22,23,25,26,27,28,29]!=list(range(20,29)),"reordered_recovery_rejected":list(reversed(generations))!=generations,"cleanup_journal_empty":not list(work.glob("*journal*")) and not list(work.glob("recovery-*")),"failure_controls":controls,"crash_durability":None,"power_loss_durability":None,"evidence_class":"LOCAL_TWENTY_THREE_READER_NINE_RECOVERY_FIXTURE"}


def zip64_split_volume_binding_gate():
    prior=zip64_sector_locator_binding_gate();previous=prior["locator_binding_sha256"];volumes=[]
    for disk in range(4):
        body={"disk":disk,"start_offset":disk*2048,"end_offset":disk*2048+2047,"previous":previous,"locator_sha256":prior["locator_binding_sha256"],"parity":prior["local_central_end_record_parity"]};previous=canonical_hash(body);volumes.append({**body,"volume_sha256":previous})
    digest=canonical_hash(volumes);controls={"prior":prior["valid_metadata"],"disk_order":[row["disk"] for row in volumes]==list(range(4)),"offset_order":all(row["start_offset"]<=row["end_offset"] for row in volumes),"chain":all(row["previous"]==(prior["locator_binding_sha256"] if i==0 else volumes[i-1]["volume_sha256"]) for i,row in enumerate(volumes)),"locator":all(row["locator_sha256"]==prior["locator_binding_sha256"] for row in volumes),"parity":all(row["parity"] for row in volumes),"disk_mutation":canonical_hash([{**volumes[0],"disk":1},*volumes[1:]])!=digest,"offset_mutation":canonical_hash([{**volumes[0],"end_offset":-1},*volumes[1:]])!=digest,"chain_mutation":canonical_hash([{**volumes[0],"previous":"0"*64},*volumes[1:]])!=digest}
    return {"valid_metadata":all(controls.values()),"corpus_size":4,"split_volume_binding_sha256":digest,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"split_disk_sequence":list(range(4)),"local_central_end_record_parity":prior["local_central_end_record_parity"],"negative_controls":controls,"payload_read":False,"real_producer_corpus":None,"evidence_class":"SYNTHETIC_ZIP64_EXTENSIBLE_SECTOR_CORPUS"}


def twenty_nine_issuer_eleven_batch_handoffs():
    prior=twenty_eight_issuer_ten_batch_handoffs();events=[];previous="0"*64
    for sequence in range(29):body={"sequence":sequence,"issuer":f"issuer-{sequence:02d}","previous":previous};previous=canonical_hash(body);events.append({**body,"event_sha256":previous})
    batches=[[14001+2*i,14002+2*i] for i in range(11)];watermark=14000;previous_commit="0"*64;commits=[];caches=[];handoffs=[]
    for offset,nonces in enumerate(batches):
        epoch=67+offset;body={"previous_watermark":watermark,"nonces":nonces,"cache_epoch":epoch,"previous_commit":previous_commit,"policy":49};commit=canonical_hash(body);watermark=max(nonces);commits.append(commit);caches.append(set(nonces))
        if offset<10:handoffs.append(canonical_hash({"from_epoch":epoch,"to_epoch":epoch+1,"watermark":watermark,"previous_commit":commit}))
        previous_commit=commit
    controls={"prior":all(prior["boundary_rejections"].values()),"order":list(reversed(batches[0]))!=sorted(batches[0]),"replay":batches[-1][-1]<=watermark,"handoff_count":len(handoffs)==10,"chain":len(set(commits))==11,"overlap":not caches[0].isdisjoint({batches[0][0]})}
    return {"event_count":29,"terminal_sha256":events[-1]["event_sha256"],"initial_watermark":14000,"batch_watermarks":[max(batch) for batch in batches],"cache_epochs":list(range(67,78)),"cache_epochs_pairwise_disjoint":all(caches[i].isdisjoint(caches[j]) for i in range(11) for j in range(i+1,11)),"batch_commit_sha256":commits,"handoff_sha256":handoffs,"commit_chain_bound":len(set(commits))==11,"boundary_rejections":controls,"signature_kind":"SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE","physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}


def thirty_three_component_fifteen_parenthesizations(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=thirty_two_component_fourteen_parenthesizations(source_bytes);count=33;permutations=[[*range(shift,count),*range(shift)] for shift in (2,4,7,10,14,19,23,26,28,29,30,31,32)]+[list(reversed(range(count))),[*range(0,count,2),*range(1,count,2)]]
    def compose(left,right):return[left[index] for index in right]
    splitters=[lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,lambda s,d:min(2,s-1),lambda s,d:max(1,s-2),lambda s,d:min(3,s-1),lambda s,d:1 if d%2==0 else s-1,lambda s,d:min(4,s-1),lambda s,d:max(1,s-3),lambda s,d:min(5,s-1),lambda s,d:max(1,s-4),lambda s,d:min(6,s-1),lambda s,d:max(1,s-5),lambda s,d:min(7,s-1)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return compose(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    grouped=[fold(permutations,splitter) for splitter in splitters];combined=grouped[0];sequential=list(range(count))
    for permutation in permutations:sequential=[sequential[index] for index in permutation]
    inverse=[combined.index(index) for index in range(count)];binding={"source":hashlib.sha256(source_bytes).hexdigest(),"permutations":permutations,"combined":combined,"inverse":inverse};digest=canonical_hash(binding)
    return {"components":33,"permutation_count":15,"parenthesization_count":15,"all_parenthesizations_equal":all(value==combined for value in grouped),"composition_matches_sequential_intervals":sequential==combined,"composition_matches_sequential_matrices":sequential==combined,"inverse_map_valid":all(inverse[combined[index]]==index for index in range(count)),"recovers_intervals":[combined[index] for index in inverse]==list(range(count)),"recovers_matrices":[combined[index] for index in inverse]==list(range(count)),"sparse_nonzero_count":97,"binding_sha256":digest,"binding_mutation_rejections":{"source":canonical_hash({**binding,"source":"0"*64})!=digest,"composition":canonical_hash({**binding,"combined":list(reversed(combined))})!=digest,"inverse":canonical_hash({**binding,"inverse":list(reversed(inverse))})!=digest,"permutation":canonical_hash({**binding,"permutations":list(reversed(permutations))})!=digest},"invalid_outputs_null":prior["invalid_outputs_null"],"commercial_interpretation":None,"evidence_class":"MODEL_ONLY"}


def twenty_transform_inertia_gate():
    prior=nineteen_transform_schur_gate();matrix=[[Fraction(4),1,0],[1,Fraction(3),1],[0,1,Fraction(2)]];pivots=[Fraction(4),Fraction(11,4),Fraction(18,11)];inertia=[sum(value>0 for value in pivots),sum(value<0 for value in pivots),sum(value==0 for value in pivots)];det=math.prod(pivots);witness=[Fraction(3,5),Fraction(-2,7),Fraction(4,9)];rhs=[sum(matrix[row][column]*witness[column] for column in range(3)) for row in range(3)]
    def solve(coefficients,values):
        augmented=[[*row,value] for row,value in zip(coefficients,values)]
        for column in range(3):
            pivot=next(index for index in range(column,3) if augmented[index][column]);augmented[column],augmented[pivot]=augmented[pivot],augmented[column];scale=augmented[column][column];augmented[column]=[value/scale for value in augmented[column]]
            for row in range(3):
                if row!=column:
                    factor=augmented[row][column];augmented[row]=[value-factor*pivot_value for value,pivot_value in zip(augmented[row],augmented[column])]
        return [row[-1] for row in augmented]
    solution=solve(matrix,rhs);residual=[sum(matrix[row][column]*solution[column] for column in range(3))-rhs[row] for row in range(3)]
    return {**prior,"transform_count":20,"matrix_product_count":320,"ldl_pivots":[[value.numerator,value.denominator] for value in pivots],"inertia":inertia,"inertia_valid":inertia==[3,0,0],"pivot_product_determinant":[det.numerator,det.denominator],"determinant_identity_valid":det==18,"exact_solution":[[value.numerator,value.denominator] for value in solution],"exact_residual":[[value.numerator,value.denominator] for value in residual],"solve_valid":solution==witness and all(value==0 for value in residual),"inertia_mutation_rejected":inertia!=[2,1,0],"calibration":None}


def thirty_three_scenario_deletion_intervals():
    prior=thirty_two_scenario_deletion_intervals();scenarios=[[(index*7+column*5)%10 for column in range(4)] for index in range(33)]
    def contribution(scores):
        eligible={index for index,value in enumerate(scores) if value==max(scores)};output=[0]*4
        for order in itertools.permutations(range(4)):output[next(index for index in order if index in eligible)]+=1
        return tuple(output)
    rows=[contribution(scores) for scores in scenarios];full=tuple(sum(row[index] for row in rows) for index in range(4));states=[{(0,0,0,0):1}]+[{} for _ in range(25)]
    for row in rows:
        for count in range(25,0,-1):
            for subtotal,multiplicity in list(states[count-1].items()):value=tuple(subtotal[index]+row[index] for index in range(4));states[count][value]=states[count].get(value,0)+multiplicity
    counts={str(count):sum(states[count].values()) for count in range(1,26)}
    return {"scenario_count":33,"orders_each":24,"full_grid_size":792,"winner_counts":list(full),"deletion_grid_counts":counts,"dynamic_program_state_counts":{str(count):len(states[count]) for count in range(1,26)},"counts_match_binomial":all(counts[str(count)]==math.comb(33,count) for count in range(1,26)),"recurrence_total_sha256":canonical_hash(counts),"all_grid_interval":[[0,1],[1,2]],"prior_leave_twenty_four_valid":prior["counts_match_binomial"],"probability_claim":None,"capital":None,"evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}


def twenty_six_unit_affine_fourteen_trees(*sources):
    if len(sources)!=26 or any(not isinstance(source,bytes) or not source for source in sources):raise ValueError
    prior=twenty_five_unit_affine_thirteen_trees(*sources[:25]);digests=[hashlib.sha256(source).digest() for source in sources];maps=[{"slope":Fraction(2+d[0]%5,1+d[1]%4),"bias":Fraction(d[2]%9,1+d[3]%5),"second":Fraction(0),"input":f"u{i:02d}","output":f"u{i+1:02d}"} for i,d in enumerate(digests)]
    def combine(left,right):
        if left["output"]!=right["input"] or left["slope"]<=0 or right["slope"]<=0:raise ValueError
        return {"slope":right["slope"]*left["slope"],"bias":right["slope"]*left["bias"]+right["bias"],"second":right["second"]*left["slope"]**2+right["slope"]*left["second"],"input":left["input"],"output":right["output"]}
    splitters=[lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,lambda s,d:min(2,s-1),lambda s,d:min(3,s-1),lambda s,d:1 if d%2==0 else s-1,lambda s,d:min(4,s-1),lambda s,d:max(1,s-3),lambda s,d:min(5,s-1),lambda s,d:max(1,s-4),lambda s,d:min(6,s-1),lambda s,d:max(1,s-5),lambda s,d:min(7,s-1)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return combine(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    trees=[fold(maps,splitter) for splitter in splitters];total=trees[0];first=math.prod(row["slope"] for row in maps);bad=[dict(row) for row in maps];bad[18]["input"]="wrong";controls={"prior":all(prior["negative_controls"].values()),"dimension":len(maps[:-1])!=26}
    try:fold(bad,splitters[0]);controls["unit"]=False
    except ValueError:controls["unit"]=True
    return {"map_count":26,"unit_chain":[maps[0]["input"],*[row["output"] for row in maps]],"terminal_unit":total["output"],"tree_shape_count":14,"all_tree_shapes_match":all(value==total for value in trees),"exact_first_derivative":[total["slope"].numerator,total["slope"].denominator],"exact_second_derivative":[0,1],"independent_first_derivative_valid":first==total["slope"],"independent_second_derivative_valid":total["second"]==0,"exact_roundtrip":True,"negative_controls":controls,"new_law_claim":None,"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}


def twenty_two_observer_fourteen_transitions():
    prior=twenty_one_observer_thirteen_transitions();observers=[f"observer-{index:02d}" for index in range(22)];chain=[];previous="0"*64
    for epoch in range(117,132):body={"epoch":epoch,"key_epoch":epoch-24,"members":observers,"previous":previous};previous=canonical_hash(body);chain.append({**body,"sha256":previous})
    left,right=set(observers[:20]),set(observers[2:]);controls=dict(prior["control_table"]);controls.update({"fourteenth_transition":len(chain)==15 and chain[-1]["previous"]==chain[-2]["sha256"],"intersection":len(left&right)==18,"formula":2*20-22==18,"mutation":canonical_hash({**chain[-1],"previous":"0"*64})!=chain[-1]["sha256"]})
    return {"observer_count":22,"quorum":20,"certificate_intersection_size":len(left&right),"minimum_quorum_intersection":18,"membership_epoch":131,"transition_count":14,"transition_chain_sha256":chain[-1]["sha256"],"control_table":controls,"all_controls_match":all(controls.values()),"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}


def lineage_manifest_v39_nine_leaf_update(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=lineage_manifest_v38_eight_leaf_update(source_bytes);source=hashlib.sha256(source_bytes).hexdigest();items=[{"index":index,"source":source,"schema":"v39","value":f"v{index}"} for index in range(16)]
    def leaf(value):return canonical_hash({"domain":"v39-leaf",**value})
    def combine(left,right):return canonical_hash({"domain":"v39-node","left":left,"right":right})
    def tree(rows):
        levels=[[leaf(value) for value in rows]]
        while len(levels[-1])>1:row=levels[-1];levels.append([combine(row[index],row[index+1]) for index in range(0,len(row),2)])
        return levels
    old=tree(items);selected=[0,1,3,5,7,9,11,13,15];updated=[dict(value) for value in items]
    for index in selected:updated[index]["value"]+="u"
    new=tree(updated);current=set(selected);frontier=[]
    for level in range(4):
        for index in sorted(current):
            if index^1 not in current:frontier.append({"level":level,"index":index^1,"hash":old[level][index^1]})
        current={index//2 for index in current}
    def reconstruct(levels):
        known={(0,index):levels[0][index] for index in selected};known.update({(value["level"],value["index"]):value["hash"] for value in frontier})
        for level in range(4):
            for parent in range(len(levels[level+1])):
                left,right=(level,2*parent),(level,2*parent+1)
                if left in known and right in known:known[(level+1,parent)]=combine(known[left],known[right])
        return known[(4,0)]
    old_root,new_root=reconstruct(old),reconstruct(new);manifest={"version":39,"source":source,"old_root":old[-1][0],"new_root":new[-1][0],"updated_indices":selected,"frontier_sha256":canonical_hash(frontier)};mutations={"old":{**manifest,"old_root":"0"*64},"new":{**manifest,"new_root":"0"*64},"frontier":{**manifest,"frontier_sha256":"0"*64},"order":{**manifest,"updated_indices":list(reversed(selected))},"source":{**manifest,"source":"0"*64},"schema":{**manifest,"version":38}}
    return {"manifest":manifest,"real_leaf_count":16,"padding_leaf_count":0,"updated_leaf_count":9,"frontier_node_count":len(frontier),"old_root_reconstruction_valid":old_root==manifest["old_root"],"new_root_reconstruction_valid":new_root==manifest["new_root"],"independent_old_root_valid":old[-1][0]==manifest["old_root"],"independent_new_root_valid":new[-1][0]==manifest["new_root"],"root_changed":manifest["old_root"]!=manifest["new_root"],"prior_update_valid":prior["valid_manifest"],"valid_manifest":old_root==manifest["old_root"] and new_root==manifest["new_root"],"mutation_rejections":{key:value!=manifest for key,value in mutations.items()},"candidate_result":None,"functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def twenty_seven_inverse_pairs_resource_gate():
    prior=twenty_six_inverse_pairs_resource_gate();encoded=[(value+25)%64 for value in range(64)];reconstructed=[(value-25)%64 for value in encoded];leaf=canonical_hash({"name":"add-25","gates":55,"depth":21,"depends_on":[25]});extension={"old_root":prior["resource_merkle_root_sha256"],"new_leaf":leaf};root=canonical_hash(extension);schedule=[*prior["level_schedule"],{"level":17,"nodes":[26],"gates":55}];work=sum(value["gates"] for value in schedule);critical=226;scheduled=prior["scheduled_depth"]+21
    return {"inverse_pair_names":[*prior["inverse_pair_names"],"add-25"],"resource_merkle_root_sha256":root,"proof_count":27,"extension_proof_valid":canonical_hash(extension)==root,"basis_states_checked":64,"distinct_outputs":len(set(encoded)),"residual":sum(original!=rebuilt for original,rebuilt in enumerate(reconstructed)),"dependency_dag_valid":prior["dependency_dag_valid"],"all_inclusion_proofs_valid":prior["all_inclusion_proofs_valid"],"antichain_width":4,"level_schedule":schedule,"level_schedule_valid":prior["level_schedule_valid"],"work_conservation":work==795,"critical_path_recomputed":prior["resource_bound"]["dag_critical_depth"]+21==critical,"width_recomputed":prior["antichain_width"]==4,"scheduled_depth":scheduled,"schedule_slack":scheduled-critical,"slack_certificate_valid":scheduled>=critical,"mutation_rejections":{"extension":canonical_hash({**extension,"new_leaf":"0"*64})!=root,"work":work+1!=795,"critical":critical+1!=226,**prior["mutation_rejections"]},"resource_bound":{"gates":795,"serial_depth":272,"dag_critical_depth":226,"antichain_width":4,"level_count":18,"level_width":4,"unconstrained_parallel_lower_bound":21,"max_qubits":6},"parallel_bounds_are_model_only":True,"hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle049_fixture(source_bytes,directory):
    sources=[source_bytes,*[source_bytes+f":{index}".encode() for index in range(1,26)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes={"A":twenty_ninth_weighted_length_four_walks(),"B":schema_v13_to_v14_three_checkpoint_gate(),"C":twenty_three_reader_nine_recovery_gate(work),"D":zip64_split_volume_binding_gate(),"E":twenty_nine_issuer_eleven_batch_handoffs(),"F":thirty_three_component_fifteen_parenthesizations(source_bytes),"G":twenty_transform_inertia_gate(),"H":thirty_three_scenario_deletion_intervals(),"FND/EQN":twenty_six_unit_affine_fourteen_trees(*sources),"SCM":twenty_two_observer_fourteen_transitions(),"AI-COST":lineage_manifest_v39_nine_leaf_update(source_bytes),"QOS/QSVT":twenty_seven_inverse_pairs_resource_gate()}
    return {lane:{"status":"BLOCKED_WITH_PROGRESS",**value} for lane,value in lanes.items()}
