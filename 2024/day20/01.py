from pathlib import Path
from a_star import find_path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read()

grid = [list(x.strip()) for x in data.split("\n")]


def printGrid(grid):
    for line in grid:
        print("".join(line))


def getPos(char):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == char:
                return (j, i)


start = getPos("S")
end = getPos("E")

path = find_path(start, end, grid)

paths = []
for j in range(1, len(grid) - 1):
    for i in range(1, len(grid[0]) - 1):
        if grid[j][i] == "#":
            grid[j][i] = "."
            print("checking", j, i, len(paths))
            c = find_path(start, end, grid)
            if len(path) - len(c) >= 100:
                paths.append(c)
            grid[j][i] = "#"
        else:
            continue


print(len(paths))
# 10003 - too high
