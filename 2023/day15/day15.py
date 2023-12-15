from collections import OrderedDict
from pathlib import Path
import regex

p = Path(__file__).with_name("input.txt")
file = open(p)

words = file.read().strip().split(",")


def hash(word):
    code = 0
    for c in word:
        code += ord(c)
        code *= 17
        code %= 256
    return code


part1 = 0
for word in words:
    part1 += hash(word)

print("Part 1", part1)

boxes = [OrderedDict() for x in range(256)]

for word in words:
    [key, operation, value] = regex.findall("(\w+)(-|=)(\d*)", word)[0]

    key_hashed = hash(key)
    if operation == '-':
        if key in boxes[key_hashed].keys():
            boxes[key_hashed].pop(key)
    else:
        boxes[key_hashed][key] = int(value)

part2 = 0
for (i, box) in enumerate(boxes):
    for (j, val) in enumerate(box.items()):

        part2 += (i + 1) * (j + 1) * val[1]

print("Part 2", part2)
