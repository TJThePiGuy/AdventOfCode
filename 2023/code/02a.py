import helper.aocdUtil as util

data = util.getData(day=2,year=2023).split('\n')

cumIdx = 0
for x,game in enumerate(data,1):
    trials = [_.split(', ') for _ in game.split(': ')[1].split('; ')]
    possible = True
    for trial in trials:
        draws = [_.split() for _ in trial]
        for draw in draws:
            count = int(draw[0])
            color = draw[1]
            if (color == 'red' and count >12) or (color=='green' and count>13) or (color=='blue' and count>14):
                possible = False
            if not possible:
                break
    if possible:
        cumIdx += x;

util.submit(cumIdx,2,2023,'a')