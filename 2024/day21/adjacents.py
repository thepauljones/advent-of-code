def get_adjacent(j, i, grid):
    adjs = []

    if j < len(grid) - 1:
        if grid[j + 1][i] != "#":
            adjs.append((1, (j + 1, i)))  # South

    if j >= 1:
        if grid[j - 1][i] != "#":
            adjs.append((1, (j - 1, i)))  # North

    if i < len(grid[j]) - 1:
        if grid[j][i + 1] != "#":
            adjs.append((1, (j, i + 1)))  # East

    if i >= 1:
        if grid[j][i - 1] != "#":
            adjs.append((1, (j, i - 1)))  # West

    return adjs
