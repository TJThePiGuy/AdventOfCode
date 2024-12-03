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
boxKeys = []
boxVals = []
for i in range(256):
    boxKeys.append([])
    boxVals.append([])

for string in strings:
    if string[-1] == '-':
        substr = string[:-1]
        hash=getHash(substr)
        if substr in boxKeys[hash]:
            idx = boxKeys[hash].index(substr)
            boxKeys[hash].pop(idx)
            boxVals[hash].pop(idx)
    else:
        substr = string[:-2]
        num = int(string[-1])
        hash=getHash(substr)
        if substr in boxKeys[hash]:
            idx = boxKeys[hash].index(substr)
            boxVals[hash][idx] = num
        else:
            boxKeys[hash].append(substr)
            boxVals[hash].append(num)
    
totalFocus = 0
for boxNum, valBox in enumerate(boxVals, 1):
    for slotNum, val in enumerate(valBox, 1):
        totalFocus += val*boxNum*slotNum
print(totalFocus)
submit(totalFocus,15,2023,'b')