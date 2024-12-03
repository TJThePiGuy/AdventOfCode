import helper.aocdUtil as util

data = [_.split('\n') for _ in util.getData(5,2023,False).split('\n\n')]

firstRow = [int(i) for i in data[0][0].split(' ')[1:]]

currentSeeds = []

for idx in range(0,len(firstRow),2):
    currentSeeds.append(tuple(firstRow[idx:idx+2]))

for newMaps in data[1:]:
    seedUnchanged = [True]*len(currentSeeds)
    firstLine = newMaps[0]
    newMaps = newMaps[1:]
    
    for idx, val in enumerate(currentSeeds):
        seedCount = val[0]
        seedLength = val[1]

        for map in newMaps:

            ranges = [int(i) for i in map.split()]
            lowerBound = ranges[1]
            length = ranges[2]
        
            if seedUnchanged[idx] and (seedCount-lowerBound) in range(length):
                if(seedCount + seedLength <= lowerBound + length):
                    currentSeeds[idx] = ((seedCount-lowerBound) + ranges[0], seedLength)
                    seedUnchanged[idx] = False
                else:
                    currentSeeds[idx] = ((seedCount-lowerBound) + ranges[0], length - (seedCount - lowerBound))
                    seedUnchanged[idx] = False

                    currentSeeds.append((lowerBound+length, seedLength+seedCount - length-lowerBound))
                    seedUnchanged.append(True)
                break

util.submit(min(i for i in currentSeeds)[0],5,2023,'b')