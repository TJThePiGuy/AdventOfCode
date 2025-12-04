from aocd.models import Puzzle
from itertools import product


puzzle = Puzzle(year = 2025, day = 4)

data = puzzle.input_data
# data = puzzle.examples[0].input_data


def part_a():
    rolls = set()
    for j, line in enumerate(data.split()):
        for i, chr in enumerate(line):
            if chr == '@':
                rolls.add((i,j))
    total = 0
    for i,j in rolls:
        count = -1
        for dx, dy in product((-1,0,1),(-1,0,1)):
            if (i+dx,j+dy) in rolls:
                count += 1
        if count < 4:
            total += 1
    print(total)
    puzzle.answer_a = total

def part_b():
    rolls = set()
    for j, line in enumerate(data.split()):
        for i, chr in enumerate(line):
            if chr == '@':
                rolls.add((i,j))
    total = 0
    start = True
    to_remove = set()
    while start or len(to_remove) > 0:
        start = False
        rolls.difference_update(to_remove)
        to_remove.clear()
        for i,j in rolls:
            count = -1
            for dx, dy in product((-1,0,1),(-1,0,1)):
                if (i+dx,j+dy) in rolls:
                    count += 1
            if count < 4:
                total += 1
                to_remove.add((i,j))

    print(total)
    puzzle.answer_b = total

part_a()
part_b()