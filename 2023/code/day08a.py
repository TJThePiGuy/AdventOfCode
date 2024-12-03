import helper.aocdUtil as util

data = util.getData(8,2023,True).split('\n')

steps = data[0]

mapString = data[2:]
maps = dict()
for mS in mapString:
    maps[mS[0:3]] = (mS[7:10],mS[12:15])

currentLoc = 'AAA'

stepCount = 0
while currentLoc != 'ZZZ':
    if steps[(stepCount)%len(steps)] == 'L':
        currentLoc = maps[currentLoc][0]
    else:
        currentLoc = maps[currentLoc][1]
    stepCount += 1

util.submit(stepCount, 8, 2023, 'a')