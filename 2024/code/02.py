import regex
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2024, day=2)

def part_a():
    count = 0
    rows = [[int(i) for i in _.split()] for _ in puzzle.input_data.split('\n')]
    for row in rows:
        diffs = np.diff(row)
        if not(all(i > 0 for i in diffs) or all(i < 0 for i in diffs)):
            continue
        if any(abs(i) > 3 or i==0 for i in diffs):
            continue
        count += 1

    print(count)
    puzzle.answer_a = count

def part_b():
    count = 0
    rows = [[int(i) for i in _.split()] for _ in puzzle.input_data.split('\n')]
    for old_row in rows:
        good = False
        for idx in range(len(old_row)+1):
            row = old_row[:idx]+old_row[idx+1:]
            diffs = np.diff(row)
            if not(all(i > 0 for i in diffs) or all(i < 0 for i in diffs)):
                continue
            if any(abs(i) > 3 or i==0 for i in diffs):
                continue
            good = True
            break
        if good:
            count += 1

    print(count)
    puzzle.answer_b = count

part_a()
part_b()