from collections import defaultdict
from pathlib import Path
import queue

p = Path(__file__).with_name("input.txt")
file = open(p)

deps_orig = defaultdict(lambda: set())
deps_reversed_orig = defaultdict(lambda: set())
updates = []

for line in file.readlines():
    if line.count("|"):
        [a, b] = map(int, line.split("|"))
        deps_orig[a].add(b)
        deps_reversed_orig[b].add(a)
    elif line.count(","):
        updates.append(list(map(int, line.split(","))))


def part1(update):
    so_far = set()
    works = True

    for page in update:
        for dep in deps_orig[page]:
            if dep in so_far:
                works = False
                break
        if not works:
            break
        so_far.add(page)

    return update[len(update) // 2] if works else 0


def create_copy(update):
    deps = defaultdict(lambda: set())
    deps_reversed = defaultdict(lambda: set())
    for page in update:
        for dep in deps_orig[page]:
            if dep in update:
                deps[page].add(dep)
        for dep in deps_reversed_orig[page]:
            if dep in update:
                deps_reversed[page].add(dep)

    return (deps, deps_reversed)


def part2(update):
    if part1(update):
        return 0

    (deps, deps_reversed) = create_copy(update)

    def has_dep_in_update(page):
        return len(deps_reversed[page]) > 0

    def order_by_pos_in_update(to_add):
        return sorted(to_add, key=lambda x: update.index(x))

    output = []
    q = queue.Queue()
    v = set()

    def add_without_deps():
        to_add = []
        for page in update:
            if not has_dep_in_update(page) and page not in v:
                to_add.append(page)
                v.add(page)
        to_add = order_by_pos_in_update(to_add)
        [q.put(x) for x in to_add]

    add_without_deps()

    while not q.empty():
        processing_page = q.get()
        output.append(processing_page)

        for dep in deps[processing_page]:
            deps_reversed[dep].remove(processing_page)

        add_without_deps()

        q.task_done()

    return output[len(output) // 2]


print("Part 1: ", sum(map(part1, updates)))
print("Part 2: ", sum(map(part2, updates)))
