from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day = 9, year = 2024)

def part_a():
    data = puzzle.input_data
    data = [int(i) for i in data]
    counts = data[::2]
    cum_sums = np.cumsum(data)
    take_from_front= True
    pos = 0
    cum_sum_idx = 0
    total = 0
    left_idx = 0
    right_idx = len(data)//2
    while(left_idx <= right_idx):
        if(take_from_front):
            total += pos * left_idx
            counts[left_idx] -= 1
            while(counts[left_idx] == 0):
                left_idx += 1
                if(left_idx >= len(data)//2):
                    break
        else:
            total += pos*right_idx
            counts[right_idx] -= 1
            while(counts[right_idx] == 0):
                right_idx -= 1
                if(right_idx < 0):
                    break
        pos += 1
        while(pos >= cum_sums[cum_sum_idx]):
            cum_sum_idx += 1
            take_from_front = not take_from_front
    print(total)
    puzzle.answer_a = total

def part_b():
    data = puzzle.input_data
    data = np.array([int(i) for i in data])
    block_lengths = data[::2]
    space_lengths = data[1::2]
    cum_sums = np.cumsum(data)
    block_starts = cum_sums[::2] - data[::2]
    space_starts = cum_sums[1::2] - data[1::2]
    for idx in range(len(block_lengths)-1,0,-1):
        update = False
        for space_dx in range(idx):
            if block_lengths[idx] <= space_lengths[space_dx]:
                update = True
                break
        if update:
            block_starts[idx] = space_starts[space_dx]
            space_starts[space_dx] += block_lengths[idx]
            space_lengths[space_dx] -= block_lengths[idx]
    total = 0
    for idx in range(len(block_lengths)):
        L = block_lengths[idx]
        start = block_starts[idx]

        total += idx * (L*(start-1) + L*(L+1)/2)
    puzzle.answer_b = total
    print(total)
part_a()

part_b()