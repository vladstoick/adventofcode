from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = [line for line in file.readlines() if line.strip()]

idx = set([lines[0].index("S")])

part1 = 0

for line in lines[1:]:
    newIdx = set()
    
    for i in range(len(line)):
        if i in idx:
            if line[i] == '.':
                newIdx.add(i)
            else:
                part1 += 1
                newIdx.add(i-1)
                newIdx.add(i+1)
    
    idx = newIdx
                
print("Part 1", part1)

poss = dict()
poss[lines[0].index("S")] = 1

for line in lines[1:]:
    newPoss = dict()
    
    keys = list(poss.keys())
    
    for i in range(len(line)):
        if i in keys:
            if line[i] == '.':
                newPoss[i] = newPoss.get(i, 0) + poss[i]
            else:
                newPoss[i-1] = newPoss.get(i-1, 0) + poss[i]
                newPoss[i+1] = newPoss.get(i+1, 0) + poss[i]

    poss = newPoss
    
part2 = sum(poss.values())
print("Part 2", part2)