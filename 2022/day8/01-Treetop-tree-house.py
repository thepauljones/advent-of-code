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

            
            # Completely toxic and subtle fuckup in the first version of this line
            # The co-ords 11, 1 and 1, 11 for example, result in the same key, so
            # prefix it with the position id to make them all unique: this cost me too much hassle
            # key = ''.join([str(i), str(j)])

            key = ''.join(['i' + str(i), 'j' + str(j)])
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

    for line in visibility:
        print(''.join(line))

    print(result)

    return result

solve(test_data)
solve(data)


def test():
    assert solve(test_data) == 21
