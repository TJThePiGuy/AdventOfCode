from aocd.models import Puzzle
import numpy as np

puzzle = Puzzle(day=16, year = 2017)

def part_a():
    data = puzzle.input_data
    rules = data.split(',')

    places = np.identity(n = 16)

    shift = np.zeros((16,16))
    for idx in range(16):
        shift[idx, (idx-1)%16] = 1
    for rule in rules:
        if rule[0] == 's':
            shift_by = int(rule[1:])
            places = np.matmul(np.linalg.matrix_power(shift, shift_by), places)
        elif rule[0] == 'x':
            swap_mat = np.identity(n = 16)

            targets = rule[1:].split('/')
            idx_1 = int(targets[0])
            idx_2 = int(targets[1])

            swap_mat[[idx_1, idx_2]] = swap_mat[[idx_2, idx_1]]
            places = np.matmul(swap_mat, places)
        elif rule[0] == 'p':
            swap_mat = np.identity(n = 16)

            targets = rule[1:].split('/')
            idx_1 = ord(targets[0]) - ord('a')
            idx_2 = ord(targets[1]) - ord('a')

            swap_mat[:,[idx_1, idx_2]] = swap_mat[:,[idx_2, idx_1]]
            places = np.matmul(places, swap_mat)

    char_vec = np.transpose(np.array(range(16)))
    exchange = np.matmul(places , char_vec)
    sol = ''.join(chr(int(i)+ord('a')) for i in exchange)
    puzzle.answer_a = sol
    print(sol)

def part_b():
    data = puzzle.input_data
    rules = data.split(',')
    
    one_l_mult = np.identity(n = 16)
    one_r_mult = np.identity(n = 16)

    shift = np.zeros((16,16))
    for idx in range(16):
        shift[idx, (idx-1)%16] = 1
    for rule in rules:
        if rule[0] == 's':
            shift_by = int(rule[1:])
            one_l_mult = np.matmul(np.linalg.matrix_power(shift, shift_by), one_l_mult)
        elif rule[0] == 'x':
            swap_mat = np.identity(n = 16)

            targets = rule[1:].split('/')
            idx_1 = int(targets[0])
            idx_2 = int(targets[1])

            swap_mat[[idx_1, idx_2]] = swap_mat[[idx_2, idx_1]]
            one_l_mult = np.matmul(swap_mat, one_l_mult)
        elif rule[0] == 'p':
            swap_mat = np.identity(n = 16)

            targets = rule[1:].split('/')
            idx_1 = ord(targets[0]) - ord('a')
            idx_2 = ord(targets[1]) - ord('a')

            swap_mat[:,[idx_1, idx_2]] = swap_mat[:,[idx_2, idx_1]]
            one_r_mult = np.matmul(one_r_mult, swap_mat)

    thousand_l = np.linalg.matrix_power(one_l_mult, 1000)
    million_l = np.linalg.matrix_power(thousand_l, 1000)
    billion_l = np.linalg.matrix_power(million_l, 1000)

    thousand_r = np.linalg.matrix_power(one_r_mult, 1000)
    million_r = np.linalg.matrix_power(thousand_r, 1000)
    billion_r = np.linalg.matrix_power(million_r, 1000)

    total_move = np.matmul(billion_l, billion_r)

    char_vec = np.transpose(np.array(range(16)))
    exchange = np.matmul(total_move , char_vec)
    sol = ''.join(chr(int(i)+ord('a')) for i in exchange)
    puzzle.answer_b = sol
    print(sol)

part_a()
part_b()