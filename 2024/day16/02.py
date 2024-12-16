from pathlib import Path
from adjacents import get_adjacent

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

grid = [list(line.strip()) for line in data]

dirs = {}
dirs["^"] = (-1, 0)
dirs["v"] = (1, 0)
dirs[">"] = (0, 1)
dirs["<"] = (0, -1)

all_dirs = [">", "v", ">", "<"]


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
        for i in range(len(grid[j])):
            if grid[j][i] == contents:
                return j, i


def find_path(start, end, field):
    frontier = []

    frontier.append((0, start))
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0

    while len(frontier) > 0:
        _, current = frontier.pop(0)

        if current == end:
            break

        for next_cost, next_pos in get_adjacent(current[0], current[1], field):
            print(next_cost, next_pos)
            j, i = next_pos
            if field[j][i] == "#":
                continue
            new_cost = cost[current] + next_cost
            if next_pos not in cost or new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                came_from[next_pos] = current
                frontier.append((new_cost, next_pos))
                frontier.sort()

    # traversed grid, now recreate path
    path = []
    path_cost = 0
    current = end

    while current != start:
        path.append(current)
        path_cost += cost[current]
        current = came_from[current]

    path.append(start)

    for j, i in path:
        field[j][i] = "0"

    path.reverse()
    return path


path = find_path(getPos("S"), getPos("E"), grid)

printWithPath(path)

print(len(path))
