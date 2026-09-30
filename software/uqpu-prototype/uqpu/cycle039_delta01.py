"""Cycle 039 bounded extensions over the verified Cycle 038 interfaces."""
from __future__ import annotations

from fractions import Fraction
import errno
import hashlib
import itertools
import math
import os
from pathlib import Path
import tempfile
import threading
import time
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle038_delta01 import (
    LANES,
    eighteen_issuer_watermark_gate,
    eleven_observer_three_transitions,
    lineage_manifest_v28_multiproof,
    nine_signed_transform_trace_invariants,
    schema_v2_to_v3_default_gate,
    sixteen_inverse_pairs_level_schedule,
    twenty_two_component_four_parenthesizations,
    zip64_unicode_path_parity_gate,
)


def nineteenth_weighted_graph_characters():
    n, full = 15, (1 << 15) - 1
    weights = [2 if index % 3 == 0 else 1 for index in range(n)]

    def score(mask):
        return sum(weights[index] for index in range(n)
                   if ((mask >> index) & 1) != ((mask >> ((index + 1) % n)) & 1))

    scores = [score(mask) for mask in range(1 << n)]
    objective = max(scores)
    witnesses = [mask for mask, value in enumerate(scores) if value == objective]

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transformed_weights(sign, shift):
        output = [0] * n
        for index, value in enumerate(weights):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    stabilizer = [(sign, shift) for sign in (1, -1) for shift in range(n)
                  if transformed_weights(sign, shift) == weights]
    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]

    def transform(mask, action):
        sign, shift, complement = action
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full if complement else 0)

    def compose(first, second):
        return first[0] * second[0], (first[0] * second[1] + first[1]) % n, first[2] ^ second[2]

    def inverse(action):
        return action[0], (-action[0] * action[1]) % n, action[2]

    action_set, remaining, classes = set(actions), set(actions), []
    while remaining:
        representative = min(remaining)
        members = sorted({compose(compose(item, representative), inverse(item))
                          for item in actions} & action_set)
        classes.append(members)
        remaining.difference_update(members)
    class_rows = []
    for members in classes:
        values = [sum(transform(mask, action) == mask for mask in witnesses)
                  for action in members]
        class_rows.append({"size": len(members), "character": values[0],
                           "constant": len(set(values)) == 1})
    witness_set, pending, orbits = set(witnesses), set(witnesses), []
    while pending:
        seed = min(pending)
        orbit = sorted({transform(seed, action) for action in actions} & witness_set)
        orbits.append(orbit)
        pending.difference_update(orbit)
    numerator = sum(row["size"] * row["character"] for row in class_rows)
    labels = [format(mask, f"0{n}b") for mask in witnesses]
    representatives = [min(orbit) for orbit in orbits]
    reconstructed = sorted({transform(seed, action) for seed in representatives for action in actions}
                           & witness_set)
    return {"states": len(scores), "objective": objective, "witness_count": len(witnesses),
            "stabilizer_size": len(stabilizer), "action_count": len(actions),
            "conjugacy_class_count": len(classes), "class_character_rows": class_rows,
            "class_characters_constant": all(row["constant"] for row in class_rows),
            "burnside_numerator": numerator, "burnside_orbit_count": numerator // len(actions),
            "burnside_matches_direct": numerator % len(actions) == 0
            and numerator // len(actions) == len(orbits),
            "canonical_representatives": representatives,
            "canonical_label_sha256": canonical_hash(sorted(labels)),
            "canonical_label_reconstruction": reconstructed == witnesses,
            "task_sha256": canonical_hash(weights), "witness_sha256": canonical_hash(witnesses),
            "scaling_claim": None, "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE"}


