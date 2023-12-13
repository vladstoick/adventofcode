from functools import lru_cache
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

patterns = []
patterns.append([])
for line in file.read().splitlines():
    if len(line) == 0:
        patterns.append([])
    else:
        patterns[-1].append(line)


def find_cut(vec, offBy):
    goodCut = None
    N = len(vec)
    M = len(vec[0])
    # Find row cut
    for cut in range(1, N):
        totalComparison = cut * 2
        offByCut = 0
        for verif in range(0, cut):
            up = verif
            down = totalComparison - verif - 1
            if (down >= N):
                continue

            if vec[up] != vec[down]:
                for j in range(M):
                    offByCut += 1 if vec[up][j] != vec[down][j] else 0

        if offByCut == offBy:
            goodCut = cut
            break

    return goodCut


part1 = 0
part2 = 0
for pattern in patterns:
    rows = pattern
    N = len(rows)
    M = len(rows[0])

    cols = [[rows[i][j] for i in range(N)] for j in range(M)]
    cols = ["".join(col) for col in cols]

    rowCutPart1 = find_cut(rows, 0)
    if rowCutPart1 is not None:
        part1 += rowCutPart1 * 100
    colCutPart1 = find_cut(cols, 0)
    if colCutPart1 is not None:
        part1 += colCutPart1

    rowCutPart2 = find_cut(rows, 1)
    if rowCutPart2 is not None:
        part2 += rowCutPart2 * 100
    colCutPart2 = find_cut(cols, 1)
    if colCutPart2 is not None:
        part2 += colCutPart2

print("Part 1", part1)
print("Part 2", part2)
