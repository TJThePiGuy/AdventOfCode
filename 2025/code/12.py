from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(year = 2025, day = 12)

data = puzzle.input_data

def part_a():
    groups = data.split('\n\n')
    shapes:dict[int, set[tuple[int,int]]] = defaultdict(set)

    for i, shape in enumerate(groups[:-1]):
        for y, line in enumerate(shape.split('\n')[1:]):
            for x, chr in enumerate(line):
                if chr == '#':
                    shapes[i].add((x,y))
    
    goals = [line.split(' ') for line in groups[-1].split('\n')]
    possible = 0
    for goal in goals:
        w, h = tuple(int(i) for i in goal[0][:-1].split('x'))
        counts = tuple(int(i) for i in goal[1:])
        area = sum(len(s) * c for s,c in zip(shapes.values(), counts))
        if area <= w*h:
            possible += 1
    print(possible)

part_a()