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


def get_rules_for_page(p):
    result = []
    for rule in rules:
        if rule[0] == p:
            result.append(rule)

    return result

invalid_updates = []
for update in updates:
    valid = False
    for page in update:
        for rule in get_rules_for_page(page):
            if rule[1] in update:
                if update.index(rule[0]) > update.index(rule[1]):
                    valid = True


    if valid:
        invalid_updates.append(update)

def get_valid(u):
    valid_updates = []
    for update in u:
        valid = True
        for page in update:
            for rule in get_rules_for_page(page):
                if rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        valid = False


        if valid:
            valid_updates.append(update)

    return valid_updates

def rewrite(invalid_updates):
    for update in invalid_updates:
        for page in update:
            for rule in get_rules_for_page(page):
                if rule[1] in update:
                    if update.index(rule[0]) > update.index(rule[1]):
                        a, b = update.index(rule[0]), update.index(rule[1])
                        update[a], update[b] = update[b], update[a]


    print(len(invalid_updates), len(get_valid(invalid_updates)))
    if len(invalid_updates) != len(get_valid(invalid_updates)):
        rewrite(invalid_updates)


rewrite(invalid_updates)

answer = 0
for v in invalid_updates:
    answer += v[int(len(v)/2)]

print(answer)
