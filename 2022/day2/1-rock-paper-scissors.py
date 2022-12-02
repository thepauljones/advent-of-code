from pathlib import Path

script_location = Path(__file__).absolute().parent
file_location = script_location / 'data.dat'
file = file_location.open()


def split(string):
    return string.strip().split(' ')

data = list(map(split, file.readlines()))


options = ['A', 'B', 'C']
coded_moves = ['X', 'Y', 'Z']
shapes = ['Rock', 'Paper', 'Scissors']

def evaluate(opponent, you):
    if opponent == you:
        return 3

    if opponent == 'Rock':
        if you == 'Paper':
            return 6

    if opponent == 'Paper':
        if you == 'Scissors':
            return 6

    if opponent == 'Scissors':
        if you == 'Rock':
            return 6
 
    return 0

def calculate_score(game):
    opp = options.index(game[0])
    you = coded_moves.index(game[1])

    score = evaluate(shapes[opp], shapes[you])

    return score + coded_moves.index(game[1]) + 1

scores = []
for game in data:
    scores.append(calculate_score(game))

print(sum(scores))
