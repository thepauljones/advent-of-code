from pathlib import Path
import time

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

data = [x.split(' ') for x in file.read().splitlines()]

def move(d, head, tail):
    if d == 'R':
        head = (head[0] + 1, head[1])

    if d == 'U':
        head = (head[0], head[1] + 1)

    if d == 'L':
        head = (head[0] - 1, head[1])

    if d == 'D':
        head = (head[0], head[1] - 1)

    directionVector = (head[0] - tail[0], head[1] - tail[1])

    dx, dy = directionVector

    if dx > 0 and dy > 0:
        tail = (tail[0] + 1, tail[1] + 1)
    elif dx < 0 and dy < 0:
        tail = (tail[0] - 1, tail[1] - 1)
    else:
        if dx > 1:
            tail = (tail[0] + 1, tail[1])
        if dx < 1:
            tail = (tail[0] - 1, tail[1])

        if dy > 1:
            tail = (tail[0], tail[1] + 1)

        if dy < 1:
            tail = (tail[0], tail[1] - 1)

    return head, tail


def show(head, tail):
    line = []
    for y in range(6, -1, -1):
        for x in range(0, 6):
            if (x == head[0] and y == head[1]):
                line.append('H')

            elif (x == tail[0] and y == tail[1]):
                line.append('T')

            else:
                line.append('.')

        line.append('\n')

    line.append('\n')

    print(''.join(line))

def print_trail(trail):
    line = []
    for y in range(6, -1, -1):
        for x in range(0, 6):
            if (x, y) in trail:
                line.append('#')
            else:
                line.append('.')

        line.append('\n')
    line.append('\n')

    print(''.join(line))



def solve(ins):
    head = (0, 0)
    tail = (0, 0)

    trail = []

    for instruction in ins[0:2]:
        steps = 0
        while steps < int(instruction[1]):
            head, tail = move(instruction[0], head, tail)
            trail.append(tail)
            steps += 1
            show(head, tail)

    print_trail(trail)

    return 0

solve(data)


def test():
    assert solve() == 0
