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

def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def find_min_x(num, rem):
    prod = 1
    for n in num:
        prod *= n

    result = 0
    for i in range(len(num)):
        prod_i = prod // num[i]
        _, inv_i, _ = gcd_extended(prod_i, num[i])
        result += rem[i] * prod_i * inv_i

    return result % prod

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