from helper.aocdUtil import getData, submit
from enum import Enum
from functools import cache

rawData = getData(20,2023,False)
rawData = '''broadcaster -> a
%a -> inv, con
&inv -> b
%b -> con
&con -> output'''
moduleStrings = rawData.split('\n')

class ModuleType(Enum):
    NONE = 0
    FLIP_FLOP = 1
    CONJUNCTION = 2

modules = dict()
active = set()

def getHash():
    return sum(0b1<<idx for idx in range(len(modules)) if modules.keys()[idx] in active)

def getSet(integer):
    return set(idx for idx in range(len(modules)) if int(integer>>idx)%2 == 1)

for idx, module in enumerate(moduleStrings):
    splitModule = module.split(' -> ')
    label = splitModule[0]
    targets = splitModule[1].split(', ')
    moduleType = ModuleType.NONE
    
    if label[0] == '%':
        moduleType = ModuleType.FLIP_FLOP
        label = label[1:]
    elif label[0] == '&':
        moduleType = ModuleType.CONJUNCTION
        label = label[1:]

    modules[label] = [idx, moduleType, targets, False]

visitedStateSets = dict()

def sendSignal(moduleName, high:bool) -> tuple:
    module = modules.get(moduleName,False)
    if not module:
        return([],False)
    mType, targets, state = module[1:]
    if mType == ModuleType.FLIP_FLOP:
        if not high:
            modules[moduleName][3] = not modules[moduleName][3]
            return (targets, modules[moduleName][3])
        return ([],False)
    elif mType == ModuleType.CONJUNCTION:
        modules[moduleName][3] = high
        return (targets, modules[moduleName][3])
    else:
        return (targets, modules[moduleName][3])

totalPulses = 0

while (hash:=getHash()) not in visitedStateSets:
    visitedStateSets.add(hash)
    sendSignal('broadcaster', False)
    signalQueue = [('broadcaster',False)]
    loops = 0
    while len(signalQueue) != 0 and loops <10000:
        print((signalQueue))
        totalPulses += len(signalQueue)
        newQueue = []
        for signal in signalQueue:
            targets, state = sendSignal(signal[0],signal[1])
            newQueue.extend((target, state) for target in targets)
        signalQueue = newQueue.copy()
        loops += 1
    break

