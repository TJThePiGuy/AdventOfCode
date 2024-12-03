from aocd.models import Puzzle
from tqdm import tqdm

puzzle = Puzzle(day=15, year = 2017)

def part_a():
    data = [int(i.split()[-1]) for i in puzzle.input_data.split('\n')]

    a_val = data[0]
    b_val = data[1]

    a_mult = 16807
    b_mult = 48271

    big_mod = 2147483647

    match_count = 0

    for i in tqdm(range(40_000_000)):
        a_val *= a_mult
        a_val %= big_mod

        b_val *= b_mult
        b_val %= big_mod

        match_count += ((a_val - b_val) % (1<<16)) == 0
    puzzle.answer_a = match_count
    print(match_count)

def part_b():
    data = [int(i.split()[-1]) for i in puzzle.input_data.split('\n')]

    a_val = data[0]
    b_val = data[1]

    a_mult = 16807
    b_mult = 48271

    big_mod = 2147483647

    match_count = 0

    for i in tqdm(range(5_000_000)):
        
        a_val *= a_mult
        a_val %= big_mod

        while(a_val % 4 != 0):
            a_val *= a_mult
            a_val %= big_mod

        b_val *= b_mult
        b_val %= big_mod

        while(b_val % 8 != 0):
            b_val *= b_mult
            b_val %= big_mod

        match_count += ((a_val - b_val) % (1<<16)) == 0
    puzzle.answer_b = match_count
    print(match_count)

# part_a()
part_b()