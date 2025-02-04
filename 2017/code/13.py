from aocd.models import Puzzle
from math import lcm

puzzle:Puzzle = Puzzle(day = 13, year = 2017)

def part_a():
    data = puzzle.input_data
    lines = [ind.split(':') for ind in data.split('\n')]
    depth_dict:dict[int,int] = dict()
    for line in lines:
        depth_dict[int(line[0])] = int(line[1])
    severity = 0
    for step in range(max(depth_dict.keys())+1):
        height = depth_dict.get(step, -5)
        if height == -5:
            continue
        if height == 1:
            severity += step
            continue
        scanner_pos = step % (2*(height-1))
        if scanner_pos == 0:
            severity += step * height
    puzzle.answer_a = severity
    print(severity)

def part_b():
    data = puzzle.input_data
    lines = [ind.split(':') for ind in data.split('\n')]
    depth_dict:dict[int,int] = dict()
    for line in lines:
        depth_dict[int(line[0])] = 2*(int(line[1])-1)

    sieve = [True] * lcm(*depth_dict.values())

    depth_dict = sorted(depth_dict.items(), key = lambda item: -item[1])

    for item in depth_dict:
        index, height = item
        for idx in range((-index) % height, len(sieve), height):
            sieve[idx] = False
        print(index, height)

    delay = sieve.index(True)
    puzzle.answer_b = delay
    print(delay)

part_a()
part_b()