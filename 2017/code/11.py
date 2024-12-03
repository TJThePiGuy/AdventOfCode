from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 11, year = 2017)

def part_a():
    data = puzzle.input_data
    n = ne = 0
    dirs = data.split(',')
    for dir in dirs:
        if dir == 'n':
            n += 1  
        elif dir == 's':
            n -= 1
        elif dir == 'ne':
            ne += 1
        elif dir == 'sw':
            ne -= 1
        elif dir == 'nw':
            ne -= 1
            n += 1
        else:
            ne += 1
            n -= 1
    ans = abs(n) + abs(ne)
    puzzle.answer_a = ans
    print(ans)

def part_b():
    data = puzzle.input_data
    n = ne = 0
    dirs = data.split(',')
    dist = 0
    for dir in dirs:
        if dir == 'n':
            n += 1  
        elif dir == 's':
            n -= 1
        elif dir == 'ne':
            ne += 1
        elif dir == 'sw':
            ne -= 1
        elif dir == 'nw':
            ne -= 1
            n += 1
        else:
            ne += 1
            n -= 1
        new_dist = abs(n) + abs(ne)
        dist = max(dist, new_dist)
    ans = dist
    puzzle.answer_b = ans
    print(ans)


part_a()

part_b()