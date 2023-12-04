from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

data = file.read().splitlines()


def solve():
    answer = 0
    for line in data:
        cardPoints = 0
        gamePart, numberSets = line.split(":")
        _, gameId = gamePart.split()
        winning, scratchcard = [x.split() for x in numberSets.split("|")]

        for x in winning:
            if x in scratchcard:
                print(x, "is winning")
                if cardPoints == 0:
                    cardPoints = 1
                else:
                    cardPoints *= 2

        answer += cardPoints

    print(answer)


solve()
