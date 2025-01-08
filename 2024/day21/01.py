from pathlib import Path
from a_star import find_path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

tel = [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"], ["#", "0", "A"]]

dir = [["#", "^", "A"], ["<", "v", ">"]]

tel_paths = {}
dir_paths = {}


def get_all_paths(grid, pos):
    res = {}
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == "#" or pos == (j, i) or grid[pos[0]][pos[1]] == "#":
                continue
            else:
                res[grid[j][i]] = find_path((j, i), pos, grid)

    return res


for j in range(len(tel)):
    for i in range(len(tel[0])):
        if tel[j][i] == "#":
            continue
        res = get_all_paths(tel, (j, i))
        tel_paths[tel[j][i]] = res

for j in range(len(dir)):
    for i in range(len(dir[0])):
        if dir[j][i] == "#":
            continue
        res = get_all_paths(dir, (j, i))
        dir_paths[dir[j][i]] = res


def get_buttons(f, t):
    return tel_paths[f][t]


def get_buttons_for_code(code):
    test = "A" + code  # start above A
    res = ""
    for i in range(len(test) - 1):
        res += get_buttons(test[i], test[i + 1])

    return res


print(get_buttons_for_code("029A"))
