import math
from pathlib import Path
import queue
from collections import defaultdict

file = open(Path(__file__).with_name("input.txt"))


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def min_path(rows, cols, bits):
    q = queue.Queue()
    q.put((0, 0))
    distances = {}
    distances[(0, 0)] = 0

    while not q.empty():
        i, j = q.get()

        for dir in range(4):
            ni = i + di[dir]
            nj = j + dj[dir]

            if ni < 0 or ni == rows or nj < 0 or nj == cols:
                continue

            if (ni, nj) in bits:
                continue

            if (ni, nj) in distances:
                continue

            distances[(ni, nj)] = distances[(i, j)] + 1
            q.put((ni, nj))

        q.task_done()

    return distances[(rows - 1, cols - 1)] if (rows - 1, cols - 1) in distances else None


bits = []
for line in file.readlines():
    a, b = [int(x) for x in line.split(",")]
    bits.append((a, b))

print("Part 1", min_path(71, 71, set(bits[:1024])))


def binary_search(bits):
    l, r = 0, len(bits)
    while l < r:
        mid = (l + r) // 2

        path = min_path(71, 71, set(bits[:mid]))

        if path is not None:
            l = mid + 1
        else:
            r = mid
    return l


index = binary_search(bits)
print("Part 2", bits[index-1])
