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


def solve(update):
    (deps, deps_reversed) = create_copy(update)

    output = []
    q = queue.Queue()
    v = set()

    def add_without_deps():
        for page in update:
            if len(deps_reversed[page]) == 0 and page not in v:
                q.put(page)
                v.add(page)

    add_without_deps()

    while not q.empty():
        processing_page = q.get()
        output.append(processing_page)

        for dep in deps[processing_page]:
            deps_reversed[dep].remove(processing_page)

        add_without_deps()

        q.task_done()

    if output != update:
        return (0, output[len(output) // 2])
    else:
        return (output[len(output) // 2], 0)


part1 = 0
part2 = 0
for update in updates:
    (p1, p2) = solve(update)
    part1 += p1
    part2 += p2

print("Part 1: ", part1)
print("part 2: ", part2)
