from pathlib import Path
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


dropBytes(1024)

path = find_path((0, 0), (SIZE - 1, SIZE - 1), grid)

printGridWithPath(path)
print(len(path) - 1)
