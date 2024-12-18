from adjacents import get_adjacent


# Returns either the path or False if no path is found
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
        if current not in cost:
            return False
        path_cost += cost[current]
        current = came_from[current]

    path.append(start)

    path.reverse()
    return path
