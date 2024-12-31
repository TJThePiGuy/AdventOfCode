from aocd.models import Puzzle
from intcode import execute_intcode

puzzle = Puzzle(year = 2019, day = 2)

data = puzzle.input_data
instr = [int(i) for i in data.split(',')]


def part_a():
    instr_a = instr.copy()
    instr_a[1] = 12
    instr_a[2] = 2
    ans = execute_intcode(instr_a, True)
    print(ans)
    puzzle.answer_a = ans

def part_b():
    instr_b = instr.copy()
    for start in range(10000):
        instr_b[1] = start//100
        instr_b[2] = start % 100
        if execute_intcode(instr_b, True) == 19690720:
            break
    print(start)
    puzzle.answer_b = start

part_a()
part_b()