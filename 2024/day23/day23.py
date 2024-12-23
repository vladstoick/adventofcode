from pathlib import Path
from collections import defaultdict
from itertools import combinations
from functools import cache

file = open(Path(__file__).with_name("input.txt"))
connections = defaultdict(lambda: set())

for line in file.readlines():
    l, r = line.strip().split("-")
    connections[l].add(r)
    connections[r].add(l)

part1_options = set()
for key in connections.keys():
    if key.startswith("t"):
        for (a, b) in combinations(connections[key], 2):
            if b in connections[a]:
                part1_options.add(frozenset([a, b, key]))
print("Part 1", len(part1_options))


@cache
def is_connected(node, existing_set):
    return existing_set.issubset(connections[node])


@cache
def expand(existing_set):
    max_set = existing_set

    for key in existing_set:
        for new_key in connections[key]:
            if new_key not in existing_set:
                if is_connected(new_key, existing_set):
                    new_set = frozenset([new_key] + list(existing_set))
                    new_set_expanded = expand(new_set)
                    if len(new_set_expanded) > len(max_set):
                        max_set = new_set_expanded

    return max_set


def det_max_set(connections):
    max_set = None
    for key in connections:
        opt = expand(frozenset([key]))
        if max_set is None or len(opt) > len(max_set):
            max_set = opt
    return max_set


print("Part 2", ",".join(sorted(det_max_set(connections))))
