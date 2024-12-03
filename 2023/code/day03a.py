import helper.aocdUtil as util
import regex as re

data = util.getData(day=3,year=2023,save=False).split('\n')
numPat = re.compile(r'\d+')

partNums = set()

for y,line in enumerate(data):
    matches = numPat.finditer(line)
    
    for match in matches:
        adjSymb = False
        
        x = match.start()
        l = len(match[0])

        left = max(0, x-1)
        right = min(len(line), x+l+1)
        
        for dy in [-1,0,1]:
            j = y+dy
            if j >= 0 and j<len(data):
                if any(data[j][k] not in r'0123456789.' for k in range(left,right)) and not adjSymb:
                    adjSymb = True

        if adjSymb:
            partNums.add((int(match[0]),x,y))

S = sum(j[0] for j in partNums)
print(S)
util.submit(S, 3,2023,'a')