import helper.aocdUtil as util
import math

data = util.getData(8,2023,True).split('\n')

currentLocs = []
steps = data[0]

mapString = data[2:]
maps = dict()
currentLocs = []
for mS in mapString:
    maps[mS[0:3]] = (mS[7:10],mS[12:15])
    if mS[2] == 'A':
        currentLocs.append(mS[0:3])

loops = 0
lengthLoops = [0] * len(currentLocs)

while any(i ==0 for i in lengthLoops):
    direction = 0 if steps[(loops%len(steps))] == 'L' else 1
    currentLocs = [maps[i][direction] for i in currentLocs]
    loops += 1
    for idx in range(len(currentLocs)):
        if lengthLoops[idx] != 0:
            continue
        if currentLocs[idx].endswith('Z'):
            lengthLoops[idx] = loops
util.submit(math.lcm(*lengthLoops),8,2023,'b')