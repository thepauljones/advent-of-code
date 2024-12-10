from pathlib import Path
from functools import cache
from itertools import chain
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().strip()

things = []
for i, ins in enumerate(data):
    items = []
    if ins == "0":
        continue
    if i % 2 == 0:
        while len(items) < int(ins):
            items.append(str(int(i / 2)))
        things.append(items)
    else:
        while len(items) < int(ins):
            items.append(".")
        things.append(items)

revc = list(things[:])

def is_space(piece):
    res = list(set(piece)) == ["."]
    return res

rev = []
for i, r in enumerate(revc):
    if list(set(r)) != ["."]:
        rev.append((i, r))

rev = list(reversed(rev))

def get_first_index_of_space_of_length(l, smap):
    for i, thing in enumerate(smap):
        if is_space(thing) and len(thing) >= l:
            return i

    return -1


def bang(smap):
    inserts = {}

    while len(rev) > 0:
        # get the mover
        moverpos, mover = rev.pop(0)
        # Where it should go
        mover_dest = get_first_index_of_space_of_length(len(mover), smap)
        # if it can't go anywhere forget it 
        if mover_dest == -1:
            continue
        if mover_dest >= moverpos:
            continue
        #check the leftover
        extra = len(smap[mover_dest]) - len(mover)

        offset = 0
        for o in inserts:
            if o <= moverpos:
                offset += inserts[o]
        smap[moverpos + offset] = list("."*len(mover))

        #move 
        smap[mover_dest] = mover
        # add in the leftovers if required
        if extra > 0:
            dest = mover_dest + 1
            if dest in inserts:
                inserts[dest] += 1
            else:
                inserts[dest] = 1
            smap.insert(dest, list(extra*"."))

        print("".join(list(chain.from_iterable(smap))))

    return smap

print("".join(list(chain.from_iterable(things))))
res = bang(things)

output = list(chain.from_iterable(res))

ans = 0
for i, o in enumerate(output):
    if o != ".":
        ans += i * int(o)

print(ans)

# 6223425894430 too low
