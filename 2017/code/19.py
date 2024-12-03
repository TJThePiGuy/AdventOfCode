from aocd.models import Puzzle

puzzle = Puzzle(day=19, year = 2017)

def part_a():
    data:str = puzzle.input_data
    lines:list[str] = data.split('\n')

    y = 0
    x = lines[0].index("|")

    dirs:dict[int,tuple[int,int]] = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

    dir = 0

    dx = 0
    dy = 1

    letters_seen = ""

    while(lines[y][x] != " "):
        if lines[y][x].isalpha():
            letters_seen = letters_seen + lines[y][x]
        
        if(lines[y][x] == "+"):
            if(dir % 2 == 0):
                if(lines[y][x+1] == "-"):
                    dir = 1
                else:
                    dir = 3
            else:
                if(lines[y+1][x] == '|'):
                    dir = 0
                else:
                    dir = 2
        (dx,dy) = dirs[dir]

        x+= dx
        y+= dy
    puzzle.answer_a = letters_seen
    print(letters_seen)


def part_b():
    data:str = puzzle.input_data
    lines:list[str] = data.split('\n')

    y = 0
    x = lines[0].index("|")

    dirs:dict[int,tuple[int,int]] = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}

    dir = 0

    dx = 0
    dy = 1

    steps = 0

    while(lines[y][x] != " "):
        steps += 1
        if(lines[y][x] == "+"):
            if(dir % 2 == 0):
                if(lines[y][x+1] == "-"):
                    dir = 1
                else:
                    dir = 3
            else:
                if(lines[y+1][x] == '|'):
                    dir = 0
                else:
                    dir = 2
        (dx,dy) = dirs[dir]

        x+= dx
        y+= dy
    puzzle.answer_b = steps
    print(steps)

part_a()

part_b()