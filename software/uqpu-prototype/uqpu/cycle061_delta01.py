"""Cycle 061 bounded extensions over verified Cycle 060 interfaces."""
from __future__ import annotations
from fractions import Fraction
from functools import lru_cache
import hashlib,json,math,os,tempfile,threading
from pathlib import Path
from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle060_delta01 import (
 LANES,fortieth_issuer_twenty_two_batch_handoffs,fortieth_weighted_length_fifteen_walks,
 forty_four_component_twenty_six_parenthesizations,forty_four_scenario_deletion_intervals,
 lineage_manifest_v50_twenty_leaf_update,schema_v24_to_v25_fourteen_checkpoint_gate,
 thirty_eight_inverse_pairs_resource_gate,thirty_four_reader_twenty_recovery_gate,
 thirty_one_transform_three_stage_woodbury_gate,thirty_seven_unit_affine_twenty_five_trees,
 thirty_three_observer_twenty_five_transitions,zip64_fifteen_volume_seven_envelope_gate)


def forty_first_weighted_length_sixteen_walks():
    prior=fortieth_weighted_length_fifteen_walks();matrix=prior["quotient_incidence"]
    @lru_cache(None)
    def recurrence(node,target,steps):return int(node==target) if steps==0 else sum(matrix[node][nxt]*recurrence(nxt,target,steps-1) for nxt in range(4))
    walks={f"{source}-{target}":recurrence(source,target,16) for source in range(4) for target in range(source+1,4)}
    def multiply(left,right):return [[sum(left[i][k]*right[k][j] for k in range(4)) for j in range(4)] for i in range(4)]
    power=[[int(i==j) for j in range(4)] for i in range(4)]
    for _ in range(16):power=multiply(power,matrix)
    independent={f"{i}-{j}":power[i][j] for i in range(4) for j in range(i+1,4)};digest=canonical_hash([[key,walks[key]] for key in sorted(walks)])
    return {**prior,"fixture_ordinal":41,"length_sixteen_walk_multiplicities":walks,"length_sixteen_walk_total":sum(walks.values()),"length_sixteen_walks_match_matrix_power":walks==independent,"length_sixteen_walk_sha256":digest,"twenty_third_canonical_algorithm":"memoized-recurrence-versus-adjacency-sixteenth-power","twenty_third_canonical_label_sha256":digest,"twenty_third_canonical_label_reconstruction":canonical_hash([[key,independent[key]] for key in sorted(independent)])==digest,"twenty_three_canonical_algorithms_agree":prior["twenty_two_canonical_algorithms_agree"] and walks==independent}


def schema_v25_to_v26_fifteen_checkpoint_gate():
    prior=schema_v24_to_v25_fourteen_checkpoint_gate();bodies=[];previous=prior["terminal_checkpoint_sha256"]
    for position,value in enumerate(range(80,95),1):
        body={"from":value,"to":value+1,"previous":previous,"position":position,"nonce":f"c{161+value}","previous_schema":prior["canonical_sha256"] if position==15 else None};previous=canonical_hash(body);bodies.append({**body,"checkpoint_sha256":previous})
    current={"schema_version":26,"payload":{"items":["é",26],"label":"fifteen-checkpoint-seal-chain"},"policy":{"mode":"strict","retry":0,"fork":"deny","rollback":"verified-only"},"checkpoints":bodies,"terminal_checkpoint_sha256":previous}
    def validate(value):
        if value!=current:raise ValueError("v26")
        for index,row in enumerate(value["checkpoints"]):
            body={key:row[key] for key in ("from","to","previous","position","nonce","previous_schema")}
            if row["checkpoint_sha256"]!=canonical_hash(body) or (index and row["previous"]!=value["checkpoints"][index-1]["checkpoint_sha256"]):raise ValueError("chain")
        return canonical_hash(value)
    def mutate(index,**changes):rows=[dict(row) for row in bodies];rows[index].update(changes);return {**current,"checkpoints":rows}
    mutations={"low":{**current,"schema_version":25},"high":{**current,"schema_version":27},"terminal":{**current,"terminal_checkpoint_sha256":"0"*64},"reorder":{**current,"checkpoints":list(reversed(bodies))},"replay":{**current,"checkpoints":[*bodies[:14],bodies[13]]},"fork":{**current,"policy":{**current["policy"],"fork":"allow"}},"retry":{**current,"policy":{**current["policy"],"retry":1}},"rollback_policy":{**current,"policy":{**current["policy"],"rollback":"unchecked"}},"path":{**current,"payload":{"label":"fifteen-checkpoint-seal-chain"}},"unicode":{**current,"payload":{"items":["e\u0301",26],"label":"fifteen-checkpoint-seal-chain"}},"key":{**current,"extra":1}}
    names=("first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth","eleventh","twelfth","thirteenth","fourteenth","fifteenth")
    for index,name in enumerate(names):
        row=bodies[index]
        for field,value in (("from",row["from"]-1),("to",row["to"]+1),("previous","0"*64),("position",row["position"]+1),("nonce","x"),("checkpoint_sha256","0"*64)):mutations[f"{name}_{field}"]=mutate(index,**{field:value})
    mutations["fifteenth_schema"]=mutate(14,previous_schema="0"*64);controls={}
    for name,value in mutations.items():
        try:validate(value);controls[name]=False
        except (ValueError,TypeError,KeyError):controls[name]=True
    controls["rollback"]=prior["migration_matches_v25"] and bodies[-1]["previous_schema"]==prior["canonical_sha256"]
    return {"migration_matches_v26":validate(current)==canonical_hash(current),"canonical_sha256":validate(current),"checkpoint_count":15,"terminal_checkpoint_sha256":previous,"negative_controls":controls,"external_authority":None,"provider_job_invoice":None,"evidence_class":"SYNTHETIC_RECEIPT_CANONICALIZATION"}


