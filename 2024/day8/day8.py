from pathlib import Path
from collections import defaultdict
import itertools

file = open(Path(__file__).with_name("input.txt"))
lines = [line.strip() for line in file.readlines()]

rows = len(lines)
cols = len(lines[0])

print("Rows:", rows, "Cols:", cols)

positions_by_key = defaultdict(lambda: [])

for i in range(rows):
    for j in range(cols):
        if lines[i][j] != '.' and lines[i][j] != '#':
            positions_by_key[lines[i][j]].append((i, j))

part1 = 0


def is_valid(pos):
    (i, j) = pos
    return i >= 0 and i < rows and j >= 0 and j < cols


valid_pos_part1 = set()
valid_pos_part2 = set()

for key in positions_by_key.keys():
    positions = itertools.combinations(positions_by_key[key], 2)

    for ((i1, j1), (i2, j2)) in positions:
        di = i1 - i2
        dj = j1 - j2

        for dif in range(-rows, rows):
            pos = (i1 + di * dif, j1 + dj * dif)
            pos_is_valid = is_valid(pos)

            if pos_is_valid:
                valid_pos_part2.add(pos)
                if (dif == -2 or dif == 1):
                    valid_pos_part1.add(pos)

print("Part1: ", len(valid_pos_part1))
print("Part2: ", len(valid_pos_part2))
