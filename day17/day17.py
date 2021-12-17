with open('data.dat') as file:
    data = [line.strip() for line in file][0]

raw_x, raw_y = data.split(':')[1].split(',')

target_x1, target_x2 = map(int, raw_x.split('=')[1].split('..'))
target_y1, target_y2 = map(int, raw_y.split('=')[1].split('..'))

def probe_in_target(pos):
    return pos[0] >= target_x1 and pos[0] <= target_x2 and pos[1] >=target_y1 and pos[1] <= target_y2

def probe_beyond_target(pos):
    return pos[0] > target_x2 or pos[1] < target_y2

Trajectories = {}

def fire_probe(pos, vel, max_y = 0):
    if probe_in_target(pos):
        print('Bullseye')
        return max_y


    posX = pos[0] + vel[0]
    posY = pos[1] + vel[1]
    max_y = max(max_y, posY)

    if vel[0] > 0:
        velX = vel[0] - 1

    if vel[0] < 0:
        velX = vel[0] + 1

    if vel[0] == 0:
        velX = 0

    velY = vel[1] - 1

    Trajectories[vel] = posY

    if probe_beyond_target(pos):
        del Trajectories[vel]
        return

    return fire_probe((posX, posY), (velX, velY), max_y)

def part_one():
    pos = (0, 0)
    max_y = 0
    for x in range(1, 300):
        for y in range(1, 300):
            Trajectories[(x, y)] = 0
            max_y = max(max_y, fire_probe(pos, (x, y)))

    print(max_y)

part_one()
