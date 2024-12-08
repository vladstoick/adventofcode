from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)


def check(items, mistakes_allowed):
    direction = 1 if items[1] > items[0] else -1

    for x in range(1, len(items)):
        dif = (items[x] - items[x-1]) * direction
        if dif < 1 or dif > 3:
            if mistakes_allowed:
                arr1 = items[:x] + items[x+1:]
                arr2 = items[:x-1] + items[x:]
                arr3 = items[:x-2] + items[x-1:]
                return check(arr1, False) or check(arr2, False) or check(arr3, False)
            else:
                return False

    return True


part1 = 0
part2 = 0
for line in file.readlines():
    items = list(map(int, line.split()))

    part1_check = check(items, False)
    part1 += 1 if part1_check else 0

    part2_check = check(items, True)
    part2 += 1 if part2_check else 0

print("Part 1: ", part1)
print("Part 2: ", part2)
