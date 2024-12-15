from pathlib import Path

dir = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}


def process_input():
    file = open(Path(__file__).with_name("input.txt"))
    lines = [list(line.strip()) for line in file.readlines()]

    input = []
    instructions = []

    for line in lines:
        if len(line) and line[0] == '#':
            input.append(line)
        elif len(line) > 0:
            instructions += line

    return input, instructions,


def find_start(input):
    starti, startj = None, None
    for i in range(len(input)):
        for j in range(len(input[0])):
            starti, startj = (i, j) if input[i][j] == '@' else (starti, startj)
    return starti, startj


def move_works(i, j, input, instruction):
    di, dj = dir[instruction]
    if input[i][j] == '#':
        return False
    elif input[i][j] == '.':
        return True
    elif input[i][j] == 'O' or input[i][j] == '@':
        ni, nj = i + di, j + dj
        return move_works(ni, nj, input, instruction)
    elif input[i][j] == '[' or input[i][j] == ']':
        lefti, leftj = (i, j) if input[i][j] == '[' else (i, j - 1)
        righti, rightj = (i, j) if input[i][j] == ']' else (i, j + 1)

        leftni, leftnj = lefti + di, leftj + dj
        rightni, rightnj = righti + di, rightj + dj

        works_left, works_right = True, True
        if instruction != '>':
            works_left = move_works(leftni, leftnj, input, instruction)
        if instruction != '<':
            works_right = move_works(rightni, rightnj, input, instruction)

        return works_left and works_right


def move(i, j, input, instruction):
    di, dj = dir[instruction]
    if input[i][j] == 'O' or input[i][j] == '@':
        ni, nj = i + di, j + dj

        move(ni, nj, input, instruction)

        input[ni][nj] = input[i][j]
        input[i][j] = '.'
    elif input[i][j] == '[' or input[i][j] == ']':
        lefti, leftj = (i, j) if input[i][j] == '[' else (i, j - 1)
        righti, rightj = (i, j) if input[i][j] == ']' else (i, j + 1)

        leftni, leftnj = lefti + di, leftj + dj
        rightni, rightnj = righti + di, rightj + dj

        if instruction != '>':
            move(leftni, leftnj, input, instruction)
        if instruction != '<':
            move(rightni, rightnj, input, instruction)

        input[lefti][leftj] = '.'
        input[righti][rightj] = '.'

        input[leftni][leftnj] = '['
        input[rightni][rightnj] = ']'


def calculate_result(input):
    result = 0
    for i in range(len(input)):
        for j in range(len(input[0])):
            if input[i][j] == 'O' or input[i][j] == '[':
                result += i * 100 + j
    return result


def process_instructions(input, instructions):
    curi, curj = find_start(input)
    for instruction in instructions:
        di, dj = dir[instruction]
        ni, nj = curi + di, curj + dj

        works = move_works(curi, curj, input, instruction)

        if works:
            move(curi, curj, input, instruction)
            curi, curj = ni, nj

    return input


def solve(part):
    input, instructions = process_input()

    if part == 2:
        orig_cols = len(input[0])
        for i in range(len(input)):
            nj = []
            for j in range(orig_cols):
                if input[i][j] == '#':
                    nj += ['#', '#']
                elif input[i][j] == 'O':
                    nj += ['[', ']']
                elif input[i][j] == '.':
                    nj += ['.', '.']
                elif input[i][j] == '@':
                    nj += ['@', '.']

            input[i] = nj

    input = process_instructions(input, instructions)
    print("Part", part, calculate_result(input))


solve(1)
solve(2)
