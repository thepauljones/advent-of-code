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
    originX = min(sensor[1], beacon[1], originX)
    originY = min(sensor[0], beacon[0], originY)

    # Set the bounds of the array
    width = max(sensor[0], beacon[0], width) 
    height = max(sensor[1], beacon[1], height) 

    beaconMap[sensor] = beacon


def drawMap(target):
    global originX, originY, height, width
    fullMap = {}

    originX = originX - -originX
    originY = originY - -originY
    width *= 2
    height *= 2

    count = 0
    for sensor in beaconMap:
        sx, sy = sensor
        bx, by = beaconMap[sensor]

        distance = abs(bx - sx) + abs(by - sy)
        fullMap[(sx, sy)] = 'S'
        fullMap[(bx, by)] = 'B'

        for y in range(sy - distance, sy + distance):
            for x in range(sx - distance , sx + distance):
                if abs(x - sx) + abs(y - sy) <= distance:
                    if (x, y) not in fullMap:
                        fullMap[(x,y)] = '#'
                        if y == target:
                            count += 1

    print(count)

def solve():
    drawMap(10)
    return 0


solve()
