from pathlib import Path
import regex as re


p = Path(__file__).with_name("input.txt")
file = open(p)
lines = file.readlines()

def solve(pairs):
    product = 1
    for (time, distance) in pairs:
        options = 0

        for x in range(time + 1):
            works = (time - x) * x > distance
            options += 1 if works else 0
        
        product *= options

    return product


times = [int(x) for x in lines[0].split()[1:]]
distances = [int(x) for x in lines[1].split()[1:]]

pairs = list(zip(times, distances))
print("Part1", solve(pairs))


timesPart2 = int("".join(lines[0].split()[1:]))
distancesPart2 = int("".join(lines[1].split()[1:]))
pairs = [[timesPart2, distancesPart2]]
print("Part2", solve(pairs))