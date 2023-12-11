from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.readlines()

part1 = 0
part2 = 0

for line in lines:

    nums = [int(x) for x in line.split()]

    levels = []
    levels.append(nums)

    while True:
        lastLevel = levels[- 1]
        next_level = [lastLevel[x + 1] - lastLevel[x]
                      for x in range(len(lastLevel) - 1)]
        if next_level.count(0) == len(next_level):
            break

        levels.append(next_level)

    # Rightmost
    lastLevel = levels[-1]
    lastLevel.append(lastLevel[-1])
    for x in range(len(levels) - 2,  -1, -1):
        currentLevel = levels[x]
        currentLevel.append(
            currentLevel[-1] + lastLevel[-1])

        lastLevel = currentLevel
    part1 += levels[0][-1]

    # Leftmost
    lastLevel = levels[len(levels) - 1]
    lastLevel.insert(0, lastLevel[-1])
    for x in range(len(levels) - 2,  -1, -1):
        currentLevel = levels[x]
        currentLevel.insert(
            0,
            currentLevel[0] - lastLevel[0]
        )

        lastLevel = currentLevel
    part2 += levels[0][0]

print("Part 1", part1)
print("Part 2", part2)
