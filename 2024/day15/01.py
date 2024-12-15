from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()

dirs = {}
dirs["^"] = (-1, 0)
dirs["v"] = (1, 0)
dirs[">"] = (0, 1)
dirs["<"] = (0, -1)

rawGrid, rawIns = data.split("\n\n")

grid = [list(x) for x in rawGrid.split("\n")]

vex = []
for line in rawIns.split():
    vex = vex + list(line)


def printGrid():
    for line in grid:
        print("".join(line))

    print()
    print()


def getRobotPos():
    r = (0, 0)
    for i in range(len(grid)):
        if "@" in grid[i]:
            r = (i, grid[i].index("@"))

    print(r, "shit")

    return r


def move(pos, dir):
    next = (pos[0] + dir[0], pos[1] + dir[1])

    posContents = grid[pos[0]][pos[1]]

    # Out of bounds check not required, grid is walled with #s
    if grid[next[0]][next[1]] == "O":
        move(next, dir)

    # Wall
    if grid[next[0]][next[1]] == "#":
        return

    # Next is empty - move
    elif grid[next[0]][next[1]] == ".":
        grid[next[0]][next[1]] = posContents
        grid[pos[0]][pos[1]] = "."


for dir in vex:
    print(getRobotPos(), dir)
    move(getRobotPos(), dirs[dir])


def getGPS(pos):
    return 100 * pos[0] + pos[1]


def getALLGPS():
    ans = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "O":
                ans += getGPS((j, i))

    print(ans)


getALLGPS()

# 1406619 -- too low
