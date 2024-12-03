import helper.aocdUtil as util

data = util.getData(day=2,year=2023).split('\n')

cumPower = 0
for x,game in enumerate(data,1):
    trials = [_.split(', ') for _ in game.split(': ')[1].split('; ')]
    red = 0
    green = 0
    blue = 0
    for trial in trials:
        draws = [_.split() for _ in trial]
        for draw in draws:
            count = int(draw[0])
            color = draw[1]
            if (color == 'red'):
                red = max(count, red)
            elif(color == 'green'):
                green = max(count, green)
            elif(color == 'blue'):
                blue = max(count, blue)
    cumPower += red*green*blue
util.submit(cumPower,2,2023,'b')