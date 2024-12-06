from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

orientations = {
    '^': (-1, 0),
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1)
}

room = []

guard_pos = ('^', (0, 0))

j = 0
for line in data:
    rline = list(line.strip())
    for o in orientations.keys():
        if o in rline:
            guard_pos = (o, (j, rline.index(o)))
    room.append(rline)
    j += 1


def move(guard_pos, room):
    dir, pos = guard_pos
    next_position = (pos[0] + orientations[dir][0], pos[1] + orientations[dir][1])

    # Walked out of room
    if next_position[0] < 0 or next_position[0] > len(room) - 1 or next_position[1] < 0 or next_position[1] > len(room[0]) - 1:
        print('Answer:', len(set(walked)))
        exit()

    # Walked into an empty space, no problem
    if room[next_position[0]][next_position[1]] == '.' or room[next_position[0]][next_position[1]] == '^':
        return (dir, next_position)

    if room[next_position[0]][next_position[1]] == '#':
        # get next orientation
        return (turn(dir), pos)

    print(guard_pos, 'STUCK')
    exit()

def turn(facing):
    os = list(orientations.keys())
    for i in range(len(os)):
        if os[i] == facing:
            if i + 1 > len(os) - 1:
                return os[0]
        else:
            continue

        return os[i + 1]

assert turn('^') == '>'
assert turn('>') == 'v'
assert turn('v') == '<'
assert turn('<') == '^'


walked = [guard_pos[1]]

while True:
    guard_pos = move(guard_pos, room)
    walked.append(guard_pos[1])

