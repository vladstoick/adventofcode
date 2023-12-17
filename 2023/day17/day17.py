import math
from pathlib import Path
import queue

p = Path(__file__).with_name("input.txt")
file = open(p)

map = [[int(c) for c in line] for line in file.read().splitlines()]
N = len(map)
M = len(map[0])

directions = ["^", ">", "v", "<"]
possibleDirs = {
    "^": [">", "<"],
    "v": [">", "<"],
    ">": ["^", "v"],
    "<": ["^", "v"],
}
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def calculate(distanceRange):
    distance = []
    visited = []
    prev = []
    for i in range(N):
        distance.append([])
        visited.append([])
        prev.append([])
        for j in range(M):
            distance[-1].append({"^": math.inf, ">": math.inf,
                                "v": math.inf, "<": math.inf})
            visited[-1].append({"^": False, ">": False,
                               "v": False, "<": False})
            prev[-1].append({"^": None, ">": None, "v": None, "<": None})

    q = queue.PriorityQueue()

    for dir in directions:
        distance[0][0][dir] = 0

    q.put((0, (0, 0, "<")))
    q.put((0, (0, 0, "^")))

    while not q.empty():
        [curDistance, [i, j, prevDir]] = q.get()
        if visited[i][j][prevDir] == True:
            q.task_done()
            continue
        if i == N - 1 and j == M - 1:
            break

        for nextDir in possibleDirs[prevDir]:
            dirIdx = directions.index(nextDir)

            for moveDistance in distanceRange:
                newI = i + di[dirIdx] * moveDistance
                newJ = j + dj[dirIdx] * moveDistance

                if newI < 0 or newJ < 0 or newI >= N or newJ >= M:
                    break

                if visited[newI][newJ][nextDir] == True:
                    continue

                heat = 0
                if newI != i:
                    rI = range(i + 1, newI + 1) if i < newI else range(newI, i)
                    for heatI in rI:
                        heat += map[heatI][j]
                else:
                    rJ = range(j + 1, newJ + 1) if j < newJ else range(newJ, j)
                    for heatJ in rJ:
                        heat += map[i][heatJ]

                newDistance = curDistance + heat
                if newDistance < distance[newI][newJ][nextDir]:
                    distance[newI][newJ][nextDir] = newDistance
                    prev[newI][newJ][nextDir] = (i, j, prevDir)
                    q.put((newDistance, (newI, newJ, nextDir)))

        visited[i][j][prevDir] = True
        q.task_done()

    return min(distance[N - 1][M - 1].values())


print("Part 1", calculate(range(1, 4)))
print("Part 2", calculate(range(4, 11)))
