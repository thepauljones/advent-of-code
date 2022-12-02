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

def get_my_move(opponent, outcome):

    if outcome == 'X':
        if opponent == 'Rock':
            return 'Scissors'
        if opponent == 'Scissors':
            return 'Paper'
        if opponent == 'Paper':
            return 'Rock'

    if outcome == 'Y':
        return opponent

    if opponent == 'Rock':
        return 'Paper'
    if opponent == 'Scissors':
        return 'Rock'

    return 'Scissors'


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

    my_move = get_my_move(shapes[opp], game[1])

    score = evaluate(shapes[opp], my_move)

    print(shapes[opp], my_move, score, shapes.index(my_move) + 1)

    return score + (shapes.index(my_move) + 1)

scores = []
for game in data:
    scores.append(calculate_score(game))

print(sum(scores))
