from pathlib import Path
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = tuple([tuple(x.split()) for x in file.read().splitlines()])

path = [(0, 0)]
minX = 0
minY = 0
maxX = 0
maxY = 0
for ins in data:
    dir, disStr, col = ins

    dis = int(disStr)

    pos = path[-1]

    vector = (0, 0)

    if dir == "R":
        vector = (0, 1)
    elif dir == "D":
        vector = (1, 0)
    elif dir == "L":
        vector = (0, -1)
    elif dir == "U":
        vector = (-1, 0)

    for i in range(dis):
        newPos = (path[-1][0] + vector[0], path[-1][1] + vector[1])

        minX = min(minX, newPos[1])
        maxX = max(maxX, newPos[1])

        minY = min(minY, newPos[0])
        maxY = max(maxY, newPos[0])

        path.append(newPos)

print(path)

# reverse the order of the co-ordinates, using j, i for the 2d array stuff is handier, but the poly
# obviously wants x, y

polygon = Polygon(path)

print(polygon.length)
print(polygon.area)

count = 0
for j in range(minY - 1, maxY + 1):
    for i in range(minX - 1, maxX + 1):
        if (j, i) in path or polygon.contains(Point(j, i)):
            print("#", end="")
            count += 1
        else:
            print(".", end="")
    print("\n")

print(count)


def solve():
    return 0


def test():
    assert solve() == 0
