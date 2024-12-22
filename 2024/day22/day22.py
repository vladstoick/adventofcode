from pathlib import Path
from functools import cache
from collections import defaultdict, deque

file = open(Path(__file__).with_name("input.txt"))
inputs = [int(line.strip()) for line in file.readlines()]


@cache
def evolve(orig):
    temp = orig
    temp ^= orig << 6  # * 64
    temp ^= orig >> 5  # // 32
    temp ^= orig << 11  # * 2048
    temp = temp & 0xFFFFFF

    return temp


sequences = defaultdict(lambda: defaultdict(lambda: None))

iters = 2000
part1 = 0

for input_idx in range(len(inputs)):
    input = inputs[input_idx]
    sequence = deque(maxlen=4)
    sequence.append(0)

    for x in range(iters):
        prev_input = input
        input = evolve(input)
        diff = input % 10 - prev_input % 10
        sequence.append(diff)

        if len(sequence) == 4:
            if sequences[tuple(sequence)][input_idx] is None:
                sequences[tuple(sequence)][input_idx] = input % 10

    part1 += input

print("Part 1", part1)

part2_val = max(sum(v.values()) for v in sequences.values())

print("Part 2", part2_val)
