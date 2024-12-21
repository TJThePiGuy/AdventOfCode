from aocd.models import Puzzle
import regex as re
import itertools as it
import functools as ft
import numpy as np
from collections import defaultdict
from tqdm import tqdm

puzzle = Puzzle(day = 21, year = 2024)

data = puzzle.input_data
data = '''029A
980A
179A
456A
379A'''

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

dist_dict:dict[tuple[str,str],int] = dict()

for a,b in it.product(keypad, keypad):
    ax, ay = get_keypad_coords(a)
    bx, by = get_keypad_coords(b)
    dist_dict[(a,b)] = abs(ax-bx) + abs(ay-by)

def get_cost(seq):
    total = 0
    for a,b in zip(seq[:-1],seq[1:]):
        total += dist_dict[(a,b)]
    return total

cheapest_paths:dict[tuple[int,int,int,int,int],int] = dict()

dirs = {'^':(0,-1),'v':(0,1),'>':(1,0),'<':(-1,0)}

def cheapest_path(x1, y1, x2, y2, r):

    if (x1,y1,x2,y2,r) in cheapest_paths:
        return cheapest_paths[((x1,y1,x2,y2,r))]
    seqs = all_arrow_seqs(x1, y1, x2, y2)

    if r == 0:
        L = abs(x1-x2) + abs(y1-y2)
        cheapest_paths[(x1,y1,x2,y2,r)] = L
        return L

    cheapest = -1

    if len(seqs) == 0:
        cheapest = 0

    for seq in seqs:
        cost = 0
        cx = x1
        cy = y1
        for c in seq:
            (dx,dy) = dirs[c]
            cost += cheapest_path(cx, cy, cx+dx, cy+dy, r-1)
            cx += dx
            cy += dy
        cost += cheapest_path(x2, y2, 2, 0, r-1)
        if cheapest < 0 or cost < cheapest:
            cheapest = cost
    cheapest_paths[(x1,y1,x2,y2,r)] = cheapest
    return cheapest

def part_a_alt():
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
            positions = [get_keypad_coords(s) for s in 'A' + start_pos]
            cost = 0
            for (sx, sy), (ex, ey) in it.pairwise(positions):
                cost += cheapest_path(sx, sy, ex, ey, 2)
            if cost < min_cost or min_cost < 0:
                min_cost = cost
        print(min_cost, int(line[:-1]))
        total += int(line[:-1]) * min_cost
    print(total)
    # puzzle.answer_a = total
        
    pass
part_a_alt()
exit()


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
        KEY_MOVES = set()
        for start_pos in nums_moves:
            max_sim_score = -1
            positions = [get_keypad_coords(s) for s in 'A' + start_pos]
            key_moves = set()
            key_moves.add('')
            for (x1, y1), (x2, y2) in zip(positions[:-1], positions[1:]):
                all_moves = all_arrow_seqs(x1, y1, x2, y2)
                if(len(all_moves) == 0):
                    all_moves = {''}
                next_moves = set()
                for s1, s2 in it.product(key_moves, all_moves):
                    sim_score = calc_sim_score(s1 + s2  + 'A')
                    if sim_score > max_sim_score:
                        next_moves = set()
                        max_sim_score = sim_score
                    if sim_score >= max_sim_score:
                        next_moves.add(s1 + s2 + 'A')
                key_moves = next_moves.copy()
            KEY_MOVES.update(key_moves)
        L = min(len(i) for i in KEY_MOVES)
        KEY_MOVES = set(filter(lambda x: len(x) == L, KEY_MOVES))
        for JDX in (range(1)):
            NEW_KEYS = set()

            for J, start_pos in enumerate(KEY_MOVES):
                # print(len(start_pos))
                positions = [get_keypad_coords(s) for s in 'A' + start_pos]
                key_moves = set()
                key_moves.add('')
                for A, B in enumerate(zip(positions[:-1], positions[1:])):
                    (x1, y1), (x2, y2) = B
                    all_moves = all_arrow_seqs(x1, y1, x2, y2)
                    if(len(all_moves) == 0):
                        all_moves = {''}
                    next_moves = set()
                    # print(len(key_moves), len(all_moves), end = ',', sep=':')
                    for s1, s2 in it.product(key_moves, all_moves):
                        next_moves.add(s1 + s2 + 'A')
                    key_moves = next_moves.copy()
                NEW_KEYS.update(key_moves)
            
            L = min(len(i) for i in NEW_KEYS)
            KEY_MOVES = set(filter(lambda x: len(x) == L, NEW_KEYS))
        total += L * int(line[:-1])

    print(total)
    puzzle.answer_a = total

part_b()