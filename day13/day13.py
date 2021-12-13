import numpy as np

with open('test-data.dat') as file:
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
    for i in range(0, max_x + 1):
        line.append('.')

print(len(grid))
print(len(grid[0]))

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
    bottom_sheet = []
    top_sheet = []

    for j in range(0, len(grid)):
        if(j == fold_pos):
            continue

        if (j < fold_pos):
            bottom_sheet.append(grid[j])
        else:
            top_sheet.append(grid[j])

    return merge_grids(bottom_sheet[:], np.flipud(top_sheet[:]), 'up')


def fold_across(grid, fold_pos):
    bottom_sheet = []
    top_sheet = []

    for j in range(0, len(grid)):
        bottom_sheet.append(grid[j][:fold_pos])
        top_sheet.append(grid[j][fold_pos + 1:])

    print_grid(bottom_sheet)
    print_grid(top_sheet)

    return merge_grids(bottom_sheet[:], np.fliplr(top_sheet[:]), 'across')


def merge_grids(source, target, fold_type):
    # init array
    result = []

    if (len(source) != len(target)):
        print('Error: ',fold_type, 'merge_grids: source and target have different lengths')
        print(len(source), len(target), len(grid))
        exit()

    if (len(source[0]) != len(target[0])):
        print('Error: merge_grids: X source and target have different lengths')
        print(len(source[0]), len(target[0]), len(grid[0]))
        exit()

    for j in range(0, len(source)):
        result.append([])
        
    for j in range(0, len(source)):
        for i in range(0, len(source[0])):
            if (source[j][i] == '#' or target[j][i] == '#'):
                result[j].append('#')
            else:
                result[j].append('.')

    print_grid(result)

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
    print_grid(grid)
    for current_fold in folds:
        result = fold(result[:], current_fold)

    print(count_hashes(result))

part_one(grid)
