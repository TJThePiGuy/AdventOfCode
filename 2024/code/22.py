from aocd.models import Puzzle
import numpy as np
from collections import defaultdict

puzzle = Puzzle(day = 22, year = 2024)

data = puzzle.input_data
starts = [int(i) for i in data.split('\n')]

MIX = 16777216

def part_a():
    total = 0
    for s in starts:
        secret = s
        for i in range(2000):
            secret = ((secret * 64) ^ secret) % MIX
            secret = ((secret // 32) ^ secret) % MIX
            secret = ((secret * 2048) ^ secret) % MIX
        total += secret
    print(total)
    puzzle.answer_a = total

nums = {i for i in range(-9,10)}

def part_b():
    bananas = defaultdict(int)
    for s in starts:
        sequence = [s % 10]
        secret = s
        for i in range(2000):
            secret = ((secret * 64) ^ secret) % MIX
            secret = ((secret // 32) ^ secret) % MIX
            secret = ((secret * 2048) ^ secret) % MIX
            sequence.append(secret % 10)
        diffs = np.diff(sequence).tolist()

        in_seq = set()
        for i in range(len(diffs)-4):
            d = tuple(diffs[i:i+4])
            if d in in_seq:
                continue
            in_seq.add(d)
            if len(d) == 4:
                 bananas[d] += sequence[i + 4]
    print(max(bananas.values()))
    puzzle.answer_b = max(bananas.values())
    
part_a()
part_b()