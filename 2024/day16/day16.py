import math
from pathlib import Path
from collections import defaultdict
from queue import Queue

file = open(Path(__file__).with_name("input.txt"))
lines = [line.strip() for line in file.readlines()]

path = defaultdict(lambda: defaultdict(lambda: math.inf))

rows = len(lines)
cols = len(lines[0])

start = None, None
end = None, None
for i in range(rows):
    for j in range(cols):
        if lines[i][j] == 'E':
            end = i, j
        elif lines[i][j] == 'S':
            start = i, j


all_directions = ['up', 'right', 'down', 'right']

dir = {
    'up': (-1, 0),
    'right': (0, 1),
    'down': (1, 0),
    'left': (0, -1)
}

reverse = {
    'up': ['left', 'right'],
    'down': ['left', 'right'],
    'left': ['up', 'down'],
    'right': ['up', 'down'],
}


def add(tuple1, tuple2):
    return (tuple1[0] + tuple2[0], tuple1[1] + tuple2[1])


def subtract(tuple1, tuple2):
    return (tuple1[0] - tuple2[0], tuple1[1] - tuple2[1])


def calculate_paths():
    queue = Queue()
    queue.put((start, 'right', 0))

    path = defaultdict(lambda: defaultdict(lambda: math.inf))

    while not queue.empty():
        (point, direction, sum) = queue.get()

        if sum < path[point][direction]:
            path[point][direction] = sum

            # Check next position
            new_point = add(point, dir[direction])
            current_path = path[new_point][direction]

            if lines[new_point[0]][new_point[1]] != '#' and sum + 1 < current_path:
                queue.put((new_point, direction, sum + 1))

            # check other direction
            for new_direction in reverse[direction]:
                current_path = path[point][new_direction]

                if sum + 1000 < current_path:
                    queue.put((point, new_direction, sum + 1000))

        queue.task_done()

    return path


def get_min_direction_for_point(point):
    min_val = path[point]['up']
    min_key = "up"
    for k, v in path[point].items():
        if v < min_val:
            min_val = v
            min_key = k

    return min_key


path = calculate_paths()


# Part 1
part1 = get_min_direction_for_point(end)
print("Part 1", part1, path[end][part1])


def trackback_paths(part1):
    point_path = {end}

    queue_points_path = Queue()
    queue_points_path.put((end, part1))

    while not queue_points_path.empty():
        current_point, current_direction = queue_points_path.get()
        point_path.add(current_point)
        current_val = path[current_point][current_direction]

        # Check next position
        new_point = subtract(current_point, dir[current_direction])
        new_point_val = path[new_point][current_direction]

        if new_point_val == current_val - 1:
            queue_points_path.put((new_point, current_direction))

        # Check turn-around
        for new_direction in reverse[current_direction]:
            new_direction_val = path[current_point][new_direction]

            if current_val - 1000 == new_direction_val:
                queue_points_path.put((current_point, new_direction))

        queue_points_path.task_done()

    return point_path


print("Part 2", len(trackback_paths(part1)))
