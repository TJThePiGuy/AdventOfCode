from aocd.models import Puzzle

puzzle = Puzzle(year = 2025, day = 6)

# data = puzzle.examples[0].input_data
data = puzzle.input_data

def part_a():
    lines = data.split('\n')
    indices = set(i for i,op in enumerate(lines[-1].split()) if op == '+')
    running = [int(i) for i in lines[0].split()]
    for line in lines[1:-1]:
        for i, n in enumerate(line.split()):
            n = int(n)
            running[i] = (running[i] + n) if i in indices else (running[i] * n )
    print(sum(running))
    puzzle.answer_a = (sum(running))


def part_b():
    lines = data.split('\n')
    breaks = [-1] + [i for i in range(len(lines[0])) if all(line[i] == ' ' for line in lines)] + [len(lines[0])]
    total = 0
    for l, r in zip(breaks[:-1],breaks[1:]):
        op = lines[-1][l+1]
        running = 1 if op == '*' else 0
        for idx in range(l+1,r):
            digit = int(''.join(line[idx] for line in lines[:-1]))
            running = running * digit if op == '*' else running + digit
        total += running
    print(total)
    puzzle.answer_b = total
    
part_a() 

part_b()