from pathlib import Path
from collections import defaultdict

file = open(Path(__file__).with_name("input.txt"))
input = [int(x) for x in file.readline().strip().split(" ")]

# Cached result for each level
bktr = defaultdict(lambda: defaultdict(lambda: -1))


def recurse(val, step, max_steps):
    if step == max_steps:
        return 1

    if bktr[step][val] != -1:
        return bktr[step][val]

    res = 0

    if val == 0:
        res = recurse(1, step + 1, max_steps)
    elif len(str(val)) % 2 == 0:
        val_str = str(val)
        len_val_str = len(val_str)
        half = len_val_str // 2
        l = val_str[:(half)]
        r = val_str[(half):]
        lr = recurse(int(l), step + 1, max_steps)
        rr = recurse(int(r), step + 1, max_steps)
        res = lr + rr
    else:
        res = recurse(val * 2024, step + 1, max_steps)

    bktr[step][val] = res

    return res


part1 = 0
for x in input:
    part1 += recurse(x, 0, 25)

# Reset bkktr
bktr = defaultdict(lambda: defaultdict(lambda: -1))
part2 = 0
for x in input:
    part2 += recurse(x, 0, 75)


print("Part 1:", part1)
print("Part 2:", part2)
