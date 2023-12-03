from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

lines = file.read().splitlines()
N = len(lines)
M = len(lines[0])

def print_debug(matrix):
    for i in range(N):
        vals = map( lambda p: str(p), matrix[i])
        print("\t".join(vals))


touching = []
idx = []
for i in range(N):
    touching.append([0] * M)
    idx.append([0] * M)

di = [-1, -1,  0,  1,  1,  1,  0, -1]
dj = [ 0,  1,  1,  1,  0, -1, -1, -1]
for i in range(N):
    for j in range(M):
        if not lines[i][j].isdigit() and not lines[i][j] == '.':
            for d in range(len(di)):
                newI = i + di[d]
                newJ = j + dj[d]

                if newI < 0 or newI == N or newJ < 0 or newJ == M:
                    continue

                touching[newI][newJ] = 1

part1 = 0
id = 1
numbers = {}
for i in range(N):
    number = 0
    hasAdjacent = False
    for j in range(M):
        if lines[i][j].isdigit():
            hasAdjacent = hasAdjacent or touching[i][j]
            number = number * 10 + int(lines[i][j])
            idx[i][j] = id
        else:
            if number > 0:
                numbers[id] = number
                if hasAdjacent:
                    part1 += number
                id = id + 1
                

            number = 0
            hasAdjacent = False
    
    if number > 0:
        numbers[id] = number
        if hasAdjacent:
            part1 += number

        id = id + 1

print("Part 1", part1)

part2 = 0
for i in range(N):
    for j in range(M):
        if not lines[i][j].isdigit() and not lines[i][j] == '.':
            adjacent = {}
            for d in range(len(di)):
                newI = i + di[d]
                newJ = j + dj[d]
                idOfIJ = idx[newI][newJ]

                if idOfIJ > 0:
                    adjacent[idOfIJ] = numbers[idOfIJ]
            
            if(len(adjacent) == 2):
                vals = list(adjacent.values())
                part2 += vals[0] * vals[1]

print("Part 2", part2)