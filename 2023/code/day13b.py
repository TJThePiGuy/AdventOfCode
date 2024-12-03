from helper.aocdUtil import getData, submit

rawData = getData(13,2023,True)
# rawData = '''#.##..##.
# ..#.##.#.
# ##......#
# ##......#
# ..#.##.#.
# ..##..##.
# #.#.##.#.

# #...##..#
# #....#..#
# ..##..###
# #####.##.
# #####.##.
# ..##..###
# #....#..#'''
valley = rawData.split('\n\n')

totalMirrorIdx = 0

for idx,pattern in enumerate(valley):
    rows = pattern.split('\n')
    width = len(rows[0])
    height = len(rows)

    for lineNum in range(1,height):
        dist = min(lineNum, height-lineNum)
        totalDiff = 0
        for dy in range(dist):
            above = rows[lineNum-dy-1] 
            below = rows[lineNum+dy]
            totalDiff += sum(i!= j for i,j in zip(above,below))
        if totalDiff == 1:
            print(idx, lineNum, 'h')
            totalMirrorIdx += 100*lineNum


    for lineNum in range(1,width):
        dist = min(lineNum, width-lineNum)
        totalDiff = 0
        for dx in range(dist):
            left = [rows[y][lineNum-dx-1] for y in range(height)]
            right = [rows[y][lineNum+dx] for y in range(height)]
            totalDiff += sum(i!=j for i,j, in zip(left, right))
        if totalDiff == 1:
            totalMirrorIdx += lineNum
            print(idx, lineNum, 'v')


print(totalMirrorIdx)

submit(totalMirrorIdx,13,2023,'b')