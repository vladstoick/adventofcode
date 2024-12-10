from pathlib import Path
from collections import defaultdict
import queue

file = open(Path(__file__).with_name("input.txt"))
input = [[int(x) for x in line.strip()]
         for line in file.readlines()]

visit_count = defaultdict(lambda: 0)
nines = defaultdict(lambda: set())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

rows = len(input)
cols = len(input[0])

q = queue.Queue()
v = set()

for i in range(rows):
    for j in range(cols):
        if input[i][j] == 9:
            q.put((i, j))
            visit_count[(i, j)] += 1
            nines[(i, j)].add((i, j))


while not q.empty():
    (i, j) = q.get()

    if (i, j) not in v:
        for d in range(4):
            (ni, nj) = (i+di[d], j+dj[d])

            if ni >= 0 and ni < rows and nj >= 0 and nj < cols and input[ni][nj] == input[i][j] - 1:
                visit_count[(ni, nj)] += visit_count[(i, j)]
                nines[(ni, nj)] = nines[(ni, nj)].union(nines[(i, j)])
                q.put((ni, nj))

    v.add((i, j))
    q.task_done()

part1 = 0
part2 = 0
for i in range(rows):
    for j in range(cols):
        if input[i][j] == 0:
            part1 += len(nines[(i, j)])
            part2 += visit_count[(i, j)]

print("Part 1", part1)
print("Part 2", part2)
