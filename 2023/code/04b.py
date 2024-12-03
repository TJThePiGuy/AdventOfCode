import helper.aocdUtil as util

data = [_.split('|') for _ in util.getData(day=4,year=2023,save=True).split('\n')]
cardCount = [1 for _ in data]

for idx, card in enumerate(data):

    wins = card[0].split(':')[1].split()
    mine = card[1].split()

    currWins = 0

    for num in mine:
        if num in wins:
            currWins += 1
    for jdx in range(1, currWins+1):
        cardCount[idx+jdx] += cardCount[idx]

util.submit(sum(cardCount),4,2023,'b')