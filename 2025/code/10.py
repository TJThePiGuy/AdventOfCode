from aocd.models import Puzzle
import itertools as it
from scipy.optimize import linprog

puzzle = Puzzle(year = 2025, day = 10)

data = puzzle.input_data
# data = puzzle.examples[0].input_data

def powerset(iterable):
    s = iterable
    return it.chain.from_iterable(it.combinations(s,r) for r in range(len(s)+1))

def part_a():
    total = 0
    for line in data.split('\n'):
        targetStr = line.split(' ')[0][1:-1]
        target = set(i for i,chr in enumerate(targetStr) if chr == '#')
        rules = line.split(' ')[1:-1]
        rules = list(set(int(i) for i in rule[1:-1].split(',')) for rule in rules)
        for ruleSubset in powerset(rules):
            current = set()
            for rule in ruleSubset:
                current.symmetric_difference_update(rule)
            if target == current:
                total += len(ruleSubset)
                break
    print(total)
    puzzle.answer_a = total

def part_b():
    total = 0
    for line in data.split('\n'):
        targetStr = line.split(' ')[-1][1:-1]
        targetCounts = list(int(v) for v in targetStr.split(','))
        rules = line.split(' ')[1:-1]
        rules = list(set(int(i) for i in rule[1:-1].split(',')) for rule in rules)
        ones = [1] * len(rules)
        A = []
        for i in range(len(targetCounts)):
            A.append(list((1 if i in s else 0) for s in rules))
        solution = linprog(A_eq=A, b_eq = targetCounts, c = ones, integrality=1)
        total += int(solution.fun)
    print(total)
    puzzle.answer_b = total

part_a()

part_b()