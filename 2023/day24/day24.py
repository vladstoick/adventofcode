import math
from pathlib import Path

p = Path(__file__).with_name("input.txt")
lines = open(p).read().splitlines()

rocks = []
for line in lines:
    rock = [int(x) for x in line.replace("@ ", ", ").split(", ")]
    x = rock[0]
    y = rock[1]
    z = rock[2]
    vx = rock[3]
    vy = rock[4]
    vz = rock[5]

    # f(x + vx * s) = y + vy * s
    # X = x + vx * s
    # S = (X - x) / vx
    # f(X) = (vy / vx) * X + y - x * vy / vx
    qfitxy = [vy/vx, y - x * vy / vx]
    qfitxz = [vz/vx, z - x * vz / vx]

    x_range = None
    if vx > 0:
        x_range = (x, math.inf)
    elif vx == 0:
        x_range = (x, x)
    else:
        x_range = (-math.inf, x)

    rocks.append((qfitxy, x_range))
    print(qfitxy)

MIN_XY = 200000000000000
MAX_XY = 400000000000000

part1 = 0
for i in range(len(rocks)):
    (rock_qfit, rock_range) = rocks[i]
    for j in range(i + 1, len(rocks)):
        (other_rock_qfit, other_rock_range) = rocks[j]

        if math.isclose(rock_qfit[0], other_rock_qfit[0]):
            continue

        intersect = (
            other_rock_qfit[1] - rock_qfit[1]) / (rock_qfit[0] - other_rock_qfit[0])
        x = intersect
        y = rock_qfit[0] * x + rock_qfit[1]
        print(x, y)

        if x < rock_range[0] or x > rock_range[1]:
            continue
        elif x < other_rock_range[0] or x > other_rock_range[1]:
            continue
        elif x >= MIN_XY and x <= MAX_XY and y >= MIN_XY and y <= MAX_XY:
            part1 += 1

print(part1)

# f(x) = a1 * x + b1
# f(x) = a2 * x + b2

# need to find f(x3)

# a1 * x + b1 =
