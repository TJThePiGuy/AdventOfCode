import helper.aocdUtil as util

data = [_.split('\n') for _ in util.getData(5,2023).split('\n\n')]

currentSeeds = [int(i) for i in data[0][0].split(' ')[1:]]

for newMaps in data[1:]:
    seedUnchanged = [True]*len(currentSeeds)
    newMaps = newMaps[1:]
    for map in newMaps:
        ranges = [int(i) for i in map.split()]
        lowerBound = ranges[1]
        length = ranges[2]
        for idx, val in enumerate(currentSeeds):
            
            if seedUnchanged[idx] and (val-lowerBound) in range(length):
                currentSeeds[idx] = (val-lowerBound) + ranges[0]
                seedUnchanged[idx] = False

util.submit(min(currentSeeds),5,2023,'a')