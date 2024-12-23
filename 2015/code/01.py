from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day = 1, year = 2015)

def part_a():
    ans = sum(1 if i== '(' else -1 for i in puzzle.input_data)
    print(ans)
    puzzle.answer_a = ans

def part_b():
    sums = np.cumsum([1 if i== '(' else -1 for i in puzzle.input_data])
    for floor, s in enumerate(sums,1):
        if s == -1:
            print(floor)
            puzzle.answer_b = floor
            break


part_a()
part_b()