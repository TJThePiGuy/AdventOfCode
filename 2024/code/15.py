from aocd.models import Puzzle

puzzle = Puzzle(year = 2024, day = 15)

data = puzzle.input_data

grid = data.split('\n\n')[0].split('\n')
H = len(grid)
moves = ''.join([i for i in data.split('\n\n')[1] if i!='\n'])

walls_a:set[tuple[int,int]] = set()
boxes_a:set[tuple[int,int]] = set()

walls_b = walls_a.copy()
boxes_b = boxes_a.copy()

start_x_a = start_y_a = -1
start_x_b = start_y_b = -1

for y,line in enumerate(grid):
    W = len(line)
    for x,chr in enumerate(line):
        if chr == '#':
            walls_a.add((x,y))
            walls_b.add((2*x, y))
            walls_b.add((2*x+1,y))
        elif chr == 'O':
            boxes_a.add((x,y))
            boxes_b.add((2*x,y))
        elif chr == '@':
            start_x_a = x
            start_y_a = y
            start_x_b = 2*x
            start_y_b = y

print(start_x_a, start_y_a, start_x_b, start_y_b)

def can_move_a(px,py,dx,dy):
    if (px+dx,py+dy) in walls_a:
        return False
    if (px+dx,py+dy) in boxes_a:
        return can_move_a(px+dx, py+dy, dx, dy)
    return True

def move_a(px,py,dx,dy):
    if (px+dx,py+dy) in boxes_a:
        boxes_a.remove((px+dx,py+dy))
        boxes_a.add(move_a(px+dx,py+dy,dx,dy))
    return (px+dx,py+dy)

def can_move_b(px,py,dx,dy):
    next_x = px+dx
    next_y = py+dy
    if (next_x, next_y) in walls_b:
        return False
    if dx == 0:
        if (next_x, next_y) in boxes_b:
            return can_move_b(next_x, next_y, dx, dy) and can_move_b(next_x+1, next_y, dx, dy)
        elif (next_x-1, next_y) in boxes_b:
            return can_move_b(next_x, next_y, dx, dy) and can_move_b(next_x-1, next_y, dx, dy)
    if dx == 1 and (next_x, next_y) in boxes_b:
            return can_move_b(next_x+1, next_y, dx, dy)
    if dx == -1 and (next_x-1, next_y) in boxes_b:
            return can_move_b(next_x-1, next_y, dx, dy)
    return True

def move_b(px,py,dx,dy):
    next_x = px+dx
    next_y = py+dy
    if dx == 0:
        if (next_x, next_y) in boxes_b:
            boxes_b.remove((next_x, next_y))
            move_b(next_x+1, next_y, dx, dy)
            boxes_b.add(move_b(next_x, next_y, dx, dy))
        elif (next_x-1, next_y) in boxes_b:
            boxes_b.remove((next_x-1, next_y))
            move_b(next_x, next_y, dx, dy)
            boxes_b.add(move_b(next_x-1, next_y, dx, dy))
    if dx == 1:
        if (next_x, next_y) in boxes_b:
            boxes_b.remove((next_x, next_y))
            move_b(next_x+1, next_y, dx, dy)
            boxes_b.add((next_x+1, next_y))
    if dx == -1:
        if (next_x-1, next_y) in boxes_b:
            boxes_b.remove((next_x-1, next_y))
            move_b(next_x-1, next_y, dx, dy)
            boxes_b.add((next_x-2, next_y))
    return (next_x, next_y)

def print_a(pos_x, pos_y, pause = True):
    for y in range(H):
        for x in range(W):
            if (x,y) in walls_a:
                print('#',end='')
            elif (x,y) in boxes_a:
                print('O',end='')
            elif (x,y) == (pos_x, pos_y):
                print('@',end='')
            else:
                print(' ',end='')
        print()
    if pause:
        input()

def print_b(pos_x, pos_y, pause = True):
    for y in range(H):
        for x in range(2*W):
            if (x,y) in walls_b:
                print('#',end='')
            elif (x-1,y) in boxes_b:
                print(']', end='')
            elif (x,y) in boxes_b:
                print('[',end='')
            elif (x,y) == (pos_x, pos_y):
                print('@',end='')
            else:
                print(' ',end='')
        print()
    if pause:
        input()

dirs = {'<':(-1,0),'^':(0,-1),'>':(1,0),'v':(0,1)}

def part_a():
    pos_x = start_x_a
    pos_y = start_y_a
    for m in moves:
        dx,dy = dirs[m]
        if can_move_a(pos_x, pos_y, dx, dy):
            pos_x, pos_y = move_a(pos_x, pos_y, dx, dy)
    total = 0
    for x,y in boxes_a:
        total += y*100 + x
    print(total)
    puzzle.answer_a = total

def part_b():
    pos_x = start_x_b
    pos_y = start_y_b
    for m in moves:
        dx,dy = dirs[m]
        if can_move_b(pos_x, pos_y, dx, dy):
            pos_x, pos_y = move_b(pos_x, pos_y, dx, dy)
    total = 0
    for x1,y in boxes_b:
        total += 100*y + x1
    print(total)
    puzzle.answer_b = total

part_a()
part_b()