from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

data = file.read().splitlines()

readings = []
for line in data:
    readings.append([int(x) for x in line.split()])


def get_next(reading):
    new_reading = []
    for i in range(len(reading) - 1):
        new_reading.append(reading[i + 1] - reading[i])

    return new_reading


assert get_next([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]


def solve(reading):
    res = get_next(reading)

    full = [res]
    while res != -1:
        res = get_next(res)
        if res == -1:
            break

        full.append(res)
        if len(list(set(res))) == 1 and list(set(res))[0] == 0:
            break

        if len(res) == 0:
            break

    full.reverse()
    full.append(reading)

    full[0].append(0)

    for i in range(1, len(full)):
        full[i].append(full[i - 1][-1] + full[i][-1])

    print(full)
    return full[-1][-1]


ans = 0
for r in readings:
    ans += solve(r)


print(ans)
# 1886645272 too high
# 1886876616 too high
# 1886413928 too high
# 1886413247 also wrong
