from collections import defaultdict
from pathlib import Path
import regex as re


ROWS = 103
COLS = 101


def print_pos(pos):
    for i in range(ROWS):
        for j in range(COLS):
            print(pos[(i, j)] if pos[(i, j)] > 0 else ".", end="")
        print("")


def calculate_quadrant(pos):
    quadrants = [0, 0, 0, 0]
    mid_row = ROWS // 2
    mid_col = COLS // 2
    for i in range(ROWS):
        for j in range(COLS):
            if i < mid_row:
                if j < mid_col:
                    quadrants[0] += pos[(i, j)]
                elif j > mid_col:
                    quadrants[1] += pos[(i, j)]
            elif i > mid_row:
                if j < mid_col:
                    quadrants[2] += pos[(i, j)]
                elif j > mid_col:
                    quadrants[3] += pos[(i, j)]
    multiply = 1
    for quadrant in quadrants:
        multiply *= quadrant
    return multiply


def process(steps):
    pos = defaultdict(lambda: 0)
    file = open(Path(__file__).with_name("input.txt"))

    for line in file.readlines():
        matches = [int(x) for x in re.findall(r'-?\d+', line)]

        x, y, vx, vy = matches

        fx = (x + vx * steps) % COLS
        fy = (y + vy * steps) % ROWS

        pos[(fy, fx)] += 1

    print("--------------------", steps, "------------------")
    print_pos(pos)
    return calculate_quadrant(pos)


print("Part 1", process(100))

# Part 2
for step in range(10000):
    process(step)
