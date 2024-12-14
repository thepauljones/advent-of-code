from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()
HEIGHT = 7
WIDTH = 11

robots = {}
for i, line in enumerate(data):
    x, y = line.split(" ")
    p = x.split("p=")[1]
    pos = list(map(int, p.split(",")))

    v = y.split("v=")[1]
    vel = list(map(int, v.split(",")))

    robots[(i, (vel[1], vel[0]))] = (pos[1], pos[0])

print(robots)


def shake():
    for bot in robots:
        i, vel = bot
        pos = robots[bot]

        robots[bot] = move(pos, vel)


def move(pos, vector):
    j = pos[0] + vector[0]
    i = pos[1] + vector[1]

    if pos[0] + vector[0] >= HEIGHT:
        j = pos[0] + vector[0] - HEIGHT
    if pos[1] + vector[1] >= WIDTH:
        i = pos[1] + vector[1] - WIDTH

    if pos[0] + vector[0] < 0:
        j = HEIGHT - abs(pos[0] + vector[0])
    if pos[1] + vector[1] < 0:
        i = WIDTH - abs(pos[1] + vector[1])

    return (j, i)


def printRoom():
    for j in range(HEIGHT):
        for i in range(WIDTH):
            if j == (HEIGHT - 1) / 2:
                print(" ", end="")
                continue
            if i == (WIDTH - 1) / 2:
                print(" ", end="")
                continue
            elif (j, i) in robots.values():
                print(list(robots.values()).count((j, i)), end="")
            else:
                print(".", end="")

        print()


for i in range(100):
    printRoom()
    shake()

printRoom()
