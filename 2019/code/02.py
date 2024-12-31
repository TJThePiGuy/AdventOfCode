from aocd.models import Puzzle
from collections import defaultdict
from itertools import count

puzzle = Puzzle(year = 2019, day = 2)

data = puzzle.input_data
instr = [int(i) for i in data.split(',')]

def part_a():

    instr_a = defaultdict(int)
    for I, N in enumerate(instr):
        instr_a[I]  = N
    instr_a[1] = 12
    instr_a[2] = 2
    idx = 0

    while (opcode:=instr_a[idx]) != 99:
        idx_1 = instr_a[idx+1]
        idx_2 = instr_a[idx+2]
        idx_3 = instr_a[idx+3]

        if opcode == 1:
            instr_a[idx_3] = instr_a[idx_1] + instr_a[idx_2]
        else:
            instr_a[idx_3] = instr_a[idx_1] * instr_a[idx_2]
        idx += 4
    ans = instr_a[0]
    print(ans)
    puzzle.answer_a = ans

def part_b():
    for start_val in count():
        instr_a = defaultdict(int)
        for I, N in enumerate(instr):
            instr_a[I]  = N
        instr_a[1] = start_val//100
        instr_a[2] = start_val % 100
        idx = 0

        while (opcode:=instr_a[idx]) != 99:
            idx_1 = instr_a[idx+1]
            idx_2 = instr_a[idx+2]
            idx_3 = instr_a[idx+3]

            if opcode == 1:
                instr_a[idx_3] = instr_a[idx_1] + instr_a[idx_2]
            else:
                instr_a[idx_3] = instr_a[idx_1] * instr_a[idx_2]
            idx += 4
        if instr_a[0] == 19690720:
            break
    print(start_val)
    puzzle.answer_b = start_val

part_a()
part_b()