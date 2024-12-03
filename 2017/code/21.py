from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day = 21, year = 2017)

def str_to_np(mat):
    return np.matrix([[i=='#' for i in _] for _ in mat.split('/')])
data = "##./#../..."

mappings:dict = dict()

def part_a():
    global mappings
    data = puzzle.input_data

    for line in data.split('\n'):
        splitput = line.split(" => ")
        key, val = map(str_to_np, splitput)
        for a in (key, np.fliplr(key)):
            for i in range(4):
                mappings[np.rot90(a, i).tobytes()] = val
        
    curr_mat:np.matrix = str_to_np('.#./..#/###')

    for iter in range(5):
        n_row, n_col = curr_mat.shape
        next_mat = np.matrix([])
        by = 2 if (n_row % 2 == 0) else 3
        next_mat = np.zeros(shape = ((by+1) * n_row//by, (by+1)*n_row//by), dtype=bool)
        for old_row in range(0, n_row, by):
            for col_start in range(0, n_col, by):
                submat = curr_mat[old_row:old_row+by,col_start:col_start+by] 
                out = mappings[submat.tobytes()]
                next_mat[((by+1)*old_row//by) : ((by+1)*old_row//by + (by+1)),
                         ((by+1)*col_start//by) : ((by+1)*col_start//by + (by+1))] = out
           
        curr_mat = next_mat
    ans = np.sum(curr_mat)
    puzzle.answer_a = ans
    print(ans)
    # puzzle.answer_a = np.sum(curr_mat)


def part_b():
    global mappings

    curr_mat:np.matrix = str_to_np('.#./..#/###')

    for iter in range(18):
        n_row, n_col = curr_mat.shape
        next_mat = np.matrix([])
        by = 2 if (n_row % 2 == 0) else 3
        next_mat = np.zeros(shape = ((by+1) * n_row//by, (by+1)*n_row//by), dtype=bool)
        for old_row in range(0, n_row, by):
            for col_start in range(0, n_col, by):
                submat = curr_mat[old_row:old_row+by,col_start:col_start+by] 
                out = mappings[submat.tobytes()]
                next_mat[((by+1)*old_row//by) : ((by+1)*old_row//by + (by+1)),
                         ((by+1)*col_start//by) : ((by+1)*col_start//by + (by+1))] = out
           
        curr_mat = next_mat
    ans = np.sum(curr_mat)
    puzzle.answer_b = ans
    print(ans)

part_a()
part_b()