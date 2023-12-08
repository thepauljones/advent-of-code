from pathlib import Path
import functools

script_location = Path(__file__).absolute().parent
file_location = script_location / "data.dat"
file = file_location.open()

cards = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

data = [x.split(" ") for x in file.read().splitlines()]

hands = []

for h in data:
    hands.append((h[0], int(h[1])))


def getWild(n):
    runs = 0
    result = []
    output = ""
    while runs < len(cards):
        for c in range(1, len(cards)):
            output += cards[c]
            for i in range(1, n):
                output += cards[i + runs]
                print(len(result))
            result.append(output)
            print(output)
            output = ""
        runs += 1

    return output


print(getWild(2))
exit()


def score_hand(hand):
    highestCount = 0
    leadingCard = ""
    score = 1

    for card in hand:
        if highestCount < hand.count(card):
            highestCount = hand.count(card)
            leadingCard = card
        highestCount = max(highestCount, hand.count(card))

    # A poker
    if highestCount == 5:
        score = 7

    # four of a kind
    if highestCount == 4:
        score = 6

    if highestCount == 3:
        rest = []
        for c in hand:
            if c != leadingCard:
                rest.append(c)

        # full house
        if rest[0] == rest[1]:
            score = 5
        # three of a kind
        else:
            score = 4

    if highestCount == 2:
        pairs = []
        for c in hand:
            if hand.count(c) > 1:
                pairs.append(c)

        # two pair
        if len(set(pairs)) > 1:
            score = 3
        # one pair
        else:
            score = 2

    return score


def compare_hands(a, b):
    handA = a[0]
    handB = b[0]

    scoreA = score_hand(handA)
    scoreB = score_hand(handB)

    if handA.count("J") == 5:
        scoreA = 7
    if handB.count("J") == 5:
        scoreB = 7

    optionsA = getWild(handA.count("J"))
    while len(optionsA):
        scoreA = max(
            scoreA,
            score_hand(
                "".join(optionsA.pop(0)) + "".join([x for x in handA if x != "J"])
            ),
        )

    optionsB = getWild(handB.count("J"))
    while len(optionsB):
        scoreB = max(
            scoreB,
            score_hand(
                "".join(optionsB.pop(0)) + "".join([x for x in handB if x != "J"])
            ),
        )

    r = scoreA - scoreB

    if r < 0:
        return -1

    if r > 0:
        return 1

    # compare individual cards
    for i in range(len(handA)):
        r = cards.index(handA[i]) - cards.index(handB[i])
        if r < 0:
            return -1

        if r > 0:
            return 1

    return r


sorted_hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
sorted_hands.reverse()

ans = 0
while len(sorted_hands):
    val = sorted_hands.pop(0)[1] * (len(sorted_hands) + 1)
    ans += val

assert ans < 253615430 and ans > 252946807

print(ans)

# 253615430 too high
# 252946807 too low
