import helper.aocdUtil as util

data = util.getData(10,2023,False).split('\n')
width = len(data[0])
height = len(data)

rules = [
    (1,0, '-J7', '-FL'),
    (-1,0,'-FL', '-J7'),
    (0,1, '|JL', '|F7'),
    (0,-1,'|F7', '|JL')]

startPos = None
for y in range(height):
    for x in range(width):
        if data[y][x] == 'S':
            startPos = (x,y)
            possibleChars = {i for i in '-|J7FL'}
            for (dx,dy,endChars, startChars) in rules:
                if not(x+dx in range(width) and y+dy in range(height)):
                    continue
                if data[y+dy][x+dx] in endChars:
                    possibleChars = possibleChars.intersection({i for i in startChars})
            data[y] = data[y].replace('S',possibleChars.pop())

pointsVisited = []
pointsToVisit = [startPos]
while(len(pointsToVisit) != 0):
    nextPoints = []
    for point in pointsToVisit:
        x,y = point
        currChar = data[y][x]
        for (dx,dy,endChars, startChars) in rules:
            if not(currChar in startChars) :
                continue
            if not(x+dx in range(width) and y+dy in range(height)):
                continue
            if (x+dx,y+dy) in pointsVisited:
                continue
            if data[y+dy][x+dx] in endChars:
                nextPoints.append((x+dx,y+dy))
        pointsVisited.append(point)
    pointsToVisit = nextPoints.copy()

areaEnclosed = 0
for y in range(height):
    enclosed = False
    inWall = False
    wallChar = ''
    for x in range(width):
        currChar = data[y][x]
        if (x,y) in pointsVisited:
            if currChar in '|':
                enclosed = not enclosed
            elif currChar in 'FL':
                inWall = True
                wallChar = currChar
            elif currChar in '7J':
                inWall = False
                if (wallChar == 'F' and currChar == 'J') or (wallChar == 'L' and currChar == '7'):
                    enclosed = not enclosed
        else:
            areaEnclosed += int(enclosed)
util.submit(areaEnclosed, 10,2023,'b')