from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = str.strip(file.read())

stones = data.split(" ")

def blink(p):
    nstones = []
    for s in p:
        if s == '0':
            nstones.append('1')
            continue
        elif len(str(s)) % 2 == 0:
            nstones.append(str(int(s[:int(len(s) / 2)])))
            nstones.append(str(int(s[int(len(s) / 2):])))
        else:
            nstones.append(str(int(s) * 2024))

    return nstones


count = 0
y = stones
while count < 25:
    y = blink(y)
    count += 1

print(len(y))
