def get_adjacent(j, i, data):
    adjs = []

    if (j < len(data) - 1):
        adjs.append((data[j+1][i],(j + 1, i))) # South

    if (j >= 1):
        adjs.append((data[j - 1][i], (j - 1, i)))  # North

    if (i < len(data[j]) - 1):# East
        adjs.append((data[j][i + 1], (j, i+ 1)))

    if (i >= 1):
        adjs.append((data[j][i - 1], (j, i - 1))) # West

    return adjs

def get_adjacent_with_diag(j, i, data):
    adjs = []
    if (j < len(data) - 1):
        adjs.append((data[j+1][i], (j+1, i))) # South
        if i >= 1:
            adjs.append((data[j+1][i-1], (j+1, i-1))) # South-West
        if i < len(data[0]) - 1:
            adjs.append((data[j+1][i+1], (j+1, i+1))) # South-East

    if (j >= 1):
        adjs.append((data[j - 1][i], (j-1, i)))  # North
        if i >= 1:
            adjs.append((data[j - 1][i - 1], (j-1, i-1)))  # North-West
        if i < len(data[0]) - 1:
            adjs.append((data[j-1][i+1], (j-1, i+1))) # North-East

    if (i < len(data[j]) - 1):# East
        adjs.append((data[j][i + 1], (j, i+1)))

    if (i >= 1):
        adjs.append((data[j][i - 1], (j, i-1))) # West

    return adjs