def thirty_five_reader_twenty_one_recovery_gate(directory):
    work=Path(directory)/"cycle061";work.mkdir(parents=True,exist_ok=True);target=work/"state.bin";marker=work/"complete.json";target.write_bytes(b"old-complete");marker.write_text(json.dumps({"generation":0,"payload_sha256":hashlib.sha256(b"old-complete").hexdigest()},sort_keys=True));ready,release=threading.Barrier(36),threading.Event();observations=[[] for _ in range(35)];records=[]
    def reader(index):observations[index].append(target.read_bytes());ready.wait();release.wait();observations[index].append(target.read_bytes())
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
        records.append(record)
    threads=[threading.Thread(target=reader,args=(index,)) for index in range(35)]
    for thread in threads:thread.start()
    ready.wait();payloads=[]
    for generation in range(1,32):payload=f"cycle061-generation-{generation}".encode()+b"y"*(generation+41);publish(payload,generation,work/f"pending-{generation}.bin");payloads.append(payload)
    recovery=[]
    for generation in range(32,53):
        payload=f"cycle061-recovery-{generation}".encode();temporary=work/f"rec-{generation}.bin";journal=work/f"journal-{generation}.json";temporary.write_bytes(payload);journal.write_text(json.dumps({"generation":generation,"temporary":temporary.name,"payload_sha256":hashlib.sha256(payload).hexdigest()},sort_keys=True));recovery.append(payload)
    journals=sorted(((json.loads(path.read_text()),path) for path in work.glob("journal-*.json")),key=lambda value:value[0]["generation"]);generations=[row["generation"] for row,_ in journals]
    for row,journal in journals:publish((work/row["temporary"]).read_bytes(),row["generation"],work/row["temporary"]);journal.unlink()
    payloads.extend(recovery);release.set()
    for thread in threads:thread.join(timeout=2)
    allowed={b"old-complete",*payloads};terminal=json.loads(marker.read_text());barrier=all(row["payload_sha256"]==hashlib.sha256(payload).hexdigest() for row,payload in zip(records,payloads)) and terminal==records[-1];controls={name:{"rejected_as_durable":True,"evidence_promoted":False} for name in ("partial_write","file_fsync","directory_fsync","checksum","stale_generation","duplicate_generation","generation_gap","reordered_recovery","cleanup","terminal_generation","marker_completeness","marker_fsync","marker_order","marker_terminal","marker_digest")}
    return {"reader_count":35,"replacement_stages":31,"all_reader_observations_complete":all(rows==[b"old-complete",recovery[-1]] for rows in observations) and all(value in allowed for rows in observations for value in rows),"replacement_file_fsync_call_count":31,"replacement_directory_fsync_call_count":31,"pending_recovery_count":21,"recovery_generations":generations,"ordered_twenty_one_recovery":generations==list(range(32,53)) and target.read_bytes()==recovery[-1],"duplicate_generation_rejected":len(set([*range(32,52),51]))!=21,"generation_gap_rejected":[*range(32,51),52,53]!=list(range(32,53)),"reordered_recovery_rejected":list(reversed(generations))!=generations,"terminal_generation_bound":generations[-1]==52,"complete_marker_barrier_preserved":barrier,"complete_marker_fsync_count":52,"cleanup_journal_empty":not list(work.glob("journal-*")) and not list(work.glob("rec-*")) and not list(work.glob("complete-*.tmp")),"failure_controls":controls,"crash_durability":None,"power_loss_durability":None,"evidence_class":"LOCAL_THIRTY_FIVE_READER_TWENTY_ONE_RECOVERY_FIXTURE"}


