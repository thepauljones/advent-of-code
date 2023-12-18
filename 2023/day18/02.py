from pathlib import Path
from tqdm import tqdm
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = tuple([tuple(x.split()) for x in file.read().splitlines()])

path = [(0, 0)]
for ins in data:
    _, _, col = ins

    dis = int("".join(col[2:7]), 16)
    dirNum = int(col[7], 16)

    if dirNum == 0:
        dir = "R"
    if dirNum == 1:
        dir = "D"
    if dirNum == 2:
        dir = "L"
    if dirNum == 3:
        dir = "U"

    vector = (0, 0)

    if dir == "R":
        vector = (0, dis)
    elif dir == "D":
        vector = (dis, 0)
    elif dir == "L":
        vector = (0, -dis)
    elif dir == "U":
        vector = (-dis, 0)

    newPos = (path[-1][0] + vector[0], path[-1][1] + vector[1])

    path.append(newPos)


# reverse the order of the co-ordinates, using j, i for the 2d array stuff is handier, but the poly
# obviously wants x, y


polygon = Polygon(path)

# I figured this out by taking the example answer, seeing that the area was similar
# then subtracting the example answer from the area and looking at the other properties
# of the polygon.
#
# The length happened to be about 2x the area, give or take the infernal (+-1 of AoC)
print("Answer", int(polygon.area + polygon.length / 2 + 1))


def solve():
    return 0


def test():
    assert solve() == 0
