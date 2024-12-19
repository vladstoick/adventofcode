from pathlib import Path
from collections import defaultdict
file = open(Path(__file__).with_name("input.txt"))

towels = file.readline().strip().split(", ")
file.readline()  # empty line
patterns = [line.strip() for line in file.readlines()]


def possibilities(pattern, towels):
    possibile = defaultdict(lambda: 0)
    possibile[0] = 1

    for idx in range(len(pattern)):
        if possibile[idx] == 0:
            continue

        for towel in towels:
            if pattern[idx:].startswith(towel) and len(pattern[idx:]) >= len(towel):
                possibile[idx + len(towel)] += possibile[idx]

    return possibile[len(pattern)]


part1 = 0
part2 = 0
for pattern in patterns:
    pos = possibilities(pattern, towels)
    part1 += min(pos, 1)
    part2 += pos


print("Part 1", part1)
print("Part 2", part2)
