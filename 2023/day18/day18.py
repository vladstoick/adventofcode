from pathlib import Path
p = Path(__file__).with_name("input.txt")
file = open(p)

pointsPart1 = [(0, 0)]
pointsPart2 = [(0, 0)]
directions = {
    "U": [-1, 0],
    "D": [1, 0],
    "L": [0, -1],
    "R": [0, 1],
}

directionsPart2 = ["R", "D", "L", "U"]

for line in file.read().splitlines():
    values = line.split()
    directionPart1 = values[0]
    distancePart1 = int(values[1])
    pointsPart1.append((
        pointsPart1[-1][0] + directions[directionPart1][0] * distancePart1,
        pointsPart1[-1][1] + directions[directionPart1][1] * distancePart1,
    ))

    distancePart2 = int(values[2][2:-2], 16)
    directionPart2 = directionsPart2[int(values[2][-2])]

    pointsPart2.append((
        pointsPart2[-1][0] + directions[directionPart2][0] * distancePart2,
        pointsPart2[-1][1] + directions[directionPart2][1] * distancePart2,
    ))


def calculate(points):
    perimeter = 0
    area = 0

    # From day 11/10??, I remember seeing this shoelace algorithm mentioned in comments
    # Playig around, I found an issue with using just shoelace algorithm
    # For a square (0,0) -> (0,1) -> (1, 1) -> (0, 1) the area returned by
    # shoelace algorithm is 1 (kinda makes sense), but the area we want is actually
    # is a bit different as we want the number of points, rather than the area
    # 4. Searching around found pick's algorithm that says
    # area = points_inside + points_outside / 2 + 1
    # So we can combine the two to determine how many points
    for i in range(0, len(points) - 1):
        [curPointY, curPointX] = points[i]
        [nextPointY, nextPointX] = points[i + 1]

        perimeter += abs(curPointY - nextPointY) + abs(curPointX - nextPointX)

        area += int((curPointY + nextPointY) * (curPointX - nextPointX) / 2)

    inside = area - int((perimeter) / 2) + 1
    return inside + perimeter


print("Part 1", calculate(pointsPart1))
print("Part 2", calculate(pointsPart2))
