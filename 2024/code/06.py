from aocd.models import Puzzle

puzzle = Puzzle(day = 6, year = 2024)

def part_a():
    data = puzzle.input_data
    hashes = set()
    lines = data.split('\n')
    H = len(lines)
    X = Y = -1
    dir_dict = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
    for y, line in enumerate(lines):
        W = len(line)
        for x, char in enumerate(line):
            if char == '^':
                X = x
                Y = y
            elif char == '#':
                hashes.add((x,y))
    locs = set()
    dir = 3
    while((X > -1) and (X < W) and (Y > -1) and (Y < H)):
        # print(X,Y)
        locs.add((X,Y))
        d = dir_dict[dir]
        dx,dy = d
        next_X = X + dx
        next_Y = Y + dy
        while (next_X,next_Y) in hashes:
            dir -= 1
            dir %= 4
            d = dir_dict[dir]
            dx,dy = d
            next_X = X + dx
            next_Y = Y + dy
        X = next_X
        Y = next_Y
    
    puzzle.answer_a = (len(locs))
    print(len(locs))
    return(locs)

        
def part_b(open:set):
    data = puzzle.input_data
    hashes = set()
    lines = data.split('\n')
    H = len(lines)
    START_X = START_Y = -1
    dir_dict = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}
    for y, line in enumerate(lines):
        W = len(line)
        for x, char in enumerate(line):
            if char == '^':
                START_X = x
                START_Y = y
            elif char == '#':
                hashes.add((x,y))
    loops  = 0
    open.remove((START_X, START_Y))
    for NEW_POINT in open:
        hashes.add(NEW_POINT)
        X = START_X
        Y = START_Y
        locs = set()
        dir = 3
        loop = False
        while((X > -1) and (X < W) and (Y > -1) and (Y < H)):
            if(X,Y,dir) in locs:
                loop = True
                break
            locs.add((X,Y,dir))
            d = dir_dict[dir]
            dx,dy = d
            next_X = X + dx
            next_Y = Y + dy
            while (next_X,next_Y) in hashes:
                dir -= 1
                dir %= 4
                d = dir_dict[dir]
                dx,dy = d
                next_X = X + dx
                next_Y = Y + dy
            X = next_X
            Y = next_Y
        if(loop):
            loops += 1
        hashes.remove(NEW_POINT)
        # print(f'{I} of {len(open)}')
    print(loops)
    puzzle.answer_b = (loops)

        

L = part_a()

part_b(L)