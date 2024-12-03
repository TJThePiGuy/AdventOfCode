from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 5, year = 2017)

def part_a():
    dists = [int(i) for i in puzzle.input_data.split("\n")]
    pos = 0
    L = len(dists)
    n = 0
    while(pos < L):
        dx = dists[pos]
        dists[pos] += 1
        pos += dx

        n = n+1
    puzzle.answer_a = n
    print(n)

def part_b():
    dists = [int(i) for i in puzzle.input_data.split("\n")]
    pos = 0
    L = len(dists)
    n = 0
    while(pos < L):
        dx = dists[pos]
        if(dx >= 3):
            dists[pos] -= 1
        else:
            dists[pos] += 1
        pos += dx
        n = n+1
    puzzle.answer_b = n
    print(n)

part_a()
part_b()