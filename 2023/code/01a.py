import regex
import helper.aocdUtil as util

day1 = util.getData(day=1,year=2023).split()

total = 0
p = regex.compile(r'\d')
for line in day1:
    match = p.findall(line)
    total += int(match[0] + match[-1])

util.submit(answer=total, day=1, year=2023, part='a')
