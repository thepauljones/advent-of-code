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
        if cand[0] == val + 1:
            adjs.append(cand)

    if j > 0:
        cand = (forest[j - 1][i], (j - 1, i))  # North
        if cand[0] == val + 1:
            adjs.append(cand)

    if i < len(forest[0]) - 1:
        cand = (forest[j][i + 1], (j, i + 1))  # East
        if cand[0] == val + 1:
            adjs.append(cand)

    if i > 0:
        cand = (forest[j][i - 1], (j, i - 1))  # West
        if cand[0] == val + 1:
            adjs.append(cand)

    assert len(adjs) < 5

    return adjs

routes = {}
def get_trailheads():
    for j in range(len(forest)):
        for i in range(len(forest[0])):
            if forest[j][i] == 0:
                routes[(j, i)] = [(j, i)]

get_trailheads()

def walk(pos):
    val = forest[pos[0]][pos[1]]
    if val == 9:
        return 1
    next_steps = get_next_step_from(val, pos)

    unique = 0
    for n in next_steps:
        v, p = n
        unique += walk(p)

    return unique

print(routes)

ans = 0
print(routes)
for a in routes:
    res = walk(a)
    print(res)
    ans += res

print(ans)
