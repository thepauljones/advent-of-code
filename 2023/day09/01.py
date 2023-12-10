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
        new_reading.append(abs(reading[i] - reading[i + 1]))

    return new_reading


assert get_next([0, 1, 1, 0]) == [1, 0, 1]
assert get_next([0, 3, 6, 9, 12, 15]) == [3, 3, 3, 3, 3]
assert get_next([0, -3, 6, 9, 12, 15]) == [3, 9, 3, 3, 3]


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
        one = full[i - 1][-1]
        two = full[i][-1]
        print("Adding ", one, " + ", two)
        full[i].append(one + two)

    print(full)
    return full[-1][-1]


ans = 0
for r in readings:
    res = solve(r)
    print("ans", ans, " + res", res, " = ")
    ans += solve(r)


print(ans)
# 1886645272 too high
# 1886876616 too high
# 1886413928 too high
# 1886413247 also wrong
