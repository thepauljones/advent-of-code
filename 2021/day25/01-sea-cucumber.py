from pathlib import Path
import math

script_location = Path(__file__).absolute().parent
file_location = script_location / "test-data.dat"
file = file_location.open()

sea = [list(x) for x in file.readlines()]


def move(grid, direction="east"):
    cucumber = ">" if direction == "east" else "v"
    moves = {}
    # if direction == 'south':
    #    printGrid(grid)
    #    print('South after east')
    #    exit()
    for i in range(0, len(grid)):
        for j in range(0, len(grid[0])):
            if grid[i][j] == cucumber:
                if direction == "east":
                    dest = j + 1
                    if dest >= len(grid[0]) - 1:
                        dest = 0
                    if grid[i][dest] == ".":
                        moves[(i, j)] = (i, dest)

                if direction == "south":
                    dest = i + 1
                    if dest >= len(grid) - 1:
                        dest = 0
                    if grid[dest][j] == ".":
                        moves[(i, j)] = (dest, j)

    return moves, grid


def performMoves(moves, grid, thing):
    for move in moves:
        grid[move[0]][move[1]] = "."
        grid[moves[move][0]][moves[move][1]] = thing

    return grid


def printGrid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end="")
        print()

    print("-------")


def solve(grid):
    moves = {
        "dummy": "nothing",
    }
    moved = 1
    count = 0
    printGrid(grid)
    while moved > 0:
        eastMoves, grid = move(grid, "east")
        grid = performMoves(eastMoves, grid, ">")
        southMoves, grid = move(grid, "south")
        grid = performMoves(southMoves, grid, "v")

        count += 1
        if count > 0:
            print(moved)
            printGrid(grid)
            exit()


solve(sea)


print(sea)
