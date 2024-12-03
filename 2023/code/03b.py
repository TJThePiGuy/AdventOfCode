import helper.aocdUtil as util
import regex as re

data = util.getData(day=3,year=2023,save=False).split('\n')
numPat = re.compile(r'\d+')

gears = dict()

for y,line in enumerate(data):
    matches = numPat.finditer(line)
    
    for match in matches:

        x = match.start()
        l = len(match[0])

        left = max(0, x-1)
        right = min(len(line), x+l+1)
        
        for dy in [-1,0,1]:
            j = y+dy
            if j >= 0 and j<len(data):
                for i in range(left, right):
                    if data[j][i] == '*':
                        if (i,j) not in gears.keys():
                            gears[(i,j)] = []
                        gears[(i,j)].append(int(match[0]))

gearRatio = 0
for gear in gears.values():
    if len(gear) == 2:
        gearRatio += gear[0]*gear[1]
util.submit(gearRatio,3,2023,'b')