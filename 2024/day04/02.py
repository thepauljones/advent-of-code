from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.readlines()

grid = []
for line in data:
    grid.append(list(line.strip()))

right = [0, 1]
down = [1, 0]
left = [-1, 0]
up = [0, -1]

down_right = [1, 1]
up_left = [-1, -1]
up_right = [-1, 1]
down_left = [1, -1]

dirs = [(0, 0, down_right), (0, 2, down_left), (2, 0, up_right), (2, 2, up_left)]

def match_string_in_vector_from_position(pos, string, vector, pgrid):
    target = list(string)

    print("Start", pos)
    for p in pgrid:
        print(p)

    check_pos = pos
    found = True
    for c in target:
        if check_pos[0] < 0 or check_pos[0] > len(pgrid) - 1:
            found = False
            break
        if check_pos[1] < 0 or check_pos[1] > len(pgrid[0]) - 1:
            found = False
            break

        if pgrid[check_pos[0]][check_pos[1]] == c:
            check_pos[0] += vector[0]
            check_pos[1] += vector[1]
        else:
            found = False
            break

    return found

def find_string(string, passed_grid):
    found = []

    for j in range(0, len(passed_grid) - 2):
        for i in range(0, len(passed_grid[0]) - 2):
            count = 0
            check_grid = []
            for y in range(3):
                check_grid.append([])
                for z in range(3):
                    check_grid[y].append(passed_grid[j + y][i + z])

            for i in range(len(dirs)):
                a, b, vec = dirs[i]
                if match_string_in_vector_from_position([a, b], string, vec, check_grid):
                    count += 1

                if count > 1:
                    found.append(True)
                    break

    return len(found)


found = find_string('MAS', grid)

print(found)
