from helper.aocdUtil import getData, submit

rawData = getData(15,2023,True)


strings = rawData.split(',')
total = 0
for string in strings:
    current = 0
    for char in string:
        current += ord(char)
        current *= 17
        current %= 256
    total += current
submit(total,15,2023,'a')