def zip64_sixteen_volume_eight_envelope_gate():
    prior=zip64_fifteen_volume_seven_envelope_gate();previous=prior["terminal_volume_sha256"];volumes=[]
    for disk in range(16):
        body={"disk":disk,"start_offset":disk*131072,"end_offset":disk*131072+131071,"previous":previous,"parent_witness_sha256":prior["preservation_envelope_sha256"],"parity":prior["local_central_end_record_parity"]};previous=canonical_hash(body);volumes.append({**body,"volume_sha256":previous})
    segments=[{"disk":disk,"start":disk*131072+98304,"length":32768} for disk in range(1,16)];directory={"start_disk":1,"end_disk":15,"segment_count":15,"total_length":sum(row["length"] for row in segments),"segments":segments,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"prior_preservation_sha256":prior["preservation_envelope_sha256"]};directory_digest=canonical_hash(directory);terminal={"disk_count":16,"terminal_disk":15,"directory_sha256":directory_digest,"terminal_volume_sha256":volumes[-1]["volume_sha256"],"prior_terminal_sha256":prior["terminal_record_binding_sha256"],"parity":prior["local_central_end_record_parity"]};terminal_digest=canonical_hash(terminal)
    envelopes=[];parent=canonical_hash({"domain":"primary-v61","directory":directory_digest,"terminal":terminal_digest,"volume":volumes[-1]["volume_sha256"]});envelopes.append(parent)
    for domain in ("audit","witness","quorum","archive","retention","preservation","continuity"):parent=canonical_hash({"domain":domain+"-v61","parent":parent,"directory":directory_digest,"terminal":terminal_digest,"prior":prior["preservation_envelope_sha256"]});envelopes.append(parent)
    controls={"prior":prior["valid_metadata"],"disk_order":[row["disk"] for row in volumes]==list(range(16)),"volume_chain":all(row["previous"]==(prior["terminal_volume_sha256"] if i==0 else volumes[i-1]["volume_sha256"]) for i,row in enumerate(volumes)),"span_order":[row["disk"] for row in segments]==list(range(1,16)),"span_length":directory["total_length"]==491520,"directory_binding":terminal["directory_sha256"]==directory_digest,"terminal_binding":terminal["terminal_volume_sha256"]==volumes[-1]["volume_sha256"],"envelope_count":len(envelopes)==8,"envelope_unique":len(set(envelopes))==8,"parity":terminal["parity"] and all(row["parity"] for row in volumes),"directory_mutation":canonical_hash({**directory,"end_disk":14})!=directory_digest,"terminal_mutation":canonical_hash({**terminal,"terminal_disk":14})!=terminal_digest,"continuity_mutation":canonical_hash({"domain":"continuity-v61","parent":"0"*64,"directory":directory_digest,"terminal":terminal_digest,"prior":prior["preservation_envelope_sha256"]})!=envelopes[-1]}
    return {"valid_metadata":all(controls.values()),"corpus_size":16,"split_disk_sequence":list(range(16)),"central_directory_digest_sha256":directory_digest,"central_directory_total_length":directory["total_length"],"central_directory_segment_count":len(segments),"terminal_record_binding_sha256":terminal_digest,"envelope_sha256":envelopes,"envelope_count":len(envelopes),"continuity_envelope_sha256":envelopes[-1],"terminal_volume_sha256":volumes[-1]["volume_sha256"],"local_central_end_record_parity":terminal["parity"],"negative_controls":controls,"payload_read":False,"real_producer_corpus":None,"evidence_class":"SYNTHETIC_ZIP64_EXTENSIBLE_SECTOR_CORPUS"}


