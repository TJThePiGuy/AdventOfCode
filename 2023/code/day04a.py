import helper.aocdUtil as util

data = [_.split('|') for _ in util.getData(day=4,year=2023,save=False).split('\n')]

winnings = 0
for wins, mine in data:
    currWins = 0
    wins = wins.split(':')[1].split()
    mine = mine.split()
    for num in mine:
        if num in wins:
            if currWins == 0:
                currWins = 0.5
            currWins *= 2
    winnings += currWins
util.submit(winnings,4,2023,'a')