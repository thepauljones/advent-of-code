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
file_location = script_location / 'test-data.dat'
file = file_location.open()

data = file.read().splitlines()

cave = []
for i in range(510):
    row = []
    for j in range(510):
        row.append('.')
    cave.append(row)

def draw_line(a, b):
    x0, y0 = a
    x1, y1 = b
    
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


@window.event
def on_draw():
    lines = []
    for y in range(len(cave)):
        for x in range(len(cave[y])):
            if cave[y][x] == '#':
                lines.append(shapes.Rectangle(x=x, y=550-y, width=1, height=1, color=(0, 244, 0), batch=batch))
    
    batch.draw()

pyglet.app.run()

def solve():
    return 0


def test():
    assert solve() == 0
