from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
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

def place_antinode(pos):
    j, i = pos
    if j < 0 or i < 0:
        return
    if j > len(grid) - 1 or i > len(grid[0]) - 1:
        return

    if grid[j][i] == ".":
        grid[j][i] = "#"

for sat in ants.keys():
    matches = ants[sat]
    print("Processing:", sat)
    for match in matches:
        for cmatch in matches:
            if match == cmatch:
                continue

            vec = get_vector(match, cmatch)
            check_pos = add_vector(cmatch, vec)

            place_antinode(check_pos)

count = 0
for line in grid:
    print("".join(line))
    for char in line:
        if char == "#":
            count += 1

print(count)
