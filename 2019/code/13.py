from aocd.models import Puzzle
from intcode import IntCodeComputer
from collections import defaultdict

puzzle = Puzzle(year = 2019, day = 13)

data = puzzle.input_data

instr = [int(i) for i in data.split(',')]

def sign(inp):
    if inp == 0:
        return 0
    return -1 if inp < 0 else 1

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
    grid:dict[tuple[int,int],int] = defaultdict(int)
    prev_x = 17
    while has_block:
        pad_x = 0
        ball_x = 0
        score = 0
        while len(computer.output_arr) > 0:
            id = computer.output_arr.pop()
            y = computer.output_arr.pop()
            x = computer.output_arr.pop()
            grid[(x,y)] = id
            if x == -1 and y == 0:
                score = id
            if id == 3:
                pad_x = x
            elif id == 4:
                ball_x = x
        dir = ball_x - prev_x
        prev_x = ball_x
        min_x = min(i[0] for i in grid.keys())
        min_y = min(i[1] for i in grid.keys())
        max_x = max(i[0] for i in grid.keys())
        max_y = max(i[1] for i in grid.keys())

        # for y in range(min_y, max_y+1):
        #     for x in range(min_x, max_x+1):
        #         id = grid[(x,y)]
        #         if id == 1:
        #             print('#',end='')
        #         elif id == 2:
        #             print('X',end='')
        #         elif id == 3:
        #             print('-',end='')
        #         elif id == 4:
        #             print('O',end='')
        #         else:
        #             print('.',end='')
        #     print()
        # print(ball_x, dir, pad_x)
        # input()
        computer.add_input(0)
        computer.compute()
        has_block = 2 in grid.values()
    ans = grid[(-1,0)]
    print(ans)
    puzzle.answer_b = ans
part_a()
part_b()