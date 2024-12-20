from functools import cache
from pathlib import Path
from collections import defaultdict
import math
from queue import Queue

file = open(Path(__file__).with_name("input.txt"))

map = [line.strip() for line in file.readlines()]
rows, cols = len(map), len(map[0])


def determine_start_end():
    start, end = None, None
    for i in range(rows):
        for j in range(cols):
            if map[i][j] == 'S':
                start = (i, j)
            elif map[i][j] == 'E':
                end = (i, j)

    return start, end


start, end = determine_start_end()

distance = defaultdict(lambda: math.inf)


di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def calculate_distance(start_point):
    distance[start_point] = 0
    queue = Queue()
    queue.put(start_point)

    while not queue.empty():
        point = queue.get()

        for d in range(4):
            ni, nj = point[0] + di[d], point[1] + dj[d]

            if map[ni][nj] != '#' and distance[(ni, nj)] > distance[point] + 1:
                distance[(ni, nj)] = distance[point] + 1
                queue.put((ni, nj))

        queue.task_done()


calculate_distance(start)


def is_point_valid(i, j):
    return i >= 0 and i < rows and j >= 0 and j < cols


def check_cheat_from_point_v2(point, max_cheat):
    orig_distance = distance[end] - distance[point]
    cheats = []
    for di in range(-max_cheat, max_cheat + 1):
        dj_allowed = max_cheat - abs(di)
        for dj in range(-dj_allowed, dj_allowed + 1):
            ni, nj = point[0] + di, point[1] + dj
            if not is_point_valid(ni, nj):
                continue

            cheat_used = abs(di) + abs(dj)

            if map[ni][nj] != '#':
                new_distance = distance[end] - distance[(ni, nj)]
                saved = orig_distance - new_distance - cheat_used

                if saved > 0:
                    cheats += [saved]

    return cheats


def calculate(max_cheats):
    cheats_count = defaultdict(lambda: 0)
    for point in distance.keys():
        cheats = check_cheat_from_point_v2(point, max_cheats)

        for cheat in cheats:
            cheats_count[cheat] += 1

    result = 0
    for cheat in sorted(list(cheats_count.keys())):
        if cheat >= 100:
            result += cheats_count[cheat]

    return result


print("Part 1", calculate(2))
print("Part 2", calculate(20))
