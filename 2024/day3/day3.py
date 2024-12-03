from collections import defaultdict
from pathlib import Path
import regex as re


p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.readlines()
input = "".join(lines)

DO = "do()"
DONT = "don't()"


def manual_regex(input, check_active):
    index = 0
    sum = 0
    active = True

    while index < len(input):
        input_idx = input[index:]
        if input_idx.startswith(DO) and check_active:
            index += len(DO)
            active = True
        elif input_idx.startswith(DONT) and check_active:
            index += len(DONT)
            active = False
        else:
            match = re.match(r"mul\((\d{1,3}),(\d{1,3})\)", input_idx)
            if match is None or not active:
                index += 1
            else:
                sum += int(match[1]) * int(match[2])
                index += len(match[0])

    return sum


part1 = manual_regex(input, False)
print("Part 1: ", part1)

part2 = manual_regex(input, True)
print("Part 2: ", part2)

# for match in match
