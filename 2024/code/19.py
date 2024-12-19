from aocd.models import Puzzle
from collections import defaultdict

puzzle = Puzzle(day = 19, year = 2024)

data = puzzle.input_data

towels = set(data.split('\n\n')[0].split(', '))
designs = set(data.split('\n\n')[1].split('\n'))

def part_a():
    total = 0
    for design in designs:
        reachable:set[int] = set()
        L = len(design)
        to_check:set[int] = {0}
        while L not in reachable and len(to_check) > 0:
            idx = to_check.pop()
            if idx in reachable:
                continue
            reachable.add(idx)
            for towel in towels:
                towel_l = len(towel)
                if towel == design[idx:idx+towel_l]:
                    to_check.add(idx+towel_l)
        if L in reachable:
            total += 1
    print(total)
    puzzle.answer_a = total


def part_b():
    total = 0
    for design in designs:
        reachable:dict[int,int] = defaultdict(int)
        L = len(design)
        reachable[0] = 1
        for i in range(len(design)):
            for towel in towels:
                towel_l = len(towel)
                if towel == design[i:i+towel_l]:
                    reachable[i+towel_l] += reachable[i]
        total += reachable[L]
    print(total)
    puzzle.answer_b = total

part_a()
part_b()