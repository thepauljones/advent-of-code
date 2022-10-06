with open('data.dat') as file:
    [pone, ptwo] = [line.strip() for line in file]
    

one = pone[len(pone)-1:len(pone)]
two = ptwo[len(ptwo)-1:len(ptwo)]

num_rolls = 3

score_one = 0
score_two = 0

def play_game(round_num = 0):
    global score_one, score_two
    
    rolls = 0
    while rolls < num_rolls:
       nums  = roll_dice(round_num, True)
       rolls += 1

    total = sum(nums)

    if (round_num % 2 == 0):
        score_one += total
    else:
        score_two += total


    if score_one > 999 or score_two > 999:
        print(min([score_one, score_two]), round_num)
        print(min([score_one, score_two]) * round_num)
        exit()

    play_game(round_num + 3)

def roll_dice(round, deterministic = False):
    if (deterministic):
        return [round * 3, round * 3 + 1, round * 3 + 2]

play_game()
