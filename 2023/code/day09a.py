import helper.aocdUtil as util

data = [[int(j) for j in i.split()] for i in util.getData(9,2023,True).split('\n')]

totalPredict = 0
for line in data:
    
    lines = [line]
    while any(i != 0 for i in line):
        line = [line[idx+1]-line[idx] for idx in range(len(line)-1)]
        lines.append(line)
    line.append(0)
    for idx in range(len(lines)-1, 0, -1):
        lines[idx-1].append(lines[idx-1][-1]+lines[idx][-1])
    totalPredict+=lines[0][-1]
util.submit(totalPredict,9,2023,'a')