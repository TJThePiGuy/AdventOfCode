from helper.aocdUtil import getData, submit
from functools import cache

rawData = getData(14,2023,False)
lines = rawData
tempLines = [list(i) for i in rawData.split('\n')]
height = len(tempLines)
width = len(tempLines[0])

def calcLoad(str):
    H = height
    load = 0
    for line in str.split('\n'):
        load += H * line.count('O')
        H -= 1
    return(load)

def cycle(lines:str):
    lines = [list(i) for i in lines.split('\n')]

    idx = 1
    while(idx < height):
        if (idx == 0):
            idx = 1
            continue
        moved = False
        for jdx in range(width):
            if (lines[idx][jdx] == 'O' and lines[idx-1][jdx]=='.'):
                lines[idx][jdx] = '.'
                lines[idx-1][jdx] = 'O'
                moved = True
        if moved:
            idx -= 1
        else:
            idx += 1

    jdx = 1
    while(jdx < width):
        if (jdx == 0):
            jdx = 1
            continue
        moved = False
        for idx in range(height):
            if (lines[idx][jdx] == 'O' and lines[idx][jdx-1]=='.'):
                lines[idx][jdx] = '.'
                lines[idx][jdx-1] = 'O'
                moved = True
        if moved:
            jdx -= 1
        else:
            jdx += 1

    idx = height-2
    while(idx >= 0):
        if (idx == height-1):
            idx -= 1
            continue
        moved = False
        for jdx in range(width):
            if (lines[idx][jdx] == 'O' and lines[idx+1][jdx]=='.'):
                lines[idx][jdx] = '.'
                lines[idx+1][jdx] = 'O'
                moved = True
        if moved:
            idx += 1
        else:
            idx -= 1

    jdx = width-2
    while(jdx >= 0):
        if (jdx == width-1):
            jdx -= 1
            continue
        moved = False
        for idx in range(height):
            if (lines[idx][jdx] == 'O' and lines[idx][jdx+1]=='.'):
                lines[idx][jdx] = '.'
                lines[idx][jdx+1] = 'O'
                moved = True
        if moved:
            jdx += 1
        else:
            jdx -= 1

    return '\n'.join([''.join(line) for line in lines])

prevLines = lines

cached = dict()
loads = dict()

loads[0] = calcLoad(prevLines)
maxCycles = 1_000_000_000
for cycleCount in range(1,maxCycles+1):
    newLines = cycle(prevLines)

    key = (newLines)
    if(key in cached.keys()):
        loopLen = cycleCount - cached[key]
        correctLoadIdx = (maxCycles - cycleCount) % (loopLen) + cached[key]
        load = loads[correctLoadIdx]
        break
    prevLines = newLines
    cached[key] = cycleCount
    loads[cycleCount] = calcLoad(prevLines)

submit(load,14,2023,'b')