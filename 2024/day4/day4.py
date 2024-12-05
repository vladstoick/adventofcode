from collections import defaultdict
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = [line.strip() for line in file.readlines()]

di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
# di = [0, 1, 1]
# dj = [1, 1, 0]

WORD = "XMAS"
# WORD_REVERSED = "SAMX"

rows = len(lines)
cols = len(lines[0])

print("Rows: ", rows, " Cols: ", cols)


def count(i, j, distance, d, word):
    if i < 0 or i >= rows or j < 0 or j >= cols:
        return 0

    if lines[i][j] != word[distance]:
        return 0

    if distance == len(word) - 1:
        return 1

    return count(i + di[d], j + dj[d], distance+1, d, word)


def part1():
    part1 = 0

    for i in range(rows):
        for j in range(cols):
            for d in range(len(di)):
                part1 += count(i, j, 0, d, WORD)

    return part1


def part2():
    part2 = 0
    for i in range(rows - 2):
        for j in range(cols - 2):
            left = count(i, j, 0, 3, "MAS") + count(i, j, 0, 3, "SAM")
            right = count(i, j + 2, 0, 5, "MAS") + count(i, j + 2, 0, 5, "SAM")

            if left and right:
                part2 += 1

    return part2


print("Part 1: ", part1())
print("Part 2: ", part2())