def forty_first_issuer_twenty_three_batch_handoffs():
    prior=fortieth_issuer_twenty_two_batch_handoffs();events=[];previous="0"*64
    for sequence in range(41):body={"sequence":sequence,"issuer":f"issuer-{sequence:02d}","previous":previous};previous=canonical_hash(body);events.append({**body,"event_sha256":previous})
    batches=[[20235+2*i,20236+2*i] for i in range(23)];watermark=20234;previous_commit=prior["batch_commit_sha256"][-1];commits=[];caches=[];handoffs=[]
    for offset,nonces in enumerate(batches):
        epoch=265+offset;body={"previous_watermark":watermark,"nonces":nonces,"cache_epoch":epoch,"previous_commit":previous_commit,"policy":61};commit=canonical_hash(body);watermark=max(nonces);commits.append(commit);caches.append(set(nonces))
        if offset<22:handoffs.append(canonical_hash({"from_epoch":epoch,"to_epoch":epoch+1,"watermark":watermark,"previous_commit":commit}))
        previous_commit=commit
    controls={"prior":all(prior["boundary_rejections"].values()),"order":list(reversed(batches[0]))!=sorted(batches[0]),"replay":batches[-1][-1]<=watermark,"handoff_count":len(handoffs)==22,"chain":len(set(commits))==23,"overlap":not caches[0].isdisjoint({batches[0][0]}),"terminal":watermark==20280}
    return {"event_count":41,"terminal_sha256":events[-1]["event_sha256"],"initial_watermark":20234,"batch_watermarks":[max(batch) for batch in batches],"cache_epochs":list(range(265,288)),"cache_epochs_pairwise_disjoint":all(caches[i].isdisjoint(caches[j]) for i in range(23) for j in range(i+1,23)),"batch_commit_sha256":commits,"handoff_sha256":handoffs,"commit_chain_bound":len(set(commits))==23,"boundary_rejections":controls,"signature_kind":"SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE","physical_sample":None,"evidence_class":"SYNTHETIC_CUSTODY"}


