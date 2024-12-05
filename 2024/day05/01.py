from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.readlines()

rules = []
updates = []
mode = 'rules'
for line in data:
    if line == '\n':
        mode = 'updates'
        continue

    if mode == 'rules':
        x, y = line.split('|')
        rules.append((int(x.strip()), int(y.strip())))

    if mode == 'updates':
        updates.append(list(map(int, line.split(","))))

valid = []

def get_rules_for_page(p):
    result = []
    for rule in rules:
        if rule[0] == p:
            result.append(rule)

    return result

valid_updates = []
for update in updates:
    valid = True
    for page in update:
        for rule in get_rules_for_page(page):
            if rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = False


    if valid:
        valid_updates.append(update)


print(valid_updates)
answer = 0
for v in valid_updates:
    answer += v[int(len(v)/2)]

print(answer)
