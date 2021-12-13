import numpy as np

with open('data.dat') as file:
    raw_data = [line.strip() for line in file]

dot_positions = []

max_x = 0
max_y = 0

mode = 'numbers'
folds = []

for line in raw_data:
    if line == '':
        mode = 'folds'
        continue

    if mode == 'numbers':
        x, y = map(int, line.split(','))
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        dot_positions.append((y, x))
    else:
        folds.append(line)

# Data is not read in and set up
# initialize arrays

grid = []

for j in range(0, max_y + 1):
    grid.append([])
    
for line in grid:
    for i in range(0, max_x + 2):
        line.append('.')

# Data setup
def print_grid(grid):
    for line in grid:
        print(''.join(line))

    print('-----------')

for pos in dot_positions:
    j, i = pos
    grid[j][i] = '#'

# Alright, scaffolding is done, lets go
def fold_up(grid, fold_pos):
    result = []

    for j in range(0, fold_pos):
        result.append([])
        for i in range(0, len(grid[0])):
            result[j].append('#' if grid[j][i] == '#' or grid[len(grid) - j - 1][i] == '#' else '.')

    return result[:]

def fold_across(grid, fold_pos):
    result = []

    for j in range(0, len(grid)):
        result.append([])
        count_i = 1
        for i in range(fold_pos, fold_pos * 2):
            if (i + 1 >= len(grid[0])):
                break
            result[j].append('#' if grid[j][i + 1] == '#' or grid[j][fold_pos - count_i] == '#' else '.')
            count_i = count_i + 1

    return result[:]

def count_hashes(grid):
    count = 0
    for j in range(0, len(grid)):
        for i in range(0, len(grid[0])):
            if grid[j][i] == '#':
                count = count + 1

    return count

def fold(grid, fold):
    if fold.find('x') > -1:
        return fold_across(grid, int(fold.split('=')[1]))[:]
    if fold.find('y') > -1:
        return fold_up(grid, int(fold.split('=')[1]))[:]

def part_one(grid):
    result = grid
    for current_fold in folds:
        result = fold(result[:], current_fold)

    print_grid(result)

    print(count_hashes(result))

part_one(grid)
