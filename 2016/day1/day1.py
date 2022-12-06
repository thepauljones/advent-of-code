i = 'R8, R4, R4, R8'.split(', ')

pos = (0, 0)
direction = 0

dirs = ['North', 'East', 'South', 'West']

trail = []

for step in i:
    turn = step[0:1]

    dist = int(step[1:])

    if turn == 'R':
        direction += 1
    else:
        direction -= 1

    if direction == 4:
        direction = 0

    if direction == -1:
        direction = 3

    walk(direction, dist)

def walk(direction, dist):
    steps = 0
    while steps < dist:

        steps += 1

