import math
with open('data.dat') as file:
    raw_data = file.read().split(',')

pos = list(map(int, map(str.strip, raw_data)))

all_diffs = []

def calculate_cost(pos):
    cost = 0
    steps = 0
    while(steps <= pos):
        cost += steps
        steps += 1

    return cost

for i in range(0, len(pos)):
    diffs = [calculate_cost(abs(x - i)) for x in pos]
    all_diffs.append((sum(diffs), i))

all_diffs.sort(key=lambda x: x[0])
print(all_diffs[0])
