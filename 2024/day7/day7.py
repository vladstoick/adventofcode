from collections import defaultdict
from pathlib import Path

file = open(Path(__file__).with_name("input.txt"))


def works(total, ops, index, sum, part2):
    if index == len(ops):
        return sum == total
    if sum > total:
        return False

    works_add = works(total, ops, index + 1, sum + ops[index], part2)
    works_multiply = works(total, ops, index + 1, sum * ops[index], part2)
    works_part2 = False
    if part2 and index > 0:
        combined = int(str(sum) + str(ops[index]))
        works_part2 = works(total, ops, index + 1, combined, part2)

    return works_add or works_multiply or works_part2


part1 = 0
part2 = 0

for line in file.readlines():
    total, ops_str = line.split(": ")
    total = int(total)
    ops = [int(x) for x in ops_str.split(" ")]

    part1 += total if works(total, ops, 0, 0, False) else 0
    part2 += total if works(total, ops, 0, 0, True) else 0

print("Part1: ", part1)
print("Part2: ", part2)
