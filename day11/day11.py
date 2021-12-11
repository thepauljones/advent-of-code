with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

def split_to_int(line):
    nums = [char for char in line]
    return map(int, nums)

data = map(split_to_int, raw_data)

# Data stored in 2d array of integers

def increment_adjacents(j, i, data):
    if (j < len(data) - 1):
        data[j+1][i] += 1 # South
        if i >= 1:
            data[j+1][i-1] += 1 # South-West
        if i < len(data[0]) - 1:
            data[j+1][i+1] += 1 # South-East

    if (j >= 1):
        data[j - 1][i] += 1  # North
        if i >= 1:
            data[j - 1][i - 1] += 1 # North-West
        if i < len(data[0]) - 1:
            data[j-1][i+1] += 1 # North-East

    if (i < len(data[j]) - 1):# East
        data[j][i + 1] += 1

    if (i >= 1):
        data[j][i - 1] += 1 # West

def get_10s(data):
    tens = []
    for j in range(0, len(data)):
        for i in range(0, len(data[0])):
            if data[j][i] > 9:
                tens.append((j, i))

    return tens

def print_grid(grid):
    for row in grid:
        print(''.join(map(str, row)))
    print('----------')

def bang_grid(grid):
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            grid[j][i] += 1

    flash = get_10s(data)
    tens = flash
    while(len(tens) > 0):
        for point in tens:
            increment_adjacents(point[0], point[1], data)

        tens = set(get_10s(data)).difference(flash)
        flash = set(flash).union(set(tens))

    for point in flash:
        grid[point[0]][point[1]] = 0

    return len(flash)


def part_one(grid):
    count_flashes = 0
    for i in range(0, 100):
        count_flashes += bang_grid(grid)
        
        print_grid(data)

    print(count_flashes)

part_one(data)

def get_adjacent(j, i, data):
    adjs = []
    if (j < len(data) - 1):
        adjs.append(data[j+1][i]) # South
        if i >= 1:
            adjs.append(data[j+1][i-1]) # South-West
        if i < len(data[0]) - 1:
            adjs.append(data[j+1][i+1]) # South-East

    if (j >= 1):
        adjs.append(data[j - 1][i])  # North
        if i >= 1:
            adjs.append(data[j - 1][i - 1])  # North-West
        if i < len(data[0]) - 1:
            print(len(data[0]) - 1)
            adjs.append(data[j-1][i+1]) # North-East

    if (i < len(data[j]) - 1):# East
        adjs.append(data[j][i + 1])

    if (i >= 1):
        adjs.append(data[j][i - 1]) # West

    return adjs

# print('ADJS(0, 0', get_adjacent(0, 0, data))
# print('ADJS(9, 9', get_adjacent(9, 9, data))
# print('ADJS(0, 9', get_adjacent(0, 9, data))
# print('ADJS(9, 0', get_adjacent(9, 0, data))
# print('ADJS', get_adjacent(1, 1, data))
