from helper.aocdUtil import getData, submit
import regex as re

workflowMatcher = re.compile(r'\w+')
mapMatcher = re.compile(r'\{.*\}')

rawData = getData(19,2023,True)

data = rawData.split('\n\n')
maps = data[0].split('\n')

mapDict = dict()

for map in maps:
    match:re.Match = (workflowMatcher.match(map))
    workflow = (match[0])
    conditions = mapMatcher.match(map[len(workflow):])[0][1:-1]

    currentConditions = []
    for condition in conditions.split(','):
        
        nums = ''.join(c for c in condition if c.isdigit())
        if len(nums) == 0:
            currentConditions.append(condition)
            continue

        value = condition[0]
        number = int(nums)
        comparison = condition[1]
        target = condition.split(':')[1]

        currentConditions.append((value, comparison, number,target))
    
    mapDict[workflow] = currentConditions

currentRanges = [['in',(1,4000),(1,4000),(1,4000),(1,4000)]]

strMap = {'x':1,'m':2,'a':3,'s':4}

totalRanges =0

while len(currentRanges) > 0:
    newRanges = []

    for currentRange in currentRanges:

        workflowStr = currentRange[0]
        currentWorkflow = mapDict[workflowStr]
        newWorkflowStr = ''

        for check in currentWorkflow:

            if type(check) != tuple:
                newWorkflowStr = check
                break

            value, comparison, number, target = check

            idx = strMap[value]

            upperBound = currentRange[idx][1]
            lowerBound = currentRange[idx][0]

            if comparison == '<' and upperBound < number:
                newWorkflowStr = target
                break

            if comparison == '>' and lowerBound > number:
                newWorkflowStr = target
                break

            if comparison == '<' and lowerBound < number and number <= upperBound:
                newRangeLowerBound = number
                newRangeUpperBound = upperBound

                newRange = currentRange.copy()
                newRange[idx] = (newRangeLowerBound, newRangeUpperBound)
                newRanges.append(newRange)

                upperBound = number-1
                currentRange[idx] = (lowerBound, upperBound)
                newWorkflowStr = target
                break

            if comparison == '>' and upperBound > number and number >= lowerBound:
                newRangeLowerBound = lowerBound
                newRangeUpperBound = number

                newRange = currentRange.copy()
                newRange[idx] = (newRangeLowerBound, newRangeUpperBound)
                newRanges.append(newRange)

                lowerBound = number+1
                currentRange[idx] = (lowerBound, upperBound)
                newWorkflowStr = target
                break

        if(newWorkflowStr) == 'A':
            numberInRange = 1
            for (lower,upper) in currentRange[1:]:
                numberInRange *= (upper-lower+1)


            totalRanges += numberInRange
            continue
        elif newWorkflowStr == 'R':
            continue

        newRange = currentRange.copy()
        newRange[0] = newWorkflowStr
        newRanges.append(newRange)
    currentRanges = newRanges.copy()

submit(totalRanges,19,2023,'b')