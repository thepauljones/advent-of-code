from pathlib import Path
from copy import deepcopy
import pyglet
from pyglet.window import Window
from pyglet.gl import *
from pyglet import shapes

batch = pyglet.graphics.Batch()
window = pyglet.window.Window(width=1024, height=768)
pyglet.gl.glClearColor(0.5,0,0,1)

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()
sandPoint = (0, 500)

cave = []
for i in range(910):
    row = []
    for j in range(910):
        row.append('.')
    cave.append(row)

floor = 0

def draw_line(a, b):
    global floor
    x0, y0 = a
    x1, y1 = b
    
    floor = max(floor, y0, y1)

    if x0 == x1:
        for y in range(min(y0, y1), max(y0, y1) + 1):
            cave[y][x0] = '#'

    elif y0 == y1:
        for x in range(min(x0, x1), max(x0, x1) + 1):
            cave[y0][x] = '#'



for line in data:
    points = line.split(' -> ')
    for i in range(len(points) - 1): 
        draw_line([int(x) for x in points[i].split(',')], [int(x) for x in points[i + 1].split(',')])

for i in range(len(cave[0])):
    cave[floor + 2][i] = '#'

activeGrain = sandPoint
grains = []
while True:
    if cave[sandPoint[0]][sandPoint[1]] == 'o':
        for i in range(0, 20):
            for j in range(480, len(cave[i])):
                print(cave[i][j], end='')
            print('\n')
        print(len(grains))
        break
    if cave[activeGrain[0] + 1][activeGrain[1]] == '.':
        activeGrain = (activeGrain[0] + 1, activeGrain[1])
    # grain of sand directly below
    if cave[activeGrain[0] + 1][activeGrain[1]] == 'o' or cave[activeGrain[0] + 1][activeGrain[1]] == '#':
        #Air to the bottom left
        if cave[activeGrain[0] + 1][activeGrain[1] -1] == '.':
            activeGrain = (activeGrain[0] + 1, activeGrain[1] - 1)
        #Air to the bottom right
        elif cave[activeGrain[0] + 1][activeGrain[1] + 1] == '.':
            activeGrain = (activeGrain[0] + 1, activeGrain[1] + 1)
        else:
            # no air, spawn another
            grains.append((activeGrain[0], activeGrain[1]))
            cave[activeGrain[0]][activeGrain[1]] = 'o'
            activeGrain = (sandPoint[0], sandPoint[1])


@window.event
def on_draw():
    lines = []
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            if cave[y][x] == '#':
                lines.append(shapes.Rectangle(x=x, y=550-y, width=1, height=1, color=(0, 244, 0), batch=batch))
            if cave[y][x] == 'o':
                lines.append(shapes.Circle(x=x, y=550-y, radius=1, color=(50, 10, 230), batch=batch))

    batch.draw()

pyglet.app.run()

def solve():
    return 0


def test():
    assert solve() == 0
