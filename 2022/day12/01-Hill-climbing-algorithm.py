from pathlib import Path
from adjacents import get_adjacent

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = [list(x) for x in file.read().splitlines()]

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
        field[j][i] = '\u2588'

    print_grid(field)
    path.reverse()
    return len(path) - 1


def print_grid(field):
    for line in field:
        print(''.join(str(''.join(line))))

def solve(field):
    for j in range(len(field[0]) - 1):
        for i in range(len(field) - 1):
            if field [i][j] == 'S':
                start = (i, j)
                field[i][j] = 'a'
            if field [i][j] == 'E':
                field[i][j] = 'z'
                end = (i, j)

    path = find_path(start, end, field)
    return path

result = solve(data)
print(result)

def test():
    assert solve() == 0
