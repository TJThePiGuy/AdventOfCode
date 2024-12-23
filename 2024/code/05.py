from aocd.models import Puzzle
from functools import cmp_to_key

puzzle = Puzzle(day = 5, year = 2024)

def part_a():
    data = puzzle.input_data.split('\n\n')
    orders = set()
    for line in data[0].split('\n'):
        xs = [int(i) for i in line.split('|')]
        orders.add((xs[0],xs[1]))

    correct = 0
    for line in data[1].split('\n'):
        line = [int(i) for i in line.split(',')]
        L = len(line)
        for idx in range(L):
            X = line[idx]
            for jdx in range(idx+1,L):
                Y = line[jdx]
                if (Y,X) in orders:
                    break
            else:
                continue
            break
        else:
            correct += line[L//2]
    puzzle.answer_a = correct
    print(correct)

def part_b():
    data = puzzle.input_data.split('\n\n')
    orders = set()
    for line in data[0].split('\n'):
        xs = [int(i) for i in line.split('|')]
        orders.add((xs[0],xs[1]))

    def comp(x,y):
        if (x,y) in orders:
            return -1
        if (y,x) in orders:
            return 1
        return 0
    
    correct = 0
    for line in data[1].split('\n'):
        line = [int(i) for i in line.split(',')]
        L = len(line)
        for idx in range(L):
            X = line[idx]
            for jdx in range(L-1, idx, -1):
                Y = line[jdx]
                if (Y,X) in orders:
                    break
            else:
                continue
            break
        else:
            continue
        line = sorted(line, key = cmp_to_key(comp))
        correct += line[L//2]
    puzzle.answer_b = correct
    print(correct)

part_a()
part_b()