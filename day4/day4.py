from array import array

with open('test-data.dat') as file:
    data = [line.strip() for line in file]

# Get all the data in some kind of structure
# keep a separate list for result status
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


# Don't forget the last one :)
cards.append(current_card)
results.append(current_result)


def mark_number(number, card, result):
    for i in range(0, len(card)):
        for j in range(0, len(card[i])):
            if (card[i][j] == number):
                result[i][j] = 'X'

def is_bingo(card):
    for i in range(0, len(list(card[0]))):
        col = []
        for line in card:
            col.append(line[i])
            if (''.join(line) == 'XXXXX' or ''.join(col) == 'XXXXX'):
                return True
            
    return False

def sum_uncrossed(card):
    count = 0
    for line in card:
        for i in list(line):
            if (i != 'X'):
                count += int(i)

    print(count)
    return count


def part_one(data):
    for seq_i in range(0, len(sequence)):
        for card_index in range(0, len(cards)):
            mark_number(sequence[seq_i], cards[card_index], results[card_index])

            is_solved = is_bingo(results[card_index])

            if (is_solved):
                return int(sequence[seq_i]) * sum_uncrossed(results[card_index])

print(part_one(data))
