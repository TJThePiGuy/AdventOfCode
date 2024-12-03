from helper.aocdUtil import getData, submit

rawData = getData(13,2023,True)
valley = rawData.split('\n\n')

totalMirrorIdx = 0

for pattern in valley:
    rows = pattern.split('\n')
    width = len(rows[0])
    height = len(rows)
    for lineNum in range(1,height):
        dist = min(lineNum, height-lineNum)

        for dy in range(dist):
            above = rows[lineNum-dy-1] 
            below = rows[lineNum+dy]
            if(above != below):
                break
        else:
            totalMirrorIdx += 100*lineNum
    for lineNum in range(1,width):
        dist = min(lineNum, width-lineNum)

        for dx in range(dist):
            left = [rows[y][lineNum-dx-1] for y in range(height)]
            right = [rows[y][lineNum+dx] for y in range(height)]
            if(left != right):
                break
        else:
            totalMirrorIdx += lineNum

print(totalMirrorIdx)

submit(totalMirrorIdx,13,2023,'a')