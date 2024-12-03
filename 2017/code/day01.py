from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 1, year = 2017)


def part_a():
    data = puzzle.input_data
    L = len(data)
    total = 0
    for idx in range(L):
        if(data[idx] == data[(idx+1)%L]):
            total += int(data[idx])
    puzzle.answer_a = total
    print(total)

def part_b():
    data = puzzle.input_data
    L = len(data)
    total = 0
    for idx in range(L):
        if(data[idx] == data[(idx + L//2) % L]):
            total += int(data[idx])
    puzzle.answer_b = total
    print(total)

part_a()
part_b()