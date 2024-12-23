from pathlib import Path
import time
from collections import defaultdict

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = [tuple(x.strip().split("-")) for x in file.readlines()]

G = defaultdict(set)

for a, b in data:
    G[a].add(b)
    G[b].add(a)

thruples = set()
# This is so awfully named I can't really remember what I'm doing BUT
# G is all the stuff, so go through each pair and add each other to the set of
# that pairs connetion in the hashmap G
#
# THEN for each item in G if the A AND the B are in _that_ things connections you've got a match
# so I add the sorted -> tuple -> of an array -> of a, b, c to a set (if I do not sort they are considered distinct)
#
# and then loop through each relationship of 3 things and see if one starts with "t"
for p in G:
    for a, b in data:
        if a in G[p] and b in G[p]:
            for q in G[p]:
                if q in G[a] and q in G[b]:
                    thruples.add(tuple(sorted([a, p, b])))


print(thruples)

start = time.time()
ans = 0
for x, y, z in thruples:
    if x[0] == "t" or y[0] == "t" or z[0] == "t":
        ans += 1
        continue  # amusingly this continue makes it ten times faster apparently

print(ans, " elapsed: ", time.time() - start)
