from aocd.models import Puzzle
from itertools import product

puzzle = Puzzle(year = 2024, day = 25)

data = puzzle.input_data

def part_a():

    objs = data.split('\n\n')

    keys = set()
    locks = set()

    for obj in objs:
        lines = obj.split('\n')
        heights = tuple(sum(line[i] == '#' for line in lines) for i in range(5))
        if all(c == '#' for c in lines[0]):
            locks.add(heights)
        else:
            keys.add(heights)
    total = 0
    for k, l in product(keys, locks):
        if all(k[i] + l[i] <= 7 for i in range(5)):
            total += 1
    print(total)
    puzzle.answer_a = total
    
part_a()