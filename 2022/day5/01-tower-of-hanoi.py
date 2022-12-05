from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

rawtowers = []
instructions = []
stage = 1
for line in data:
    if line == '':
        stage = 2
        continue

    if stage == 1:
        rawtowers.append([str(x) for x in line])

    if stage == 2:
        rawmoves = line.split(' ')
        moves = rawmoves[1], rawmoves[3], rawmoves[5]
        instructions.append(moves)


def get_arrays_for_towers(raw):
    towers = []
    for i in range(len(raw) - 1, len(raw) - 2, -1):
        for j in range(len(raw[i]) - 2, 0, -4):
            towers.append((raw[i][j], []))

    for i in range(len(raw) - 2, -1, -1):
        count = 0
        for j in range(len(raw[i]) - 2, 0, -4):
            if raw[i][j] != ' ':
                towers[count][1].append(raw[i][j])
            count += 1

    return towers


towers = get_arrays_for_towers(rawtowers)

towers.reverse()


def move(tow, source, to):
    print('Move 1 from ', source, 'to', to, tow[source][1])
    val = tow[source][1].pop()
    tow[to][1].append(val)
    return tow


def perform_move(tow, ins):
    num, source, to = ins
    print(num, source, to)
    count = 0
    while count < int(num):
        tow = move(tow, int(source) - 1, int(to) - 1)
        count += 1

    return tow


for ins in instructions:
    towers = perform_move(towers, ins)


def get_tops(towers):
    result = []
    for tower in towers:
        result.append(tower[1][len(tower[1]) - 1])

    return ''.join(result)


print(get_tops(towers))
