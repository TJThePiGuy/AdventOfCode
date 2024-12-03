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
steps = 0
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

    steps += 1
util.submit(steps-1,10,2023,'a')