from pathlib import Path
import functools

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

data = [x.split(" ") for x in file.read().splitlines()]

hands = []

for h in data:
    hands.append((h[0], int(h[1])))


def score_hand(hand):
    highestCount = 0
    leadingCard = ""
    score = 1

    for card in hand:
        if highestCount < hand.count(card):
            highestCount = hand.count(card)
            leadingCard = card
        highestCount = max(highestCount, hand.count(card))

    if highestCount == 5:
        score = 7

    if highestCount == 4:
        score = 6

    if highestCount == 3:
        rest = []
        for c in hand:
            if c != leadingCard:
                rest.append(c)

        if rest[0] == rest[1]:
            score = 5
        else:
            score = 4

    if highestCount == 2:
        pairs = []
        for c in hand:
            if hand.count(c) > 1:
                pairs.append(c)

        if len(set(pairs)) > 1:
            score = 3
        else:
            score = 2

    return score


def compare_hands(a, b):
    r = score_hand(a[0]) - score_hand(b[0])
    if r < 0:
        return -1

    if r > 0:
        return 1

    # compare individual cards
    for i in range(len(a)):
        r = cards.index(a[0][i]) - cards.index(b[0][i])
        if r < 0:
            return -1

        if r > 0:
            return 1

    return r


sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
sorted_hands.reverse()

ans = 0

print(sorted_hands)

while len(sorted_hands):
    val = sorted_hands.pop(0)[1] * (len(sorted_hands) + 1)
    ans += val


print(ans)

# 252640338 this is the answer! for sure just waiting for the timer to let me put it in in 9 minutes but committing it now for the power play
