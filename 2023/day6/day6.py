import cmath
import math
from pathlib import Path
import regex as re


p = Path(__file__).with_name("input.txt")
file = open(p)
lines = file.readlines()

def solve(pairs):
    product = 1
    for (time, distance) in pairs:
        a = -1
        b = time
        c = -distance
        d = (b**2) - (4*a*c)

        sol1 = math.ceil((-b+math.sqrt(d))/(2*a)+0.00001)
        sol2 = math.floor((-b-math.sqrt(d))/(2*a)-0.0001)

        product *= sol2 - sol1 + 1

    return product


times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

pairs = list(zip(times, distances))
print("Part1", solve(pairs))


timesPart2 = int("".join(lines[0].split()[1:]))
distancesPart2 = int("".join(lines[1].split()[1:]))
pairs = [[timesPart2, distancesPart2]]
print("Part2", solve(pairs))