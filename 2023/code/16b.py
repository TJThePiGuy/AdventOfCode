from helper.aocdUtil import getData, submit
from functools import cache

charToDirs = {
    '.':
    {
        (0,1):[(0,1)],
        (0,-1):[(0,-1)],
        (1,0):[(1,0)],
        (-1,0):[(-1,0)]
    },
    '-':
    {
        (0,1): [(1,0),(-1,0)],
        (0,-1): [(1,0),(-1,0)],
        (1,0):[(1,0)],
        (-1,0):[(-1,0)]
    },
    '|':
    {
        (1,0):[(0,1),(0,-1)],
        (-1,0):[(0,1),(0,-1)],
        (0,1):[(0,1)],
        (0,-1):[(0,-1)],

    },
    "\\":{
        (1,0):[(0,1)],
        (-1,0):[(0,-1)],
        (0,1):[(1,0)],
        (0,-1):[(-1,0)]
    },
    '/':{
        (1,0):[(0,-1)],
        (-1,0):[(0,1)],
        (0,1):[(-1,0)],
        (0,-1):[(1,0)]
    }
}

rawData = getData(16, 2023, False)
maze = [[i for i in string] for string in rawData.split("\n")]
width = len(maze[0])
height = len(maze[1])

beamPaths = set()


@cache
def move(x, y, dx, dy):
    newBeams = []
    nextX, nextY = x + dx, y + dy
    if nextX in range(width) and nextY in range(height):
        char = maze[nextY][nextX]
        nextDirDict: dict | int = charToDirs.get(char, -1)

        nextDirs: list[tuple] = nextDirDict.get((dx, dy), [(dx, dy)])

        for nextDirs in nextDirs:
            nextDx, nextDy = nextDirs
            nextBeam = (nextX, nextY, nextDx, nextDy)
            newBeams.append((nextX, nextY, nextDx, nextDy))
    return newBeams


def lineTest(x, y, dx, dy):
    beamPaths = set()
    beams = [(x, y, dx, dy)]
    energized = set()
    beamPaths = set()
    started = False
    while len(beams) > 0:
        x, y, dx, dy = beams.pop(0)

        if started:
            energized.add((x, y))
        started = True
        beamPaths.add((x, y, dx, dy))
        for beam in move(x, y, dx, dy):
            if not (beam in beamPaths or beam in beams):
                beams.append(beam)

    return len(energized)


maxTest = 0

for yStart in range(height):
    maxTest = max(maxTest, lineTest(-1, yStart, 1, 0), lineTest(width, yStart, -1, 0))

for xStart in range(width):
    maxTest = max(maxTest, lineTest(xStart, -1, 0, 1), lineTest(xStart, height, 0, -1))

submit(maxTest, 16, 2023, "b")