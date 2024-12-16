def get_adjacent(j, i, data, dir):
    adjs = []

    if j < len(data) - 1:
        adjs.append((1 if dir == "v" else 1001, "v", (j + 1, i)))  # South

    if j >= 1:
        adjs.append((1 if dir == "^" else 1001, "^", (j - 1, i)))  # North

    if i < len(data[j]) - 1:  # East
        adjs.append((1 if dir == ">" else 1001, ">", (j, i + 1)))

    if i >= 1:
        adjs.append((1 if dir == "<" else 1001, "<", (j, i - 1)))  # West

    return adjs
