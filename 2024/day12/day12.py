from collections import defaultdict
from pathlib import Path

file = open(Path(__file__).with_name("input.txt"))
lines = [line.strip() for line in file.readlines()]

rows, cols = len(lines), len(lines[0])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited = set()
edges = defaultdict(lambda: [])


def depth(i, j, orig):

    if (i, j) in visited:
        return (0, 0)

    visited.add((i, j))

    area = 1
    perim = 0

    for d in range(len(di)):
        ni = i + di[d]
        nj = j + dj[d]

        if ni < 0 or ni == rows or nj < 0 or nj == cols or lines[ni][nj] != orig:
            perim += 1
            edges[(i, j)].append(d)
        else:
            a, p = depth(ni, nj, orig)
            area += a
            perim += p

    return (area, perim)


part1 = 0
part2 = 0

for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            edges = defaultdict(lambda: [])
            a, p = depth(i, j, lines[i][j])
            part1 += a * p

            e = 0

            keys = list(edges.keys())
            for (ei, ej) in keys:
                for d in range(4):
                    if d in edges[(ei, ej)]:
                        ni, nj = ei + di[(d - 1) % 4], ej + dj[(d - 1) % 4]

                        if d not in edges[(ni, nj)]:
                            e += 1

            part2 += a * e


print("Part 1", part1)
print("Part 2", part2)
