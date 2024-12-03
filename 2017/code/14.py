from aocd.models import Puzzle
from numpy import base_repr

puzzle:Puzzle = Puzzle(day = 14, year = 2017)

def ind_map(idx):
    return(idx % 256)

def pinch(List, first, length):
    for dx in range(length//2):
        temp = List[ind_map(first + dx)]
        List[ind_map(first + dx)] = List[ind_map(first + length - dx-1)] 
        List[ind_map(first+length-dx-1)] = temp
    return(List)

def knot_hash(key):
    nums = [i for i in range(256)]
    skip_size = 0
    curr_idx = 0
    rules = [ord(i) for i in key] + [17, 31, 73, 47, 23]
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
    hash = ''.join(str(base_repr(j, 16)).zfill(2) for j in dense_hash)
    return(hash)

def part_a():
    data = puzzle.input_data


    ones = 0
    
    for row in range(128):
        hash = knot_hash(data + '-' + str(row))
        b_rep = str(bin(int(hash,16)))[2:]
        ones += sum(int(i) for i in b_rep)
    print(ones)
    puzzle.answer_a = ones

def part_b():
    data = puzzle.input_data
    hashes:set[int] = set()

    for row in range(128):
        hash = knot_hash(data + '-' + str(row))
        b_rep = str(bin(int(hash,16)))[2:].zfill(128)

        for col in range(len(b_rep)):
            if b_rep[col] == '1':
                hashes.add((row, col))

    checked:set[tuple[int,int]] = set()

    groups = 0

    for start in hashes:
        if start in checked:
            continue
        groups += 1

        to_check:set[tuple[int,int]] = {start}
        while(len(to_check)!= 0):
            val = to_check.pop()
            if val in checked:
                continue

            checked.add(val)
            if not(val in hashes):
                continue
            for deltas in [(-1,0),(1,0),(0,-1),(0,1)]:
                new_x = val[0] + deltas[0]
                new_y = val[1] + deltas[1]

                new_val = (new_x, new_y)

                if new_val in checked:
                    continue
                if new_val in to_check:
                    continue
                to_check.add(new_val)
        
    print(groups)
    puzzle.answer_b = groups

# part_a()
part_b()