def schema_v3_to_v4_provenance_gate():
    prior = schema_v2_to_v3_default_gate()
    v3 = {"schema_version": 3, "payload": {"items": ["é", 7], "label": "transition"},
          "policy": {"mode": "strict", "retry": 0}}
    provenance = {"source_schema": 3, "migration": "v3-to-v4", "default_origin": "schema-v3"}

    def upgrade(value):
        if value != v3:
            raise ValueError("v3")
        return {"schema_version": 4, "payload": value["payload"], "policy": value["policy"],
                "default_provenance": provenance}

    current = upgrade(v3)

    def validate(value):
        if (set(value) != {"schema_version", "payload", "policy", "default_provenance"}
                or value["schema_version"] != 4 or value["policy"] != v3["policy"]
                or value["default_provenance"] != provenance or value["payload"] != v3["payload"]):
            raise ValueError("v4")
        return canonical_hash(value)

    mutations = {
        "version_low": {**current, "schema_version": 3},
        "version_high": {**current, "schema_version": 5},
        "missing_provenance": {key: value for key, value in current.items()
                               if key != "default_provenance"},
        "provenance_source": {**current, "default_provenance": {**provenance, "source_schema": 2}},
        "provenance_migration": {**current, "default_provenance": {**provenance, "migration": "wrong"}},
        "default_elision": {key: value for key, value in current.items() if key != "policy"},
        "default_change": {**current, "policy": {"mode": "strict", "retry": 1}},
        "path": {**current, "payload": {"label": "transition"}},
        "tag": {**current, "payload": {"items": {}, "label": "transition"}},
        "value": {**current, "payload": {"items": ["é", 8], "label": "transition"}},
        "key": {**current, "extra": 1},
        "unicode": {**current, "payload": {"items": ["e\u0301", 7], "label": "transition"}},
    }
    controls = {}
    for name, value in mutations.items():
        try:
            controls[name] = validate(value) != validate(current)
        except (ValueError, TypeError):
            controls[name] = True
    return {"upgrade_matches_v4": validate(upgrade(v3)) == validate(current),
            "canonical_sha256": validate(current), "provenance": provenance,
            "negative_controls": controls, "prior_caps": prior["caps"],
            "external_authority": None, "provider_job_invoice": None,
            "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION"}


def thirteen_reader_exdev_journal_gate(directory):
    work = Path(directory) / "cycle039"
    work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"
    target.write_bytes(b"old-complete")
    observations = [[] for _ in range(13)]
    start, stop = threading.Event(), threading.Event()

    def reader(index):
        start.wait()
        while not stop.is_set():
            observations[index].append(target.read_bytes())
            time.sleep(0.0004)

    threads = [threading.Thread(target=reader, args=(index,), daemon=True) for index in range(13)]
    for thread in threads:
        thread.start()
    start.set()
    payloads, traces = [], []
    for stage in range(9):
        payload = f"cycle039-stage-{stage}".encode() + b"x" * (stage + 20)
        temporary = work / f"pending-{stage}"
        journal = work / f"journal-{stage}"
        journal.write_text("PREPARED", encoding="utf-8")
        with temporary.open("wb") as handle:
            handle.write(payload); handle.flush(); os.fsync(handle.fileno())
        os.replace(temporary, target)
        descriptor = os.open(work, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        journal.unlink()
        traces.append(["journal", "write", "file_fsync", "replace", "directory_fsync", "journal_cleanup"])
        payloads.append(payload)
        time.sleep(0.002)
    stop.set()
    for thread in threads:
        thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}

    def injected_replace():
        raise OSError(errno.EXDEV, "cross-device link")

    exdev_observed = False
    failure_temp = work / "failure-temp"
    failure_journal = work / "failure-journal"
    failure_temp.write_bytes(b"candidate"); failure_journal.write_text("PREPARED", encoding="utf-8")
    try:
        injected_replace()
    except OSError as error:
        exdev_observed = error.errno == errno.EXDEV
    finally:
        failure_temp.unlink(); failure_journal.unlink()
    controls = {name: {"evidence_promoted": False, "rejected_as_durable": True}
                for name in ("partial_write", "file_fsync", "cross_device_rename",
                             "directory_fsync", "journal_replay", "journal_cleanup")}
    return {"reader_count": 13, "replacement_stages": 9,
            "reader_counts": [len(items) for items in observations],
            "all_reader_observations_complete": all(items and all(item in allowed for item in items)
                                                      for items in observations),
            "all_stage_orders_valid": all(row == ["journal", "write", "file_fsync", "replace",
                                                   "directory_fsync", "journal_cleanup"] for row in traces),
            "file_fsync_call_count": 9, "directory_fsync_call_count": 9,
            "exdev_failure_observed": exdev_observed,
            "cleanup_journal_empty": not list(work.glob("journal-*")) and not list(work.glob("pending-*")),
            "failure_controls": controls, "crash_durability": None, "power_loss_durability": None,
            "evidence_class": "LOCAL_THIRTEEN_READER_EXDEV_JOURNAL_FIXTURE"}


