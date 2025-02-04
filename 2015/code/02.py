from aocd.models import Puzzle

puzzle = Puzzle(day = 2, year = 2015)

def part_a():
    dims = [tuple(int(i) for i in _.split('x')) for _ in puzzle.input_data.split('\n')]
    total = 0
    for dim in dims:
        prod1 = dim[0]*dim[1]
        prod2 = dim[0]*dim[2]
        prod3 = dim[1]*dim[2]
        total += 2*(prod1 + prod2 + prod3) + min(prod1, prod2, prod3)
    print(total)
    puzzle.answer_a = total
    pass

def part_b():
    dims = [tuple(int(i) for i in _.split('x')) for _ in puzzle.input_data.split('\n')]
    total = 0
    for dim in dims:
        sum1 = dim[0]+dim[1]
        sum2 = dim[0]+dim[2]
        sum3 = dim[1]+dim[2]

        total += 2*(min(sum1, sum2, sum3)) + dim[0]*dim[1]*dim[2]
    print(total)
    puzzle.answer_b = total
    pass
part_a()
part_b()