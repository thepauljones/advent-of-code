num_rolls = 3

scores = [0, 0]

d = list(range(1, 101))
print(d[0], d[99])

def play_game(pos, round_num = 1):
    global score_one, score_two

    
    rolls = 0
    while rolls < num_rolls:
       nums  = roll_dice(round_num, True)
       rolls += 1

    player = int(round_num % 2 != 0)

    moves = sum(nums)

    pos[player] += moves

    if (pos[player] != 10):
        pos[player] = pos[player] % 10

    if(pos[player] == 0):
        pos[player] = 10

    score = pos[player]
    scores[player] += score

    if (scores[player] > 999):
        print(round_num + 3)
        final_num_rolls = round_num + 3
        lowest_score = min(scores)
        print(final_num_rolls, lowest_score)
        print(final_num_rolls * lowest_score)
        exit()
 
    print('Player', player + 1, 'rolls', '+'.join(map(str, nums)), 'and moves to space', score, 'for a total score of', scores[player]);

    play_game(pos, round_num + 3)

def roll_dice(round, deterministic = False):
    res = []
    if (deterministic):
        for x in range(3):
            i = round + x
            if (i > len(d) - 1):
                i = i % len(d)

            res.append(d[i])

        return res

play_game([6, 9], 0)
