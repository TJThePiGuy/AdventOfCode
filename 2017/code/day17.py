from aocd.models import Puzzle
from tqdm import tqdm

puzzle = Puzzle(day=17, year = 2017)

def part_a():
    data = int(puzzle.input_data)
    curr_list = [0]
    curr_pos = 0
    for i in range(1,2018):
        curr_pos += data
        curr_pos %= i
        curr_list.insert(curr_pos, i)
        curr_pos += 1
        # print(curr_list)
    pass
    puzzle.answer_a = curr_list[curr_pos]
    print(curr_list[curr_pos])


def part_b():
    data = int(puzzle.input_data)
    curr_pos = 0
    front = 0
    for i in tqdm(range(1,50_000_001)):
        curr_pos += data
        curr_pos %= i
        if curr_pos==0:
            front = i
        curr_pos += 1
    puzzle.answer_b = front
    print(front)

part_a()
part_b()