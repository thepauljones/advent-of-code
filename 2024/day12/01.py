from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()
grid = []

groups = {}
processed = []

def get_adjacent(pos, data, debug = False):
    j, i = pos
    adjs = []
    letter = data[j][i]

    if j >= 1:
        cand = (data[j - 1][i], (j - 1, i))  # North
        l, pos = cand
        if l == letter:
            adjs.append(pos) 

    if i < len(data[j]) - 1:  # East
        cand = (data[j][i + 1], (j, i + 1))
        l, pos = cand
        if l == letter:
            adjs.append(pos)

    if i >= 1:
        cand = (data[j][i - 1], (j, i - 1)) # West
        l, pos = cand
        if l == letter:
            adjs.append(pos)  

    if j < len(data) - 1: # South
        cand = (data[j + 1][i], (j + 1, i))
        l, pos = cand
        if l == letter:
            adjs.append(pos) 


    if debug:
        print("Letter", adjs)

    assert len(adjs) < 5

    return adjs

for line in data:
    grid.append(list(map(str.strip, line.strip())))


for j in range(len(grid)):
    for i in range(len(grid[0])):
        letter = grid[j][i]
        cand = (j, i)
        if cand not in groups and cand not in processed:
            groups[cand] = [cand]
            test = get_adjacent(cand, grid)
            while len(test) > 0:
                spot = test.pop()
                if spot not in groups[cand]:
                    groups[cand].append(spot)
                    processed.append(spot)
                    adjs = get_adjacent(spot, grid)
                    for a in adjs:
                        test.append(a)

def pGroup(pos):
    if pos not in groups:
        print("Group not found")

    print(len(groups[pos]))

    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if (j, i) in groups[pos]:
                print("X", end="")
            else:
                print(grid[j][i], end="")
        print()

def getArea(pos):
    return len(groups[pos])

def getPerimeter(pos):
    ans = 0
    for p in groups[pos]:
        ans += 4 - len(get_adjacent(p, grid))

    return ans

ans = 0
for group in groups:
    ans += getArea(group) * getPerimeter(group)

print(ans)
