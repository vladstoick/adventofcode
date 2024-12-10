from pathlib import Path


def parse():
    file = open(Path(__file__).with_name("input.txt"))
    input = [int(x) for x in file.readline().strip()]
    final_output = []
    for i in range(len(input)):
        if i % 2 == 1:
            final_output.append((input[i] * -1, -1))
        else:
            final_output.append((input[i], i // 2))

    return final_output


def modify(v, m):
    return (v[0] + m, v[1])


def sum_f(start, end):
    return ((end - start + 1) * (end + start)) // 2


def print_input(input):
    print('---')
    print(input)
    for (c, id) in input:
        for x in range(abs(c)):
            print(id if id >= 0 else '.', end="")
    print("")


def calculate(part2):
    input = parse()

    result = 0
    start = 0

    end = len(input) - 1

    while end >= 0:

        if input[end][0] >= 0:
            start = 0
            while (input[start][0] >= 0 or (part2 and abs(input[start][0]) < input[end][0])) and end > start:
                start += 1

            if end <= start:
                end -= 1
                continue

            to_add = min(input[end][0], abs(input[start][0]))

            if to_add == 0:
                end -= 1
                continue

            id = input[end][1]

            input[start] = modify(input[start], to_add)

            if input[start] == 0:
                del input[start]
                end -= 1

            input.insert(start, (to_add, id))
            end += 1

            input[end] = modify(input[end], -to_add)
            if input[end][0] == 0:
                del input[end]
                end -= 1

            input.insert(end + 1, (-to_add, -1))
            end += 1

            while end < len(input) and input[end - 1][0] < 0 and input[end][0] < 0:
                input[end - 1] = modify(input[end - 1], input[end][0])
                del input[end]

        end -= 1

    id_so_far = 0

    for (c, id) in input:
        if id >= 0:
            positions_sum = sum_f(id_so_far, id_so_far + c - 1)
            multiplied_sum = positions_sum * id
            result += multiplied_sum
        id_so_far += abs(c)

    print_input(input)

    return result


print("part 1:", calculate(False))
print("part 2:", calculate(True))
