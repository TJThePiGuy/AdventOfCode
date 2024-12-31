from aocd.models import Puzzle
from itertools import product

puzzle = Puzzle(year = 2019, day = 3)

data = puzzle.input_data

dirs = [line.split(',') for line in data.splitlines()]

def part_a():
    lines:list[list[set]] = [[set(), set()],[set(), set()]]

    for idx in range(2):
        DIRS = dirs[idx]
        x,y = 0,0
        for dir in DIRS:
            dist = int(dir[1:])
            if dir[0] == 'U':
                lines[idx][0].add((x, y, y+dist))
                y += dist
            elif dir[0] == 'D':
                lines[idx][0].add((x,y-dist, y))
                y -= dist
            elif dir[0] == 'L':
                lines[idx][1].add((y, x-dist, x))
                x -= dist
            else:
                lines[idx][1].add((y, x, x+dist))
                x += dist
    manhattan = -1
    for (ax, ay1, ay2), (by, bx1, bx2) in product(lines[0][0], lines[1][1]):
        if bx1 <= ax <= bx2 and ay1 <= by <= ay2:
            dist = abs(ax) + abs(by)
            if manhattan < 0 or dist < manhattan:
                manhattan = dist
    for (ax, ay1, ay2), (by, bx1, bx2) in product(lines[1][0], lines[0][1]):
        if bx1 <= ax <= bx2 and ay1 <= by <= ay2:
            dist = abs(ax) + abs(by)
            if manhattan < 0 or dist < manhattan:
                manhattan = dist
    print(manhattan)
    puzzle.answer_a = manhattan

def part_b():
    lines:list[list[set]] = [[set(), set()],[set(), set()]]

    for idx in range(2):
        DIRS = dirs[idx]
        x,y = 0,0
        total_dist = 0
        for dir in DIRS:
            dist = int(dir[1:])
            if dir[0] == 'U':
                lines[idx][0].add((x, y, y+dist, total_dist, True))
                y += dist
            elif dir[0] == 'D':
                lines[idx][0].add((x,y-dist, y, total_dist, False))
                y -= dist
            elif dir[0] == 'L':
                lines[idx][1].add((y, x-dist, x, total_dist, False))
                x -= dist
            else:
                lines[idx][1].add((y, x, x+dist, total_dist, True))
                x += dist
            total_dist += dist
    shortest_dist = -1
    for (ax, ay1, ay2, ad, ai), (by, bx1, bx2, bd, bi) in product(lines[0][0], lines[1][1]):
        if bx1 <= ax <= bx2 and ay1 <= by <= ay2:
            dist = ad + (by-ay1 if ai else ay2-by) + bd + (ax-bx1 if bi else bx2-ax)
            if shortest_dist < 0 or dist < shortest_dist:
                shortest_dist = dist
    for (ax, ay1, ay2, ad, ai), (by, bx1, bx2, bd, bi) in product(lines[1][0], lines[0][1]):
        if bx1 <= ax <= bx2 and ay1 <= by <= ay2:
            dist = ad + (by-ay1 if ai else ay2-by) + bd + (ax-bx1 if bi else bx2-ax)
            if shortest_dist < 0 or dist < shortest_dist:
                shortest_dist = dist
    print(shortest_dist)
    puzzle.answer_b = shortest_dist


part_a()

part_b()  