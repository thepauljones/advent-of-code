from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

safe_levels = []
def isSafe(level, up, isRetry = False):
    result = True
    problem = -1
    if up:
        for i in range(0, len(level) - 1):
            a = level[i]
            b = level[i + 1]

            if abs(a - b) > 3 or a == b:
                result = False
                problem = i + 1

            if (a > b):
                result = False
                problem = i + 1


    if not up:
        for i in range(0, len(level) - 1):
            a = level[i]
            b = level[i + 1]

            if abs(a - b) > 3 or a == b:
                result = False
                problem = i + 1

            if (a < b):
                result = False
                problem = i + 1

    if (problem > -1 and isRetry == False):
        levelA = level.copy()
        levelB = level.copy()
        popped = levelA.pop(problem)
        poppedB =  levelB.pop(problem - 1)
        result = isSafe(levelA, up, True) or isSafe(levelB, up, True)
        if(not result):
            print('POPPED: ', popped, result)

    return result



answer = 0
count = 0
for line in data:
    count += 1
    level = list(map(int, line.split()))

    asc = level[0] < level[-1]
    safe = isSafe(level, asc)
    if not safe and not asc:
        print(level, safe)

    if safe:
        answer += 1 



print(answer)


