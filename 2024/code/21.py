from aocd.models import Puzzle
import itertools as it

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

def get_keypad_coords(s):
    for i, c in enumerate(keypad):
        if c == s:
            return (2 - (i % 3), 1 - (i)//3)
     
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

        key_moves_1 = set()
        for start_pos in nums_moves:
            positions = [get_keypad_coords(s) for s in 'A' + start_pos]
            key_moves = set()
            key_moves.add('')
            for (x1, y1), (x2, y2) in zip(positions[:-1], positions[1:]):
                all_moves = all_arrow_seqs(x1, y1, x2, y2)
                if(len(all_moves) == 0):
                    all_moves = {''}
                next_moves = set()
                for s1, s2 in it.product(key_moves, all_moves):
                    next_moves.add(s1 + s2 + 'A')
                key_moves = next_moves.copy()
            key_moves_1.update(key_moves)

        key_moves_2 = set()
        for start_pos in key_moves_1:
            positions = [get_keypad_coords(s) for s in 'A' + start_pos]
            key_moves = set()
            key_moves.add('')
            for (x1, y1), (x2, y2) in zip(positions[:-1], positions[1:]):
                all_moves = all_arrow_seqs(x1, y1, x2, y2)
                if(len(all_moves) == 0):
                    all_moves = {''}
                next_moves = set()
                for s1, s2 in it.product(key_moves, all_moves):
                    next_moves.add(s1 + s2 + 'A')
                key_moves = next_moves.copy()
            key_moves_2.update(key_moves)
        total += min(len(i) for i in key_moves_2) * int(line[:-1])
    print(total)
    puzzle.answer_a = total

part_a()