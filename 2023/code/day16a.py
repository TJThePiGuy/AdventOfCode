from helper.aocdUtil import getData, submit

rawData = getData(16, 2023, False)
maze = [[i for i in string] for string in rawData.split("\n")]
width = len(maze[0])
height = len(maze[1])

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

beams = [(-1, 0, 1, 0)]
energized = set()
beamPaths = set()
started = False

while len(beams) > 0:
    x, y, dx, dy = beams.pop(0)
    if started:
        energized.add((x, y))
    started = True
    beamPaths.add((x, y, dx, dy))
    nextX, nextY = x + dx, y + dy
    if nextX in range(width) and nextY in range(height):
        char = maze[nextY][nextX]
        nextDirDict: dict | int = charToDirs.get(char, -1)

        nextDirs: list[tuple] = nextDirDict.get((dx, dy), [(dx, dy)])

        for nextDirs in nextDirs:
            nextDx, nextDy = nextDirs

            nextBeam = (nextX, nextY, nextDx, nextDy)

            if not (nextBeam in beamPaths or nextBeam in beams):
                beams.append((nextX, nextY, nextDx, nextDy))

submit(len(energized), 16, 2023, "a")