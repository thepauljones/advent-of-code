with open('data.dat') as file:
    raw_data = file.read().split(',')

pos = list(map(int, map(str.strip, raw_data)))

all_diffs = []

for i in range(0, len(pos)):
    diffs = [abs(x - i) for x in pos]
    all_diffs.append((sum(diffs), i))

all_diffs.sort(key=lambda x: x[0])

print(all_diffs[0][0])
