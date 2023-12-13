from functools import lru_cache
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.read().splitlines()


def is_valid(code, num, codeIdx):
    if codeIdx + num > len(code):
        return False

    # All valid, and after there's a space or question mark
    for i in range(codeIdx, codeIdx + num):
        if code[i] == '.':
            return False

    if codeIdx + num < len(code):
        return code[codeIdx + num] == '.' or code[codeIdx + num] == '?'

    return True


cc = 0

code = None
nums = None


@lru_cache()
def calculate(codeIdx, numsIdx, codeNo):
    if numsIdx == len(nums):
        for i in range(codeIdx, len(code)):
            if code[i] == '#':
                return 0

        return 1
    sum = 0

    for i in range(codeIdx, len(code)):
        if is_valid(code, nums[numsIdx], i):
            sum += calculate(i +
                             nums[numsIdx] + 1, numsIdx + 1, codeNo)

        if code[i] == '#':
            break

    return sum


part1 = 0
for line in lines:
    cc += 1
    code = line.split()[0]
    nums = [int(x) for x in line.split()[1].split(",")]

    part1 += calculate(0, 0, cc)

print("Part 1", part1)

MULTIPLIER = 5
part2 = 0
for line in lines:
    cc += 1

    code = line.split()[0]
    code = "?".join([code] * MULTIPLIER)

    numsStr = line.split()[1]
    numsStr = ",".join([numsStr] * MULTIPLIER)

    nums = [int(x) for x in numsStr.split(",")]
    part2 += calculate(0, 0, cc)

print("Part 2", part2)
