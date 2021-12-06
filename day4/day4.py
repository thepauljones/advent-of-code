from array import array

with open('data.dat') as file:
    data = [line.strip() for line in file]

sequence = data[0].split(',')
cards = []
results = []
current_card = []
current_result = []

for i in range(1, len(data)):
    if (data[i] == ''):
        if (len(current_card) > 0):
            cards.append(current_card)
            results.append(current_result)
        current_card = []
        current_result = []
    else:
        current_card.append(data[i].split())
        current_result.append(data[i].split())


cards.append(current_card)
results.append(current_result)

for seq_i in range(0, len(sequence)):
    for card_index in range(0, len(cards)):
        bingo_card = cards[card_index]
        for i in range(0, len(bingo_card)):
            for j in range(0, len(bingo_card[i])):
                if (bingo_card[i][j] == sequence[seq_i]):
                    results[card_index][i][j] = 'X'
                    if (''.join(results[card_index][i]) == 'XXXXX'):
                        print('BINGO!', card_index, i, sequence[seq_i])
                        count = 0
                        for k in range(0, len(results[card_index])):
                            for l in range(0, len(results[card_index][k])):
                                if (results[card_index][k][l] != 'X'):
                                    count += int(results[card_index][k][l])

                        print(count * int(sequence[seq_i]))
                        exit()


