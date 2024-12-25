from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().split("\n\n")

keys = []
locks = []

for i in data:
    item = i.strip().split("\n")
    if set(item[0]) == {"#"}:
        locks.append(item)
    else:
        keys.append(item)


def profile(item):
    res = []
    for i in range(len(item[0])):
        count = 0
        for j in range(1, len(item)):
            if item[j][i] == "#":
                count += 1

        res.append(count)

    return res


def fits(plock, pkey):
    res = True

    for i in range(len(plock)):
        if plock[i] + pkey[i] > 6:
            res = False

    return res


plocks = []
for l in locks:
    plocks.append(profile(l))

pkeys = []
for k in keys:
    pkeys.append(profile(k))

ans = 0
for p in plocks:
    for k in pkeys:
        if fits(p, k):
            ans += 1

print(ans)
