import helper.aocdUtil as util
import regex as re
import math

data = util.getData(6,2023).split('\n')
nums = re.compile(r'\d+')

recordBeats = 1

for (time,dist) in zip(nums.findall(data[0]),nums.findall(data[1])):
    totalDist = int(dist)
    totalTime = int(time)
    
    lowerB = math.ceil((totalTime - math.sqrt(pow(totalTime,2)-4*totalDist))/2)
    upperB = math.ceil((totalTime + math.sqrt(pow(totalTime,2)-4*totalDist))/2)
    recordBeats *= upperB - lowerB
    
util.submit(recordBeats,6,2023,'a')