from adjacents import get_adjacent


def find_path(start, end, field):
    frontier = []

    frontier.append((0, start))
    came_from = {}
    cost = {}
    came_from[start] = None
    cost[start] = 0

    count = 0
    while len(frontier) > 0:
        _, current = frontier.pop(0)

        if current == end:
            break

        for next_cost, next_pos in get_adjacent(
            current[0],
            current[1],
            field,
        ):
            new_cost = cost[current] + next_cost
            if next_pos not in cost or new_cost < cost[next_pos]:
                cost[next_pos] = new_cost
                came_from[next_pos] = current
                frontier.append((new_cost, next_pos))
                frontier.sort()

        count += 1
    # traversed grid, now recreate path
    path = []
    path_cost = 0
    current = end

    while current != start:
        path.append(current)
        path_cost += cost[current]
        current = came_from[current]

    for j, i in path:
        field[j][i] = "0"

    # print_grid(field)
    path.reverse()
    return path
