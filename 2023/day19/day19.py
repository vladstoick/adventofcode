from pathlib import Path
import queue
import regex

p = Path(__file__).with_name("input.txt")
file = open(p)

# Parsing
workflows = {}

lines = file.read().splitlines()
i = 0
while len(lines[i]) > 0:
    line = lines[i]
    i += 1

    [name, rulesStr] = regex.findall("(\w+){(.*)}", line)[0]
    rules = []

    for rule in rulesStr.split(","):
        if rule.count(':') == 0:
            rules.append((None, rule))
        else:
            [valToCompare, condition, numToCompare, ifTrue] = regex.findall(
                "(\w+)(<|>)(\d+):(\w+)", rule)[0]
            greater = True if condition == ">" else False
            rules.append(
                ((valToCompare, greater, int(numToCompare)), ifTrue))

    workflows[name] = rules

i += 1

parts = []
while i < len(lines):
    line = lines[i]
    i += 1

    numsStr = regex.findall("(\w)=(\d+)", line)
    nums = {}
    for pair in numsStr:
        nums[pair[0]] = int(pair[1])
    parts.append(nums)

valid_ranges_for_approve = []


def is_range_valid(range):
    for val in range.values():
        if val[0] > val[1]:
            return False
    return True


def calculate_range(condition, currentRange):
    [rangeToModify, greater, value] = condition
    rangeIfTrue = currentRange.copy()
    rangeIfFalse = currentRange.copy()
    if greater:
        rangeIfTrue[rangeToModify] = (
            value + 1, currentRange[rangeToModify][1])
        rangeIfFalse[rangeToModify] = (currentRange[rangeToModify][0], value)
        return (rangeIfTrue, rangeIfFalse)
    else:
        rangeIfTrue[rangeToModify] = (
            currentRange[rangeToModify][0], value - 1)
        rangeIfFalse[rangeToModify] = (value, currentRange[rangeToModify][1])
        return (rangeIfTrue, rangeIfFalse)


def dfs(elem, range):
    if elem == "A":
        valid_ranges_for_approve.append(range)
        return
    elif elem == "R":
        return

    for [condition, next] in workflows[elem]:
        if condition == None:
            dfs(next, range)
        else:
            (rangeIfTrue, rangeIfFalse) = calculate_range(condition, range)
            if is_range_valid(rangeIfTrue):
                dfs(next, rangeIfTrue)

            if is_range_valid(rangeIfFalse):
                range = rangeIfFalse
            else:
                return


dfs("in", {
    "x": (1, 4000),
    "m": (1, 4000),
    "a": (1, 4000),
    "s": (1, 4000),
})

part1 = 0
for part in parts:
    matches = False

    for valid_range in valid_ranges_for_approve:
        matches_range = True
        for (category, range) in valid_range.items():
            if not (part[category] >= range[0] and part[category] <= range[1]):
                matches_range = False
                break
        if matches_range:
            matches = True
            break

    if matches:
        part1 += sum(part.values())

print("Part 1", part1)

part2 = 0
for valid_range in valid_ranges_for_approve:
    options = 1
    for val in valid_range.values():
        options *= (val[1] - val[0] + 1)
    part2 += options
print("Part 2", part2)
