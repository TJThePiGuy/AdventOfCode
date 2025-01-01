from aocd.models import Puzzle
from intcode import IntCodeComputer
from collections import defaultdict

puzzle = Puzzle(year = 2019, day = 13)

data = puzzle.input_data

instr = [int(i) for i in data.split(',')]

def part_a():
    computer = IntCodeComputer(instructions=instr, print_out=False, input_console=False)
    computer.compute()

    count = 0
    for ident in computer.output_arr[2::3]:
        if ident == 2:
            count += 1
    print(count)
    puzzle.answer_a = count

def part_b():
    instr_b = instr.copy()
    instr_b[0] = 2
    computer = IntCodeComputer(instructions=instr_b, print_out=False, input_console=False)
    computer.compute()
    has_block = True
    while has_block:
        print(len(computer.output_arr))
        pad_x = 0
        ball_x = 0
        score = 0
        has_block = False
        while len(computer.output_arr) > 0:
            id = computer.output_arr.pop()
            y = computer.output_arr.pop()
            x = computer.output_arr.pop()
            if x == -1 and y == 0:
                score = id
            if id == 3:
                pad_x = x
            elif id == 4:
                ball_x = x
            elif id == 2:
                has_block = True
        # print(score)
        if pad_x == ball_x:
            computer.add_input(0)
        else:
            computer.add_input(-1 if ball_x < pad_x else 1)
        computer.compute()

# part_a()
part_b()