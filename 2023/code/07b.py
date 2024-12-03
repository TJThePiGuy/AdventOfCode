import helper.aocdUtil as util
import regex as re
import functools

fiveKind = re.compile(r'(\w)\1{4}')
fourKind = re.compile(r'\w?(\w)\1{3}\w?')
fullHouse = re.compile(r'(\w)\1{2}(\w)\2{1}|(\w)\3{1}(\w)\4{2}')
threeKind = re.compile(r'\w{0,2}(\w)\1{2}\w{0,2}')
twoPair = re.compile(r'.?(\w)\1.?(\w)\2')
onePair = re.compile(r'.*(\w)\1.*')

allHands = [fiveKind, fourKind, fullHouse, threeKind, twoPair, onePair]

data = util.getData(7,2023,False).split('\n')
hands = [i.split(' ') for i in data]

sortedHands = [[],[],[],[],[],[],[]]

for hand in hands:
    (totalHand, value) = hand
    sortedHand = ''.join(sorted(totalHand))
    valueCount = {}
    for char in totalHand:
        valueCount[char] = sortedHand.count(char)
    found = False
    jokerCount = valueCount.get('J',0)
    if jokerCount == 0:
        for idx, matchHand in enumerate(allHands):
            Match = matchHand.match(sortedHand)
            if not found and Match:
                sortedHands[idx].append(hand)
                found = True
        if not found:
            sortedHands[6].append(hand)
    else:
        valueCount.pop('J',None)
        values = valueCount.values()
        if len(values) == 0 or max(values) + jokerCount == 5:
            sortedHands[0].append(hand)
        elif max(values) + jokerCount == 4:
            sortedHands[1].append(hand)
        elif len(values) == 2:
            sortedHands[2].append(hand)
        elif len(values) == 3:
            sortedHands[3].append(hand)
        else:
            sortedHands[5].append(hand)

valueToVal = {'A':14, 'K':13, 'Q':12, 'J':-1, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5, '4':4, '3':3, '2':2}
 
def compare(item1, item2):
    for v1, v2 in zip(item1[0], item2[0]):
        if valueToVal[v1] > valueToVal[v2]:
            return -1
        if valueToVal[v1] < valueToVal[v2]:
            return 1
    return 0

for hands in sortedHands:
    hands.sort(key=functools.cmp_to_key(compare))

handNo = 1
val = 0

for hands in sortedHands[::-1]:
    for hand in hands[::-1]:
        val += handNo * int(hand[1])
        handNo += 1
util.submit(val, 7,2023,'b')