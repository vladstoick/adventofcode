from pathlib import Path
import queue

p = Path(__file__).with_name("input.txt")
file = open(p)

map = [[*x.strip()] for x in file.readlines()]

N = len(map)
M = len(map[0])

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
#  0
# 3 1
#  2

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
revDir = [2, 3, 0, 1]

pipes = {
    "|": [0, 2],
    "-": [1, 3],
    "L": [0, 1],
    "J": [0, 3],
    "7": [2, 3],
    "F": [1, 2],
    ".": []
}

copy = {
    "|": [
        [0, 1, 0],
        [0, 1, 0],
        [0, 1, 0]
    ],
    "-": [
        [0, 0, 0],
        [1, 1, 1],
        [0, 0, 0]
    ],
    "L": [
        [0, 1, 0],
        [0, 1, 1],
        [0, 0, 0]
    ],
    "J": [
        [0, 1, 0],
        [1, 1, 0],
        [0, 0, 0]
    ],
    "7": [
        [0, 0, 0],
        [1, 1, 0],
        [0, 1, 0]
    ],
    "F": [
        [0, 0, 0],
        [0, 1, 1],
        [0, 1, 0]
    ],
    ".": [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]
}


# Find and replace start

S = (0, 0)

for row in range(N):
    for col in range(M):
        if map[row][col] == "S":
            S = (row, col)

            okDirs = []

            for dir in range(4):
                newI = row + di[dir]
                newJ = col + dj[dir]

                if revDir[dir] in pipes[map[newI][newJ]]:
                    okDirs.append(dir)

            for pipe in pipes.keys():
                if okDirs == pipes[pipe]:
                    map[row][col] = pipe


# Calcualte dinstance


dist = [
    [-1 for x in range(M)] for x in range(N)
]
mainLoop = [
    [0 for x in range(M)] for x in range(N)
]
dist[S[0]][S[1]] = 0
q = queue.Queue()
q.put(S)

part1 = 0
while not q.empty():
    (i, j) = q.get()
    mainLoop[i][j] = 1
    if (dist[i][j] > part1):
        part1 = dist[i][j]

    for dir in pipes[map[i][j]]:
        newI = i + di[dir]
        newJ = j + dj[dir]

        if newI >= 0 and newJ >= 0 and newI < N and newJ < M:
            if dist[newI][newJ] == -1:
                dist[newI][newJ] = dist[i][j] + 1
                q.put((newI, newJ))

    q.task_done()

print("Part 1", part1)

expanded = [
    [0 for x in range(M * 3)] for x in range(N * 3)
]

for row in range(N):
    for col in range(M):
        for i in range(3):
            for j in range(3):
                char = map[row][col]
                actualChar = char if mainLoop[row][col] else '.'
                expanded[row * 3 + i][col * 3 + j] = copy[actualChar][i][j]

lastSet = 2
goodSets = []

N = N * 3
M = M * 3

for row in range(N):
    for col in range(M):
        isGood = True

        if expanded[row][col] != 0:
            continue

        expanded[row][col] = lastSet

        q.put((row, col))
        count = 0

        while not q.empty():
            [i, j] = q.get()

            count += 1
            if i == 0 or j == 0 or i == N - 1 or j == M - 1:
                isGood = False

            for dir in range(4):
                newI = i + di[dir]
                newJ = j + dj[dir]
                if newI >= 0 and newJ >= 0 and newI < N and newJ < M:
                    if expanded[newI][newJ] == 0:
                        q.put((newI, newJ))
                        expanded[newI][newJ] = lastSet

            q.task_done()

        if isGood:
            goodSets.append(lastSet)

        lastSet += 1

N = int(N/3)
M = int(M/3)


part2 = 0
for row in range(N):
    for col in range(M):
        if mainLoop[row][col] == 0:
            isGood = True
            for i in range(3):
                for j in range(3):
                    isGood = isGood and (
                        expanded[row * 3 + i][col * 3 + j] in goodSets)

            part2 += 1 if isGood else 0

print("Part 2", part2)
