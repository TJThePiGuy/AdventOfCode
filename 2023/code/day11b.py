import helper.aocdUtil as util

rawData = util.getData(11,2023,False)
lines = rawData.split('\n')
chars = []
for line in lines:
    chars.append([i for i in line])
yExt = set()
xExt = set()

for y in range(len(lines)-1,0,-1):
    if len(set(lines[y])) == 1:
        yExt.add(y)

for x in range(len(lines[0])-1,0,-1):
    if len(set(lines[y][x] for y in range(len(lines))))==1:
        xExt.add(x)

locations = []
for y in range(len(lines)):
    for x in range(len(lines[y])):
        if lines[y][x] == '#':
            locations.append((x,y))

totalDist = 0
for idx in range(len(locations)):
    x1, y1 = locations[idx]
    for jdx in range(idx+1, len(locations)):
        x2, y2 = locations[jdx]
        addedX = [x for x in xExt if x in range(min(x1,x2),max(x1,x2))]
        addedY = [y for y in yExt if y in range(y1,y2)]
        totalDist += abs(x1-x2) + len(addedX)*999_999 + (y2-y1)+ len(addedY)*999_999
util.submit(totalDist,11,2023,'b')