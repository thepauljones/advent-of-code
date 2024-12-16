from pathlib import Path
from adjacents import get_adjacent

# twopaths.txt:                3006         1012 CHECK
# twoturns.txt:                3004         1005 CHECK
# threeturns.txt:              3006            7 CHECK
# labyrinth.txt:             327848        29849 CHECK
# turnalot.txt:             3285637         8236 CHECK


script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

grid = [list(line.strip()) for line in data]

dirs = {}
dirs["^"] = (-1, 0)
dirs["v"] = (1, 0)
dirs[">"] = (0, 1)
dirs["<"] = (0, -1)

dirt = {
    (0, 1): ">",
    (0, -1): "<",
    (1, 0): "v",
    (-1, 0): "^",
}

all_dirs = [">", "v", "^", "<"]


def printWithPath(path):
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            if (j, i) in path:
                print("X", end="")
            else:
                print(grid[j][i], end="")
        print()


def getPos(contents):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == contents:
                return (j, i)


def find_path(start, end, field):
    frontier = []

    frontier.append((0, ">", start))
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0

    while len(frontier) > 0:
        _, dir, current = frontier.pop(0)

        if current == end:
            break

        for next_cost, next_dir, next_pos in get_adjacent(
            current[0], current[1], field, dir
        ):
            j, i = next_pos
            if field[j][i] == "#":
                continue
            new_cost = cost[current] + next_cost
            if next_pos not in cost or new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                came_from[next_pos] = current
                frontier.append((new_cost, next_dir, next_pos))
                frontier.sort()

    # traversed grid, now recreate path
    path = []
    path_cost = 0
    current = end

    while current != start:
        path.append(current)
        path_cost += cost[current]
        current = came_from[current]

    # path.append(start)
    path.reverse()

    for j, i in path:
        field[j][i] = "0"

    return path, path_cost


path, cost = find_path(getPos("S"), getPos("E"), grid)


def getTurns(path):
    turns = 0
    dir = ">"
    current = path[0]

    if current is not None:
        for p in path[1:]:
            newDir = dirt[(p[0] - current[0], p[1] - current[1])]

            if dir != newDir:
                turns += 1

            current = p
            dir = newDir

    return turns * 1000


print(len(path))
print("Total score:", len(path) + getTurns(path))

# 41476 too low
# 107476 too high
# 107475 too high
# 106476 too low!!
#
# 106477 wrong
# 106478 also wrong
