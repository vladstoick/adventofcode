from pathlib import Path
import queue

p = Path(__file__).with_name("input.txt")
file = open(p)

map = [[*x.strip()] for x in file.readlines()]
N = len(map)
M = len(map[0])

emptyRows = []
for i in range(N):
    prevValue = 0 if i == 0 else emptyRows[-1]
    curValue = 1 if map[i].count('#') == 0 else 0
    emptyRows.append(prevValue + curValue)

print(emptyRows)

emptyCols = []
for j in range(M):
    col = [map[i][j] for i in range(N)]

    prevValue = 0 if j == 0 else emptyCols[-1]
    curValue = 1 if col.count('#') == 0 else 0
    emptyCols.append(prevValue + curValue)


# find stars
galaxies = []
for i in range(N):
    for j in range(M):
        if map[i][j] == "#":
            galaxies.append((i, j))


def calc(multiplier):
    result = 0
    multiplier = multiplier - 1
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            [g1i, g1j] = galaxies[i]
            [g2i, g2j] = galaxies[j]

            iS = sorted([g1i, g2i])
            jS = sorted([g1j, g2j])

            emptyRow = emptyRows[iS[1]] - emptyRows[iS[0]]
            distI = iS[1] - iS[0] + multiplier * emptyRow

            emptyCol = (emptyCols[jS[1]] - emptyCols[jS[0]])
            distJ = jS[1] - jS[0] + multiplier * emptyCol

            result += distI + distJ

    return result


print("Part 1", calc(1))
print("Part 2", calc(1000000))
