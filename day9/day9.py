with open('data.dat') as file:
    data = [line.strip() for line in file]

def get_adjacent(j, i, data):
    adjs = []
    if (j < len(data) - 1):
        adjs.append(data[j+1][i])

    if (j >= 1):
        adjs.append(data[j-1][i])

    if (i < len(data[j]) - 1):
        adjs.append(data[j][i+1])

    if (i >= 1):
        adjs.append(data[j][i-1])
    
    return adjs

print(get_adjacent(0, 1, data))

low_points = []
for j in range(0, len(data)):
    for i in range(0, len(data[0])):
        if data[j][i] < min(get_adjacent(j, i, data)):
            low_points.append(data[j][i])

print(sum(map(int, low_points))+len(low_points))
