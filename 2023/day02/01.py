from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()

max = {"blue": 14, "red": 12, "green": 13}


def solve():
    answer = 0
    for line in data:
        tot = {"blue": [], "red": [], "green": []}
        game, handfuls = line.split(":")
        gameId = int(game.split(" ")[1])

        cubes = handfuls.split(";")

        for colors in cubes:
            handfuls = [x.strip() for x in colors.split(", ")]
            for individual in handfuls:
                num, col = individual.split(" ")
                tot[col].append(int(num))

        print(tot)
        isValid = True
        for color in max:
            for count in tot[color]:
                print(count)
                if count > max[color]:
                    isValid = False

        if isValid:
            answer += gameId

    print("answer", answer)


solve()
