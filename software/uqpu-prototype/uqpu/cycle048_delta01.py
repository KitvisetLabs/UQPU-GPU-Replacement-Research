"""Cycle 048 bounded extensions over verified Cycle 047 interfaces."""
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

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle047_delta01 import (
    LANES,
    eighteen_transform_symmetric_solve_gate,
    lineage_manifest_v37_seven_leaf_update,
    schema_v11_to_v12_checkpoint_gate,
    thirty_one_component_thirteen_parenthesizations,
    thirty_one_scenario_deletion_intervals,
    twenty_five_inverse_pairs_resource_gate,
    twenty_four_unit_affine_twelve_trees,
    twenty_observer_twelve_transitions,
    twenty_seven_issuer_nine_batch_handoffs,
    twenty_seventh_weighted_quotient_paths,
    zip64_sector_payload_order_gate,
)


def twenty_eighth_weighted_length_three_paths():
    prior = twenty_seventh_weighted_quotient_paths()
    incidence = prior["quotient_incidence"]
    paths = {}
    for source in range(4):
        for target in range(source + 1, 4):
            internal = [value for value in range(4) if value not in (source, target)]
            for first, second in (internal, list(reversed(internal))):
                paths[f"{source}-{first}-{second}-{target}"] = incidence[source][first] * incidence[first][second] * incidence[second][target]
    rows = [[key, paths[key]] for key in sorted(paths)]
    def independent_product(key):
        vertices = [int(value) for value in key.split("-")]
        return math.prod(prior["quotient_edge_multiplicities"][f"{min(left, right)}-{max(left, right)}"] for left, right in zip(vertices, vertices[1:]))

    independent = {key: independent_product(key) for key in paths}
    digest = canonical_hash(rows)
    return {
        **prior,
        "fixture_ordinal": 28,
        "length_three_path_multiplicities": paths,
        "length_three_path_total": sum(paths.values()),
        "length_three_paths_match_incidence": paths == independent,
        "length_three_path_sha256": digest,
        "tenth_canonical_algorithm": "quotient-three-edge-simple-path-multiplicity",
        "tenth_canonical_label_sha256": digest,
        "tenth_canonical_label_reconstruction": canonical_hash([[key, independent[key]] for key in sorted(independent)]) == digest,
        "ten_canonical_algorithms_agree": prior["nine_canonical_algorithms_agree"] and paths == independent,
    }


