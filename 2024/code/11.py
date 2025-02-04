from aocd.models import Puzzle

puzzle = Puzzle(day = 11, year = 2024)
data = puzzle.input_data


def part_a():
    start = [int(i) for i in data.split(' ')]
    run  = start.copy()

    for blink in range(25):
        next = []
        for item in run:
            if item == 0:
                next.append(1)
                continue
            L = len(str(item))
            if L % 2 == 0:
                first = int(str(item)[:L//2])
                last = int(str(item)[L//2:])
                next.append(first)
                next.append(last)
            else:
                next.append(item * 2024)
        
        run = next.copy()
    print(len(run))
    puzzle.answer_a = len(run)

def part_b():
    start = [int(i) for i in data.split(' ')]
    run = dict()
    for item in start:
        run[item] = 1
    for blink in range(75):
        next = dict()
        for item,ct in run.items():
            if item == 0:
                if 1 not in next:
                    next[1] = 0
                next[1] += ct
                continue
            L = len(str(item))
            if L % 2 == 0:
                first = int(str(item)[:L//2])
                last = int(str(item)[L//2:])
                if first not in next:
                    next[first] = 0
                next[first] += ct
                if last not in next:
                    next[last] = 0
                next[last] += ct
            else:
                if (item*2024) not in next:
                    next[item * 2024] = 0
                next[item * 2024] += ct
        run = next.copy()
    print(sum(next.values()))
    puzzle.answer_b = sum(run.values())


part_a()
part_b()