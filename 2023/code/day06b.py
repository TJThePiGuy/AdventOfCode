import helper.aocdUtil as util
import math

data = util.getData(6,2023).split('\n')

totalTime = int(data[0].split(':')[1].replace(' ',''))
totalDist = int(data[1].split(':')[1].replace(' ',''))

lowerB = math.ceil((totalTime - math.sqrt(pow(totalTime,2)-4*totalDist))/2)
upperB = math.ceil((totalTime + math.sqrt(pow(totalTime,2)-4*totalDist))/2)

ways = (upperB - lowerB)

util.submit(ways,6,2023,'b')