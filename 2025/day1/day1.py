from collections import defaultdict
from math import ceil, floor
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

val = 50
part1 = 0
part2 = 0

for line in file.readlines():
    command = line[0]
    number = int(line[1:])

    
    ord = -1 if command == "L" else 1
    
    newVal = val + number * ord

    if (newVal >= 100 or newVal <=0):
        if newVal <= 0:
            part2 += ceil(val/ 100) - ceil(newVal / 100)
        else:
            part2 += floor(newVal / 100.0)
    
    val = newVal % 100

    if val == 0:
        part1 += 1

    print(command, number, newVal, val, part2)


print("Part 1", part1)
print("Part 2", part2)