from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()

times = [int(x.strip()) for x in data[0].split(":")[1].split()]
distances = [int(x.strip()) for x in data[1].split(":")[1].split()]


def getPossibleRaces(t, d):
    result = []
    for i in range(1, t):
        if i * (t - i) > d:
            result.append(i)

    return result


ans = []
for p in range(len(times)):
    ans.append(len(getPossibleRaces(times[p], distances[p])))

r = 1
for i in ans:
    r = r * i

print(r)
