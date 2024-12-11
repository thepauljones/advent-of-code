from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

forest = []

for line in data:
    forest.append(list(map(int, list(line.strip()))))

def get_next_step_from(val, pos):
    j, i = pos
    adjs = []
    if j < len(forest) - 1:
        cand = (forest[j + 1][i], (j + 1, i)) # South
        if cand[0] - val ==1:
            adjs.append(cand)

    if j >= 1:
        cand = (forest[j - 1][i], (j - 1, i))  # North
        if cand[0] - val ==1:
            adjs.append(cand)

    if i < len(forest[j]) - 1:
        cand = (forest[j][i + 1], (j, i + 1))  # East
        if cand[0] - val ==1:
            adjs.append(cand)

    if i >= 1:
        cand = (forest[j][i - 1], (j, i - 1))  # West
        if cand[0] - val ==1:
            adjs.append(cand)

    assert len(adjs) < 5

    return adjs

routes = {}
paths = []
def get_trailheads():
    for j in range(len(forest)):
        for i in range(len(forest[0])):
            if forest[j][i] == 0:
                routes[(j, i)] = (0,(j, i))

get_trailheads()


total = 0
def walk_from(point):
    global total
    val, pos = point
    next_steps = get_next_step_from(val, pos)
    paths = {}
    for s in next_steps:
        print("s", s)
        if s[0] == 9:
            total += 1
        paths[s[1]] = walk_from(s)

    print(paths)


for k in routes:
    walk_from(routes[k])

print(total)
