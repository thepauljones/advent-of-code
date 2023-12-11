from os import getcwd
from pathlib import Path

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()


def get_adjacent(j, i, data):
    adjs = []
    if j < len(data) - 1:
        adjs.append((data[j + 1][i], (j + 1, i)))  # South

    if j >= 1:
        adjs.append((data[j - 1][i], (j - 1, i)))  # North

    if i < len(data[j]) - 1:  # East
        adjs.append((data[j][i + 1], (j, i + 1)))

    if i >= 1:
        adjs.append((data[j][i - 1], (j, i - 1)))  # West

    assert len(adjs) < 5

    return adjs


def get_connected(pos, prevPos):
    y, x = pos
    adjs = get_adjacent(y, x, field[:])

    result = []

    for adj in adjs:
        char, posA = adj
        localY, localX = posA

        if posA == prevPos:
            continue

        if localX == x:
            # same x, is underneath
            if localY > y and field[y][x] in ["|", "7", "F", "S"]:
                if char in ["|", "L", "J", "S"]:
                    return adj[1]
                    result.append(adj[1])

            # same x y is above
            if localY < y and field[y][x] in ["|", "J", "L", "S"]:
                if char in ["|", "7", "F", "S"]:
                    return adj[1]
                    result.append(adj[1])

        if localY == y:
            # is to the right
            if localX > x and field[y][x] in ["-", "L", "F", "S"]:
                if char in ["-", "7", "J", "S"]:
                    return adj[1]
                    result.append(adj[1])

            if localX < x and field[y][x] in ["-", "7", "J", "S"]:
                if char in ["-", "F", "L", "S"]:
                    return adj[1]
                    result.append(adj[1])

    print('should never get here')
    exit()


def nodes_contain(nodes, target):
    result = False
    for node in nodes:
        if node[1] == target:
            result = True
            break

    return result


assert nodes_contain([("J", (2, 1)), ("|", (2, 0))], (2, 0)) is True

gab = [x for x in file.read().splitlines()]

field = []
for line in gab:
    field.append([x for x in line])

map = {}

# find start
startPos = (-1, -1)
for i, line in enumerate(field):
    if "S" in line:
        startPos = (i, line.index("S"))
# find start
#

pipe = [startPos]
checked = [startPos]

next = get_connected(startPos, startPos)
while next != startPos:
    pipe.append(next)
    next = get_connected(pipe[-1], pipe[-2])


print('Furthest point:', int(len(list(set(pipe))) / 2))

polyPoints = []

# reverse the order of the co-ordinates, using j, i for the 2d array stuff is handier, but the poly
# obviously wants x, y
for p in pipe:
    polyPoints.append((p[1], p[0]))

polygon = Polygon(polyPoints)
contained = 0
for j in range(len(field)):
    for i in range(len(field[0])):
        point = (j, i)
        if polygon.contains(Point(point)):
            contained += 1


print("Contained:", contained)
