from pathlib import Path
import re

import numpy as np

file = open(Path(__file__).with_name("input.txt"))
lines = file.readlines()

registers = [int(re.findall(r'\d+', lines[x])[0]) for x in range(3)]
output = []
program = [int(x) for x in re.findall(r'\d+', lines[4])]

i = 0


def get_combo_value(operand):
    if operand <= 3:
        return operand
    else:
        return registers[operand % 4]


while i < len(program):

    instruction = program[i]
    operand = program[i + 1]

    if instruction == 0:
        registers[0] = registers[0] // 2 ** get_combo_value(operand)
    elif instruction == 1:
        registers[1] = registers[1] ^ operand
    elif instruction == 2:
        registers[1] = get_combo_value(operand) % 8
    elif instruction == 3:
        print(registers[0])
        if registers[0] != 0:
            i = operand - 2
    elif instruction == 4:
        registers[1] = registers[1] ^ registers[2]
    elif instruction == 5:
        output.append(get_combo_value(operand) % 8)
    elif instruction == 6:
        registers[1] = registers[0] // 2 ** get_combo_value(operand)
    elif instruction == 7:
        registers[2] = registers[0] // 2 ** get_combo_value(operand)

    i += 2

print(",".join([str(x) for x in output]))
