import math
from pathlib import Path
import queue
import numpy as np

p = Path(__file__).with_name("input.txt")
map = open(p).read().splitlines()

N = len(map)
M = len(map[0])


# find start
S = None
for i in range(N):
    for j in range(M):
        if map[i][j] == "S":
            S = (i, j)

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def calculate(distance_limit):
    distance = {S: 0}
    q = queue.Queue()
    q.put(S)

    while not q.empty():
        (i, j) = q.get()
        currentDistance = distance[(i, j)]
        if currentDistance == distance_limit:
            q.task_done()
            break

        nextDistance = currentDistance + 1
        for dir in range(4):
            newI = i + di[dir]
            newJ = j + dj[dir]
            distanceForNewItem = distance.get((newI, newJ), math.inf)
            if map[newI % N][newJ % M] == "#":
                continue
            elif distanceForNewItem == math.inf or (distanceForNewItem % 2 == 1 and nextDistance % 2 == 0):
                q.put((newI, newJ))
                distance[(newI, newJ)] = nextDistance

        q.task_done()

    result = 0
    for dist in distance.values():
        if dist % 2 == distance_limit % 2:
            result += 1

    return result


print("Part 1", calculate(64))

PART2_GOAL = 26501365
mod = PART2_GOAL % N
rest = int(PART2_GOAL / N)

x = np.array([0, 1, 2])
y = np.array([calculate(mod), calculate(mod + N), calculate(mod + N * 2)])
qfit = np.polyfit(x, y, 2)

print("Part 2", int(np.round(qfit[0]) * rest * rest +
      np.round(qfit[1]) * rest + np.round(qfit[2])))
