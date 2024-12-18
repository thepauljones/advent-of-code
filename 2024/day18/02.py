from pathlib import Path
import time
from a_star import find_path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

# Reverse the order of the integers in the tuple
byte_rain = [tuple(map(int, line.strip().split(",")[::-1])) for line in data]


SIZE = 71

grid = [["." for _ in range(SIZE)] for _ in range(SIZE)]


def dropBytes(bytes):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if (j, i) in byte_rain[:bytes]:
                grid[j][i] = "#"


def printGridWithPath(path):
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if (j, i) in path:
                print("0", end="")
            else:
                print(grid[j][i], end="")
        print()


start = 1024
dropBytes(start)
print(len(byte_rain))

# ~ 360 seconds to solve :D hahaha fuck you I don't care
s = time.time()
for i in range(start, len(byte_rain) - 1):
    dropBytes(i)
    path = find_path((0, 0), (SIZE - 1, SIZE - 1), grid)

    if not path:
        print("Path not found after", i, "bytes in", time.time() - s, "seconds")
        print("Byte location that blocked path", byte_rain[i - 1][::-1])
        exit()
