import math
from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)
input = [[c for c in line] for line in file.read().splitlines()]

N = len(input)
M = len(input[0])

part1 = 0


def calculate_weight(matrix):
    result = 0
    for row in range(N):
        for col in range(M):
            result += (N - row) if matrix[row][col] == 'O' else 0
    return result


def get_range(start, sum, isUD):
    if isUD:
        return range(start, start + sum)
    else:
        return range(start - sum + 1, start + 1)


def move_vertical(matrix, north):
    new_matrix = [['.' for _ in range(M)] for _ in range(N)]

    for col in range(M):
        start = None
        sum = 0
        for row in (range(N) if north else reversed(range(N))):
            if start == None and matrix[row][col] != '#':
                start = row
            if matrix[row][col] == '#':
                new_matrix[row][col] = '#'

                if sum > 0:
                    for x in get_range(start, sum, north):
                        new_matrix[x][col] = 'O'

                start = None
                sum = 0
            elif matrix[row][col] == 'O':
                sum += 1

        if sum > 0:
            for x in get_range(start, sum, north):
                new_matrix[x][col] = 'O'

    return new_matrix


def move_horizontal(matrix, west):
    new_matrix = [['.' for _ in range(M)] for _ in range(N)]

    for row in range(N):
        start = None
        sum = 0
        for col in (range(M) if west else reversed(range(M))):
            if start == None and matrix[row][col] != '#':
                start = col
            if matrix[row][col] == '#':
                new_matrix[row][col] = '#'

                if sum > 0:
                    for x in get_range(start, sum, west):
                        new_matrix[row][x] = 'O'

                start = None
                sum = 0
            elif matrix[row][col] == 'O':
                sum += 1

        if sum > 0:
            for x in get_range(start, sum, west):
                new_matrix[row][x] = 'O'

    return new_matrix


print("Part 1", calculate_weight(move_vertical(input, True)))


def convert_to_str(matrix):
    all_chars = []
    for row in range(N):
        for col in range(M):
            all_chars.append(matrix[row][col])
    return "".join(all_chars)


def convert_to_2d(matrixStr):
    return [
        [matrixStr[row * M + col] for col in range(M)] for row in range(N)
    ]


def performCycle(matrixStr):
    matrix = convert_to_2d(matrixStr)

    matrix = move_vertical(matrix, True)
    matrix = move_horizontal(matrix, True)
    matrix = move_vertical(matrix, False)
    matrix = move_horizontal(matrix, False)

    return convert_to_str(matrix)


matrix_as_str = convert_to_str(input)

CYCLES = 1000000000
CACHE = {}
cycle = 0
while cycle < CYCLES:
    matrix_as_str = performCycle(matrix_as_str)
    if matrix_as_str in CACHE.keys():
        cycle_length = cycle - CACHE[matrix_as_str]
        remaining_cycles = CYCLES - cycle

        remaining_loops = math.floor(remaining_cycles / cycle_length)
        cycle += remaining_loops * cycle_length
    else:
        CACHE[matrix_as_str] = cycle
    cycle += 1

matrix = convert_to_2d(matrix_as_str)
print("Part 2", calculate_weight(matrix))