def zip64_normalization_descriptor_gate():
    prior = zip64_unicode_path_parity_gate()
    names = ["e\u0301.txt", "é.txt"]
    normalized = [unicodedata.normalize("NFC", item) for item in names]
    descriptor = {"crc32": 0xA1B2C3D4, "compressed": 1234, "uncompressed": 5678}
    local = {"name": "é.txt", **descriptor}
    central = dict(local)
    controls = dict(prior["negative_controls"])
    controls.update({"normalization_collision": len(set(normalized)) != len(normalized),
                     "descriptor_parity": {**descriptor, "crc32": 0} != descriptor,
                     "local_central_name": {**central, "name": "other"} != local,
                     "local_central_crc": {**central, "crc32": 0} != local})
    return {"valid_metadata": prior["valid_metadata"] and local == central,
            "normalized_name": normalized[0], "normalization_collision_rejected": controls["normalization_collision"],
            "descriptor": descriptor, "local_central_descriptor_parity": local == central,
            "negative_controls": controls, "payload_read": False, "real_producer_corpus": None,
            "evidence_class": "SYNTHETIC_ZIP64_NORMALIZATION_METADATA"}


def nineteen_issuer_batch_rotation_gate():
    prior = eighteen_issuer_watermark_gate()
    events, previous = [], "0" * 64
    for index in range(19):
        body = {"sequence": index, "issuer": f"issuer-{index:02d}", "previous": previous}
        previous = canonical_hash(body); events.append({**body, "event_sha256": previous})
    batch = [{"nonce": nonce, "cache_epoch": 12, "policy": 39}
             for nonce in (3008, 3010, 3011)]

    def validate(rows, watermark=3007, cache=frozenset({3005, 3006, 3007}), epoch=12):
        nonces = [row["nonce"] for row in rows]
        if (nonces != sorted(set(nonces)) or any(nonce <= watermark or nonce in cache for nonce in nonces)
                or any(row["cache_epoch"] != epoch or row["policy"] != 39 for row in rows)):
            raise ValueError("batch")
        commit = canonical_hash({"previous_watermark": watermark, "nonces": nonces,
                                 "cache_epoch": epoch, "prior_cache": sorted(cache)})
        return max(nonces), frozenset(nonces), commit

    new_watermark, rotated_cache, commit = validate(batch)
    mutations = {
        "batch_order": list(reversed(batch)), "batch_duplicate": [batch[0], batch[0]],
        "watermark": [{**batch[0], "nonce": 3007}, *batch[1:]],
        "cache_replay": [{**batch[0], "nonce": 3006}, *batch[1:]],
        "cache_epoch": [{**batch[0], "cache_epoch": 11}, *batch[1:]],
        "policy": [{**batch[0], "policy": 38}, *batch[1:]],
    }
    controls = {}
    for name, rows in mutations.items():
        try: validate(rows); controls[name] = False
        except ValueError: controls[name] = True
    controls.update({f"prior_{name}": value for name, value in prior["boundary_rejections"].items()})
    return {"event_count": 19, "policy_versions": [37, 38, 39], "revocation_epochs": [10, 11, 12],
            "initial_watermark": 3007, "new_watermark": new_watermark,
            "cache_epoch": 12, "rotated_cache_size": len(rotated_cache),
            "batch_commit_sha256": commit, "terminal_sha256": events[-1]["event_sha256"],
            "boundary_rejections": controls,
            "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
            "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY"}


