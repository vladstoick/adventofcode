from pathlib import Path
import regex as re
from functools import cmp_to_key

p = Path(__file__).with_name("input.txt")
file = open(p)

order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
orderpart2 = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
indexOfJPart2 = orderpart2.index('J')

# Scores:
# Five of a kind: 0
# Four of a kind: 1
# Full house: 2
# Three of a kind: 3
# Two pair: 4
# One pair: 5
# High card: 6


def calculate_score(cardsOrig, part2=False):
    cards = sorted(cardsOrig)
    cardsCount = {}

    for c in cards:
        cardsCount[c] = cardsCount.get(c, 0) + 1

    cardsCount = sorted(cardsCount.items(), key=lambda x: x[1], reverse=True)

    keysSorted = [x[0] for x in cardsCount]
    if part2 and indexOfJPart2 in keysSorted and len(cardsCount) >= 2:
        index = keysSorted.index(indexOfJPart2)
        count = cardsCount[index][1]
        del cardsCount[index]
        cardsCount[0] = (cardsCount[0][0], cardsCount[0][1] + count)

    print(cardsCount)

    if (len(cardsCount) == 1):
        # Five of a kind
        return 0
    elif (len(cardsCount) == 2):
        if (cardsCount[0][1] == 4):
            # Four of a kind
            return 1
        else:
            return 2
    elif (len(cardsCount) == 3):
        if (cardsCount[0][1] == 3):
            # Three of a kind
            return 3
        else:
            # Two pair
            return 4
    elif (len(cardsCount) == 4):
        # One pair
        return 5
    else:
        # Find biggest card
        return 6


hands = []
handsPart2 = []

for line in file.readlines():
    [cards, points] = line.split()
    points = int(points)
    cardsConverted = ([order.index(x) for x in cards])
    cardsConvertedPart2 = ([orderpart2.index(x) for x in cards])

    score = calculate_score(cardsConverted, False)
    hands.append([score, cardsConverted, cards, points])

    scorePart2 = calculate_score(cardsConvertedPart2, True)
    handsPart2.append([scorePart2, cardsConvertedPart2, cards, points])


def comparator(item1, item2):
    [score1, cards1, _, _] = item1
    [score2, cards2, _, _] = item2
    if score1 != score2:
        return -1 if score1 < score2 else 1
    for i in range(5):
        if cards1[i] != cards2[i]:
            return -1 if cards1[i] < cards2[i] else 1

    return 0


hands = sorted(
    hands,
    reverse=True,
    key=cmp_to_key(comparator)
)

part1 = 0
for i, x in enumerate(hands):
    part1 += (i+1) * x[3]

print("Part 1", part1)

handsPart2 = sorted(
    handsPart2,
    reverse=True,
    key=cmp_to_key(comparator)
)
part2 = 0
for i, x in enumerate(handsPart2):
    part2 += (i+1) * x[3]

print("Part 2", part2)
