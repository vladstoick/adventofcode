from pathlib import Path

prevVals = set()

def calculate_recurse(digits, start, end, currentVal, isPart1):
    index = len(currentVal)

    repetitions = 0 if index == 0 else int(digits / index)

    sum = 0

    if repetitions > 1 and digits % index == 0:
        if not isPart1 or repetitions == 2:
            buildNumber = int(currentVal * repetitions)
            
            if buildNumber >= start and buildNumber <= end and buildNumber not in prevVals:
                sum += buildNumber
                prevVals.add(buildNumber)
        
    if index > digits / 2:
        return sum
    

    startVal = 0 if index >0 else 1
    for val in range(startVal, 10):
        newVal = currentVal + str(val)
        result = calculate_recurse(digits, start, end, newVal, isPart1)

        sum += result

    return sum


def calculate(itemRange, isPart1):
    startStr, endStr = itemRange[0], itemRange[1]
    start, end = int(startStr), int(endStr)

    minDigits = len(startStr)
    maxDigits = len(endStr)

    sum = 0

    for digits in range(minDigits, maxDigits + 1):
        prevVals.clear()
        sum += calculate_recurse(digits, start, end, "", isPart1)

    return sum

p = Path(__file__).with_name("input.txt")
file = open(p)

bigLine = "".join(line.strip() for line in file.readlines())
itemRanges = [item.split("-") for item in bigLine.split(",")]

part1 = 0
part2 = 0

for itemRange in itemRanges:
    part1 += calculate(itemRange, True)
    part2 += calculate(itemRange, False)

print("Part 1", part1)
print("Part 2", part2)