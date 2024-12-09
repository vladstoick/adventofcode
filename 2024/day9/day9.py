from pathlib import Path


def calculate_idx_sum(input):
    idx_sum = [0]
    for i in input:
        idx_sum.append(idx_sum[-1] + abs(i[0]))
    return idx_sum


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


def calculate(part2):
    input = parse()

    result = 0
    start = 0

    while start < len(input):
        if input[start][0] < 0:
            end = len(input) - 1
            while input[end][0] <= 0 or (part2 and input[end][0] > abs(input[start][0])) and end >= start:
                end -= 1

            if end < 0 or end < start:
                start += 1
                continue

            to_add = min(input[end][0], abs(input[start][0]))

            input[end] = modify(input[end], -to_add)
            id = input[end][1]
            input.insert(end, (-to_add, -1))
            input[start] = modify(input[start], to_add)
            input.insert(start, (to_add, id))

        start += 1
    id_so_far = 0

    for (c, id) in input:
        if id >= 0:
            positions_sum = sum_f(id_so_far, id_so_far + c - 1)
            multiplied_sum = positions_sum * id
            result += multiplied_sum
        id_so_far += abs(c)

    return result


print("part 1:", calculate(False))
print("part 2:", calculate(True))
