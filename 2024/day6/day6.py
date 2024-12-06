from collections import defaultdict
from pathlib import Path
import bisect

file = open(Path(__file__).with_name("input.txt"))
lines = [line.strip() for line in file.readlines()]

rows = len(lines)
cols = len(lines[0])

conflicts_row = defaultdict(lambda: [-2])
conflicts_col = defaultdict(lambda: [-2])

bisect_move = [-1, 0, 0, -1]
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
starti, startj, startdir = 0, 0, 0
dirs = ['^', '>', 'V', '<']

for i in range(rows):
    for j in range(cols):
        char = lines[i][j]
        if char in dirs:
            starti, startj, startdir = i, j, dirs.index(char)
        if char == '#':
            conflicts_row[i].append(j)
            conflicts_col[j].append(i)

[conflicts_row[i].append(cols + 1) for i in range(rows)]
[conflicts_col[j].append(rows + 1) for j in range(cols)]


def check():
    currenti, currentj, currentdir = starti, startj, startdir
    visited = set()
    processed = set()

    while currenti >= 0 and currenti < rows and currentj >= 0 and currentj < cols:
        if (currenti, currentj, currentdir) in processed:
            return set()
        processed.add((currenti, currentj, currentdir))

        newi, newj = currenti, currentj

        if currentdir == 0 or currentdir == 2:
            pos = bisect.bisect_left(conflicts_col[currentj], currenti)
            newi = conflicts_col[currentj][pos +
                                           bisect_move[currentdir]] + -1 * di[currentdir]
        else:
            pos = bisect.bisect_left(conflicts_row[currenti], currentj)
            newj = conflicts_row[currenti][pos +
                                           bisect_move[currentdir]] + -1 * dj[currentdir]

        for i in range(min(currenti, newi), max(currenti, newi) + 1):
            for j in range(min(currentj, newj), max(currentj, newj) + 1):
                visited.add((i, j))

        currentdir = (currentdir + 1) % 4
        currenti, currentj = newi, newj

    return visited


part1 = check()
print("Part 1: ", len(part1) - 1)

part2 = 0
for (i, j) in part1:
    if i != starti or j != startj:
        conflicts_row[i].append(j)
        conflicts_col[j].append(i)
        conflicts_row[i] = sorted(conflicts_row[i])
        conflicts_col[j] = sorted(conflicts_col[j])

        p2 = check()

        if len(p2) == 0:
            part2 += 1

        conflicts_row[i].remove(j)
        conflicts_col[j].remove(i)
        conflicts_row[i] = sorted(conflicts_row[i])
        conflicts_col[j] = sorted(conflicts_col[j])

print("Part 2: ", part2)
