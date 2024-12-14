from pathlib import Path
import re

import numpy as np

file = open(Path(__file__).with_name("input.txt"))
lines = file.readlines()


def determine_min_combo(b1_x, b1_y, b2_x, b2_y, p_x, p_y):
    A = np.array([[b1_x, b2_x],
                  [b1_y, b2_y]])
    B = np.array([p_x, p_y])
    a_lin, b_lin = np.linalg.solve(A, B)
    a_lin, b_lin = a_lin.astype(int), b_lin.astype(int)

    min_b1 = a_lin - 1
    max_b1 = a_lin + 2  # Range is exclusive of last, so + 2

    combo = None
    for a in range(min_b1, max_b1):
        b = (p_x - a * b1_x) // b2_x
        if a * b1_x + b * b2_x == p_x and a * b1_y + b * b2_y == p_y:
            combo_sum = 3 * a + b
            combo = min(combo, combo_sum) if combo is not None else combo_sum

    return combo


part1 = 0
part2 = 0


for i in range(len(lines) // 4):
    [b1_x, b1_y] = [int(x) for x in re.findall(r'-?\d+', lines[i*4])]
    [b2_x, b2_y] = [int(x) for x in re.findall(r'-?\d+', lines[i*4 + 1])]
    [p_x, p_y] = [int(x) for x in re.findall(r'-?\d+', lines[i*4 + 2])]

    p1 = determine_min_combo(b1_x, b1_y, b2_x, b2_y, p_x, p_y)
    part1 += p1 if p1 is not None else 0

    p2 = determine_min_combo(b1_x, b1_y, b2_x, b2_y,
                             10000000000000 + p_x, 10000000000000 + p_y)
    part2 += p2 if p2 is not None else 0

print("Part 1", part1)
print("Part 2", part2)
