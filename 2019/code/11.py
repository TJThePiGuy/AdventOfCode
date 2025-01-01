from aocd.models import Puzzle
from intcode import IntCodeComputer
from collections import defaultdict

puzzle = Puzzle(year = 2019, day = 11)

data = puzzle.input_data

instr = [int(i) for i in data.split(',')]

dirs = [(0,1),(1,0),(0,-1),(-1,0)]

def part_a():
    computer = IntCodeComputer(instr, print_out=False, input_console=False, input_arr=[0])
    dir = 0
    x = y = 0
    colors:dict[tuple[int,int],int] = defaultdict(int)
    painted = set()
    computer.compute()
    while(not(computer.finished)):
        painted.add((x,y))

        turn = -1 if computer.output_arr.pop() == 0 else 1
        next_col = computer.output_arr.pop()

        colors[(x,y)] = next_col
        dir += turn
        dir %= 4

        dx,dy = dirs[dir]
        x += dx
        y += dy
        
        computer.add_input(colors[(x,y)])
        computer.compute()
    print(len(painted))
    puzzle.answer_a = len(painted)

def part_b():
    computer = IntCodeComputer(instr, print_out=False, input_console=False, input_arr=[1])
    dir = 0
    x = y = 0
    colors:dict[tuple[int,int],int] = defaultdict(int)
    painted = set()
    computer.compute()
    while(not(computer.finished)):
        painted.add((x,y))

        turn = -1 if computer.output_arr.pop() == 0 else 1
        next_col = computer.output_arr.pop()

        colors[(x,y)] = next_col
        dir += turn
        dir %= 4

        dx,dy = dirs[dir]
        x += dx
        y += dy
        
        computer.add_input(colors[(x,y)])
        computer.compute()
    min_x = min(i[0] for i in colors.keys())
    min_y = min(i[1] for i in colors.keys())
    max_x = max(i[0] for i in colors.keys())
    max_y = max(i[1] for i in colors.keys())
    for y in range(max_y, min_y-1, -1):
        for x in range(min_x, max_x+1):
            print(' ' if colors[(x,y)] == 0 else '#', end='')
        print()
    puzzle.answer_b = 'ZRZPKEZR'

part_a()
part_b()