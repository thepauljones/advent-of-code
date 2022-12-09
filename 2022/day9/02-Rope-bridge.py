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

def move(d, knots):
    print('moving')
    head = knots[0]
    if d == 'R':
        head = (head[0] + 1, head[1])

    if d == 'U':
        head = (head[0], head[1] + 1)

    if d == 'L':
        head = (head[0] - 1, head[1])

    if d == 'D':
        head = (head[0], head[1] - 1)

    knots[0] = head
    for i in range(1, len(knots)):
        head = knots[i - 1]
        tail = knots[i]

        directionVector = (head[0] - tail[0], head[1] - tail[1])

        dx, dy = directionVector

        print(knots)
        dis = math.sqrt(pow(tail[0] - head[0], 2) + pow(tail[1] - head[1], 2))
        if (dis < 1.5):
            knots[i - 1] = head
            knots[i] = tail
            return knots

        print(i, head, tail)

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

        knots[i - 1] = head
        knots[i] = tail

    return knots


def show(knots):
    line = []
    min_size = 16
    max_x = max([x[0] for x in knots]) + 1
    max_y = max([x[1] for x in knots]) + 1

    min_x = min([x[0] for x in knots]) - 1
    min_y = min([x[1] for x in knots]) -1 

    max_x = max(max_x, min_size)
    max_y = max(max_y, min_size)

    print('\n')

    for y in range(max_y, min_y, -1):
        for x in range(min_x, max_x):
            for i in range(0, len(knots)):
                if (x == knots[i][0] and y == knots[i][1]):
                    if i == 0:
                        line.append('H')
                    else:
                        line.append(str(i + 1))

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
    knots = [(0, 0)] * 10

    trail = []
    
    for instruction in ins:
        print(instruction)
        steps = 0
        while steps < int(instruction[1]):
            knots = move(instruction[0], knots)
            trail.append(knots[9])
            steps += 1

    
    print(knots)

    print_trail(trail)

solve(data)
solve(real_data)

def test():
    assert solve() == 0
