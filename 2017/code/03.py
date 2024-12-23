from aocd.models import Puzzle
from numpy import sqrt

puzzle:Puzzle = Puzzle(day = 3, year = 2017)

def coords(data:int) -> tuple[int,int]:
    sqrt_n = int(sqrt(data))
    n = sqrt_n**2
    X = Y = 0

    if(n == data):
        if(n%2 == 0):
            X = -(sqrt_n//2-1)
            Y = sqrt_n//2
        else:
            X = sqrt_n//2
            Y = -(sqrt_n//2)
        return((X,Y))

    if(n % 2 == 0):
        if(n + sqrt(n) + 1 >= data):
            X = -sqrt_n//2
            midpoint = (n+1 + n+sqrt_n+1)//2
            Y = midpoint - data
        else:
            Y = -sqrt_n//2
            midpoint = (n+sqrt_n+1+n+2*sqrt_n+1)//2
            X = data - midpoint
    else:
        if(n + sqrt_n + 1 > data):
            X = sqrt_n//2 + 1
            midpoint = (n+1 + n+sqrt_n+1)//2
            Y = data - midpoint
        else:
            Y = sqrt_n//2+1
            midpoint = (n+sqrt_n+1+n+2*sqrt_n+2)//2
            X = midpoint - data
    return((X,Y,midpoint))

def part_a():
    # data = 24
    data = int(puzzle.input_data)
    sqrt_n = int(sqrt(data))
    n = sqrt_n**2
    if(n == data):
        final = sqrt_n-1
        puzzle.answer_a = final
        print(final)
        return
    
    dx = dy = 0
    if(n % 2 == 0):
        if(n + sqrt(n) + 1 >= data):
            dx = sqrt_n//2
            midpoint = (n+1 + n+sqrt_n+1)//2
            dy = abs(midpoint - data)
        else:
            dy = sqrt_n//2
            midpoint = (n+sqrt_n+1+n+2*sqrt_n+1)//2
            dx = abs(midpoint - data)
    else:
        if(n + sqrt(n) + 1 >= data):
            dx = sqrt_n//2 + 1
            midpoint = (n+1 + n+sqrt_n+1)//2
            dy = abs(midpoint - data)
        else:
            dy = sqrt_n//2+1
            midpoint = (n+sqrt_n+1+n+2*sqrt_n+1)//2
            dx = abs(midpoint - data)

    dist = dx+dy
    print(dx, dy, dist)
    puzzle.answer_a = dist

def part_b():

    data = int(puzzle.input_data)
    # data = 800
    n = 2

    dict_val:dict[tuple[int,int],int] = dict()

    dict_val[(0,0)] = 1

    while True:
        pos = coords(n)
        x = pos[0]
        y = pos[1]
        running_tot = 0
        for dx in [-1,0,1]:
            for dy in [-1,0,1]:
                running_tot += dict_val.get((x+dx,y+dy),0)

        if running_tot >= data:
            largest = running_tot
            break
        dict_val[(x,y)] = running_tot
        print(n, running_tot)
        n = n+1


    print(largest)
    puzzle.answer_b = largest

part_a()
part_b()