from pathlib import Path

p = Path(__file__).with_name("input.txt")
file = open(p)

matrix = [[c for c in line.strip()] for line in file.readlines()]
rows = len(matrix)
cols = len(matrix[0])

def compute_around(r, c):
    total = 0
    directions = [(-1, -1,), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    for dr, dc in directions:
        rr = r + dr
        cc = c + dc

        if 0 <= rr < rows and 0 <= cc < cols:
            total += 1 if matrix[rr][cc] == '@' else 0
    return total


part1 = 0

for r in range(rows):
    for c in range(cols):
        around = compute_around(r, c)
        if matrix[r][c] == '@' and around < 4:
            part1 += 1

print("Part 1", part1)

has_change = True
part2 = 0

while has_change:
    has_change = False
    new_matrix = [[c for c in line] for line in matrix]

    for r in range(rows):
        for c in range(cols):
            around = compute_around(r, c)

            if matrix[r][c] == '@' and around < 4:
                new_matrix[r][c] = '.'
                has_change = True
                part2 += 1

    matrix = new_matrix

print("Part 2", part2)

