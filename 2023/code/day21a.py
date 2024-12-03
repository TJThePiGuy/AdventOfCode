from helper.aocdUtil import getData, submit

from functools import cache
rawData = getData(21,2023,True)

grid = [[_ for _ in line] for line in rawData.split('\n')]
startPos = None

height = len(grid)
width = len(grid[0])

boulders = set()

for y in range(height):
    for x in range(width):
        if grid[y][x] == 'S':
            startPos = (x,y)
        elif grid[y][x] == '#':
            boulders.add((x,y))

print(startPos)

@cache
def getNeighbors(pos):
    x,y = pos
    validNeighbors = {(1,0),(-1,0),(0,1),(0,-1)}
    if x == 0:
        validNeighbors.difference_update({(-1,0)})
        
    if x == width-1:
        validNeighbors.difference_update({(1,0)})
        
    if y == 0:
        validNeighbors.difference_update({(0,-1)})
        
    if y == height-1:
        validNeighbors.difference_update({(0,1)})
    return set((x+dx, y+dy) for dx,dy in validNeighbors)

positions = {startPos}

for idx in range(64):
    newPositions = set()
    for position in positions:
        newPositions = newPositions.union(getNeighbors(position))

    positions = newPositions.difference(boulders)
submit(len(positions),day=21,year=2023,part='a')