from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

max_allowed_part1 = {"red": 12, "green": 13, "blue": 14}
part1 = 0
part2 = 0

for i, line in enumerate(file.readlines()):
    possible = True
    groups = re.findall("(\d+) (\w+)", line)

    part2Values = {"red": 0, "green": 0, "blue": 0}

    for group in groups:
        val = int(group[0])
        colour = group[1]
        if(val > max_allowed_part1[colour]):
            possible = False
        if(val > part2Values[colour]):
            part2Values[colour] = val
    
    if possible:
        print("Game ", i, " is possible")
        part1 += (i + 1)

    part2 += part2Values["red"] * part2Values["green"] * part2Values["blue"]

print("Part 1: ", part1)
print("Part 2: ", part2)