from aocd.models import Puzzle
import regex as re
import itertools as it
import functools as ft

puzzle = Puzzle(day = 14, year = 2024)

data = puzzle.input_data

def part_a():
    W = 101
    H = 103

    quads = [0,0, 0,0]

    for line in data.split('\n'):
        match = re.findall('-?\\d+', line)
        px,py,vx,vy = (int(i) for i in match)
        px += 100*vx
        px %= W
        py += 100*vy
        py %= H
        if px == W//2 or py == H//2:
            continue
        left = (px < W//2)
        up = (py < H//2)
        quads[left+2*up] += 1
    total = ft.reduce(lambda x,y: x*y,quads)
    print(total)
    puzzle.answer_a = total 

def part_b():
    W = 101
    H = 103

    robots = []

    for line in data.split('\n'):
        match = re.findall('-?\\d+', line)
        robots.append([int(i) for i in match])
    for ct in it.count(1):
        pos = set()
        for robot in robots:
            robot[0] += robot[2]
            robot[1] += robot[3]
            robot[0] %= W
            robot[1] %= H
            pos.add((robot[0],robot[1]))
        if(ct % 1000 == 0):
            print(ct)
        if len(robots) ==  len(pos):
            break
    puzzle.answer_b = ct
    print(ct)
    # for y in range(H):
        
    #     for x in range(W):
    #         if (x,y) in pos:
    #             print('#', end='')
    #         else:
    #             print(' ',end='')
    #     print()
part_a()
part_b()