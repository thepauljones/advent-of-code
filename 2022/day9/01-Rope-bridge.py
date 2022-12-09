from pathlib import Path
import time
import math

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

data = [x.split(' ') for x in file.read().splitlines()]

script_location = Path(__file__).absolute().parent
file_location = script_location / 'mirror-data.dat'
file = file_location.open()

mirror_data = [x.split(' ') for x in file.read().splitlines()]

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

real_data = [x.split(' ') for x in file.read().splitlines()]

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

    dis = math.sqrt(pow(tail[0] - head[0], 2) + pow(tail[1] - head[1], 2))
    if (dis < 1.5):
        return head, tail

    # Diagonal
    if dx > 0 and dy > 0:
        tail = (tail[0] + 1, tail[1] + 1)
    elif dx < 0 and dy > 0:
        tail = (tail[0] - 1, tail[1] + 1)
    elif dx > 0 and dy < 0:
        tail = (tail[0] + 1, tail[1] - 1)
    elif dx < 0 and dy < 0:
        tail = (tail[0] - 1, tail[1] - 1)
    # Adjacent
    else:
        if dx > 1:
            tail = (tail[0] + 1, tail[1])

        if dx < -1:
            tail = (tail[0] - 1, tail[1])

        if dy > 1:
            tail = (tail[0], tail[1] + 1)

        if dy < -1:
            tail = (tail[0], tail[1] - 1)

    return head, tail


def show(head, tail):
    line = []
    min_size = 16
    max_x = max([x[0] for x in [head, tail]]) + 1
    max_y = max([x[1] for x in [head, tail]]) + 1

    min_x = min([x[0] for x in [head, tail]]) - 1
    min_y = min([x[1] for x in [head, tail]]) -1 

    max_x = max(max_x, min_size)
    max_y = max(max_y, min_size)

    print('\n')

    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            if (x == head[0] and y == head[1]):
                line.append('H')

            elif (x == tail[0] and y == tail[1]):
                line.append('T')

            elif (x == 0 and y == 0):
                line.append('0')

            else:
                line.append('.')

        line.append('\n')

    line.append('\n')

    print(''.join(line))

def print_trail(trail):
    line = []
    min_size = 8
    max_x = max([x[0] for x in trail]) + 1
    max_y = max([x[1] for x in trail]) + 1

    min_x = min([x[0] for x in trail]) - 1
    min_y = min([x[1] for x in trail]) - 1

    max_x = max(max_x, min_size)
    max_y = max(max_y, min_size)

    print('\n')

    count = 0
    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            if (x, y) in trail:
                line.append('#')
                count += 1
            else:
                line.append('.')

        line.append('\n')
    line.append('\n')


    print(''.join(line))
    print('tail visited', count, 'locations')


def solve(ins):
    head = (0, 0)
    tail = (0, 0)

    trail = []
    
    for instruction in ins:
        steps = 0
        while steps < int(instruction[1]):
            head, tail = move(instruction[0], head, tail)
            trail.append(tail)
            steps += 1
            # show(head, tail)

    print_trail(trail)

solve(data)
solve(mirror_data)
solve(real_data)

def test():
    assert solve() == 0
