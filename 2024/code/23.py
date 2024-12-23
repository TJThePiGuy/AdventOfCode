from aocd.models import Puzzle
from tqdm import tqdm

puzzle = Puzzle(year = 2024, day = 23)

data = puzzle.input_data

pairs = set(tuple(line.split('-')) for line in data.split('\n'))

comps = list()
idx = 0
idx_map:dict[str,int] = dict()

for pair in pairs:
    for i in pair:
        if i not in comps:
            idx_map[i] = idx
            idx += 1
            comps.append(i)

pairs = set(tuple(sorted(i, key = lambda x:idx_map[x])) for i in pairs)

def part_a():
    trios = set()
    for idx, a in enumerate(comps):
        for jdx, b in enumerate(comps[idx+1:], idx+1):
            if (a,b) not in pairs:
                continue
            for c in comps[jdx+1:]:
                if (a,c) not in pairs:
                    continue
                if (b,c) not in pairs:
                    continue
                trios.add((a,b,c))
    total = 0
    for t in trios:
        if any(i[0] == 't' for i in t):
            total += 1
    print(total)
    puzzle.answer_a = total

def part_b():
    size = 2
    to_check = pairs.copy()
    while len(to_check) > 1:
        next_check = set()
        for group in tqdm(to_check):
            largest_idx = idx_map[group[-1]]
            for c in comps[largest_idx+1:]:
                if all((a,c) in pairs for a in group):
                    next_check.add(group + (c,))

        to_check = next_check.copy()
        size += 1
        print(size, len(to_check))
    final_group = to_check.pop()
    ans = ','.join(sorted(final_group))
    print(ans)
    puzzle.answer_b = ans

part_a()
part_b()