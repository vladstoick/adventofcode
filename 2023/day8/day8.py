import math
from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.readlines()

steps = [0 if x == 'L' else 1 for x in lines[0].strip()]

paths = {}
for line in lines[2:]:
    matches = re.findall("\w\w\w", line)
    paths[matches[0]] = [matches[1], matches[2]]


def calculate(start, part2):
    current = start
    i = 0

    while True:
        current = paths[current][steps[i % len(steps)]]
        i += 1

        if (part2 and current[-1] == 'Z') or (not part2 and current == 'ZZZ'):
            return i


print("Part 1", calculate('AAA', False))

# For part2, somehow once you reach a Z, then it takes the same amount of time
# to reach the node again A->Z= Z->Z
arr = []
for item in paths.keys():
    if item[-1] == 'A':
        arr.append(calculate(item, True))

gcd = math.gcd(*arr)
product = 1
for x in arr:
    product *= int(x / gcd)
product *= gcd

print("Part 2", product)
