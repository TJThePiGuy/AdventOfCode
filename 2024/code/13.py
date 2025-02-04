from aocd.models import Puzzle
import regex as re
import numpy as np

puzzle = Puzzle(day = 13, year = 2024)

data = puzzle.input_data

def part_a():
    boxes = data.split('\n\n')
    total = 0
    for box in boxes:
        lines = box.split('\n')
        a_moves = [int(i) for i in re.findall('\\d+', lines[0])]
        b_moves = [int(i) for i in re.findall('\\d+', lines[1])]
        goal = [int(i) for i in re.findall('\\d+', lines[2])]

        to_check = {(0,0)}
        checked = set()
        found = False
        least_presses = 40000
        while(len(to_check) != 0):
            counts = to_check.pop()
            if counts in checked:
                continue
            checked.add(counts)
            A, B = counts
            if A > 100 or B > 100:
                continue
            curr_x = A*a_moves[0] + B*b_moves[0]    
            curr_y = A*a_moves[1] + B*b_moves[1]
            if curr_x == goal[0] and curr_y == goal[1]:
                found = True
                least_presses = min(least_presses, 3*A + B)
                continue
            if (curr_x + a_moves[0] <=goal[0]) and (curr_y + a_moves[1]<= goal[1]):
                to_check.add((A+1,B)) 

            if (curr_x + b_moves[0] <= goal[0]) and (curr_y + b_moves[1] <= goal[1]):
                to_check.add((A, B+1))
        if found:
            total += least_presses
    puzzle.answer_a = total
    print(total)

def part_b():
    boxes = data.split('\n\n')
    total = 0
    for box in boxes:
        lines = box.split('\n')
        a_moves = [int(i) for i in re.findall('\\d+', lines[0])]
        b_moves = [int(i) for i in re.findall('\\d+', lines[1])]
        goal = np.matrix([10000000000000 + int(i) for i in re.findall('\\d+', lines[2])])

        mat = np.transpose(np.matrix([a_moves, b_moves]))
        
        sol = [i[0] for i in np.linalg.solve(mat, np.transpose(goal)).tolist()]

        if all( abs(i -round(i)) < 2**-8 for i in sol):
            total += 3 * sol[0] + sol[1]

    print(total)
    puzzle.answer_b = total

part_a()
part_b()