from pathlib import Path

file = open(Path(__file__).with_name("input.txt"))
lines = [line.strip() for line in file.readlines()]

rows, cols = len(lines), len(lines[0])

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

visited = set()


def depth(i, j, d, orig):
    if i < 0 or i == rows or j < 0 or j == cols or lines[i][j] != orig:
        return (0, 1)

    if (i, j) in visited:
        return (0, 0)

    visited.add((i, j))

    area = 1
    perim = 0

    for d in range(len(di)):
        ni = i + di[d]
        nj = j + dj[d]
        a, p = depth(ni, nj, orig)
        area += a
        perim += p

    return (area, perim)


part1 = 0

for i in range(rows):
    for j in range(cols):
        if (i, j) not in visited:
            a, p = depth(i, j, lines[i][j])
            part1 += a * p

# part1 = 0

# for k in area_calc.keys():
#     part1 += area_calc[k] * perim_calc[k]

print("Part 1", part1)
