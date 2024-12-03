from helper.aocdUtil import getData, submit

rawData = getData(14,2023,True)

lines = [list(i) for i in rawData.split('\n')]
height = len(lines)
width = len(lines[0])

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

H = height
load = 0
for line in lines:
    load += H * line.count('O')
    H -= 1
submit(load,14,2023,'a')