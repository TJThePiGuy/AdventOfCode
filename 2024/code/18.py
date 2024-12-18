from aocd.models import Puzzle

puzzle = Puzzle(day = 18, year = 2024)

data = puzzle.input_data
walls_1024 = set()
walls_list = list()

for line in data.split('\n')[:1024]:
    walls_1024.add(tuple(int(i) for i in line.split(',')))

for line in data.split('\n'):
    walls_list.append(tuple(int(i) for i in line.split(',')))

def in_bounds(x, y):
    return 0<=x<71 and 0<=y<71

dirs = {(-1,0),(1,0),(0,-1),(0,1)}

def part_a():
    visited = set()
    dist = -1
    to_visit = {(0,0)}
    found = False
    while not found:
        next_visit = set()
        for x,y in to_visit:
            if (x,y) in visited:
                continue
            visited.add((x,y))
            if x == 70 and y == 70:
                found = True
            for dx,dy in dirs:
                next_x = x+dx
                next_y = y+dy
                if not (in_bounds(next_x, next_y)) or (next_x, next_y) in walls_1024 or (next_x, next_y) in visited:
                    continue
                next_visit.add((x+dx,y+dy))
        to_visit = next_visit.copy()
        dist += 1
    print(dist)
    puzzle.answer_a = dist

def part_b():
    checked_walls = walls_1024.copy()
    for (wx,wy) in walls_list[1024:]:
        checked_walls.add((wx,wy))
        found = False
        to_visit = {(0,0)}
        visited = set()
        while (not found) and len(to_visit) > 0:
            next_visit = set()
            for x,y in to_visit:
                if (x,y) in visited:
                    continue
                visited.add((x,y))
                if x == 70 and y == 70:
                    found = True
                    break
                for dx,dy in dirs:
                    next_x = x+dx
                    next_y = y+dy
                    if not (in_bounds(next_x, next_y)) or (next_x, next_y) in checked_walls or (next_x, next_y) in visited:
                        continue
                    next_visit.add((x+dx,y+dy))
            to_visit = next_visit.copy()
        if not found:
            break
    print(wx,wy)
    puzzle.answer_b = str(wx) + ',' + str(wy)

part_a()
part_b()