from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.readlines()
lines = list(filter(lambda line: line != "\n", lines))

# Parsing

seeds = [int(numStr) for numStr in lines[0].split(":")[1].strip().split(" ")]

rangesPerTransform = []
i = 2
while(i < len(lines)):
    ranges = []

    while(i < len(lines) and lines[i].count("to") == 0):
        nums = [int(numStr) for numStr in lines[i].strip().split(" ")]
        r = [nums[1], nums[1] + nums[2] - 1, nums[0] - nums[1]]
        ranges.append(r)
        i = i + 1
    
    i = i + 1

    rangesPerTransform.append(sorted(ranges))

# Solving

def is_range_valid(range):
    return range[0] <= range[1]

def calculate_intersection(range1, range2): # returns [leftRange, intersectionRange, rightRange]
    mergedRange = [max(range1[0], range2[0]), min(range1[1], range2[1])]
    return mergedRange if is_range_valid(mergedRange) else None

def merge(levelRange, transformRange):
    transformRangeAsValues = [transformRange[0], transformRange[1]]
    intersection = calculate_intersection(levelRange, transformRangeAsValues)

    if intersection is None:
        return [None, None, levelRange]
    else:
        leftRange = [levelRange[0],intersection[0] -1]
        leftRange = leftRange if is_range_valid(leftRange) else None
        
        mergedRange = [intersection[0] + transformRange[2], intersection[1] + transformRange[2]]

        rightRange = [intersection[1] + 1, levelRange[1]]
        rightRange = rightRange if is_range_valid(rightRange) else None
        return [leftRange, mergedRange, rightRange]


def solve(initialRanges):
    levels = [sorted(initialRanges)]
    
    for ranges in rangesPerTransform:
        prevLevel = levels[-1]
        nextLevel = []
        
        for levelRange in prevLevel:
            currentRange = levelRange
            for range in ranges:
                arr = merge(currentRange, range)
                
                for r in arr[0:2]:
                    if r is not None:
                        nextLevel.append(r)

                currentRange = arr[2]
                if currentRange is None:
                    break
            
            if currentRange is not None:
                nextLevel.append(currentRange)
        
        nextLevel = sorted(nextLevel)
        levels.append(nextLevel)


    return min(levels[-1])[0]

part1Ranges = [[i, i] for i in seeds]
print("Part 1", solve(part1Ranges))

part2Ranges = ([seeds[i*2], seeds[i*2] + seeds[i*2+1] - 1] for i in range(int(len(seeds) / 2)))
print("Part 2", solve(part2Ranges))
