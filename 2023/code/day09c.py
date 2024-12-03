import helper.aocdUtil as util
partAdiff = lambda line: 0 if all(i==0 for i in [line[idx+1]-line[idx] for idx in range(len(line)-1)]) else [line[idx+1]-line[idx] for idx in range(len(line)-1)][-1]+partAdiff([line[idx+1]-line[idx] for idx in range(len(line)-1)])
util.submit(sum(l[-1]+partAdiff(l) for l in [[int(j) for j in i.split()] for i in util.getData(9,2023,True).split('\n')]),9,2023,'a')
util.submit(sum(l[0]+partAdiff(l[::-1]) for l in [[int(j) for j in i.split()] for i in util.getData(9,2023,True).split('\n')]),9,2023,'b')