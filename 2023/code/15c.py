from helper.aocdUtil import getData, submit
from functools import cache

rawData = getData(15,2023,True)

@cache
def getHash(string):
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    return current

strings = rawData.split(',')
total = 0
boxes:list[dict[str,int]] = [dict() for _ in range(256)]

for string in strings:
    if string[-1] == '-':
        substr = string[:-1]
        hash=getHash(substr)
        boxes[hash].pop(substr,-1)
    else:
        substr = string[:-2]
        num = int(string[-1])
        hash=getHash(substr)
        boxes[hash][substr] = num
    
totalFocus = 0
for boxNum, valBox in enumerate(boxes, 1):
    for slotNum, val in enumerate(valBox.values(), 1):
        totalFocus += val*boxNum*slotNum
print(totalFocus)
submit(totalFocus,15,2023,'b')