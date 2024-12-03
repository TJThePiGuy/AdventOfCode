import regex
from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(year=2024, day=1)

def part_a():

    data = puzzle.input_data.split('\n')

    rows = [_.split() for _ in data]
    col1 = sorted([int(rows[j][0]) for j in range(len(rows))])
    col2 = sorted([int(rows[j][1]) for j in range(len(rows))])

    diff = [abs(col1[i] - col2[i]) for i in range(len(col1))]

    puzzle.answer_a = sum(diff)
    print(sum(diff))

def part_b():
    data = puzzle.input_data.split('\n')

    rows = [_.split() for _ in data]
    col1 = sorted([int(rows[j][0]) for j in range(len(rows))])
    col2 = sorted([int(rows[j][1]) for j in range(len(rows))])
    total = 0
    for j in col1:
        for i in col2:
            if i==j:
                total += i
    puzzle.answer_b = total
    print(total)

part_a()
part_b()