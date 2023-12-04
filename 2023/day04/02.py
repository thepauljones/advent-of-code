from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

input = file.read().splitlines()

inputMap = {}

for line in input:
    cardPoints = 0
    gamePart, numberSets = line.split(":")
    _, gameId = gamePart.split()

    inputMap[int(gameId)] = line


def solve(data):
    for line in data:
        cardPoints = []
        gamePart, numberSets = line.split(":")
        _, gameId = gamePart.split()
        winning, scratchcard = [x.split() for x in numberSets.split("|")]
        winning = list(map(int, winning))
        scratchcard = list(map(int, scratchcard))

        count = 0
        for x in winning:
            if x in scratchcard:
                count = count + 1
                cardPoints.append(int(int(gameId) + count))

        for y in cardPoints:
            data.append(inputMap[y])
            # print("Game ", gameId, " wins ", inputMap[y])

    return len(data)


answer = solve(input[:])

print(answer)
