from aocd.models import Puzzle

puzzle = Puzzle(day = 10, year = 2024)

def in_bounds(x,y,w,h):
    return (0<=x<w) and (0<=y<h)

def part_a():
    data = puzzle.input_data
    heads:set[tuple[int,int]] = set()
    lines = data.split('\n')
    H = len(lines)
    for y,line in enumerate(lines):
        W = len(line)
        for x in range(W):
            if line[x] == '0':
                heads.add((x,y))
    dirs = set([(-1,0),(1,0),(0,1),(0,-1)])
    total = 0

    for head in heads:
        x,y = head
        to_check:set[tuple[int,int]] = {(x,y)}
        for next in range(1,10):
            next_check = set()
            for x,y in to_check:
                for dx,dy in dirs:
                    if not in_bounds(x+dx, y+dy, W, H):
                        continue
                    if lines[y+dy][x+dx] == str(next):
                        next_check.add((x+dx,y+dy))
            to_check = next_check
        total += len(to_check)
    print(total)
    puzzle.answer_a = total

    
def part_b():
    data = puzzle.input_data
    heads:set[tuple[int,int]] = set()
    lines = data.split('\n')
    H = len(lines)
    for y,line in enumerate(lines):
        W = len(line)
        for x in range(W):
            if line[x] == '0':
                heads.add((x,y))
    dirs = set([(-1,0),(1,0),(0,1),(0,-1)])
    total = 0
    for head in heads:
        x,y = head
        to_check:dict[tuple[int,int],int] = {(x,y):1}
        for next in range(1,10):
            next_check = dict()
            for pos, ct in to_check.items():
                x,y = pos
                for dx,dy in dirs:
                    next_x = x+dx
                    next_y = y+dy
                    if not in_bounds(next_x, next_y, W, H):
                        continue
                    if lines[next_y][next_x] == str(next):
                        if(next_x,next_y) not in next_check:
                            next_check[(next_x, next_y)] = 0
                        next_check[(next_x, next_y)] += ct
            to_check = next_check
        total += sum(to_check.values())
    print(total)
    puzzle.answer_b = total
part_a()
part_b()