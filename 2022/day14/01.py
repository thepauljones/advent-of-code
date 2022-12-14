from pathlib import Path
from copy import deepcopy

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

cave = []
for i in range(510):
    row = []
    for j in range(510):
        row.append('.')
    cave.append(row)


def draw_line(a, b):
    print(a, b)
    x0, y0 = a
    x1, y1 = b

    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            print('printing # ', x0, y)
            cave[y][x0] = '#'
    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            print('printing # ', x, y0)
            cave[y0][x] = '#'


for line in data:
    points = line.split(' -> ')
    for i in range(len(points) - 1):
        draw_line([int(x) for x in points[i].split(',')], [int(x) for x in points[i + 1].split(',')])

def render_cave(cave):
    for y in range(0, 150):
        for x in range(390, 504):
            print(cave[y][x], end='')
        print('\n')

render_cave(cave)

def solve():
    return 0


def test():
    assert solve() == 0
