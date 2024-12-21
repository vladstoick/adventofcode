import math
from pathlib import Path
from itertools import permutations
from functools import cache

file = open(Path(__file__).with_name("input.txt"))
inputs = [line.strip() for line in file.readlines()]

key_map = {
    '7': (0, 0), '8': (0, 1), '9': (0, 2),
    '4': (1, 0), '5': (1, 1), '6': (1, 2),
    '1': (2, 0), '2': (2, 1), '3': (2, 2),
                 '0': (3, 1), 'A': (3, 2)
}

robot_map = {
    '^': (0, 1), 'A': (0, 2),
    '<': (1, 0), 'v': (1, 1), '>': (1, 2)
}

move = {
    '^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)
}


def is_position_valid(position, map):
    return position in map.values()


def is_permutation_valid(permutation, current_position, map):
    for op in permutation:
        mi, mj = move[op]
        current_position = (current_position[0] + mi, current_position[1] + mj)
        if not is_position_valid(current_position, map):
            return False
    return True


cached = {}


def find_move(map_idx, current_position, end_position):
    map = key_map if map_idx == 0 else robot_map
    si, sj = map[current_position]
    ei, ej = map[end_position]

    output = ""
    if si > ei:
        output += "^" * (si-ei)
    elif si < ei:
        output += "v" * (ei-si)

    if sj > ej:
        output += "<" * (sj-ej)
    elif sj < ej:
        output += ">" * (ej-sj)

    possible_paths = list(filter(
        lambda x: is_permutation_valid(x, (si, sj), map), set(permutations(output, len(output)))))
    possible_paths = ["".join(list(possible_path) + ["A"])
                      for possible_path in possible_paths]

    return possible_paths


@cache
def final_path_v2(input, level, max_robots):
    if level > max_robots:
        return len(input)

    final = 0
    for i in range(len(input)):
        prev = input[i - 1] if i > 0 else "A"
        cur = input[i]

        level = max(level, 0)

        min_next_level = None
        options = find_move(max(level, 0), prev, cur)

        min_next_level = None
        for option in options:
            next_level = final_path_v2(option, level + 1, max_robots)
            if min_next_level is None or next_level < min_next_level:
                min_next_level = next_level

        final += min_next_level

    return final


def calculate(max_robots):
    result = 0
    for input in inputs:
        sum = int(input[:-1].lstrip("0"))
        min_len_path = final_path_v2(input, 0, max_robots)
        result += sum * min_len_path
    return result


print("Part 1", calculate(2))
print("Part 2", calculate(25))
