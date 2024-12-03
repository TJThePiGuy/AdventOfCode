import helper.aocdUtil as util
from itertools import chain,combinations
import numpy

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def createRanges(given:list[int]):
    given.sort()
    # print(given)
    ranges = []
    currentLen = 0
    currentVal = -1
    for i in given:
        if (currentVal != -1) and i-currentVal != 1:
            ranges.append(currentLen)
            currentLen = 0
        currentLen += 1
        currentVal = i
    ranges.append(currentLen)
    return ranges

rawData = util.getData(12,2023,True)
# rawData = '''???.### 1,1,3
# .??..??...?##. 1,1,3
# ?#?#?#?#?#?#?#? 1,3,1,6
# ????.#...#... 4,1,1
# ????.######..#####. 1,6,5
# ?###???????? 3,2,1'''
data = [i.split() for i in rawData.split('\n')]

totalArrange = 0

for x,line in enumerate(data):
    sizes = [int(i) for i in line[1].split(',')]
    given = [i for i in range(len(line[0])) if line[0][i] == '#']
    unknown = set(i for i in range(len(line[0])) if line[0][i] == '?' )
    
    totalDefective = len(given)
    maxDefective = sum(sizes)
    for thing in combinations(unknown,maxDefective-totalDefective):
        new = given.copy()
        for i in thing:
            new.append(i)
        ranges = createRanges(new)
        # print(new, ranges, sizes)
        if(numpy.array_equal(ranges,sizes)):
            totalArrange += 1
        
    print(x,totalArrange)