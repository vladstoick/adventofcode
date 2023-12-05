from pathlib import Path
import regex as re

p = Path(__file__).with_name("input.txt")
file = open(p)

matchedNumbersPerCard = []

for line in file.readlines():
    winningNumbersStr = line.split("|")[0]
    winningNumbersMatches = re.findall("(\d+)", winningNumbersStr)
    winningNumbersMatches = [int(x) for x in winningNumbersMatches]
    winningNumbers = set(winningNumbersMatches[1:])
    
    playedNumbersStr = line.split("|")[1]
    playedNumbersMatches = re.findall("(\d+)", playedNumbersStr)
    playedNumbersMatches = [int(x) for x in playedNumbersMatches]
    playedNumbers = set(playedNumbersMatches)

    matchedNumbersSet = winningNumbers.intersection(playedNumbers)
    matchedNumbers = len(matchedNumbersSet)
    matchedNumbersPerCard.append(matchedNumbers)

part1Values = [0 if matchedNumbers == 0 else  2**(matchedNumbers - 1) for matchedNumbers in matchedNumbersPerCard]
part1 = sum(part1Values)
print("Part 1", part1)

noCards = len(matchedNumbersPerCard)

part2Vals = [1 for x in range(noCards)]

for card in range(noCards):
    if matchedNumbersPerCard[card] > 0:
        didWin = True
        for cardToAdd in range(card + 1, min(noCards, card + matchedNumbersPerCard[card]) + 1):
            part2Vals[cardToAdd] += part2Vals[card]

part2 = sum(part2Vals)
print("Part 2", part2)


