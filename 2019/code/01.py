from aocd.models import Puzzle

puzzle = Puzzle(year = 2019, day = 1)

data = puzzle.input_data
nums = [int(i) for i in data.splitlines()]

def part_a():
    total = 0
    for n in nums:
        total += (n//3)-2
    print(total)
    puzzle.answer_a = total

def part_b():
    total = 0
    for num in nums:
        while num > 0:
            total += (num:= max(num//3 - 2,0))
    print(total)
    puzzle.answer_b=total

part_a()
part_b()