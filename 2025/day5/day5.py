from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

ranges = []
ingredients = set()

for line in file.readlines():
    line = line.strip()
    if len(line) == 0:
        continue

    if line.count('-') > 0:
        parts = line.split('-')
        start = int(parts[0])
        end = int(parts[1])
        ranges.append((start, end))
    else:
        ingredients.add(int(line))

# Merge ranges
ranges.sort()
merged_ranges = []
current_start, current_end = ranges[0]
for start, end in ranges[1:]:
    if start <= current_end + 1:
        current_end = max(current_end, end)
    else:
        merged_ranges.append((current_start, current_end))
        current_start, current_end = start, end
merged_ranges.append((current_start, current_end))

part1 = 0
for ingredient in ingredients:
    for start, end in merged_ranges:
        if start <= ingredient <= end:
            part1 += 1
            break
print("Part 1", part1)


part2 = 0
for range_start, range_end in merged_ranges:
    part2 += (range_end - range_start + 1)
    
print("Part 2", part2)


