from aocd.models import Puzzle
from intcode import execute_intcode

puzzle = Puzzle(year = 2019, day = 5)

data = puzzle.input_data
# data = '''1002,4,3,4,33'''

instr = [int(i) for i in data.split(',')]
print('Part A')
execute_intcode(instr)
print('Part B')
execute_intcode(instr)