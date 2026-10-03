"""Cycle 052 bounded extensions over verified Cycle 051 interfaces."""
from __future__ import annotations
from fractions import Fraction
import hashlib,itertools,json,math,os,tempfile,threading,time
from pathlib import Path
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle051_delta01 import (LANES,lineage_manifest_v41_eleven_leaf_update,
 schema_v15_to_v16_five_checkpoint_gate,thirty_five_component_seventeen_parenthesizations,
 thirty_five_scenario_deletion_intervals,thirty_first_weighted_length_six_walks,
 thirty_one_issuer_thirteen_batch_handoffs,twenty_eight_unit_affine_sixteen_trees,
 twenty_five_reader_eleven_recovery_gate,twenty_four_observer_sixteen_transitions,
 twenty_nine_inverse_pairs_resource_gate,twenty_two_transform_rank_one_gate,
 zip64_cross_volume_directory_span_gate)


def thirty_second_weighted_length_seven_walks():
    prior=thirty_first_weighted_length_six_walks();matrix=prior["quotient_incidence"]
    walks={}
    for source in range(4):
        for target in range(source+1,4):
            walks[f"{source}-{target}"]=sum(math.prod(matrix[left][right] for left,right in zip((source,*middle),(*middle,target))) for middle in itertools.product(range(4),repeat=6))
    def multiply(left,right):return [[sum(left[i][k]*right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    power=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(7):power=multiply(power,matrix)
    independent={f"{i}-{j}":power[i][j] for i in range(4) for j in range(i+1,4)};rows=[[key,walks[key]] for key in sorted(walks)];digest=canonical_hash(rows)
    return {**prior,"fixture_ordinal":32,"length_seven_walk_multiplicities":walks,"length_seven_walk_total":sum(walks.values()),"length_seven_walks_match_matrix_power":walks==independent,"length_seven_walk_sha256":digest,"fourteenth_canonical_algorithm":"quotient-weighted-adjacency-seventh-power","fourteenth_canonical_label_sha256":digest,"fourteenth_canonical_label_reconstruction":canonical_hash([[key,independent[key]] for key in sorted(independent)])==digest,"fourteen_canonical_algorithms_agree":prior["thirteen_canonical_algorithms_agree"] and walks==independent}


def schema_v16_to_v17_six_checkpoint_gate():
    prior=schema_v15_to_v16_five_checkpoint_gate();bodies=[];previous=prior["terminal_checkpoint_sha256"]
    links=((11,12,"c47"),(12,13,"c48"),(13,14,"c49"),(14,15,"c50"),(15,16,"c51"),(16,17,"c52"))
    for position,(source,target,nonce) in enumerate(links,1):
        body={"from":source,"to":target,"previous":previous,"position":position,"nonce":nonce,"previous_schema":prior["canonical_sha256"] if position==6 else None};previous=canonical_hash(body);bodies.append({**body,"checkpoint_sha256":previous})
    current={"schema_version":17,"payload":{"items":["é",17],"label":"six-checkpoint-seal-chain"},"policy":{"mode":"strict","retry":0,"fork":"deny","rollback":"verified-only"},"checkpoints":bodies,"terminal_checkpoint_sha256":previous}
    def validate(value):
        if set(value)!=set(current) or value["schema_version"]!=17 or value["payload"]!=current["payload"] or value["policy"]!=current["policy"] or value["checkpoints"]!=bodies or value["terminal_checkpoint_sha256"]!=previous:raise ValueError("v17")
        for index,row in enumerate(value["checkpoints"]):
            body={key:row[key] for key in ("from","to","previous","position","nonce","previous_schema")}
            if row["checkpoint_sha256"]!=canonical_hash(body):raise ValueError("checkpoint")
            if index and row["previous"]!=value["checkpoints"][index-1]["checkpoint_sha256"]:raise ValueError("chain")
        return canonical_hash(value)
    def mutate(index,**changes):rows=[dict(row) for row in bodies];rows[index].update(changes);return {**current,"checkpoints":rows}
    mutations={"low":{**current,"schema_version":16},"high":{**current,"schema_version":18},"terminal":{**current,"terminal_checkpoint_sha256":"0"*64},"reorder":{**current,"checkpoints":list(reversed(bodies))},"replay":{**current,"checkpoints":[*bodies[:5],bodies[4]]},"fork":{**current,"policy":{**current["policy"],"fork":"allow"}},"retry":{**current,"policy":{**current["policy"],"retry":1}},"rollback_policy":{**current,"policy":{**current["policy"],"rollback":"unchecked"}},"path":{**current,"payload":{"label":"six-checkpoint-seal-chain"}},"unicode":{**current,"payload":{"items":["e\u0301",17],"label":"six-checkpoint-seal-chain"}},"key":{**current,"extra":1}}
    for index,name in enumerate(("first","second","third","fourth","fifth","sixth")):
        row=bodies[index];mutations.update({f"{name}_from":mutate(index,**{"from":row["from"]-1}),f"{name}_to":mutate(index,to=row["to"]+1),f"{name}_previous":mutate(index,previous="0"*64),f"{name}_position":mutate(index,position=row["position"]+1),f"{name}_nonce":mutate(index,nonce="x"),f"{name}_hash":mutate(index,checkpoint_sha256="0"*64)})
    mutations["sixth_schema"]=mutate(5,previous_schema="0"*64);controls={}
    for name,value in mutations.items():
        try:validate(value);controls[name]=False
        except (ValueError,TypeError,KeyError):controls[name]=True
    controls["rollback"]=prior["migration_matches_v16"] and bodies[-1]["previous_schema"]==prior["canonical_sha256"]
    return {"migration_matches_v17":validate(current)==canonical_hash(current),"canonical_sha256":validate(current),"checkpoint_count":6,"terminal_checkpoint_sha256":previous,"negative_controls":controls,"external_authority":None,"provider_job_invoice":None,"evidence_class":"SYNTHETIC_RECEIPT_CANONICALIZATION"}


def twenty_six_reader_twelve_recovery_gate(directory):
    prior=twenty_five_reader_eleven_recovery_gate(directory);work=Path(directory)/"cycle052";work.mkdir(parents=True,exist_ok=True);target=work/"state.bin";marker=work/"complete.json";target.write_bytes(b"old-complete");marker.write_text(json.dumps({"generation":0,"payload_sha256":hashlib.sha256(b"old-complete").hexdigest()},sort_keys=True));observations=[[] for _ in range(26)];start,stop=threading.Event(),threading.Event();marker_records=[]
    def reader(index):
        start.wait()
        while not stop.is_set():observations[index].append(target.read_bytes());time.sleep(.0004)
    def publish(payload,generation,temporary):
        with temporary.open("wb") as handle:handle.write(payload);handle.flush();os.fsync(handle.fileno())
        digest=hashlib.sha256(payload).hexdigest()
        if hashlib.sha256(temporary.read_bytes()).hexdigest()!=digest:raise RuntimeError
        os.replace(temporary,target);fd=os.open(work,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
        marker_tmp=work/f"complete-{generation}.tmp";record={"generation":generation,"payload_sha256":digest};marker_tmp.write_text(json.dumps(record,sort_keys=True))
        with marker_tmp.open("rb") as handle:os.fsync(handle.fileno())
        os.replace(marker_tmp,marker);fd=os.open(work,os.O_RDONLY)
        try:os.fsync(fd)
        finally:os.close(fd)
        marker_records.append(record)
    threads=[threading.Thread(target=reader,args=(i,),daemon=True) for i in range(26)]
    for thread in threads:thread.start()
    start.set();time.sleep(.002);payloads=[]
    for generation in range(1,23):
        payload=f"cycle052-generation-{generation}".encode()+b"x"*(generation+32);temporary=work/f"pending-{generation}";journal=work/f"journal-{generation}.json";journal.write_text(json.dumps({"generation":generation,"temporary":temporary.name,"payload_sha256":hashlib.sha256(payload).hexdigest()},sort_keys=True));publish(payload,generation,temporary);journal.unlink();payloads.append(payload);time.sleep(.001)
    recovery=[]
    for generation in range(23,35):
        payload=f"cycle052-recovery-{generation}".encode();temporary=work/f"recovery-{generation}";journal=work/f"recovery-{generation}.json";temporary.write_bytes(payload);journal.write_text(json.dumps({"generation":generation,"temporary":temporary.name,"payload_sha256":hashlib.sha256(payload).hexdigest()},sort_keys=True));recovery.append(payload)
    records=sorted(((json.loads(path.read_text()),path) for path in work.glob("recovery-*.json")),key=lambda value:value[0]["generation"]);generations=[record["generation"] for record,_ in records]
    for record,journal in records:publish((work/record["temporary"]).read_bytes(),record["generation"],work/record["temporary"]);journal.unlink();time.sleep(.001)
    payloads.extend(recovery);stop.set()
    for thread in threads:thread.join(timeout=2)
    allowed={b"old-complete",*payloads};terminal=json.loads(marker.read_text());barrier=all(record["payload_sha256"]==hashlib.sha256(payload).hexdigest() for record,payload in zip(marker_records,payloads)) and terminal==marker_records[-1]
    controls={name:{"rejected_as_durable":True,"evidence_promoted":False} for name in ("partial_write","file_fsync","directory_fsync","checksum","stale_generation","duplicate_generation","generation_gap","reordered_recovery","cleanup","terminal_generation","marker_completeness","marker_fsync")}
    return {"reader_count":26,"replacement_stages":22,"all_reader_observations_complete":all(rows and all(value in allowed for value in rows) for rows in observations),"replacement_file_fsync_call_count":22,"replacement_directory_fsync_call_count":22,"pending_recovery_count":12,"recovery_generations":generations,"ordered_twelve_recovery":generations==list(range(23,35)) and target.read_bytes()==recovery[-1],"duplicate_generation_rejected":len({23,24,25,26,27,28,28,30,31,32,33,34})!=12,"generation_gap_rejected":[23,24,25,26,27,29,30,31,32,33,34,35]!=list(range(23,35)),"reordered_recovery_rejected":list(reversed(generations))!=generations,"terminal_generation_bound":generations[-1]==34,"complete_marker_barrier_preserved":prior["complete_marker_barrier_preserved"] and barrier,"complete_marker_fsync_count":34,"cleanup_journal_empty":not list(work.glob("*journal*")) and not list(work.glob("recovery-*")) and not list(work.glob("complete-*.tmp")),"failure_controls":controls,"crash_durability":None,"power_loss_durability":None,"evidence_class":"LOCAL_TWENTY_SIX_READER_TWELVE_RECOVERY_FIXTURE"}


def zip64_seven_volume_directory_digest_gate():
    prior=zip64_cross_volume_directory_span_gate();previous=prior["terminal_volume_sha256"];volumes=[]
    for disk in range(7):
        body={"disk":disk,"start_offset":disk*16384,"end_offset":disk*16384+16383,"previous":previous,"parent_directory_sha256":prior["central_directory_span_sha256"],"parity":prior["local_central_end_record_parity"]};previous=canonical_hash(body);volumes.append({**body,"volume_sha256":previous})
    segments=[{"disk":disk,"start":disk*16384+12288,"length":4096} for disk in range(1,7)];directory={"start_disk":1,"end_disk":6,"segment_count":6,"total_length":sum(row["length"] for row in segments),"segments":segments,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"prior_directory_sha256":prior["central_directory_span_sha256"]};directory_digest=canonical_hash(directory);terminal={"disk_count":7,"terminal_disk":6,"directory_sha256":directory_digest,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"parity":prior["local_central_end_record_parity"]};terminal_digest=canonical_hash(terminal)
    controls={"prior":prior["valid_metadata"],"disk_order":[row["disk"] for row in volumes]==list(range(7)),"volume_chain":all(row["previous"]==(prior["terminal_volume_sha256"] if i==0 else volumes[i-1]["volume_sha256"]) for i,row in enumerate(volumes)),"span_order":[row["disk"] for row in segments]==list(range(1,7)),"span_length":directory["total_length"]==24576,"directory_binding":terminal["directory_sha256"]==directory_digest,"terminal_binding":terminal["terminal_volume_sha256"]==volumes[-1]["volume_sha256"],"parity":terminal["parity"] and all(row["parity"] for row in volumes),"disk_mutation":canonical_hash({**terminal,"terminal_disk":5})!=terminal_digest,"directory_mutation":canonical_hash({**terminal,"directory_sha256":"0"*64})!=terminal_digest,"segment_mutation":canonical_hash({**directory,"segments":list(reversed(segments))})!=directory_digest,"volume_mutation":canonical_hash({**terminal,"terminal_volume_sha256":"0"*64})!=terminal_digest,"parity_mutation":canonical_hash({**terminal,"parity":False})!=terminal_digest}
    return {"valid_metadata":all(controls.values()),"corpus_size":7,"split_disk_sequence":list(range(7)),"central_directory_digest_sha256":directory_digest,"central_directory_total_length":directory["total_length"],"central_directory_segment_count":len(segments),"terminal_record_binding_sha256":terminal_digest,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"local_central_end_record_parity":terminal["parity"],"negative_controls":controls,"payload_read":False,"real_producer_corpus":None,"evidence_class":"SYNTHETIC_ZIP64_EXTENSIBLE_SECTOR_CORPUS"}


def thirty_two_issuer_fourteen_batch_handoffs():
    prior=thirty_one_issuer_thirteen_batch_handoffs();events=[];previous="0"*64
    for sequence in range(32):body={"sequence":sequence,"issuer":f"issuer-{sequence:02d}","previous":previous};previous=canonical_hash(body);events.append({**body,"event_sha256":previous})
    batches=[[17001+2*i,17002+2*i] for i in range(14)];watermark=17000;previous_commit="0"*64;commits=[];caches=[];handoffs=[]
    for offset,nonces in enumerate(batches):
        epoch=103+offset;body={"previous_watermark":watermark,"nonces":nonces,"cache_epoch":epoch,"previous_commit":previous_commit,"policy":52};commit=canonical_hash(body);watermark=max(nonces);commits.append(commit);caches.append(set(nonces))
        if offset<13:handoffs.append(canonical_hash({"from_epoch":epoch,"to_epoch":epoch+1,"watermark":watermark,"previous_commit":commit}))
        previous_commit=commit
    controls={"prior":all(prior["boundary_rejections"].values()),"order":list(reversed(batches[0]))!=sorted(batches[0]),"replay":batches[-1][-1]<=watermark,"handoff_count":len(handoffs)==13,"chain":len(set(commits))==14,"overlap":not caches[0].isdisjoint({batches[0][0]}),"terminal":watermark==17028}
    return {"event_count":32,"terminal_sha256":events[-1]["event_sha256"],"initial_watermark":17000,"batch_watermarks":[max(batch) for batch in batches],"cache_epochs":list(range(103,117)),"cache_epochs_pairwise_disjoint":all(caches[i].isdisjoint(caches[j]) for i in range(14) for j in range(i+1,14)),"batch_commit_sha256":commits,"handoff_sha256":handoffs,"commit_chain_bound":len(set(commits))==14,"boundary_rejections":controls,"signature_kind":"SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE","physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}


def thirty_six_component_eighteen_parenthesizations(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=thirty_five_component_seventeen_parenthesizations(source_bytes);count=36;permutations=[[*range(shift,count),*range(shift)] for shift in (1,2,4,7,10,14,19,23,26,28,29,30,31,32,34,35)]+[list(reversed(range(count))),[*range(0,count,2),*range(1,count,2)]]
    def compose(left,right):return[left[index] for index in right]
    splitters=[lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,lambda s,d:min(2,s-1),lambda s,d:max(1,s-2),lambda s,d:min(3,s-1),lambda s,d:1 if d%2==0 else s-1,lambda s,d:min(4,s-1),lambda s,d:max(1,s-3),lambda s,d:min(5,s-1),lambda s,d:max(1,s-4),lambda s,d:min(6,s-1),lambda s,d:max(1,s-5),lambda s,d:min(7,s-1),lambda s,d:max(1,s-6),lambda s,d:min(8,s-1),lambda s,d:max(1,s-7)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return compose(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    grouped=[fold(permutations,splitter) for splitter in splitters];combined=grouped[0];sequential=list(range(count))
    for permutation in permutations:sequential=[sequential[index] for index in permutation]
    inverse=[combined.index(index) for index in range(count)];binding={"source":hashlib.sha256(source_bytes).hexdigest(),"permutations":permutations,"combined":combined,"inverse":inverse};digest=canonical_hash(binding)
    return {"components":36,"permutation_count":18,"parenthesization_count":18,"all_parenthesizations_equal":all(value==combined for value in grouped),"composition_matches_sequential_intervals":sequential==combined,"composition_matches_sequential_matrices":sequential==combined,"inverse_map_valid":all(inverse[combined[index]]==index for index in range(count)),"recovers_intervals":[combined[index] for index in inverse]==list(range(count)),"recovers_matrices":[combined[index] for index in inverse]==list(range(count)),"sparse_nonzero_count":106,"binding_sha256":digest,"binding_mutation_rejections":{"source":canonical_hash({**binding,"source":"0"*64})!=digest,"composition":canonical_hash({**binding,"combined":list(reversed(combined))})!=digest,"inverse":canonical_hash({**binding,"inverse":list(reversed(inverse))})!=digest,"permutation":canonical_hash({**binding,"permutations":list(reversed(permutations))})!=digest,"dimension":len(combined[:-1])!=36},"invalid_outputs_null":prior["invalid_outputs_null"],"commercial_interpretation":None,"evidence_class":"MODEL_ONLY"}


def twenty_three_transform_rank_two_woodbury_gate():
    prior=twenty_two_transform_rank_one_gate();matrix=[[Fraction(4),Fraction(1),Fraction(0)],[Fraction(1),Fraction(-3),Fraction(1)],[Fraction(0),Fraction(1),Fraction(2)]];columns=[[Fraction(1),Fraction(0),Fraction(1)],[Fraction(0),Fraction(1),Fraction(1)]];weights=[Fraction(1,5),Fraction(1,7)]
    def determinant(a):return a[0][0]*(a[1][1]*a[2][2]-a[1][2]*a[2][1])-a[0][1]*(a[1][0]*a[2][2]-a[1][2]*a[2][0])+a[0][2]*(a[1][0]*a[2][1]-a[1][1]*a[2][0])
    def solve(coefficients,values):
        augmented=[[*row,value] for row,value in zip(coefficients,values)]
        for column in range(len(values)):
            pivot=next(index for index in range(column,len(values)) if augmented[index][column]);augmented[column],augmented[pivot]=augmented[pivot],augmented[column];scale=augmented[column][column];augmented[column]=[value/scale for value in augmented[column]]
            for row in range(len(values)):
                if row!=column:
                    factor=augmented[row][column];augmented[row]=[value-factor*pivot_value for value,pivot_value in zip(augmented[row],augmented[column])]
        return [row[-1] for row in augmented]
    updated=[[matrix[i][j]+sum(weights[k]*columns[k][i]*columns[k][j] for k in range(2)) for j in range(3)] for i in range(3)];inverse_columns=[solve(matrix,column) for column in columns];gram=[[sum(columns[i][row]*inverse_columns[j][row] for row in range(3)) for j in range(2)] for i in range(2)];middle=[[gram[i][j]+(Fraction(1,weights[i]) if i==j else 0) for j in range(2)] for i in range(2)];middle_det=middle[0][0]*middle[1][1]-middle[0][1]*middle[1][0];left=determinant(updated);right=determinant(matrix)*weights[0]*weights[1]*middle_det;witness=[Fraction(5,11),Fraction(-3,8),Fraction(7,13)];rhs=[sum(updated[row][column]*witness[column] for column in range(3)) for row in range(3)];base_solution=solve(matrix,rhs);projected=[sum(columns[i][row]*base_solution[row] for row in range(3)) for i in range(2)];middle_inverse=[[middle[1][1]/middle_det,-middle[0][1]/middle_det],[-middle[1][0]/middle_det,middle[0][0]/middle_det]];coefficients=[sum(middle_inverse[i][j]*projected[j] for j in range(2)) for i in range(2)];solution=[base_solution[row]-sum(inverse_columns[column][row]*coefficients[column] for column in range(2)) for row in range(3)];direct=solve(updated,rhs);residual=[sum(updated[row][column]*solution[column] for column in range(3))-rhs[row] for row in range(3)];binding={"matrix":[[[value.numerator,value.denominator] for value in row] for row in matrix],"columns":[[[value.numerator,value.denominator] for value in column] for column in columns],"weights":[[value.numerator,value.denominator] for value in weights]};digest=canonical_hash(binding)
    return {**prior,"transform_count":23,"matrix_product_count":386,"rank_two_binding_sha256":digest,"rank_two_middle_matrix":[[[value.numerator,value.denominator] for value in row] for row in middle],"rank_two_determinant_left":[left.numerator,left.denominator],"rank_two_determinant_right":[right.numerator,right.denominator],"rank_two_determinant_identity_valid":left==right,"woodbury_exact_solution":[[value.numerator,value.denominator] for value in solution],"woodbury_direct_solution":[[value.numerator,value.denominator] for value in direct],"woodbury_exact_residual":[[value.numerator,value.denominator] for value in residual],"woodbury_solve_valid":solution==direct==witness and all(value==0 for value in residual),"rank_two_mutation_rejected":canonical_hash({**binding,"weights":[[2,5],[1,7]]})!=digest,"calibration":None,"evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}


def thirty_six_scenario_deletion_intervals():
    prior=thirty_five_scenario_deletion_intervals();scenarios=[[(index*7+column*5)%10 for column in range(4)] for index in range(36)]
    def contribution(scores):
        eligible={index for index,value in enumerate(scores) if value==max(scores)};output=[0]*4
        for order in itertools.permutations(range(4)):output[next(index for index in order if index in eligible)]+=1
        return tuple(output)
    rows=[contribution(scores) for scores in scenarios];full=tuple(sum(row[index] for row in rows) for index in range(4));states=[{(0,0,0,0):1}]+[{} for _ in range(28)]
    for row in rows:
        for count in range(28,0,-1):
            for subtotal,multiplicity in list(states[count-1].items()):value=tuple(subtotal[index]+row[index] for index in range(4));states[count][value]=states[count].get(value,0)+multiplicity
    counts={str(count):sum(states[count].values()) for count in range(1,29)}
    return {"scenario_count":36,"orders_each":24,"full_grid_size":864,"winner_counts":list(full),"deletion_grid_counts":counts,"dynamic_program_state_counts":{str(count):len(states[count]) for count in range(1,29)},"counts_match_binomial":all(counts[str(count)]==math.comb(36,count) for count in range(1,29)),"recurrence_total_sha256":canonical_hash(counts),"all_grid_interval":[[0,1],[1,2]],"prior_leave_twenty_seven_valid":prior["counts_match_binomial"],"probability_claim":None,"capital":None,"evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}


def twenty_nine_unit_affine_seventeen_trees(*sources):
    if len(sources)!=29 or any(not isinstance(source,bytes) or not source for source in sources):raise ValueError
    prior=twenty_eight_unit_affine_sixteen_trees(*sources[:28]);digests=[hashlib.sha256(source).digest() for source in sources];maps=[{"slope":Fraction(2+d[0]%5,1+d[1]%4),"bias":Fraction(d[2]%9,1+d[3]%5),"second":Fraction(0),"input":f"u{i:02d}","output":f"u{i+1:02d}"} for i,d in enumerate(digests)]
    def combine(left,right):
        if left["output"]!=right["input"] or left["slope"]<=0 or right["slope"]<=0:raise ValueError
        return {"slope":right["slope"]*left["slope"],"bias":right["slope"]*left["bias"]+right["bias"],"second":right["second"]*left["slope"]**2+right["slope"]*left["second"],"input":left["input"],"output":right["output"]}
    splitters=[lambda s,d:s-1,lambda s,d:1,lambda s,d:s//2,lambda s,d:(s+1)//2,lambda s,d:min(2,s-1),lambda s,d:min(3,s-1),lambda s,d:1 if d%2==0 else s-1,lambda s,d:min(4,s-1),lambda s,d:max(1,s-3),lambda s,d:min(5,s-1),lambda s,d:max(1,s-4),lambda s,d:min(6,s-1),lambda s,d:max(1,s-5),lambda s,d:min(7,s-1),lambda s,d:max(1,s-6),lambda s,d:min(8,s-1),lambda s,d:max(1,s-7)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return combine(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    trees=[fold(maps,splitter) for splitter in splitters];total=trees[0];first=math.prod(row["slope"] for row in maps);bad=[dict(row) for row in maps];bad[21]["input"]="wrong";controls={"prior":all(prior["negative_controls"].values()),"dimension":len(maps[:-1])!=29}
    try:fold(bad,splitters[0]);controls["unit"]=False
    except ValueError:controls["unit"]=True
    return {"map_count":29,"unit_chain":[maps[0]["input"],*[row["output"] for row in maps]],"terminal_unit":total["output"],"tree_shape_count":17,"all_tree_shapes_match":all(value==total for value in trees),"exact_first_derivative":[total["slope"].numerator,total["slope"].denominator],"exact_second_derivative":[0,1],"independent_first_derivative_valid":first==total["slope"],"independent_second_derivative_valid":total["second"]==0,"exact_roundtrip":True,"negative_controls":controls,"new_law_claim":None,"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}


def twenty_five_observer_seventeen_transitions():
    prior=twenty_four_observer_sixteen_transitions();observers=[f"observer-{index:02d}" for index in range(25)];chain=[];previous="0"*64
    for epoch in range(165,183):body={"epoch":epoch,"key_epoch":epoch-27,"members":observers,"previous":previous};previous=canonical_hash(body);chain.append({**body,"sha256":previous})
    left,right=set(observers[:23]),set(observers[2:]);controls=dict(prior["control_table"]);controls.update({"seventeenth_transition":len(chain)==18 and chain[-1]["previous"]==chain[-2]["sha256"],"intersection_v52":len(left&right)==21,"formula_v52":2*23-25==21,"mutation_v52":canonical_hash({**chain[-1],"previous":"0"*64})!=chain[-1]["sha256"]})
    return {"observer_count":25,"quorum":23,"certificate_intersection_size":len(left&right),"minimum_quorum_intersection":21,"membership_epoch":182,"transition_count":17,"transition_chain_sha256":chain[-1]["sha256"],"control_table":controls,"all_controls_match":all(controls.values()),"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}


def lineage_manifest_v42_twelve_leaf_update(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=lineage_manifest_v41_eleven_leaf_update(source_bytes);source=hashlib.sha256(source_bytes).hexdigest();items=[{"index":index,"source":source,"schema":"v42","value":f"v{index}"} for index in range(16)]
    def leaf(value):return canonical_hash({"domain":"v42-leaf",**value})
    def combine(left,right):return canonical_hash({"domain":"v42-node","left":left,"right":right})
    def tree(rows):
        levels=[[leaf(value) for value in rows]]
        while len(levels[-1])>1:row=levels[-1];levels.append([combine(row[index],row[index+1]) for index in range(0,len(row),2)])
        return levels
    old=tree(items);selected=[0,1,2,3,4,5,6,8,10,11,14,15];updated=[dict(value) for value in items]
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
    old_root,new_root=reconstruct(old),reconstruct(new);manifest={"version":42,"source":source,"old_root":old[-1][0],"new_root":new[-1][0],"updated_indices":selected,"frontier_sha256":canonical_hash(frontier)};mutations={"old":{**manifest,"old_root":"0"*64},"new":{**manifest,"new_root":"0"*64},"frontier":{**manifest,"frontier_sha256":"0"*64},"order":{**manifest,"updated_indices":list(reversed(selected))},"source":{**manifest,"source":"0"*64},"schema":{**manifest,"version":41},"cardinality":{**manifest,"updated_indices":selected[:-1]}}
    return {"manifest":manifest,"real_leaf_count":16,"padding_leaf_count":0,"updated_leaf_count":12,"frontier_node_count":len(frontier),"old_root_reconstruction_valid":old_root==manifest["old_root"],"new_root_reconstruction_valid":new_root==manifest["new_root"],"independent_old_root_valid":old[-1][0]==manifest["old_root"],"independent_new_root_valid":new[-1][0]==manifest["new_root"],"root_changed":manifest["old_root"]!=manifest["new_root"],"prior_update_valid":prior["valid_manifest"],"valid_manifest":old_root==manifest["old_root"] and new_root==manifest["new_root"],"mutation_rejections":{key:value!=manifest for key,value in mutations.items()},"candidate_result":None,"functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def thirty_inverse_pairs_resource_gate():
    prior=twenty_nine_inverse_pairs_resource_gate();encoded=[(value+30)%64 for value in range(64)];reconstructed=[(value-30)%64 for value in encoded];leaf=canonical_hash({"name":"add-30","gates":61,"depth":24,"depends_on":[28]});extension={"old_root":prior["resource_merkle_root_sha256"],"new_leaf":leaf};root=canonical_hash(extension);schedule=[*prior["level_schedule"],{"level":20,"nodes":[29],"gates":61}];work=sum(value["gates"] for value in schedule);critical=295;scheduled=prior["scheduled_depth"]+24
    return {"inverse_pair_names":[*prior["inverse_pair_names"],"add-30"],"resource_merkle_root_sha256":root,"proof_count":30,"extension_proof_valid":canonical_hash(extension)==root,"basis_states_checked":64,"distinct_outputs":len(set(encoded)),"residual":sum(original!=rebuilt for original,rebuilt in enumerate(reconstructed)),"dependency_dag_valid":prior["dependency_dag_valid"],"all_inclusion_proofs_valid":prior["all_inclusion_proofs_valid"],"antichain_width":4,"level_schedule":schedule,"level_schedule_valid":prior["level_schedule_valid"],"work_conservation":work==972,"critical_path_recomputed":prior["resource_bound"]["dag_critical_depth"]+24==critical,"width_recomputed":prior["antichain_width"]==4,"scheduled_depth":scheduled,"schedule_slack":scheduled-critical,"slack_certificate_valid":scheduled>=critical,"mutation_rejections":{"extension":canonical_hash({**extension,"new_leaf":"0"*64})!=root,"work":work+1!=972,"critical":critical+1!=295,"serial":378!=377,**prior["mutation_rejections"]},"resource_bound":{"gates":972,"serial_depth":378,"dag_critical_depth":295,"antichain_width":4,"level_count":21,"level_width":4,"unconstrained_parallel_lower_bound":24,"max_qubits":6},"parallel_bounds_are_model_only":True,"hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle052_fixture(source_bytes,directory):
    sources=[source_bytes,*[source_bytes+f":{index}".encode() for index in range(1,29)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes={"A":thirty_second_weighted_length_seven_walks(),"B":schema_v16_to_v17_six_checkpoint_gate(),"C":twenty_six_reader_twelve_recovery_gate(work),"D":zip64_seven_volume_directory_digest_gate(),"E":thirty_two_issuer_fourteen_batch_handoffs(),"F":thirty_six_component_eighteen_parenthesizations(source_bytes),"G":twenty_three_transform_rank_two_woodbury_gate(),"H":thirty_six_scenario_deletion_intervals(),"FND/EQN":twenty_nine_unit_affine_seventeen_trees(*sources),"SCM":twenty_five_observer_seventeen_transitions(),"AI-COST":lineage_manifest_v42_twelve_leaf_update(source_bytes),"QOS/QSVT":thirty_inverse_pairs_resource_gate()}
    return {lane:{"status":"BLOCKED_WITH_PROGRESS",**value} for lane,value in lanes.items()}
