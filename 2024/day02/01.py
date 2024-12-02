from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

safe_levels = []

def isSafe(level, up):
    result = True
    if up:
        for i in range(0, len(level) - 1):
            a = level[i]
            b = level[i + 1]

            if abs(a - b) > 3 or a == b:
                print('1', a, b)
                result = False

            if (a > b):
                print('2', a, b)
                result = False


    if not up:
        for i in range(0, len(level) - 1):
            a = level[i]
            b = level[i + 1]

            if abs(a - b) > 3 or a == b:
                print('3', a, b)
                result = False

            if (a < b):
                print('4', a, b)
                result = False

    return result



answer = 0

for line in data:
    level = list(map(int, line.split()))

    safe = isSafe(level, level[0] < level[1])
    print(level, safe)
    if safe:
        answer += 1 

print(answer)


