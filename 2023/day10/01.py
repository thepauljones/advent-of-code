from os import getcwd
from pathlib import Path

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


def get_connected(pos):
    y, x = pos
    adjs = get_adjacent(y, x, field[:])

    result = []

    for adj in adjs:
        char, posA = adj
        localY, localX = posA

        if localX == x:
            # same x, is underneath
            if localY > y and field[y][x] in ["|", "7", "F", "S"]:
                if char in ["|", "L", "J", "S"]:
                    result.append(adj[1])

            # same x y is above
            if localY < y and field[y][x] in ["|", "J", "L", "S"]:
                if char in ["|", "7", "F", "S"]:
                    result.append(adj[1])

        if localY == y:
            # is to the right
            if localX > x and field[y][x] in ["-", "L", "F", "S"]:
                if char in ["-", "7", "J", "S"]:
                    result.append(adj[1])

            if localX < x and field[y][x] in ["-", "7", "J", "S"]:
                if char in ["-", "F", "L", "S"]:
                    result.append(adj[1])

    return result


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

for item in checked:
    connected = get_connected(item)
    for conn in connected:
        if conn not in checked:
            pipe.append(conn)
            checked.append(conn)


print(len(list(set(pipe))) / 2)

for j in range(len(field)):
    for i in range(len(field[j])):
        if (j, i) in pipe:
            print("*", end="")
        else:
            print(field[j][i], end="")

    print()

# 8493 too high
