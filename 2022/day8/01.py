from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

test_data = list(map(list, file.read().splitlines()))


def solve(grid):
    # Create a dictionary of positions all set to invisible
    visible = {}

    visibility = []

    columns = []
    for i in range(0, len(grid)):
        col = []
        for j in range(0, len(grid[i])):
            col.append(int(grid[j][i]))
        columns.append(col)

    for i in range(0, len(grid)):
        visibility.append([])
        for j in range(0, len(grid[i])):
            height = int(grid[i][j])

            key = ''.join([str(i), str(j)])
            visible[key] = False

            toLeft = list(map(int, grid[i][0:j]))
            toRight = list(map(int, grid[i][j + 1:]))

            above = list(map(int, columns[j][0:i]))
            below = list(map(int, columns[j][i + 1:]))

            # visible from the left
            if height > max(toLeft, default=-1):
                visible[key] = True

            # visible from the bottom
            if height > max(below, default=-1):
                visible[key] = True

            # visible from the right
            if height > max(toRight, default=-1):
                visible[key] = True

            # visible from the top
            if height > max(above, default=-1):
                visible[key] = True

            visibility[i].append('O' if visible[key] == True else 'X')

            print('-----------------')
            print('Key', key, height)
            print('Left', toLeft)
            print('Right', toRight)
            print('Above', above)
            print('Below', below)
            print('-----------------')


    result = list(visible.values()).count(True)
    print(result)

    for line in visibility:
        print(''.join(line))

    return result

solve(test_data)
#solve(data)


def test():
    assert solve(test_data) == 21
