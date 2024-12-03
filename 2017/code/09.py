from aocd.models import Puzzle

puzzle:Puzzle = Puzzle(day = 9, year = 2017)

def part_a():
    total_score = 0
    in_garbage = False
    cancel = False
    full_str = puzzle.input_data
    L = len(full_str)
    open_inds = list()
    for idx in range(L):
        if(cancel):
            cancel = False
            continue
        curr_char = full_str[idx]
        if(curr_char == "!"):
            cancel = True
        elif(curr_char == '>' and in_garbage):
            in_garbage = False
        elif(in_garbage):
            continue
        elif(curr_char == "<"):
            in_garbage = True
        elif(curr_char == "{"):
            open_inds.append(idx)
        elif(curr_char == "}"):
            total_score += len(open_inds)
            open_inds.pop()
    puzzle.answer_a = total_score
    print(total_score)

def part_b():
    char_count = 0
    in_garbage = False
    cancel = False
    full_str = puzzle.input_data
    L = len(full_str)
    open_inds = list()
    for idx in range(L):
        if(cancel):
            cancel = False
            continue
        curr_char = full_str[idx]
        if(curr_char == "!"):
            cancel = True
        elif(curr_char == '>' and in_garbage):
            in_garbage = False
        elif(in_garbage):
            char_count += 1
            continue
        elif(curr_char == "<"):
            in_garbage = True
        elif(curr_char == "{"):
            open_inds.append(idx)
        elif(curr_char == "}"):
            open_inds.pop()
    puzzle.answer_b = char_count
    print(char_count)


part_a()
part_b()