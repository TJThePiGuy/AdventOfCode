import helper.aocdUtil as util

day1 = util.getData(day=1,year=2023).split()
total2 = 0

numDict = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'zero':0}

for line in day1:

    y = ""
    for i in range(len(line)):
        if line[i] in "0123456789":
            y = y+line[i]
        else:
            for number in numDict.keys():
                if line[i:i+len(number)] == number:
                    y+= str(numDict.get(number));

    total2 += int(y[0]+y[-1])

util.submit(answer=total2,day=1,year=2023,part='b')
