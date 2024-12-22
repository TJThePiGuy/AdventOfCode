from aocd.models import Puzzle
import itertools as it
import numpy as np

puzzle = Puzzle(day = 21, year = 2024)

data = puzzle.input_data

NUM_SEQS:dict[tuple[int,int,int,int], set[str]] = dict()

def all_num_seqs(x1,y1,x2,y2):
    if(x1, y1, x2, y2) in NUM_SEQS:
        return NUM_SEQS[(x1,y1,x2,y2)]
    seqs = set()
    dx = x2-x1
    dy = y2-y1
    if dx != 0:
        step = 1 if dx > 0 else -1
        if (x1+step, y1) != (0,3):
            step_things = all_num_seqs(x1+step, y1, x2, y2)
            if len(step_things) == 0:
                step_things = {''}
            chr = '>' if step > 0 else '<'
            seqs.update(chr + s for s in step_things)
    if dy != 0:
        step = 1 if dy > 0 else -1
        if (x1, y1+step) != (0,3):
            step_things = all_num_seqs(x1, y1+step, x2, y2)
            if len(step_things) == 0:
                step_things = {''}
            chr = 'v' if step > 0 else '^'
            seqs.update(chr + s for s in step_things)

    NUM_SEQS[(x1,y1,x2,y2)] = seqs
    return seqs

nums = ''.join(str(i) for i in range(9, 0, -1)) + 'A0'

def get_numpad_coords(s):
    for i, c in enumerate(nums):
        if c == s:
            return ( 2 - (i % 3), i//3)

ARR_SEQS:dict[tuple[int,int,int,int], set[str]] = dict()

def all_arrow_seqs(x1, y1, x2, y2):
    if(x1, y1, x2, y2) in ARR_SEQS:
        return ARR_SEQS[(x1,y1,x2,y2)]
    
    seqs = set()
    dx = x2-x1
    dy = y2-y1

    if dx != 0:
        step = 1 if dx > 0 else -1

        if (x1+step, y1) != (0,0):
            step_things = all_arrow_seqs(x1+step, y1, x2, y2)
            if len(step_things) == 0:
                step_things = {''}
            chr = '>' if step > 0 else '<'
            seqs.update(chr + s for s in step_things)
    if dy != 0:
        step = 1 if dy > 0 else -1
        if (x1, y1+step) != (0,0):
            step_things = all_arrow_seqs(x1, y1+step, x2, y2)
            if len(step_things) == 0:
                step_things = {''}
            chr = 'v' if step > 0 else '^'
            seqs.update(chr + s for s in step_things)

    ARR_SEQS[(x1,y1,x2,y2)] = seqs
    return seqs

keypad = '>v<A^'

RAW_TRANS = '''0	0	0	0	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	1	0	0	1	0	1	1	0	0	0	0	0	0	0	0	1	0	0	1	0
0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	1	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	1	0	0	0	0	1	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0
0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0
0	1	1	0	0	0	0	1	0	0	0	0	0	0	0	0	0	1	0	1	0	0	1	0	0
0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	1	0	0	0	0	1	1	0	1	1	0	0	0	0	0	0	0	0	1	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	1	0	1	0	0	1	1	1	0	0
0	1	1	0	1	0	0	1	0	0	0	0	0	0	0	0	1	0	0	1	0	0	0	0	0
1	0	0	0	0	0	1	0	0	0	0	0	1	0	0	0	0	0	1	0	0	0	0	0	1
0	0	0	1	0	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	1	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
0	0	0	1	1	0	0	0	0	1	0	0	0	1	1	0	0	0	0	0	0	0	0	0	0
0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0	0
'''

TRANSITION = [int(i) for i in RAW_TRANS.replace('\t','').replace('\n','')]

trans_mat = np.array(TRANSITION, dtype=np.int64).reshape(25,25)

five_step = np.linalg.matrix_power(trans_mat, 5)
twenty_five_step = np.linalg.matrix_power(five_step, 5)

def part_a():
    total = 0
    for line in data.split('\n'):
        positions = [get_numpad_coords(s) for s in 'A' + line]
        nums_moves = set()
        nums_moves.add('')
        for (x1, y1), (x2, y2) in zip(positions[:-1], positions[1:]):
            all_moves = all_num_seqs(x1, y1, x2, y2)
            next_moves = set()
            for s1, s2 in it.product(nums_moves, all_moves):
                next_moves.add(s1 + s2 + 'A')
            nums_moves = next_moves.copy()
        min_cost = -1
        for start_pos in nums_moves:
            positions = [keypad.index(s) for s in 'A' + start_pos]
            vec = np.zeros([25,1],dtype=int)
            for s, e in it.pairwise(positions):
                vec[5*s+e] += 1
            vec = np.matmul(np.linalg.matrix_power(trans_mat, 2), vec)
            cost = sum(vec)
            if min_cost < 0 or cost < min_cost:
                min_cost = cost
        total += min_cost * int(line[:-1])
        print(min_cost, line)
    puzzle.answer_a = total[0]

def part_b():
    total = 0
    for line in data.split('\n'):
        positions = [get_numpad_coords(s) for s in 'A' + line]
        nums_moves = set()
        nums_moves.add('')
        for (x1, y1), (x2, y2) in zip(positions[:-1], positions[1:]):
            all_moves = all_num_seqs(x1, y1, x2, y2)
            next_moves = set()
            for s1, s2 in it.product(nums_moves, all_moves):
                next_moves.add(s1 + s2 + 'A')
            nums_moves = next_moves.copy()
        min_cost = -1
        for start_pos in nums_moves:
            positions = [keypad.index(s) for s in 'A' + start_pos]
            vec = np.zeros([25,1],dtype=int)
            for s, e in it.pairwise(positions):
                vec[5*s+e] += 1
            vec = np.matmul(twenty_five_step, vec)
            print(np.transpose(vec))
            cost = sum(vec)
            if min_cost < 0 or cost < min_cost:
                min_cost = cost
        total += min_cost * int(line[:-1])
        print(min_cost, line)
    puzzle.answer_b = total[0]
    pass

part_a()
part_b()