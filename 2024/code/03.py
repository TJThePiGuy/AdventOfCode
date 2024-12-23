import regex
from aocd.models import Puzzle

puzzle = Puzzle(year=2024, day=3)

def part_a():
    data = puzzle.input_data
    I = regex.finditer(r'mul\(\d{1,3},\d{1,3}\)', data)
    tot = 0
    for r in I:
        words = [int(i) for i in r[0][4:-1].split(',')]
        tot += words[0] * words[1]
    puzzle.answer_a = tot
    print(tot)

def part_b():
    data = puzzle.input_data
    I = regex.finditer(r'(mul\(\d{1,3},\d{1,3}\))|(do\(\))|(don\'t\(\))', data)
    tot = 0
    do = True
    for r in I:
        words = r[0]
        if words == 'do()':
            do = True
            continue
        if words == 'don\'t()':
            do = False
            continue
        if do:
            words = [int(i) for i in r[0][4:-1].split(',')]
            tot += words[0] * words[1]
    puzzle.answer_b = tot
    print(tot)


part_a()
part_b()