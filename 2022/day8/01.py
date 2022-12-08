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
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            key = ''.join([str(i), str(j)])
            visible[key] = False

            if i == 0 or i == len(grid) - 1 or j == 0 or j == len(grid[0]) - 1:
                visible[key] = True


    result = list(visible.values()).count(True)
    print(result)
    return result

solve(test_data)


def test():
    assert solve(test_data) == 21
