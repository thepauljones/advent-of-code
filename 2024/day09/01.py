from pathlib import Path
from functools import cache
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().strip()

disk = {}

for i, ins in enumerate(data):
    if i % 2 == 0:
        disk[i] = (str(int(i / 2)) * int(ins))
    else:
        disk[i] = ("." * int(ins))

def has_space(check):
    return "." in check

def is_empty(check):
    return check == ""

def has_content(check):
    if is_empty(check):
        return False
    result = list(set(list(check))) != ["."]
    return result

@cache
def move(content, empty):
    c = list(content)
    e = list(empty)

    for i in range(len(c) - 1, -1, -1):
        if c[i] != ".":
            cand = c.pop(i)

            e.insert(empty.index("."), cand)
            e.pop()
            c.append(".")
            break

    return "".join(c), "".join(e)

def defrag(disk):
    moved = False
    look_content = len(disk) - 1
    check_content = disk[look_content]
    look_empty = 0
    check_empty = disk[look_empty]

    while moved == False:
        if has_content(check_content):
            while moved == False:
                if not has_space(check_empty):
                    look_empty += 1
                    check_empty = disk[look_empty]
                else:
                    disk[look_content], disk[look_empty] = move(check_content, check_empty)
                    moved = True
        else:
            look_content -= 1
            check_content = disk[look_content]

        if look_empty > len(disk):
            return False


    return check_disk_state(disk)

def check_disk_state(disk):
    res = ""
    for line in disk.values():
        res += line
        print(line, end="")
    print()

    if list(set(list(res)[res.index("."):])) == ["."]:
        return True
    return False

check_disk_state(disk)

def get_final_state(disk):
    res = ""
    for line in disk.values():
        res += line

    return list(map(int, list(res[:res.index(".")])))

res = defrag(disk)
print(disk)
while not res:
    res = defrag(disk)

final_state = get_final_state(disk)

answer = 0
for i, num in enumerate(final_state):
    answer += i * num

print(final_state)
print(answer)

# 90095094087 too low
