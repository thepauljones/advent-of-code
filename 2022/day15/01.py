from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

data = file.read().splitlines()

beaconMap = {}

originX = 0
originY = 0
height = 0
width = 0

for line in data:
    s, b = line.split(':')
    sensor = (int(s[s.index('x'):].split(',')[0].split('=')[1]),int(s[s.index('y'):].split(',')[0].split('=')[1]))
    beacon = (int(b[b.index('x'):].split(',')[0].split('=')[1]),int(b[b.index('y'):].split(',')[0].split('=')[1]))

    # Set the bounds of the array
    originX = min(sensor[0], beacon[0], originX)
    originY = min(sensor[1], beacon[1], originY)

    # Set the bounds of the array
    width = max(sensor[0], beacon[0], width)
    height = max(sensor[1], beacon[1], height)

    beaconMap[sensor] = beacon


def drawMap():
    fullMap = {}
    for y in range(originY, height):
        for x in range(originX, width):
            if (x,y) in beaconMap:
                fullMap[(x, y)] = 'S'
                fullMap[(beaconMap[(x,y)][0], beaconMap[(x,y)][1])] = 'B'

    for sensor in beaconMap:
        sx, sy = sensor
        bx, by = beaconMap[sensor]

        distance = abs(sx-bx) + abs(sy-by)

        for y in range(originY, height):
            for x in range(originX, width):
                if abs(x-bx) + abs(y-by) < distance:
                    if (x, y) not in fullMap:
                        fullMap[(x,y)] = '#'

    for y in range(originY, height):
        for x in range(originX, width):
            if (x, y) in fullMap:
                print(fullMap[(x, y)], end='')
            else: 
                print('.', end='')
        print()

drawMap()


def solve():
    return 0


def test():
    assert solve() == 0
