from aocd.models import Puzzle
import numpy as np
from itertools import groupby

puzzle = Puzzle(year = 2019, day = 4)

data = puzzle.input_data

def part_a():
    nums = [int(i) for i in data.split('-')]
    lower = nums[0]
    upper = nums[1]
    good = 0
    for N in range(lower, upper+1):
        digits = [int(i) for i in str(N)]
        if all(i != j for i,j in zip(digits[:-1],digits[1:])):
            continue
        if any(i>j for i,j in zip(digits[:-1],digits[1:])):
            continue
        good += 1
    print(good)
    puzzle.answer_a = good

def part_b():
    nums = [int(i) for i in data.split('-')]
    lower = nums[0]
    upper = nums[1]
    good = 0
    for N in range(lower, upper+1):
        S = str(N)
        digits = [int(i) for i in S]
        if any(i>j for i,j in zip(digits[:-1],digits[1:])):
            continue
        has_two = False
        for k, g in groupby(digits):
            if len(list(g)) == 2:
                has_two = True
                break

        if has_two:
            good += 1
    print(good)
    puzzle.answer_b = good

part_a()
part_b()