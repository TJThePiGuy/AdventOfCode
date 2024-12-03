from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 2, year = 2017)


def part_a():
    data = puzzle.input_data
    lines = [set(int(_) for _ in line.split()) for line in data.split("\n")]
    total = 0
    for line in lines:
        total += max(line) - min(line)
    print(total)
    puzzle.answer_a = total

def part_b():
    data = puzzle.input_data
    lines = [[int(_) for _ in line.split()] for line in data.split("\n")]
    total = 0
    for line in lines:
        for idx in range(len(line)):
            x = line[idx]
            for jdx in range(idx+1, len(line)):
                y = line[jdx]
                if(x%y==0) or (y%x==0):
                    total += max(x//y, y//x)

    print(total)
    puzzle.answer_b = total

part_a()
part_b()