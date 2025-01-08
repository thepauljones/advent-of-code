from pathlib import Path
from functools import cache

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = [int(x.strip()) for x in file.readlines()]


def mix(val, num):
    return val ^ num


def prune(val):
    return val % 16777216


@cache
def bang(num):
    t = mix(num * 64, num)
    t = prune(t)

    t = mix(t // 32, t)
    t = prune(t)

    t = mix(t * 2048, t)
    res = prune(t)

    return res


res = 0
for i, n in enumerate(data):
    count = 0
    while count < 2000:
        n = bang(n)
        count += 1
    res += n

print(res)
