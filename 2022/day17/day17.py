from pathlib import Path
import regex as re
import sys

WIDTH = 7
D_COLUMN = 2
D_ROW = 3
MAX_HEIGHT = 0

def print_debug(matrix):
    print ("XXXX")
    for i in reversed(range(0, MAX_HEIGHT + D_ROW + 4)):
        vals = map( lambda p: '.' if p == 0 else '#', matrix[i])
        valsStr = "".join(vals)
        print("|" + valsStr + "|")
    
    print(9*"-")

def merge_rock(matrix, rock, i, j, copy = True):
    # We need to copy
    if copy:
        new_matrix = [row[:] for row in matrix]
    else:
        new_matrix = matrix
    for rockRow in range(len(rock)):
        for rockCol in range(len(rock[rockRow])):
            posI = i + rockRow
            posJ = j + rockCol
            new_matrix[posI][posJ] = rock[rockRow][rockCol]
    
    return new_matrix

def check_conflict(matrix, rock, i, j):
    for rockRow in range(len(rock)):
        for rockCol in range(len(rock[rockRow])):
            posI = i + rockRow
            posJ = j + rockCol
            if(rock[rockRow][rockCol] == 0):
                continue
                
            # are we still in bounds
            if posJ == -1 or posJ == WIDTH:
                return False
            
            # did we hit ground
            if posI == -1:
                return False
            
            # are we on conflict
            if matrix[posI][posJ]:
                return False
    
    return True


p = Path(__file__).with_name("input.txt")
p2 = Path(__file__).with_name("output.txt")
file = open(p)
sys.stdout = open(p2, 'w')

rocks = [
    [[1,1,1,1]],
    [
        [0,1,0],
        [1,1,1],
        [0,1,0]
    ],
    [
        [1,1,1],
        [0,0,1],
        [0,0,1],
    ],
    [
        [1],
        [1],
        [1],
        [1],
    ],
    [
        [1,1],
        [1,1]
    ]
]

jet = file.read()

matrix = []
for i in range(30000):
    matrix.append([0] * WIDTH)

jetIndex = 0

STEPS = 2022
for rockI in range(STEPS):
    rock = rocks[rockI % len(rocks)]

    i = MAX_HEIGHT + D_ROW
    j = D_COLUMN 
    if rockI == 414:
        print_debug(merge_rock(matrix, rock, i, j))
    while True:
        if rockI == 414:
            print(jet[jetIndex])
            print_debug(merge_rock(matrix, rock, i, j))
        dj = 1 if jet[jetIndex] == ">" else -1
        jetIndex = (jetIndex + 1) % len(jet)

        if(check_conflict(matrix, rock, i, j + dj)):
            j += dj

        if(check_conflict(matrix, rock, i - 1, j)):
            i -= 1
        else:
            break

        
    merge_rock(matrix, rock, i, j, False)
    
    currentHeight = i + len(rock)
    if currentHeight > MAX_HEIGHT:
        MAX_HEIGHT = currentHeight

print_debug(matrix)
print(jetIndex)
print("Part 1", MAX_HEIGHT)