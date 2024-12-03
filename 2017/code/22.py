from aocd.models import Puzzle
from tqdm import tqdm

puzzle = Puzzle(day = 22, year = 2017)

def part_a():
    data = puzzle.input_data
    # data = '..#\n#..\n...'
    infected:set[tuple[int,int]] = set()
    
    center_y = len(data.split('\n'))//2
    center_x = len(data.split('\n')[0])//2
    for y, line in enumerate(data.split('\n')):
        for x, chr in enumerate(line):
            if(chr == '#'):
                infected.add((x,y))
    x = center_x
    y = center_y
    dirs:dict[int,tuple[int,int]] = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
    dir = 3
    infect = 0

    for burst in range(10000):
        if((x,y) in infected):
            dir += 1
            infected.remove((x,y))
        else:
            dir -= 1
            infected.add((x,y))
            infect += 1
        dir %= 4
        dx, dy = dirs[dir]
        x += dx
        y += dy
    puzzle.answer_a = infect
    print(infect)

def part_b():
    data = puzzle.input_data
    # data = '..#\n#..\n...'
    states:dict[tuple[int,int],int] = dict()
    
    center_y = len(data.split('\n'))//2
    center_x = len(data.split('\n')[0])//2
    for y, line in enumerate(data.split('\n')):
        for x, chr in enumerate(line):
            if(chr == '#'):
                states[(x,y)] = 2
    
    x = center_x
    y = center_y
    dirs:dict[int,tuple[int,int]] = {0:(1,0),1:(0,1),2:(-1,0),3:(0,-1)}
    dir = 3
    infect = 0

    for burst in tqdm(range(10_000_000)):
        state = states.get((x,y),0)
        if(state == 1):
            infect += 1
        dir += (state-1)
        states[(x,y)] = (state+1)%4

        dir %= 4
        dx, dy = dirs[dir]
        x += dx
        y += dy
    puzzle.answer_b = infect
    print(infect)
    
part_a()
part_b()