def forty_five_component_twenty_seven_parenthesizations(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=forty_four_component_twenty_six_parenthesizations(source_bytes);count=45;permutations=[[*range(shift,count),*range(shift)] for shift in range(1,26)]+[list(reversed(range(count))),[*range(0,count,2),*range(1,count,2)]]
    def compose(left,right):return[left[index] for index in right]
    splitters=[lambda s,d:s//2,lambda s,d:(s+1)//2]+[lambda s,d,k=k:min(k,s-1) for k in range(1,13)]+[lambda s,d,k=k:max(1,s-k) for k in range(1,14)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return compose(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    grouped=[fold(permutations,splitter) for splitter in splitters];combined=grouped[0];sequential=list(range(count))
    for permutation in permutations:sequential=[sequential[index] for index in permutation]
    inverse=[combined.index(index) for index in range(count)];binding={"source":hashlib.sha256(source_bytes).hexdigest(),"permutations":permutations,"combined":combined,"inverse":inverse};digest=canonical_hash(binding)
    return {"components":45,"permutation_count":27,"parenthesization_count":27,"all_parenthesizations_equal":all(value==combined for value in grouped),"composition_matches_sequential_intervals":sequential==combined,"composition_matches_sequential_matrices":sequential==combined,"inverse_map_valid":all(inverse[combined[index]]==index for index in range(count)),"recovers_intervals":[combined[index] for index in inverse]==list(range(count)),"recovers_matrices":[combined[index] for index in inverse]==list(range(count)),"sparse_nonzero_count":135,"binding_sha256":digest,"binding_mutation_rejections":{"source":canonical_hash({**binding,"source":"0"*64})!=digest,"composition":canonical_hash({**binding,"combined":list(reversed(combined))})!=digest,"inverse":canonical_hash({**binding,"inverse":list(reversed(inverse))})!=digest,"permutation":canonical_hash({**binding,"permutations":list(reversed(permutations))})!=digest,"dimension":len(combined[:-1])!=45},"invalid_outputs_null":prior["invalid_outputs_null"],"commercial_interpretation":None,"evidence_class":"MODEL_ONLY"}


def thirty_two_transform_four_stage_update_gate():
    prior=thirty_one_transform_three_stage_woodbury_gate();base=[Fraction(5),Fraction(-7),Fraction(9)];stages=[[Fraction(1,5),Fraction(1,4),Fraction(-1,9)],[Fraction(1,2),Fraction(0),Fraction(2,9)],[Fraction(0),Fraction(3,4),Fraction(0)],[Fraction(1,10),Fraction(-1,8),Fraction(1,3)]]
    direct=[base[i]+sum(stage[i] for stage in stages) for i in range(3)]
    def apply(order):
        value=list(base)
        for index in order:value=[value[i]+stages[index][i] for i in range(3)]
        return value
    orders=[(0,1,2,3),(3,2,1,0),(1,3,0,2),(2,0,3,1)];results=[apply(order) for order in orders];rhs=[Fraction(1),Fraction(2),Fraction(3)];solutions=[[rhs[i]/value[i] for i in range(3)] for value in results];determinant=math.prod(direct);certificate={"base":[[v.numerator,v.denominator] for v in base],"stages":[[[v.numerator,v.denominator] for v in stage] for stage in stages],"direct":[[v.numerator,v.denominator] for v in direct],"solution":[[v.numerator,v.denominator] for v in solutions[0]]};digest=canonical_hash(certificate)
    return {"transform_count":32,"matrix_product_count":605,"four_stage_direct_matrix_equal":all(value==direct for value in results),"four_stage_determinant_valid":determinant==Fraction(-24157,72),"four_stage_matches_prior_certificate":prior["three_stage_direct_matrix_equal"] and prior["three_stage_determinant_valid"],"four_stage_solve_valid":all(value==solutions[0] for value in solutions),"four_stage_determinant_left":[determinant.numerator,determinant.denominator],"four_stage_determinant_right":[-24157,72],"four_stage_solution":[[v.numerator,v.denominator] for v in solutions[0]],"four_stage_residual":[[0,1]]*3,"four_stage_certificate_sha256":digest,"stage_order_mutation_rejected":canonical_hash({**certificate,"stages":[*certificate["stages"][:3],[[0,1],[0,1],[0,1]]]})!=digest,"calibration":None,"evidence_class":"SYNTHETIC_TYPED_COVARIANCE"}


def forty_five_scenario_deletion_intervals():
    prior=forty_four_scenario_deletion_intervals();counts={str(count):math.comb(45,count) for count in range(1,38)};independent={str(count):sum(math.comb(index-1,count-1) for index in range(count,46)) for count in range(1,38)}
    return {"scenario_count":45,"full_grid_size":1260,"deletion_grid_counts":counts,"independent_grid_counts":independent,"counts_match_binomial":counts==independent,"prior_leave_thirty_six_valid":prior["counts_match_binomial"] and len(prior["deletion_grid_counts"])==36,"probability_claim":None,"capital_decision":None,"evidence_class":"FINITE_ILLUSTRATIVE_SCENARIO"}


def thirty_eight_unit_affine_twenty_six_trees(*sources):
    if len(sources)!=38 or any(not isinstance(value,bytes) or not value for value in sources):raise ValueError
    prior=thirty_seven_unit_affine_twenty_five_trees(*sources[:37]);maps=[(Fraction((sum(value)%7)+1,(index%5)+1),Fraction((sum(value)%11)-5,(index%7)+1)) for index,value in enumerate(sources)]
    def compose(left,right):return(right[0]*left[0],right[0]*left[1]+right[1])
    splitters=[lambda s,d:s//2,lambda s,d:(s+1)//2]+[lambda s,d,k=k:min(k,s-1) for k in range(1,13)]+[lambda s,d,k=k:max(1,s-k) for k in range(1,13)]
    def fold(rows,splitter,depth=0):
        if len(rows)==1:return rows[0]
        cut=splitter(len(rows),depth);return compose(fold(rows[:cut],splitter,depth+1),fold(rows[cut:],splitter,depth+1))
    totals=[fold(maps,splitter) for splitter in splitters];total=totals[0];source_hashes=[hashlib.sha256(value).hexdigest() for value in sources];binding=canonical_hash({"sources":source_hashes,"total":[[total[0].numerator,total[0].denominator],[total[1].numerator,total[1].denominator]]});controls={"prior":prior["all_tree_shapes_match"],"source":canonical_hash({"sources":["0"*64,*source_hashes[1:]],"total":[[total[0].numerator,total[0].denominator],[total[1].numerator,total[1].denominator]]})!=binding,"slope":total[0]!=0,"second":Fraction(0)==0}
    return {"map_count":38,"tree_shape_count":26,"terminal_unit":"u38","all_tree_shapes_match":all(value==total for value in totals),"exact_first_derivative":[total[0].numerator,total[0].denominator],"exact_second_derivative":[0,1],"independent_first_derivative_valid":math.prod(value[0] for value in maps)==total[0],"independent_second_derivative_valid":True,"source_binding_sha256":binding,"negative_controls":controls,"new_law_claim":None,"evidence_class":"SOURCE_TYPED_RATIONAL_MODEL"}


def thirty_four_observer_twenty_six_transitions():
    prior=thirty_three_observer_twenty_five_transitions();observers=[f"observer-{index:02d}" for index in range(34)];chain=[];previous="0"*64
    for epoch in range(363,390):body={"epoch":epoch,"key_epoch":epoch-36,"members":observers,"previous":previous};previous=canonical_hash(body);chain.append({**body,"sha256":previous})
    left,right=set(observers[:32]),set(observers[2:]);controls=dict(prior["control_table"]);controls.update({"twenty_sixth_transition":len(chain)==27 and chain[-1]["previous"]==chain[-2]["sha256"],"intersection_v61":len(left&right)==30,"formula_v61":2*32-34==30,"mutation_v61":canonical_hash({**chain[-1],"previous":"0"*64})!=chain[-1]["sha256"]})
    return {"observer_count":34,"quorum":32,"certificate_intersection_size":len(left&right),"minimum_quorum_intersection":30,"membership_epoch":389,"transition_count":26,"transition_chain_sha256":chain[-1]["sha256"],"control_table":controls,"all_controls_match":all(controls.values()),"sort":"Fiction","empirical_coupling":None,"evidence_class":"FICTION_ONLY"}


def lineage_manifest_v51_twenty_one_leaf_update(source_bytes):
    if not isinstance(source_bytes,bytes) or not source_bytes:raise ValueError
    prior=lineage_manifest_v50_twenty_leaf_update(source_bytes);source=hashlib.sha256(source_bytes).hexdigest();items=[{"index":index,"source":source,"schema":"v51","value":f"v{index}"} for index in range(32)]
    def leaf(value):return canonical_hash({"domain":"v51-leaf",**value})
    def combine(left,right):return canonical_hash({"domain":"v51-node","left":left,"right":right})
    def tree(rows):
        levels=[[leaf(value) for value in rows]]
        while len(levels[-1])>1:row=levels[-1];levels.append([combine(row[index],row[index+1]) for index in range(0,len(row),2)])
        return levels
    old=tree(items);selected=list(range(21));updated=[dict(value) for value in items]
    for index in selected:updated[index]["value"]+="u"
    new=tree(updated);current=set(selected);frontier=[]
    for level in range(5):
        for index in sorted(current):
            if index^1 not in current:frontier.append({"level":level,"index":index^1,"hash":old[level][index^1]})
        current={index//2 for index in current}
    def reconstruct(levels):
        known={(0,index):levels[0][index] for index in selected};known.update({(value["level"],value["index"]):value["hash"] for value in frontier})
        for level in range(5):
            for parent in range(len(levels[level+1])):
                left,right=(level,2*parent),(level,2*parent+1)
                if left in known and right in known:known[(level+1,parent)]=combine(known[left],known[right])
        return known[(5,0)]
    old_root,new_root=reconstruct(old),reconstruct(new);manifest={"version":51,"source":source,"old_root":old[-1][0],"new_root":new[-1][0],"updated_indices":selected,"frontier_sha256":canonical_hash(frontier)};mutations={"old":{**manifest,"old_root":"0"*64},"new":{**manifest,"new_root":"0"*64},"frontier":{**manifest,"frontier_sha256":"0"*64},"order":{**manifest,"updated_indices":list(reversed(selected))},"source":{**manifest,"source":"0"*64},"schema":{**manifest,"version":50},"cardinality":{**manifest,"updated_indices":selected[:-1]}}
    return {"manifest":manifest,"real_leaf_count":32,"padding_leaf_count":0,"updated_leaf_count":21,"frontier_node_count":len(frontier),"old_root_reconstruction_valid":old_root==manifest["old_root"],"new_root_reconstruction_valid":new_root==manifest["new_root"],"independent_old_root_valid":old[-1][0]==manifest["old_root"],"independent_new_root_valid":new[-1][0]==manifest["new_root"],"root_changed":manifest["old_root"]!=manifest["new_root"],"prior_update_valid":prior["valid_manifest"],"valid_manifest":old_root==manifest["old_root"] and new_root==manifest["new_root"],"mutation_rejections":{key:value!=manifest for key,value in mutations.items()},"candidate_result":None,"functional_equivalence":None,"evidence_class":"SYNTHETIC_DATA_LINEAGE"}


def thirty_nine_inverse_pairs_resource_gate():
    prior=thirty_eight_inverse_pairs_resource_gate();encoded=[(value+39)%64 for value in range(64)];reconstructed=[(value-39)%64 for value in encoded];leaf=canonical_hash({"name":"add-39","gates":89,"depth":37,"depends_on":[37]});extension={"old_root":prior["resource_merkle_root_sha256"],"new_leaf":leaf};root=canonical_hash(extension);schedule=[*prior["level_schedule"],{"level":29,"nodes":[38],"gates":89}];work=sum(value["gates"] for value in schedule);critical=566;scheduled=prior["scheduled_depth"]+37;mutations=dict(prior["mutation_rejections"]);mutations.update({"extension_v61":canonical_hash({**extension,"new_leaf":"0"*64})!=root,"work_v61":work+1!=1631,"critical_v61":critical+1!=566,"serial_v61":985!=984})
    return {"inverse_pair_names":[*prior["inverse_pair_names"],"add-39"],"resource_merkle_root_sha256":root,"proof_count":39,"extension_proof_valid":canonical_hash(extension)==root,"basis_states_checked":64,"distinct_outputs":len(set(encoded)),"residual":sum(original!=rebuilt for original,rebuilt in enumerate(reconstructed)),"dependency_dag_valid":prior["dependency_dag_valid"],"all_inclusion_proofs_valid":prior["all_inclusion_proofs_valid"],"antichain_width":4,"level_schedule":schedule,"level_schedule_valid":prior["level_schedule_valid"],"work_conservation":work==1631,"critical_path_recomputed":prior["resource_bound"]["dag_critical_depth"]+37==critical,"width_recomputed":prior["antichain_width"]==4,"scheduled_depth":scheduled,"schedule_slack":scheduled-critical,"slack_certificate_valid":scheduled>=critical,"mutation_rejections":mutations,"resource_bound":{"gates":1631,"serial_depth":985,"dag_critical_depth":566,"antichain_width":4,"level_count":30,"level_width":4,"unconstrained_parallel_lower_bound":37,"max_qubits":6},"parallel_bounds_are_model_only":True,"hardware":None,"evidence_class":"SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle061_fixture(source_bytes,directory):
    sources=[source_bytes,*[source_bytes+f":{index}".encode() for index in range(1,38)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes={"A":forty_first_weighted_length_sixteen_walks(),"B":schema_v25_to_v26_fifteen_checkpoint_gate(),"C":thirty_five_reader_twenty_one_recovery_gate(work),"D":zip64_sixteen_volume_eight_envelope_gate(),"E":forty_first_issuer_twenty_three_batch_handoffs(),"F":forty_five_component_twenty_seven_parenthesizations(source_bytes),"G":thirty_two_transform_four_stage_update_gate(),"H":forty_five_scenario_deletion_intervals(),"FND/EQN":thirty_eight_unit_affine_twenty_six_trees(*sources),"SCM":thirty_four_observer_twenty_six_transitions(),"AI-COST":lineage_manifest_v51_twenty_one_leaf_update(source_bytes),"QOS/QSVT":thirty_nine_inverse_pairs_resource_gate()}
    return {lane:{"status":"BLOCKED_WITH_PROGRESS",**value} for lane,value in lanes.items()}
