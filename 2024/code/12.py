from aocd.models import Puzzle
import itertools as it

puzzle = Puzzle(day = 12, year = 2024)

data = puzzle.input_data
lines = data.split('\n')
W = len(lines[0])
H = len(lines)

def in_bounds(x,y,w,h):
    return (0<=x<w) and (0<=y<h)

def part_a():
    indices:dict[str,set[tuple[int,int]]] = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in indices:
                indices[c] = set()
            indices[c].add((x,y))
    total = 0
    for plant, spots in indices.items():
        area = len(spots)
        checked = set()
        for spot in spots:
            if spot in checked:
                continue
            x, y = spot
            to_check = {(x,y)}
            area = 0
            perimeter = 0
            while(len(to_check)) != 0:
                x,y = to_check.pop()
                if(x,y) in checked:
                    continue
                checked.add((x,y))
                area += 1
                for dx,dy in {(-1,0),(1,0),(0,1),(0,-1)}:
                    next_x = x+dx
                    next_y = y+dy
                    if (not in_bounds(next_x, next_y, W, H)):
                        perimeter += 1
                        continue
                    if lines[next_y][next_x] != plant:
                        perimeter += 1
                    elif (next_x, next_y) not in checked:
                        to_check.add((next_x, next_y))
            total += area * perimeter

    puzzle.answer_a = total
    print(total)

def part_b():
    indices:dict[str,set[tuple[int,int]]] = dict()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c not in indices:
                indices[c] = set()
            indices[c].add((x,y))
    total = 0
    for plant, spots in indices.items():
        area = len(spots)
        checked = set()
        for spot in spots:
            if spot in checked:
                continue
            x, y = spot
            to_check = {(x,y)}
            area = 0
            sides = 0
            left_edges:dict[int,list[int]] = dict()
            right_edges:dict[int,list[int]] = dict()

            while(len(to_check)) != 0:
                x,y = to_check.pop()
                if(x,y) in checked:
                    continue
                checked.add((x,y))
                area += 1
                for dy in [-1,1]:
                    next_y = y+dy
                    if next_y < 0 or next_y >= H:
                        continue
                    if lines[next_y][x] == plant and (x, next_y) not in checked:
                        to_check.add((x, next_y))

                next_x = x-1
                if next_x < 0 or next_x >= W or lines[y][next_x] != plant:
                    if x not in left_edges:
                        left_edges[x] = []
                    left_edges[x].append(y)

                elif (next_x, y) not in checked:
                    to_check.add((next_x, y))

                next_x = x+1
                if next_x < 0 or next_x >= W or lines[y][next_x] != plant:
                    if x not in right_edges:
                        right_edges[x] = []
                    right_edges[x].append(y)
                elif (next_x, y) not in checked:
                    to_check.add((next_x, y))

            for val in left_edges.values():
                val.sort()
                for _ in it.groupby(enumerate(val), lambda X : X[0]-X[1]):
                    sides += 1

            for val in right_edges.values():
                val.sort()
                for _ in it.groupby(enumerate(val), lambda X : X[0]-X[1]):
                    sides += 1
            total += area * sides * 2
    print(total)
    puzzle.answer_b = total

part_a()
part_b()