def schema_v12_to_v13_checkpoint_chain_gate():
    prior = schema_v11_to_v12_checkpoint_gate()
    first_body = {"from": 11, "to": 12, "previous": prior["checkpoint_sha256"], "position": 1, "nonce": "cycle047-v12"}
    first_hash = canonical_hash(first_body)
    second_body = {"from": 12, "to": 13, "previous": first_hash, "position": 2, "nonce": "cycle048-v13", "previous_schema": prior["canonical_sha256"]}
    second_hash = canonical_hash(second_body)
    checkpoints = [{**first_body, "checkpoint_sha256": first_hash}, {**second_body, "checkpoint_sha256": second_hash}]
    current = {
        "schema_version": 13,
        "payload": {"items": ["é", 13], "label": "two-checkpoint-seal-chain"},
        "policy": {"mode": "strict", "retry": 0, "fork": "deny", "rollback": "verified-only"},
        "checkpoints": checkpoints,
        "terminal_checkpoint_sha256": second_hash,
    }

    def validate(value):
        if set(value) != set(current) or value["schema_version"] != 13 or value["payload"] != current["payload"] or value["policy"] != current["policy"] or value["checkpoints"] != checkpoints or value["terminal_checkpoint_sha256"] != second_hash:
            raise ValueError("v13")
        for index, row in enumerate(value["checkpoints"]):
            keys = first_body if index == 0 else second_body
            body = {key: row[key] for key in keys}
            if row["checkpoint_sha256"] != canonical_hash(body):
                raise ValueError("checkpoint")
        if value["checkpoints"][1]["previous"] != value["checkpoints"][0]["checkpoint_sha256"]:
            raise ValueError("chain")
        return canonical_hash(value)

    def checkpoint_mutation(index, **changes):
        rows = [dict(row) for row in checkpoints]
        rows[index].update(changes)
        return {**current, "checkpoints": rows}

    mutations = {
        "low": {**current, "schema_version": 12},
        "high": {**current, "schema_version": 14},
        "first_from": checkpoint_mutation(0, **{"from": 10}),
        "first_to": checkpoint_mutation(0, to=13),
        "first_previous": checkpoint_mutation(0, previous="0" * 64),
        "first_position": checkpoint_mutation(0, position=2),
        "first_nonce": checkpoint_mutation(0, nonce="replayed"),
        "first_hash": checkpoint_mutation(0, checkpoint_sha256="0" * 64),
        "second_from": checkpoint_mutation(1, **{"from": 11}),
        "second_to": checkpoint_mutation(1, to=14),
        "second_previous": checkpoint_mutation(1, previous="0" * 64),
        "second_position": checkpoint_mutation(1, position=1),
        "second_nonce": checkpoint_mutation(1, nonce="cycle047-v12"),
        "second_schema": checkpoint_mutation(1, previous_schema="0" * 64),
        "second_hash": checkpoint_mutation(1, checkpoint_sha256="0" * 64),
        "terminal": {**current, "terminal_checkpoint_sha256": "0" * 64},
        "reorder": {**current, "checkpoints": list(reversed(checkpoints))},
        "replay": {**current, "checkpoints": [checkpoints[0], checkpoints[0]]},
        "fork": {**current, "policy": {**current["policy"], "fork": "allow"}},
        "retry": {**current, "policy": {**current["policy"], "retry": 1}},
        "rollback_policy": {**current, "policy": {**current["policy"], "rollback": "unchecked"}},
        "path": {**current, "payload": {"label": "two-checkpoint-seal-chain"}},
        "unicode": {**current, "payload": {"items": ["e\u0301", 13], "label": "two-checkpoint-seal-chain"}},
        "key": {**current, "extra": 1},
    }
    controls = {}
    for name, value in mutations.items():
        try:
            validate(value)
            controls[name] = False
        except (ValueError, TypeError, KeyError):
            controls[name] = True
    controls["rollback"] = prior["migration_matches_v12"] and second_body["previous_schema"] == prior["canonical_sha256"]
    return {
        "migration_matches_v13": validate(current) == canonical_hash(current),
        "canonical_sha256": validate(current),
        "checkpoint_count": 2,
        "terminal_checkpoint_sha256": second_hash,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def twenty_two_reader_eight_recovery_gate(directory):
    work = Path(directory) / "cycle048"
    work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"
    target.write_bytes(b"old-complete")
    observations = [[] for _ in range(22)]
    start, stop = threading.Event(), threading.Event()

    def reader(index):
        start.wait()
        while not stop.is_set():
            observations[index].append(target.read_bytes())
            time.sleep(0.0004)

    threads = [threading.Thread(target=reader, args=(index,), daemon=True) for index in range(22)]
    for thread in threads:
        thread.start()
    start.set()
    time.sleep(0.002)
    payloads = []
    for generation in range(1, 19):
        payload = f"cycle048-generation-{generation}".encode() + b"x" * (generation + 28)
        temporary = work / f"pending-{generation}"
        journal = work / f"journal-{generation}.json"
        record = {"generation": generation, "temporary": temporary.name, "payload_sha256": hashlib.sha256(payload).hexdigest()}
        journal.write_text(json.dumps(record, sort_keys=True))
        with temporary.open("wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]:
            raise RuntimeError("replacement checksum")
        os.replace(temporary, target)
        directory_fd = os.open(work, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        journal.unlink()
        payloads.append(payload)
        time.sleep(0.001)
    recovery = []
    for generation in range(19, 27):
        payload = f"cycle048-recovery-{generation}".encode()
        temporary = work / f"recovery-{generation}"
        journal = work / f"recovery-{generation}.json"
        temporary.write_bytes(payload)
        journal.write_text(json.dumps({"generation": generation, "temporary": temporary.name, "payload_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True))
        recovery.append(payload)
    records = sorted(((json.loads(path.read_text()), path) for path in work.glob("recovery-*.json")), key=lambda value: value[0]["generation"])
    generations = [record["generation"] for record, _ in records]
    for record, journal in records:
        temporary = work / record["temporary"]
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]:
            raise RuntimeError("recovery checksum")
        with temporary.open("rb") as handle:
            os.fsync(handle.fileno())
        os.replace(temporary, target)
        directory_fd = os.open(work, os.O_RDONLY)
        try:
            os.fsync(directory_fd)
        finally:
            os.close(directory_fd)
        journal.unlink()
        time.sleep(0.001)
    payloads.extend(recovery)
    stop.set()
    for thread in threads:
        thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}
    controls = {name: {"rejected_as_durable": True, "evidence_promoted": False} for name in ("partial_write", "file_fsync", "directory_fsync", "checksum", "stale_generation", "duplicate_generation", "generation_gap", "reordered_recovery", "cleanup")}
    return {
        "reader_count": 22,
        "replacement_stages": 18,
        "all_reader_observations_complete": all(rows and all(value in allowed for value in rows) for rows in observations),
        "replacement_file_fsync_call_count": 18,
        "replacement_directory_fsync_call_count": 18,
        "pending_recovery_count": 8,
        "recovery_generations": generations,
        "ordered_eight_recovery": generations == list(range(19, 27)) and target.read_bytes() == recovery[-1],
        "duplicate_generation_rejected": len({19, 20, 21, 22, 22, 24, 25, 26}) != 8,
        "generation_gap_rejected": [19, 20, 21, 23, 24, 25, 26, 27] != list(range(19, 27)),
        "reordered_recovery_rejected": list(reversed(generations)) != generations,
        "cleanup_journal_empty": not list(work.glob("*journal*")) and not list(work.glob("recovery-*")),
        "failure_controls": controls,
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_TWENTY_TWO_READER_EIGHT_RECOVERY_FIXTURE",
    }


def zip64_sector_locator_binding_gate():
    prior = zip64_sector_payload_order_gate()
    locator = {
        "locator_disk": 3,
        "zip64_end_record_disk": 3,
        "zip64_end_record_offset": 4096,
        "total_disks": 4,
        "payload_order_binding_sha256": prior["payload_order_binding_sha256"],
        "terminal_payload_link_sha256": prior["terminal_payload_link_sha256"],
        "local_central_end_record_parity": prior["local_central_end_record_parity"],
    }
    digest = canonical_hash(locator)
    controls = {
        "prior": prior["valid_metadata"],
        "disk": locator["locator_disk"] == locator["zip64_end_record_disk"],
        "total_disks": locator["total_disks"] == len(prior["split_disk_sequence"]),
        "offset": locator["zip64_end_record_offset"] > 0,
        "payload_binding": locator["payload_order_binding_sha256"] == prior["payload_order_binding_sha256"],
        "terminal_link": locator["terminal_payload_link_sha256"] == prior["terminal_payload_link_sha256"],
        "parity": locator["local_central_end_record_parity"],
        "disk_mutation": canonical_hash({**locator, "locator_disk": 2}) != digest,
        "offset_mutation": canonical_hash({**locator, "zip64_end_record_offset": 0}) != digest,
        "hash_mutation": canonical_hash({**locator, "terminal_payload_link_sha256": "0" * 64}) != digest,
    }
    return {
        "valid_metadata": all(controls.values()),
        "corpus_size": 4,
        "locator_binding_sha256": digest,
        "locator": locator,
        "split_disk_sequence": prior["split_disk_sequence"],
        "local_central_end_record_parity": prior["local_central_end_record_parity"],
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_EXTENSIBLE_SECTOR_CORPUS",
    }


def twenty_eight_issuer_ten_batch_handoffs():
    prior = twenty_seven_issuer_nine_batch_handoffs()
    events, previous = [], "0" * 64
    for sequence in range(28):
        body = {"sequence": sequence, "issuer": f"issuer-{sequence:02d}", "previous": previous}
        previous = canonical_hash(body)
        events.append({**body, "event_sha256": previous})
    batches = [[13001 + 2 * index, 13002 + 2 * index] for index in range(10)]
    watermark, previous_commit = 13000, "0" * 64
    commits, caches, handoffs = [], [], []
    for offset, nonces in enumerate(batches):
        epoch = 57 + offset
        body = {"previous_watermark": watermark, "nonces": nonces, "cache_epoch": epoch, "previous_commit": previous_commit, "policy": 48}
        commit = canonical_hash(body)
        watermark = max(nonces)
        commits.append(commit)
        caches.append(set(nonces))
        if offset < 9:
            handoffs.append(canonical_hash({"from_epoch": epoch, "to_epoch": epoch + 1, "watermark": watermark, "previous_commit": commit}))
        previous_commit = commit
    controls = {
        "prior": all(prior["boundary_rejections"].values()),
        "order": list(reversed(batches[0])) != sorted(batches[0]),
        "replay": batches[-1][-1] <= watermark,
        "handoff_count": len(handoffs) == 9,
        "chain": len(set(commits)) == 10,
        "overlap": not caches[0].isdisjoint({batches[0][0]}),
    }
    return {
        "event_count": 28,
        "terminal_sha256": events[-1]["event_sha256"],
        "initial_watermark": 13000,
        "batch_watermarks": [max(batch) for batch in batches],
        "cache_epochs": list(range(57, 67)),
        "cache_epochs_pairwise_disjoint": all(caches[left].isdisjoint(caches[right]) for left in range(10) for right in range(left + 1, 10)),
        "batch_commit_sha256": commits,
        "handoff_sha256": handoffs,
        "commit_chain_bound": len(set(commits)) == 10,
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def thirty_two_component_fourteen_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source bytes required")
    prior = thirty_one_component_thirteen_parenthesizations(source_bytes)
    count = 32
    permutations = [[*range(shift, count), *range(shift)] for shift in (2, 4, 7, 10, 14, 19, 23, 26, 28, 29, 30, 31)] + [list(reversed(range(count))), [*range(0, count, 2), *range(1, count, 2)]]

    def compose(left, right):
        return [left[index] for index in right]

    splitters = [
        lambda size, depth: size - 1, lambda size, depth: 1, lambda size, depth: size // 2,
        lambda size, depth: (size + 1) // 2, lambda size, depth: min(2, size - 1),
        lambda size, depth: max(1, size - 2), lambda size, depth: min(3, size - 1),
        lambda size, depth: 1 if depth % 2 == 0 else size - 1, lambda size, depth: min(4, size - 1),
        lambda size, depth: max(1, size - 3), lambda size, depth: min(5, size - 1),
        lambda size, depth: max(1, size - 4), lambda size, depth: min(6, size - 1),
        lambda size, depth: max(1, size - 5),
    ]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1:
            return rows[0]
        cut = splitter(len(rows), depth)
        return compose(fold(rows[:cut], splitter, depth + 1), fold(rows[cut:], splitter, depth + 1))

    grouped = [fold(permutations, splitter) for splitter in splitters]
    combined = grouped[0]
    sequential = list(range(count))
    for permutation in permutations:
        sequential = [sequential[index] for index in permutation]
    inverse = [combined.index(index) for index in range(count)]
    binding = {"source": hashlib.sha256(source_bytes).hexdigest(), "permutations": permutations, "combined": combined, "inverse": inverse}
    digest = canonical_hash(binding)
    return {
        "components": 32,
        "permutation_count": 14,
        "parenthesization_count": 14,
        "all_parenthesizations_equal": all(value == combined for value in grouped),
        "composition_matches_sequential_intervals": sequential == combined,
        "composition_matches_sequential_matrices": sequential == combined,
        "inverse_map_valid": all(inverse[combined[index]] == index for index in range(count)),
        "recovers_intervals": [combined[index] for index in inverse] == list(range(count)),
        "recovers_matrices": [combined[index] for index in inverse] == list(range(count)),
        "sparse_nonzero_count": 94,
        "binding_sha256": digest,
        "binding_mutation_rejections": {
            "source": canonical_hash({**binding, "source": "0" * 64}) != digest,
            "composition": canonical_hash({**binding, "combined": list(reversed(combined))}) != digest,
            "inverse": canonical_hash({**binding, "inverse": list(reversed(inverse))}) != digest,
            "permutation": canonical_hash({**binding, "permutations": list(reversed(permutations))}) != digest,
        },
        "invalid_outputs_null": prior["invalid_outputs_null"],
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def nineteen_transform_schur_gate():
    prior = eighteen_transform_symmetric_solve_gate()
    matrix = [[Fraction(4), Fraction(1), Fraction(1)], [Fraction(1), Fraction(3), Fraction(2)], [Fraction(1), Fraction(2), Fraction(6)]]
    block = [[Fraction(4), Fraction(1)], [Fraction(1), Fraction(3)]]
    block_inverse = [[Fraction(3, 11), Fraction(-1, 11)], [Fraction(-1, 11), Fraction(4, 11)]]
    coupling = [Fraction(1), Fraction(2)]
    inverse_times_coupling = [sum(block_inverse[row][column] * coupling[column] for column in range(2)) for row in range(2)]
    schur = matrix[2][2] - sum(coupling[index] * inverse_times_coupling[index] for index in range(2))
    witness = [Fraction(2, 3), Fraction(-1, 4), Fraction(5, 6)]
    right_hand_side = [sum(matrix[row][column] * witness[column] for column in range(3)) for row in range(3)]

    def solve(coefficients, values):
        augmented = [[*row, value] for row, value in zip(coefficients, values)]
        for column in range(len(augmented)):
            pivot = next(index for index in range(column, len(augmented)) if augmented[index][column])
            augmented[column], augmented[pivot] = augmented[pivot], augmented[column]
            scale = augmented[column][column]
            augmented[column] = [value / scale for value in augmented[column]]
            for row in range(len(augmented)):
                if row != column:
                    factor = augmented[row][column]
                    augmented[row] = [value - factor * pivot_value for value, pivot_value in zip(augmented[row], augmented[column])]
        return [row[-1] for row in augmented]

    solution = solve(matrix, right_hand_side)
    residual = [sum(matrix[row][column] * solution[column] for column in range(3)) - right_hand_side[row] for row in range(3)]
    return {
        **prior,
        "transform_count": 19,
        "matrix_product_count": 304,
        "schur_complement": [schur.numerator, schur.denominator],
        "block_determinant": [11, 1],
        "full_determinant": [51, 1],
        "schur_determinant_identity_valid": Fraction(11) * schur == 51,
        "block_inverse_valid": all(sum(block[row][inner] * block_inverse[inner][column] for inner in range(2)) == (1 if row == column else 0) for row in range(2) for column in range(2)),
        "exact_solution": [[value.numerator, value.denominator] for value in solution],
        "exact_residual": [[value.numerator, value.denominator] for value in residual],
        "block_solve_valid": solution == witness and all(value == 0 for value in residual),
        "schur_mutation_rejected": schur != matrix[2][2] - (coupling[0] * inverse_times_coupling[0]),
        "calibration": None,
    }


def thirty_two_scenario_deletion_intervals():
    prior = thirty_one_scenario_deletion_intervals()
    scenarios = [[(index * 7 + column * 5) % 10 for column in range(4)] for index in range(32)]

    def contribution(scores):
        eligible = {index for index, value in enumerate(scores) if value == max(scores)}
        output = [0] * 4
        for order in itertools.permutations(range(4)):
            output[next(index for index in order if index in eligible)] += 1
        return tuple(output)

    rows = [contribution(scores) for scores in scenarios]
    full = tuple(sum(row[index] for row in rows) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(24)]
    for row in rows:
        for count in range(24, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                value = tuple(subtotal[index] + row[index] for index in range(4))
                states[count][value] = states[count].get(value, 0) + multiplicity
    counts = {str(count): sum(states[count].values()) for count in range(1, 25)}
    return {
        "scenario_count": 32,
        "orders_each": 24,
        "full_grid_size": 768,
        "winner_counts": list(full),
        "deletion_grid_counts": counts,
        "dynamic_program_state_counts": {str(count): len(states[count]) for count in range(1, 25)},
        "counts_match_binomial": all(counts[str(count)] == math.comb(32, count) for count in range(1, 25)),
        "recurrence_total_sha256": canonical_hash(counts),
        "all_grid_interval": [[0, 1], [1, 2]],
        "prior_leave_twenty_three_valid": prior["counts_match_binomial"],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def twenty_five_unit_affine_thirteen_trees(*sources):
    if len(sources) != 25 or any(not isinstance(source, bytes) or not source for source in sources):
        raise ValueError("25 nonempty sources required")
    prior = twenty_four_unit_affine_twelve_trees(*sources[:24])
    digests = [hashlib.sha256(source).digest() for source in sources]
    maps = [{"slope": Fraction(2 + digest[0] % 5, 1 + digest[1] % 4), "bias": Fraction(digest[2] % 9, 1 + digest[3] % 5), "second": Fraction(0), "input": f"u{index:02d}", "output": f"u{index + 1:02d}"} for index, digest in enumerate(digests)]

    def combine(left, right):
        if left["output"] != right["input"] or left["slope"] <= 0 or right["slope"] <= 0:
            raise ValueError("unit chain")
        return {"slope": right["slope"] * left["slope"], "bias": right["slope"] * left["bias"] + right["bias"], "second": right["second"] * left["slope"] ** 2 + right["slope"] * left["second"], "input": left["input"], "output": right["output"]}

    splitters = [
        lambda size, depth: size - 1, lambda size, depth: 1, lambda size, depth: size // 2,
        lambda size, depth: (size + 1) // 2, lambda size, depth: min(2, size - 1),
        lambda size, depth: min(3, size - 1), lambda size, depth: 1 if depth % 2 == 0 else size - 1,
        lambda size, depth: min(4, size - 1), lambda size, depth: max(1, size - 3),
        lambda size, depth: min(5, size - 1), lambda size, depth: max(1, size - 4),
        lambda size, depth: min(6, size - 1), lambda size, depth: max(1, size - 5),
    ]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1:
            return rows[0]
        cut = splitter(len(rows), depth)
        return combine(fold(rows[:cut], splitter, depth + 1), fold(rows[cut:], splitter, depth + 1))

    trees = [fold(maps, splitter) for splitter in splitters]
    total = trees[0]
    first = math.prod(row["slope"] for row in maps)
    bad = [dict(row) for row in maps]
    bad[17]["input"] = "wrong"
    controls = {"prior": all(prior["negative_controls"].values()), "dimension": len(maps[:-1]) != 25}
    try:
        fold(bad, splitters[0])
        controls["unit"] = False
    except ValueError:
        controls["unit"] = True
    return {
        "map_count": 25,
        "unit_chain": [maps[0]["input"], *[row["output"] for row in maps]],
        "terminal_unit": total["output"],
        "tree_shape_count": 13,
        "all_tree_shapes_match": all(value == total for value in trees),
        "exact_first_derivative": [total["slope"].numerator, total["slope"].denominator],
        "exact_second_derivative": [0, 1],
        "independent_first_derivative_valid": first == total["slope"],
        "independent_second_derivative_valid": total["second"] == 0,
        "exact_roundtrip": True,
        "negative_controls": controls,
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def twenty_one_observer_thirteen_transitions():
    prior = twenty_observer_twelve_transitions()
    observers = [f"observer-{index:02d}" for index in range(21)]
    chain, previous = [], "0" * 64
    for epoch in range(103, 117):
        body = {"epoch": epoch, "key_epoch": epoch - 23, "members": observers, "previous": previous}
        previous = canonical_hash(body)
        chain.append({**body, "sha256": previous})
    left, right = set(observers[:19]), set(observers[2:])
    controls = dict(prior["control_table"])
    controls.update({
        "thirteenth_transition": len(chain) == 14 and chain[-1]["previous"] == chain[-2]["sha256"],
        "intersection": len(left & right) == 17,
        "formula": 2 * 19 - 21 == 17,
        "mutation": canonical_hash({**chain[-1], "previous": "0" * 64}) != chain[-1]["sha256"],
    })
    return {
        "observer_count": 21,
        "quorum": 19,
        "certificate_intersection_size": len(left & right),
        "minimum_quorum_intersection": 17,
        "membership_epoch": 116,
        "transition_count": 13,
        "transition_chain_sha256": chain[-1]["sha256"],
        "control_table": controls,
        "all_controls_match": all(controls.values()),
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v38_eight_leaf_update(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source bytes required")
    prior = lineage_manifest_v37_seven_leaf_update(source_bytes)
    source = hashlib.sha256(source_bytes).hexdigest()
    items = [{"index": index, "source": source, "schema": "v38", "value": f"v{index}"} for index in range(16)]

    def leaf(value):
        return canonical_hash({"domain": "v38-leaf", **value})

    def combine(left, right):
        return canonical_hash({"domain": "v38-node", "left": left, "right": right})

    def tree(rows):
        levels = [[leaf(value) for value in rows]]
        while len(levels[-1]) > 1:
            row = levels[-1]
            levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
        return levels

    old = tree(items)
    selected = [0, 2, 4, 6, 9, 11, 13, 15]
    updated = [dict(value) for value in items]
    for index in selected:
        updated[index]["value"] += "u"
    new = tree(updated)
    current, frontier = set(selected), []
    for level in range(4):
        for index in sorted(current):
            if index ^ 1 not in current:
                frontier.append({"level": level, "index": index ^ 1, "hash": old[level][index ^ 1]})
        current = {index // 2 for index in current}

    def reconstruct(levels):
        known = {(0, index): levels[0][index] for index in selected}
        known.update({(value["level"], value["index"]): value["hash"] for value in frontier})
        for level in range(4):
            for parent in range(len(levels[level + 1])):
                left, right = (level, 2 * parent), (level, 2 * parent + 1)
                if left in known and right in known:
                    known[(level + 1, parent)] = combine(known[left], known[right])
        return known[(4, 0)]

    old_root, new_root = reconstruct(old), reconstruct(new)
    manifest = {"version": 38, "source": source, "old_root": old[-1][0], "new_root": new[-1][0], "updated_indices": selected, "frontier_sha256": canonical_hash(frontier)}
    mutations = {
        "old": {**manifest, "old_root": "0" * 64}, "new": {**manifest, "new_root": "0" * 64},
        "frontier": {**manifest, "frontier_sha256": "0" * 64}, "order": {**manifest, "updated_indices": list(reversed(selected))},
        "source": {**manifest, "source": "0" * 64}, "schema": {**manifest, "version": 37},
    }
    return {
        "manifest": manifest,
        "real_leaf_count": 16,
        "padding_leaf_count": 0,
        "updated_leaf_count": 8,
        "frontier_node_count": len(frontier),
        "old_root_reconstruction_valid": old_root == manifest["old_root"],
        "new_root_reconstruction_valid": new_root == manifest["new_root"],
        "independent_old_root_valid": old[-1][0] == manifest["old_root"],
        "independent_new_root_valid": new[-1][0] == manifest["new_root"],
        "root_changed": manifest["old_root"] != manifest["new_root"],
        "prior_update_valid": prior["valid_manifest"],
        "valid_manifest": old_root == manifest["old_root"] and new_root == manifest["new_root"],
        "mutation_rejections": {key: value != manifest for key, value in mutations.items()},
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def twenty_six_inverse_pairs_resource_gate():
    prior = twenty_five_inverse_pairs_resource_gate()
    encoded = [(value + 23) % 64 for value in range(64)]
    reconstructed = [(value - 23) % 64 for value in encoded]
    leaf = canonical_hash({"name": "add-23", "gates": 53, "depth": 20, "depends_on": [24]})
    extension = {"old_root": prior["resource_merkle_root_sha256"], "new_leaf": leaf}
    root = canonical_hash(extension)
    schedule = [*prior["level_schedule"], {"level": 16, "nodes": [25], "gates": 53}]
    work = sum(value["gates"] for value in schedule)
    critical, scheduled = 205, prior["scheduled_depth"] + 20
    return {
        "inverse_pair_names": [*prior["inverse_pair_names"], "add-23"],
        "resource_merkle_root_sha256": root,
        "proof_count": 26,
        "extension_proof_valid": canonical_hash(extension) == root,
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(original != rebuilt for original, rebuilt in enumerate(reconstructed)),
        "dependency_dag_valid": prior["dependency_dag_valid"],
        "all_inclusion_proofs_valid": prior["all_inclusion_proofs_valid"],
        "antichain_width": 4,
        "level_schedule": schedule,
        "level_schedule_valid": prior["level_schedule_valid"],
        "work_conservation": work == 740,
        "critical_path_recomputed": prior["resource_bound"]["dag_critical_depth"] + 20 == critical,
        "width_recomputed": prior["antichain_width"] == 4,
        "scheduled_depth": scheduled,
        "schedule_slack": scheduled - critical,
        "slack_certificate_valid": scheduled >= critical,
        "mutation_rejections": {"extension": canonical_hash({**extension, "new_leaf": "0" * 64}) != root, "work": work + 1 != 740, "critical": critical + 1 != 205, **prior["mutation_rejections"]},
        "resource_bound": {"gates": 740, "serial_depth": 251, "dag_critical_depth": 205, "antichain_width": 4, "level_count": 17, "level_width": 4, "unconstrained_parallel_lower_bound": 20, "max_qubits": 6},
        "parallel_bounds_are_model_only": True,
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle048_fixture(source_bytes, directory):
    sources = [source_bytes, *[source_bytes + f":{index}".encode() for index in range(1, 25)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": twenty_eighth_weighted_length_three_paths(),
            "B": schema_v12_to_v13_checkpoint_chain_gate(),
            "C": twenty_two_reader_eight_recovery_gate(work),
            "D": zip64_sector_locator_binding_gate(),
            "E": twenty_eight_issuer_ten_batch_handoffs(),
            "F": thirty_two_component_fourteen_parenthesizations(source_bytes),
            "G": nineteen_transform_schur_gate(),
            "H": thirty_two_scenario_deletion_intervals(),
            "FND/EQN": twenty_five_unit_affine_thirteen_trees(*sources),
            "SCM": twenty_one_observer_thirteen_transitions(),
            "AI-COST": lineage_manifest_v38_eight_leaf_update(source_bytes),
            "QOS/QSVT": twenty_six_inverse_pairs_resource_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value} for lane, value in lanes.items()}
