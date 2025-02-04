from aocd.models import Puzzle
import itertools as it

puzzle = Puzzle(day = 8, year = 2024)

def in_bounds(x,y,w,h):
    return (0<=x<w) and (0<=y<h)

def part_a():
    data = puzzle.input_data
    antennas:dict[str,tuple[int,int]] = dict()
    H = len(data.split('\n'))
    W = len(data.split('\n')[0])
    for y,line in enumerate(data.split('\n')):
        for x,chr in enumerate(line):
            if chr == '.':
                continue
            if chr not in antennas:
                antennas[chr] = set()
            antennas[chr].add((x,y))
    antis = set()
    for k,sets in antennas.items():
        for p1, p2 in it.combinations(sets, r=2):
            x1,y1 = p1
            x2,y2 = p2
            dx = x2-x1
            dy = y2-y1
            if in_bounds(x2+dx,y2+dy,W,H):
                antis.add((x2+dx,y2+dy))
            if in_bounds(x1-dx,y1-dy,W,H):
                antis.add((x1-dx,y1-dy))
    print(len(antis))
    puzzle.answer_a = len(antis)


def part_b():
    data = puzzle.input_data
    antennas:dict[str,tuple[int,int]] = dict()
    H = len(data.split('\n'))
    W = len(data.split('\n')[0])
    antis = set()
    for y,line in enumerate(data.split('\n')):
        for x,chr in enumerate(line):
            if chr == '.':
                continue
            if chr not in antennas:
                antennas[chr] = set()
            antennas[chr].add((x,y))
            antis.add((x,y))
    for k,sets in antennas.items():
        for p1, p2 in it.combinations(sets, r=2):
            x1,y1 = p1
            x2,y2 = p2
            dx = x2-x1
            dy = y2-y1
            next_x = x1 - dx
            next_y = y1 - dy
            while in_bounds(next_x, next_y,W,H):
                antis.add((next_x, next_y))
                next_x -= dx
                next_y -= dy
            next_x = x2 + dx
            next_y = y2 + dy

            while in_bounds(next_x, next_y, W,H):
                antis.add((next_x, next_y))
                next_x += dx
                next_y += dy
    puzzle.answer_b = len(antis)
    print(len(antis))
part_a()
part_b()