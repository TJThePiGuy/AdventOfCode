from aocd.models import Puzzle
from queue import PriorityQueue

puzzle = Puzzle(day = 16, year = 2024)

data = puzzle.input_data
maze = data.split('\n')
walls = set()
s_x = s_y = e_x = e_y = 0

space_count = 0
space_idx:dict[tuple[int,int],int] = dict()

for y,line in enumerate(maze):
    for x, chr in enumerate(line):
        if chr == '#':
            walls.add((x,y))
            continue
        elif chr == 'S':
            s_x = x
            s_y = y
        elif chr == 'E':
            e_x = x
            e_y = y
            
        space_idx[(x,y)] = space_count
        space_count += 1

dir_dict = {0:(-1,0),1:(0,1),2:(1,0),3:(0,-1)}

def part_a():
    costs:dict[tuple[int,int,int],int] = dict()

    to_check = PriorityQueue()
    to_check.put((0, (s_x, s_y, 2)))

    min_cost = -1

    while not to_check.empty():
        COST, (x, y, DIR) = to_check.get()
        
        if (x, y, DIR) in costs and costs[(x, y, DIR)] <= COST:
            continue
        costs[(x, y, DIR)] = COST

        if x == e_x and y == e_y:
            min_cost = COST
            break

        dx,dy = dir_dict[DIR]

        if(x+dx, y+dy) not in walls:
            to_check.put((COST+1, (x+dx, y+dy, DIR)))
            
        to_check.put((COST+1000, (x, y, (DIR+1)%4)))
        to_check.put((COST+1000, (x, y, (DIR-1)%4)))
    print(min_cost)
    puzzle.answer_a = min_cost
    return(min_cost)

def part_b(max_cost):
    costs:dict[tuple[int,int,int],int] = dict()
    to_check = PriorityQueue()
    to_check.put((0, (s_x, s_y, 2, 0)))

    total_path = 0
    count = 0

    while not to_check.empty():
        COST, (x, y, DIR, PATH) = to_check.get()
        if (x, y, DIR) in costs and costs[(x, y, DIR)] < COST:
            continue
        if COST > max_cost:
            continue
        count += 1
        costs[(x, y, DIR)] = COST

        PATH |= 2<<space_idx[(x,y)]

        if x == e_x and y == e_y and COST == max_cost:
            total_path |= PATH
            continue

        dx,dy = dir_dict[DIR]

        if(x+dx, y+dy) not in walls:
            to_check.put((COST+1, (x+dx, y+dy, DIR, PATH)))
        to_check.put((COST+1000, (x, y, (DIR+1)%4, PATH)))
        to_check.put((COST+1000, (x, y, (DIR-1)%4, PATH)))
    T = sum(int(i) for i in bin(total_path)[2:])
    print(T)
    puzzle.answer_b = T

M = part_a()
part_b(M)