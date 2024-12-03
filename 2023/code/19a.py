from helper.aocdUtil import getData, submit
import regex as re

workflowMatcher = re.compile(r'\w+')
mapMatcher = re.compile(r'\{.*\}')

rawData = getData(19,2023,True)
data = rawData.split('\n\n')
maps = data[0].split('\n')

mapDict = dict()

for map in maps[1:]:
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

ratings = [tuple(re.findall(r'\d+',line)) for line in data[1].split('\n')]


ratingNumberSum = 0
for rating in ratings:
    x,m,a,s = (int(i) for i in rating)
    testDict = {'x':x,'m':m,'a':a,'s':s}
    workflowStr = 'in'

    while workflowStr not in 'AR':

        currentWorkflow = mapDict[workflowStr]
        for check in currentWorkflow:
            if type(check) != tuple:
                workflowStr = check
                break
            value, comparison, number, target = check
            if comparison == '<' and testDict[value] < number:
                workflowStr = target
                break
            elif comparison == '>' and testDict[value] > number:
                workflowStr = target
                break

    if workflowStr == 'A':
        ratingNumberSum += sum(testDict.values())

submit(ratingNumberSum,day=19,year=2023,part='a')