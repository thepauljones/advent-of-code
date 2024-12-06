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
initial_guard_pos = guard_pos

j = 0
for line in data:
    rline = list(line.strip())
    for o in orientations.keys():
        if o in rline:
            guard_pos = (o, (j, rline.index(o)))
            initial_guard_pos = (o, (j, rline.index(o)))
    room.append(rline)
    j += 1

num_obstacles_in_room = 0
for line in room:
    for pos in line:
        if pos == "#":
            num_obstacles_in_room += 1


def move(guard_pos, room):
    dir, pos = guard_pos
    next_position = (pos[0] + orientations[dir][0], pos[1] + orientations[dir][1])

    # Walked out of room
    if next_position[0] < 0 or next_position[0] > len(room) - 1 or next_position[1] < 0 or next_position[1] > len(room[0]) - 1:
        return -1

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

def test_room(room, walked):
    while True:
        guard_pos = move(walked[-1], room)

        if guard_pos == -1:
            return False

        if guard_pos in walked:
            return True

        walked.append(guard_pos)

def get_path(room, walked):
    while True:
        guard_pos = move(walked[-1], room)
        if guard_pos == True:
            break
        if guard_pos == -1:
            return walked
        walked.append(guard_pos)


path = get_path(room, [initial_guard_pos])


loops = []
for step in path:
    j, i = step[1]
    if room[j][i] == "#" or room[j][i] == "^":
        continue
    temp = room[j][i]
    room[j][i] = "#"
    isLoop = test_room(room, [initial_guard_pos])
    if isLoop:
        loops.append((j, i))

    room[j][i] = temp

print(len(list(set(loops)))) # -1 because the initial guard position is also counted as a position which can't have an obstacle added

