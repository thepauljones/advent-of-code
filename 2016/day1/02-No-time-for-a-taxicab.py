i = 'R1, L4, L5, L5, R2, R2, L1, L1, R2, L3, R4, R3, R2, L4, L2, R5, L1, R5, L5, L2, L3, L1, R1, R4, R5, L3, R2, L4, L5, R1, R2, L3, R3, L3, L1, L2, R5, R4, R5, L5, R1, L190, L3, L3, R3, R4, R47, L3, R5, R79, R5, R3, R1, L4, L3, L2, R194, L2, R1, L2, L2, R4, L5, L5, R1, R1, L1, L3, L2, R5, L3, L3, R4, R1, R5, L4, R3, R1, L1, L2, R4, R1, L2, R4, R4, L5, R3, L5, L3, R1, R1, L3, L1, L1, L3, L4, L1, L2, R1, L5, L3, R2, L5, L3, R5, R3, L4, L2, R2, R4, R4, L4, R5, L1, L3, R3, R4, R4, L5, R4, R2, L3, R4, R2, R1, R2, L4, L2, R2, L5, L5, L3, R5, L5, L1, R4, L1, R1, L1, R4, L5, L3, R4, R1, L3, R4, R1, L3, L1, R1, R2, L4, L2, R1, L5, L4, L5'.split(', ')

pos = (0, 0)
direction = 0

dirs = ['North', 'East', 'South', 'West']

trail = []

def walk(direction, dist):
    global pos
    steps = 0

    while steps < dist:
        # North
        if direction == 0:
            pos = (pos[0], pos[1] + 1)

        # East
        if direction == 1:
            pos = (pos[0] + 1, pos[1])

        # South
        if direction == 2:
            pos = (pos[0], pos[1] - 1)

        # West
        if direction == 3:
            pos = (pos[0] - 1, pos[1])

        if trail.count(pos) > 0:
            print('Found', pos)
            print(abs(pos[0]) + abs(pos[1]))
            exit()

        trail.append(pos)

        steps += 1


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

