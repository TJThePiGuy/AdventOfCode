from helper.aocdUtil import getData, submit

rawData = getData(18,2023,False)
directions:list[list[str]] = [_.split() for _ in rawData.split('\n')]

dirMap = {'U':(0,-1),'R':(1,0),'D':(0,1),'L':(-1,0)}

x=y=0

onPath = set()

onPath.add((x,y))

for line in directions:
    dir, dist, color = line
    dist = int(dist)
    dx,dy = dirMap[dir]
    for i in range(dist):
        x+= dx
        y+= dy
        onPath.add((x,y))
minX = min(x for x,y in onPath)
maxX = max(x for x,y in onPath)
minY = min(y for x,y in onPath)
maxY = max(y for x,y in onPath)

inPath = onPath.copy()
firstX = firstY = None

for y in range(minY+1, maxY+1):
    inFigure = False
    for x in range(minX, maxX):
        if ((x,y) in onPath) and ((x-1,y) not in onPath):
            inFigure = not inFigure
        if inFigure:
            firstX = x+1
            firstY = y
        if firstX != None:
            break
    if firstX != None:
        break

toCheck = [(firstX, firstY)]
checked = set((firstX, firstY))

while len(toCheck) > 0:
    x,y = toCheck.pop(0)
    if (x,y) in checked:
        continue
    checked.add((x,y))
    inPath.add((x,y))
    for dx,dy in [(-1,0),(0,1),(1,0),(0,-1)]:
        if (x+dx, y+dy) not in inPath:
            toCheck.append((x+dx,y+dy)) 

submit(len(inPath),18,2023,'a')