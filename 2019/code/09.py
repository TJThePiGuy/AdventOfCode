from aocd.models import Puzzle
from intcode import IntCodeComputer

puzzle = Puzzle(year = 2019, day = 9)

data = puzzle.input_data

instr = [int(i) for i in data.split(',')]

print('Part A')
computer = IntCodeComputer(instr, input_console=False, input_arr=[1])
computer.compute()
print('Part B')
computer = IntCodeComputer(instr, input_console=False, input_arr=[2])
computer.compute()