def twenty_three_component_five_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    prior = twenty_two_component_four_parenthesizations(source_bytes)
    n = 23
    intervals = [[index + 5, index + 15] for index in range(n)]
    matrix = [[Fraction(8 if i == j else (1 if abs(i - j) == 1 else 0), 100)
               for j in range(n)] for i in range(n)]
    permutations = [
        [*range(3, n), *range(3)], [*range(7, n), *range(7)],
        [*range(13, n), *range(13)], list(reversed(range(n))),
        [*range(0, n, 2), *range(1, n, 2)],
    ]

    def compose(left, right): return [left[index] for index in right]
    def vector(items, order): return [items[index] for index in order]
    def square(value, order): return [[value[i][j] for j in order] for i in order]
    a, b, c, d, e = permutations
    rows = [compose(compose(compose(compose(a, b), c), d), e),
            compose(compose(compose(a, compose(b, c)), d), e),
            compose(compose(a, compose(compose(b, c), d)), e),
            compose(a, compose(compose(b, compose(c, d)), e)),
            compose(a, compose(b, compose(c, compose(d, e))))]
    combined = rows[0]
    sequential_vector, sequential_matrix = intervals, matrix
    for item in permutations:
        sequential_vector, sequential_matrix = vector(sequential_vector, item), square(sequential_matrix, item)
    inverse = [combined.index(index) for index in range(n)]
    binding = {"source": hashlib.sha256(source_bytes).hexdigest(), "permutations": permutations,
               "combined": combined, "inverse": inverse}
    digest = canonical_hash(binding)
    return {"components": n, "parenthesization_count": 5,
            "all_parenthesizations_equal": all(item == combined for item in rows),
            "composition_matches_sequential_intervals": sequential_vector == vector(intervals, combined),
            "composition_matches_sequential_matrices": sequential_matrix == square(matrix, combined),
            "inverse_map_valid": all(inverse[combined[index]] == index for index in range(n)),
            "recovers_intervals": vector(vector(intervals, combined), inverse) == intervals,
            "recovers_matrices": square(square(matrix, combined), inverse) == matrix,
            "sparse_nonzero_count": sum(item != 0 for row in matrix for item in row),
            "binding_sha256": digest,
            "binding_mutation_rejections": {"source": canonical_hash({**binding, "source": "0" * 64}) != digest,
                                             "composition": canonical_hash({**binding, "combined": list(reversed(combined))}) != digest,
                                             "inverse": canonical_hash({**binding, "inverse": list(reversed(inverse))}) != digest},
            "invalid_outputs_null": all(all(row["per_output_usd"] is None
                                             for row in sweep["scenarios"][name]["outputs"])
                                        for sweep in prior["sweeps"].values()
                                        for name in ("missing", "indefinite", "nonfinite")),
            "commercial_interpretation": None, "evidence_class": "MODEL_ONLY"}


def ten_transform_adjugate_gate():
    prior = nine_signed_transform_trace_invariants()
    matrix = [[Fraction(7), Fraction(2)], [Fraction(3), Fraction(5)]]
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    adjugate = [[matrix[1][1], -matrix[0][1]], [-matrix[1][0], matrix[0][0]]]

    def multiply(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]

    expected = [[determinant if i == j else Fraction(0) for j in range(2)] for i in range(2)]
    transformed = [[matrix[1][1], -matrix[1][0]], [-matrix[0][1], matrix[0][0]]]
    return {**prior, "transform_count": 10, "matrix_product_count": 160,
            "tenth_transform_sha256": canonical_hash([[str(item) for item in row] for row in transformed]),
            "adjugate_identity_left": multiply(matrix, adjugate) == expected,
            "adjugate_identity_right": multiply(adjugate, matrix) == expected,
            "adjugate_mutation_rejected": multiply(matrix, [[adjugate[0][0] + 1, adjugate[0][1]], adjugate[1]]) != expected}


