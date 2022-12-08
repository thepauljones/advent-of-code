from pathlib import Path
import math

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()

data = file.read().splitlines()

script_location = Path(__file__).absolute().parent
file_location = script_location / 'test-data.dat'
file = file_location.open()

test_data = list(map(list, file.read().splitlines()))

def trees_in_view(treeHeight, view, debug=False):
    num = 0

    for tree in view:
        num+=1

        if tree >= treeHeight:
            break

    if debug:
        print(treeHeight, view, num)

    return num

def solve(grid):
    columns = []
    for i in range(0, len(grid)):
        col = []
        for j in range(0, len(grid[i])):
            col.append(int(grid[j][i]))
        columns.append(col)

    scenic_scores = []
    for i in range(0, len(grid)):
        for j in range(0, len(grid[i])):
            height = int(grid[i][j])

            # Completely toxic and subtle fuckup in the first version of this line
            # The co-ords 11, 1 and 1, 11 for example, result in the same key, so
            # prefix it with the position id to make them all unique: this cost me too much hassle
            # key = ''.join([str(i), str(j)])

            key = ''.join(['i' + str(i), ',j' + str(j)])

            toLeft = list(map(int, grid[i][0:j]))
            above = list(map(int, columns[j][0:i]))

            below = list(map(int, columns[j][i + 1:]))
            toRight = list(map(int, grid[i][j + 1:]))

            toLeft.reverse()
            above.reverse()

            views = [above, toLeft, below, toRight]

            scores = []
            for view in views:
                scores.append(trees_in_view(height, view, True if key == 'i3,j2' else False))

            scenic_score = scores[0]

            for k in range(1, len(scores)):
                scenic_score *= scores[k]

            print(key, scenic_score, scores)


            scenic_scores.append(scenic_score)

    scenic_scores.sort()
    scenic_scores.reverse()

    print(scenic_scores[0])

    return scenic_scores[0]

solve(test_data)
solve(data)


def test():
    assert solve(test_data) == 21
