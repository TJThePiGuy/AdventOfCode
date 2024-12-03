from aocd.models import Puzzle
from tqdm import tqdm

puzzle = Puzzle(day=25, year = 2017)

vals:dict[int,int] = dict()

def get(key):
    return vals.get(key, 0)

def set(key, val):
    vals[key] = val

def part_a():
    data = puzzle.input_data

    instrs = data.split('\n\n')

    curr_state:str = instrs[0].split('\n')[0][-2]
    steps:int = int(instrs[0].split('\n')[1].split()[-2])

    state_dict:dict[str,tuple[tuple[int,int,str],tuple[int,int,str]]] = dict()

    for instr in instrs[1:]:
        lines = instr.split('\n')
        state = lines[0][-2]
        zero_write = int(lines[2][-2])
        zero_dir = 1 if lines[3][-3] == 'h' else -1
        zero_state = lines[4][-2]
        one_write = int(lines[6][-2])
        one_dir = 1 if lines[7][-3] == 'h' else -1
        one_state = lines[8][-2]
        state_dict[state] = ((zero_write, zero_dir, zero_state),(one_write, one_dir, one_state))

    curr_idx = 0

    for step in tqdm(range(steps)):
        curr_val = get(curr_idx)
        (wr, dx, st) = state_dict[curr_state][curr_val]
        set(curr_idx, wr)
        curr_idx += dx
        curr_state = st
    checksum = sum(vals.values())
    print(checksum)
    puzzle.answer_a = checksum


part_a()