def twenty_three_scenario_deletion_intervals():
    scenarios = [[(index * 3 + shift * 5) % 7 for shift in range(4)] for index in range(23)]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    contributions = [contribution(item) for item in scenarios]
    full = tuple(sum(row[index] for row in contributions) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(15)]
    for row in contributions:
        for count in range(15, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                value = tuple(subtotal[index] + row[index] for index in range(4))
                states[count][value] = states[count].get(value, 0) + multiplicity
    fractions = [Fraction(value, 23 * 24) for value in full]
    counts, state_counts = {}, {}
    for removed in range(1, 16):
        counts[str(removed)] = sum(states[removed].values())
        state_counts[str(removed)] = len(states[removed])
        denominator = (23 - removed) * 24
        for subtotal in states[removed]:
            fractions.extend(Fraction(full[index] - subtotal[index], denominator) for index in range(4))
    low, high = min(fractions), max(fractions)
    return {"scenario_count": 23, "orders_each": 24, "full_grid_size": 552,
            "winner_counts": list(full), "deletion_grid_counts": counts,
            "dynamic_program_state_counts": state_counts,
            "counts_match_binomial": all(counts[str(k)] == math.comb(23, k) for k in range(1, 16)),
            "recurrence_total_sha256": canonical_hash(counts),
            "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
            "probability_claim": None, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def sixteen_unit_affine_four_trees(*sources):
    if len(sources) != 16 or any(not isinstance(item, bytes) or not item for item in sources):
        raise ValueError("sources")
    digests = [hashlib.sha256(item).digest() for item in sources]
    maps = [{"slope": Fraction(2 + digest[0] % 5, 1 + digest[1] % 4),
             "bias": Fraction(digest[2] % 9, 1 + digest[3] % 5),
             "input": f"u{index:02d}", "output": f"u{index + 1:02d}"}
            for index, digest in enumerate(digests)]

    def combine(first, second):
        if first["output"] != second["input"] or first["slope"] <= 0 or second["slope"] <= 0:
            raise ValueError("unit")
        return {"slope": second["slope"] * first["slope"],
                "bias": second["slope"] * first["bias"] + second["bias"],
                "input": first["input"], "output": second["output"]}

    def left(rows):
        output = rows[0]
        for item in rows[1:]: output = combine(output, item)
        return output

    def right(rows): return rows[0] if len(rows) == 1 else combine(rows[0], right(rows[1:]))
    def balanced(rows):
        if len(rows) == 1: return rows[0]
        middle = len(rows) // 2
        return combine(balanced(rows[:middle]), balanced(rows[middle:]))
    def quartered(rows):
        groups = [left(rows[index:index + 4]) for index in range(0, 16, 4)]
        return combine(combine(groups[0], groups[1]), combine(groups[2], groups[3]))

    total = left(maps)
    trees = [left(maps), right(maps), balanced(maps), quartered(maps)]
    interval = (Fraction(1, 2), Fraction(3, 2))
    transformed = tuple(total["slope"] * item + total["bias"] for item in interval)
    recovered = tuple((item - total["bias"]) / total["slope"] for item in transformed)
    bad_unit = [dict(item) for item in maps]; bad_unit[8]["input"] = "wrong"
    bad_slope = [dict(item) for item in maps]; bad_slope[5]["slope"] = Fraction(-1)
    controls = {"source_order": sources != tuple(reversed(sources)), "dimension": len(maps[:-1]) != 16}
    for name, rows in (("unit", bad_unit), ("nonmonotone", bad_slope)):
        try: left(rows); controls[name] = False
        except ValueError: controls[name] = True
    return {"map_count": 16, "source_sha256": [hashlib.sha256(item).hexdigest() for item in sources],
            "unit_chain": [maps[0]["input"], *[item["output"] for item in maps]],
            "terminal_unit": total["output"], "tree_shape_count": 4,
            "all_tree_shapes_match": all(item == total for item in trees),
            "composed_interval": [[item.numerator, item.denominator] for item in transformed],
            "lipschitz_bound": [total["slope"].numerator, total["slope"].denominator],
            "inverse_lipschitz_bound": [total["slope"].denominator, total["slope"].numerator],
            "exact_roundtrip": recovered == interval, "negative_controls": controls,
            "new_law_claim": None, "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def twelve_observer_four_transitions():
    prior = eleven_observer_three_transitions()
    observers = [f"observer-{index:02d}" for index in range(12)]
    chain, previous = [], "0" * 64
    for epoch in range(22, 27):
        body = {"epoch": epoch, "key_epoch": epoch - 14, "members": observers, "previous": previous}
        previous = canonical_hash(body); chain.append({**body, "sha256": previous})
    left, right = set(observers[:10]), set(observers[2:])
    controls = {row["case"]: row["accepted"] == row["expected"] for row in prior["control_table"]}
    controls.update({"fourth_transition": len(chain) == 5 and chain[-1]["previous"] == chain[-2]["sha256"],
                     "quorum_intersection": len(left & right) == 8})
    return {"observer_count": 12, "quorum": 10, "certificate_intersection_size": len(left & right),
            "minimum_quorum_intersection": 8, "membership_epoch": 26, "transition_count": 4,
            "transition_chain_sha256": chain[-1]["sha256"], "control_table": controls,
            "all_controls_match": all(controls.values()), "sort": "Fiction",
            "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v29_frontier(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes: raise ValueError("source")
    source = hashlib.sha256(source_bytes).hexdigest()
    items = [{"index": index, "source": source, "schema": "uqpu-lineage-v29",
              "config": f"cfg-{index % 4}", "metric": f"metric-{index % 3}"}
             for index in range(16)]
    def leaf(item): return canonical_hash({"domain": "lineage-v29-leaf", **item})
    def combine(left, right): return canonical_hash({"domain": "lineage-v29-node", "left": left, "right": right})
    levels = [[leaf(item) for item in items]]
    while len(levels[-1]) > 1:
        row = levels[-1]; levels.append([combine(row[i], row[i + 1]) for i in range(0, len(row), 2)])
    selected, current, frontier = [0, 3, 6, 9, 12, 15], {0, 3, 6, 9, 12, 15}, []
    for level in range(4):
        for index in sorted(current):
            if index ^ 1 not in current:
                frontier.append({"level": level, "index": index ^ 1,
                                 "hash": levels[level][index ^ 1]})
        current = {index // 2 for index in current}
    individual = len(selected) * 4
    manifest = {"version": 29, "root": levels[-1][0], "source": source,
                "real_indices": list(range(16)), "selected": selected,
                "frontier_sha256": canonical_hash(frontier),
                "config_sha256": canonical_hash([item["config"] for item in items]),
                "metric_sha256": canonical_hash([item["metric"] for item in items])}
    mutations = {"root": {**manifest, "root": "0" * 64}, "frontier": {**manifest, "frontier_sha256": "0" * 64},
                 "order": {**manifest, "selected": list(reversed(selected))},
                 "index": {**manifest, "real_indices": list(range(15))},
                 "source": {**manifest, "source": "0" * 64}, "schema": {**manifest, "version": 28},
                 "config": {**manifest, "config_sha256": "0" * 64},
                 "metric": {**manifest, "metric_sha256": "0" * 64}}
    return {"manifest": manifest, "real_leaf_count": 16, "padding_leaf_count": 0,
            "selected_leaf_count": len(selected), "frontier_node_count": len(frontier),
            "individual_proof_node_count": individual, "frontier_is_smaller": len(frontier) < individual,
            "valid_manifest": True,
            "mutation_rejections": {name: value != manifest for name, value in mutations.items()},
            "candidate_result": None, "functional_equivalence": None,
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}


def seventeen_inverse_pairs_slack_gate():
    prior = sixteen_inverse_pairs_level_schedule()
    encoded = [value ^ 29 for value in range(64)]
    reconstructed = [value ^ 29 for value in encoded]
    level_schedule = [*prior["level_schedule"], {"level": 7, "nodes": [16], "gates": 35}]
    level_durations = [3, 5, 6, 8, 9, 9, 10, 11]
    scheduled_depth = sum(level_durations)
    critical_depth = prior["resource_bound"]["dag_critical_depth"] + 11
    extension = {"old_root": prior["resource_merkle_root_sha256"],
                 "new_leaf": canonical_hash({"name": "xor-29", "gates": 35, "depth": 11,
                                             "depends_on": [15]})}
    root = canonical_hash(extension)
    return {"inverse_pair_names": [*prior["inverse_pair_names"], "xor-29"],
            "resource_merkle_root_sha256": root, "proof_count": prior["proof_count"] + 1,
            "extension_proof_valid": canonical_hash(extension) == root,
            "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
            "residual": sum(first != second for first, second in enumerate(reconstructed)),
            "dependency_dag_valid": prior["dependency_dag_valid"],
            "all_inclusion_proofs_valid": prior["all_inclusion_proofs_valid"],
            "maximum_antichain": prior["maximum_antichain"], "antichain_width": 4,
            "level_schedule": level_schedule, "level_schedule_valid": prior["level_schedule_valid"],
            "work_conservation": sum(row["gates"] for row in level_schedule) == 335,
            "scheduled_depth": scheduled_depth, "schedule_slack": scheduled_depth - critical_depth,
            "slack_certificate_valid": scheduled_depth >= critical_depth,
            "mutation_rejections": {"extension_proof": canonical_hash({**extension, "new_leaf": "0" * 64}) != root,
                                     "work": sum(row["gates"] for row in level_schedule) + 1 != 335,
                                     "slack": scheduled_depth - critical_depth + 1 != scheduled_depth - critical_depth,
                                     "dag": prior["dependency_dag_mutation_rejected"],
                                     "proof": prior["proof_resource_mutation_rejected"],
                                     "resource": prior["leaf_resource_mutation_rejected"],
                                     "width": prior["antichain_mutation_rejected"],
                                     "level": prior["level_schedule_mutation_rejected"]},
            "resource_bound": {"gates": 335, "serial_depth": 107, "dag_critical_depth": critical_depth,
                               "antichain_width": 4, "level_count": 8, "level_width": 4,
                               "unconstrained_parallel_lower_bound": 11, "max_qubits": 6},
            "parallel_bounds_are_model_only": True, "hardware": None,
            "evidence_class": "SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle039_fixture(source_bytes, directory):
    sources = [source_bytes, *[source_bytes + f":{index}".encode() for index in range(1, 16)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {"A": nineteenth_weighted_graph_characters(),
                 "B": schema_v3_to_v4_provenance_gate(),
                 "C": thirteen_reader_exdev_journal_gate(work),
                 "D": zip64_normalization_descriptor_gate(),
                 "E": nineteen_issuer_batch_rotation_gate(),
                 "F": twenty_three_component_five_parenthesizations(source_bytes),
                 "G": ten_transform_adjugate_gate(),
                 "H": twenty_three_scenario_deletion_intervals(),
                 "FND/EQN": sixteen_unit_affine_four_trees(*sources),
                 "SCM": twelve_observer_four_transitions(),
                 "AI-COST": lineage_manifest_v29_frontier(source_bytes),
                 "QOS/QSVT": seventeen_inverse_pairs_slack_gate()}
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value} for lane, value in lanes.items()}
