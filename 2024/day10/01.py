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

    if j >= 1:
        cand = (forest[j - 1][i], (j - 1, i))  # North
        if cand[0] == val + 1:
            adjs.append(cand)

    if i < len(forest[j]) - 1:
        cand = (forest[j][i + 1], (j, i + 1))  # East
        if cand[0] == val + 1:
            adjs.append(cand)

    if i >= 1:
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

def walk(val, pos, dests):
    next = get_next_step_from(val, pos)

    for n in next:
        val, pos = n
        if val == 9:
            print(val, pos)
            if pos not in dests:
                dests.append(pos)

        walk(val, pos, dests)

    return len(dests)


all_dests = {}
for a in routes:
    res = walk(0, a, [])
    all_dests[a] = res

print(all_dests)

ans = 0
for a in all_dests:
    ans += all_dests[a]

print(ans)


