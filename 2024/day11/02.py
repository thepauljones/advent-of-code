from pathlib import Path
from functools import lru_cache
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = str.strip(file.read())

stones = data.split(" ")

@lru_cache(maxsize=None)
def process(s):
    res = []

    if s == '0':
        res.append('1')
    elif len(str(s)) % 2 == 0:
        res.append(str(int(s[:int(len(s) / 2)])))
        res.append(str(int(s[int(len(s) / 2):])))
    else:
        res.append(str(int(s) * 2024))

    return res


def blink(p):
    nstones = []
    for s in p:
        res = process(s)
        for r in res:
            nstones.append(r)

    return nstones


count = 0
y = stones
while count < 75:
    y = blink(y)
    print("Blink: ", count + 1, "length: ", len(y))
    count += 1

print(len(y))
