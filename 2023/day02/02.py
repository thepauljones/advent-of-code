from pathlib import Path
import re

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()


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

        pieces = []
        for col in tot:
            pieces.append(max(tot[col]))

        power = pieces[0] * pieces[1] * pieces[2]
        print(power)
        answer += power

    print("answer", answer)


solve()
