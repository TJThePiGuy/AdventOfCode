from aocd.models import Puzzle
from numpy import base_repr

puzzle:Puzzle = Puzzle(day = 10, year = 2017)

def ind_map(idx):
    return(idx % 256)

def pinch(List, first, length):
    for dx in range(length//2):
        temp = List[ind_map(first + dx)]
        List[ind_map(first + dx)] = List[ind_map(first + length - dx-1)] 
        List[ind_map(first+length-dx-1)] = temp
    return(List)

def part_a():
    nums = [i for i in range(256)]
    skip_size = 0
    curr_idx = 0
    rules = [int(i) for i in puzzle.input_data.split(',')]
    for rule in rules:
        nums = pinch(nums, curr_idx, rule)

        curr_idx += rule + skip_size
        curr_idx %= 256
        skip_size += 1
    mult = nums[0] * nums[1]
    puzzle.answer_a = mult
    print(mult)


def part_b():
    nums = [i for i in range(256)]
    skip_size = 0
    curr_idx = 0
    rules = [ord(i) for i in puzzle.input_data] + [17, 31, 73, 47, 23]
    for _ in range(64):
        for rule in rules:
            nums = pinch(nums, curr_idx, rule)

            curr_idx += rule + skip_size
            curr_idx %= 256
            skip_size += 1
    dense_hash = [0]*16
    for start in range(0, 256, 16):
        for dx in range(16):
            dense_hash[start//16] ^= nums[start + dx]
    hash = ''.join(str(base_repr(j, 16)) for j in dense_hash).lower()
    print(hash)
    puzzle.answer_b = hash

part_a()
part_b()