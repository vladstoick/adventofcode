from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = [line for line in file.readlines() if line.strip()]

vals = []
valsPart2 = []

operations = lines[len(lines) - 1].split()

for op in operations:
    vals.append(1 if op == '*' else 0)
    valsPart2.append(1 if op == '*' else 0)
    

for line in lines[:(len(lines) - 1)]:
    for num, i in enumerate(line.split()):
        if operations[num] == '*':
            vals[num] *= int(i)
        else:
            vals[num] += int(i)
            
part1 = sum(vals)
print("Part 1", part1)
    
idx = 0
for num in range(len(lines[0]) - 1):
    isAllWhitespace = True
    
    val = 0
    for x in range(len(lines) - 1):
        if lines[x][num] != ' ':
            isAllWhitespace = False
            val = val * 10 + int(lines[x][num])
    
    if isAllWhitespace:
        idx += 1
    else:
        if operations[idx] == '*':
            valsPart2[idx] *= int(val)
        else:
            valsPart2[idx] += int(val) 

print("Part 2", sum(valsPart2))