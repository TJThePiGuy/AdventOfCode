from aocd.models import Puzzle

puzzle = Puzzle(year = 2025, day = 5)
data = puzzle.input_data.split('\n\n')

rules = [word.split('-') for word in data[0].split('\n')]

ranges = set((int(i[0]),int(i[1])) for i in rules)

def part_a():
    count = 0

    for num in data[1].split('\n'):
        num = int(num)
        found = False
        for i,j in ranges:
            if i<=num and num<=j:
                found = True
                break
        if found:
            count += 1
    print(count)
    puzzle.answer_a = count

def part_b():
    unique_ranges = set()
    for nextL, nextR in ranges:
        to_remove = set()
        for L, R in unique_ranges:
            if nextR < L or R < nextL:
                continue
            nextL = min(L, nextL)
            nextR = max(R, nextR)
            to_remove.add((L,R))
        unique_ranges.difference_update(to_remove)
        unique_ranges.add((nextL, nextR))

    count = 0

    for i,j in unique_ranges:
        count += (j-i+1)
    print(count)
    puzzle.answer_b = count

part_a()
part_b()