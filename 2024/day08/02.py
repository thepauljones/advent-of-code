from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()
ants = {}
grid = []
j = 0

for line in data:
    grid.append(list(map(str.strip, line.strip())))
    i = 0
    for item in grid[-1]:
        if item != '.':
            if item in ants:
                ants[item].append((j, i))
            else:
                ants[item] = [(j, i)]
                
        i += 1
    j+= 1


def get_vector(a, b):
    return (b[0] - a[0], b[1] - a[1])

def add_vector(to, vec):
    res = (to[0] + vec[0], to[1] + vec[1])
    return res

antinodes = {}
def place_antinode(pos, sat):
    global antinodes
    j, i = pos
    if j < 0 or i < 0:
        return False
    if j > len(grid) - 1 or i > len(grid[0]) - 1:
        return False

    if sat in antinodes:
        if pos not in antinodes[sat]:
            antinodes[sat].append(pos)
    else:
        antinodes[sat] = [pos]

    return True

for sat in ants.keys():
    matches = ants[sat]
    for match in matches:
        for cmatch in matches:
            if match == cmatch:
                continue

            vec = get_vector(match, cmatch)
            check_pos = add_vector(cmatch, vec)

            placed = place_antinode(check_pos, sat)
            placed = place_antinode(cmatch, sat)
            placed = place_antinode(match, sat)

            if placed:
                place_antinode(cmatch, sat)

            while placed:
                check_pos = add_vector(check_pos, vec)
                placed = place_antinode(check_pos, sat)

all = []
for val in antinodes.values():
    all += val

print(all)


for j in range(len(grid)):
    for i in range(len(grid[0])):
        if (j, i) in all and grid[j][i] == ".":
            print('#', end="")
        else:
            print(grid[j][i], end="")

    print()

print(len(list(set(all))))
