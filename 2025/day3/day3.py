from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

part1 = 0
part2 = 0

for line in file.readlines():
    line = line.strip()

    maxSoFar = [0] + [None] * 12
    
    for c in line:
        c = int(c)

        clone = [x for x in maxSoFar]

        for length in range(len(maxSoFar) - 1):
            if clone[length] is not None:
                newVal = clone[length] * 10 + c
                
                if maxSoFar[length + 1] is None or maxSoFar[length + 1] < newVal:
                    maxSoFar[length + 1] = newVal

    part1 += maxSoFar[2]
    part2 += maxSoFar[12]

print("Part 1", part1)
print("Part 2", part2)