from collections import defaultdict
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

no1 = []
no2 = []
no2_freq = defaultdict(lambda: 0)

for line in file.readlines():
    arr = line.split()
    no1.append(int(arr[0]))
    no2_v = int(arr[1])
    no2.append(no2_v)
    no2_freq[no2_v] = no2_freq[no2_v] + 1

no1.sort()
no2.sort()

part1 = 0
for x in range(len(no1)):
    part1 += abs(no1[x] - no2[x])

print("Part 1: ", part1)

part2 = 0
for x in no1:
    part2 += x * no2_freq[x]

print("Part 2: ", part2)
