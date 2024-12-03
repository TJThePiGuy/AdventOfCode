from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 6, year = 2017)

def hash_a(pile):
    H = 0
    for (idx, val) in enumerate(pile[:-1:]):
        H += val * (56**idx)
    return(H)

def part_a():
    pile = [int(i) for i in puzzle.input_data.split()]
    curr_hash = hash_a(pile)
    seen_hashes = set()

    n = 0

    while not (curr_hash in seen_hashes):
        seen_hashes.add(curr_hash)
        size = max(pile)
        idx = pile.index(size)
        pile[idx] = 0
        for _ in range(size):
            idx = (idx+1) % len(pile)
            pile[idx] += 1
        n += 1
        curr_hash = hash_a(pile)
    puzzle.answer_a = n
    print(n)

def part_b():
    pile = [int(i) for i in puzzle.input_data.split()]
    curr_hash = hash_a(pile)
    seen_hashes = set()

    pos_dict = dict()

    n = 0

    while not (curr_hash in seen_hashes):
        seen_hashes.add(curr_hash)
        pos_dict[curr_hash] = n
        size = max(pile)
        idx = pile.index(size)
        pile[idx] = 0
        for _ in range(size):
            idx = (idx+1) % len(pile)
            pile[idx] += 1
        n += 1
        curr_hash = hash_a(pile)
    puzzle.answer_b = n - pos_dict[curr_hash]
    print(n - pos_dict[curr_hash])

part_a()
part_b()