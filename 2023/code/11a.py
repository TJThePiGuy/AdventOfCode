import helper.aocdUtil as util

rawData = util.getData(11,2023,False)
lines = rawData.split('\n')
chars = []
for line in lines:
    chars.append([i for i in line])

for y in range(len(lines)-1,0,-1):
    if len(set(lines[y])) == 1:
        lines.insert(y,lines[y])

for x in range(len(lines[0])-1,0,-1):
    if len(set(lines[y][x] for y in range(len(lines))))==1:
        for y in range(len(lines)):
            lines[y] = lines[y][0:x]+"."+lines[y][x:]

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
        totalDist += abs(x1-x2) + abs(y1-y2)

print(totalDist)