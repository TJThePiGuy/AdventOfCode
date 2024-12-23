from aocd.models import Puzzle

puzzle = Puzzle(day = 20, year = 2024)

data = puzzle.input_data

grid = data.split('\n')
H = len(grid)
W = len(grid[0])

def in_bounds(x, y):
    return 0<=x<W and 0<=y<H

walls = set()
sx = sy = -1
ex = ey = -1

for y, line in enumerate(grid):
    for x, chr in enumerate(line):
        if chr == '#':
            walls.add((x,y))
        elif chr == 'S':
            sx = x
            sy = y
        elif chr == 'E':
            ex = x
            ey = y

dist:dict[tuple[int,int],int] = dict()
to_check = {(ex,ey)}
dirs = {(-1,0),(1,0),(0,-1),(0,1)}

d = 0
while len(to_check) > 0:
    next_check = set()
    for x,y in to_check:
        if (x,y) in dist:
            continue
        dist[(x,y)] = d
        for dx,dy in dirs:
            next_x = x+dx
            next_y = y+dy
            if not (in_bounds(next_x, next_y)) or (next_x, next_y) in walls:
                continue
            next_check.add((next_x, next_y))
    to_check = next_check.copy()
    d += 1

def part_a():
    total = 0
    for x,y in dist.keys():
        for dx,dy in dirs:
            next_x = x+2*dx
            next_y = y+2*dy
            if not (in_bounds(next_x, next_y)) or (next_x, next_y) in walls:
                continue
            if dist[(x,y)] - dist[(next_x, next_y)] -1 >= 100:
                total += 1
    print(total)
    puzzle.answer_a = total

cheat_dirs = dict()
cheat_dirs[1] = dirs

for n in range(2,21):
    new_dirs = set()
    for x,y in cheat_dirs[n-1]:
        for dx,dy in dirs:
            if abs(x+dx) + abs(y+dy) == n:
                new_dirs.add((x+dx, y+dy))
    cheat_dirs[n] = new_dirs

def part_b():
    total = 0
    for x,y in dist.keys():
        for d in range(1,21):
            D = cheat_dirs[d]
            for dx,dy in D:
                next_x = x+dx
                next_y = y+dy
                if not (in_bounds(next_x, next_y)) or (next_x, next_y) in walls:
                    continue
                if dist[(x,y)] - dist[(next_x, next_y)] - d >= 100:
                    total += 1
    print(total)
    puzzle.answer_b = total


part_a()
part_b()