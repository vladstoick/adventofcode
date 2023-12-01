from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

part1 = 0
part2 = 0

for line in file.readlines():
    numbersPart1 = re.findall(r'(\d)', line)


    valPart1 = int(numbersPart1[0]) * 10 + int(numbersPart1[-1])
    part1 += valPart1

    numbersPart2 = re.findall(r'((?:\d)|(?:one)|(?:two)|(?:three)|(?:four)|(?:five)|(?:six)|(?:seven)|(?:eight)|(?:nine))', line, overlapped=True)
    numbersPart2Converted = []
    for number in numbersPart2:
        if number in numbers:
            numbersPart2Converted.append(numbers.index(number))
        else:
            numbersPart2Converted.append(int(number))

    # print(numbersPart2)
    print(numbersPart2Converted)
    
    valPart2 = numbersPart2Converted[0] * 10 +numbersPart2Converted[-1]
    part2 += valPart2

print("Part 1: ", part1)
print("Part 2: ", part2)
