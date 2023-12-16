from pathlib import Path
import queue

p = Path(__file__).with_name("input.txt")
file = open(p)

map = [[c for c in line] for line in file.read().splitlines()]
N = len(map)
M = len(map[0])

# i, j
transform = {
    ".": {
        ">": [(0, 1, ">")],
        "<": [(0, -1, "<")],
        "^": [(-1, 0, "^")],
        "v": [(1, 0, "v")],
    },
    "-": {
        ">": [(0, 1, ">")],
        "<": [(0, -1, "<")],
        "^": [
            (0, 1, ">"),
            (0, -1, "<"),
        ],
        "v": [
            (0, 1, ">"),
            (0, -1, "<"),
        ]
    },
    "|": {
        ">": [
            (-1, 0, "^"),
            (1, 0, "v"),
        ],
        "<": [
            (-1, 0, "^"),
            (1, 0, "v"),
        ],
        "^": [(-1, 0, "^")],
        "v": [(1, 0, "v")],
    },
    "/": {
        ">": [(-1, 0, "^")],
        "<": [(1, 0, "v")],
        "^": [(0, 1, ">")],
        "v": [(0, -1, "<")],
    },
    "\\": {
        ">": [(1, 0, "v")],
        "<": [(-1, 0, "^")],
        "^": [(0, -1, "<")],
        "v": [(0, 1, ">")],
    }
}


def calculate(start):
    energized = [[False for _ in range(M)] for _ in range(N)]

    visisted = set()
    q = queue.Queue()
    q.put((start))

    while not q.empty():
        elem = q.get()
        [i, j, direction] = elem
        visisted.add(elem)
        energized[i][j] = True

        actions = transform[map[i][j]][direction]

        for action in actions:
            [di, dj, direction] = action
            newI = i + di
            newJ = j + dj

            if newI < 0 or newJ < 0 or newI == N or newJ == M:
                continue

            nextElem = (newI, newJ, direction)
            if nextElem in visisted:
                continue

            q.put(nextElem)

        q.task_done()

    result = 0
    for row in range(N):
        result += sum(energized[row])
    return result


CACHE = {}


print("Part 1", calculate((0, 0, ">")))

part2 = 0

# Top and Bottom
for j in range(M):
    part2 = max(part2, calculate((0, j, "v")))
    part2 = max(part2, calculate((N - 1, j, "^")))

# Left and Right
for i in range(N):
    part2 = max(part2, calculate((i, 0, ">")))
    part2 = max(part2, calculate((i, M - 1, "<")))

print("Part 2", part2)
